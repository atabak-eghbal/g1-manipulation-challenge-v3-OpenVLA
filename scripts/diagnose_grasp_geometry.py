#!/usr/bin/env python3
"""Diagnose the hand geometry at grasp position: print finger tips, palm, cylinder positions."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mujoco
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from common.controller import WalkerReacherController
from common.grasp import KinematicAttachment, ContactAwarePhysicalGrasp
from common.onnx_policy import ONNXPolicy
from common.scene import reset_robot
from policies.base import PolicyOutput
from policies.fsm_core import FSMCore, FSMState
from vla_bridge.action_adapter import world_to_pelvis

import importlib.util
_run_spec = importlib.util.spec_from_file_location("run", ROOT / "run.py")
_run_mod  = importlib.util.module_from_spec(_run_spec)
sys.modules["run"] = _run_mod
_run_spec.loader.exec_module(_run_mod)
ContactGuidedGraspPolicy = _run_mod.ContactGuidedGraspPolicy


def set_armature(model, joint_names):
    for i, name in enumerate(joint_names):
        dof = 6 + i
        if "elbow" in name or "shoulder" in name or "wrist_roll" in name:
            model.dof_armature[dof] = 0.00360972
        elif "hip_pitch" in name or "hip_yaw" in name or name == "waist_yaw_joint":
            model.dof_armature[dof] = 0.01017752
        elif "hip_roll" in name or "knee" in name:
            model.dof_armature[dof] = 0.02510192
        elif "wrist_pitch" in name or "wrist_yaw" in name:
            model.dof_armature[dof] = 0.00425000
        elif "ankle" in name or name in ("waist_pitch_joint", "waist_roll_joint"):
            model.dof_armature[dof] = 0.00721945
        else:
            model.dof_armature[dof] = 0.00360972


def main():
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
    walker(np.zeros((1, 99), dtype=np.float32))
    croucher(np.zeros((1, 101), dtype=np.float32))
    rotator(np.zeros((1, 99), dtype=np.float32))
    right_reacher(np.zeros((1, 36), dtype=np.float32))

    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = ContactAwarePhysicalGrasp(
        model, data, ctrl.right_palm_site_id, rb_body_id
    )
    policy = ContactGuidedGraspPolicy(ctrl, grasp_backend, rb_body_id)

    # Get all hand-related body IDs for diagnosis
    hand_body_names = []
    for i in range(model.nbody):
        name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_BODY, i)
        if name and "right_hand" in name:
            hand_body_names.append((i, name))

    finger_names = [
        "right_hand_thumb_2_link",
        "right_hand_middle_1_link",
        "right_hand_index_1_link",
        "right_hand_thumb_1_link",
        "right_hand_middle_2_link",
        "right_hand_index_2_link",
        "right_hand_ring_1_link",
        "right_hand_pinky_1_link",
    ]
    finger_ids = {}
    for name in finger_names:
        bid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, name)
        if bid >= 0:
            finger_ids[name] = bid

    decimation = 4
    target_pos = ctrl.default_joint_pos.copy()
    MAX_TICKS = 4000
    probe_started = False
    last_print_probe_ticks = -50

    def print_geometry(label, tick):
        cyl = data.xpos[rb_body_id].copy()
        palm = data.site_xpos[ctrl.right_palm_site_id].copy()
        palm_lat = float(np.linalg.norm(cyl[:2] - palm[:2]))
        palm_3d  = float(np.linalg.norm(cyl - palm))
        print(f"\n--- {label} (tick={tick}) ---")
        print(f"  cylinder_world : {cyl.round(4)}")
        print(f"  palm_world     : {palm.round(4)}")
        print(f"  palm_lat_dist  : {palm_lat*100:.2f} cm")
        print(f"  palm_3d_dist   : {palm_3d*100:.2f} cm")
        for name, bid in finger_ids.items():
            fp = data.xpos[bid].copy()
            d_cyl = float(np.linalg.norm(fp - cyl))
            print(f"  {name:35s}: {fp.round(4)}  d_cyl={d_cyl*100:.2f}cm")
        # Print contact info
        n_contacts = 0
        for i in range(data.ncon):
            c = data.contact[i]
            n_contacts += 1
        print(f"  total_contacts : {data.ncon}")
        finger_geom_ids = set()
        for bid in finger_ids.values():
            for g in range(model.ngeom):
                if int(model.geom_bodyid[g]) == bid:
                    finger_geom_ids.add(g)
        obj_geoms = [g for g in range(model.ngeom)
                     if int(model.geom_bodyid[g]) == rb_body_id]
        print(f"  finger_geoms   : {len(finger_geom_ids)}")
        print(f"  obj_geoms      : {obj_geoms}")
        for i in range(data.ncon):
            c = data.contact[i]
            g1, g2 = int(c.geom1), int(c.geom2)
            in_fing = (g1 in finger_geom_ids or g2 in finger_geom_ids)
            in_obj  = (g1 in obj_geoms or g2 in obj_geoms)
            if in_fing or in_obj:
                n1 = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, g1) or str(g1)
                n2 = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, g2) or str(g2)
                print(f"  contact        : {n1} <-> {n2}")

    for tick in range(MAX_TICKS):
        out = policy.step()
        ctrl.lin_vel_x, ctrl.lin_vel_y, ctrl.ang_vel_z = out.walk_cmd
        ctrl.reach_target[:] = out.reach_target
        ctrl.reach_active    = out.reach_active
        ctrl.grip_closed     = out.grip_closed
        target_pos = ctrl.step()
        for _ in range(decimation):
            ctrl.apply_pd_control(target_pos)
            mujoco.mj_step(model, data)
            grasp_backend.tick(ctrl.grip_closed)

        fsm_state = policy._fsm.state

        if fsm_state == FSMState.CLOSE_GRIP and not probe_started and policy._probe_active:
            probe_started = True
            print_geometry("PROBE START", tick)

        if probe_started and policy._probe_active:
            pt = policy._probe_ticks
            if pt - last_print_probe_ticks >= 50:
                last_print_probe_ticks = pt
                cyl = data.xpos[rb_body_id].copy()
                palm = data.site_xpos[ctrl.right_palm_site_id].copy()
                lat = float(np.linalg.norm(cyl[:2] - palm[:2]))
                streak = getattr(grasp_backend, "contact_streak", 0)
                caging = policy._caging
                print(f"  probe_tick={pt:>4}  palm_lat={lat*100:.1f}cm  streak={streak}  caging={caging}")

        if probe_started and policy._caging and not getattr(policy, '_diag_cage_printed', False):
            policy._diag_cage_printed = True
            print_geometry("CAGE START", tick)

        if policy.done or tick == MAX_TICKS - 1:
            print_geometry("FINAL", tick)
            break

        if float(data.qpos[2]) < 0.40:
            print(f"Robot fell at tick {tick}")
            break


if __name__ == "__main__":
    main()
