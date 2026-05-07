#!/usr/bin/env python3
"""Record a scripted keyboard plan rollout as a VLA-style demonstration.

Step 23:
- no FSM
- no OpenVLA inference
- no replay
- drives the G1 controller from a JSON-defined scripted plan
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
from common.grasp import KinematicAttachment
from common.onnx_policy import ONNXPolicy
from common.scene import CameraRenderer, reset_robot
from vla_bridge.demo_recorder import VLADemoRecorder
from vla_bridge.scripted_keyboard import (
    command_for_tick,
    load_scripted_keyboard_plan,
    plan_summary as scripted_plan_summary,
    ScriptedKeyboardPlan,
)


# ---------------------------------------------------------------------------
# Armature helper (copied from record_vla_demo.py)
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
# Helpers
# ---------------------------------------------------------------------------

def _policy_output_to_controller(ctrl: WalkerReacherController, cmd) -> None:
    """Write scripted command into the controller's command fields."""
    ctrl.lin_vel_x, ctrl.lin_vel_y, ctrl.ang_vel_z = cmd.walk_cmd
    ctrl.reach_target[:] = np.asarray(cmd.reach_target, dtype=np.float32)
    ctrl.reach_active = cmd.reach_active
    ctrl.grip_closed = cmd.grip_closed


def summarize_demo(recorder: VLADemoRecorder, scripted_plan: ScriptedKeyboardPlan, ever_attached: bool, scenario_id: str, seed: int | None, red_block_xy_offset: tuple[float, float]) -> dict:
    """Build a summary dict from the finalized recorder."""
    steps = recorder.steps
    if not steps:
        return {
            "num_steps": 0,
            "script_name": scripted_plan.name,
            "teacher_type": scripted_plan.teacher_type,
            "ever_attached": ever_attached,
            "scenario_id": scenario_id,
            "seed": seed,
            "red_block_xy_offset_m": red_block_xy_offset,
        }
    
    xyz = np.array([s.action_7d[:3] for s in steps], dtype=np.float64)
    mag = np.linalg.norm(xyz, axis=1)
    phases = [s.phase for s in steps]
    
    return {
        "num_steps": len(steps),
        "num_frames": int(sum(1 for s in steps if s.image_path)),
        "script_name": scripted_plan.name,
        "teacher_type": scripted_plan.teacher_type,
        "first_phase": phases[0],
        "last_phase": phases[-1],
        "unique_phases": sorted(set(phases)),
        "max_action_xyz_m": float(mag.max()) if len(mag) else 0.0,
        "mean_action_xyz_m": float(mag.mean()) if len(mag) else 0.0,
        "grip_closed_steps": int(sum(1 for s in steps if s.grip_closed)),
        "walk_nonzero_steps": int(sum(np.linalg.norm(s.walk_cmd) > 1e-9 for s in steps)),
        "reach_active_steps": int(sum(s.reach_active for s in steps)),
        "ever_attached": ever_attached,
        "scenario_id": scenario_id,
        "seed": seed,
        "red_block_xy_offset_m": red_block_xy_offset,
    }


