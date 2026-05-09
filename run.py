#!/usr/bin/env python3
"""G1 Table Red Block — standalone MuJoCo scene with walker + reacher policies.

Converted from the LuckyEngine G1-Table-Red-Block.hscene. Runs the G1 robot
with trained Walker/Croucher/Rotator/Reacher ONNX policies in a scene with
a table, red cylindrical block, and multiple cameras (head, wrist, overhead).

Controls (press keys in the GLFW viewer window):
  Arrow Keys   : Walk forward/back, strafe left/right
  ; / '        : Turn left / right
  ,            : Toggle crouch mode
  [ / ]        : Height down / up
  \\           : Stop (zero velocity)
  /            : Toggle arm freeze
  .            : Toggle reach mode (right arm)
  Numpad 8/2   : Reach target forward/backward
  Numpad 4/6   : Reach target left/right
  Numpad 7/1   : Reach target up/down
  Numpad 5     : Reset reach target (auto mode)
  U/J, Y/H, 9/0 : Reach orientation roll/pitch/yaw
  R            : Reset reach orientation
  Space        : Reset robot + zero velocity
  C            : Cycle camera view in main window
  1            : Toggle head camera window
  2            : Toggle wrist camera window

Prerequisites:
  pip install mujoco onnxruntime numpy opencv-python

Usage:
  python run.py
  python run.py --no-cameras    # Disable camera windows (faster)
"""

import argparse
import json
import time
from pathlib import Path

import mujoco
import numpy as np

from common.controller import WalkerReacherController
from common.grasp import KinematicAttachment
from common.onnx_policy import ONNXPolicy
from common.scene import CameraRenderer, reset_robot
from policies.base import BasePolicy, PolicyOutput
from policies.fsm import FSMPolicy
from policies.fsm_core import FSMCore, FSMState

_FSM_RELEASE_STATES = frozenset({FSMState.OPEN_GRIP, FSMState.RETRACT, FSMState.DONE})
from policies.keyboard import KeyboardPolicy
from common.grasp import make_grasp_backend
from vla_bridge.action_adapter import world_to_pelvis
from vla_bridge.scripted_keyboard import (
    ScriptedKeyboardPlan,
    command_for_tick,
    load_scripted_keyboard_plan,
    plan_summary as scripted_plan_summary,
)

_SK_REACH_LOW   = np.array([-0.30, -0.60, -0.40], dtype=np.float32)
_SK_REACH_HIGH  = np.array([ 0.60,  0.30,  0.60], dtype=np.float32)
_SK_RIGHT_BIAS  = -0.03  # matches FSM hover/grasp bias — keeps arm on cylinder centerline

SCRIPT_DIR = Path(__file__).resolve().parent


# --------------------------------------------------------------------------- #
# Armature setup
# --------------------------------------------------------------------------- #
def set_armature(model, joint_names):
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


