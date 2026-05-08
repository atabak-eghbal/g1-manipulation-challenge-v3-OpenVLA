#!/usr/bin/env python3
"""Record a scripted keyboard plan rollout as a VLA-style demonstration.

Step 23 / 23B:
- no FSM
- no OpenVLA inference
- drives the G1 controller from a JSON-defined scripted plan
- tracks grasp attachment and task-success metrics
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import mujoco
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from common.controller import WalkerReacherController
from common.grasp import KinematicAttachment, make_grasp_backend
from common.onnx_policy import ONNXPolicy
from common.scene import CameraRenderer, reset_robot
from vla_bridge.demo_recorder import VLADemoRecorder
from vla_bridge.scripted_keyboard import (
    ExpandedScriptedCommand,
    ScriptedKeyboardPlan,
    command_for_tick,
    load_scripted_keyboard_plan,
    plan_summary as scripted_plan_summary,
)
from vla_bridge.action_adapter import world_to_pelvis
from vla_bridge.task_success import TaskSuccessTracker

# Workspace bounds matching FSM / action adapter
_REACH_LOW  = np.array([-0.30, -0.60, -0.40], dtype=np.float32)
_REACH_HIGH = np.array([ 0.60,  0.30,  0.60], dtype=np.float32)
_RIGHT_BIAS = -0.03  # matches FSM hover/grasp bias — keeps arm on cylinder centerline

# ---------------------------------------------------------------------------
# Phase sets for grasp-assurance logic
# ---------------------------------------------------------------------------

POST_GRASP_PHASES = frozenset({
    "lift_source",
    "turn_toward_target",
    "approach_target",
    "hover_target",
    "lower_target",
    "open_grip",
    "retract",
})


# ---------------------------------------------------------------------------
# Armature helper (matches record_vla_demo.py)
# ---------------------------------------------------------------------------

def _set_armature(model, joint_names: list[str]) -> None:
    ARM_5020 = 0.00360972
    ARM_7520_14 = 0.01017752
    ARM_7520_22 = 0.02510192
    ARM_4010 = 0.00425000
    ARM_2x5020 = 0.00721945
    for i, name in enumerate(joint_names):
        dof = 6 + i
        if "elbow" in name or "shoulder" in name or "wrist_roll" in name:
            model.dof_armature[dof] = ARM_5020
        elif "hip_pitch" in name or "hip_yaw" in name or name == "waist_yaw_joint":
            model.dof_armature[dof] = ARM_7520_14
        elif "hip_roll" in name or "knee" in name:
            model.dof_armature[dof] = ARM_7520_22
        elif "wrist_pitch" in name or "wrist_yaw" in name:
            model.dof_armature[dof] = ARM_4010
        elif "ankle" in name or name in ("waist_pitch_joint", "waist_roll_joint"):
            model.dof_armature[dof] = ARM_2x5020
        else:
            model.dof_armature[dof] = ARM_5020


# ---------------------------------------------------------------------------
# MuJoCo scene helpers
# ---------------------------------------------------------------------------

def _is_grasp_attached(grasp_backend) -> bool:
    for attr in ("attached", "is_attached", "object_attached"):
        if hasattr(grasp_backend, attr):
            val = getattr(grasp_backend, attr)
            return bool(val() if callable(val) else val)
    return False


def _body_world_pos(model, data, body_name: str) -> list[float]:
    body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, body_name)
    if body_id < 0:
        raise RuntimeError(f"body not found: {body_name}")
    return [float(x) for x in data.xpos[body_id]]


def _geom_surface_z(model, data, geom_name: str, fallback_body: str = "") -> float:
    """Return world Z of a geom's top surface (centre + half-height)."""
    geom_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, geom_name)
    if geom_id >= 0:
        return float(data.geom_xpos[geom_id][2] + model.geom_size[geom_id][2])
    if fallback_body:
        body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, fallback_body)
        if body_id >= 0:
            return float(data.xpos[body_id][2]) + 0.02
    return 0.75  # reasonable fallback