def apply_red_block_xy_offset(model, data, dx: float, dy: float) -> dict[str, Any]:
    """Apply a small x/y offset to the red_block freejoint qpos.

    Returns metadata with before/after positions.
    """
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
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory for frames and demo.jsonl",
    )
    parser.add_argument(
        "--record-every",
        type=int,
        default=1,
        help="Record one observation every N control ticks",
    )
    parser.add_argument(
        "--camera",
        default="head_cam",
        help="Camera name to render from",
    )
    parser.add_argument(
        "--no-images",
        action="store_true",
        help="Skip camera rendering (saves time in headless runs)",
    )
    parser.add_argument(
        "--max-control-ticks",
        type=int,
        default=4000,
        help="Maximum number of control ticks to run",
    )
    parser.add_argument("--scenario-id", default="", help="Scenario identifier stored in demo metadata.")
    parser.add_argument("--seed", type=int, default=None, help="Scenario seed stored in demo metadata.")
    parser.add_argument(
        "--red-block-xy-offset",
        nargs=2,
        type=float,
        default=(0.0, 0.0),
        metavar=("DX", "DY"),
        help="Small x/y offset in meters applied to the red_block initial pose before recording.",
    )
    args = parser.parse_args()

    output_dir = args.output_dir

    # --- Load scripted plan ---
    scripted_plan = load_scripted_keyboard_plan(args.script_config)
    script_total_ticks = scripted_plan_summary(scripted_plan)["total_ticks"]

    # --- Load config and model ---
    config_path = ROOT / "model_config.json"
    with open(config_path) as f:
        config = json.load(f)
    joint_names: list[str] = config["joint_names"]

    model = mujoco.MjModel.from_xml_path(str(ROOT / "scene.xml"))
    model.opt.timestep = 0.005
    _set_armature(model, joint_names)
    data = mujoco.MjData(model)
    reset_robot(model, data, config, joint_names, reset_data=True)
    
    red_offset_dx, red_offset_dy = float(args.red_block_xy_offset[0]), float(args.red_block_xy_offset[1])
    _ = apply_red_block_xy_offset(model, data, red_offset_dx, red_offset_dy) # Apply offset, ignore metadata for now.

    # --- Load ONNX policies ---
    walker = ONNXPolicy(str(ROOT / "walker.onnx"))
    croucher = ONNXPolicy(str(ROOT / "croucher.onnx"))
    rotator = ONNXPolicy(str(ROOT / "rotator.onnx"))
    right_reacher = ONNXPolicy(str(ROOT / "right_reacher.onnx"))

    # Warm up ONNX runtimes
    walker(np.zeros((1, 99), dtype=np.float32))
    croucher(np.zeros((1, 101), dtype=np.float32))
    rotator(np.zeros((1, 99), dtype=np.float32))
    right_reacher(np.zeros((1, 36), dtype=np.float32))

    # --- Build controller, grasp backend ---
    ctrl = WalkerReacherController(
        model, data, walker, croucher, rotator, config, right_reacher=right_reacher
    )
    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = KinematicAttachment(
        model, data, ctrl.right_palm_site_id, rb_body_id
    )

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

    decimation = 4
    ever_attached = False
    target_pos = ctrl.default_joint_pos.copy()

    print(f"[record_scripted_keyboard_demo] Starting rollout for plan '{scripted_plan.name}'")
    print(f"[record_scripted_keyboard_demo] Output dir: {output_dir.resolve()}")

    for tick in range(args.max_control_ticks):
        # --- Get scripted command ---
        cmd = command_for_tick(scripted_plan, tick)
        _policy_output_to_controller(ctrl, cmd)
        target_pos = ctrl.step()

        # --- Physics ---
        for _ in range(decimation):
            ctrl.apply_pd_control(target_pos)
            mujoco.mj_step(model, data)
            grasp_backend.tick(ctrl.grip_closed)
        
        if grasp_backend.attached:
            ever_attached = True

        # --- Render ---
        rgb: np.ndarray | None = None
        if renderer is not None:
            try:
                rgb = renderer.render(args.camera)
            except Exception:
                rgb = None

        # --- Observe ---
        palm_world = data.site_xpos[ctrl.right_palm_site_id].copy()
        pelvis_pos = data.qpos[:3].copy()
        pelvis_quat = data.qpos[3:7].copy()
        
        recorder.observe(
            control_tick=tick,
            sim_time=float(data.time),
            rgb=rgb,
            phase=cmd.phase, # Use step name as phase
            palm_world=palm_world,
            pelvis_pos=pelvis_pos,
            pelvis_quat=pelvis_quat,
            walk_cmd=cmd.walk_cmd,
            reach_target_pelvis=cmd.reach_target,
            reach_active=cmd.reach_active,
            grip_closed=cmd.grip_closed,
        )

        # --- Stop condition ---
        if tick >= script_total_ticks -1: # stop after last command in script
            print(f"[record_scripted_keyboard_demo] Script finished at tick {tick}")
            break
        
        # --- Fall detection ---
        if float(data.qpos[2]) < 0.40:
            print(f"[record_scripted_keyboard_demo] Robot fell (pelvis z={data.qpos[2]:.3f}) at tick {tick}")
            break

    # --- Finalize ---
    recorder.finalize()

    summary = summarize_demo(
        recorder,
        scripted_plan,
        ever_attached,
        args.scenario_id,
        args.seed,
        args.red_block_xy_offset,
    )
    summary_path = output_dir / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("\n--- Scripted Keyboard Demo Recording Summary ---")
    print(f"  output_dir            : {output_dir.resolve()}")
    print(f"  metadata_path         : {recorder.metadata_path.resolve()}")
    print(f"  script_name           : {summary['script_name']}")
    print(f"  teacher_type          : {summary['teacher_type']}")
    print(f"  num_steps             : {summary.get('num_steps', 0)}")
    if summary.get("num_steps", 0):
        print(f"  num_frames            : {summary['num_frames']}")
        print(f"  first_phase           : {summary['first_phase']}")
        print(f"  last_phase            : {summary['last_phase']}")
        print(f"  unique_phases         : {summary['unique_phases']}")
        print(f"  max_action_m          : {summary['max_action_xyz_m']:.6f}")
        print(f"  grip_closed_steps     : {summary['grip_closed_steps']}")
        print(f"  walk_nonzero_steps    : {summary['walk_nonzero_steps']}")
        print(f"  reach_active_steps    : {summary['reach_active_steps']}")
    print(f"  ever_attached         : {summary['ever_attached']}")
    print(f"  scenario_id           : {summary['scenario_id']}")
    print(f"  seed                  : {summary['seed']}")
    print(f"  red_block_xy_offset_m : {summary['red_block_xy_offset_m']}")

    if not recorder.steps:
        print("[record_scripted_keyboard_demo] ERROR: no steps were recorded.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())