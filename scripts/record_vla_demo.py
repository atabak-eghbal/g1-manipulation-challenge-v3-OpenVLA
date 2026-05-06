#!/usr/bin/env python3
"""Record an FSM teacher rollout as a VLA-style demonstration.

Step 14:
- FSM controls the robot
- recorder watches and saves images/actions
- no OpenVLA inference
- no replay

Usage:
    python scripts/record_vla_demo.py \\
        --output-dir data/vla_demos/demo_000 \\
        --max-control-ticks 4000 \\
        --record-every 5 \\
        --camera head_cam
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mujoco
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from common.controller import WalkerReacherController
from common.grasp import KinematicAttachment
from common.onnx_policy import ONNXPolicy
from common.scene import CameraRenderer, reset_robot
from policies.fsm import FSMPolicy
from policies.fsm_core import FSMState
from vla_bridge.demo_recorder import VLADemoRecorder


# ---------------------------------------------------------------------------
# Armature helper (identical to other scripts in this repo)
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

def _get_fsm_phase(policy: FSMPolicy) -> str:
    """Return the current FSM state name as a string."""
    core = getattr(policy, "_fsm", None)
    if core is None:
        core = getattr(policy, "core", None)
    if core is None:
        core = getattr(policy, "_core", None)
    state = getattr(core, "state", None)
    return getattr(state, "name", "UNKNOWN")


def _policy_output_to_controller(ctrl: WalkerReacherController, out) -> None:
    """Write FSM policy output into the controller's command fields."""
    ctrl.lin_vel_x, ctrl.lin_vel_y, ctrl.ang_vel_z = out.walk_cmd
    ctrl.reach_target[:] = np.asarray(out.reach_target, dtype=np.float32)
    ctrl.reach_active = bool(out.reach_active)
    ctrl.grip_closed = bool(out.grip_closed)


def summarize_demo(recorder: VLADemoRecorder, done_reached: bool) -> dict:
    """Build a summary dict from the finalized recorder."""
    steps = recorder.steps
    if not steps:
        return {"num_steps": 0, "done_reached": done_reached}
    xyz = np.array([s.action_7d[:3] for s in steps], dtype=np.float64)
    mag = np.linalg.norm(xyz, axis=1)
    phases = [s.phase for s in steps]
    return {
        "num_steps": len(steps),
        "done_reached": bool(done_reached),
        "first_phase": phases[0],
        "last_phase": phases[-1],
        "unique_phases": sorted(set(phases)),
        "max_action_xyz_m": float(mag.max()) if len(mag) else 0.0,
        "mean_action_xyz_m": float(mag.mean()) if len(mag) else 0.0,
        "grip_closed_steps": int(sum(1 for s in steps if s.grip_closed)),
        "walk_nonzero_steps": int(sum(np.linalg.norm(s.walk_cmd) > 1e-9 for s in steps)),
        "reach_active_steps": int(sum(s.reach_active for s in steps)),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Record an FSM teacher rollout as a VLA-style demonstration."
    )
    parser.add_argument(
        "--output-dir",
        default="data/vla_demos/demo_000",
        help="Directory for frames and demo.jsonl",
    )
    parser.add_argument(
        "--max-control-ticks",
        type=int,
        default=4000,
        help="Maximum number of control ticks to run",
    )
    parser.add_argument(
        "--record-every",
        type=int,
        default=5,
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
        "--instruction",
        default="Pick up the red cylinder and place it on the blue table.",
        help="Language instruction to embed in the demonstration metadata",
    )
    parser.add_argument(
        "--done-extra-ticks",
        type=int,
        default=100,
        help="Continue recording this many ticks after FSM reaches DONE",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)

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

    # --- Build controller, grasp backend, FSM policy ---
    ctrl = WalkerReacherController(
        model, data, walker, croucher, rotator, config, right_reacher=right_reacher
    )
    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = KinematicAttachment(
        model, data, ctrl.right_palm_site_id, rb_body_id
    )
    policy = FSMPolicy(ctrl, grasp_backend=grasp_backend)

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
        instruction=args.instruction,
        record_every=args.record_every,
        camera_name=args.camera,
    )

    decimation = 4
    done_reached = False
    done_tick: int | None = None
    target_pos = ctrl.default_joint_pos.copy()

    print(f"[record_vla_demo] Starting FSM rollout (max {args.max_control_ticks} ticks)")
    print(f"[record_vla_demo] Output dir: {output_dir.resolve()}")

    for tick in range(args.max_control_ticks):
        # --- FSM step ---
        out = policy.step()
        _policy_output_to_controller(ctrl, out)
        target_pos = ctrl.step()

        # --- Physics ---
        for _ in range(decimation):
            ctrl.apply_pd_control(target_pos)
            mujoco.mj_step(model, data)
            grasp_backend.tick(ctrl.grip_closed)

        # --- Render ---
        rgb: np.ndarray | None = None
        if renderer is not None:
            try:
                rgb = renderer.render(args.camera)
            except Exception:
                rgb = None

        # --- Observe ---
        phase = _get_fsm_phase(policy)
        palm_world = data.site_xpos[ctrl.right_palm_site_id].copy()
        pelvis_pos = data.qpos[:3].copy()
        pelvis_quat = data.qpos[3:7].copy()
        reach_target_pelvis = tuple(float(v) for v in ctrl.reach_target[:3])

        recorder.observe(
            control_tick=tick,
            sim_time=float(data.time),
            rgb=rgb,
            phase=phase,
            palm_world=palm_world,
            pelvis_pos=pelvis_pos,
            pelvis_quat=pelvis_quat,
            walk_cmd=out.walk_cmd,
            reach_target_pelvis=tuple(float(v) for v in out.reach_target),
            reach_active=bool(out.reach_active),
            grip_closed=bool(out.grip_closed),
        )

        # --- DONE detection ---
        if phase == FSMState.DONE.name:
            if not done_reached:
                done_reached = True
                done_tick = tick
                print(f"[record_vla_demo] FSM reached DONE at tick {tick}")
            if done_tick is not None and tick >= done_tick + args.done_extra_ticks:
                print(f"[record_vla_demo] Settle window complete; stopping.")
                break

        # --- Fall detection ---
        if float(data.qpos[2]) < 0.40:
            print(f"[record_vla_demo] Robot fell (pelvis z={data.qpos[2]:.3f}) at tick {tick}")
            break

    # --- Finalize ---
    recorder.finalize()

    summary = summarize_demo(recorder, done_reached)
    summary_path = output_dir / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("\n--- VLA Demo Recording Summary ---")
    print(f"  output_dir    : {output_dir.resolve()}")
    print(f"  metadata_path : {recorder.metadata_path.resolve()}")
    print(f"  num_steps     : {summary.get('num_steps', 0)}")
    if summary.get("num_steps", 0):
        num_frames = sum(
            1 for s in recorder.steps if s.image_path
        )
        print(f"  num_frames    : {num_frames}")
        print(f"  first_phase   : {summary['first_phase']}")
        print(f"  last_phase    : {summary['last_phase']}")
        print(f"  unique_phases : {summary['unique_phases']}")
        print(f"  max_action_m  : {summary['max_action_xyz_m']:.6f}")
        print(f"  grip_closed   : {summary['grip_closed_steps']}")
        print(f"  walk_nonzero  : {summary['walk_nonzero_steps']}")
        print(f"  reach_active  : {summary['reach_active_steps']}")
    print(f"  done_reached  : {done_reached}")

    if not recorder.steps:
        print("[record_vla_demo] ERROR: no steps were recorded.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