def apply_red_block_xy_offset(model, data, dx: float, dy: float) -> dict[str, Any]:
    body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    if body_id < 0:
        raise RuntimeError("red_block body not found")
    joint_id = int(model.body_jntadr[body_id])
    if joint_id < 0:
        raise RuntimeError("red_block has no joint to perturb")
    qposadr = int(model.jnt_qposadr[joint_id])
    before = data.qpos[qposadr:qposadr + 3].copy()
    data.qpos[qposadr + 0] += float(dx)
    data.qpos[qposadr + 1] += float(dy)
    mujoco.mj_forward(model, data)
    after = data.qpos[qposadr:qposadr + 3].copy()
    return {
        "red_block_body_id": int(body_id),
        "red_block_qposadr": int(qposadr),
        "red_block_pos_before": [float(x) for x in before],
        "red_block_pos_after": [float(x) for x in after],
        "red_block_xy_offset_m": [float(dx), float(dy)],
    }


# ---------------------------------------------------------------------------
# Controller helpers
# ---------------------------------------------------------------------------

def _world_reach_to_pelvis(data, world_target) -> np.ndarray:
    """Convert a world-frame reach target to clipped pelvis-frame, with right-arm bias."""
    pelvis_pos  = np.array(data.qpos[:3], dtype=np.float64)
    pelvis_quat = np.array(data.qpos[3:7], dtype=np.float64)
    reach_p = world_to_pelvis(pelvis_pos, pelvis_quat, np.asarray(world_target, dtype=np.float64))
    reach_p[1] = min(float(reach_p[1]), _RIGHT_BIAS)
    return np.clip(reach_p, _REACH_LOW, _REACH_HIGH).astype(np.float32)


def _policy_output_to_controller(
    ctrl: WalkerReacherController,
    cmd: ExpandedScriptedCommand,
    *,
    use_world_frame: bool = False,
    data=None,
) -> None:
    ctrl.lin_vel_x, ctrl.lin_vel_y, ctrl.ang_vel_z = cmd.walk_cmd
    if not cmd.reach_active:
        ctrl.reach_target[:] = np.array([0.30, -0.20, 0.20], dtype=np.float32)
    elif use_world_frame and data is not None:
        ctrl.reach_target[:] = _world_reach_to_pelvis(data, cmd.reach_target)
    else:
        ctrl.reach_target[:] = np.asarray(cmd.reach_target, dtype=np.float32)
    ctrl.reach_active = cmd.reach_active

    if cmd.grip_fraction is not None:
        # Continuous grip: set fraction override (and optionally speed).
        ctrl.set_grip_fraction(cmd.grip_fraction, close_speed=cmd.grip_close_speed)
        # Keep grip_closed in sync for grasp-backend tick() compatibility.
        ctrl.grip_closed = float(cmd.grip_fraction) >= 0.5
    else:
        ctrl.clear_grip_fraction_override()
        ctrl.grip_closed = cmd.grip_closed
        if cmd.grip_close_speed is not None:
            ctrl.grip_close_speed = float(cmd.grip_close_speed)


# ---------------------------------------------------------------------------
# Object-motion tracker
# ---------------------------------------------------------------------------

def _xy_dist(a: list[float], b: list[float]) -> float:
    return float(np.linalg.norm(np.asarray(a[:2]) - np.asarray(b[:2])))