# --------------------------------------------------------------------------- #
# Scripted keyboard policy wrapper
# --------------------------------------------------------------------------- #
class ScriptedKeyboardPolicy(BasePolicy):
  """Drives the controller from a JSON scripted plan instead of a human.

  If the plan uses reach_frame="world", reach targets are converted to the
  current pelvis frame on every step() call using the controller's live data.
  """

  def __init__(self, plan: ScriptedKeyboardPlan, ctrl) -> None:
    self._plan = plan
    self._ctrl = ctrl
    self._use_world = getattr(plan, "reach_frame", "pelvis") == "world"
    self._total_ticks = scripted_plan_summary(plan)["total_ticks"]
    self._tick = 0
    self._last_phase = ""

  @property
  def done(self) -> bool:
    return self._tick >= self._total_ticks

  def handle_key(self, keycode: int) -> None:
    if keycode == 32:  # Space — rewind to start
      self._tick = 0
      self._last_phase = ""

  def _world_to_pelvis_reach(self, world_target) -> tuple:
    data = self._ctrl.data
    pelvis_pos  = np.array(data.qpos[:3], dtype=np.float64)
    pelvis_quat = np.array(data.qpos[3:7], dtype=np.float64)
    reach_p = world_to_pelvis(pelvis_pos, pelvis_quat,
                               np.asarray(world_target, dtype=np.float64))
    reach_p[1] = min(float(reach_p[1]), _SK_RIGHT_BIAS)
    reach_p = np.clip(reach_p, _SK_REACH_LOW, _SK_REACH_HIGH)
    return tuple(float(x) for x in reach_p)

  def step(self) -> PolicyOutput:
    cmd = command_for_tick(self._plan, self._tick)
    if cmd.phase != self._last_phase:
      print(f"[scripted] tick={self._tick:>5}  phase={cmd.phase}")
      self._last_phase = cmd.phase
    self._tick += 1

    if not cmd.reach_active:
      reach_target = (0.30, -0.20, 0.20)  # FSM carry pose — arm tucked during walk
    elif self._use_world:
      reach_target = self._world_to_pelvis_reach(cmd.reach_target)
    else:
      reach_target = tuple(cmd.reach_target)

    return PolicyOutput(
      walk_cmd=tuple(cmd.walk_cmd),
      reach_target=reach_target,
      reach_active=cmd.reach_active,
      grip_closed=cmd.grip_closed,
    )


