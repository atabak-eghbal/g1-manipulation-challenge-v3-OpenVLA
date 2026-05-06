#!/usr/bin/env python3
"""Replay a recorded VLA-style FSM demonstration through the G1 action adapter.

Step 15:
- load demo.jsonl
- replay action_7d through G1VLAActionAdapter
- do not use FSM target lookups
- do not load OpenVLA

Step 16 additions:
- teacher-command mode: replay recorded teacher walk/reach/grip directly
- hybrid-7d mode: teacher walk_cmd + adapter manipulation
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
from common.scene import reset_robot
from policies.base import PolicyOutput
from vla_bridge.action_adapter import G1VLAActionAdapter
from vla_bridge.demo_schema import read_jsonl
from vla_bridge.replay_metrics import compute_replay_metrics


# ---------------------------------------------------------------------------
# Armature helper (same pattern as record_vla_demo.py)
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

def policy_output_to_controller(ctrl: WalkerReacherController, out) -> None:
    ctrl.lin_vel_x, ctrl.lin_vel_y, ctrl.ang_vel_z = out.walk_cmd
    ctrl.reach_target[:] = np.asarray(out.reach_target, dtype=np.float32)
    ctrl.reach_active = bool(out.reach_active)
    ctrl.grip_closed = bool(out.grip_closed)


def write_summary(path: Path, summary: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replay a recorded VLA-style FSM demonstration through the G1 action adapter."
    )
    parser.add_argument("metadata", type=Path, help="Path to demo.jsonl")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/vla_replays/replay_000"),
        help="Directory for replay outputs",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        default=0,
        help="Maximum steps to replay (0 = all)",
    )
    parser.add_argument(
        "--mode",
        choices=["arm-only", "teacher-command", "hybrid-7d"],
        default="arm-only",
        help=(
            "Replay mode: arm-only (adapter, walk=(0,0,0)), "
            "teacher-command (recorded teacher fields), "
            "hybrid-7d (teacher walk_cmd + adapter manipulation)"
        ),
    )
    parser.add_argument(
        "--init-current-palm",
        action="store_true",
        help="Initialise adapter from current sim palm instead of first recorded palm",
    )
    parser.add_argument(
        "--decimation",
        type=int,
        default=4,
        help="Physics steps per control tick",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    args = parse_args()

    if args.decimation <= 0:
        raise ValueError("--decimation must be positive")

    # --- Load demo steps ---
    steps = read_jsonl(args.metadata)
    if not steps:
        raise RuntimeError(f"No steps found in {args.metadata}")
    if args.max_steps > 0:
        steps = steps[: args.max_steps]

    # --- Load config and model (same pattern as record_vla_demo.py) ---
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

    # --- Build controller and grasp backend ---
    ctrl = WalkerReacherController(
        model, data, walker, croucher, rotator, config, right_reacher=right_reacher
    )
    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = KinematicAttachment(
        model, data, ctrl.right_palm_site_id, rb_body_id
    )

    # --- Build VLA adapter ---
    if args.init_current_palm:
        initial_palm_world = data.site_xpos[ctrl.right_palm_site_id].copy()
    else:
        initial_palm_world = np.asarray(steps[0].palm_world, dtype=np.float64)
    adapter = G1VLAActionAdapter(initial_palm_world=initial_palm_world)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    replay_palm: list[np.ndarray] = []
    replay_grip: list[bool] = []
    replay_attached: list[bool] = []

    print("[replay_vla_demo] Starting replay")
    print(f"[replay_vla_demo] metadata : {args.metadata}")
    print(f"[replay_vla_demo] output_dir: {args.output_dir}")
    print(f"[replay_vla_demo] mode      : {args.mode}")
    print(f"[replay_vla_demo] steps     : {len(steps)}")

    attached = False
    for i, step in enumerate(steps):
        pelvis_pos = data.qpos[:3].copy()
        pelvis_quat = data.qpos[3:7].copy()
        current_palm = data.site_xpos[ctrl.right_palm_site_id].copy()

        if args.mode == "arm-only":
            out = adapter.step(
                np.asarray(step.action_7d, dtype=np.float64),
                pelvis_pos=pelvis_pos,
                pelvis_quat=pelvis_quat,
                current_palm_world=current_palm,
                walk_cmd=(0.0, 0.0, 0.0),
            )
        elif args.mode == "teacher-command":
            out = PolicyOutput(
                walk_cmd=tuple(float(x) for x in step.walk_cmd),
                reach_target=tuple(float(x) for x in step.reach_target_pelvis),
                reach_active=bool(step.reach_active),
                grip_closed=bool(step.grip_closed),
            )
        else:  # hybrid-7d
            out = adapter.step(
                np.asarray(step.action_7d, dtype=np.float64),
                pelvis_pos=pelvis_pos,
                pelvis_quat=pelvis_quat,
                current_palm_world=current_palm,
                walk_cmd=step.walk_cmd,
            )

        policy_output_to_controller(ctrl, out)
        target_pos = ctrl.step()
        ctrl.apply_pd_control(target_pos)

        for _ in range(args.decimation):
            mujoco.mj_step(model, data)
            attached = grasp_backend.tick(ctrl.grip_closed)

        replay_palm.append(data.site_xpos[ctrl.right_palm_site_id].copy())
        replay_grip.append(bool(ctrl.grip_closed))
        replay_attached.append(bool(attached))

        if (i + 1) % 100 == 0:
            print(f"[replay_vla_demo] replayed {i + 1}/{len(steps)} steps")

    # --- Compute metrics ---
    replay_palm_arr = np.asarray(replay_palm, dtype=np.float64)
    metrics = compute_replay_metrics(steps, replay_palm_arr, replay_grip)

    summary = {
        "metadata": str(args.metadata),
        "output_dir": str(args.output_dir),
        "mode": args.mode,
        "num_steps": metrics.num_steps,
        "mean_palm_error_m": metrics.mean_palm_error_m,
        "max_palm_error_m": metrics.max_palm_error_m,
        "final_palm_error_m": metrics.final_palm_error_m,
        "mean_action_magnitude_m": metrics.mean_action_magnitude_m,
        "max_action_magnitude_m": metrics.max_action_magnitude_m,
        "grip_mismatch_count": metrics.grip_mismatch_count,
        "walk_nonzero_steps": int(sum(np.linalg.norm(s.walk_cmd) > 1e-9 for s in steps)),
        "reach_active_steps": int(sum(s.reach_active for s in steps)),
        "attached_steps": int(sum(replay_attached)),
        "ever_attached": bool(any(replay_attached)),
    }

    write_summary(args.output_dir / "replay_summary.json", summary)

    np.savez(
        args.output_dir / "replay_trace.npz",
        teacher_palm_world=np.asarray([s.palm_world for s in steps], dtype=np.float64),
        replay_palm_world=replay_palm_arr,
        teacher_grip=np.asarray([s.grip_closed for s in steps], dtype=bool),
        replay_grip=np.asarray(replay_grip, dtype=bool),
        action_7d=np.asarray([s.action_7d for s in steps], dtype=np.float64),
        attached=np.asarray(replay_attached, dtype=bool),
    )

    print("\n--- VLA Replay Summary ---")
    for key, value in summary.items():
        print(f"  {key:24s}: {value}")
    print(f"\n[replay_vla_demo] wrote {args.output_dir / 'replay_summary.json'}")
    print(f"[replay_vla_demo] wrote {args.output_dir / 'replay_trace.npz'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