class ObjectMotionTracker:
    """Tracks red_block world position over a rollout."""

    def __init__(self, initial_pos: list[float]) -> None:
        self._init = list(initial_pos)
        self._max_z = float(initial_pos[2])
        self._min_z = float(initial_pos[2])
        self._max_xy_disp = 0.0
        self._final: list[float] = list(initial_pos)

    def update(self, pos: list[float]) -> None:
        self._final = list(pos)
        if pos[2] > self._max_z:
            self._max_z = float(pos[2])
        if pos[2] < self._min_z:
            self._min_z = float(pos[2])
        d = _xy_dist(pos, self._init)
        if d > self._max_xy_disp:
            self._max_xy_disp = d

    def summary(self) -> dict[str, Any]:
        lift = self._max_z - self._init[2]
        final_xy_disp = _xy_dist(self._final, self._init)
        # Heuristic: object was knocked/pushed significantly but not lifted.
        knocked = (
            (self._max_xy_disp > 0.15 and lift < 0.03)
            or (self._final[2] < self._init[2] - 0.05)
        )
        return {
            "initial_red_block_world": self._init,
            "final_red_block_world": self._final,
            "max_red_block_z": round(self._max_z, 6),
            "min_red_block_z": round(self._min_z, 6),
            "final_xy_displacement_from_initial": round(final_xy_disp, 6),
            "max_xy_displacement_from_initial": round(self._max_xy_disp, 6),
            "lift_height_from_initial": round(lift, 6),
            "possible_knockover_or_push": bool(knocked),
        }


# ---------------------------------------------------------------------------
# Summary builder
# ---------------------------------------------------------------------------

