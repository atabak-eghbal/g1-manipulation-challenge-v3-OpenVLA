#!/usr/bin/env python3
"""Headless integration test for ContactGuidedGraspPolicy.

Runs the full FSMCore approach + staged-cage probe pipeline without a GUI.
Reports key metrics after each run so we can iterate without opening a viewer.

Usage:
    python scripts/test_contact_guided_grasp.py
    python scripts/test_contact_guided_grasp.py --grasp-backend kinematic
    python scripts/test_contact_guided_grasp.py --grasp-backend contact-aware-physical
    python scripts/test_contact_guided_grasp.py --max-ticks 3000
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
from common.grasp import KinematicAttachment, HybridGraspBackend, make_grasp_backend
from common.onnx_policy import ONNXPolicy
from common.scene import reset_robot
from policies.base import PolicyOutput
from policies.fsm_core import FSMCore, FSMState
from vla_bridge.action_adapter import world_to_pelvis

# Must import ContactGuidedGraspPolicy from run.py
import importlib.util, types

_run_spec = importlib.util.spec_from_file_location("run", ROOT / "run.py")
_run_mod  = importlib.util.module_from_spec(_run_spec)
# Patch sys.modules so run.py's own imports work
sys.modules["run"] = _run_mod
_run_spec.loader.exec_module(_run_mod)
ContactGuidedGraspPolicy = _run_mod.ContactGuidedGraspPolicy


def set_armature(model, joint_names):
    ARM_5020    = 0.00360972
    ARM_7520_14 = 0.01017752
    ARM_7520_22 = 0.02510192
    ARM_4010    = 0.00425000
    ARM_2x5020  = 0.00721945
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--grasp-backend", default="kinematic",
                        choices=["kinematic", "contact-aware-physical"])
    parser.add_argument("--max-ticks", type=int, default=4000)
    parser.add_argument("--report-every", type=int, default=200,
                        help="Print progress every N control ticks")
    args = parser.parse_args()

    config_path = ROOT / "model_config.json"
    with open(config_path) as f:
        config = json.load(f)
    joint_names = config["joint_names"]

    model = mujoco.MjModel.from_xml_path(str(ROOT / "scene.xml"))
    model.opt.timestep = 0.005
    set_armature(model, joint_names)
    data = mujoco.MjData(model)
    reset_robot(model, data, config, joint_names, reset_data=False)

    walker        = ONNXPolicy(str(ROOT / "walker.onnx"))
    croucher      = ONNXPolicy(str(ROOT / "croucher.onnx"))
    rotator       = ONNXPolicy(str(ROOT / "rotator.onnx"))
    right_reacher = ONNXPolicy(str(ROOT / "right_reacher.onnx"))

    ctrl = WalkerReacherController(model, data, walker, croucher, rotator,
                                   config, right_reacher=right_reacher)

    # Warm-up
    walker(np.zeros((1, 99), dtype=np.float32))
    croucher(np.zeros((1, 101), dtype=np.float32))
    rotator(np.zeros((1, 99), dtype=np.float32))
    right_reacher(np.zeros((1, 36), dtype=np.float32))

    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    # contact-aware-physical uses a HybridGraspBackend: physical contact detection
    # for cage confirmation, then kinematic attachment for reliable transport.
    if args.grasp_backend == "contact-aware-physical":
        grasp_backend = HybridGraspBackend(model, data, ctrl.right_palm_site_id, rb_body_id)
    else:
        grasp_backend = make_grasp_backend(args.grasp_backend, model, data,
                                           ctrl.right_palm_site_id, rb_body_id)
    policy = ContactGuidedGraspPolicy(ctrl, grasp_backend, rb_body_id)

    decimation = 4
    target_pos = ctrl.default_joint_pos.copy()
    initial_cyl_z = float(data.xpos[rb_body_id][2])

    print(f"\n=== ContactGuidedGraspPolicy headless test ===")
    print(f"  grasp_backend  : {args.grasp_backend}")
    print(f"  max_ticks      : {args.max_ticks}")
    print(f"  initial_cyl_z  : {initial_cyl_z:.4f} m\n")

    prev_fsm_state = None
    probe_start_tick = None
    max_cyl_z = initial_cyl_z

    for tick in range(args.max_ticks):
        out = policy.step()

        # Write commands to controller
        ctrl.lin_vel_x, ctrl.lin_vel_y, ctrl.ang_vel_z = out.walk_cmd
        ctrl.reach_target[:] = out.reach_target
        ctrl.reach_active    = out.reach_active
        ctrl.grip_closed     = out.grip_closed

        target_pos = ctrl.step()
        for _ in range(decimation):
            ctrl.apply_pd_control(target_pos)
            mujoco.mj_step(model, data)
            grasp_backend.tick(ctrl.grip_closed)

        cyl_z     = float(data.xpos[rb_body_id][2])
        max_cyl_z = max(max_cyl_z, cyl_z)
        palm_world = data.site_xpos[ctrl.right_palm_site_id].copy()
        block_world = data.xpos[rb_body_id].copy()
        palm_lat = float(np.linalg.norm(block_world[:2] - palm_world[:2]))

        fsm_state = policy._fsm.state
        if fsm_state != prev_fsm_state:
            print(f"  tick={tick:>5}  FSM: {prev_fsm_state.name if prev_fsm_state else 'START'}"
                  f" → {fsm_state.name}  "
                  f"cyl_z={cyl_z:.4f}  palm_lat={palm_lat*100:.1f}cm")
            prev_fsm_state = fsm_state
            if fsm_state == FSMState.CLOSE_GRIP:
                probe_start_tick = tick

        if tick % args.report_every == 0 and tick > 0:
            attached = getattr(grasp_backend, "attached", False)
            print(f"  tick={tick:>5}  state={fsm_state.name:<20}  "
                  f"cyl_z={cyl_z:.4f}  lift={cyl_z-initial_cyl_z:+.4f}  "
                  f"palm_lat={palm_lat*100:.1f}cm  "
                  f"attached={attached}  probe={policy._probe_active}")

        # Fall detection
        if float(data.qpos[2]) < 0.40:
            print(f"\nFAIL — robot fell at tick {tick}")
            _final_report(tick, policy, grasp_backend, data, rb_body_id, ctrl,
                          initial_cyl_z, max_cyl_z, probe_start_tick)
            sys.exit(1)

        if policy.done:
            print(f"\nDONE reached at tick {tick}")
            _final_report(tick, policy, grasp_backend, data, rb_body_id, ctrl,
                          initial_cyl_z, max_cyl_z, probe_start_tick)
            attached = getattr(grasp_backend, "attached", False)
            cyl_on_tgt = _cyl_on_target(policy._fsm, data, rb_body_id)
            print(f"\n{'PASS' if cyl_on_tgt else 'PARTIAL'} — "
                  f"attached={attached}  cyl_on_target={cyl_on_tgt}")
            sys.exit(0 if cyl_on_tgt else 2)

    # Timeout
    attached = getattr(grasp_backend, "attached", False)
    print(f"\nTIMEOUT after {args.max_ticks} ticks")
    _final_report(args.max_ticks, policy, grasp_backend, data, rb_body_id, ctrl,
                  initial_cyl_z, max_cyl_z, probe_start_tick)
    sys.exit(3)


def _final_report(tick, policy, grasp_backend, data, rb_body_id, ctrl,
                  initial_cyl_z, max_cyl_z, probe_start_tick):
    cyl_world  = data.xpos[rb_body_id].copy()
    palm_world = data.site_xpos[ctrl.right_palm_site_id].copy()
    palm_lat   = float(np.linalg.norm(cyl_world[:2] - palm_world[:2]))
    attached   = getattr(grasp_backend, "attached", False)
    lift       = max_cyl_z - initial_cyl_z
    probe_dur  = (tick - probe_start_tick) if probe_start_tick is not None else 0
    print(f"\n--- Final report (tick {tick}) ---")
    print(f"  FSM state       : {policy._fsm.state.name}")
    print(f"  probe_active    : {policy._probe_active}")
    print(f"  grip_triggered  : {policy._grip_triggered}")
    print(f"  caging          : {policy._caging}  stage={policy._cage_stage}")
    print(f"  attached        : {attached}")
    print(f"  palm_lateral    : {palm_lat*100:.2f} cm")
    print(f"  cyl_z_current   : {cyl_world[2]:.4f}")
    print(f"  max_cyl_z       : {max_cyl_z:.4f}  (lift={lift:+.4f} m)")
    print(f"  probe_start_tick: {probe_start_tick}  probe_duration≈{probe_dur} ticks")


def _cyl_on_target(fsm, data, rb_body_id) -> bool:
    try:
        return fsm._cylinder_on_target_table()
    except Exception:
        return False


if __name__ == "__main__":
    main()