# --------------------------------------------------------------------------- #
# Contact-guided grasp policy
# --------------------------------------------------------------------------- #
class ContactGuidedGraspPolicy(BasePolicy):
  """FSMCore approach + staged cage probe for close_grip.

  Uses FSMCore's fully reactive settle/walk/hover/descend (same logic as the
  original kinematic session).  When FSMCore reaches CLOSE_GRIP this policy
  intercepts and runs a lateral probe instead of a kinematic snap:

    Stage 1 — APPROACH: fingers pre-shaped to 22%, palm drifts 1 mm/tick
      laterally toward cylinder centre.  Keeps z fixed so arm stays at the
      correct height rather than being driven up.

    Stage 2 — CAGE: three-stage grip (38 % → 55 % → 72 %) so the cylinder
      is not knocked by a sudden hard close.  Each stage advances on contact
      or a max-tick timeout.

  After cage completes, FSMCore resumes from LIFT_SOURCE (via attached=True).
  """

  PROBE_STEP_M      = 0.002  # 2 mm/tick — faster approach
  CLOSE_ON_CONTACT  = 2
  GRIP_LATERAL_DIST = 0.015  # enter cage when palm is within 1.5 cm of cylinder
  MAX_PROBE_TICKS   = 600
  MIN_PROBE_TICKS   = 60     # wait at least 60 ticks for arm to settle before cage

  PRESHAPE_FRAC  = 0.22
  PRESHAPE_SPEED = 0.004

  CAGE_FRACS   = (0.25, 0.45, 0.65)
  CAGE_SPEEDS  = (0.003, 0.002, 0.0015)
  CAGE_TICKS   = (60,   80,   100)
  CAGE_MIN_CON = (999,  999,  999)   # time-only advance; don't rush on contact count

  PINCH_STEP_M = 0.0005  # gentle nudge during cage — keep palm seated

  def __init__(self, ctrl, grasp_backend, rb_body_id: int) -> None:
    self._ctrl  = ctrl
    self._gb    = grasp_backend
    self._rb_id = rb_body_id
    self._fsm   = FSMCore(ctrl.model, ctrl.data)

    # Fingertip body IDs — centroid used as the grasp-centre reference for drift.
    _finger_names = (
        "right_hand_thumb_2_link",
        "right_hand_middle_1_link",
        "right_hand_index_1_link",
    )
    self._finger_ids = [
        mujoco.mj_name2id(ctrl.model, mujoco.mjtObj.mjOBJ_BODY, n)
        for n in _finger_names
    ]

    self._reset_probe()

  def _reset_probe(self) -> None:
    self._probe_active    = False
    self._probe_ticks     = 0
    self._grip_triggered  = False
    self._probe_world_tgt = None
    self._probe_palm_z_world = 0.0  # world-frame Z frozen at probe start
    self._caging          = False
    self._cage_stage      = 0
    self._cage_ticks      = 0

  @property
  def done(self) -> bool:
    return self._fsm.state == FSMState.DONE

  def handle_key(self, keycode: int) -> None:
    if keycode == 32:
      self._fsm = FSMCore(self._ctrl.model, self._ctrl.data)
      self._reset_probe()
      self._ctrl.clear_grip_fraction_override()

  # ------------------------------------------------------------------ #

  def step(self) -> PolicyOutput:
    if self._probe_active:
      return self._probe_step()

    # Intercept at CLOSE_GRIP — let FSMCore complete HOVER+DESCEND at the closer
    # robot-body position, then hand off to the physical probe.
    if self._fsm.state == FSMState.CLOSE_GRIP and not self._grip_triggered:
      self._start_probe_from_cylinder()
      return self._probe_step()

    # After probe: pass attached=True so FSMCore advances through lift/carry/place.
    out = self._fsm.tick(attached=self._grip_triggered)

    # Keep grip closed while carrying (FSMCore release states open intentionally).
    if self._grip_triggered and not out.grip_closed and self._fsm.state not in _FSM_RELEASE_STATES:
      out = PolicyOutput(out.walk_cmd, out.reach_target, grip_closed=True, reach_active=out.reach_active)

    return out

  def _finger_centroid(self) -> np.ndarray:
    """Average position of 3 fingertips in world frame."""
    d = self._ctrl.data
    return np.mean([d.xpos[bid].copy() for bid in self._finger_ids], axis=0)

  def _world_step_to_pelvis(self, step_xy: np.ndarray) -> np.ndarray:
    """Rotate a world-frame XY step vector into pelvis frame (XY only)."""
    pelvis_quat = np.array(self._ctrl.data.qpos[3:7], dtype=np.float64)
    step_3d     = np.array([step_xy[0], step_xy[1], 0.0])
    # world_to_pelvis with zero origin = pure rotation q^{-1} * v
    pelvis_3d = world_to_pelvis(np.zeros(3), pelvis_quat, step_3d)
    return pelvis_3d[:2]

  _PALM_X_SETBACK_M = 0.05  # keep palm 5 cm behind cylinder X so fingertips sit inside radius

  def _probe_world_target(self, block: np.ndarray) -> np.ndarray:
    """Compute probe reach-target in pelvis frame from current world geometry.

    Targets (cyl_X − setback, cyl_Y, palm_Z_frozen) so the arm approaches
    naturally in both X and Y without direction reversal, while Z stays at
    the probe-start palm height to prevent vertical instability.
    """
    data        = self._ctrl.data
    pelvis_pos  = np.array(data.qpos[:3],  dtype=np.float64)
    pelvis_quat = np.array(data.qpos[3:7], dtype=np.float64)
    tgt_world = np.array([
        float(block[0]) - self._PALM_X_SETBACK_M,  # X: 5 cm behind cylinder (fingertips reach in)
        float(block[1]),                             # Y: toward cylinder center
        self._probe_palm_z_world,                    # Z: frozen at probe-start palm height
    ], dtype=np.float64)
    tgt_pelvis = world_to_pelvis(pelvis_pos, pelvis_quat, tgt_world)
    return np.clip(tgt_pelvis, _SK_REACH_LOW, _SK_REACH_HIGH)

  def _probe_step(self) -> PolicyOutput:
    data  = self._ctrl.data
    block = data.xpos[self._rb_id].copy()
    palm_world    = data.site_xpos[self._ctrl.right_palm_site_id].copy()
    lateral_world = block[:2] - palm_world[:2]   # world-frame XY: palm-to-cylinder
    lateral_dist  = float(np.linalg.norm(lateral_world))
    # Y-only distance: approach is from the side, so Y measures closure progress.
    lateral_y     = abs(float(block[1] - palm_world[1]))

    # ---- Phase 2: CAGE ----
    if self._caging:
      n_contacts = getattr(self._gb, "contact_count", lambda: 0)()
      self._cage_ticks += 1

      min_con = self.CAGE_MIN_CON[self._cage_stage]
      max_t   = self.CAGE_TICKS[self._cage_stage]

      if n_contacts >= min_con or self._cage_ticks >= max_t:
        if self._cage_stage < len(self.CAGE_FRACS) - 1:
          self._cage_stage += 1
          self._cage_ticks  = 0
          print(f"[contact-guided] cage stage {self._cage_stage}  "
                f"frac={self.CAGE_FRACS[self._cage_stage]:.2f}  contacts={n_contacts}  "
                f"lateral={lateral_dist*100:.1f} cm")
          self._ctrl.set_grip_fraction(
            self.CAGE_FRACS[self._cage_stage],
            close_speed=self.CAGE_SPEEDS[self._cage_stage],
          )
        else:
          print(f"[contact-guided] cage complete  contacts={n_contacts}  "
                f"lateral={lateral_dist*100:.1f} cm")
          self._caging         = False
          self._grip_triggered = True
          self._probe_active   = False
          self._ctrl.clear_grip_fraction_override()
          # Activate kinematic transport if backend supports it (HybridGraspBackend).
          if hasattr(self._gb, "confirm_contact"):
            self._gb.confirm_contact()
          tgt = self._probe_world_target(block)
          self._probe_world_tgt = list(tgt)
          return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=tuple(tgt),
            reach_active=True,
            grip_closed=True,
          )

      # Hold position during cage — target is live cylinder XY with frozen Z.
      tgt = self._probe_world_target(block)
      self._probe_world_tgt = list(tgt)

      return PolicyOutput(
        walk_cmd=(0.0, 0.0, 0.0),
        reach_target=tuple(tgt),
        reach_active=True,
        grip_closed=True,
      )

    # ---- Phase 1: APPROACH ----
    self._ctrl.set_grip_fraction(self.PRESHAPE_FRAC, close_speed=self.PRESHAPE_SPEED)

    streak    = getattr(self._gb, "contact_streak", 0)
    timed_out = self._probe_ticks >= self.MAX_PROBE_TICKS

    # No walking during probe: walking with reach_active=True is ineffective because the
    # reacher policy fights the walker.  The arm approaches the cylinder from the closer
    # robot position established by SOURCE_APPROACH_X=0.10.
    tgt = self._probe_world_target(block)
    self._probe_world_tgt = list(tgt)

    # Trigger cage once arm has settled (MIN_PROBE_TICKS) AND contact/proximity confirmed.
    settled = self._probe_ticks >= self.MIN_PROBE_TICKS
    if settled and streak >= self.CLOSE_ON_CONTACT and lateral_dist < 0.08:
      reason = f"contact (streak={streak})"
    elif settled and lateral_dist < 0.06:
      reason = f"proximity ({lateral_dist*100:.1f} cm)"
    elif timed_out:
      reason = "timeout"
    else:
      reason = None

    if reason is not None:
      print(f"[contact-guided] entering cage stage 0 — {reason}  "
            f"lateral={lateral_dist*100:.1f} cm  lateral_y={lateral_y*100:.1f} cm  "
            f"probe_ticks={self._probe_ticks}")
      self._caging     = True
      self._cage_stage = 0
      self._cage_ticks = 0
      self._ctrl.set_grip_fraction(self.CAGE_FRACS[0], close_speed=self.CAGE_SPEEDS[0])
      return PolicyOutput(
        walk_cmd=(0.0, 0.0, 0.0),
        reach_target=tuple(tgt),
        reach_active=True,
        grip_closed=True,
      )

    self._probe_ticks += 1
    return PolicyOutput(
      walk_cmd=(0.0, 0.0, 0.0),
      reach_target=tuple(tgt),
      reach_active=True,
      grip_closed=False,
    )

  def _to_pelvis(self, world_target, bias: bool = True) -> tuple:
    data        = self._ctrl.data
    pelvis_pos  = np.array(data.qpos[:3],  dtype=np.float64)
    pelvis_quat = np.array(data.qpos[3:7], dtype=np.float64)
    p = world_to_pelvis(pelvis_pos, pelvis_quat,
                        np.asarray(world_target, dtype=np.float64))
    if bias:
      p[1] = min(float(p[1]), _SK_RIGHT_BIAS)
    p = np.clip(p, _SK_REACH_LOW, _SK_REACH_HIGH)
    return tuple(float(x) for x in p)

  def _start_probe_from_cylinder(self) -> None:
    """Initialise the probe — arm approaches cylinder XY with Z frozen at palm height.

    Freezing Z prevents the reacher from being pulled off the table plane.
    X and Y target the cylinder directly (minus X setback) so there is no
    direction reversal from the FSM's prior approach trajectory.
    """
    data        = self._ctrl.data
    block_world = data.xpos[self._rb_id].copy()
    palm_world  = data.site_xpos[self._ctrl.right_palm_site_id].copy()
    pelvis_pos  = np.array(data.qpos[:3],  dtype=np.float64)
    pelvis_quat = np.array(data.qpos[3:7], dtype=np.float64)

    cyl_pelvis  = world_to_pelvis(pelvis_pos, pelvis_quat, block_world)
    palm_pelvis = world_to_pelvis(pelvis_pos, pelvis_quat, palm_world)

    # Freeze Z at probe-start palm world height to prevent vertical instability.
    self._probe_palm_z_world = float(palm_world[2])

    # Initial target: cylinder XY with X setback, frozen Z.
    # This continues the FSM's natural approach direction (no direction reversal).
    tgt = self._probe_world_target(block_world)
    self._probe_world_tgt = list(tgt)

    palm_lat = float(np.linalg.norm(block_world[:2] - palm_world[:2]))
    print(f"[contact-guided] probe init — cyl_pelvis={list(cyl_pelvis.round(3))}  "
          f"palm_pelvis={list(palm_pelvis.round(3))}  "
          f"palm_world=({float(palm_world[0]):.3f},{float(palm_world[1]):.3f},{float(palm_world[2]):.3f})  "
          f"palm_lat={palm_lat*100:.1f} cm  palm_z_frozen={self._probe_palm_z_world:.3f}")

    self._probe_active    = True
    self._probe_ticks     = 0
    self._ctrl.set_grip_fraction(self.PRESHAPE_FRAC, close_speed=self.PRESHAPE_SPEED)