def _build_summary(
    *,
    recorder: VLADemoRecorder,
    scripted_plan: ScriptedKeyboardPlan,
    script_config: Path,
    task_metrics: dict[str, Any],
    require_attachment: bool,
    attachment_timeout_ticks: int,
    stop_on_failure: bool,
    stopped_early: bool,
    stop_reason: str,
    scenario_id: str,
    seed: int | None,
    red_block_xy_offset: tuple[float, float],
    grasp_backend=None,
    object_motion: dict[str, Any] | None = None,
    grip_fraction_stats: dict[str, Any] | None = None,
) -> dict[str, Any]:
    steps = recorder.steps
    base: dict[str, Any] = {
        "teacher_type": "scripted_keyboard",
        "script_name": scripted_plan.name,
        "script_config": str(script_config),
        "num_steps": len(steps),
        "num_frames": int(sum(1 for s in steps if s.image_path)),
        "scenario_id": scenario_id,
        "seed": seed,
        "red_block_xy_offset_m": list(red_block_xy_offset),
        "require_attachment": require_attachment,
        "attachment_timeout_ticks": attachment_timeout_ticks,
        "stop_on_failure": stop_on_failure,
        "stopped_early": stopped_early,
        "stop_reason": stop_reason,
    }
    if steps:
        xyz = np.array([s.action_7d[:3] for s in steps], dtype=np.float64)
        mag = np.linalg.norm(xyz, axis=1)
        phases = [s.phase for s in steps]
        base.update({
            "first_phase": phases[0],
            "last_phase": phases[-1],
            "unique_phases": sorted(set(phases)),
            "max_action_xyz_m": float(mag.max()),
            "mean_action_xyz_m": float(mag.mean()),
            "grip_closed_steps": int(sum(1 for s in steps if s.grip_closed)),
            "walk_nonzero_steps": int(sum(np.linalg.norm(s.walk_cmd) > 1e-9 for s in steps)),
            "reach_active_steps": int(sum(s.reach_active for s in steps)),
        })
    base.update(task_metrics)
    if grasp_backend is not None and hasattr(grasp_backend, "summary"):
        base["grasp_summary"] = grasp_backend.summary()
    if object_motion is not None:
        base["object_motion_summary"] = object_motion
    if grip_fraction_stats is not None:
        base.update(grip_fraction_stats)
    return base


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Record a scripted keyboard plan rollout as a VLA-style demonstration."
    )
    parser.add_argument(
        "--script-config",
        type=Path,
        default=ROOT / "configs/scripts/nominal_scripted_keyboard_v1.json",
        help="Path to the scripted keyboard plan JSON file.",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--record-every", type=int, default=1)
    parser.add_argument("--camera", default="head_cam")
    parser.add_argument("--no-images", action="store_true")
    parser.add_argument("--max-control-ticks", type=int, default=4000)
    parser.add_argument("--scenario-id", default="")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument(
        "--red-block-xy-offset",
        nargs=2, type=float, default=(0.0, 0.0), metavar=("DX", "DY"),
    )
    parser.add_argument(
        "--require-attachment",
        action="store_true",
        help="Hold close_grip if the plan exits close_grip without attaching.",
    )
    parser.add_argument(
        "--attachment-timeout-ticks",
        type=int,
        default=160,
        help="Extra ticks to hold grip during attachment check before declaring never_attached.",
    )
    parser.add_argument(
        "--stop-on-failure",
        action="store_true",
        help="Stop rollout early once a required checkpoint fails.",
    )
    parser.add_argument(
        "--grasp-backend",
        choices=["kinematic", "contact-aware-physical"],
        default="kinematic",
        help=(
            "Grasp backend to use: 'kinematic' (teleport-weld, default) or "
            "'contact-aware-physical' (observe-only contact detection)."
        ),
    )
    args = parser.parse_args()

    output_dir: Path = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Load scripted plan ---
    scripted_plan = load_scripted_keyboard_plan(args.script_config)
    script_total_ticks: int = scripted_plan_summary(scripted_plan)["total_ticks"]
    use_world_frame: bool = scripted_plan.reach_frame == "world"
    if use_world_frame:
        print(f"[record_scripted_keyboard_demo] reach_frame=world — converting per tick")

    # --- Load MuJoCo model ---
    config_path = ROOT / "model_config.json"
    with open(config_path) as f:
        config = json.load(f)
    joint_names: list[str] = config["joint_names"]

    model = mujoco.MjModel.from_xml_path(str(ROOT / "scene.xml"))
    model.opt.timestep = 0.005
    _set_armature(model, joint_names)
    data = mujoco.MjData(model)
    reset_robot(model, data, config, joint_names, reset_data=True)

    red_offset_dx = float(args.red_block_xy_offset[0])
    red_offset_dy = float(args.red_block_xy_offset[1])
    apply_red_block_xy_offset(model, data, red_offset_dx, red_offset_dy)

    # --- Table geometry (for task-success metrics) ---
    source_table_z = _geom_surface_z(model, data, "table_top", fallback_body="table")
    target_table_z = _geom_surface_z(model, data, "table_white_top", fallback_body="table_white")
    target_center_world = _body_world_pos(model, data, "table_white")

    # --- Load ONNX policies ---
    walker = ONNXPolicy(str(ROOT / "walker.onnx"))
    croucher = ONNXPolicy(str(ROOT / "croucher.onnx"))
    rotator = ONNXPolicy(str(ROOT / "rotator.onnx"))
    right_reacher = ONNXPolicy(str(ROOT / "right_reacher.onnx"))
    walker(np.zeros((1, 99), dtype=np.float32))
    croucher(np.zeros((1, 101), dtype=np.float32))
    rotator(np.zeros((1, 99), dtype=np.float32))
    right_reacher(np.zeros((1, 36), dtype=np.float32))

    # --- Build controller + grasp backend ---
    ctrl = WalkerReacherController(
        model, data, walker, croucher, rotator, config, right_reacher=right_reacher
    )
    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = make_grasp_backend(
        args.grasp_backend, model, data, ctrl.right_palm_site_id, rb_body_id
    )
    print(f"[record_scripted_keyboard_demo] grasp_backend={args.grasp_backend}")

    # --- Optional camera renderer ---
    renderer: CameraRenderer | None = None
    if not args.no_images:
        try:
            renderer = CameraRenderer(model, data)
        except Exception as exc:
            print(f"[warn] CameraRenderer unavailable ({exc}); running without images.")
            renderer = None

    # --- Recorder ---
    recorder = VLADemoRecorder(
        output_dir=output_dir,
        instruction="Pick up the red cylinder and place it on the blue table.",
        record_every=args.record_every,
        camera_name=args.camera,
    )

    # --- Task-success tracker ---
    tracker = TaskSuccessTracker(
        source_table_z=source_table_z,
        target_table_z=target_table_z,
    )

    # --- Object-motion tracker ---
    initial_rb_pos = _body_world_pos(model, data, "red_block")
    motion_tracker = ObjectMotionTracker(initial_rb_pos)

    # --- Grip-fraction stats accumulator ---
    _commanded_fractions: list[float] = []
    psum = scripted_plan_summary(scripted_plan)
    _plan_uses_continuous_grip: bool = bool(psum.get("uses_continuous_grip", False))

    # --- Grasp-assurance state ---
    saved_close_grip_cmd: ExpandedScriptedCommand | None = None
    in_attachment_hold = False
    attachment_hold_remaining = 0
    grasp_check_done = False  # prevent triggering hold more than once
    stopped_early = False
    stop_reason = ""

    decimation = 4
    target_pos = ctrl.default_joint_pos.copy()

    print(f"[record_scripted_keyboard_demo] Starting rollout for plan '{scripted_plan.name}'")
    print(f"[record_scripted_keyboard_demo] Output dir: {output_dir.resolve()}")
    print(f"[record_scripted_keyboard_demo] source_table_z={source_table_z:.4f}  target_table_z={target_table_z:.4f}")

    for tick in range(args.max_control_ticks):
        raw_cmd = command_for_tick(scripted_plan, tick)

        # Save close_grip command for potential hold override
        if raw_cmd.phase == "close_grip":
            saved_close_grip_cmd = raw_cmd

        # Determine effective command
        if in_attachment_hold:
            effective_cmd = saved_close_grip_cmd
            attachment_hold_remaining -= 1
        else:
            # Check whether to start the hold
            if (
                args.require_attachment
                and not grasp_check_done
                and not tracker.ever_attached
                and raw_cmd.phase in POST_GRASP_PHASES
                and saved_close_grip_cmd is not None
            ):
                in_attachment_hold = True
                attachment_hold_remaining = args.attachment_timeout_ticks
                grasp_check_done = True
                effective_cmd = saved_close_grip_cmd
                print(
                    f"[record_scripted_keyboard_demo] Grip hold started at tick {tick} "
                    f"(phase={raw_cmd.phase}, timeout={args.attachment_timeout_ticks})"
                )
            else:
                effective_cmd = raw_cmd

        # --- Apply command + step physics ---
        _policy_output_to_controller(ctrl, effective_cmd, use_world_frame=use_world_frame, data=data)
        target_pos = ctrl.step()
        for _ in range(decimation):
            ctrl.apply_pd_control(target_pos)
            mujoco.mj_step(model, data)
            grasp_backend.tick(ctrl.grip_closed)

        # --- Collect grip-fraction sample ---
        if effective_cmd.grip_fraction is not None:
            _commanded_fractions.append(float(effective_cmd.grip_fraction))

        # --- Update task tracker ---
        attached_now = _is_grasp_attached(grasp_backend)
        tracker.update_attachment(attached_now=attached_now, tick=tick, phase=effective_cmd.phase)
        rb_pos = _body_world_pos(model, data, "red_block")
        tracker.update_object_position(rb_pos)
        motion_tracker.update(rb_pos)

        # --- Render ---
        rgb: np.ndarray | None = None
        if renderer is not None:
            try:
                rgb = renderer.render(args.camera)
            except Exception:
                rgb = None

        # --- Record observation ---
        palm_world = data.site_xpos[ctrl.right_palm_site_id].copy()
        pelvis_pos = data.qpos[:3].copy()
        pelvis_quat = data.qpos[3:7].copy()
        recorder.observe(
            control_tick=tick,
            sim_time=float(data.time),
            rgb=rgb,
            phase=effective_cmd.phase,
            palm_world=palm_world,
            pelvis_pos=pelvis_pos,
            pelvis_quat=pelvis_quat,
            walk_cmd=effective_cmd.walk_cmd,
            reach_target_pelvis=effective_cmd.reach_target,
            reach_active=effective_cmd.reach_active,
            grip_closed=effective_cmd.grip_closed,
        )

        # --- Resolve attachment hold ---
        if in_attachment_hold:
            if tracker.ever_attached:
                in_attachment_hold = False
                print(f"[record_scripted_keyboard_demo] Attached during hold at tick {tick}.")
            elif attachment_hold_remaining <= 0:
                in_attachment_hold = False
                stopped_early = True
                stop_reason = "never_attached"
                print(
                    f"[record_scripted_keyboard_demo] Attachment hold expired at tick {tick}. "
                    f"failure_reason=never_attached"
                )
                if args.stop_on_failure:
                    print("[record_scripted_keyboard_demo] Stopping early (--stop-on-failure).")
                    break

        # --- Normal script-end condition ---
        if not in_attachment_hold and tick >= script_total_ticks - 1:
            print(f"[record_scripted_keyboard_demo] Script finished at tick {tick}.")
            break

        # --- Fall detection ---
        if float(data.qpos[2]) < 0.40:
            stopped_early = True
            stop_reason = "robot_fell"
            print(
                f"[record_scripted_keyboard_demo] Robot fell "
                f"(pelvis z={data.qpos[2]:.3f}) at tick {tick}."
            )
            break

    # --- Finalize ---
    recorder.finalize()

    # Get final positions for task metrics
    final_rb_pos = _body_world_pos(model, data, "red_block")
    final_target_center = _body_world_pos(model, data, "table_white")
    task_metrics = tracker.finalize(
        final_red_block_world=final_rb_pos,
        target_center_world=final_target_center,
        target_table_z=target_table_z,
    )

    grip_fraction_stats: dict[str, Any] = {
        "uses_continuous_grip": _plan_uses_continuous_grip,
        "min_commanded_grip_fraction": float(min(_commanded_fractions)) if _commanded_fractions else None,
        "max_commanded_grip_fraction": float(max(_commanded_fractions)) if _commanded_fractions else None,
        "mean_commanded_grip_fraction": float(np.mean(_commanded_fractions)) if _commanded_fractions else None,
        "final_grip_fraction": _commanded_fractions[-1] if _commanded_fractions else None,
        "caging_plan": "caging" in scripted_plan.name.lower(),
    }

    summary = _build_summary(
        recorder=recorder,
        scripted_plan=scripted_plan,
        script_config=args.script_config,
        task_metrics=task_metrics,
        require_attachment=args.require_attachment,
        attachment_timeout_ticks=args.attachment_timeout_ticks,
        stop_on_failure=args.stop_on_failure,
        stopped_early=stopped_early,
        stop_reason=stop_reason,
        scenario_id=args.scenario_id,
        seed=args.seed,
        red_block_xy_offset=tuple(args.red_block_xy_offset),
        grasp_backend=grasp_backend,
        object_motion=motion_tracker.summary(),
        grip_fraction_stats=grip_fraction_stats,
    )

    summary_path = output_dir / "summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("\n--- Scripted Keyboard Demo Recording Summary ---")
    print(f"  output_dir            : {output_dir.resolve()}")
    print(f"  script_name           : {summary['script_name']}")
    print(f"  teacher_type          : {summary['teacher_type']}")
    print(f"  num_steps             : {summary['num_steps']}")
    if summary.get("first_phase"):
        print(f"  first_phase           : {summary['first_phase']}")
        print(f"  last_phase            : {summary['last_phase']}")
        print(f"  grip_closed_steps     : {summary['grip_closed_steps']}")
        print(f"  walk_nonzero_steps    : {summary['walk_nonzero_steps']}")
        print(f"  reach_active_steps    : {summary['reach_active_steps']}")
    print(f"  ever_attached         : {summary['ever_attached']}")
    print(f"  object_lifted         : {summary['object_lifted']}")
    print(f"  object_on_target_table: {summary['object_on_target_table']}")
    print(f"  task_success          : {summary['task_success']}")
    print(f"  failure_reason        : {summary['failure_reason']!r}")
    print(f"  stopped_early         : {summary['stopped_early']}")
    print(f"  stop_reason           : {summary['stop_reason']!r}")
    print(f"  final_red_block_world : {summary['final_red_block_world']}")
    print(f"  final_height_above_tgt: {summary['final_height_above_target']:.4f} m")
    print(f"  final_xy_dist_to_tgt  : {summary['final_xy_distance_to_target']:.4f} m")

    if not recorder.steps:
        print("[record_scripted_keyboard_demo] ERROR: no steps were recorded.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