# --------------------------------------------------------------------------- #
# Policy helpers
# --------------------------------------------------------------------------- #
def _apply_policy_output(ctrl, out) -> None:
  """Write a PolicyOutput into controller state before ctrl.step() runs."""
  ctrl.lin_vel_x, ctrl.lin_vel_y, ctrl.ang_vel_z = out.walk_cmd
  ctrl.reach_target[:] = out.reach_target
  ctrl.reach_active    = out.reach_active
  ctrl.grip_closed     = out.grip_closed


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
  parser = argparse.ArgumentParser(description="G1 Table Red Block — MuJoCo standalone")
  parser.add_argument("--no-cameras", action="store_true", help="Disable camera windows")
  parser.add_argument("--cam-fps", type=int, default=10, help="Camera render FPS (default: 10)")
  parser.add_argument(
    "--policy",
    choices=["keyboard", "fsm", "scripted_keyboard", "contact-guided-grasp"],
    default="keyboard",
    help="Control policy to use (default: keyboard)",
  )
  parser.add_argument(
    "--script-config",
    type=Path,
    default=SCRIPT_DIR / "configs/scripts/nominal_scripted_keyboard_v1.json",
    help="Scripted keyboard plan JSON (used with --policy scripted_keyboard)",
  )
  parser.add_argument(
    "--grasp-backend",
    choices=["kinematic", "contact-aware-physical"],
    default="kinematic",
    help="Grasp backend: 'kinematic' (teleport-weld) or 'contact-aware-physical' (observe-only)",
  )
  args = parser.parse_args()

  # Load config
  config_path = SCRIPT_DIR / "model_config.json"
  with open(config_path) as f:
    config = json.load(f)
  joint_names = config["joint_names"]

  # Load scene
  xml_path = SCRIPT_DIR / "scene.xml"
  print(f"Loading scene: {xml_path}")
  model = mujoco.MjModel.from_xml_path(str(xml_path))
  model.opt.timestep = 0.005  # 200 Hz — must match training
  set_armature(model, joint_names)

  data = mujoco.MjData(model)

  # Init robot pose — spawn behind the table, facing it
  reset_robot(model, data, config, joint_names, reset_data=False)

  # Load policies
  print("Loading ONNX policies...")
  walker = ONNXPolicy(str(SCRIPT_DIR / "walker.onnx"))
  croucher = ONNXPolicy(str(SCRIPT_DIR / "croucher.onnx"))
  rotator = ONNXPolicy(str(SCRIPT_DIR / "rotator.onnx"))

  right_reacher = None
  rr_path = SCRIPT_DIR / "right_reacher.onnx"
  if rr_path.exists():
    right_reacher = ONNXPolicy(str(rr_path))
    print("  Right reacher loaded.")

  # Create controller
  ctrl = WalkerReacherController(model, data, walker, croucher, rotator, config,
                                 right_reacher=right_reacher)

  grasp_backend = None
  if args.policy == "fsm":
    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = make_grasp_backend(args.grasp_backend, model, data, ctrl.right_palm_site_id, rb_body_id)
    policy = FSMPolicy(ctrl, grasp_backend=grasp_backend)
    print(f"Policy: FSM (autonomous) + {args.grasp_backend} grasp backend")
  elif args.policy == "scripted_keyboard":
    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = make_grasp_backend(args.grasp_backend, model, data, ctrl.right_palm_site_id, rb_body_id)
    scripted_plan = load_scripted_keyboard_plan(args.script_config)
    policy = ScriptedKeyboardPolicy(scripted_plan, ctrl)
    summary = scripted_plan_summary(scripted_plan)
    print(f"Policy: scripted_keyboard  plan={scripted_plan.name}  grasp={args.grasp_backend}")
    print(f"  {summary['num_steps']} steps  {summary['total_ticks']} ticks  {summary['total_seconds']:.1f}s")
    print("  Space = rewind to start")
  elif args.policy == "contact-guided-grasp":
    from common.grasp import HybridGraspBackend
    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = HybridGraspBackend(
        model, data, ctrl.right_palm_site_id, rb_body_id
    )
    policy = ContactGuidedGraspPolicy(ctrl, grasp_backend, rb_body_id)
    print("Policy: contact-guided-grasp (FSM approach + staged cage probe)")
    print("  Space = reset")
  else:
    policy = KeyboardPolicy(ctrl)
    print("Policy: keyboard (manual)")

  # Warm up ONNX models (first call triggers JIT compilation)
  print("Warming up policies...")
  _dummy99 = np.zeros((1, 99), dtype=np.float32)
  _dummy101 = np.zeros((1, 101), dtype=np.float32)
  _dummy36 = np.zeros((1, 36), dtype=np.float32)
  walker(_dummy99)
  croucher(_dummy101)
  rotator(_dummy99)
  if right_reacher:
    right_reacher(_dummy36)
  print("  Policies warm.")

  # Camera renderer (offscreen, for head/wrist cam windows)
  cam_renderer = None
  cv2 = None
  show_head_cam = not args.no_cameras
  show_wrist_cam = not args.no_cameras
  if not args.no_cameras:
    try:
      import cv2 as _cv2
      cv2 = _cv2
      cam_renderer = CameraRenderer(model, data, 320, 240)
      # Warm up renderer (first call compiles shaders)
      cam_renderer.render("head_cam")
      cam_renderer.render("wrist_cam")
      print("  Camera renderer ready (head_cam, wrist_cam).")
    except ImportError:
      print("  [WARN] opencv-python not installed — camera windows disabled.")
      print("  Install with: pip install opencv-python")
      show_head_cam = show_wrist_cam = False
    except Exception as e:
      print(f"  [WARN] Camera renderer init failed: {e}")
      show_head_cam = show_wrist_cam = False

  # Print controls
  print(f"\n{'='*50}")
  print("G1 TABLE RED BLOCK — MuJoCo Standalone")
  print(f"{'='*50}")
  print("  .          Toggle WALK / REACH mode")
  print("  --- WALK mode ---")
  print("  Arrows     Walk fwd/back, strafe L/R")
  print("  ; / '      Turn left / right")
  print("  \\          Stop")
  print("  --- REACH mode ---")
  print("  Up/Down    Reach forward / backward")
  print("  Left/Right Reach left / right")
  print("  ; / '      Reach up / down")
  print("  \\          Reset reach target")
  print("  --- Always ---")
  print("  Space      Reset robot")
  print(f"{'='*50}\n")

  # Mutable state for key callback
  state = {"reset": False}

  def on_key(keycode: int) -> None:
    if keycode == 32:  # Space
      state["reset"] = True
    else:
      policy.handle_key(keycode)

  # ------------------------------------------------------------------- #
  # Simulation loop using launch_passive (MuJoCo's built-in viewer)
  # ------------------------------------------------------------------- #
  from mujoco import viewer

  decimation = 4
  control_step = 0
  target_pos = ctrl.default_joint_pos.copy()
  sim_time = 0.0
  last_cam_render = 0.0
  cam_interval = 1.0 / args.cam_fps

  print("Launching MuJoCo viewer...")

  with viewer.launch_passive(model, data, key_callback=on_key) as v:
    # Reset clock AFTER viewer opens — prevents catchup lag burst on startup
    t0 = time.time()
    while v.is_running():
      # Handle spacebar reset
      if state["reset"]:
        reset_robot(model, data, config, joint_names)
        ctrl.last_action[:] = 0
        ctrl.last_arm_action[:] = 0
        ctrl.lin_vel_x = ctrl.lin_vel_y = ctrl.ang_vel_z = 0.0
        ctrl.reach_active = False
        ctrl.last_arm_target = None
        ctrl.frozen_arm_pos = None
        ctrl.grip_closed = False
        ctrl.input_mode = "walk"
        target_pos = ctrl.default_joint_pos.copy()
        state["reset"] = False
        print("[RESET] Robot reset → WALK mode")

      # Step physics in real time (cap catchup to avoid jitter snowball)
      wall = time.time() - t0
      max_catchup = 0.05  # Never try to catch up more than 50ms per frame
      if wall - sim_time > max_catchup:
        sim_time = wall - max_catchup
      while sim_time < wall:
        if control_step % decimation == 0:
          if args.policy in ("scripted_keyboard", "contact-guided-grasp") and policy.done:
            pass  # hold final pose when script finishes
          else:
            _apply_policy_output(ctrl, policy.step())
          target_pos = ctrl.step()
        ctrl.apply_pd_control(target_pos)
        mujoco.mj_step(model, data)
        if grasp_backend is not None:
          attached = grasp_backend.tick(ctrl.grip_closed)
          if attached and args.policy == "scripted_keyboard":
            pass  # attached state tracked inside grasp_backend
        control_step += 1
        sim_time += model.opt.timestep

      # Sync viewer
      v.sync()

      # Render camera views at lower FPS
      if cam_renderer and cv2 and (show_head_cam or show_wrist_cam):
        now = time.time()
        if now - last_cam_render >= cam_interval:
          last_cam_render = now
          if show_head_cam:
            img = cam_renderer.render("head_cam")
            cv2.imshow("Head Camera", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
          if show_wrist_cam:
            img = cam_renderer.render("wrist_cam")
            cv2.imshow("Wrist Camera", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
          cv2.waitKey(1)

  # Cleanup
  if cv2:
    try:
      cv2.destroyAllWindows()
    except Exception:
      pass
  print("Done.")


if __name__ == "__main__":
  main()
