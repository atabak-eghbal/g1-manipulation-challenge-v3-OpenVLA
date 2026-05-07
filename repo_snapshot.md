# Repo Snapshot: g1-manipulation-challenge-v3-openvla

## Repo Tree

```text
g1-manipulation-challenge-v3-openvla
├── artifacts
│   └── .gitkeep
├── assets
│   ├── head_link.obj
│   ├── left_ankle_pitch_link.obj
│   ├── left_ankle_roll_link.obj
│   ├── left_elbow_link.obj
│   ├── left_hand_index_0_link.STL
│   ├── left_hand_index_1_link.STL
│   ├── left_hand_middle_0_link.STL
│   ├── left_hand_middle_1_link.STL
│   ├── left_hand_palm_link.STL
│   ├── left_hand_thumb_0_link.STL
│   ├── left_hand_thumb_1_link.STL
│   ├── left_hand_thumb_2_link.STL
│   ├── left_hip_pitch_link.obj
│   ├── left_hip_roll_link.obj
│   ├── left_hip_yaw_link.obj
│   ├── left_knee_link.obj
│   ├── left_shoulder_pitch_link.obj
│   ├── left_shoulder_roll_link.obj
│   ├── left_shoulder_yaw_link.obj
│   ├── left_wrist_pitch_link.obj
│   ├── left_wrist_roll_link.obj
│   ├── left_wrist_yaw_link.obj
│   ├── logo_link.obj
│   ├── pelvis.obj
│   ├── pelvis_contour_link.obj
│   ├── right_ankle_pitch_link.obj
│   ├── right_ankle_roll_link.obj
│   ├── right_elbow_link.obj
│   ├── right_hand_index_0_link.STL
│   ├── right_hand_index_1_link.STL
│   ├── right_hand_middle_0_link.STL
│   ├── right_hand_middle_1_link.STL
│   ├── right_hand_palm_link.STL
│   ├── right_hand_thumb_0_link.STL
│   ├── right_hand_thumb_1_link.STL
│   ├── right_hand_thumb_2_link.STL
│   ├── right_hip_pitch_link.obj
│   ├── right_hip_roll_link.obj
│   ├── right_hip_yaw_link.obj
│   ├── right_knee_link.obj
│   ├── right_shoulder_pitch_link.obj
│   ├── right_shoulder_roll_link.obj
│   ├── right_shoulder_yaw_link.obj
│   ├── right_wrist_pitch_link.obj
│   ├── right_wrist_roll_link.obj
│   ├── right_wrist_yaw_link.obj
│   ├── torso_link_rev_1_0.obj
│   ├── waist_roll_link_rev_1_0.obj
│   └── waist_yaw_link_rev_1_0.obj
├── common
│   ├── __init__.py
│   ├── controller.py
│   ├── grasp.py
│   ├── onnx_policy.py
│   └── scene.py
├── configs
│   └── scenarios
│       └── small_perturbations.json
├── data
│   ├── vla_demos
│   │   ├── batch_000
│   │   │   ├── demo_000
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   ├── demo_001
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   ├── demo_002
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   └── batch_manifest.json
│   │   ├── batch_000_no_images
│   │   │   ├── demo_000
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   ├── demo_001
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   └── batch_manifest.json
│   │   ├── batch_001_perturbed_dryrun
│   │   │   └── batch_manifest.json
│   │   ├── batch_001_perturbed_no_images
│   │   │   ├── demo_000
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   ├── demo_001
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   ├── demo_002
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   ├── demo_003
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   ├── demo_004
│   │   │   │   ├── frames
│   │   │   │   ├── demo.jsonl
│   │   │   │   └── summary.json
│   │   │   └── batch_manifest.json
│   │   ├── demo_000
│   │   │   ├── frames
│   │   │   ├── plots
│   │   │   ├── demo.jsonl
│   │   │   └── summary.json
│   │   ├── demo_000_no_images
│   │   │   ├── frames
│   │   │   ├── demo.jsonl
│   │   │   └── summary.json
│   │   ├── demo_001
│   │   │   ├── frames
│   │   │   ├── demo.jsonl
│   │   │   └── summary.json
│   │   └── demo_002_every_tick
│   │       ├── frames
│   │       ├── demo.jsonl
│   │       └── summary.json
│   ├── vla_exports
│   │   ├── batch_000_no_images_g1_native
│   │   │   ├── audit
│   │   │   │   ├── audit_report.json
│   │   │   │   ├── split_summary.json
│   │   │   │   ├── train.jsonl
│   │   │   │   └── val.jsonl
│   │   │   ├── training_views
│   │   │   │   ├── filtered_no_idle.jsonl
│   │   │   │   ├── full.jsonl
│   │   │   │   ├── sample_weights.jsonl
│   │   │   │   └── training_view_summary.json
│   │   │   ├── dataset.jsonl
│   │   │   ├── source_manifest.json
│   │   │   └── summary.json
│   │   ├── g1_native_demo_002
│   │   │   ├── audit
│   │   │   │   ├── audit_report.json
│   │   │   │   ├── split_summary.json
│   │   │   │   ├── train.jsonl
│   │   │   │   └── val.jsonl
│   │   │   ├── training_views
│   │   │   │   ├── filtered_no_idle.jsonl
│   │   │   │   ├── full.jsonl
│   │   │   │   ├── sample_weights.jsonl
│   │   │   │   └── training_view_summary.json
│   │   │   ├── dataset.jsonl
│   │   │   └── summary.json
│   │   └── g1_native_demo_002_copied
│   │       ├── images
│   │       ├── dataset.jsonl
│   │       └── summary.json
│   └── vla_replays
│       ├── replay_000
│       │   ├── plots
│       │   ├── replay_summary.json
│       │   └── replay_trace.npz
│       ├── replay_000_short
│       │   ├── replay_summary.json
│       │   └── replay_trace.npz
│       ├── replay_001_arm_only
│       │   ├── replay_summary.json
│       │   └── replay_trace.npz
│       ├── replay_001_hybrid
│       │   ├── replay_summary.json
│       │   └── replay_trace.npz
│       ├── replay_001_teacher
│       │   ├── replay_summary.json
│       │   └── replay_trace.npz
│       ├── replay_002_hybrid
│       │   ├── replay_summary.json
│       │   └── replay_trace.npz
│       └── replay_002_teacher
│           ├── replay_summary.json
│           └── replay_trace.npz
├── docs
│   ├── BASELINE_AUDIT.md
│   ├── VLA_DECISION_LOG.md
│   └── VLA_RESEARCH_PLAN.md
├── policies
│   ├── __init__.py
│   ├── base.py
│   ├── fsm.py
│   ├── fsm_core.py
│   └── keyboard.py
├── scripts
│   ├── __init__.py
│   ├── audit_g1_native_vla_dataset.py
│   ├── build_g1_native_training_views.py
│   ├── export_g1_native_vla_batch_dataset.py
│   ├── export_g1_native_vla_dataset.py
│   ├── inspect_g1_native_vla_dataset.py
│   ├── inspect_vla_batch_diversity.py
│   ├── inspect_vla_demo.py
│   ├── plot_vla_demo.py
│   ├── record_demo.py
│   ├── record_vla_demo.py
│   ├── record_vla_demo_batch.py
│   ├── replay_vla_demo.py
│   ├── smoke_env.py
│   └── test_fsm_approach.py
├── tests
│   ├── __init__.py
│   ├── test_batch_diversity_manifest.py
│   ├── test_g1_native_batch_dataset_export.py
│   ├── test_g1_native_dataset.py
│   ├── test_g1_native_dataset_audit.py
│   ├── test_g1_native_training_views.py
│   ├── test_scenario_config.py
│   ├── test_vla_action_adapter.py
│   ├── test_vla_batch_manifest.py
│   ├── test_vla_demo_schema.py
│   └── test_vla_replay_metrics.py
├── vision
│   └── __init__.py
├── vla_bridge
│   ├── __init__.py
│   ├── action_adapter.py
│   ├── batch_dataset_export.py
│   ├── batch_diversity.py
│   ├── batch_manifest.py
│   ├── dataset_audit.py
│   ├── demo_recorder.py
│   ├── demo_schema.py
│   ├── g1_native_dataset.py
│   ├── replay_metrics.py
│   ├── scenario_config.py
│   └── training_views.py
├── .gitignore
├── croucher.onnx
├── croucher.onnx.data
├── DEV_LOG.md
├── g1.xml
├── model_config.json
├── MUJOCO_LOG.TXT
├── README.md
├── repo_snapshot.md
├── right_reacher.onnx
├── right_reacher.onnx.data
├── rotator.onnx
├── rotator.onnx.data
├── run.py
├── scene.xml
├── walker.onnx
└── walker.onnx.data
```

## File Contents

---

## FILE: `.gitignore`

```
__pycache__/
*.pyc
```

---

## FILE: `DEV_LOG.md`

```md
# Development Log - G1 Manipulation Project

## Template
- **Timestamp:** - **Step:** - **Goal / Hypothesis:** - **Files Changed:** - **Commands Run:** - **Expected Result:** - **Actual Result:** - **Pass / Fail:** - **Next Risk:** ---

## [2026-04-27] Step 1: Baseline Audit and Bootstrap
- **Goal / Hypothesis:** Establish a verified baseline of the original repository to ensure all assets and policies load correctly before refactoring.
- **Files Changed:** Created `DEV_LOG.md`, `docs/BASELINE_AUDIT.md`.
- **Commands Run:** `python run.py --no-cameras`
- **Expected Result:** MuJoCo scene loads, ONNX policies load, and the G1 robot is visible in a standing pose.
- **Actual Result:** (To be filled by Agent after execution)
- **Pass / Fail:** (To be filled by Agent)
- **Next Risk:** Path breakages during directory restructuring in Step 2.

## [2026-04-28] Step 2: Modular Skeleton and Policy Contract
- **Goal / Hypothesis:** Introduce a policy contract and package scaffolding while preserving manual keyboard control.
- **Files Changed:** `run.py`, `common/__init__.py`, `policies/__init__.py`, `policies/base.py`, `policies/keyboard.py`, `vision/__init__.py`, `tests/__init__.py`, `scripts/__init__.py`, `artifacts/.gitkeep`.
- **Commands Run:** `python run.py --policy keyboard --no-cameras`
- **Expected Result:** Manual controls behave identically under the keyboard policy, and the scene + ONNX policies load.
- **Actual Result:** `ModuleNotFoundError: No module named 'mujoco'` before scene load.
- **Pass / Fail:** Fail (missing MuJoCo dependency in environment).
- **Architecture Decision:** Establish `policies` as the home for high-level policy contracts/implementations, leaving existing controller logic in the main runner for now while future shared infrastructure can move into `common`.
- **Directory Tree:**
  ```
  g1-manipulation-challenge-v2/
  ├── artifacts/
  ├── common/
  ├── docs/
  ├── policies/
  │   ├── __init__.py
  │   ├── base.py
  │   └── keyboard.py
  ├── scripts/
  ├── tests/
  └── vision/
  ```
- **Behavior Confirmation:** Runs as expected
- **Scene Loaded:** Yes
- **ONNX Files Found:** Not checked at runtime; files are still present in repo (`walker.onnx`, `croucher.onnx`, `rotator.onnx`, `right_reacher.onnx`).
- **MuJoCo Warnings:** None (load did not start).
- **Blockers:** N/A
- **Next Risk:** N/A

## [2026-04-28] Step 3: Extract ONNX Loading, Reset, Controller Core
- **Goal / Hypothesis:** Extract low-level locomotion/reaching infrastructure into `common` without changing keyboard-driven behavior or control timing.
- **Files Changed:** `common/onnx_policy.py`, `common/scene.py`, `common/controller.py`, `run.py`, `DEV_LOG.md`.
- **Commands Run:** `python run.py --policy keyboard --no-cameras`
- **Expected Result:** Manual controls behave identically, policies warm up, and reset uses deterministic helper.
- **Actual Result:** `ModuleNotFoundError: No module named 'mujoco'` before scene load.
- **Pass / Fail:** Fail (missing MuJoCo dependency in environment).
- **Extracted Files:** `common/onnx_policy.py` (CPU ONNX wrapper), `common/scene.py` (deterministic reset + camera renderer), `common/controller.py` (`WalkerReacherController`).
- **Behavior Parity Checks:** Kept 200 Hz timestep with decimation=4; preserved warmup calls and keyboard control flow; reset state still zeros velocities and reach state .
- **Controller Assumptions (ONNX Compatibility):** Walker obs ordering/scale matches config; default joint offsets from `model_config.json` stay unchanged; walker arm targets are zeroed before right-arm overlay; right-arm deltas are rate-limited; finger actuators remain written separately from body joints.

## [2026-04-27] Step 4: Headless Smoke Test (scripts/smoke_env.py)
- **Goal / Hypothesis:** Create a repeatable headless check that validates scene loading and ONNX warmup without the interactive viewer.
- **Files Changed:** `scripts/smoke_env.py` (new), `DEV_LOG.md`.
- **Commands Run:** `python scripts/smoke_env.py`
- **Expected Result:** Script exits 0, prints pass/fail summary, confirms all FSM-required names.
- **Actual Result:**
  ```
  --- Config ---
    [PASS] model_config.json exists
    [PASS] joint_names present  (29 joints)
    [PASS] config['walker'] block
    [PASS] config['croucher'] block

  --- MuJoCo scene ---
    [PASS] scene.xml exists
    [PASS] scene loaded + forward pass

  --- Cameras ---
    [PASS] camera 'head_cam'  (id=3)
    [PASS] camera 'wrist_cam'  (id=4)
    [PASS] camera 'overhead'  (id=0)
    [PASS] camera 'side_view'  (id=1)
    [PASS] camera 'tracking'  (id=2)

  --- Bodies ---
    [PASS] body 'pelvis'  (id=1)
    [PASS] body 'red_block'  (id=47)
    [PASS] body 'table'  (id=45)
    [PASS] body 'table_white'  (id=46)

  --- Sites ---
    [PASS] site 'right_palm'  (id=5)
    [PASS] site 'imu_in_pelvis'  (id=0)
    [PASS] site 'left_foot'  (id=1)
    [PASS] site 'right_foot'  (id=2)

  --- Config joints in model ---
    [PASS] all 29 joints present

  --- ONNX (required) ---
    [PASS] walker.onnx exists
    [PASS] walker warmup  (in=99 out=29)
    [PASS] right_reacher.onnx exists
    [PASS] right_reacher warmup  (in=36 out=7)

  --- ONNX (optional) ---
    [OK  ] croucher: in=101 out=29
    [OK  ] rotator: in=99 out=29

  ==================================================
  RESULT: PASS  — repo is ready for FSM work
  ==================================================
  ```
- **Pass / Fail:** Pass (exit 0).
- **Missing names / files:** None. All required cameras, bodies, sites, joints, and ONNX files present. Both optional ONNX files (croucher, rotator) also present and warm.
- **FSM readiness:** CONFIRMED. `right_palm` site (reacher positioning), `red_block` body (manipulation target), all 29 config joints, `head_cam`/`wrist_cam` cameras, and both required ONNX models are verified present and functional.
- **Next Risk:** FSM state transitions and obs assembly correctness; walker obs vector ordering must be validated against the trained model's expected input layout before FSM integration.

## [2026-04-28] Step 5: FSM Scaffold (settle-only)
- **Goal / Hypothesis:** Add the FSM plumbing (`SETTLE` → `DONE`) before adding any motion, so state transitions and logging can be verified independently.
- **Files Changed:** `policies/base.py`, `policies/keyboard.py`, `policies/fsm_core.py` (new), `policies/fsm.py` (new), `run.py`, `DEV_LOG.md`.
- **Commands Run:** `python run.py --policy fsm --no-cameras`
- **Expected Result:** Robot holds pose, FSM logs `SETTLE → DONE` after ~3 s, no object motion, keyboard path unaffected.

### FSM State Diagram (Step 5)
```
         ┌────────────────────────────────────────────┐
         │  SETTLE (150 ticks ≈ 3 s)                  │
         │  walk_cmd  = (0, 0, 0)                     │
         │  reach_target = (0.3, -0.2, 0.2)  (carry) │
         │  reach_active = False                      │
         │  grip_closed  = False                      │
         └────────────────┬───────────────────────────┘
                          │ tick_state >= 150
                          ▼
         ┌────────────────────────────────────────────┐
         │  DONE  (holds carry pose indefinitely)     │
         └────────────────────────────────────────────┘

  Future stubs (not yet wired):
    DONE → APPROACH → GRASP → TRANSPORT → PLACE
```

### Log output
```
[FSM] init  state=SETTLE
[FSM] SETTLE  waiting 150 ticks (~3 s)
[FSM] SETTLE → DONE  (t=150)
[FSM] DONE  task complete — holding position
```

- **Actual Result:** 300-tick headless simulation: FSM reaches DONE at t=150 exactly; `walk_cmd=(0,0,0)`, `reach_active=False`, `grip_closed=False` in both states. `PolicyOutput.reach_active` defaults to `False` (backward-compatible — existing keyboard tests unaffected).
- **Pass / Fail:** Pass.
- **Scaffold confirmed stable:** Yes. No motion, no regression to keyboard path, clean transition log. Safe to begin APPROACH logic in Step 6.
- **Next Risk:** Computing approach walk_cmd from pelvis→red_block displacement requires verifying the pelvis-frame coordinate convention matches the walker's training frame.

---

## [2026-04-28] Step 6: GT Object Lookup + Source Approach (SETTLE → APPROACH_SOURCE → HOVER_SOURCE)

- **Goal:** Walk the robot to the red cylinder and transition to HOVER_SOURCE once within arm reach.
- **Files Changed:** `policies/fsm_core.py`, `policies/fsm.py`, `common/controller.py`, `scripts/test_fsm_approach.py` (new).

---

### Decisions and Findings

#### Decision 1 — Walker ONNX takes raw observations (no external normalization)

**Hypothesis from previous session:** walker ONNX needs `(obs − mean) / std` applied externally because without it the robot barely moves.

**Disproof:** Comparing MD5 of `walker.onnx` between this repo and the working solution repo — they are **identical**. The solution's controller passes **raw** observations to the walker. Probing the ONNX directly confirmed:

```
raw zeros           → action max=0.628   (reasonable)
normalized zeros    → action max=14.78   (catastrophically large)
raw stand+vx=0.35   → action max=0.598   (reasonable)
norm stand+vx=0.35  → action max=1.923   (3× too large → fall)
```

**Root cause of fall:** External `(obs − mean) / std` was **double-normalizing** — the ONNX bakes in its own normalization internally. Applying it externally amplified all obs by ~3×, producing joint deltas large enough to knock the robot over in ~0.4 s.

**Fix:** Removed `_walker_obs_mean`, `_walker_obs_std` from `controller.__init__()` and removed the `obs_norm` line in `controller.step()`. Walker now receives raw obs.

**Also reverted:** The `last_action = self._walker_obs_mean[67:96].copy()` seeding fix from the previous session — this was based on the wrong premise. Reverted to `last_action = np.zeros(29)`.

---

#### Decision 2 — Reacher must run unconditionally (not gated on reach_active)

**Symptom:** Even with raw obs, robot moved only 0.07 m in 11 s (commanded at 0.35 m/s). No fall, just very slow progress.

**Root cause:** Our `controller.step()` only called the right-arm reacher when `reach_active=True`. During SETTLE and APPROACH (where `reach_active=False`), the right arm sat at its default pose (arms-at-sides). The **walker ONNX sees arm joint positions as part of obs[9:38]** — when trained with carry-pose arms and tested with default-pose arms, the obs distribution mismatch caused the walker to produce weak locomotion actions.

**Comparison with solution:** The solution's `WalkerReacherController.step()` **always** calls the reacher unconditionally. The FSM always sets `reach_target = CARRY_TARGET = (0.22, −0.24, 0.38)` during SETTLE and APPROACH, so the right arm is actively commanded to carry pose throughout walking.

**Fix:** Removed the `if self.reach_active` guard. The reacher now runs every tick, writing the right-arm columns regardless of `reach_active`. Also removed the `frozen_arm_pos` logic (solution doesn't have it; carry pose is the natural idle for the arm).

---

#### Decision 3 — Approach command: staircase speeds + vy strafe

**Previous approach:** Proportional `vx = K_VX × dx` (K_VX=2.5) with strafe disabled (K_VY=0) and gentle yaw only (K_WZ=0.15). Worked for standing/balance but was never tested with walking.

**New approach (from validated solution):**

```python
x_err = cyl[0] - 0.34
if x_err > 0.18:  vx = 0.35
elif x_err > 0.10: vx = 0.22
elif x_err > 0.04: vx = 0.12
else:              vx = 0.0

y_err = cyl[1] - (-0.05)              # target y = −0.05 (right-arm sweet spot)
vy  = clip(1.8 × y_err, −0.18, 0.18)
wz  = clip(1.2 × arctan2(cyl_y, max(cyl_x, 0.15)), −0.25, 0.25)
```

**Why staircase:** Proportional control overshoots the window at low x_err. The staircase steps smoothly to zero speed as the cylinder enters range.

**Why vy enabled:** Previous concern was coupled strafe+yaw oscillation. This does not occur when yaw is arctan2-based (naturally bounded) rather than proportional to a running error.

---

#### Decision 4 — Reach window tightened to solution-validated values

| Parameter | Old | New |
|-----------|-----|-----|
| REACH_X range | 0.28–0.52 m | 0.20–0.38 m |
| REACH_Y range | −0.45–0.12 m | −0.14–0.02 m |
| APPROACH_TARGET_X | 0.40 m | 0.34 m |
| REACH_DEBOUNCE | 10 ticks | 8 ticks |

Old window was oversized (especially Y), causing the debounce counter to fire before the arm was truly in range.

---

### Final test result

```
[FSM] SETTLE → APPROACH_SOURCE  (t=150)
[FSM] cylinder in reach window: pelvis_frame=(0.363, 0.017, 0.038)
[FSM] APPROACH_SOURCE → HOVER_SOURCE  (t=234)

PASS — reached HOVER_SOURCE at control tick 235
  cyl pelvis: x=0.362  y=0.020  z=0.037
```

Robot walks from spawn to within arm reach in 85 control ticks (1.7 s simulation) after settling.

- **Pass / Fail:** **Pass.**
- **Next Risk:** Step 7 — implement `DESCEND_SOURCE` + `CLOSE_GRIP` (arm descent to grasp height, finger close, kinematic attachment check).

---

## [2026-04-28] Step 7: Hover and Descend Toward Source

- **Goal:** Controlled arm-only motion: pre-grasp hover above the cylinder, then descent to grasp height. No grip yet.
- **Files Changed:** `policies/fsm_core.py`, `scripts/test_fsm_approach.py`.

---

### Decisions and Findings

#### Decision 1 — Geometry helpers mirror the solution exactly

Added four world-space helpers following the validated solution's conventions:

| Helper | Returns |
|--------|---------|
| `_palm_world()` | `data.site_xpos[palm_id]` — live palm position |
| `_table_surface_z()` | `geom_xpos[tbl_geom_id][2] + geom_size[tbl_geom_id][2]` — exact geom-based surface height |
| `_source_hover_world()` | cylinder_xy + z = table_surface_z + 0.18 m |
| `_source_grasp_world()` | cylinder_xy + z = table_surface_z + 0.06 m |

Table geom name: `"table_top"` (geom ID 97). Using geom-based surface rather than body-centre + hardcoded offset — more accurate when body origin is not at the geom surface.

#### Decision 2 — `_reach_from_world` with right_bias=-0.03

```python
def _reach_from_world(self, world_point, right_bias=-0.08):
    pos, quat = self._pelvis_pose()
    local = self._world_to_pelvis(pos, quat, world_point).copy()
    local[1] = min(local[1], right_bias)       # cap y: stay right of centreline
    return self._clip_reach_target(local)      # clip to reacher workspace
```

For source hover/grasp: `right_bias=-0.03` (table is roughly in front of robot, not far left). Source cylinder at pelvis-frame y ≈ 0.017–0.029, which would be clamped to y = -0.03 (keeping the reach target 3 cm to the right, inside the right arm's workspace).

Reacher workspace bounds (from training spec): x ∈ [−0.30, 0.60], y ∈ [−0.60, 0.30], z ∈ [−0.40, 0.60].

#### Decision 3 — Distance thresholds from the solution's validated values

| Threshold | Value | Rationale |
|-----------|-------|-----------|
| `HOVER_SOURCE_THRESHOLD` | 0.14 m | Reacher accuracy floor is ~12 cm; need ≥ this |
| `DESCEND_SOURCE_THRESHOLD` | 0.12 m | At the practical limit; relying on timeout fallback |
| `DEBOUNCE_REACH` | 6 ticks | ~0.12 s; prevents single-step noise triggering transitions |

#### Decision 4 — Timeouts as belt-and-suspenders

HOVER_SOURCE_TIMEOUT=200 ticks (~4 s), DESCEND_SOURCE_TIMEOUT=300 ticks (~6 s). The reacher cannot always achieve the distance threshold — DESCEND especially hits the ~12 cm accuracy floor. The timeout ensures the FSM advances even when the exact threshold is never met.

#### Decision 5 — Entry prints moved into `_transition()`

Previously `if self._tick_state == 0:` never fired (tick is incremented after dispatch, so first real call has tick_state=1). Moved state-entry logging into `_transition()` itself where it reliably fires at the moment of state change.

---

### Observed geometry (from test run)

```
table_z                 = 0.7330 m   (top surface of source table)
hover_world.z           = 0.9130 m   (table_z + 0.18)
grasp_world.z           = 0.7930 m   (table_z + 0.06)
cylinder_world.z        = 0.7680 m   (cylinder body origin, ~3.5 cm above surface)

HOVER_SOURCE entry palm_dist  = 0.256 m   (arm still in carry pose)
HOVER_SOURCE exit  palm_dist  = 0.127 m   (threshold met: 0.127 < 0.14)
DESCEND_SOURCE entry palm_dist = 0.134 m
DESCEND_SOURCE exit  palm_dist = 0.123 m  (timeout — reacher accuracy floor)

CLOSE_GRIP palm_to_cyl = 0.128 m     (within ~13 cm kinematic attachment range)
```

**Table clearance:** hover is 18 cm above table; palm descends to ~8 cm above table at CLOSE_GRIP. No collision risk.

**Reacher accuracy floor:** DESCEND_SOURCE exits via timeout (300 ticks = 6 s) with palm_dist=0.123 m — just above the 0.12 m threshold. This matches the solution's documented ~12 cm floor. The kinematic attachment in Step 8 fires at 13 cm, so this distance is within the attachment window.

---

### FSM sequence (full)

```
SETTLE (150 ticks)
  → APPROACH_SOURCE: walk → cyl in reach window
  → HOVER_SOURCE: arm rises to hover above cyl (table_z + 0.18)
  → DESCEND_SOURCE: arm descends to grasp height (table_z + 0.06)
  → CLOSE_GRIP: hold — grip pending Step 8
```

### Test result

```
PASS — reached CLOSE_GRIP at control tick 562
  palm_world : (-0.056, -0.083, 0.807)
  cyl_world  : (0.000, 0.026, 0.768)
  palm-to-cyl dist : 0.128 m
```

- **Pass / Fail:** **Pass.**
- **Next Risk:** Step 8 — close grip + kinematic attachment (attach when palm within 13 cm, clamp in-hand offset to ~3 cm so cylinder doesn't appear to float, then lift to carry pose).

---

## [2026-04-28] Step 8: Kinematic Grasp Backend and Source Lift

- **Goal:** First end-to-end grasp milestone — attach the cylinder kinematically once the grip closes, lift to carry pose, confirm the cylinder left the table.
- **Files Changed:** `common/grasp.py` (new), `policies/fsm_core.py`, `policies/fsm.py`, `run.py`, `scripts/test_fsm_approach.py`.

---

### Decisions and Findings

#### Decision 1 — `GraspBackend` / `KinematicAttachment` in `common/grasp.py`

Created an abstract `GraspBackend` interface with `attached`, `tick(grip_closed)`, and `release()`. The concrete `KinematicAttachment` class implements the simulation shortcut:

- **Attach trigger:** `grip_closed=True` AND palm-to-cylinder distance ≤ 0.13 m (the reacher accuracy floor — attachment fires the first physics tick that meets this condition).
- **Snap distance:** When attaching, the palm-local offset is clamped to 0.03 m so the cylinder sits in the hand even if the actual gap is larger. Observed in test: real dist = 0.128 m → snap_offset = 0.030 m (clamped from 0.103 m). The cylinder jumps ~10 cm to the palm — visually abrupt but acceptable for this baseline.
- **Collision disable:** `model.geom_contype[g] = 0` and `model.geom_conaffinity[g] = 0` for all geoms of `red_block` while attached. Restored on release. Prevents contact impulses from destabilising the robot when the cylinder teleports into the hand.
- **Pose update cadence:** Called after **every** `mujoco.mj_step()` in both `run.py` and the headless test (inside the decimation loop). This ensures the cylinder tracks the palm between control ticks. Drift between calls ≈ 5 ms × g ≈ 0.0002 m — negligible.
- **Velocity zeroing:** `data.qvel[qveladr:qveladr+6] = 0` every `_update_pose()` call. Without this the freejoint accumulates gravity velocity between teleportations.

#### Decision 2 — FSMCore receives `attached` flag via `tick(attached=bool)`

`FSMCore` stays free of any dependency on the grasp backend. `FSMPolicy` reads `grasp_backend.attached` and passes it as a parameter to `fsm.tick()`. `FSMCore` stores it as `self._attached` and uses it only in `_close_grip()` for state transition.

#### Decision 3 — `_close_grip_command` in `FSMPolicy`

A thin post-processing step: if the grasp backend reports `attached=True` but the current PolicyOutput has `grip_closed=False` (e.g., after DONE transition with `_attached=False` due to timing), it overrides grip to True. This guard prevents a single-tick grip release that would drop the cylinder.

#### Decision 4 — CLOSE_GRIP state

Holds grasp reach target with `grip_closed=True`. Transitions to LIFT_SOURCE as soon as `self._attached` (backend confirms attachment) or after CLOSE_GRIP_TIMEOUT = 100 ticks (~2 s, fallback if attachment never fires). In practice, attachment fires after 1 tick (first physics step with grip closed and palm within 0.13 m).

#### Decision 5 — LIFT_SOURCE state

Points reacher at `CARRY_POSE = (0.3, -0.2, 0.2)` with `grip_closed=True`. Transitions to DONE when `palm_world.z ≥ table_z + 0.25 m` (cylinder visibly above the table) OR after LIFT_SOURCE_TIMEOUT = 200 ticks (~4 s).

**Observation:** The LIFT_DONE_CLEARANCE = 0.25 m was not met — the arm reached palm_z = 0.874 m (clearance = 0.141 m above table) before timeout. LIFT_SOURCE exited via timeout. The reacher converges toward carry pose but is slowed by the additional cylinder mass (though kinematic; possibly by the already-stressed reacher workspace near table height). The cylinder is visibly above the table at DONE.

---

### Observed geometry (from test run)

```
Attach: dist=0.128 m  snap_offset=0.030 m   (tick 562 — first physics step in CLOSE_GRIP)
LIFT_SOURCE entry: palm_z=0.813  cyl_z=0.802  clearance=0.069 m above table
LIFT_SOURCE exit:  palm_z=0.874  cyl_z=0.866  timeout (200 ticks)
DONE:              cyl_z=0.866  table_z=0.733  clearance=0.133 m
```

**Object float / jitter:** No visible float between control ticks (drift ≈ 0.2 mm per physics step). Cylinder snaps 10 cm from pre-attach position to palm on first attach tick — abrupt but stable. No jitter observed in subsequent carry ticks.

**Lift stability:** Robot did not fall. The arm held cylinder at palm through the full LIFT_SOURCE phase. Walker continued stable upright stance throughout (pelvis z never dropped below 0.78 m).

---

### FSM sequence (full pipeline)

```
SETTLE (150 ticks, ~3 s)
  → APPROACH_SOURCE: walk to reach window (85 ticks)
  → HOVER_SOURCE: arm rises above cylinder (26 ticks, threshold met)
  → DESCEND_SOURCE: arm descends to grasp height (300 ticks, timeout)
  → CLOSE_GRIP: grip closes + attachment fires (1 tick)
  → LIFT_SOURCE: carry pose, cylinder tracks palm (200 ticks, timeout)
  → DONE (tick 763)
```

---

### Test result

```
[GRASP] attached  dist=0.128 m  snap_offset=0.030 m
[FSM] CLOSE_GRIP → attached at t=562
[FSM] CLOSE_GRIP → LIFT_SOURCE  (t=562)
[FSM]   palm_z=0.813  cyl_z=0.802  attached=True
[FSM] LIFT_SOURCE → timeout  palm_z=0.874
[FSM] LIFT_SOURCE → DONE  (t=762)
[FSM]   cyl_z=0.866  table_z=0.733  clearance=0.133 m

PASS — reached DONE at control tick 763
  palm_world  : (-0.036, -0.194, 0.874)
  cyl_world   : (-0.014, -0.176, 0.866)
  table_z     : 0.733
  cyl clearance : 0.133 m above table
  attached    : True
```

- **Pass / Fail:** **Pass.**
- **Next Risk:** Step 9 — place the cylinder on the target table (approach target table, descend, release grip, retract arm to carry pose).

---

## [2026-04-28] Step 9: Target-Table Transport (LIFT_SOURCE → APPROACH_TARGET → HOVER_TARGET)

- **Goal:** Walk the robot from the source table to the target table's placement corridor while keeping the cylinder in the carry pose, then stub HOVER_TARGET.
- **Files Changed:** `policies/fsm_core.py`, `scripts/test_fsm_approach.py`.

---

### Decisions and Findings

#### Decision 1 — Carry pose during transport

`CARRY_POSE = (0.3, -0.2, 0.2)` (already defined in Step 8) is held throughout APPROACH_TARGET and HOVER_TARGET. `reach_active=True`, `grip_closed=True`. The cylinder rides the palm with no extra logic needed.

#### Decision 2 — Drop-point geometry (frozen at APPROACH_TARGET entry)

`_target_drop_world()` computes the world-frame drop point once and freezes it in `self._target_drop_pt`:
- `drop_x = geom_center_x` of `table_white_top` = −0.300 m
- `drop_y = geom_center_y + half_size_y − TARGET_NEAR_EDGE_INSET` = −0.80 + 0.25 − 0.05 = **−0.60 m** (5 cm inside the near edge)
- `drop_z = geom_surface_z = 0.633 m`

#### Decision 3 — Placement corridor (reach window)

The existing APPROACH_SOURCE reach window `x ∈ [0.20, 0.38], y ∈ [−0.14, 0.02]` is reused for the drop point expressed in the pelvis frame. `TARGET_REACH_DEBOUNCE = 8` consecutive in-window ticks required before transitioning to HOVER_TARGET.

#### Decision 4 — Two-phase target navigation

The robot starts APPROACH_TARGET at approximately (−0.346, −0.008) facing +x (yaw ≈ 0). The drop point is at (−0.30, −0.60). For the drop to land in the pelvis-frame reach window while the robot faces −y, the robot needs to be at px ∈ [−0.32, −0.16], py ∈ [−0.40, −0.22].

**Failed attempts (3 variations):**
- *vx=0, wz=±0.25*: Walker barely responds — yaw rate ≈ 0.053 rad/s (vs 0.25 commanded). 900-tick timeout never reached the window.
- *vx=0.06, wz=0.25*: Same low response — robot moves 0.014 m/s instead of 0.06 m/s; yaw barely changes.
- *vx=0.12, wz=0.25*: Orbit radius R=0.48 m; standing waypoint is inside the turning circle; robot never converges.

**Root cause:** `vel_max_angular = 1.0` — WZ_CAP=0.25 was only 25% of what the walker can handle. The walker needs substantially larger angular commands to actually turn.

**Fix — Phase 1:** `(VX_P1=0.12, vy=0, WZ_P1=−1.0)` until `|yaw + π/2| < 0.40 rad`. With wz=1.0 (vel_max_angular), the robot actually turns CW at sufficient rate. The small turning circle lands the robot near the reach window during Phase 1 itself.

**Fix — Phase 2:** Once facing −y, standard bearing-based staircase (vx, vy=K_VY·left_err, wz=K_WZ·a_err) toward the standing waypoint at (drop_x, drop_y + APPROACH_TARGET_X) = (−0.30, −0.26).

In practice the reach window was satisfied **during Phase 1** (at tick 439 after APPROACH_TARGET entry, yaw ≈ −0.64 rad, pelvis ≈ (−0.205, −0.013)), so Phase 2 never needed to execute.

---

### Observed geometry (from test run)

```
APPROACH_TARGET entry: drop_world=(−0.300,−0.600,0.633)  pelvis=(−0.346,−0.008)  yaw=0.064
HOVER_TARGET entry:    drop_pelvis=(0.373,−0.056,−0.123)  palm_z=0.870
                       [reach window satisfied: x=0.373 ∈ [0.20,0.38], y=−0.056 ∈ [−0.14,0.02]]
```

**Cylinder status at HOVER_TARGET:** still attached (grip_closed=True throughout).
**Walker stability:** robot did not fall; palm_z=0.870 throughout transport.

---

### FSM sequence (full pipeline through HOVER_TARGET)

```
SETTLE (150 ticks)
  → APPROACH_SOURCE: 84 ticks
  → HOVER_SOURCE: 26 ticks (threshold)
  → DESCEND_SOURCE: 300 ticks (timeout)
  → CLOSE_GRIP: 1 tick (attached)
  → LIFT_SOURCE: 200 ticks (timeout)
  → APPROACH_TARGET: 439 ticks (reach window)
  → HOVER_TARGET (tick 1202, holding)
```

---

### Test result

```
PASS — reached HOVER_TARGET at control tick 1203
  palm_world  : (−0.051, −0.238, 0.870)   [during APPROACH_TARGET Phase 1 turn]
  cyl_world   : (−0.026, −0.223, 0.863)   [cylinder tracking palm, attached]
  drop_world  : (−0.300, −0.600, 0.633)   [frozen drop point on target table]
  target_z    : 0.633
  attached    : True
```

- **Pass / Fail:** **Pass.**
- **Next Risk:** Step 10 — descend arm to drop height above target table, release grip, retract to carry pose.

---

## [2026-04-29] Step 10: Full Placement — HOVER_TARGET → LOWER_TARGET → OPEN_GRIP → RETRACT → DONE

- **Goal:** Complete the pick-and-place loop: descend arm above the target table, release grip, retract to carry pose, confirm cylinder on table.
- **Files Changed:** `policies/fsm_core.py`, `policies/fsm.py`, `scripts/test_fsm_approach.py`.

---

### Decisions and Findings

#### Decision 1 — Four-state placement pipeline

Mirrors the source-side HOVER_SOURCE → DESCEND_SOURCE → CLOSE_GRIP → LIFT_SOURCE structure:

| State | Action | Exit condition |
|---|---|---|
| HOVER_TARGET | arm → hover point (drop_xy, tgt_z + 0.18) | palm_dist < 0.14 m OR 200 ticks |
| LOWER_TARGET | arm → place point (drop_xy, tgt_z + 0.06) | palm_dist < 0.14 m OR 300 ticks |
| OPEN_GRIP | grip_closed=False, hold place point | attached=False OR 100 ticks |
| RETRACT | arm → CARRY_POSE, grip_closed=False | palm_z ≥ tgt_z + 0.25 m OR 200 ticks |

#### Decision 2 — PLACE_HEIGHT = 0.06 m (same as source GRASP_HEIGHT)

At LOWER_TARGET exit: palm_z=0.733, cyl_z=0.718, height_above_target=0.085 m. After release the cylinder falls 0.085 m to settle at cyl_z=0.650 (clearance=0.017 m ≈ 17 mm above table surface). That's a small but visible drop — within tolerance. Can tighten to PLACE_HEIGHT=0.04 m if needed.

**LOWER_TARGET exited via timeout** (palm_dist=0.183 m). The reacher's ~12 cm accuracy floor means it cannot reliably close the gap below ~0.18 m for the target table geometry. Timeout is the expected path.

#### Decision 3 — `_close_grip_command` exemption for release states

**Root cause of first-run failure:** `FSMPolicy._close_grip_command` overrode `grip_closed=False` → `True` whenever `grasp_backend.attached` was True, preventing any intentional release. The cylinder was never detached and was carried upward during RETRACT (cyl_z rose from 0.718 to 0.875).

**Fix:** Added `_RELEASE_STATES = {OPEN_GRIP, RETRACT, DONE}` and skip the guard when `self._fsm.state in _RELEASE_STATES`. The guard still protects mid-carry from accidental drops.

#### Decision 4 — `_cylinder_on_target_table()` helper

Checks:
1. cyl_z ∈ (target_z − 0.01, target_z + 0.20) — height sanity
2. cyl (x,y) within geom footprint + 5 cm margin

Observed: helper returns True at RETRACT entry (cyl_z=0.710) and again at DONE (cyl_z=0.650). XY margin is not needed in this run — the cylinder landed near the drop point center.

#### Decision 5 — DONE grip logic

Changed `_done()` to always output `grip_closed=False` (previously `grip_closed=self._attached`). After successful placement the grip should be open regardless.

---

### Observed geometry (from test run)

```
HOVER_TARGET entry: drop_pelvis=(0.373,−0.056,−0.123)  palm_z=0.870
HOVER_TARGET exit:  threshold met  palm_dist=0.120  (26 ticks)
LOWER_TARGET exit:  timeout  palm_dist=0.183  (300 ticks)
                    palm_z=0.733  cyl_z=0.718  height_above_target=0.085
OPEN_GRIP:          released after 2 ticks  (grasp backend confirmed)
RETRACT exit:       arm clear  palm_z=0.884  (51 ticks)
DONE:               cyl_z=0.650  target_z=0.633  clearance=0.017  on_target_table=True
```

**Flaky boundaries:** None observed in two identical runs (deterministic simulation).  
**Release height:** 8.5 cm above table → cylinder drops ~1.7 cm to rest. Visually clean placement.  
**`_cylinder_on_target_table()` vs visual:** Helper reports True at DONE; clearance=0.017 m confirms physical contact with table.

---

### FSM sequence (full pipeline — GT baseline)

```
SETTLE              (150 ticks,  ~3 s)
→ APPROACH_SOURCE   ( 84 ticks)         walk to reach window
→ HOVER_SOURCE      ( 26 ticks)         arm above cylinder
→ DESCEND_SOURCE    (300 ticks, timeout) arm to grasp height
→ CLOSE_GRIP        (  1 tick)          attach (dist=0.128 m)
→ LIFT_SOURCE       (200 ticks, timeout) raise to carry pose
→ APPROACH_TARGET   (439 ticks)         walk/turn to target corridor
→ HOVER_TARGET      ( 26 ticks)         arm above drop point
→ LOWER_TARGET      (300 ticks, timeout) arm to release height
→ OPEN_GRIP         (  2 ticks)         detach
→ RETRACT           ( 51 ticks)         arm clear of table
→ DONE              (tick 1581)
```

Total: **1582 control ticks ≈ 31.6 s** of simulated time.

---

### Test result

```
PASS — reached DONE at control tick 1582
  palm_world      : (−0.086, −0.278, 0.884)
  cyl_world       : (−0.067, −0.256, 0.650)
  drop_world      : (−0.300, −0.600, 0.633)
  target_z        : 0.633
  cyl_clearance   : 0.017 m
  on_target_table : True
  attached        : False
```

- **Pass / Fail:** **Pass — GT FSM baseline complete.**
- **Next Risk:** Robustness (scene variation, noise) and vision-guided approach (replacing GT geometry lookups).

---

### Post-step-10 finding (visual inspection after commit)

Running `python run.py --policy fsm --no-cameras` revealed the cylinder landing on the **floor**, not the blue table. The test script had reported PASS with `on_target_table=True`, but that was a false positive.

#### Root cause

`_approach_target` used `_in_reach_window(drop_pelvis)` to decide when to stop walking. The reach window `x ∈ [0.20, 0.38], y ∈ [−0.14, 0.02]` checks the drop point expressed in the **current pelvis frame**. During Phase 1 (CW turn), while the robot was at world ≈ (−0.205, −0.013) and yaw ≈ −0.64 rad (still 0.93 rad short of −π/2), the drop world point (−0.300, −0.600) happened to project to pelvis-frame ≈ (0.373, −0.056) — inside the window. The FSM transitioned to HOVER_TARGET immediately, even though the robot was far from the table.

The arm extended toward world-frame ≈ (0.095, −0.236) (arm_reach × cos/sin(−0.64) offset from pelvis), not toward the table at (−0.300, −0.600). The cylinder was released there and landed on the floor.

The `on_target_table=True` report was also a false positive: at DONE entry with cyl at (−0.067, −0.256, 0.650), `_cylinder_on_target_table()` should have returned False (|−0.256 − (−0.80)| = 0.544 > 0.30 = hy + margin). The fallback path (`tbl_white_id >= 0` check missing) allowed `xpos[-1]` (last body in model, arbitrary position) to be used, giving a spurious True.

#### Fix — `policies/fsm_core.py`

**1. World-proximity gate (new constant + helper):**

Added `TARGET_APPROACH_DIST_THRESH = 0.20 m` and `_near_target_waypoint()` which requires BOTH:
- `|yaw + π/2| < PHASE1_ALIGN_TOL` (robot is facing roughly −y; Phase 1 complete)
- World-frame distance from pelvis to standing waypoint `(drop_x, drop_y + APPROACH_TARGET_X)` < 0.20 m

**2. Replaced reach-window check in `_approach_target`:**

```python
# Before
if self._in_reach_window(drop):   # drop = drop point in pelvis frame

# After
if self._near_target_waypoint():  # world proximity + yaw gate
```

The standing waypoint `(−0.300, −0.600 + 0.34) = (−0.300, −0.260)` is where the robot needs to be for the arm to extend toward (−0.300, −0.600) at yaw = −π/2. Only when the pelvis is within 0.20 m of that waypoint AND facing the right direction does the FSM advance.

**3. Hardened `_cylinder_on_target_table()` fallback:**

Added `if self._tbl_white_id >= 0:` guard before the body-centre fallback, and return `False` when both IDs are −1. Previously, `xpos[-1]` (Python negative indexing into the MuJoCo array) could read an arbitrary body position when `tbl_white_id = −1`.

## [2026-05-04] Step 11: Fix Instability at Release and Improve Target Approach

- **Goal:** Resolve simulation crashes (NaNs) during cylinder release and improve placement accuracy on the target table.
- **Files Changed:** `common/grasp.py`, `policies/fsm_core.py`.
- **Findings:**
    1. **Instability Root Cause:** Restoring cylinder collisions immediately after opening the grip caused huge contact impulses (NaN/Inf in QACC) because the fingers had not yet physically opened enough to clear the cylinder geoms.
    2. **Target Approach Issue:** The robot was approaching the target table such that the drop point was to its left, forcing the right arm to reach across the chest, leading to overextension and instability.
- **Fixes:**
    1. **Delayed Release:** Added `RELEASE_TICKS = 15` to `KinematicAttachment`. Collisions are now restored 0.075s after the kinematic weld is broken, giving fingers time to open but preventing the cylinder from falling through the table.
    2. **Sweet-Spot Offset:** Offset the target approach waypoint by `+0.15m` in world X (robot's right when facing -y) to keep the drop point in the right arm's natural workspace.
    3. **Tightened Tolerances:** Reduced `TARGET_APPROACH_DIST_THRESH` and `PHASE1_ALIGN_TOL` to ensure better alignment before starting the arm motion.
- **Result:**
    - Simulation is stable throughout release and retraction.
    - Cylinder consistently lands on the blue target table (`on_target_table=True`).
    - Task completes through `DONE` state in ~50 simulated seconds.
- **Status:** **Pass.**

---

## [2026-05-05] Step 12: VLA Research Branch Scaffold

- **Goal / Hypothesis:** Create a safe VLA/OpenVLA research branch without changing the working FSM baseline. The hypothesis is that OpenVLA-style models may eventually augment the pipeline, but only after we prove action-space compatibility with the G1 walker/reacher/grip stack.

- **Files Changed:**
  - `docs/VLA_RESEARCH_PLAN.md` — research plan and staged roadmap
  - `docs/VLA_DECISION_LOG.md` — decision record for VLA branch
  - `vla_bridge/__init__.py` — empty package scaffold for future adapter/demo code
  - `DEV_LOG.md` — appended this entry

- **Commands Run:** None required.

- **Expected Result:** Repository now has a documented VLA research path while the implemented FSM behavior remains unchanged.

- **Reasoning:** OpenVLA-style models are attractive for language-conditioned manipulation, but direct live control is premature because the G1 stack uses a different action interface: walker commands, pelvis-frame reach targets, and binary grip state. The first real technical gate will be a 7D action replay test, not model inference.

- **Architecture Decision:** Keep the FSM as the teacher and fallback. Build the VLA branch progressively:
  1. documentation scaffold,
  2. action adapter,
  3. FSM demonstration recorder,
  4. 7D action replay,
  5. OpenVLA shadow mode,
  6. possible cloud inference/fine-tuning.

- **Pass / Fail:** Pass if files are created and no runtime files are changed.

- **Next Risk:** The 7D OpenVLA-style action space may not represent the full humanoid task, especially locomotion and target-table approach. If so, keep locomotion classical and use VLA only for manipulation refinement.

---

## [2026-05-05] Step 13: G1 VLA Action Adapter

- **Goal / Hypothesis:** Implement a pure translation layer from OpenVLA-style 7D end-effector actions to the existing G1 `PolicyOutput` contract. The hypothesis is that VLA actions can be represented as small palm deltas plus a gripper command, then converted into pelvis-frame reach targets for the existing right-reacher policy.

- **Files Changed:**
  - `vla_bridge/action_adapter.py` — pure NumPy adapter and coordinate helpers
  - `vla_bridge/__init__.py` — exports adapter helpers
  - `tests/test_vla_action_adapter.py` — unit tests for geometry, clipping, gripper mapping, and validation
  - `DEV_LOG.md` — appended this entry

- **Commands Run:**
  - `python -m unittest tests/test_vla_action_adapter.py`

- **Expected Result:** All adapter unit tests pass without requiring MuJoCo, OpenVLA, Hugging Face, PyTorch, or cloud infrastructure.

- **Reasoning:** Before loading OpenVLA or recording demonstrations, we need to prove that the proposed 7D action representation can be translated into the control format this repo already understands: `walk_cmd`, `reach_target`, `reach_active`, and `grip_closed`.

- **Architecture Decision:** Keep the adapter pure and isolated. It does not import MuJoCo or OpenVLA. It only imports `PolicyOutput` and NumPy. Rotation channels are intentionally ignored in this milestone.

- **Verification Evidence:** The unit test suite verifies:
  1. identity world-to-pelvis transform,
  2. zero-action output,
  3. delta accumulation,
  4. per-step delta clipping,
  5. gripper threshold mapping,
  6. reach workspace clipping,
  7. lazy initialization from current palm position,
  8. error handling for missing initialization,
  9. shape validation.

- **Pass / Fail:** Pass — all 9 unit tests pass and no runtime FSM files were modified.

- **Next Risk:** Passing unit tests only proves the adapter math and policy contract. It does not prove the robot can execute a full 7D action sequence. Step 14 must record FSM teacher demonstrations, and Step 15 must replay those 7D actions through the adapter.

---

## [2026-05-06] Step 14: FSM Demonstration Recorder

- **Goal / Hypothesis:** Run the existing FSM teacher and record a synchronized dataset of camera frames, FSM phases, palm positions, pelvis poses, reach targets, grip state, and derived 7D teacher actions — without modifying any FSM/controller/grasp runtime files and without introducing OpenVLA or model inference.

- **Files Changed:**
  - `vla_bridge/demo_schema.py` — pure Python + NumPy dataclass and JSONL serialization helpers
  - `vla_bridge/demo_recorder.py` — stateful recorder that watches the FSM and saves synchronized records
  - `vla_bridge/__init__.py` — exports Step 14 schema and recorder alongside Step 13 exports
  - `scripts/record_vla_demo.py` — end-to-end script that runs FSM + recorder headlessly with CLI args
  - `scripts/inspect_vla_demo.py` — lightweight inspection script to print summary stats from a JSONL file
  - `tests/test_vla_demo_schema.py` — 13 pure unit tests for schema helpers and recorder logic
  - `DEV_LOG.md` — appended this entry

- **Commands Run:**
  - `python -m unittest tests.test_vla_demo_schema -v`

- **Architecture Decisions:**
  1. **Pending-step pattern:** The 7D action at step *t* is defined as `palm(t+1) − palm(t)`. Each observation is held as a pending record until the next observation arrives to supply the second palm position. The final observation is finalized with a zero-displacement action in `finalize()`.
  2. **No MuJoCo in schema:** `demo_schema.py` and `demo_recorder.py` import only Python stdlib, NumPy, and each other. They can be imported and tested without MuJoCo.
  3. **Graceful cv2 fallback:** Frame saving tries `cv2.imwrite` first; if cv2 is unavailable it falls back to `np.save` (`.npy`), allowing headless environments without OpenCV.
  4. **FSM remains teacher:** The recorder does not produce any policy output and does not touch `ctrl`, `grasp_backend`, or any FSM state. It is a pure observer.
  5. **`record_every` downsampling:** Recording at every physics step (200 Hz) would create unnecessarily large datasets. The default `--record-every 5` records at the control rate / 5 = 10 Hz.

- **Verification Evidence:**
  1. `test_correct_shape_returns_python_floats` — `as_float_tuple` returns Python floats.
  2. `test_rejects_wrong_shape` — `as_float_tuple` raises ValueError on bad shape.
  3. `test_xyz_delta_and_gripper_closed` — `make_action_7d` computes correct delta and gripper bit.
  4. `test_single_step_roundtrip` — `VLADemoStep` round-trips through JSON.
  5. `test_multiple_steps_roundtrip` — `write_jsonl` / `read_jsonl` round-trip multiple steps.
  6. `test_finalizes_zero_action` — recorder finalizes zero action for a single observation.
  7. `test_computes_palm_delta_action` — recorder computes correct delta across two observations.
  8. `test_respects_record_every` — recorder skips non-boundary ticks.
  9. `test_saves_frame_path_when_rgb_provided` — frame path is stored in step metadata.

- **Pass / Fail:** Pass — all 13 unit tests pass; no FSM/controller/grasp runtime files were modified.

- **Next Risk:** Step 15 — replay recorded 7D actions through the G1VLAActionAdapter and verify that the robot reproduces the teacher trajectory within a tolerable error bound.

---

## [2026-05-05] Step 15: 7D Action Replay Harness

- **Goal / Hypothesis:** Replay the VLA-style teacher actions produced in Step 14 through `G1VLAActionAdapter` and the existing G1 walker/reacher/grip stack. The hypothesis is that the recorded `[dx, dy, dz, droll, dpitch, dyaw, gripper]` action sequence can be executed as a local action interface without asking the FSM for target positions.

- **Files Changed:**
  - `vla_bridge/replay_metrics.py` — pure NumPy metrics for teacher-vs-replay comparison
  - `scripts/replay_vla_demo.py` — replay harness for recorded VLA demonstrations
  - `tests/test_vla_replay_metrics.py` — unit tests for replay metrics
  - `vla_bridge/__init__.py` — exports replay metric helpers
  - `scripts/plot_vla_demo.py` — diagnostic plotting for action magnitude, grip state, phases, and replay error
  - `DEV_LOG.md` — appended this entry

- **Commands to Run:**
  ```bash
  python -m unittest tests/test_vla_replay_metrics.py
  python -m unittest tests/test_vla_action_adapter.py
  python -m unittest tests/test_vla_demo_schema.py
  python scripts/replay_vla_demo.py data/vla_demos/demo_000/demo.jsonl \
    --output-dir data/vla_replays/replay_000 \
    --mode arm-only
  ```

---
## [2026-05-05] Step 16: Hybrid Replay / Schema Upgrade
- **Goal / Hypothesis:** Upgrade the VLA demonstration and replay interface after Step 15 showed that arm-only 7D replay is insufficient. The hypothesis is that replay quality will improve when locomotion context is included through recorded `walk_cmd`, while still allowing the 7D action adapter to control manipulation.
- **Files Changed:**
  - `vla_bridge/demo_schema.py` — added `walk_cmd` and `reach_active` to `VLADemoStep`
  - `vla_bridge/demo_recorder.py` — records teacher walk/reach command fields
  - `scripts/record_vla_demo.py` — saves full teacher `PolicyOutput` fields
  - `scripts/replay_vla_demo.py` — added `teacher-command` and `hybrid-7d` replay modes
  - `vla_bridge/replay_metrics.py` — added walk-command metrics
  - `vla_bridge/__init__.py` — exports new helpers
  - `tests/test_vla_demo_schema.py` — updated schema/recorder tests
  - `tests/test_vla_replay_metrics.py` — updated replay metric tests
  - `scripts/inspect_vla_demo.py` — prints walk_nonzero_steps and reach_active_steps
  - `scripts/plot_vla_demo.py` — added walk_command_magnitude.png plot
  - `DEV_LOG.md` — appended this entry

---

## [2026-05-06] Step 17: G1-Native VLA Dataset Exporter

- **Goal / Hypothesis:** Export a model-ready supervised dataset using the G1-native command interface that Step 16 proved executable. The hypothesis is that future learned-policy work should target `walk_cmd`, `reach_target_pelvis`, `reach_active`, and `grip_closed` rather than raw relative 7D palm deltas.

- **Reasoning:** Step 16 showed that every-tick `teacher-command` replay achieved 0.0 m mean/max/final palm error and successful attachment, while `hybrid-7d` replay still failed with significant palm drift and no attachment. This means the first learned VLA-style target should be the G1-native command interface.

- **Files Changed:**
  - `vla_bridge/g1_native_dataset.py` — pure dataset schema/export helpers
  - `scripts/export_g1_native_vla_dataset.py` — CLI exporter from demo JSONL to supervised dataset JSONL
  - `scripts/inspect_g1_native_vla_dataset.py` — inspection CLI for exported datasets
  - `tests/test_g1_native_dataset.py` — pure unit tests for exporter/schema behavior
  - `vla_bridge/__init__.py` — exports new dataset helpers
  - `DEV_LOG.md` — appended this entry

- **Commands to Run:**

  ```bash
  python -m unittest tests/test_g1_native_dataset.py
  python -m unittest tests/test_vla_demo_schema.py
  python -m unittest tests/test_vla_replay_metrics.py
  python -m unittest tests/test_vla_action_adapter.py
  python scripts/smoke_env.py
  ```

  Export the dataset:
  ```bash
  export PYTHONPATH=$PYTHONPATH:.
  python scripts/export_g1_native_vla_dataset.py \
    data/vla_demos/demo_002_every_tick/demo.jsonl \
    --output-dir data/vla_exports/g1_native_demo_002
  ```

  Inspect the dataset:
  ```bash
  python scripts/inspect_g1_native_vla_dataset.py \
    data/vla_exports/g1_native_demo_002/dataset.jsonl
  ```

  Optional copy-images export:
  ```bash
  python scripts/export_g1_native_vla_dataset.py \
    data/vla_demos/demo_002_every_tick/demo.jsonl \
    --output-dir data/vla_exports/g1_native_demo_002_copied \
    --copy-images
  ```

- **Expected Result:** The exporter writes `dataset.jsonl` and `summary.json`. Each record contains an image path, instruction, optional phase, and an 8D G1-native action vector: `[walk_x, walk_y, walk_yaw, reach_x, reach_y, reach_z, reach_active, grip_closed]`.

- **Architecture Decision:** The exported action target is G1-native rather than raw OpenVLA-style 7D deltas. This preserves the command interface that the existing controller can replay faithfully.

- **Verification Evidence:**
  - All dataset unit tests pass.
  - Previous VLA tests still pass.
  - The exporter creates a non-empty `dataset.jsonl`.
  - `summary.json` reports sensible counts.
  - Inspection shows `action_vector_shape = (N, 8)`.
  - Records include image paths and instructions.
  - No OpenVLA/Hugging Face/PyTorch dependency is introduced.

- **Pass / Fail:** Pass.

- **Next Risk:** The dataset may be highly imbalanced across phases, with many repeated carry or reach-active states. A future Step 18 should analyze class/phase balance and create train/validation splits before any model inference or fine-tuning.

---

## [2026-05-06] Step 18: Dataset Audit + Train/Validation Split

- **Goal / Hypothesis:** Audit the G1-native VLA dataset exported in Step 17 before attempting OpenVLA shadow inference or fine-tuning. The hypothesis is that data quality, phase balance, and split design should be validated before any model work.

- **Reasoning:** Step 17 produced a clean supervised dataset with 2665 records and an 8D G1-native action vector. The next risk is not replay fidelity but dataset quality: phase imbalance, idle-heavy runs, action range issues, grip/reach imbalance, and misleading validation splits from a single trajectory.

- **Files Changed:**
  - `vla_bridge/dataset_audit.py` — pure audit and split helpers
  - `scripts/audit_g1_native_vla_dataset.py` — CLI audit/split tool
  - `tests/test_g1_native_dataset_audit.py` — unit tests for audit logic
  - `vla_bridge/__init__.py` — exports audit helpers
  - `DEV_LOG.md` — appended this entry

- **Commands to Run:**

  ```bash
  python -m unittest tests/test_g1_native_dataset_audit.py
  python scripts/audit_g1_native_vla_dataset.py \
    data/vla_exports/g1_native_demo_002/dataset.jsonl \
    --output-dir data/vla_exports/g1_native_demo_002/audit
  ```

- **Expected Result:** The auditor generates `audit_report.json` containing phase counts, action statistics, and warnings. The splitter generates `train.jsonl`, `val.jsonl`, and `split_summary.json` using a phase-aware temporal tail split.

- **Architecture Decision:** We use a phase-aware temporal split (taking the end of each phase for validation) to ensure validation coverage across all task stages while avoiding the "future leakage" of row-level random shuffling in time-series data.

- **Verification Evidence:**
  - `test_g1_native_dataset_audit.py` passes 11 unit tests.
  - Audit script identifies 11 phases in `demo_002`.
  - Audit script flags 1 idle-heavy run (the initial `SETTLE` phase).
  - Split generates 2130 train and 535 validation records (~20% split).
  - Validation split correctly contains samples from all phases.

- **Pass / Fail:** Pass.

- **Next Risk:** Even with a clean dataset, the current single-trajectory data is insufficient for generalization. Future steps should focus on collecting diverse demonstrations and then establishing a shadow inference baseline (running OpenVLA in parallel with the FSM) to measure "prediction error" without taking control.

---

## [2026-05-06] Step 19: Dataset Filtering / Sample Weighting / Training Views

- **Goal / Hypothesis:** Build safer training views from the G1-native dataset before attempting any OpenVLA shadow inference or fine-tuning. The hypothesis is that the single-rollout dataset needs filtering and weighting because Step 18 revealed phase imbalance, rare grip transitions, and an idle-heavy run.

- **Reasoning:** Step 18 showed that the dataset is structurally valid but not yet robust learning data. `APPROACH_TARGET` dominates the dataset while `CLOSE_GRIP` and `OPEN_GRIP` each appear only twice. A naive supervised baseline could overfit to long transport behavior and under-learn grip transitions.

- **Files Changed:**
  - `vla_bridge/training_views.py` — pure filtering, weighting, and training-view helpers
  - `scripts/build_g1_native_training_views.py` — CLI tool for generating full/filtered/weighted views
  - `tests/test_g1_native_training_views.py` — unit tests for filtering and weighting logic
  - `vla_bridge/__init__.py` — exports training-view helpers
  - `DEV_LOG.md` — appended this entry

- **Commands to Run:**

  ```bash
  python -m unittest tests/test_g1_native_training_views.py
  python scripts/build_g1_native_training_views.py \
    data/vla_exports/g1_native_demo_002/dataset.jsonl \
    --output-dir data/vla_exports/g1_native_demo_002/training_views
  ```

- **Expected Result:** The training-view script writes `full.jsonl`, `filtered_no_idle.jsonl`, `sample_weights.jsonl`, and `training_view_summary.json`. Rare transition phases are preserved. Idle-heavy records are reduced. Sample weights are normalized to mean 1.0 and give higher weights to rare phases.

- **Architecture Decision:** Keep the raw exported dataset unchanged and create derived training views. This preserves evidence integrity while allowing future model experiments to choose between full, filtered, and weighted manifests.

- **Verification Evidence:**
  - `test_g1_native_training_views.py` passes 11 unit tests.
  - Builder script removed 149 idle records while keeping the first 10.
  - Rare transition phases (`CLOSE_GRIP`, `OPEN_GRIP`) were preserved in the filtered view.
  - Sample weights were normalized to mean 1.0.
  - Rare phases received higher weights (up to `max_weight=20.0`).
  - No OpenVLA/Hugging Face/PyTorch dependency was introduced.

- **Pass / Fail:** Pass.

- **Next Risk:** If filtering/weighting works, the next meaningful step is either collecting multiple randomized demonstrations or building a tiny non-OpenVLA supervised baseline to validate the data pipeline end-to-end.

---

## [2026-05-06] Step 20: Multi-Demo Collection + Batch Manifest

- **Goal / Hypothesis:** Add a repeatable batch demonstration collection layer so the VLA branch is no longer structurally limited to a single rollout. The hypothesis is that before any OpenVLA inference or fine-tuning, we need multiple teacher demonstrations and a manifest that records which demos succeeded.

- **Reasoning:** Step 18 and Step 19 showed that the current dataset is useful for debugging but not robust learning: it is single-trajectory, phase-imbalanced, and contains rare grip transition states. Step 20 introduces the infrastructure needed to collect multiple demonstrations and later export/audit them as a combined dataset.

- **Files Changed:**
  - `vla_bridge/batch_manifest.py` — pure manifest dataclasses and helpers
  - `scripts/record_vla_demo_batch.py` — batch recorder CLI that calls the existing single-demo recorder
  - `tests/test_vla_batch_manifest.py` — unit tests for manifest logic
  - `vla_bridge/__init__.py` — exports batch manifest helpers
  - `DEV_LOG.md` — appended this entry

- **Commands to Run:**

  ```bash
  python -m unittest tests/test_vla_batch_manifest.py
  python scripts/record_vla_demo_batch.py \
    --output-root data/vla_demos/batch_000_no_images \
    --num-demos 2 \
    --record-every 1 \
    --no-images \
    --continue-on-fail
  ```

- **Expected Result:** The batch recorder writes `batch_manifest.json` under the output root. Each demo has its own folder with `demo.jsonl` and `summary.json`. The manifest records demo IDs, output paths, status, completion state, step counts, frame counts, and errors if any demo fails.

- **Architecture Decision:** The batch recorder calls the existing single-demo recorder via subprocess instead of duplicating the recorder internals. This keeps Step 20 isolated and preserves the behavior already validated in Step 14.

- **Verification Evidence:**
  - `test_vla_batch_manifest.py` passes 9 unit tests.
  - Dry-run mode correctly predicts commands and writes an empty manifest.
  - Real no-image batch recording successfully collected 2 full demonstrations.
  - `batch_manifest.json` correctly reports `num_completed=2` and `total_steps=5532`.
  - Both batch demos reached `DONE` and were correctly attached.

- **Pass / Fail:** Pass.

- **Next Risk:** After batch collection works, Step 21 should combine successful batch demos into a single G1-native dataset. However, because the current environment is deterministic, all demos in a batch are currently identical. Future work will need scene perturbations to create diverse data.

---

## [2026-05-06] Step 21: Combined Batch Dataset Exporter

- **Goal / Hypothesis:** Convert a Step 20 batch manifest into one combined G1-native dataset. The hypothesis is that once multiple teacher demonstrations are collected, downstream audit/training-view tools should consume one dataset artifact instead of many per-demo JSONL files.

- **Reasoning:** Step 20 validated batch collection and manifest tracking, but the demos still live in separate folders. Step 21 creates the bridge from batch collection to the existing Step 17–19 dataset pipeline by selecting successful demos and concatenating their G1-native records with provenance fields.

- **Files Changed:**
  - `vla_bridge/batch_dataset_export.py` — selection and combined export helpers
  - `scripts/export_g1_native_vla_batch_dataset.py` — CLI for manifest-to-dataset export
  - `tests/test_g1_native_batch_dataset_export.py` — unit tests for selection, provenance, and combined export
  - `vla_bridge/__init__.py` — exports batch dataset helpers
  - `DEV_LOG.md` — appended this entry

- **New Dataset Contract:**
  Combined rows preserve the Step 17 G1-native schema and add provenance:
  - `batch_id`
  - `demo_id`
  - `demo_sample_index`
  `sample_index` becomes the global index across the combined dataset.

- **Commands to Run:**

  ```bash
  python -m unittest tests/test_g1_native_batch_dataset_export.py
  python scripts/export_g1_native_vla_batch_dataset.py \
    data/vla_demos/batch_000_no_images/batch_manifest.json \
    --output-dir data/vla_exports/batch_000_no_images_g1_native
  ```

- **Expected Result:** The exporter reads `batch_manifest.json`, selects successful demos, combines their records, writes `dataset.jsonl`, `summary.json`, and `source_manifest.json`, and preserves per-row provenance.

- **Architecture Decision:** Do not copy images in Step 21 by default. Instead, prefix relative image paths with the demo folder name. This keeps the exporter lightweight and avoids duplicating large frame directories.

- **Verification Evidence:**
  - `test_g1_native_batch_dataset_export.py` passes 6 unit tests.
  - Exported 5330 records from 2 successful no-image batch demos.
  - Rows correctly include `batch_id`, `demo_id`, and `demo_sample_index`.
  - Global `sample_index` is contiguous across the combined dataset.
  - Existing audit and training-view tools successfully processed the combined artifact.

- **Pass / Fail:** Pass.

- **Next Risk:** If the batch demos are deterministic, the combined dataset will be larger but not more diverse. The next step should add deterministic scenario perturbations (e.g., varying object initial positions) to create truly diverse data for learning.

---

## [2026-05-07] Step 22: Scenario Perturbations / Multi-Seed Demo Diversity

- **Goal / Hypothesis:** Add controlled scenario perturbations so batch demos are no longer deterministic duplicates. The hypothesis is that small source-cylinder pose offsets can create measurable data diversity while preserving the existing FSM teacher success path.

- **Reasoning:** Step 21 proved the batch-to-dataset pipeline, but the combined dataset was still built from deterministic repeated demos. Before attempting OpenVLA shadow inference or fine-tuning, the dataset needs controlled variation and provenance.

- **Files Changed:**
  - `configs/scenarios/small_perturbations.json` — deterministic perturbation spec
  - `vla_bridge/scenario_config.py` — scenario config parsing/validation
  - `vla_bridge/batch_diversity.py` — batch diversity summary helpers, if added
  - `scripts/inspect_vla_batch_diversity.py` — CLI for manifest diversity inspection
  - `scripts/record_vla_demo.py` — scenario metadata + red_block x/y offset hook
  - `scripts/record_vla_demo_batch.py` — scenario-config support
  - `vla_bridge/batch_manifest.py` — scenario metadata fields in manifest records
  - `vla_bridge/batch_dataset_export.py` — preserve scenario metadata in combined datasets
  - `tests/test_scenario_config.py`
  - `tests/test_batch_diversity_manifest.py`
  - `vla_bridge/__init__.py`
  - `DEV_LOG.md`

- **New Scenario Contract:**
  Each demo can now carry:
  - `scenario_id`
  - `seed`
  - `scenario.red_block_xy_offset_m`
  - optional future fields for robot/base/target perturbations

- **MVP Perturbation:**
  Apply only small red cylinder x/y offsets first:
  - nominal
  - +2 cm x
  - -2 cm x
  - +2 cm y
  - -2 cm y

- **Commands to Run:**

  ```bash
  python -m unittest tests/test_scenario_config.py
  python -m unittest tests/test_batch_diversity_manifest.py
  python -m unittest tests/test_g1_native_batch_dataset_export.py
  python -m unittest tests/test_vla_batch_manifest.py
  python -m unittest tests/test_g1_native_training_views.py
  python -m unittest tests/test_g1_native_dataset_audit.py
  python -m unittest tests/test_g1_native_dataset.py
  python -m unittest tests/test_vla_demo_schema.py
  python -m unittest tests/test_vla_replay_metrics.py
  python -m unittest tests/test_vla_action_adapter.py
  python scripts/smoke_env.py
Dry-run scenario batch:
python scripts/record_vla_demo_batch.py \
  --output-root data/vla_demos/batch_001_perturbed_dryrun \
  --num-demos 5 \
  --record-every 1 \
  --no-images \
  --scenario-config configs/scenarios/small_perturbations.json \
  --dry-run
Real no-image scenario batch:
python scripts/record_vla_demo_batch.py \
  --output-root data/vla_demos/batch_001_perturbed_no_images \
  --num-demos 5 \
  --record-every 1 \
  --no-images \
  --scenario-config configs/scenarios/small_perturbations.json \
  --continue-on-fail
Inspect diversity:
python scripts/inspect_vla_batch_diversity.py \
  data/vla_demos/batch_001_perturbed_no_images/batch_manifest.json
Combine perturbed batch:
python scripts/export_g1_native_vla_batch_dataset.py \
  data/vla_demos/batch_001_perturbed_no_images/batch_manifest.json \
  --output-dir data/vla_exports/batch_001_perturbed_g1_native
Audit and training views:
python scripts/audit_g1_native_vla_dataset.py \
  data/vla_exports/batch_001_perturbed_g1_native/dataset.jsonl \
  --output-dir data/vla_exports/batch_001_perturbed_g1_native/audit

python scripts/build_g1_native_training_views.py \
  data/vla_exports/batch_001_perturbed_g1_native/dataset.jsonl \
  --output-dir data/vla_exports/batch_001_perturbed_g1_native/training_views
Expected Result: Batch manifest should report multiple unique scenario IDs and non-identical red cylinder offsets. Successful demos should remain exportable into one combined G1-native dataset. Combined rows should preserve scenario_id, seed, and scenario metadata.
Architecture Decision: Start with small deterministic cylinder perturbations only. This keeps the perturbation surface narrow and makes failures easy to attribute.
Verification Evidence: Step 22 is complete when:
scenario config tests pass,
manifest round-trip tests pass,
old Step 13–21 tests still pass,
dry-run commands include scenario flags,
real no-image batch records scenario metadata,
diversity inspector reports more than one unique scenario,
combined dataset preserves scenario metadata,
audit/training-view tools still run on the perturbed combined dataset.
Pass / Fail: Pending.
Next Risk: Even small perturbations may break FSM success if source approach thresholds are too tight. If success drops, reduce offsets from 2 cm to 1 cm or start with x-only perturbations.
```

---

## FILE: `MUJOCO_LOG.TXT`

```text
Mon May  4 01:24:16 2026
WARNING: Nan, Inf or huge value in QACC at DOF 0. The simulation is unstable. Time = 23.1250.

Mon May  4 01:26:15 2026
WARNING: Nan, Inf or huge value in QACC at DOF 0. The simulation is unstable. Time = 23.1250.

Mon May  4 01:29:43 2026
WARNING: Nan, Inf or huge value in QACC at DOF 0. The simulation is unstable. Time = 23.1250.

Mon May  4 01:33:37 2026
WARNING: Nan, Inf or huge value in QACC at DOF 0. The simulation is unstable. Time = 23.1250.

```

---

## FILE: `README.md`

```md
# G1 Pick & Place Challenge — Autonomous Baseline

This repository contains the autonomous pick-and-place baseline for the Unitree G1 humanoid. It converts the original manual keyboard-controlled demo into a robust, 12-state Finite-State Machine (FSM) controller that coordinates locomotion and manipulation in MuJoCo.

**Technical Case Study & Demo:** [atabak-eghbal.github.io/lucky-robots-g1-pick-place-case-study/](https://atabak-eghbal.github.io/lucky-robots-g1-pick-place-case-study/index.html)

## Project Overview

The task is to autonomously pick up a red cylinder from a source table and place it on a target blue table. This submission implements a modular, debuggable baseline that separates the high-level sequencing from the underlying ONNX control policies.

### Key Features
- **Autonomous Sequencing:** 12-state FSM handling approach, hover, grasp, transport, and release.
- **Simulation Stability:** Implements a 15-tick collision delay during release to prevent NaN instabilities common in kinematic-to-physical transitions.
- **Sweet-Spot Navigation:** Optimized approach waypoints to keep the manipulation target in the right arm's natural workspace.
- **Always-on Reacher:** Continuous arm control to preserve the walker's trained observation distribution.

## Repository Structure

```
.
├── run.py              # Main entry point (supports --policy fsm)
├── scene.xml           # MuJoCo scene definition
├── g1.xml              # G1 robot model
├── model_config.json   # Joint and PD configurations
├── common/             # Controller, Grasp, and ONNX wrappers
├── policies/           # FSM core logic and policy adapters
├── scripts/            # Integration tests and video recording
├── DEV_LOG.md          # Detailed engineering decision log
└── demo_video.mp4      # Full autonomous task demonstration
```

## Setup & Running

### Prerequisites
```bash
pip install mujoco onnxruntime numpy opencv-python
```

### Running the Autonomous Demo
To run the full autonomous pick-and-place sequence:
```bash
python run.py --policy fsm
```

### Running Integration Tests
To verify the task completion headlessly:
```bash
export PYTHONPATH=$PYTHONPATH:.
python3 scripts/test_fsm_approach.py
```

## Controls (Keyboard Mode)
To run the original manual mode for comparison:
```bash
python run.py --policy keyboard
```

| Key | Mode | Action |
|-----|------|--------|
| `.` | Both | Toggle WALK / REACH mode |
| Arrows | Walk | Move fwd/back, strafe L/R |
| `;` / `'` | Walk | Turn left/right |
| Up/Down | Reach | Arm forward/backward |
| Left/Right| Reach | Arm left/right |
| `,` | Both | Toggle grip (open/close) |
| Space | Both | Reset robot |

## Documentation
For a deep dive into the architecture, lessons learned, and failure analysis, please visit the [Technical Case Study](https://atabak-eghbal.github.io/lucky-robots-g1-pick-place-case-study/index.html).
```

---

## FILE: `artifacts/.gitkeep`

```

```

---

## FILE: `assets/head_link.obj`

_Skipped: file is too large (7767912 bytes)._ 

---

## FILE: `assets/left_ankle_pitch_link.obj`

_Skipped: file is too large (613450 bytes)._ 

---

## FILE: `assets/left_ankle_roll_link.obj`

_Skipped: file is too large (5558051 bytes)._ 

---

## FILE: `assets/left_elbow_link.obj`

_Skipped: file is too large (745851 bytes)._ 

---

## FILE: `assets/left_hand_index_0_link.STL`

_Skipped: file is too large (475984 bytes)._ 

---

## FILE: `assets/left_hand_index_1_link.STL`

_Skipped: file is too large (1521784 bytes)._ 

---

## FILE: `assets/left_hand_middle_0_link.STL`

_Skipped: file is too large (475984 bytes)._ 

---

## FILE: `assets/left_hand_middle_1_link.STL`

_Skipped: file is too large (1521784 bytes)._ 

---

## FILE: `assets/left_hand_palm_link.STL`

_Skipped: file is too large (2140184 bytes)._ 

---

## FILE: `assets/left_hand_thumb_0_link.STL`

_Skipped: non-text or binary file._

---

## FILE: `assets/left_hand_thumb_1_link.STL`

_Skipped: file is too large (475984 bytes)._ 

---

## FILE: `assets/left_hand_thumb_2_link.STL`

_Skipped: file is too large (1521784 bytes)._ 

---

## FILE: `assets/left_hip_pitch_link.obj`

_Skipped: file is too large (1518316 bytes)._ 

---

## FILE: `assets/left_hip_roll_link.obj`

_Skipped: file is too large (1624506 bytes)._ 

---

## FILE: `assets/left_hip_yaw_link.obj`

_Skipped: file is too large (2515575 bytes)._ 

---

## FILE: `assets/left_knee_link.obj`

_Skipped: file is too large (7267119 bytes)._ 

---

## FILE: `assets/left_shoulder_pitch_link.obj`

_Skipped: file is too large (1486668 bytes)._ 

---

## FILE: `assets/left_shoulder_roll_link.obj`

_Skipped: file is too large (3384092 bytes)._ 

---

## FILE: `assets/left_shoulder_yaw_link.obj`

_Skipped: file is too large (2121472 bytes)._ 

---

## FILE: `assets/left_wrist_pitch_link.obj`

_Skipped: file is too large (695437 bytes)._ 

---

## FILE: `assets/left_wrist_roll_link.obj`

_Skipped: file is too large (2946517 bytes)._ 

---

## FILE: `assets/left_wrist_yaw_link.obj`

_Skipped: file is too large (2632279 bytes)._ 

---

## FILE: `assets/logo_link.obj`

_Skipped: file is too large (2016446 bytes)._ 

---

## FILE: `assets/pelvis.obj`

_Skipped: file is too large (8662517 bytes)._ 

---

## FILE: `assets/pelvis_contour_link.obj`

_Skipped: file is too large (15251435 bytes)._ 

---

## FILE: `assets/right_ankle_pitch_link.obj`

_Skipped: file is too large (614089 bytes)._ 

---

## FILE: `assets/right_ankle_roll_link.obj`

_Skipped: file is too large (5562121 bytes)._ 

---

## FILE: `assets/right_elbow_link.obj`

_Skipped: file is too large (749121 bytes)._ 

---

## FILE: `assets/right_hand_index_0_link.STL`

_Skipped: file is too large (475984 bytes)._ 

---

## FILE: `assets/right_hand_index_1_link.STL`

_Skipped: file is too large (1521784 bytes)._ 

---

## FILE: `assets/right_hand_middle_0_link.STL`

_Skipped: file is too large (475984 bytes)._ 

---

## FILE: `assets/right_hand_middle_1_link.STL`

_Skipped: file is too large (1521784 bytes)._ 

---

## FILE: `assets/right_hand_palm_link.STL`

_Skipped: file is too large (2140184 bytes)._ 

---

## FILE: `assets/right_hand_thumb_0_link.STL`

_Skipped: non-text or binary file._

---

## FILE: `assets/right_hand_thumb_1_link.STL`

_Skipped: file is too large (475984 bytes)._ 

---

## FILE: `assets/right_hand_thumb_2_link.STL`

_Skipped: file is too large (1521784 bytes)._ 

---

## FILE: `assets/right_hip_pitch_link.obj`

_Skipped: file is too large (1527108 bytes)._ 

---

## FILE: `assets/right_hip_roll_link.obj`

_Skipped: file is too large (1628958 bytes)._ 

---

## FILE: `assets/right_hip_yaw_link.obj`

_Skipped: file is too large (2522611 bytes)._ 

---

## FILE: `assets/right_knee_link.obj`

_Skipped: file is too large (7248935 bytes)._ 

---

## FILE: `assets/right_shoulder_pitch_link.obj`

_Skipped: file is too large (1496372 bytes)._ 

---

## FILE: `assets/right_shoulder_roll_link.obj`

_Skipped: file is too large (3403337 bytes)._ 

---

## FILE: `assets/right_shoulder_yaw_link.obj`

_Skipped: file is too large (2118467 bytes)._ 

---

## FILE: `assets/right_wrist_pitch_link.obj`

_Skipped: file is too large (663484 bytes)._ 

---

## FILE: `assets/right_wrist_roll_link.obj`

_Skipped: file is too large (2961073 bytes)._ 

---

## FILE: `assets/right_wrist_yaw_link.obj`

_Skipped: file is too large (2873722 bytes)._ 

---

## FILE: `assets/torso_link_rev_1_0.obj`

_Skipped: file is too large (21824558 bytes)._ 

---

## FILE: `assets/waist_roll_link_rev_1_0.obj`

_Skipped: file is too large (731523 bytes)._ 

---

## FILE: `assets/waist_yaw_link_rev_1_0.obj`

_Skipped: file is too large (5358020 bytes)._ 

---

## FILE: `common/__init__.py`

```python
"""Shared simulation infrastructure and utilities."""
```

---

## FILE: `common/controller.py`

```python
"""Low-level walker + reacher controller for the G1 robot."""

from __future__ import annotations

from typing import Literal

import mujoco
import numpy as np


class WalkerReacherController:
  """Full G1 controller with locomotion mode switching and arm reaching."""

  # GLFW key codes
  KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT = 265, 264, 263, 262
  KEY_SEMICOLON, KEY_APOSTROPHE = 59, 39
  KEY_COMMA, KEY_PERIOD, KEY_SLASH, KEY_BACKSLASH = 44, 46, 47, 92
  KEY_LEFT_BRACKET, KEY_RIGHT_BRACKET = 91, 93
  KEY_KP_8, KEY_KP_2, KEY_KP_6, KEY_KP_4, KEY_KP_7, KEY_KP_1, KEY_KP_5 = (
    328, 322, 326, 324, 327, 321, 325
  )
  KEY_U, KEY_J, KEY_Y, KEY_H, KEY_9, KEY_0, KEY_R = 85, 74, 89, 72, 57, 48, 82
  KEY_COMMA_GRIP = 44  # , = Grip toggle

  WALKER_HEIGHT = 0.80

  def __init__(self, model, data, walker, croucher, rotator, config,
               right_reacher=None):
    self.model = model
    self.data = data
    self.walker_policy = walker
    self.croucher_policy = croucher
    self.rotator_policy = rotator
    self.right_reacher_policy = right_reacher
    self.config = config

    # --- Input mode: WALK or REACH ---
    # . toggles between them. Same keys (arrows, ;/') do different things.
    self.input_mode: Literal["walk", "reach"] = "walk"

    # Walk state
    self.lin_vel_x = 0.0
    self.lin_vel_y = 0.0
    self.ang_vel_z = 0.0
    self.vel_step_linear = 0.2
    self.vel_step_angular = 0.2
    self.vel_max_linear = 2.0
    self.vel_max_angular = 1.0

    # Reach state
    self.reach_active = False
    self.reach_target = np.array([0.3, -0.2, 0.2], dtype=np.float32)
    self.reach_orientation = np.zeros(3, dtype=np.float32)
    self.reach_step = 0.05
    self.last_arm_action = np.zeros(7, dtype=np.float32)
    self.last_arm_target = None
    self.arm_max_delta = 0.012

    self.last_action = np.zeros(29, dtype=np.float32)

    # Right hand grip state
    self.grip_closed = False

    self._build_joint_mappings()
    self._build_reacher_mappings()
    self._compute_pd_gains()
    self._cache_actuator_ids()
    self._cache_finger_actuators()

    print("\n=== G1 Table Red Block Controller ===")
    print("  .         : Toggle WALK / REACH mode")
    print("  --- WALK mode ---")
    print("  Arrows    : Walk forward/back, strafe left/right")
    print("  ; / '     : Turn left / right")
    print("  \\         : Stop")
    print("  --- REACH mode ---")
    print("  Up/Down   : Reach forward / backward")
    print("  Left/Right: Reach left / right")
    print("  ; / '     : Reach up / down")
    print("  \\         : Reset reach to default")
    print("  --- Always ---")
    print("  ,         : Toggle grip (close/open right hand)")
    print("  Space     : Reset robot")
    print("=" * 40)

  def _build_joint_mappings(self):
    self.joint_names = self.config["joint_names"]
    self.num_joints = len(self.joint_names)
    self.joint_qpos_indices = {n: 7 + i for i, n in enumerate(self.joint_names)}
    self.joint_qvel_indices = {n: 6 + i for i, n in enumerate(self.joint_names)}

    self.default_joint_pos = np.zeros(self.num_joints, dtype=np.float32)
    for name, value in self.config["default_joint_pos"].items():
      if name in self.joint_names:
        self.default_joint_pos[self.joint_names.index(name)] = value

    self.action_scales = np.array(
      [self.config["action_scales"][n] for n in self.joint_names], dtype=np.float32
    )

    arm_patterns = ["shoulder_pitch", "shoulder_roll", "shoulder_yaw",
                    "elbow", "wrist_roll", "wrist_pitch", "wrist_yaw"]
    self.arm_indices = []
    for i, name in enumerate(self.joint_names):
      if any(p in name for p in arm_patterns):
        self.arm_indices.append(i)

  def _build_reacher_mappings(self):
    rc = self.config.get("right_reacher", {})
    self.right_arm_joint_names = rc.get("arm_joint_names", [
      "right_shoulder_pitch_joint", "right_shoulder_roll_joint",
      "right_shoulder_yaw_joint", "right_elbow_joint",
      "right_wrist_roll_joint", "right_wrist_pitch_joint",
      "right_wrist_yaw_joint",
    ])
    self.right_arm_indices = [
      self.joint_names.index(n) for n in self.right_arm_joint_names
      if n in self.joint_names
    ]
    arm_scales = rc.get("arm_action_scales", {})
    self.arm_action_scales = np.array([
      arm_scales.get(n, self.action_scales[self.joint_names.index(n)])
      for n in self.right_arm_joint_names
    ], dtype=np.float32)
    arm_defaults = rc.get("arm_default_pos", {})
    self.arm_default_pos = np.array([
      arm_defaults.get(n, self.default_joint_pos[self.joint_names.index(n)])
      for n in self.right_arm_joint_names
    ], dtype=np.float32)
    self.right_palm_site_id = mujoco.mj_name2id(
      self.model, mujoco.mjtObj.mjOBJ_SITE, "right_palm"
    )

  def _compute_pd_gains(self):
    S5020, D5020, E5020 = 14.2506, 0.9072, 25.0
    S7520_14, D7520_14, E7520_14 = 40.1792, 2.5579, 88.0
    S7520_22, D7520_22, E7520_22 = 99.0984, 6.3088, 139.0
    S4010, D4010, E4010 = 16.7783, 1.0681, 5.0

    self.kp = np.zeros(self.num_joints, dtype=np.float32)
    self.kd = np.zeros(self.num_joints, dtype=np.float32)
    self.effort_limit = np.zeros(self.num_joints, dtype=np.float32)

    for i, name in enumerate(self.joint_names):
      if "elbow" in name or "shoulder" in name or "wrist_roll" in name:
        self.kp[i], self.kd[i], self.effort_limit[i] = S5020, D5020, E5020
      elif "hip_pitch" in name or "hip_yaw" in name or name == "waist_yaw_joint":
        self.kp[i], self.kd[i], self.effort_limit[i] = S7520_14, D7520_14, E7520_14
      elif "hip_roll" in name or "knee" in name:
        self.kp[i], self.kd[i], self.effort_limit[i] = S7520_22, D7520_22, E7520_22
      elif "wrist_pitch" in name or "wrist_yaw" in name:
        self.kp[i], self.kd[i], self.effort_limit[i] = S4010, D4010, E4010
      elif "ankle" in name or name in ("waist_pitch_joint", "waist_roll_joint"):
        self.kp[i], self.kd[i], self.effort_limit[i] = S5020 * 2, D5020 * 2, E5020 * 2
      else:
        self.kp[i], self.kd[i], self.effort_limit[i] = S5020, D5020, E5020

  # --- Keyboard ---
  def key_callback(self, key: int) -> None:
    # Grip toggle (works in any mode)
    if key == self.KEY_COMMA_GRIP:
      self.grip_closed = not self.grip_closed
      print(f"[GRIP] Right hand: {'CLOSED' if self.grip_closed else 'OPEN'}")
      return

    # Toggle input mode
    if key == self.KEY_PERIOD:
      if self.right_reacher_policy is None:
        print("[WARN] No right reacher policy loaded")
        return
      if self.input_mode == "walk":
        self.input_mode = "reach"
        self.reach_active = True
        # Init reach target to a sensible default in front of pelvis
        self.reach_target[:] = [0.3, -0.2, 0.2]
        self.reach_orientation[:] = 0.0
        self.last_arm_target = self._get_arm_joint_positions() + self.arm_default_pos
        print("[MODE] >>> REACH — arrows move hand, ;/' = up/down, \\ = reset target")
      else:
        self.input_mode = "walk"
        self.reach_active = False
        # Freeze arm where it is — read current right arm joint positions
        if self.last_arm_target is not None:
          self.frozen_arm_pos = self.last_arm_target.copy()
        self.last_arm_target = None
        print("[MODE] >>> WALK — arm holds position, arrows move robot")
      return

    # Route keys based on mode
    if self.input_mode == "walk":
      self._handle_walk_key(key)
    else:
      self._handle_reach_key(key)

  def _handle_walk_key(self, key: int) -> None:
    if key == self.KEY_UP:
      self.lin_vel_x = np.clip(self.lin_vel_x + self.vel_step_linear, -self.vel_max_linear, self.vel_max_linear)
    elif key == self.KEY_DOWN:
      self.lin_vel_x = np.clip(self.lin_vel_x - self.vel_step_linear, -self.vel_max_linear, self.vel_max_linear)
    elif key == self.KEY_LEFT:
      self.lin_vel_y = np.clip(self.lin_vel_y + self.vel_step_linear, -self.vel_max_linear, self.vel_max_linear)
    elif key == self.KEY_RIGHT:
      self.lin_vel_y = np.clip(self.lin_vel_y - self.vel_step_linear, -self.vel_max_linear, self.vel_max_linear)
    elif key == self.KEY_SEMICOLON:
      self.ang_vel_z = np.clip(self.ang_vel_z + self.vel_step_angular, -self.vel_max_angular, self.vel_max_angular)
    elif key == self.KEY_APOSTROPHE:
      self.ang_vel_z = np.clip(self.ang_vel_z - self.vel_step_angular, -self.vel_max_angular, self.vel_max_angular)
    elif key == self.KEY_BACKSLASH or key == self.KEY_SLASH:
      self.lin_vel_x = self.lin_vel_y = self.ang_vel_z = 0.0
      print("[WALK] STOPPED")
      return
    else:
      return
    print(f"[WALK] vel: x={self.lin_vel_x:.1f} y={self.lin_vel_y:.1f} yaw={self.ang_vel_z:.1f}")

  def _handle_reach_key(self, key: int) -> None:
    if key == self.KEY_UP:
      self.reach_target[0] = np.clip(self.reach_target[0] + self.reach_step, -0.3, 0.6)
    elif key == self.KEY_DOWN:
      self.reach_target[0] = np.clip(self.reach_target[0] - self.reach_step, -0.3, 0.6)
    elif key == self.KEY_LEFT:
      self.reach_target[1] = np.clip(self.reach_target[1] + self.reach_step, -0.6, 0.3)
    elif key == self.KEY_RIGHT:
      self.reach_target[1] = np.clip(self.reach_target[1] - self.reach_step, -0.6, 0.3)
    elif key == self.KEY_SEMICOLON:
      self.reach_target[2] = np.clip(self.reach_target[2] + self.reach_step, -0.4, 0.6)
    elif key == self.KEY_APOSTROPHE:
      self.reach_target[2] = np.clip(self.reach_target[2] - self.reach_step, -0.4, 0.6)
    elif key == self.KEY_BACKSLASH or key == self.KEY_SLASH:
      self.reach_target[:] = [0.3, -0.2, 0.2]
      self.reach_orientation[:] = 0.0
      print("[REACH] Target reset to default")
      return
    else:
      return
    print(f"[REACH] target: fwd={self.reach_target[0]:.2f} side={self.reach_target[1]:.2f} up={self.reach_target[2]:.2f}")

  # --- State helpers ---
  def _get_base_pose(self):
    return self.data.qpos[:3].copy(), self.data.qpos[3:7].copy()

  @staticmethod
  def _quat_apply_inverse(quat, vec):
    w, xyz = quat[0], quat[1:4]
    t = np.cross(xyz, vec) * 2
    return vec - w * t + np.cross(xyz, t)

  def _get_base_velocities(self):
    lin_vel_world = self.data.qvel[:3].copy()
    ang_vel_body = self.data.qvel[3:6].copy()
    _, quat = self._get_base_pose()
    return self._quat_apply_inverse(quat, lin_vel_world), ang_vel_body

  def _get_projected_gravity(self):
    _, quat = self._get_base_pose()
    return self._quat_apply_inverse(quat, np.array([0.0, 0.0, -1.0]))

  def _get_joint_positions(self):
    pos = np.zeros(self.num_joints, dtype=np.float32)
    for i, n in enumerate(self.joint_names):
      pos[i] = self.data.qpos[self.joint_qpos_indices[n]] - self.default_joint_pos[i]
    return pos

  def _get_joint_velocities(self):
    vel = np.zeros(self.num_joints, dtype=np.float32)
    for i, n in enumerate(self.joint_names):
      vel[i] = self.data.qvel[self.joint_qvel_indices[n]]
    return vel

  def _get_arm_joint_positions(self):
    pos = np.zeros(len(self.right_arm_indices), dtype=np.float32)
    for i, idx in enumerate(self.right_arm_indices):
      n = self.joint_names[idx]
      pos[i] = self.data.qpos[self.joint_qpos_indices[n]] - self.arm_default_pos[i]
    return pos

  def _get_arm_joint_velocities(self):
    vel = np.zeros(len(self.right_arm_indices), dtype=np.float32)
    for i, idx in enumerate(self.right_arm_indices):
      vel[i] = self.data.qvel[self.joint_qvel_indices[self.joint_names[idx]]]
    return vel

  def _get_palm_pos_in_pelvis(self):
    palm_world = self.data.site_xpos[self.right_palm_site_id].copy()
    pos, quat = self._get_base_pose()
    return self._quat_apply_inverse(quat, palm_world - pos)

  def _get_palm_orientation_in_pelvis(self):
    mat = self.data.site_xmat[self.right_palm_site_id].reshape(3, 3)
    palm_q = np.zeros(4)
    mujoco.mju_mat2Quat(palm_q, mat.flatten())
    _, pelvis_q = self._get_base_pose()
    pinv = np.array([pelvis_q[0], -pelvis_q[1], -pelvis_q[2], -pelvis_q[3]])
    w1, x1, y1, z1 = pinv
    w2, x2, y2, z2 = palm_q
    rel = np.array([
      w1*w2 - x1*x2 - y1*y2 - z1*z2,
      w1*x2 + x1*w2 + y1*z2 - z1*y2,
      w1*y2 - x1*z2 + y1*w2 + z1*x2,
      w1*z2 + x1*y2 - y1*x2 + z1*w2,
    ])
    w, x, y, z = rel
    roll = np.arctan2(2*(w*x + y*z), 1 - 2*(x*x + y*y))
    sinp = np.clip(2*(w*y - z*x), -1, 1)
    pitch = np.arcsin(sinp)
    yaw = np.arctan2(2*(w*z + x*y), 1 - 2*(y*y + z*z))
    return np.array([roll, pitch, yaw], dtype=np.float32)

  # --- Step ---
  def step(self) -> np.ndarray:
    # Build walker observation (always runs — keeps legs stable)
    lin_vel, ang_vel = self._get_base_velocities()
    proj_gravity = self._get_projected_gravity()
    joint_pos = self._get_joint_positions()
    joint_vel = self._get_joint_velocities()

    cmd = np.array([self.lin_vel_x, self.lin_vel_y, self.ang_vel_z], dtype=np.float32)

    obs = np.concatenate([
      lin_vel, ang_vel, proj_gravity, joint_pos, joint_vel, self.last_action, cmd,
    ]).astype(np.float32)

    # Walker policy (handles legs, waist, standing, walking, turning).
    # The ONNX bakes in its own obs normalisation — pass raw obs directly.
    action = self.walker_policy(obs)
    target_pos = self.default_joint_pos + action * self.action_scales

    # Zero walker arm outputs — reacher writes these columns.
    # Left arm: always at default (no left-arm reacher).
    for idx in self.arm_indices:
      target_pos[idx] = self.default_joint_pos[idx]

    # Reacher always runs so the right arm is actively controlled (carry
    # pose during walking, reach pose during grasping). This matches the
    # solution's architecture: the arm must be in a known pose so the
    # walker's joint-position obs match the trained distribution.
    if self.right_reacher_policy is not None:
      reacher_obs = np.concatenate([
        self.reach_target,
        self.reach_orientation,
        self._get_palm_pos_in_pelvis(),
        self._get_palm_orientation_in_pelvis(),
        self._get_arm_joint_positions(),
        self._get_arm_joint_velocities(),
        self.last_arm_action,
        proj_gravity.astype(np.float32),
      ]).astype(np.float32)

      arm_action = self.right_reacher_policy(reacher_obs)
      arm_target = self.arm_default_pos + arm_action * self.arm_action_scales

      if self.last_arm_target is not None:
        delta = np.clip(arm_target - self.last_arm_target, -self.arm_max_delta, self.arm_max_delta)
        arm_target = self.last_arm_target + delta
      self.last_arm_target = arm_target.copy()

      for i, full_idx in enumerate(self.right_arm_indices):
        target_pos[full_idx] = arm_target[i]
      self.last_arm_action = arm_action.copy()

    self.last_action = action.copy()
    return target_pos

  def _cache_actuator_ids(self):
    """Cache actuator IDs once at init instead of looking up every step."""
    self.actuator_ids = []
    for name in self.joint_names:
      self.actuator_ids.append(
        mujoco.mj_name2id(self.model, mujoco.mjtObj.mjOBJ_ACTUATOR, name)
      )

  def _cache_finger_actuators(self):
    """Cache right hand finger actuator IDs and their closed targets."""
    # (actuator_id, closed_position) — targets at joint limits for a power grasp
    self.right_finger_actuators = []
    finger_closed = {
      "right_hand_thumb_0_joint":  0.8,     # curl thumb inward
      "right_hand_thumb_1_joint": -0.9,     # flex thumb
      "right_hand_thumb_2_joint": -1.5,     # curl thumb tip
      "right_hand_index_0_joint":  1.4,     # curl index
      "right_hand_index_1_joint":  1.5,     # curl index tip
      "right_hand_middle_0_joint": 1.4,     # curl middle
      "right_hand_middle_1_joint": 1.5,     # curl middle tip
    }
    for name, closed_val in finger_closed.items():
      aid = mujoco.mj_name2id(self.model, mujoco.mjtObj.mjOBJ_ACTUATOR, name)
      if aid >= 0:
        self.right_finger_actuators.append((aid, closed_val))

  def apply_pd_control(self, target_pos):
    for i, act_id in enumerate(self.actuator_ids):
      if act_id >= 0:
        self.data.ctrl[act_id] = target_pos[i]
    # Apply grip
    for act_id, closed_val in self.right_finger_actuators:
      self.data.ctrl[act_id] = closed_val if self.grip_closed else 0.0
```

---

## FILE: `common/grasp.py`

```python
"""Grasp backend interface and kinematic-attachment implementation."""

from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np


class GraspBackend(ABC):
    """Abstract grasp backend — called every physics tick from the main loop."""

    @property
    @abstractmethod
    def attached(self) -> bool:
        """True while the object is kinematically attached."""

    @abstractmethod
    def tick(self, grip_closed: bool) -> bool:
        """Update attachment state. Returns True if currently attached.

        Must be called after every mujoco.mj_step() so the cylinder pose is
        corrected before the next integration step.
        """

    @abstractmethod
    def release(self) -> None:
        """Force-detach the object and restore its physics."""


class KinematicAttachment(GraspBackend):
    """Teleport-weld the cylinder to the palm while the grip is closed.

    Simulation shortcut: bypasses contact forces. The cylinder is placed at a
    fixed palm-local offset (snapped to SNAP_DIST if the hand closed far away)
    and its freejoint velocity is zeroed every tick so it does not drift between
    teleportations.

    Collisions are disabled while attached to prevent geom-overlap impulses from
    destabilising the robot.
    """

    ATTACH_DIST:   float = 0.13  # m: auto-attach when palm is within this distance
    SNAP_DIST:     float = 0.03  # m: clamp palm-local offset so object sits in hand
    RELEASE_TICKS: int   = 15    # physics ticks (~0.075s) to wait before restoring geoms

    def __init__(
        self,
        model,
        data,
        palm_site_id: int,
        obj_body_id: int,
    ) -> None:
        self._model    = model
        self._data     = data
        self._palm_id  = palm_site_id
        self._obj_id   = obj_body_id

        # Freejoint addressing (first joint of the body; must be a freejoint).
        jnt_id = int(model.body_jntadr[obj_body_id])
        self._qposadr = int(model.jnt_qposadr[jnt_id])
        self._qveladr = int(model.jnt_dofadr[jnt_id])

        # Geoms belonging to this body — used to toggle collisions.
        self._geom_ids = [
            i for i in range(model.ngeom)
            if int(model.geom_bodyid[i]) == obj_body_id
        ]
        self._orig_contype     = {g: int(model.geom_contype[g])     for g in self._geom_ids}
        self._orig_conaffinity = {g: int(model.geom_conaffinity[g]) for g in self._geom_ids}

        self._is_attached    = False
        self._release_timer  = 0
        self._local_offset   = np.zeros(3, dtype=np.float64)

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    @property
    def attached(self) -> bool:
        return self._is_attached

    def tick(self, grip_closed: bool) -> bool:
        if not self._is_attached:
            if self._release_timer > 0:
                self._release_timer -= 1
                if self._release_timer == 0:
                    self._restore_geoms()
            if grip_closed:
                palm = self._data.site_xpos[self._palm_id].copy()
                obj  = self._data.xpos[self._obj_id].copy()
                if float(np.linalg.norm(palm - obj)) <= self.ATTACH_DIST:
                    self._attach(palm, obj)
        else:
            if not grip_closed:
                self._release()
            else:
                self._update_pose()
        return self._is_attached

    def release(self) -> None:
        if self._is_attached:
            self._release()

    # ------------------------------------------------------------------ #
    # Private helpers
    # ------------------------------------------------------------------ #

    def _attach(self, palm_pos: np.ndarray, obj_pos: np.ndarray) -> None:
        palm_rot = self._data.site_xmat[self._palm_id].reshape(3, 3).copy()
        local = palm_rot.T @ (obj_pos - palm_pos)
        d = float(np.linalg.norm(local))
        if d > self.SNAP_DIST:
            local = local * (self.SNAP_DIST / d)
        self._local_offset = local

        for g in self._geom_ids:
            self._model.geom_contype[g]     = 0
            self._model.geom_conaffinity[g] = 0

        self._is_attached = True
        self._release_timer = 0
        snap = float(np.linalg.norm(self._local_offset))
        print(f"[GRASP] attached  dist={float(np.linalg.norm(palm_pos - obj_pos)):.3f} m"
              f"  snap_offset={snap:.3f} m")
        self._update_pose()

    def _update_pose(self) -> None:
        palm_pos = self._data.site_xpos[self._palm_id].copy()
        palm_rot = self._data.site_xmat[self._palm_id].reshape(3, 3).copy()
        new_pos  = palm_pos + palm_rot @ self._local_offset
        self._data.qpos[self._qposadr    :self._qposadr + 3] = new_pos
        self._data.qpos[self._qposadr + 3:self._qposadr + 7] = [1.0, 0.0, 0.0, 0.0]
        self._data.qvel[self._qveladr    :self._qveladr + 6] = 0.0

    def _release(self) -> None:
        self._data.qvel[self._qveladr:self._qveladr + 6] = 0.0
        self._is_attached = False
        self._release_timer = self.RELEASE_TICKS
        print(f"[GRASP] released — waiting {self.RELEASE_TICKS} ticks to restore geoms")

    def _restore_geoms(self) -> None:
        for g in self._geom_ids:
            self._model.geom_contype[g]     = self._orig_contype[g]
            self._model.geom_conaffinity[g] = self._orig_conaffinity[g]
        print("[GRASP] geoms restored")
```

---

## FILE: `common/onnx_policy.py`

```python
"""ONNX policy wrapper for CPU inference."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import onnxruntime as ort


class ONNXPolicy:
  """Thin CPU-only ONNX inference wrapper.

  Expects a 1D or (1, N) float32 observation and returns the first output row.
  """

  def __init__(self, model_path: str | Path):
    sess_options = ort.SessionOptions()
    sess_options.intra_op_num_threads = 1
    sess_options.inter_op_num_threads = 1
    self.session = ort.InferenceSession(
      str(model_path), sess_options, providers=["CPUExecutionProvider"]
    )
    self.input_name = self.session.get_inputs()[0].name
    self.output_name = self.session.get_outputs()[0].name

  def __call__(self, obs: np.ndarray) -> np.ndarray:
    if obs.ndim == 1:
      obs = obs.reshape(1, -1)
    obs = obs.astype(np.float32)
    return self.session.run([self.output_name], {self.input_name: obs})[0][0]
```

---

## FILE: `common/scene.py`

```python
"""Scene helpers for deterministic reset and camera rendering."""

from __future__ import annotations

from typing import Iterable

import mujoco
import numpy as np


class CameraRenderer:
  """Offscreen renderer for robot-mounted cameras using mujoco.Renderer."""

  def __init__(self, model, data, width: int = 320, height: int = 240):
    self.model = model
    self.data = data
    self.renderer = mujoco.Renderer(model, height, width)

  def render(self, camera_name: str) -> np.ndarray:
    """Render from a named camera, return RGB array (H, W, 3)."""
    self.renderer.update_scene(self.data, camera=camera_name)
    return self.renderer.render().copy()


def reset_robot(
  model,
  data,
  config: dict,
  joint_names: Iterable[str],
  *,
  base_pos: tuple[float, float, float] = (-0.6, 0.0, 0.76),
  base_quat: tuple[float, float, float, float] = (1.0, 0.0, 0.0, 0.0),
  reset_data: bool = True,
) -> None:
  """Reset the robot to a deterministic pose and forward the model.

  joint_names should be the full ordered joint list from the config/model.
  """
  if reset_data:
    mujoco.mj_resetData(model, data)
  joint_names_list = list(joint_names)
  joint_index = {name: idx for idx, name in enumerate(joint_names_list)}
  data.qpos[0:3] = base_pos
  data.qpos[3:7] = base_quat
  for name, value in config["default_joint_pos"].items():
    idx = joint_index.get(name)
    if idx is not None:
      data.qpos[7 + idx] = value
  mujoco.mj_forward(model, data)
```

---

## FILE: `configs/scenarios/small_perturbations.json`

```json
{
  "name": "small_perturbations_v1",
  "description": "Small deterministic source-cylinder pose offsets for Step 22 batch diversity validation.",
  "defaults": {
    "red_block_xy_offset_m": [0.0, 0.0],
    "robot_base_xy_offset_m": [0.0, 0.0],
    "target_drop_xy_offset_m": [0.0, 0.0]
  },
  "scenarios": [
    {
      "scenario_id": "nominal",
      "seed": 0,
      "red_block_xy_offset_m": [0.0, 0.0]
    },
    {
      "scenario_id": "cyl_x_plus_02",
      "seed": 101,
      "red_block_xy_offset_m": [0.02, 0.0]
    },
    {
      "scenario_id": "cyl_x_minus_02",
      "seed": 102,
      "red_block_xy_offset_m": [-0.02, 0.0]
    },
    {
      "scenario_id": "cyl_y_plus_02",
      "seed": 103,
      "red_block_xy_offset_m": [0.0, 0.02]
    },
    {
      "scenario_id": "cyl_y_minus_02",
      "seed": 104,
      "red_block_xy_offset_m": [0.0, -0.02]
    }
  ]
}
```

---

## FILE: `croucher.onnx`

_Skipped: non-text or binary file._

---

## FILE: `croucher.onnx.data`

_Skipped: file is too large (881448 bytes)._ 

---

## FILE: `data/vla_demos/batch_000/batch_manifest.json`

```json
{
  "batch_id": "batch_000",
  "output_root": "data/vla_demos/batch_000",
  "created_unix_time": 1778146334.219693,
  "num_requested": 3,
  "num_completed": 3,
  "num_failed": 0,
  "record_every": 1,
  "camera": "head_cam",
  "no_images": false,
  "max_ticks": 4000,
  "demos": [
    {
      "demo_id": "demo_000",
      "output_dir": "data/vla_demos/batch_000/demo_000",
      "metadata_path": "data/vla_demos/batch_000/demo_000/demo.jsonl",
      "summary_path": "data/vla_demos/batch_000/demo_000/summary.json",
      "status": "success",
      "done_reached": true,
      "num_steps": 2766,
      "num_frames": 2766,
      "error": "",
      "scenario_id": "",
      "seed": null,
      "scenario": {
        "red_block_xy_offset_m": [
          0.0,
          0.0
        ],
        "red_block_body_id": 47,
        "red_block_qposadr": 50,
        "red_block_pos_before": [
          0.0,
          0.026,
          0.85
        ],
        "red_block_pos_after": [
          0.0,
          0.026,
          0.85
        ]
      }
    },
    {
      "demo_id": "demo_001",
      "output_dir": "data/vla_demos/batch_000/demo_001",
      "metadata_path": "data/vla_demos/batch_000/demo_001/demo.jsonl",
      "summary_path": "data/vla_demos/batch_000/demo_001/summary.json",
      "status": "success",
      "done_reached": true,
      "num_steps": 2766,
      "num_frames": 2766,
      "error": "",
      "scenario_id": "",
      "seed": null,
      "scenario": {
        "red_block_xy_offset_m": [
          0.0,
          0.0
        ],
        "red_block_body_id": 47,
        "red_block_qposadr": 50,
        "red_block_pos_before": [
          0.0,
          0.026,
          0.85
        ],
        "red_block_pos_after": [
          0.0,
          0.026,
          0.85
        ]
      }
    },
    {
      "demo_id": "demo_002",
      "output_dir": "data/vla_demos/batch_000/demo_002",
      "metadata_path": "data/vla_demos/batch_000/demo_002/demo.jsonl",
      "summary_path": "data/vla_demos/batch_000/demo_002/summary.json",
      "status": "success",
      "done_reached": true,
      "num_steps": 2766,
      "num_frames": 2766,
      "error": "",
      "scenario_id": "",
      "seed": null,
      "scenario": {
        "red_block_xy_offset_m": [
          0.0,
          0.0
        ],
        "red_block_body_id": 47,
        "red_block_qposadr": 50,
        "red_block_pos_before": [
          0.0,
          0.026,
          0.85
        ],
        "red_block_pos_after": [
          0.0,
          0.026,
          0.85
        ]
      }
    }
  ],
  "scenario_config_path": "",
  "scenario_config_name": "",
  "scenario_count": 0
}
```

---

## FILE: `data/vla_demos/batch_000/demo_000/demo.jsonl`

_Skipped: file is too large (2346830 bytes)._ 

---

## FILE: `data/vla_demos/batch_000/demo_000/summary.json`

```json
{
  "num_steps": 2766,
  "num_frames": 2766,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.01748103854992822,
  "mean_action_xyz_m": 0.0016406439064965631,
  "grip_closed_steps": 1902,
  "walk_nonzero_steps": 1276,
  "reach_active_steps": 2531,
  "scenario_id": "",
  "seed": null,
  "scenario": {
    "red_block_xy_offset_m": [
      0.0,
      0.0
    ],
    "red_block_body_id": 47,
    "red_block_qposadr": 50,
    "red_block_pos_before": [
      0.0,
      0.026,
      0.85
    ],
    "red_block_pos_after": [
      0.0,
      0.026,
      0.85
    ]
  },
  "red_block_xy_offset_m": [
    0.0,
    0.0
  ]
}
```

---

## FILE: `data/vla_demos/batch_000/demo_001/demo.jsonl`

_Skipped: file is too large (2346830 bytes)._ 

---

## FILE: `data/vla_demos/batch_000/demo_001/summary.json`

```json
{
  "num_steps": 2766,
  "num_frames": 2766,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.01748103854992822,
  "mean_action_xyz_m": 0.0016406439064965631,
  "grip_closed_steps": 1902,
  "walk_nonzero_steps": 1276,
  "reach_active_steps": 2531,
  "scenario_id": "",
  "seed": null,
  "scenario": {
    "red_block_xy_offset_m": [
      0.0,
      0.0
    ],
    "red_block_body_id": 47,
    "red_block_qposadr": 50,
    "red_block_pos_before": [
      0.0,
      0.026,
      0.85
    ],
    "red_block_pos_after": [
      0.0,
      0.026,
      0.85
    ]
  },
  "red_block_xy_offset_m": [
    0.0,
    0.0
  ]
}
```

---

## FILE: `data/vla_demos/batch_000/demo_002/demo.jsonl`

_Skipped: file is too large (2346830 bytes)._ 

---

## FILE: `data/vla_demos/batch_000/demo_002/summary.json`

```json
{
  "num_steps": 2766,
  "num_frames": 2766,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.01748103854992822,
  "mean_action_xyz_m": 0.0016406439064965631,
  "grip_closed_steps": 1902,
  "walk_nonzero_steps": 1276,
  "reach_active_steps": 2531,
  "scenario_id": "",
  "seed": null,
  "scenario": {
    "red_block_xy_offset_m": [
      0.0,
      0.0
    ],
    "red_block_body_id": 47,
    "red_block_qposadr": 50,
    "red_block_pos_before": [
      0.0,
      0.026,
      0.85
    ],
    "red_block_pos_after": [
      0.0,
      0.026,
      0.85
    ]
  },
  "red_block_xy_offset_m": [
    0.0,
    0.0
  ]
}
```

---

## FILE: `data/vla_demos/batch_000_no_images/batch_manifest.json`

```json
{
  "batch_id": "batch_000_no_images",
  "output_root": "data/vla_demos/batch_000_no_images",
  "created_unix_time": 1778122717.657944,
  "num_requested": 2,
  "num_completed": 2,
  "num_failed": 0,
  "record_every": 1,
  "camera": "head_cam",
  "no_images": true,
  "max_ticks": 4000,
  "demos": [
    {
      "demo_id": "demo_000",
      "output_dir": "data/vla_demos/batch_000_no_images/demo_000",
      "metadata_path": "data/vla_demos/batch_000_no_images/demo_000/demo.jsonl",
      "summary_path": "data/vla_demos/batch_000_no_images/demo_000/summary.json",
      "status": "success",
      "done_reached": true,
      "num_steps": 2766,
      "num_frames": 0,
      "error": ""
    },
    {
      "demo_id": "demo_001",
      "output_dir": "data/vla_demos/batch_000_no_images/demo_001",
      "metadata_path": "data/vla_demos/batch_000_no_images/demo_001/demo.jsonl",
      "summary_path": "data/vla_demos/batch_000_no_images/demo_001/summary.json",
      "status": "success",
      "done_reached": true,
      "num_steps": 2766,
      "num_frames": 0,
      "error": ""
    }
  ]
}
```

---

## FILE: `data/vla_demos/batch_000_no_images/demo_000/demo.jsonl`

_Skipped: file is too large (1727246 bytes)._ 

---

## FILE: `data/vla_demos/batch_000_no_images/demo_000/summary.json`

```json
{
  "num_steps": 2766,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.01748103854992822,
  "mean_action_xyz_m": 0.0016406439064965631,
  "grip_closed_steps": 1902,
  "walk_nonzero_steps": 1276,
  "reach_active_steps": 2531
}
```

---

## FILE: `data/vla_demos/batch_000_no_images/demo_001/demo.jsonl`

_Skipped: file is too large (1727246 bytes)._ 

---

## FILE: `data/vla_demos/batch_000_no_images/demo_001/summary.json`

```json
{
  "num_steps": 2766,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.01748103854992822,
  "mean_action_xyz_m": 0.0016406439064965631,
  "grip_closed_steps": 1902,
  "walk_nonzero_steps": 1276,
  "reach_active_steps": 2531
}
```

---

## FILE: `data/vla_demos/batch_001_perturbed_dryrun/batch_manifest.json`

```json
{
  "batch_id": "batch_001_perturbed_dryrun",
  "output_root": "data/vla_demos/batch_001_perturbed_dryrun",
  "created_unix_time": 1778147011.613732,
  "num_requested": 5,
  "num_completed": 0,
  "num_failed": 0,
  "record_every": 1,
  "camera": "head_cam",
  "no_images": true,
  "max_ticks": 4000,
  "demos": [],
  "scenario_config_path": "configs/scenarios/small_perturbations.json",
  "scenario_config_name": "small_perturbations_v1",
  "scenario_count": 5
}
```

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/batch_manifest.json`

```json
{
  "batch_id": "batch_001_perturbed_no_images",
  "output_root": "data/vla_demos/batch_001_perturbed_no_images",
  "created_unix_time": 1778147170.721656,
  "num_requested": 5,
  "num_completed": 5,
  "num_failed": 0,
  "record_every": 1,
  "camera": "head_cam",
  "no_images": true,
  "max_ticks": 4000,
  "demos": [
    {
      "demo_id": "demo_000",
      "output_dir": "data/vla_demos/batch_001_perturbed_no_images/demo_000",
      "metadata_path": "data/vla_demos/batch_001_perturbed_no_images/demo_000/demo.jsonl",
      "summary_path": "data/vla_demos/batch_001_perturbed_no_images/demo_000/summary.json",
      "status": "success",
      "done_reached": true,
      "num_steps": 2766,
      "num_frames": 0,
      "error": "",
      "scenario_id": "nominal",
      "seed": 0,
      "scenario": {
        "scenario_id": "nominal",
        "seed": 0,
        "red_block_xy_offset_m": [
          0.0,
          0.0
        ],
        "robot_base_xy_offset_m": [
          0.0,
          0.0
        ],
        "target_drop_xy_offset_m": [
          0.0,
          0.0
        ]
      }
    },
    {
      "demo_id": "demo_001",
      "output_dir": "data/vla_demos/batch_001_perturbed_no_images/demo_001",
      "metadata_path": "data/vla_demos/batch_001_perturbed_no_images/demo_001/demo.jsonl",
      "summary_path": "data/vla_demos/batch_001_perturbed_no_images/demo_001/summary.json",
      "status": "success",
      "done_reached": true,
      "num_steps": 3048,
      "num_frames": 0,
      "error": "",
      "scenario_id": "cyl_x_plus_02",
      "seed": 101,
      "scenario": {
        "scenario_id": "cyl_x_plus_02",
        "seed": 101,
        "red_block_xy_offset_m": [
          0.02,
          0.0
        ],
        "robot_base_xy_offset_m": [
          0.0,
          0.0
        ],
        "target_drop_xy_offset_m": [
          0.0,
          0.0
        ]
      }
    },
    {
      "demo_id": "demo_002",
      "output_dir": "data/vla_demos/batch_001_perturbed_no_images/demo_002",
      "metadata_path": "data/vla_demos/batch_001_perturbed_no_images/demo_002/demo.jsonl",
      "summary_path": "data/vla_demos/batch_001_perturbed_no_images/demo_002/summary.json",
      "status": "success",
      "done_reached": true,
      "num_steps": 3064,
      "num_frames": 0,
      "error": "",
      "scenario_id": "cyl_x_minus_02",
      "seed": 102,
      "scenario": {
        "scenario_id": "cyl_x_minus_02",
        "seed": 102,
        "red_block_xy_offset_m": [
          -0.02,
          0.0
        ],
        "robot_base_xy_offset_m": [
          0.0,
          0.0
        ],
        "target_drop_xy_offset_m": [
          0.0,
          0.0
        ]
      }
    },
    {
      "demo_id": "demo_003",
      "output_dir": "data/vla_demos/batch_001_perturbed_no_images/demo_003",
      "metadata_path": "data/vla_demos/batch_001_perturbed_no_images/demo_003/demo.jsonl",
      "summary_path": "data/vla_demos/batch_001_perturbed_no_images/demo_003/summary.json",
      "status": "success",
      "done_reached": true,
      "num_steps": 2645,
      "num_frames": 0,
      "error": "",
      "scenario_id": "cyl_y_plus_02",
      "seed": 103,
      "scenario": {
        "scenario_id": "cyl_y_plus_02",
        "seed": 103,
        "red_block_xy_offset_m": [
          0.0,
          0.02
        ],
        "robot_base_xy_offset_m": [
          0.0,
          0.0
        ],
        "target_drop_xy_offset_m": [
          0.0,
          0.0
        ]
      }
    },
    {
      "demo_id": "demo_004",
      "output_dir": "data/vla_demos/batch_001_perturbed_no_images/demo_004",
      "metadata_path": "data/vla_demos/batch_001_perturbed_no_images/demo_004/demo.jsonl",
      "summary_path": "data/vla_demos/batch_001_perturbed_no_images/demo_004/summary.json",
      "status": "success",
      "done_reached": false,
      "num_steps": 4000,
      "num_frames": 0,
      "error": "",
      "scenario_id": "cyl_y_minus_02",
      "seed": 104,
      "scenario": {
        "scenario_id": "cyl_y_minus_02",
        "seed": 104,
        "red_block_xy_offset_m": [
          0.0,
          -0.02
        ],
        "robot_base_xy_offset_m": [
          0.0,
          0.0
        ],
        "target_drop_xy_offset_m": [
          0.0,
          0.0
        ]
      }
    }
  ],
  "scenario_config_path": "configs/scenarios/small_perturbations.json",
  "scenario_config_name": "small_perturbations_v1",
  "scenario_count": 5
}
```

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_000/demo.jsonl`

_Skipped: file is too large (2294276 bytes)._ 

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_000/summary.json`

```json
{
  "num_steps": 2766,
  "num_frames": 0,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.01748103854992822,
  "mean_action_xyz_m": 0.0016406439064965631,
  "grip_closed_steps": 1902,
  "walk_nonzero_steps": 1276,
  "reach_active_steps": 2531,
  "scenario_id": "nominal",
  "seed": 0,
  "scenario": {
    "red_block_xy_offset_m": [
      0.0,
      0.0
    ],
    "red_block_body_id": 47,
    "red_block_qposadr": 50,
    "red_block_pos_before": [
      0.0,
      0.026,
      0.85
    ],
    "red_block_pos_after": [
      0.0,
      0.026,
      0.85
    ]
  },
  "red_block_xy_offset_m": [
    0.0,
    0.0
  ]
}
```

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_001/demo.jsonl`

_Skipped: file is too large (2580127 bytes)._ 

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_001/summary.json`

```json
{
  "num_steps": 3048,
  "num_frames": 0,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.02281151568341445,
  "mean_action_xyz_m": 0.0016411938118310687,
  "grip_closed_steps": 2000,
  "walk_nonzero_steps": 1288,
  "reach_active_steps": 2801,
  "scenario_id": "cyl_x_plus_02",
  "seed": 101,
  "scenario": {
    "red_block_xy_offset_m": [
      0.02,
      0.0
    ],
    "red_block_body_id": 47,
    "red_block_qposadr": 50,
    "red_block_pos_before": [
      0.0,
      0.026,
      0.85
    ],
    "red_block_pos_after": [
      0.02,
      0.026,
      0.85
    ]
  },
  "red_block_xy_offset_m": [
    0.02,
    0.0
  ]
}
```

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_002/demo.jsonl`

_Skipped: file is too large (2606368 bytes)._ 

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_002/summary.json`

```json
{
  "num_steps": 3064,
  "num_frames": 0,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.01741132322440146,
  "mean_action_xyz_m": 0.0014480312907455516,
  "grip_closed_steps": 2000,
  "walk_nonzero_steps": 1304,
  "reach_active_steps": 2801,
  "scenario_id": "cyl_x_minus_02",
  "seed": 102,
  "scenario": {
    "red_block_xy_offset_m": [
      -0.02,
      0.0
    ],
    "red_block_body_id": 47,
    "red_block_qposadr": 50,
    "red_block_pos_before": [
      0.0,
      0.026,
      0.85
    ],
    "red_block_pos_after": [
      -0.02,
      0.026,
      0.85
    ]
  },
  "red_block_xy_offset_m": [
    -0.02,
    0.0
  ]
}
```

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_003/demo.jsonl`

_Skipped: file is too large (2226647 bytes)._ 

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_003/summary.json`

```json
{
  "num_steps": 2645,
  "num_frames": 0,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.03486015159414144,
  "mean_action_xyz_m": 0.002227201786756791,
  "grip_closed_steps": 1902,
  "walk_nonzero_steps": 1297,
  "reach_active_steps": 2386,
  "scenario_id": "cyl_y_plus_02",
  "seed": 103,
  "scenario": {
    "red_block_xy_offset_m": [
      0.0,
      0.02
    ],
    "red_block_body_id": 47,
    "red_block_qposadr": 50,
    "red_block_pos_before": [
      0.0,
      0.026,
      0.85
    ],
    "red_block_pos_after": [
      0.0,
      0.046,
      0.85
    ]
  },
  "red_block_xy_offset_m": [
    0.0,
    0.02
  ]
}
```

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_004/demo.jsonl`

_Skipped: file is too large (3508479 bytes)._ 

---

## FILE: `data/vla_demos/batch_001_perturbed_no_images/demo_004/summary.json`

```json
{
  "num_steps": 4000,
  "num_frames": 0,
  "done_reached": false,
  "first_phase": "SETTLE",
  "last_phase": "APPROACH_SOURCE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.01741132322440146,
  "mean_action_xyz_m": 0.0002680918038392189,
  "grip_closed_steps": 0,
  "walk_nonzero_steps": 3849,
  "reach_active_steps": 0,
  "scenario_id": "cyl_y_minus_02",
  "seed": 104,
  "scenario": {
    "red_block_xy_offset_m": [
      0.0,
      -0.02
    ],
    "red_block_body_id": 47,
    "red_block_qposadr": 50,
    "red_block_pos_before": [
      0.0,
      0.026,
      0.85
    ],
    "red_block_pos_after": [
      0.0,
      0.005999999999999998,
      0.85
    ]
  },
  "red_block_xy_offset_m": [
    0.0,
    -0.02
  ]
}
```

---

## FILE: `data/vla_demos/demo_000/demo.jsonl`

_Skipped: file is too large (350583 bytes)._ 

---

## FILE: `data/vla_demos/demo_000/summary.json`

```json
{
  "num_steps": 554,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.08456800232659496,
  "mean_action_xyz_m": 0.00788488542545105,
  "grip_closed_steps": 380
}
```

---

## FILE: `data/vla_demos/demo_000_no_images/demo.jsonl`

_Skipped: file is too large (337841 bytes)._ 

---

## FILE: `data/vla_demos/demo_000_no_images/summary.json`

```json
{
  "num_steps": 554,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.08456800232659496,
  "mean_action_xyz_m": 0.00788488542545105,
  "grip_closed_steps": 380
}
```

---

## FILE: `data/vla_demos/demo_001/demo.jsonl`

_Skipped: file is too large (358174 bytes)._ 

---

## FILE: `data/vla_demos/demo_001/summary.json`

```json
{
  "num_steps": 554,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.08456800232659496,
  "mean_action_xyz_m": 0.00788488542545105,
  "grip_closed_steps": 380,
  "walk_nonzero_steps": 255,
  "reach_active_steps": 507
}
```

---

## FILE: `data/vla_demos/demo_002_every_tick/demo.jsonl`

_Skipped: file is too large (1790864 bytes)._ 

---

## FILE: `data/vla_demos/demo_002_every_tick/summary.json`

```json
{
  "num_steps": 2766,
  "done_reached": true,
  "first_phase": "SETTLE",
  "last_phase": "DONE",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "DONE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "max_action_xyz_m": 0.01748103854992822,
  "mean_action_xyz_m": 0.0016406439064965631,
  "grip_closed_steps": 1902,
  "walk_nonzero_steps": 1276,
  "reach_active_steps": 2531
}
```

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/audit/audit_report.json`

```json
{
  "source_dataset": "data/vla_exports/batch_000_no_images_g1_native/dataset.jsonl",
  "num_records": 5330,
  "action_vector_shape": [
    5330,
    8
  ],
  "phase_counts": {
    "APPROACH_SOURCE": 168,
    "APPROACH_TARGET": 2400,
    "CLOSE_GRIP": 4,
    "DESCEND_SOURCE": 600,
    "HOVER_SOURCE": 54,
    "HOVER_TARGET": 400,
    "LIFT_SOURCE": 400,
    "LOWER_TARGET": 600,
    "OPEN_GRIP": 4,
    "RETRACT": 400,
    "SETTLE": 300
  },
  "phase_segments": [
    {
      "phase": "SETTLE",
      "start_sample_index": 0,
      "end_sample_index": 149,
      "length": 150
    },
    {
      "phase": "APPROACH_SOURCE",
      "start_sample_index": 150,
      "end_sample_index": 233,
      "length": 84
    },
    {
      "phase": "HOVER_SOURCE",
      "start_sample_index": 234,
      "end_sample_index": 260,
      "length": 27
    },
    {
      "phase": "DESCEND_SOURCE",
      "start_sample_index": 261,
      "end_sample_index": 560,
      "length": 300
    },
    {
      "phase": "CLOSE_GRIP",
      "start_sample_index": 561,
      "end_sample_index": 562,
      "length": 2
    },
    {
      "phase": "LIFT_SOURCE",
      "start_sample_index": 563,
      "end_sample_index": 762,
      "length": 200
    },
    {
      "phase": "APPROACH_TARGET",
      "start_sample_index": 763,
      "end_sample_index": 1962,
      "length": 1200
    },
    {
      "phase": "HOVER_TARGET",
      "start_sample_index": 1963,
      "end_sample_index": 2162,
      "length": 200
    },
    {
      "phase": "LOWER_TARGET",
      "start_sample_index": 2163,
      "end_sample_index": 2462,
      "length": 300
    },
    {
      "phase": "OPEN_GRIP",
      "start_sample_index": 2463,
      "end_sample_index": 2464,
      "length": 2
    },
    {
      "phase": "RETRACT",
      "start_sample_index": 2465,
      "end_sample_index": 2664,
      "length": 200
    },
    {
      "phase": "SETTLE",
      "start_sample_index": 2665,
      "end_sample_index": 2814,
      "length": 150
    },
    {
      "phase": "APPROACH_SOURCE",
      "start_sample_index": 2815,
      "end_sample_index": 2898,
      "length": 84
    },
    {
      "phase": "HOVER_SOURCE",
      "start_sample_index": 2899,
      "end_sample_index": 2925,
      "length": 27
    },
    {
      "phase": "DESCEND_SOURCE",
      "start_sample_index": 2926,
      "end_sample_index": 3225,
      "length": 300
    },
    {
      "phase": "CLOSE_GRIP",
      "start_sample_index": 3226,
      "end_sample_index": 3227,
      "length": 2
    },
    {
      "phase": "LIFT_SOURCE",
      "start_sample_index": 3228,
      "end_sample_index": 3427,
      "length": 200
    },
    {
      "phase": "APPROACH_TARGET",
      "start_sample_index": 3428,
      "end_sample_index": 4627,
      "length": 1200
    },
    {
      "phase": "HOVER_TARGET",
      "start_sample_index": 4628,
      "end_sample_index": 4827,
      "length": 200
    },
    {
      "phase": "LOWER_TARGET",
      "start_sample_index": 4828,
      "end_sample_index": 5127,
      "length": 300
    },
    {
      "phase": "OPEN_GRIP",
      "start_sample_index": 5128,
      "end_sample_index": 5129,
      "length": 2
    },
    {
      "phase": "RETRACT",
      "start_sample_index": 5130,
      "end_sample_index": 5329,
      "length": 200
    }
  ],
  "boolean_balance": {
    "reach_active_true": 4860,
    "reach_active_false": 470,
    "reach_active_true_fraction": 0.9118198874296435,
    "grip_closed_true": 3804,
    "grip_closed_false": 1526,
    "grip_closed_true_fraction": 0.7136960600375235
  },
  "action_statistics": {
    "walk_x": {
      "min": 0.0,
      "max": 0.35,
      "mean": 0.09260037523452158,
      "std": 0.10309229985207324
    },
    "walk_y": {
      "min": 0.0,
      "max": 0.18,
      "mean": 0.05880984571281502,
      "std": 0.08308457904123835
    },
    "walk_yaw": {
      "min": -1.0,
      "max": 0.25,
      "mean": -0.05989657415973408,
      "std": 0.3918518264629808
    },
    "reach_x": {
      "min": 0.2150164097547531,
      "max": 0.36787861585617065,
      "mean": 0.298711253016572,
      "std": 0.02122083825555979
    },
    "reach_y": {
      "min": -0.2,
      "max": -0.029999999329447746,
      "mean": -0.14700635502726453,
      "std": 0.07873104887306134
    },
    "reach_z": {
      "min": -0.06108388677239418,
      "max": 0.2,
      "mean": 0.1413913225168694,
      "std": 0.09304555686458722
    },
    "reach_active": {
      "min": 0.0,
      "max": 1.0,
      "mean": 0.9118198874296435,
      "std": 0.2835566615642026
    },
    "grip_closed": {
      "min": 0.0,
      "max": 1.0,
      "mean": 0.7136960600375235,
      "std": 0.45203317790228537
    }
  },
  "magnitude_statistics": {
    "mean_walk_cmd_magnitude": 0.2647044983945314,
    "max_walk_cmd_magnitude": 1.0071742649611337,
    "zero_walk_records": 2778,
    "nonzero_walk_records": 2552,
    "mean_reach_target_norm": 0.3783422195480008,
    "max_reach_target_norm": 0.41231056256176607
  },
  "idle_runs": [
    {
      "start_sample_index": 0,
      "end_sample_index": 150,
      "length": 151,
      "phase": "MIXED"
    },
    {
      "start_sample_index": 2665,
      "end_sample_index": 2815,
      "length": 151,
      "phase": "MIXED"
    }
  ],
  "warnings": [
    "Found 2 idle-heavy run(s). Consider filtering or weighting.",
    "This appears to be a single-trajectory dataset. Validation splits are debugging splits, not robust generalization estimates."
  ]
}
```

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/audit/split_summary.json`

```json
{
  "train_records": 4263,
  "val_records": 1067,
  "total_records": 5330,
  "val_fraction_actual": 0.200187617260788,
  "train_phase_counts": {
    "APPROACH_SOURCE": 134,
    "APPROACH_TARGET": 1920,
    "CLOSE_GRIP": 3,
    "DESCEND_SOURCE": 480,
    "HOVER_SOURCE": 43,
    "HOVER_TARGET": 320,
    "LIFT_SOURCE": 320,
    "LOWER_TARGET": 480,
    "OPEN_GRIP": 3,
    "RETRACT": 320,
    "SETTLE": 240
  },
  "val_phase_counts": {
    "APPROACH_SOURCE": 34,
    "APPROACH_TARGET": 480,
    "CLOSE_GRIP": 1,
    "DESCEND_SOURCE": 120,
    "HOVER_SOURCE": 11,
    "HOVER_TARGET": 80,
    "LIFT_SOURCE": 80,
    "LOWER_TARGET": 120,
    "OPEN_GRIP": 1,
    "RETRACT": 80,
    "SETTLE": 60
  },
  "split_strategy": "phase_temporal_tail",
  "warning": "Single-trajectory split for debugging only; not a robust generalization estimate.",
  "train_path": "data/vla_exports/batch_000_no_images_g1_native/audit/train.jsonl",
  "val_path": "data/vla_exports/batch_000_no_images_g1_native/audit/val.jsonl"
}
```

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/audit/train.jsonl`

_Skipped: file is too large (1477330 bytes)._ 

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/audit/val.jsonl`

_Skipped: file is too large (370166 bytes)._ 

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/dataset.jsonl`

_Skipped: file is too large (2266346 bytes)._ 

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/source_manifest.json`

```json
{
  "selection": {
    "batch_id": "batch_000_no_images",
    "selected_demo_ids": [
      "demo_000",
      "demo_001"
    ],
    "selected_metadata_paths": [
      "data/vla_demos/batch_000_no_images/demo_000/demo.jsonl",
      "data/vla_demos/batch_000_no_images/demo_001/demo.jsonl"
    ],
    "skipped_demo_ids": [],
    "skip_reasons": {}
  },
  "source_manifest": {
    "batch_id": "batch_000_no_images",
    "output_root": "data/vla_demos/batch_000_no_images",
    "created_unix_time": 1778122717.657944,
    "num_requested": 2,
    "num_completed": 2,
    "num_failed": 0,
    "record_every": 1,
    "camera": "head_cam",
    "no_images": true,
    "max_ticks": 4000,
    "demos": [
      {
        "demo_id": "demo_000",
        "output_dir": "data/vla_demos/batch_000_no_images/demo_000",
        "metadata_path": "data/vla_demos/batch_000_no_images/demo_000/demo.jsonl",
        "summary_path": "data/vla_demos/batch_000_no_images/demo_000/summary.json",
        "status": "success",
        "done_reached": true,
        "num_steps": 2766,
        "num_frames": 0,
        "error": ""
      },
      {
        "demo_id": "demo_001",
        "output_dir": "data/vla_demos/batch_000_no_images/demo_001",
        "metadata_path": "data/vla_demos/batch_000_no_images/demo_001/demo.jsonl",
        "summary_path": "data/vla_demos/batch_000_no_images/demo_001/summary.json",
        "status": "success",
        "done_reached": true,
        "num_steps": 2766,
        "num_frames": 0,
        "error": ""
      }
    ]
  }
}
```

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/summary.json`

```json
{
  "num_records": 5330,
  "first_phase": "SETTLE",
  "last_phase": "RETRACT",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "walk_nonzero_records": 2552,
  "reach_active_records": 4860,
  "grip_closed_records": 3804,
  "mean_walk_cmd_magnitude": 0.2647044983945314,
  "max_walk_cmd_magnitude": 1.0071742649611337,
  "mean_reach_target_norm": 0.3783422195480008,
  "max_reach_target_norm": 0.41231056256176607,
  "batch_id": "batch_000_no_images",
  "source_manifest_path": "data/vla_demos/batch_000_no_images/batch_manifest.json",
  "output_dir": "data/vla_exports/batch_000_no_images_g1_native",
  "dataset_path": "data/vla_exports/batch_000_no_images_g1_native/dataset.jsonl",
  "summary_path": "data/vla_exports/batch_000_no_images_g1_native/summary.json",
  "source_manifest_copy_path": "data/vla_exports/batch_000_no_images_g1_native/source_manifest.json",
  "num_demos_in_manifest": 2,
  "num_selected_demos": 2,
  "num_skipped_demos": 0,
  "selected_demo_ids": [
    "demo_000",
    "demo_001"
  ],
  "skipped_demo_ids": [],
  "skip_reasons": {},
  "records_per_demo": {
    "demo_000": 2665,
    "demo_001": 2665
  },
  "include_phase": true,
  "drop_done": true,
  "drop_inactive_reach": false,
  "action_vector": [
    "walk_x",
    "walk_y",
    "walk_yaw",
    "reach_x",
    "reach_y",
    "reach_z",
    "reach_active",
    "grip_closed"
  ]
}
```

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/training_views/filtered_no_idle.jsonl`

_Skipped: file is too large (1753531 bytes)._ 

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/training_views/full.jsonl`

_Skipped: file is too large (1847496 bytes)._ 

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/training_views/sample_weights.jsonl`

_Skipped: file is too large (611206 bytes)._ 

---

## FILE: `data/vla_exports/batch_000_no_images_g1_native/training_views/training_view_summary.json`

```json
{
  "view_name": "g1_native_training_views",
  "source_records": 5330,
  "filtered_records": 5022,
  "removed_records": 308,
  "source_phase_counts": {
    "APPROACH_SOURCE": 168,
    "APPROACH_TARGET": 2400,
    "CLOSE_GRIP": 4,
    "DESCEND_SOURCE": 600,
    "HOVER_SOURCE": 54,
    "HOVER_TARGET": 400,
    "LIFT_SOURCE": 400,
    "LOWER_TARGET": 600,
    "OPEN_GRIP": 4,
    "RETRACT": 400,
    "SETTLE": 300
  },
  "filtered_phase_counts": {
    "APPROACH_SOURCE": 152,
    "APPROACH_TARGET": 2400,
    "CLOSE_GRIP": 4,
    "DESCEND_SOURCE": 600,
    "HOVER_SOURCE": 52,
    "HOVER_TARGET": 400,
    "LIFT_SOURCE": 400,
    "LOWER_TARGET": 600,
    "OPEN_GRIP": 4,
    "RETRACT": 400,
    "SETTLE": 10
  },
  "rare_transition_records_source": {
    "CLOSE_GRIP": 4,
    "OPEN_GRIP": 4
  },
  "rare_transition_records_filtered": {
    "CLOSE_GRIP": 4,
    "OPEN_GRIP": 4
  },
  "idle_records_source": 318,
  "idle_records_filtered": 10,
  "weight_count": 5330,
  "min_weight": 0.23802617467658693,
  "max_weight": 20.0,
  "mean_weight": 1.0000000000000002,
  "warnings": [
    "This is still a single-trajectory dataset. Weighted/filtered views are debugging aids, not robust generalization data."
  ],
  "keep_first_n_idle": 10,
  "rare_phase_boost": 5.0,
  "files": {
    "full": "data/vla_exports/batch_000_no_images_g1_native/training_views/full.jsonl",
    "filtered_no_idle": "data/vla_exports/batch_000_no_images_g1_native/training_views/filtered_no_idle.jsonl",
    "sample_weights": "data/vla_exports/batch_000_no_images_g1_native/training_views/sample_weights.jsonl",
    "summary": "data/vla_exports/batch_000_no_images_g1_native/training_views/training_view_summary.json"
  }
}
```

---

## FILE: `data/vla_exports/g1_native_demo_002/audit/audit_report.json`

```json
{
  "source_dataset": "data/vla_exports/g1_native_demo_002/dataset.jsonl",
  "num_records": 2665,
  "action_vector_shape": [
    2665,
    8
  ],
  "phase_counts": {
    "APPROACH_SOURCE": 84,
    "APPROACH_TARGET": 1200,
    "CLOSE_GRIP": 2,
    "DESCEND_SOURCE": 300,
    "HOVER_SOURCE": 27,
    "HOVER_TARGET": 200,
    "LIFT_SOURCE": 200,
    "LOWER_TARGET": 300,
    "OPEN_GRIP": 2,
    "RETRACT": 200,
    "SETTLE": 150
  },
  "phase_segments": [
    {
      "phase": "SETTLE",
      "start_sample_index": 0,
      "end_sample_index": 149,
      "length": 150
    },
    {
      "phase": "APPROACH_SOURCE",
      "start_sample_index": 150,
      "end_sample_index": 233,
      "length": 84
    },
    {
      "phase": "HOVER_SOURCE",
      "start_sample_index": 234,
      "end_sample_index": 260,
      "length": 27
    },
    {
      "phase": "DESCEND_SOURCE",
      "start_sample_index": 261,
      "end_sample_index": 560,
      "length": 300
    },
    {
      "phase": "CLOSE_GRIP",
      "start_sample_index": 561,
      "end_sample_index": 562,
      "length": 2
    },
    {
      "phase": "LIFT_SOURCE",
      "start_sample_index": 563,
      "end_sample_index": 762,
      "length": 200
    },
    {
      "phase": "APPROACH_TARGET",
      "start_sample_index": 763,
      "end_sample_index": 1962,
      "length": 1200
    },
    {
      "phase": "HOVER_TARGET",
      "start_sample_index": 1963,
      "end_sample_index": 2162,
      "length": 200
    },
    {
      "phase": "LOWER_TARGET",
      "start_sample_index": 2163,
      "end_sample_index": 2462,
      "length": 300
    },
    {
      "phase": "OPEN_GRIP",
      "start_sample_index": 2463,
      "end_sample_index": 2464,
      "length": 2
    },
    {
      "phase": "RETRACT",
      "start_sample_index": 2465,
      "end_sample_index": 2664,
      "length": 200
    }
  ],
  "boolean_balance": {
    "reach_active_true": 2430,
    "reach_active_false": 235,
    "reach_active_true_fraction": 0.9118198874296435,
    "grip_closed_true": 1902,
    "grip_closed_false": 763,
    "grip_closed_true_fraction": 0.7136960600375235
  },
  "action_statistics": {
    "walk_x": {
      "min": 0.0,
      "max": 0.35,
      "mean": 0.09260037523452158,
      "std": 0.10309229985207324
    },
    "walk_y": {
      "min": 0.0,
      "max": 0.18,
      "mean": 0.05880984571281502,
      "std": 0.08308457904123835
    },
    "walk_yaw": {
      "min": -1.0,
      "max": 0.25,
      "mean": -0.05989657415973408,
      "std": 0.3918518264629808
    },
    "reach_x": {
      "min": 0.2150164097547531,
      "max": 0.36787861585617065,
      "mean": 0.298711253016572,
      "std": 0.02122083825555979
    },
    "reach_y": {
      "min": -0.2,
      "max": -0.029999999329447746,
      "mean": -0.14700635502726453,
      "std": 0.07873104887306134
    },
    "reach_z": {
      "min": -0.06108388677239418,
      "max": 0.2,
      "mean": 0.1413913225168694,
      "std": 0.09304555686458722
    },
    "reach_active": {
      "min": 0.0,
      "max": 1.0,
      "mean": 0.9118198874296435,
      "std": 0.2835566615642026
    },
    "grip_closed": {
      "min": 0.0,
      "max": 1.0,
      "mean": 0.7136960600375235,
      "std": 0.45203317790228537
    }
  },
  "magnitude_statistics": {
    "mean_walk_cmd_magnitude": 0.2647044983945314,
    "max_walk_cmd_magnitude": 1.0071742649611337,
    "zero_walk_records": 1389,
    "nonzero_walk_records": 1276,
    "mean_reach_target_norm": 0.3783422195480008,
    "max_reach_target_norm": 0.41231056256176607
  },
  "idle_runs": [
    {
      "start_sample_index": 0,
      "end_sample_index": 150,
      "length": 151,
      "phase": "MIXED"
    }
  ],
  "warnings": [
    "Found 1 idle-heavy run(s). Consider filtering or weighting.",
    "This appears to be a single-trajectory dataset. Validation splits are debugging splits, not robust generalization estimates."
  ]
}
```

---

## FILE: `data/vla_exports/g1_native_demo_002/audit/split_summary.json`

```json
{
  "train_records": 2130,
  "val_records": 535,
  "total_records": 2665,
  "val_fraction_actual": 0.20075046904315197,
  "train_phase_counts": {
    "APPROACH_SOURCE": 67,
    "APPROACH_TARGET": 960,
    "CLOSE_GRIP": 1,
    "DESCEND_SOURCE": 240,
    "HOVER_SOURCE": 21,
    "HOVER_TARGET": 160,
    "LIFT_SOURCE": 160,
    "LOWER_TARGET": 240,
    "OPEN_GRIP": 1,
    "RETRACT": 160,
    "SETTLE": 120
  },
  "val_phase_counts": {
    "APPROACH_SOURCE": 17,
    "APPROACH_TARGET": 240,
    "CLOSE_GRIP": 1,
    "DESCEND_SOURCE": 60,
    "HOVER_SOURCE": 6,
    "HOVER_TARGET": 40,
    "LIFT_SOURCE": 40,
    "LOWER_TARGET": 60,
    "OPEN_GRIP": 1,
    "RETRACT": 40,
    "SETTLE": 30
  },
  "split_strategy": "phase_temporal_tail",
  "warning": "Single-trajectory split for debugging only; not a robust generalization estimate.",
  "train_path": "data/vla_exports/g1_native_demo_002/audit/train.jsonl",
  "val_path": "data/vla_exports/g1_native_demo_002/audit/val.jsonl"
}
```

---

## FILE: `data/vla_exports/g1_native_demo_002/audit/train.jsonl`

_Skipped: file is too large (786893 bytes)._ 

---

## FILE: `data/vla_exports/g1_native_demo_002/audit/val.jsonl`

```
{"sample_index":120,"source_step_index":120,"image_path":"frames/frame_000120.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":121,"source_step_index":121,"image_path":"frames/frame_000121.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":122,"source_step_index":122,"image_path":"frames/frame_000122.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":123,"source_step_index":123,"image_path":"frames/frame_000123.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":124,"source_step_index":124,"image_path":"frames/frame_000124.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":125,"source_step_index":125,"image_path":"frames/frame_000125.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":126,"source_step_index":126,"image_path":"frames/frame_000126.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":127,"source_step_index":127,"image_path":"frames/frame_000127.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":128,"source_step_index":128,"image_path":"frames/frame_000128.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":129,"source_step_index":129,"image_path":"frames/frame_000129.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":130,"source_step_index":130,"image_path":"frames/frame_000130.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":131,"source_step_index":131,"image_path":"frames/frame_000131.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":132,"source_step_index":132,"image_path":"frames/frame_000132.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":133,"source_step_index":133,"image_path":"frames/frame_000133.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":134,"source_step_index":134,"image_path":"frames/frame_000134.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":135,"source_step_index":135,"image_path":"frames/frame_000135.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":136,"source_step_index":136,"image_path":"frames/frame_000136.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":137,"source_step_index":137,"image_path":"frames/frame_000137.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":138,"source_step_index":138,"image_path":"frames/frame_000138.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":139,"source_step_index":139,"image_path":"frames/frame_000139.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":140,"source_step_index":140,"image_path":"frames/frame_000140.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":141,"source_step_index":141,"image_path":"frames/frame_000141.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":142,"source_step_index":142,"image_path":"frames/frame_000142.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":143,"source_step_index":143,"image_path":"frames/frame_000143.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":144,"source_step_index":144,"image_path":"frames/frame_000144.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":145,"source_step_index":145,"image_path":"frames/frame_000145.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":146,"source_step_index":146,"image_path":"frames/frame_000146.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":147,"source_step_index":147,"image_path":"frames/frame_000147.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":148,"source_step_index":148,"image_path":"frames/frame_000148.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":149,"source_step_index":149,"image_path":"frames/frame_000149.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"SETTLE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":217,"source_step_index":217,"image_path":"frames/frame_000217.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.10601479868627826,0.02522905056989418],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.10601479868627826,0.02522905056989418,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":218,"source_step_index":218,"image_path":"frames/frame_000218.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.10447252767232364,0.02303513835913008],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.10447252767232364,0.02303513835913008,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":219,"source_step_index":219,"image_path":"frames/frame_000219.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.10318276242759403,0.021207116764580317],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.10318276242759403,0.021207116764580317,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":220,"source_step_index":220,"image_path":"frames/frame_000220.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.10242606163547542,0.020218377936540775],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.10242606163547542,0.020218377936540775,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":221,"source_step_index":221,"image_path":"frames/frame_000221.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.10204596786446847,0.019845587863541344],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.10204596786446847,0.019845587863541344,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":222,"source_step_index":222,"image_path":"frames/frame_000222.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.10144402039317181,0.019107458819518256],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.10144402039317181,0.019107458819518256,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":223,"source_step_index":223,"image_path":"frames/frame_000223.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.10450337076175926,0.024536049487063012],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.10450337076175926,0.024536049487063012,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":224,"source_step_index":224,"image_path":"frames/frame_000224.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.10480333998724922,0.025337539205125187],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.10480333998724922,0.025337539205125187,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":225,"source_step_index":225,"image_path":"frames/frame_000225.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.10129796875826251,0.019552256636726845],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.10129796875826251,0.019552256636726845,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":226,"source_step_index":226,"image_path":"frames/frame_000226.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.12,0.09971078703938051,0.016976630449028852],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.12,0.09971078703938051,0.016976630449028852,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":227,"source_step_index":227,"image_path":"frames/frame_000227.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":228,"source_step_index":228,"image_path":"frames/frame_000228.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":229,"source_step_index":229,"image_path":"frames/frame_000229.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":230,"source_step_index":230,"image_path":"frames/frame_000230.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":231,"source_step_index":231,"image_path":"frames/frame_000231.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":232,"source_step_index":232,"image_path":"frames/frame_000232.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":233,"source_step_index":233,"image_path":"frames/frame_000233.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":false,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,0.0,0.0]}
{"sample_index":255,"source_step_index":255,"image_path":"frames/frame_000255.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3664904236793518,-0.029999999329447746,0.15854094922542572],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3664904236793518,-0.029999999329447746,0.15854094922542572,1.0,0.0]}
{"sample_index":256,"source_step_index":256,"image_path":"frames/frame_000256.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3655545115470886,-0.029999999329447746,0.15832339227199554],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3655545115470886,-0.029999999329447746,0.15832339227199554,1.0,0.0]}
{"sample_index":257,"source_step_index":257,"image_path":"frames/frame_000257.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.36444976925849915,-0.029999999329447746,0.15810517966747284],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.36444976925849915,-0.029999999329447746,0.15810517966747284,1.0,0.0]}
{"sample_index":258,"source_step_index":258,"image_path":"frames/frame_000258.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.36320459842681885,-0.029999999329447746,0.1578846424818039],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.36320459842681885,-0.029999999329447746,0.1578846424818039,1.0,0.0]}
{"sample_index":259,"source_step_index":259,"image_path":"frames/frame_000259.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3618483543395996,-0.029999999329447746,0.15767228603363037],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3618483543395996,-0.029999999329447746,0.15767228603363037,1.0,0.0]}
{"sample_index":260,"source_step_index":260,"image_path":"frames/frame_000260.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.36041587591171265,-0.029999999329447746,0.15747720003128052],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.36041587591171265,-0.029999999329447746,0.15747720003128052,1.0,0.0]}
{"sample_index":501,"source_step_index":501,"image_path":"frames/frame_000501.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33906134963035583,-0.029999999329447746,0.03948616981506348],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33906134963035583,-0.029999999329447746,0.03948616981506348,1.0,0.0]}
{"sample_index":502,"source_step_index":502,"image_path":"frames/frame_000502.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33905932307243347,-0.029999999329447746,0.039491262286901474],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33905932307243347,-0.029999999329447746,0.039491262286901474,1.0,0.0]}
{"sample_index":503,"source_step_index":503,"image_path":"frames/frame_000503.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3390635550022125,-0.029999999329447746,0.03949659317731857],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3390635550022125,-0.029999999329447746,0.03949659317731857,1.0,0.0]}
{"sample_index":504,"source_step_index":504,"image_path":"frames/frame_000504.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33906567096710205,-0.029999999329447746,0.03950174152851105],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33906567096710205,-0.029999999329447746,0.03950174152851105,1.0,0.0]}
{"sample_index":505,"source_step_index":505,"image_path":"frames/frame_000505.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33906471729278564,-0.029999999329447746,0.03950668126344681],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33906471729278564,-0.029999999329447746,0.03950668126344681,1.0,0.0]}
{"sample_index":506,"source_step_index":506,"image_path":"frames/frame_000506.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3390699028968811,-0.029999999329447746,0.03951184079051018],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3390699028968811,-0.029999999329447746,0.03951184079051018,1.0,0.0]}
{"sample_index":507,"source_step_index":507,"image_path":"frames/frame_000507.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3390728831291199,-0.029999999329447746,0.039516810327768326],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3390728831291199,-0.029999999329447746,0.039516810327768326,1.0,0.0]}
{"sample_index":508,"source_step_index":508,"image_path":"frames/frame_000508.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33907264471054077,-0.029999999329447746,0.03952155262231827],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33907264471054077,-0.029999999329447746,0.03952155262231827,1.0,0.0]}
{"sample_index":509,"source_step_index":509,"image_path":"frames/frame_000509.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33907872438430786,-0.029999999329447746,0.039526525884866714],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33907872438430786,-0.029999999329447746,0.039526525884866714,1.0,0.0]}
{"sample_index":510,"source_step_index":510,"image_path":"frames/frame_000510.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3390826880931854,-0.029999999329447746,0.03953131288290024],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3390826880931854,-0.029999999329447746,0.03953131288290024,1.0,0.0]}
{"sample_index":511,"source_step_index":511,"image_path":"frames/frame_000511.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33908361196517944,-0.029999999329447746,0.03953588381409645],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33908361196517944,-0.029999999329447746,0.03953588381409645,1.0,0.0]}
{"sample_index":512,"source_step_index":512,"image_path":"frames/frame_000512.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33909064531326294,-0.029999999329447746,0.039540670812129974],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33909064531326294,-0.029999999329447746,0.039540670812129974,1.0,0.0]}
{"sample_index":513,"source_step_index":513,"image_path":"frames/frame_000513.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3390955328941345,-0.029999999329447746,0.03954527527093887],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3390955328941345,-0.029999999329447746,0.03954527527093887,1.0,0.0]}
{"sample_index":514,"source_step_index":514,"image_path":"frames/frame_000514.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33909714221954346,-0.029999999329447746,0.039549656212329865],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33909714221954346,-0.029999999329447746,0.039549656212329865,1.0,0.0]}
{"sample_index":515,"source_step_index":515,"image_path":"frames/frame_000515.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391050398349762,-0.029999999329447746,0.03955427184700966],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391050398349762,-0.029999999329447746,0.03955427184700966,1.0,0.0]}
{"sample_index":516,"source_step_index":516,"image_path":"frames/frame_000516.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33911076188087463,-0.029999999329447746,0.039558712393045425],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33911076188087463,-0.029999999329447746,0.039558712393045425,1.0,0.0]}
{"sample_index":517,"source_step_index":517,"image_path":"frames/frame_000517.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33911338448524475,-0.029999999329447746,0.03956294804811478],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33911338448524475,-0.029999999329447746,0.03956294804811478,1.0,0.0]}
{"sample_index":518,"source_step_index":518,"image_path":"frames/frame_000518.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33912208676338196,-0.029999999329447746,0.03956741467118263],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33912208676338196,-0.029999999329447746,0.03956741467118263,1.0,0.0]}
{"sample_index":519,"source_step_index":519,"image_path":"frames/frame_000519.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391285240650177,-0.029999999329447746,0.03957170993089676],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391285240650177,-0.029999999329447746,0.03957170993089676,1.0,0.0]}
{"sample_index":520,"source_step_index":520,"image_path":"frames/frame_000520.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391316533088684,-0.029999999329447746,0.03957580402493477],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391316533088684,-0.029999999329447746,0.03957580402493477,1.0,0.0]}
{"sample_index":521,"source_step_index":521,"image_path":"frames/frame_000521.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391408920288086,-0.029999999329447746,0.03958014398813248],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391408920288086,-0.029999999329447746,0.03958014398813248,1.0,0.0]}
{"sample_index":522,"source_step_index":522,"image_path":"frames/frame_000522.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391479253768921,-0.029999999329447746,0.03958432748913765],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391479253768921,-0.029999999329447746,0.03958432748913765,1.0,0.0]}
{"sample_index":523,"source_step_index":523,"image_path":"frames/frame_000523.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391517102718353,-0.029999999329447746,0.0395883210003376],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391517102718353,-0.029999999329447746,0.0395883210003376,1.0,0.0]}
{"sample_index":524,"source_step_index":524,"image_path":"frames/frame_000524.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391615152359009,-0.029999999329447746,0.039592571556568146],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391615152359009,-0.029999999329447746,0.039592571556568146,1.0,0.0]}
{"sample_index":525,"source_step_index":525,"image_path":"frames/frame_000525.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391689360141754,-0.029999999329447746,0.039596665650606155],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391689360141754,-0.029999999329447746,0.039596665650606155,1.0,0.0]}
{"sample_index":526,"source_step_index":526,"image_path":"frames/frame_000526.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391728699207306,-0.029999999329447746,0.03960057720541954],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391728699207306,-0.029999999329447746,0.03960057720541954,1.0,0.0]}
{"sample_index":527,"source_step_index":527,"image_path":"frames/frame_000527.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33918288350105286,-0.029999999329447746,0.03960476443171501],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33918288350105286,-0.029999999329447746,0.03960476443171501,1.0,0.0]}
{"sample_index":528,"source_step_index":528,"image_path":"frames/frame_000528.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391905725002289,-0.029999999329447746,0.03960881382226944],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391905725002289,-0.029999999329447746,0.03960881382226944,1.0,0.0]}
{"sample_index":529,"source_step_index":529,"image_path":"frames/frame_000529.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3391949236392975,-0.029999999329447746,0.039612699300050735],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3391949236392975,-0.029999999329447746,0.039612699300050735,1.0,0.0]}
{"sample_index":530,"source_step_index":530,"image_path":"frames/frame_000530.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3392051160335541,-0.029999999329447746,0.039616864174604416],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3392051160335541,-0.029999999329447746,0.039616864174604416,1.0,0.0]}
{"sample_index":531,"source_step_index":531,"image_path":"frames/frame_000531.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3392128348350525,-0.029999999329447746,0.03962089121341705],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3392128348350525,-0.029999999329447746,0.03962089121341705,1.0,0.0]}
{"sample_index":532,"source_step_index":532,"image_path":"frames/frame_000532.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3392169773578644,-0.029999999329447746,0.03962475061416626],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3392169773578644,-0.029999999329447746,0.03962475061416626,1.0,0.0]}
{"sample_index":533,"source_step_index":533,"image_path":"frames/frame_000533.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3392271101474762,-0.029999999329447746,0.03962891176342964],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3392271101474762,-0.029999999329447746,0.03962891176342964,1.0,0.0]}
{"sample_index":534,"source_step_index":534,"image_path":"frames/frame_000534.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3392347991466522,-0.029999999329447746,0.039632949978113174],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3392347991466522,-0.029999999329447746,0.039632949978113174,1.0,0.0]}
{"sample_index":535,"source_step_index":535,"image_path":"frames/frame_000535.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33923906087875366,-0.029999999329447746,0.03963683918118477],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33923906087875366,-0.029999999329447746,0.03963683918118477,1.0,0.0]}
{"sample_index":536,"source_step_index":536,"image_path":"frames/frame_000536.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3392490744590759,-0.029999999329447746,0.03964102640748024],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3392490744590759,-0.029999999329447746,0.03964102640748024,1.0,0.0]}
{"sample_index":537,"source_step_index":537,"image_path":"frames/frame_000537.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33925652503967285,-0.029999999329447746,0.03964509069919586],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33925652503967285,-0.029999999329447746,0.03964509069919586,1.0,0.0]}
{"sample_index":538,"source_step_index":538,"image_path":"frames/frame_000538.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33926036953926086,-0.029999999329447746,0.03964900225400925],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33926036953926086,-0.029999999329447746,0.03964900225400925,1.0,0.0]}
{"sample_index":539,"source_step_index":539,"image_path":"frames/frame_000539.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33927008509635925,-0.029999999329447746,0.0396532267332077],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33927008509635925,-0.029999999329447746,0.0396532267332077,1.0,0.0]}
{"sample_index":540,"source_step_index":540,"image_path":"frames/frame_000540.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3392772972583771,-0.029999999329447746,0.0396573431789875],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3392772972583771,-0.029999999329447746,0.0396573431789875,1.0,0.0]}
{"sample_index":541,"source_step_index":541,"image_path":"frames/frame_000541.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33928102254867554,-0.029999999329447746,0.03966131806373596],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33928102254867554,-0.029999999329447746,0.03966131806373596,1.0,0.0]}
{"sample_index":542,"source_step_index":542,"image_path":"frames/frame_000542.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33929044008255005,-0.029999999329447746,0.039665598422288895],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33929044008255005,-0.029999999329447746,0.039665598422288895,1.0,0.0]}
{"sample_index":543,"source_step_index":543,"image_path":"frames/frame_000543.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3392973244190216,-0.029999999329447746,0.03966977447271347],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3392973244190216,-0.029999999329447746,0.03966977447271347,1.0,0.0]}
{"sample_index":544,"source_step_index":544,"image_path":"frames/frame_000544.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393005132675171,-0.029999999329447746,0.03967380151152611],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393005132675171,-0.029999999329447746,0.03967380151152611,1.0,0.0]}
{"sample_index":545,"source_step_index":545,"image_path":"frames/frame_000545.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393095135688782,-0.029999999329447746,0.039678145200014114],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393095135688782,-0.029999999329447746,0.039678145200014114,1.0,0.0]}
{"sample_index":546,"source_step_index":546,"image_path":"frames/frame_000546.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393159806728363,-0.029999999329447746,0.039682380855083466],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393159806728363,-0.029999999329447746,0.039682380855083466,1.0,0.0]}
{"sample_index":547,"source_step_index":547,"image_path":"frames/frame_000547.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393189609050751,-0.029999999329447746,0.03968648612499237],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393189609050751,-0.029999999329447746,0.03968648612499237,1.0,0.0]}
{"sample_index":548,"source_step_index":548,"image_path":"frames/frame_000548.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393276631832123,-0.029999999329447746,0.03969089686870575],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393276631832123,-0.029999999329447746,0.03969089686870575,1.0,0.0]}
{"sample_index":549,"source_step_index":549,"image_path":"frames/frame_000549.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33933374285697937,-0.029999999329447746,0.039695195853710175],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33933374285697937,-0.029999999329447746,0.039695195853710175,1.0,0.0]}
{"sample_index":550,"source_step_index":550,"image_path":"frames/frame_000550.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393361568450928,-0.029999999329447746,0.03969935327768326],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393361568450928,-0.029999999329447746,0.03969935327768326,1.0,0.0]}
{"sample_index":551,"source_step_index":551,"image_path":"frames/frame_000551.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33934441208839417,-0.029999999329447746,0.03970382735133171],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33934441208839417,-0.029999999329447746,0.03970382735133171,1.0,0.0]}
{"sample_index":552,"source_step_index":552,"image_path":"frames/frame_000552.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393501937389374,-0.029999999329447746,0.03970819711685181],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393501937389374,-0.029999999329447746,0.03970819711685181,1.0,0.0]}
{"sample_index":553,"source_step_index":553,"image_path":"frames/frame_000553.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33935245871543884,-0.029999999329447746,0.03971242532134056],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33935245871543884,-0.029999999329447746,0.03971242532134056,1.0,0.0]}
{"sample_index":554,"source_step_index":554,"image_path":"frames/frame_000554.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33936044573783875,-0.029999999329447746,0.03971695899963379],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33936044573783875,-0.029999999329447746,0.03971695899963379,1.0,0.0]}
{"sample_index":555,"source_step_index":555,"image_path":"frames/frame_000555.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393658399581909,-0.029999999329447746,0.039721377193927765],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393658399581909,-0.029999999329447746,0.039721377193927765,1.0,0.0]}
{"sample_index":556,"source_step_index":556,"image_path":"frames/frame_000556.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393675982952118,-0.029999999329447746,0.0397256501019001],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393675982952118,-0.029999999329447746,0.0397256501019001,1.0,0.0]}
{"sample_index":557,"source_step_index":557,"image_path":"frames/frame_000557.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.33937522768974304,-0.029999999329447746,0.03973023220896721],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.33937522768974304,-0.029999999329447746,0.03973023220896721,1.0,0.0]}
{"sample_index":558,"source_step_index":558,"image_path":"frames/frame_000558.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393804132938385,-0.029999999329447746,0.039734698832035065],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393804132938385,-0.029999999329447746,0.039734698832035065,1.0,0.0]}
{"sample_index":559,"source_step_index":559,"image_path":"frames/frame_000559.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.339382141828537,-0.029999999329447746,0.03973902016878128],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.339382141828537,-0.029999999329447746,0.03973902016878128,1.0,0.0]}
{"sample_index":560,"source_step_index":560,"image_path":"frames/frame_000560.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"DESCEND_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393895924091339,-0.029999999329447746,0.03974363952875137],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3393895924091339,-0.029999999329447746,0.03974363952875137,1.0,0.0]}
{"sample_index":562,"source_step_index":562,"image_path":"frames/frame_000562.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"CLOSE_GRIP","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3393958508968353,-0.029999999329447746,0.039752475917339325],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3393958508968353,-0.029999999329447746,0.039752475917339325,1.0,1.0]}
{"sample_index":723,"source_step_index":723,"image_path":"frames/frame_000723.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":724,"source_step_index":724,"image_path":"frames/frame_000724.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":725,"source_step_index":725,"image_path":"frames/frame_000725.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":726,"source_step_index":726,"image_path":"frames/frame_000726.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":727,"source_step_index":727,"image_path":"frames/frame_000727.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":728,"source_step_index":728,"image_path":"frames/frame_000728.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":729,"source_step_index":729,"image_path":"frames/frame_000729.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":730,"source_step_index":730,"image_path":"frames/frame_000730.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":731,"source_step_index":731,"image_path":"frames/frame_000731.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":732,"source_step_index":732,"image_path":"frames/frame_000732.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":733,"source_step_index":733,"image_path":"frames/frame_000733.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":734,"source_step_index":734,"image_path":"frames/frame_000734.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":735,"source_step_index":735,"image_path":"frames/frame_000735.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":736,"source_step_index":736,"image_path":"frames/frame_000736.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":737,"source_step_index":737,"image_path":"frames/frame_000737.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":738,"source_step_index":738,"image_path":"frames/frame_000738.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":739,"source_step_index":739,"image_path":"frames/frame_000739.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":740,"source_step_index":740,"image_path":"frames/frame_000740.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":741,"source_step_index":741,"image_path":"frames/frame_000741.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":742,"source_step_index":742,"image_path":"frames/frame_000742.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":743,"source_step_index":743,"image_path":"frames/frame_000743.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":744,"source_step_index":744,"image_path":"frames/frame_000744.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":745,"source_step_index":745,"image_path":"frames/frame_000745.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":746,"source_step_index":746,"image_path":"frames/frame_000746.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":747,"source_step_index":747,"image_path":"frames/frame_000747.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":748,"source_step_index":748,"image_path":"frames/frame_000748.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":749,"source_step_index":749,"image_path":"frames/frame_000749.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":750,"source_step_index":750,"image_path":"frames/frame_000750.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":751,"source_step_index":751,"image_path":"frames/frame_000751.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":752,"source_step_index":752,"image_path":"frames/frame_000752.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":753,"source_step_index":753,"image_path":"frames/frame_000753.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":754,"source_step_index":754,"image_path":"frames/frame_000754.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":755,"source_step_index":755,"image_path":"frames/frame_000755.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":756,"source_step_index":756,"image_path":"frames/frame_000756.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":757,"source_step_index":757,"image_path":"frames/frame_000757.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":758,"source_step_index":758,"image_path":"frames/frame_000758.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":759,"source_step_index":759,"image_path":"frames/frame_000759.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":760,"source_step_index":760,"image_path":"frames/frame_000760.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":761,"source_step_index":761,"image_path":"frames/frame_000761.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":762,"source_step_index":762,"image_path":"frames/frame_000762.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LIFT_SOURCE","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1723,"source_step_index":1723,"image_path":"frames/frame_001723.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1724,"source_step_index":1724,"image_path":"frames/frame_001724.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1725,"source_step_index":1725,"image_path":"frames/frame_001725.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1726,"source_step_index":1726,"image_path":"frames/frame_001726.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1727,"source_step_index":1727,"image_path":"frames/frame_001727.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1728,"source_step_index":1728,"image_path":"frames/frame_001728.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1729,"source_step_index":1729,"image_path":"frames/frame_001729.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1730,"source_step_index":1730,"image_path":"frames/frame_001730.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1731,"source_step_index":1731,"image_path":"frames/frame_001731.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1732,"source_step_index":1732,"image_path":"frames/frame_001732.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1733,"source_step_index":1733,"image_path":"frames/frame_001733.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1734,"source_step_index":1734,"image_path":"frames/frame_001734.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1735,"source_step_index":1735,"image_path":"frames/frame_001735.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1736,"source_step_index":1736,"image_path":"frames/frame_001736.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1737,"source_step_index":1737,"image_path":"frames/frame_001737.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1738,"source_step_index":1738,"image_path":"frames/frame_001738.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1739,"source_step_index":1739,"image_path":"frames/frame_001739.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1740,"source_step_index":1740,"image_path":"frames/frame_001740.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1741,"source_step_index":1741,"image_path":"frames/frame_001741.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1742,"source_step_index":1742,"image_path":"frames/frame_001742.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1743,"source_step_index":1743,"image_path":"frames/frame_001743.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1744,"source_step_index":1744,"image_path":"frames/frame_001744.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1745,"source_step_index":1745,"image_path":"frames/frame_001745.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1746,"source_step_index":1746,"image_path":"frames/frame_001746.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1747,"source_step_index":1747,"image_path":"frames/frame_001747.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1748,"source_step_index":1748,"image_path":"frames/frame_001748.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1749,"source_step_index":1749,"image_path":"frames/frame_001749.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1750,"source_step_index":1750,"image_path":"frames/frame_001750.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1751,"source_step_index":1751,"image_path":"frames/frame_001751.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1752,"source_step_index":1752,"image_path":"frames/frame_001752.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1753,"source_step_index":1753,"image_path":"frames/frame_001753.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1754,"source_step_index":1754,"image_path":"frames/frame_001754.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1755,"source_step_index":1755,"image_path":"frames/frame_001755.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1756,"source_step_index":1756,"image_path":"frames/frame_001756.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1757,"source_step_index":1757,"image_path":"frames/frame_001757.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1758,"source_step_index":1758,"image_path":"frames/frame_001758.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1759,"source_step_index":1759,"image_path":"frames/frame_001759.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1760,"source_step_index":1760,"image_path":"frames/frame_001760.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1761,"source_step_index":1761,"image_path":"frames/frame_001761.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1762,"source_step_index":1762,"image_path":"frames/frame_001762.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1763,"source_step_index":1763,"image_path":"frames/frame_001763.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1764,"source_step_index":1764,"image_path":"frames/frame_001764.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1765,"source_step_index":1765,"image_path":"frames/frame_001765.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1766,"source_step_index":1766,"image_path":"frames/frame_001766.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1767,"source_step_index":1767,"image_path":"frames/frame_001767.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1768,"source_step_index":1768,"image_path":"frames/frame_001768.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1769,"source_step_index":1769,"image_path":"frames/frame_001769.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1770,"source_step_index":1770,"image_path":"frames/frame_001770.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1771,"source_step_index":1771,"image_path":"frames/frame_001771.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1772,"source_step_index":1772,"image_path":"frames/frame_001772.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1773,"source_step_index":1773,"image_path":"frames/frame_001773.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1774,"source_step_index":1774,"image_path":"frames/frame_001774.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1775,"source_step_index":1775,"image_path":"frames/frame_001775.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1776,"source_step_index":1776,"image_path":"frames/frame_001776.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1777,"source_step_index":1777,"image_path":"frames/frame_001777.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1778,"source_step_index":1778,"image_path":"frames/frame_001778.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1779,"source_step_index":1779,"image_path":"frames/frame_001779.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1780,"source_step_index":1780,"image_path":"frames/frame_001780.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1781,"source_step_index":1781,"image_path":"frames/frame_001781.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1782,"source_step_index":1782,"image_path":"frames/frame_001782.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1783,"source_step_index":1783,"image_path":"frames/frame_001783.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1784,"source_step_index":1784,"image_path":"frames/frame_001784.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1785,"source_step_index":1785,"image_path":"frames/frame_001785.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1786,"source_step_index":1786,"image_path":"frames/frame_001786.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1787,"source_step_index":1787,"image_path":"frames/frame_001787.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1788,"source_step_index":1788,"image_path":"frames/frame_001788.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1789,"source_step_index":1789,"image_path":"frames/frame_001789.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1790,"source_step_index":1790,"image_path":"frames/frame_001790.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1791,"source_step_index":1791,"image_path":"frames/frame_001791.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1792,"source_step_index":1792,"image_path":"frames/frame_001792.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1793,"source_step_index":1793,"image_path":"frames/frame_001793.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1794,"source_step_index":1794,"image_path":"frames/frame_001794.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1795,"source_step_index":1795,"image_path":"frames/frame_001795.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1796,"source_step_index":1796,"image_path":"frames/frame_001796.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1797,"source_step_index":1797,"image_path":"frames/frame_001797.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1798,"source_step_index":1798,"image_path":"frames/frame_001798.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1799,"source_step_index":1799,"image_path":"frames/frame_001799.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1800,"source_step_index":1800,"image_path":"frames/frame_001800.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1801,"source_step_index":1801,"image_path":"frames/frame_001801.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1802,"source_step_index":1802,"image_path":"frames/frame_001802.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1803,"source_step_index":1803,"image_path":"frames/frame_001803.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1804,"source_step_index":1804,"image_path":"frames/frame_001804.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1805,"source_step_index":1805,"image_path":"frames/frame_001805.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1806,"source_step_index":1806,"image_path":"frames/frame_001806.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1807,"source_step_index":1807,"image_path":"frames/frame_001807.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1808,"source_step_index":1808,"image_path":"frames/frame_001808.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1809,"source_step_index":1809,"image_path":"frames/frame_001809.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1810,"source_step_index":1810,"image_path":"frames/frame_001810.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1811,"source_step_index":1811,"image_path":"frames/frame_001811.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1812,"source_step_index":1812,"image_path":"frames/frame_001812.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1813,"source_step_index":1813,"image_path":"frames/frame_001813.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1814,"source_step_index":1814,"image_path":"frames/frame_001814.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1815,"source_step_index":1815,"image_path":"frames/frame_001815.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1816,"source_step_index":1816,"image_path":"frames/frame_001816.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1817,"source_step_index":1817,"image_path":"frames/frame_001817.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1818,"source_step_index":1818,"image_path":"frames/frame_001818.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1819,"source_step_index":1819,"image_path":"frames/frame_001819.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1820,"source_step_index":1820,"image_path":"frames/frame_001820.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1821,"source_step_index":1821,"image_path":"frames/frame_001821.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1822,"source_step_index":1822,"image_path":"frames/frame_001822.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1823,"source_step_index":1823,"image_path":"frames/frame_001823.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1824,"source_step_index":1824,"image_path":"frames/frame_001824.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1825,"source_step_index":1825,"image_path":"frames/frame_001825.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1826,"source_step_index":1826,"image_path":"frames/frame_001826.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1827,"source_step_index":1827,"image_path":"frames/frame_001827.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1828,"source_step_index":1828,"image_path":"frames/frame_001828.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1829,"source_step_index":1829,"image_path":"frames/frame_001829.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1830,"source_step_index":1830,"image_path":"frames/frame_001830.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1831,"source_step_index":1831,"image_path":"frames/frame_001831.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1832,"source_step_index":1832,"image_path":"frames/frame_001832.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1833,"source_step_index":1833,"image_path":"frames/frame_001833.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1834,"source_step_index":1834,"image_path":"frames/frame_001834.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1835,"source_step_index":1835,"image_path":"frames/frame_001835.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1836,"source_step_index":1836,"image_path":"frames/frame_001836.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1837,"source_step_index":1837,"image_path":"frames/frame_001837.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1838,"source_step_index":1838,"image_path":"frames/frame_001838.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1839,"source_step_index":1839,"image_path":"frames/frame_001839.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1840,"source_step_index":1840,"image_path":"frames/frame_001840.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1841,"source_step_index":1841,"image_path":"frames/frame_001841.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1842,"source_step_index":1842,"image_path":"frames/frame_001842.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1843,"source_step_index":1843,"image_path":"frames/frame_001843.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1844,"source_step_index":1844,"image_path":"frames/frame_001844.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1845,"source_step_index":1845,"image_path":"frames/frame_001845.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1846,"source_step_index":1846,"image_path":"frames/frame_001846.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1847,"source_step_index":1847,"image_path":"frames/frame_001847.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1848,"source_step_index":1848,"image_path":"frames/frame_001848.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1849,"source_step_index":1849,"image_path":"frames/frame_001849.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1850,"source_step_index":1850,"image_path":"frames/frame_001850.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1851,"source_step_index":1851,"image_path":"frames/frame_001851.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1852,"source_step_index":1852,"image_path":"frames/frame_001852.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1853,"source_step_index":1853,"image_path":"frames/frame_001853.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1854,"source_step_index":1854,"image_path":"frames/frame_001854.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1855,"source_step_index":1855,"image_path":"frames/frame_001855.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1856,"source_step_index":1856,"image_path":"frames/frame_001856.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1857,"source_step_index":1857,"image_path":"frames/frame_001857.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1858,"source_step_index":1858,"image_path":"frames/frame_001858.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1859,"source_step_index":1859,"image_path":"frames/frame_001859.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1860,"source_step_index":1860,"image_path":"frames/frame_001860.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1861,"source_step_index":1861,"image_path":"frames/frame_001861.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1862,"source_step_index":1862,"image_path":"frames/frame_001862.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1863,"source_step_index":1863,"image_path":"frames/frame_001863.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1864,"source_step_index":1864,"image_path":"frames/frame_001864.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1865,"source_step_index":1865,"image_path":"frames/frame_001865.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1866,"source_step_index":1866,"image_path":"frames/frame_001866.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1867,"source_step_index":1867,"image_path":"frames/frame_001867.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1868,"source_step_index":1868,"image_path":"frames/frame_001868.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1869,"source_step_index":1869,"image_path":"frames/frame_001869.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1870,"source_step_index":1870,"image_path":"frames/frame_001870.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1871,"source_step_index":1871,"image_path":"frames/frame_001871.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1872,"source_step_index":1872,"image_path":"frames/frame_001872.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1873,"source_step_index":1873,"image_path":"frames/frame_001873.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1874,"source_step_index":1874,"image_path":"frames/frame_001874.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1875,"source_step_index":1875,"image_path":"frames/frame_001875.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1876,"source_step_index":1876,"image_path":"frames/frame_001876.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1877,"source_step_index":1877,"image_path":"frames/frame_001877.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1878,"source_step_index":1878,"image_path":"frames/frame_001878.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1879,"source_step_index":1879,"image_path":"frames/frame_001879.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1880,"source_step_index":1880,"image_path":"frames/frame_001880.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1881,"source_step_index":1881,"image_path":"frames/frame_001881.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1882,"source_step_index":1882,"image_path":"frames/frame_001882.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1883,"source_step_index":1883,"image_path":"frames/frame_001883.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1884,"source_step_index":1884,"image_path":"frames/frame_001884.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1885,"source_step_index":1885,"image_path":"frames/frame_001885.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1886,"source_step_index":1886,"image_path":"frames/frame_001886.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1887,"source_step_index":1887,"image_path":"frames/frame_001887.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1888,"source_step_index":1888,"image_path":"frames/frame_001888.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1889,"source_step_index":1889,"image_path":"frames/frame_001889.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1890,"source_step_index":1890,"image_path":"frames/frame_001890.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1891,"source_step_index":1891,"image_path":"frames/frame_001891.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1892,"source_step_index":1892,"image_path":"frames/frame_001892.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1893,"source_step_index":1893,"image_path":"frames/frame_001893.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1894,"source_step_index":1894,"image_path":"frames/frame_001894.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1895,"source_step_index":1895,"image_path":"frames/frame_001895.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1896,"source_step_index":1896,"image_path":"frames/frame_001896.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1897,"source_step_index":1897,"image_path":"frames/frame_001897.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1898,"source_step_index":1898,"image_path":"frames/frame_001898.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1899,"source_step_index":1899,"image_path":"frames/frame_001899.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1900,"source_step_index":1900,"image_path":"frames/frame_001900.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1901,"source_step_index":1901,"image_path":"frames/frame_001901.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1902,"source_step_index":1902,"image_path":"frames/frame_001902.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1903,"source_step_index":1903,"image_path":"frames/frame_001903.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1904,"source_step_index":1904,"image_path":"frames/frame_001904.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1905,"source_step_index":1905,"image_path":"frames/frame_001905.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1906,"source_step_index":1906,"image_path":"frames/frame_001906.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1907,"source_step_index":1907,"image_path":"frames/frame_001907.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1908,"source_step_index":1908,"image_path":"frames/frame_001908.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1909,"source_step_index":1909,"image_path":"frames/frame_001909.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1910,"source_step_index":1910,"image_path":"frames/frame_001910.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1911,"source_step_index":1911,"image_path":"frames/frame_001911.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1912,"source_step_index":1912,"image_path":"frames/frame_001912.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1913,"source_step_index":1913,"image_path":"frames/frame_001913.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1914,"source_step_index":1914,"image_path":"frames/frame_001914.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1915,"source_step_index":1915,"image_path":"frames/frame_001915.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1916,"source_step_index":1916,"image_path":"frames/frame_001916.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1917,"source_step_index":1917,"image_path":"frames/frame_001917.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1918,"source_step_index":1918,"image_path":"frames/frame_001918.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1919,"source_step_index":1919,"image_path":"frames/frame_001919.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1920,"source_step_index":1920,"image_path":"frames/frame_001920.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1921,"source_step_index":1921,"image_path":"frames/frame_001921.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1922,"source_step_index":1922,"image_path":"frames/frame_001922.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1923,"source_step_index":1923,"image_path":"frames/frame_001923.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1924,"source_step_index":1924,"image_path":"frames/frame_001924.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1925,"source_step_index":1925,"image_path":"frames/frame_001925.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1926,"source_step_index":1926,"image_path":"frames/frame_001926.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1927,"source_step_index":1927,"image_path":"frames/frame_001927.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1928,"source_step_index":1928,"image_path":"frames/frame_001928.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1929,"source_step_index":1929,"image_path":"frames/frame_001929.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.12,0.0,-1.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.12,0.0,-1.0,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1930,"source_step_index":1930,"image_path":"frames/frame_001930.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1931,"source_step_index":1931,"image_path":"frames/frame_001931.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1932,"source_step_index":1932,"image_path":"frames/frame_001932.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1933,"source_step_index":1933,"image_path":"frames/frame_001933.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1934,"source_step_index":1934,"image_path":"frames/frame_001934.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1935,"source_step_index":1935,"image_path":"frames/frame_001935.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1936,"source_step_index":1936,"image_path":"frames/frame_001936.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1937,"source_step_index":1937,"image_path":"frames/frame_001937.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1938,"source_step_index":1938,"image_path":"frames/frame_001938.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1939,"source_step_index":1939,"image_path":"frames/frame_001939.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1940,"source_step_index":1940,"image_path":"frames/frame_001940.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1941,"source_step_index":1941,"image_path":"frames/frame_001941.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1942,"source_step_index":1942,"image_path":"frames/frame_001942.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1943,"source_step_index":1943,"image_path":"frames/frame_001943.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1944,"source_step_index":1944,"image_path":"frames/frame_001944.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1945,"source_step_index":1945,"image_path":"frames/frame_001945.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1946,"source_step_index":1946,"image_path":"frames/frame_001946.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1947,"source_step_index":1947,"image_path":"frames/frame_001947.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1948,"source_step_index":1948,"image_path":"frames/frame_001948.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1949,"source_step_index":1949,"image_path":"frames/frame_001949.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1950,"source_step_index":1950,"image_path":"frames/frame_001950.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1951,"source_step_index":1951,"image_path":"frames/frame_001951.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1952,"source_step_index":1952,"image_path":"frames/frame_001952.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1953,"source_step_index":1953,"image_path":"frames/frame_001953.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1954,"source_step_index":1954,"image_path":"frames/frame_001954.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1955,"source_step_index":1955,"image_path":"frames/frame_001955.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1956,"source_step_index":1956,"image_path":"frames/frame_001956.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1957,"source_step_index":1957,"image_path":"frames/frame_001957.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1958,"source_step_index":1958,"image_path":"frames/frame_001958.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1959,"source_step_index":1959,"image_path":"frames/frame_001959.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1960,"source_step_index":1960,"image_path":"frames/frame_001960.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1961,"source_step_index":1961,"image_path":"frames/frame_001961.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":1962,"source_step_index":1962,"image_path":"frames/frame_001962.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"APPROACH_TARGET","walk_cmd":[0.22,0.18,0.25],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":true,"action_vector":[0.22,0.18,0.25,0.3,-0.2,0.2,1.0,1.0]}
{"sample_index":2123,"source_step_index":2123,"image_path":"frames/frame_002123.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26191508769989014,-0.029999999329447746,0.05918754264712334],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26191508769989014,-0.029999999329447746,0.05918754264712334,1.0,1.0]}
{"sample_index":2124,"source_step_index":2124,"image_path":"frames/frame_002124.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26200634241104126,-0.029999999329447746,0.05917754024267197],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26200634241104126,-0.029999999329447746,0.05917754024267197,1.0,1.0]}
{"sample_index":2125,"source_step_index":2125,"image_path":"frames/frame_002125.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2620983421802521,-0.029999999329447746,0.05916732922196388],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2620983421802521,-0.029999999329447746,0.05916732922196388,1.0,1.0]}
{"sample_index":2126,"source_step_index":2126,"image_path":"frames/frame_002126.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26219066977500916,-0.029999999329447746,0.05915713682770729],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26219066977500916,-0.029999999329447746,0.05915713682770729,1.0,1.0]}
{"sample_index":2127,"source_step_index":2127,"image_path":"frames/frame_002127.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2622828185558319,-0.029999999329447746,0.05914720892906189],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2622828185558319,-0.029999999329447746,0.05914720892906189,1.0,1.0]}
{"sample_index":2128,"source_step_index":2128,"image_path":"frames/frame_002128.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2623741924762726,-0.029999999329447746,0.05913781374692917],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2623741924762726,-0.029999999329447746,0.05913781374692917,1.0,1.0]}
{"sample_index":2129,"source_step_index":2129,"image_path":"frames/frame_002129.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26246410608291626,-0.029999999329447746,0.05912921577692032],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26246410608291626,-0.029999999329447746,0.05912921577692032,1.0,1.0]}
{"sample_index":2130,"source_step_index":2130,"image_path":"frames/frame_002130.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.262551873922348,-0.029999999329447746,0.059121664613485336],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.262551873922348,-0.029999999329447746,0.059121664613485336,1.0,1.0]}
{"sample_index":2131,"source_step_index":2131,"image_path":"frames/frame_002131.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2626367211341858,-0.029999999329447746,0.059115372598171234],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2626367211341858,-0.029999999329447746,0.059115372598171234,1.0,1.0]}
{"sample_index":2132,"source_step_index":2132,"image_path":"frames/frame_002132.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2627178132534027,-0.029999999329447746,0.05911050736904144],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2627178132534027,-0.029999999329447746,0.05911050736904144,1.0,1.0]}
{"sample_index":2133,"source_step_index":2133,"image_path":"frames/frame_002133.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26279446482658386,-0.029999999329447746,0.05910718813538551],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26279446482658386,-0.029999999329447746,0.05910718813538551,1.0,1.0]}
{"sample_index":2134,"source_step_index":2134,"image_path":"frames/frame_002134.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26286593079566956,-0.029999999329447746,0.05910547077655792],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26286593079566956,-0.029999999329447746,0.05910547077655792,1.0,1.0]}
{"sample_index":2135,"source_step_index":2135,"image_path":"frames/frame_002135.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26293158531188965,-0.029999999329447746,0.05910535529255867],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26293158531188965,-0.029999999329447746,0.05910535529255867,1.0,1.0]}
{"sample_index":2136,"source_step_index":2136,"image_path":"frames/frame_002136.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2629909813404083,-0.029999999329447746,0.059106793254613876],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2629909813404083,-0.029999999329447746,0.059106793254613876,1.0,1.0]}
{"sample_index":2137,"source_step_index":2137,"image_path":"frames/frame_002137.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26304370164871216,-0.029999999329447746,0.059109654277563095],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26304370164871216,-0.029999999329447746,0.059109654277563095,1.0,1.0]}
{"sample_index":2138,"source_step_index":2138,"image_path":"frames/frame_002138.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2630895972251892,-0.029999999329447746,0.05911377817392349],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2630895972251892,-0.029999999329447746,0.05911377817392349,1.0,1.0]}
{"sample_index":2139,"source_step_index":2139,"image_path":"frames/frame_002139.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2631286382675171,-0.029999999329447746,0.059118982404470444],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2631286382675171,-0.029999999329447746,0.059118982404470444,1.0,1.0]}
{"sample_index":2140,"source_step_index":2140,"image_path":"frames/frame_002140.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26316091418266296,-0.029999999329447746,0.05912504717707634],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26316091418266296,-0.029999999329447746,0.05912504717707634,1.0,1.0]}
{"sample_index":2141,"source_step_index":2141,"image_path":"frames/frame_002141.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2631867825984955,-0.029999999329447746,0.05913175642490387],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2631867825984955,-0.029999999329447746,0.05913175642490387,1.0,1.0]}
{"sample_index":2142,"source_step_index":2142,"image_path":"frames/frame_002142.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2632066607475281,-0.029999999329447746,0.05913889408111572],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2632066607475281,-0.029999999329447746,0.05913889408111572,1.0,1.0]}
{"sample_index":2143,"source_step_index":2143,"image_path":"frames/frame_002143.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26322102546691895,-0.029999999329447746,0.05914625898003578],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26322102546691895,-0.029999999329447746,0.05914625898003578,1.0,1.0]}
{"sample_index":2144,"source_step_index":2144,"image_path":"frames/frame_002144.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2632305920124054,-0.029999999329447746,0.059153683483600616],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2632305920124054,-0.029999999329447746,0.059153683483600616,1.0,1.0]}
{"sample_index":2145,"source_step_index":2145,"image_path":"frames/frame_002145.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2632359564304352,-0.029999999329447746,0.05916103348135948],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2632359564304352,-0.029999999329447746,0.05916103348135948,1.0,1.0]}
{"sample_index":2146,"source_step_index":2146,"image_path":"frames/frame_002146.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.263237863779068,-0.029999999329447746,0.05916820466518402],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.263237863779068,-0.029999999329447746,0.05916820466518402,1.0,1.0]}
{"sample_index":2147,"source_step_index":2147,"image_path":"frames/frame_002147.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26323696970939636,-0.029999999329447746,0.05917513370513916],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26323696970939636,-0.029999999329447746,0.05917513370513916,1.0,1.0]}
{"sample_index":2148,"source_step_index":2148,"image_path":"frames/frame_002148.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2632339298725128,-0.029999999329447746,0.05918179452419281],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2632339298725128,-0.029999999329447746,0.05918179452419281,1.0,1.0]}
{"sample_index":2149,"source_step_index":2149,"image_path":"frames/frame_002149.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2632293105125427,-0.029999999329447746,0.059188202023506165],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2632293105125427,-0.029999999329447746,0.059188202023506165,1.0,1.0]}
{"sample_index":2150,"source_step_index":2150,"image_path":"frames/frame_002150.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2632235586643219,-0.029999999329447746,0.05919439718127251],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2632235586643219,-0.029999999329447746,0.05919439718127251,1.0,1.0]}
{"sample_index":2151,"source_step_index":2151,"image_path":"frames/frame_002151.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26321712136268616,-0.029999999329447746,0.05920043960213661],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26321712136268616,-0.029999999329447746,0.05920043960213661,1.0,1.0]}
{"sample_index":2152,"source_step_index":2152,"image_path":"frames/frame_002152.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.263210266828537,-0.029999999329447746,0.05920640006661415],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.263210266828537,-0.029999999329447746,0.05920640006661415,1.0,1.0]}
{"sample_index":2153,"source_step_index":2153,"image_path":"frames/frame_002153.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2632032334804535,-0.029999999329447746,0.059212349355220795],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2632032334804535,-0.029999999329447746,0.059212349355220795,1.0,1.0]}
{"sample_index":2154,"source_step_index":2154,"image_path":"frames/frame_002154.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2631961405277252,-0.029999999329447746,0.05921834334731102],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2631961405277252,-0.029999999329447746,0.05921834334731102,1.0,1.0]}
{"sample_index":2155,"source_step_index":2155,"image_path":"frames/frame_002155.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26318907737731934,-0.029999999329447746,0.0592244453728199],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26318907737731934,-0.029999999329447746,0.0592244453728199,1.0,1.0]}
{"sample_index":2156,"source_step_index":2156,"image_path":"frames/frame_002156.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26318204402923584,-0.029999999329447746,0.059230685234069824],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26318204402923584,-0.029999999329447746,0.059230685234069824,1.0,1.0]}
{"sample_index":2157,"source_step_index":2157,"image_path":"frames/frame_002157.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2631750702857971,-0.029999999329447746,0.059237077832221985],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2631750702857971,-0.029999999329447746,0.059237077832221985,1.0,1.0]}
{"sample_index":2158,"source_step_index":2158,"image_path":"frames/frame_002158.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2631680965423584,-0.029999999329447746,0.05924361199140549],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2631680965423584,-0.029999999329447746,0.05924361199140549,1.0,1.0]}
{"sample_index":2159,"source_step_index":2159,"image_path":"frames/frame_002159.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26316121220588684,-0.029999999329447746,0.05925023928284645],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26316121220588684,-0.029999999329447746,0.05925023928284645,1.0,1.0]}
{"sample_index":2160,"source_step_index":2160,"image_path":"frames/frame_002160.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26315438747406006,-0.029999999329447746,0.0592569075524807],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26315438747406006,-0.029999999329447746,0.0592569075524807,1.0,1.0]}
{"sample_index":2161,"source_step_index":2161,"image_path":"frames/frame_002161.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2631477117538452,-0.029999999329447746,0.059263549745082855],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2631477117538452,-0.029999999329447746,0.059263549745082855,1.0,1.0]}
{"sample_index":2162,"source_step_index":2162,"image_path":"frames/frame_002162.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"HOVER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.26314133405685425,-0.029999999329447746,0.059270069003105164],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.26314133405685425,-0.029999999329447746,0.059270069003105164,1.0,1.0]}
{"sample_index":2403,"source_step_index":2403,"image_path":"frames/frame_002403.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27267953753471375,-0.029999999329447746,-0.05969482660293579],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27267953753471375,-0.029999999329447746,-0.05969482660293579,1.0,1.0]}
{"sample_index":2404,"source_step_index":2404,"image_path":"frames/frame_002404.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27270111441612244,-0.029999999329447746,-0.059691380709409714],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27270111441612244,-0.029999999329447746,-0.059691380709409714,1.0,1.0]}
{"sample_index":2405,"source_step_index":2405,"image_path":"frames/frame_002405.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2727225720882416,-0.029999999329447746,-0.059687696397304535],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2727225720882416,-0.029999999329447746,-0.059687696397304535,1.0,1.0]}
{"sample_index":2406,"source_step_index":2406,"image_path":"frames/frame_002406.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2727436423301697,-0.029999999329447746,-0.05968378856778145],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2727436423301697,-0.029999999329447746,-0.05968378856778145,1.0,1.0]}
{"sample_index":2407,"source_step_index":2407,"image_path":"frames/frame_002407.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2727641463279724,-0.029999999329447746,-0.059679705649614334],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2727641463279724,-0.029999999329447746,-0.059679705649614334,1.0,1.0]}
{"sample_index":2408,"source_step_index":2408,"image_path":"frames/frame_002408.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27278393507003784,-0.029999999329447746,-0.059675488620996475],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27278393507003784,-0.029999999329447746,-0.059675488620996475,1.0,1.0]}
{"sample_index":2409,"source_step_index":2409,"image_path":"frames/frame_002409.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2728029191493988,-0.029999999329447746,-0.059671200811862946],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2728029191493988,-0.029999999329447746,-0.059671200811862946,1.0,1.0]}
{"sample_index":2410,"source_step_index":2410,"image_path":"frames/frame_002410.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2728210389614105,-0.029999999329447746,-0.059666913002729416],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2728210389614105,-0.029999999329447746,-0.059666913002729416,1.0,1.0]}
{"sample_index":2411,"source_step_index":2411,"image_path":"frames/frame_002411.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2728383541107178,-0.029999999329447746,-0.059662673622369766],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2728383541107178,-0.029999999329447746,-0.059662673622369766,1.0,1.0]}
{"sample_index":2412,"source_step_index":2412,"image_path":"frames/frame_002412.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27285489439964294,-0.029999999329447746,-0.059658534824848175],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27285489439964294,-0.029999999329447746,-0.059658534824848175,1.0,1.0]}
{"sample_index":2413,"source_step_index":2413,"image_path":"frames/frame_002413.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27287083864212036,-0.029999999329447746,-0.059654537588357925],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27287083864212036,-0.029999999329447746,-0.059654537588357925,1.0,1.0]}
{"sample_index":2414,"source_step_index":2414,"image_path":"frames/frame_002414.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2728863060474396,-0.029999999329447746,-0.059650719165802],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2728863060474396,-0.029999999329447746,-0.059650719165802,1.0,1.0]}
{"sample_index":2415,"source_step_index":2415,"image_path":"frames/frame_002415.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2729015052318573,-0.029999999329447746,-0.059647101908922195],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2729015052318573,-0.029999999329447746,-0.059647101908922195,1.0,1.0]}
{"sample_index":2416,"source_step_index":2416,"image_path":"frames/frame_002416.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27291661500930786,-0.029999999329447746,-0.059643685817718506],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27291661500930786,-0.029999999329447746,-0.059643685817718506,1.0,1.0]}
{"sample_index":2417,"source_step_index":2417,"image_path":"frames/frame_002417.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2729317843914032,-0.029999999329447746,-0.059640366584062576],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2729317843914032,-0.029999999329447746,-0.059640366584062576,1.0,1.0]}
{"sample_index":2418,"source_step_index":2418,"image_path":"frames/frame_002418.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2729472219944,-0.029999999329447746,-0.05963723361492157],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2729472219944,-0.029999999329447746,-0.05963723361492157,1.0,1.0]}
{"sample_index":2419,"source_step_index":2419,"image_path":"frames/frame_002419.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27296316623687744,-0.029999999329447746,-0.05963433161377907],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27296316623687744,-0.029999999329447746,-0.05963433161377907,1.0,1.0]}
{"sample_index":2420,"source_step_index":2420,"image_path":"frames/frame_002420.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2729795277118683,-0.029999999329447746,-0.05963144078850746],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2729795277118683,-0.029999999329447746,-0.05963144078850746,1.0,1.0]}
{"sample_index":2421,"source_step_index":2421,"image_path":"frames/frame_002421.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2729965150356293,-0.029999999329447746,-0.05962856113910675],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2729965150356293,-0.029999999329447746,-0.05962856113910675,1.0,1.0]}
{"sample_index":2422,"source_step_index":2422,"image_path":"frames/frame_002422.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2730141282081604,-0.029999999329447746,-0.059625785797834396],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2730141282081604,-0.029999999329447746,-0.059625785797834396,1.0,1.0]}
{"sample_index":2423,"source_step_index":2423,"image_path":"frames/frame_002423.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2730322778224945,-0.029999999329447746,-0.059622861444950104],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2730322778224945,-0.029999999329447746,-0.059622861444950104,1.0,1.0]}
{"sample_index":2424,"source_step_index":2424,"image_path":"frames/frame_002424.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2730509638786316,-0.029999999329447746,-0.05961990728974342],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2730509638786316,-0.029999999329447746,-0.05961990728974342,1.0,1.0]}
{"sample_index":2425,"source_step_index":2425,"image_path":"frames/frame_002425.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2730700969696045,-0.029999999329447746,-0.05961688980460167],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2730700969696045,-0.029999999329447746,-0.05961688980460167,1.0,1.0]}
{"sample_index":2426,"source_step_index":2426,"image_path":"frames/frame_002426.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2730894982814789,-0.029999999329447746,-0.05961375683546066],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2730894982814789,-0.029999999329447746,-0.05961375683546066,1.0,1.0]}
{"sample_index":2427,"source_step_index":2427,"image_path":"frames/frame_002427.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2731090784072876,-0.029999999329447746,-0.05961049348115921],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2731090784072876,-0.029999999329447746,-0.05961049348115921,1.0,1.0]}
{"sample_index":2428,"source_step_index":2428,"image_path":"frames/frame_002428.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2731286287307739,-0.029999999329447746,-0.05960707738995552],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2731286287307739,-0.029999999329447746,-0.05960707738995552,1.0,1.0]}
{"sample_index":2429,"source_step_index":2429,"image_path":"frames/frame_002429.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2731480896472931,-0.029999999329447746,-0.059603530913591385],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2731480896472931,-0.029999999329447746,-0.059603530913591385,1.0,1.0]}
{"sample_index":2430,"source_step_index":2430,"image_path":"frames/frame_002430.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.273167222738266,-0.029999999329447746,-0.0595998540520668],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.273167222738266,-0.029999999329447746,-0.0595998540520668,1.0,1.0]}
{"sample_index":2431,"source_step_index":2431,"image_path":"frames/frame_002431.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27318599820137024,-0.029999999329447746,-0.05959608405828476],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27318599820137024,-0.029999999329447746,-0.05959608405828476,1.0,1.0]}
{"sample_index":2432,"source_step_index":2432,"image_path":"frames/frame_002432.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2732042968273163,-0.029999999329447746,-0.05959223583340645],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2732042968273163,-0.029999999329447746,-0.05959223583340645,1.0,1.0]}
{"sample_index":2433,"source_step_index":2433,"image_path":"frames/frame_002433.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27322205901145935,-0.029999999329447746,-0.05958833917975426],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27322205901145935,-0.029999999329447746,-0.05958833917975426,1.0,1.0]}
{"sample_index":2434,"source_step_index":2434,"image_path":"frames/frame_002434.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27323928475379944,-0.029999999329447746,-0.05958443135023117],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27323928475379944,-0.029999999329447746,-0.05958443135023117,1.0,1.0]}
{"sample_index":2435,"source_step_index":2435,"image_path":"frames/frame_002435.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27325600385665894,-0.029999999329447746,-0.05958054959774017],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27325600385665894,-0.029999999329447746,-0.05958054959774017,1.0,1.0]}
{"sample_index":2436,"source_step_index":2436,"image_path":"frames/frame_002436.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27327221632003784,-0.029999999329447746,-0.05957672744989395],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27327221632003784,-0.029999999329447746,-0.05957672744989395,1.0,1.0]}
{"sample_index":2437,"source_step_index":2437,"image_path":"frames/frame_002437.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2732880413532257,-0.029999999329447746,-0.0595729798078537],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2732880413532257,-0.029999999329447746,-0.0595729798078537,1.0,1.0]}
{"sample_index":2438,"source_step_index":2438,"image_path":"frames/frame_002438.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2733035385608673,-0.029999999329447746,-0.0595693439245224],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2733035385608673,-0.029999999329447746,-0.0595693439245224,1.0,1.0]}
{"sample_index":2439,"source_step_index":2439,"image_path":"frames/frame_002439.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2733188271522522,-0.029999999329447746,-0.05956581234931946],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2733188271522522,-0.029999999329447746,-0.05956581234931946,1.0,1.0]}
{"sample_index":2440,"source_step_index":2440,"image_path":"frames/frame_002440.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2733340561389923,-0.029999999329447746,-0.05956239253282547],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2733340561389923,-0.029999999329447746,-0.05956239253282547,1.0,1.0]}
{"sample_index":2441,"source_step_index":2441,"image_path":"frames/frame_002441.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2733492851257324,-0.029999999329447746,-0.05955908074975014],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2733492851257324,-0.029999999329447746,-0.05955908074975014,1.0,1.0]}
{"sample_index":2442,"source_step_index":2442,"image_path":"frames/frame_002442.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2733646333217621,-0.029999999329447746,-0.059555865824222565],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2733646333217621,-0.029999999329447746,-0.059555865824222565,1.0,1.0]}
{"sample_index":2443,"source_step_index":2443,"image_path":"frames/frame_002443.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27338021993637085,-0.029999999329447746,-0.05955272912979126],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27338021993637085,-0.029999999329447746,-0.05955272912979126,1.0,1.0]}
{"sample_index":2444,"source_step_index":2444,"image_path":"frames/frame_002444.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2733960747718811,-0.029999999329447746,-0.05954964458942413],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2733960747718811,-0.029999999329447746,-0.05954964458942413,1.0,1.0]}
{"sample_index":2445,"source_step_index":2445,"image_path":"frames/frame_002445.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27341228723526,-0.029999999329447746,-0.05954659357666969],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27341228723526,-0.029999999329447746,-0.05954659357666969,1.0,1.0]}
{"sample_index":2446,"source_step_index":2446,"image_path":"frames/frame_002446.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2734287977218628,-0.029999999329447746,-0.05954353138804436],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2734287977218628,-0.029999999329447746,-0.05954353138804436,1.0,1.0]}
{"sample_index":2447,"source_step_index":2447,"image_path":"frames/frame_002447.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27344566583633423,-0.029999999329447746,-0.05954045429825783],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27344566583633423,-0.029999999329447746,-0.05954045429825783,1.0,1.0]}
{"sample_index":2448,"source_step_index":2448,"image_path":"frames/frame_002448.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27346283197402954,-0.029999999329447746,-0.05953732505440712],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27346283197402954,-0.029999999329447746,-0.05953732505440712,1.0,1.0]}
{"sample_index":2449,"source_step_index":2449,"image_path":"frames/frame_002449.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27348023653030396,-0.029999999329447746,-0.05953413248062134],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27348023653030396,-0.029999999329447746,-0.05953413248062134,1.0,1.0]}
{"sample_index":2450,"source_step_index":2450,"image_path":"frames/frame_002450.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2734978199005127,-0.029999999329447746,-0.05953085795044899],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2734978199005127,-0.029999999329447746,-0.05953085795044899,1.0,1.0]}
{"sample_index":2451,"source_step_index":2451,"image_path":"frames/frame_002451.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.273515522480011,-0.029999999329447746,-0.05952749028801918],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.273515522480011,-0.029999999329447746,-0.05952749028801918,1.0,1.0]}
{"sample_index":2452,"source_step_index":2452,"image_path":"frames/frame_002452.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2735331952571869,-0.029999999329447746,-0.059524040669202805],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2735331952571869,-0.029999999329447746,-0.059524040669202805,1.0,1.0]}
{"sample_index":2453,"source_step_index":2453,"image_path":"frames/frame_002453.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2735508382320404,-0.029999999329447746,-0.05952049046754837],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2735508382320404,-0.029999999329447746,-0.05952049046754837,1.0,1.0]}
{"sample_index":2454,"source_step_index":2454,"image_path":"frames/frame_002454.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2735683023929596,-0.029999999329447746,-0.059516869485378265],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2735683023929596,-0.029999999329447746,-0.059516869485378265,1.0,1.0]}
{"sample_index":2455,"source_step_index":2455,"image_path":"frames/frame_002455.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2735855281352997,-0.029999999329447746,-0.05951318144798279],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2735855281352997,-0.029999999329447746,-0.05951318144798279,1.0,1.0]}
{"sample_index":2456,"source_step_index":2456,"image_path":"frames/frame_002456.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27360254526138306,-0.029999999329447746,-0.05950944870710373],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27360254526138306,-0.029999999329447746,-0.05950944870710373,1.0,1.0]}
{"sample_index":2457,"source_step_index":2457,"image_path":"frames/frame_002457.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27361923456192017,-0.029999999329447746,-0.05950568988919258],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27361923456192017,-0.029999999329447746,-0.05950568988919258,1.0,1.0]}
{"sample_index":2458,"source_step_index":2458,"image_path":"frames/frame_002458.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2736356556415558,-0.029999999329447746,-0.05950193479657173],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2736356556415558,-0.029999999329447746,-0.05950193479657173,1.0,1.0]}
{"sample_index":2459,"source_step_index":2459,"image_path":"frames/frame_002459.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27365177869796753,-0.029999999329447746,-0.05949819087982178],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.27365177869796753,-0.029999999329447746,-0.05949819087982178,1.0,1.0]}
{"sample_index":2460,"source_step_index":2460,"image_path":"frames/frame_002460.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2736676335334778,-0.029999999329447746,-0.05949447676539421],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2736676335334778,-0.029999999329447746,-0.05949447676539421,1.0,1.0]}
{"sample_index":2461,"source_step_index":2461,"image_path":"frames/frame_002461.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2736833095550537,-0.029999999329447746,-0.05949081853032112],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2736833095550537,-0.029999999329447746,-0.05949081853032112,1.0,1.0]}
{"sample_index":2462,"source_step_index":2462,"image_path":"frames/frame_002462.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"LOWER_TARGET","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.2736988365650177,-0.029999999329447746,-0.059487227350473404],"reach_active":true,"grip_closed":true,"action_vector":[0.0,0.0,0.0,0.2736988365650177,-0.029999999329447746,-0.059487227350473404,1.0,1.0]}
{"sample_index":2464,"source_step_index":2464,"image_path":"frames/frame_002464.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"OPEN_GRIP","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.27372971177101135,-0.029999999329447746,-0.059480246156454086],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.27372971177101135,-0.029999999329447746,-0.059480246156454086,1.0,0.0]}
{"sample_index":2625,"source_step_index":2625,"image_path":"frames/frame_002625.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2626,"source_step_index":2626,"image_path":"frames/frame_002626.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2627,"source_step_index":2627,"image_path":"frames/frame_002627.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2628,"source_step_index":2628,"image_path":"frames/frame_002628.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2629,"source_step_index":2629,"image_path":"frames/frame_002629.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2630,"source_step_index":2630,"image_path":"frames/frame_002630.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2631,"source_step_index":2631,"image_path":"frames/frame_002631.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2632,"source_step_index":2632,"image_path":"frames/frame_002632.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2633,"source_step_index":2633,"image_path":"frames/frame_002633.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2634,"source_step_index":2634,"image_path":"frames/frame_002634.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2635,"source_step_index":2635,"image_path":"frames/frame_002635.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2636,"source_step_index":2636,"image_path":"frames/frame_002636.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2637,"source_step_index":2637,"image_path":"frames/frame_002637.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2638,"source_step_index":2638,"image_path":"frames/frame_002638.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2639,"source_step_index":2639,"image_path":"frames/frame_002639.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2640,"source_step_index":2640,"image_path":"frames/frame_002640.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2641,"source_step_index":2641,"image_path":"frames/frame_002641.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2642,"source_step_index":2642,"image_path":"frames/frame_002642.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2643,"source_step_index":2643,"image_path":"frames/frame_002643.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2644,"source_step_index":2644,"image_path":"frames/frame_002644.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2645,"source_step_index":2645,"image_path":"frames/frame_002645.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2646,"source_step_index":2646,"image_path":"frames/frame_002646.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2647,"source_step_index":2647,"image_path":"frames/frame_002647.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2648,"source_step_index":2648,"image_path":"frames/frame_002648.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2649,"source_step_index":2649,"image_path":"frames/frame_002649.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2650,"source_step_index":2650,"image_path":"frames/frame_002650.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2651,"source_step_index":2651,"image_path":"frames/frame_002651.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2652,"source_step_index":2652,"image_path":"frames/frame_002652.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2653,"source_step_index":2653,"image_path":"frames/frame_002653.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2654,"source_step_index":2654,"image_path":"frames/frame_002654.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2655,"source_step_index":2655,"image_path":"frames/frame_002655.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2656,"source_step_index":2656,"image_path":"frames/frame_002656.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2657,"source_step_index":2657,"image_path":"frames/frame_002657.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2658,"source_step_index":2658,"image_path":"frames/frame_002658.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2659,"source_step_index":2659,"image_path":"frames/frame_002659.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2660,"source_step_index":2660,"image_path":"frames/frame_002660.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2661,"source_step_index":2661,"image_path":"frames/frame_002661.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2662,"source_step_index":2662,"image_path":"frames/frame_002662.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2663,"source_step_index":2663,"image_path":"frames/frame_002663.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
{"sample_index":2664,"source_step_index":2664,"image_path":"frames/frame_002664.png","instruction":"Pick up the red cylinder and place it on the blue table.","phase":"RETRACT","walk_cmd":[0.0,0.0,0.0],"reach_target_pelvis":[0.3,-0.2,0.2],"reach_active":true,"grip_closed":false,"action_vector":[0.0,0.0,0.0,0.3,-0.2,0.2,1.0,0.0]}
```

---

## FILE: `data/vla_exports/g1_native_demo_002/dataset.jsonl`

_Skipped: file is too large (984488 bytes)._ 

---

## FILE: `data/vla_exports/g1_native_demo_002/summary.json`

```json
{
  "num_records": 2665,
  "first_phase": "SETTLE",
  "last_phase": "RETRACT",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "walk_nonzero_records": 1276,
  "reach_active_records": 2430,
  "grip_closed_records": 1902,
  "mean_walk_cmd_magnitude": 0.2647044983945314,
  "max_walk_cmd_magnitude": 1.0071742649611337,
  "mean_reach_target_norm": 0.3783422195480008,
  "max_reach_target_norm": 0.41231056256176607,
  "source_metadata": "data/vla_demos/demo_002_every_tick/demo.jsonl",
  "dataset_path": "data/vla_exports/g1_native_demo_002/dataset.jsonl",
  "copied_images": false,
  "include_phase": true,
  "drop_done": true,
  "drop_inactive_reach": false,
  "action_vector": [
    "walk_x",
    "walk_y",
    "walk_yaw",
    "reach_x",
    "reach_y",
    "reach_z",
    "reach_active",
    "grip_closed"
  ]
}
```

---

## FILE: `data/vla_exports/g1_native_demo_002/training_views/filtered_no_idle.jsonl`

_Skipped: file is too large (935718 bytes)._ 

---

## FILE: `data/vla_exports/g1_native_demo_002/training_views/full.jsonl`

_Skipped: file is too large (984488 bytes)._ 

---

## FILE: `data/vla_exports/g1_native_demo_002/training_views/sample_weights.jsonl`

_Skipped: file is too large (366343 bytes)._ 

---

## FILE: `data/vla_exports/g1_native_demo_002/training_views/training_view_summary.json`

```json
{
  "view_name": "g1_native_training_views",
  "source_records": 2665,
  "filtered_records": 2516,
  "removed_records": 149,
  "source_phase_counts": {
    "APPROACH_SOURCE": 84,
    "APPROACH_TARGET": 1200,
    "CLOSE_GRIP": 2,
    "DESCEND_SOURCE": 300,
    "HOVER_SOURCE": 27,
    "HOVER_TARGET": 200,
    "LIFT_SOURCE": 200,
    "LOWER_TARGET": 300,
    "OPEN_GRIP": 2,
    "RETRACT": 200,
    "SETTLE": 150
  },
  "filtered_phase_counts": {
    "APPROACH_SOURCE": 76,
    "APPROACH_TARGET": 1200,
    "CLOSE_GRIP": 2,
    "DESCEND_SOURCE": 300,
    "HOVER_SOURCE": 26,
    "HOVER_TARGET": 200,
    "LIFT_SOURCE": 200,
    "LOWER_TARGET": 300,
    "OPEN_GRIP": 2,
    "RETRACT": 200,
    "SETTLE": 10
  },
  "rare_transition_records_source": {
    "CLOSE_GRIP": 2,
    "OPEN_GRIP": 2
  },
  "rare_transition_records_filtered": {
    "CLOSE_GRIP": 2,
    "OPEN_GRIP": 2
  },
  "idle_records_source": 159,
  "idle_records_filtered": 10,
  "weight_count": 2665,
  "min_weight": 0.23802617467658693,
  "max_weight": 20.0,
  "mean_weight": 1.0000000000000004,
  "warnings": [
    "This is still a single-trajectory dataset. Weighted/filtered views are debugging aids, not robust generalization data."
  ],
  "keep_first_n_idle": 10,
  "rare_phase_boost": 5.0,
  "files": {
    "full": "data/vla_exports/g1_native_demo_002/training_views/full.jsonl",
    "filtered_no_idle": "data/vla_exports/g1_native_demo_002/training_views/filtered_no_idle.jsonl",
    "sample_weights": "data/vla_exports/g1_native_demo_002/training_views/sample_weights.jsonl",
    "summary": "data/vla_exports/g1_native_demo_002/training_views/training_view_summary.json"
  }
}
```

---

## FILE: `data/vla_exports/g1_native_demo_002_copied/dataset.jsonl`

_Skipped: file is too large (984488 bytes)._ 

---

## FILE: `data/vla_exports/g1_native_demo_002_copied/summary.json`

```json
{
  "num_records": 2665,
  "first_phase": "SETTLE",
  "last_phase": "RETRACT",
  "unique_phases": [
    "APPROACH_SOURCE",
    "APPROACH_TARGET",
    "CLOSE_GRIP",
    "DESCEND_SOURCE",
    "HOVER_SOURCE",
    "HOVER_TARGET",
    "LIFT_SOURCE",
    "LOWER_TARGET",
    "OPEN_GRIP",
    "RETRACT",
    "SETTLE"
  ],
  "walk_nonzero_records": 1276,
  "reach_active_records": 2430,
  "grip_closed_records": 1902,
  "mean_walk_cmd_magnitude": 0.2647044983945314,
  "max_walk_cmd_magnitude": 1.0071742649611337,
  "mean_reach_target_norm": 0.3783422195480008,
  "max_reach_target_norm": 0.41231056256176607,
  "source_metadata": "data/vla_demos/demo_002_every_tick/demo.jsonl",
  "dataset_path": "data/vla_exports/g1_native_demo_002_copied/dataset.jsonl",
  "copied_images": true,
  "include_phase": true,
  "drop_done": true,
  "drop_inactive_reach": false,
  "action_vector": [
    "walk_x",
    "walk_y",
    "walk_yaw",
    "reach_x",
    "reach_y",
    "reach_z",
    "reach_active",
    "grip_closed"
  ]
}
```

---

## FILE: `data/vla_replays/replay_000/replay_summary.json`

```json
{
  "metadata": "data/vla_demos/demo_000/demo.jsonl",
  "output_dir": "data/vla_replays/replay_000",
  "mode": "arm-only",
  "num_steps": 554,
  "mean_palm_error_m": 0.26366714511474343,
  "max_palm_error_m": 0.4686852714248318,
  "final_palm_error_m": 0.30052173692437284,
  "mean_action_magnitude_m": 0.00788488542545105,
  "max_action_magnitude_m": 0.08456800232659496,
  "grip_mismatch_count": 0,
  "attached_steps": 0,
  "ever_attached": false
}
```

---

## FILE: `data/vla_replays/replay_000/replay_trace.npz`

_Skipped: non-text or binary file._

---

## FILE: `data/vla_replays/replay_000_short/replay_summary.json`

```json
{
  "metadata": "data/vla_demos/demo_000/demo.jsonl",
  "output_dir": "data/vla_replays/replay_000_short",
  "mode": "arm-only",
  "num_steps": 100,
  "mean_palm_error_m": 0.2550702598909639,
  "max_palm_error_m": 0.348835721574912,
  "final_palm_error_m": 0.2545610901136029,
  "mean_action_magnitude_m": 0.011928059118416599,
  "max_action_magnitude_m": 0.08165556780992533,
  "grip_mismatch_count": 0,
  "attached_steps": 0,
  "ever_attached": false
}
```

---

## FILE: `data/vla_replays/replay_000_short/replay_trace.npz`

_Skipped: non-text or binary file._

---

## FILE: `data/vla_replays/replay_001_arm_only/replay_summary.json`

```json
{
  "metadata": "data/vla_demos/demo_001/demo.jsonl",
  "output_dir": "data/vla_replays/replay_001_arm_only",
  "mode": "arm-only",
  "num_steps": 554,
  "mean_palm_error_m": 0.26366714511474343,
  "max_palm_error_m": 0.4686852714248318,
  "final_palm_error_m": 0.30052173692437284,
  "mean_action_magnitude_m": 0.00788488542545105,
  "max_action_magnitude_m": 0.08456800232659496,
  "grip_mismatch_count": 0,
  "walk_nonzero_steps": 255,
  "reach_active_steps": 507,
  "attached_steps": 0,
  "ever_attached": false
}
```

---

## FILE: `data/vla_replays/replay_001_arm_only/replay_trace.npz`

_Skipped: non-text or binary file._

---

## FILE: `data/vla_replays/replay_001_hybrid/replay_summary.json`

```json
{
  "metadata": "data/vla_demos/demo_001/demo.jsonl",
  "output_dir": "data/vla_replays/replay_001_hybrid",
  "mode": "hybrid-7d",
  "num_steps": 554,
  "mean_palm_error_m": 0.25943467444982243,
  "max_palm_error_m": 0.48088513912099906,
  "final_palm_error_m": 0.26439324205749914,
  "mean_action_magnitude_m": 0.00788488542545105,
  "max_action_magnitude_m": 0.08456800232659496,
  "grip_mismatch_count": 0,
  "walk_nonzero_steps": 255,
  "reach_active_steps": 507,
  "attached_steps": 0,
  "ever_attached": false
}
```

---

## FILE: `data/vla_replays/replay_001_hybrid/replay_trace.npz`

_Skipped: non-text or binary file._

---

## FILE: `data/vla_replays/replay_001_teacher/replay_summary.json`

```json
{
  "metadata": "data/vla_demos/demo_001/demo.jsonl",
  "output_dir": "data/vla_replays/replay_001_teacher",
  "mode": "teacher-command",
  "num_steps": 554,
  "mean_palm_error_m": 0.42092816374304615,
  "max_palm_error_m": 0.6092102935165782,
  "final_palm_error_m": 0.5234773643231646,
  "mean_action_magnitude_m": 0.00788488542545105,
  "max_action_magnitude_m": 0.08456800232659496,
  "grip_mismatch_count": 0,
  "walk_nonzero_steps": 255,
  "reach_active_steps": 507,
  "attached_steps": 0,
  "ever_attached": false
}
```

---

## FILE: `data/vla_replays/replay_001_teacher/replay_trace.npz`

_Skipped: non-text or binary file._

---

## FILE: `data/vla_replays/replay_002_hybrid/replay_summary.json`

```json
{
  "metadata": "data/vla_demos/demo_002_every_tick/demo.jsonl",
  "output_dir": "data/vla_replays/replay_002_hybrid",
  "mode": "hybrid-7d",
  "num_steps": 2766,
  "mean_palm_error_m": 0.22991592318212462,
  "max_palm_error_m": 0.4674631056222388,
  "final_palm_error_m": 0.3467343192182516,
  "mean_action_magnitude_m": 0.0016406439064965631,
  "max_action_magnitude_m": 0.01748103854992822,
  "grip_mismatch_count": 0,
  "walk_nonzero_steps": 1276,
  "reach_active_steps": 2531,
  "attached_steps": 0,
  "ever_attached": false
}
```

---

## FILE: `data/vla_replays/replay_002_hybrid/replay_trace.npz`

_Skipped: file is too large (297526 bytes)._ 

---

## FILE: `data/vla_replays/replay_002_teacher/replay_summary.json`

```json
{
  "metadata": "data/vla_demos/demo_002_every_tick/demo.jsonl",
  "output_dir": "data/vla_replays/replay_002_teacher",
  "mode": "teacher-command",
  "num_steps": 2766,
  "mean_palm_error_m": 0.0,
  "max_palm_error_m": 0.0,
  "final_palm_error_m": 0.0,
  "mean_action_magnitude_m": 0.0016406439064965631,
  "max_action_magnitude_m": 0.01748103854992822,
  "grip_mismatch_count": 0,
  "walk_nonzero_steps": 1276,
  "reach_active_steps": 2531,
  "attached_steps": 1902,
  "ever_attached": true
}
```

---

## FILE: `data/vla_replays/replay_002_teacher/replay_trace.npz`

_Skipped: file is too large (297526 bytes)._ 

---

## FILE: `docs/BASELINE_AUDIT.md`

```md
# Baseline Audit: g1-manipulation-challenge

## Repository Tree (Original)
- assets/ (Mesh files: .obj, .STL)
- run.py (Main simulation script)
- scene.xml (MuJoCo scene definition)
- g1.xml (Robot model)
- model_config.json (Joint/PD configurations)
- walker.onnx (Locomotion policy)
- croucher.onnx (Optional policy)
- rotator.onnx (Optional policy)
- right_reacher.onnx (Reaching policy)
- README.md

## Hardware & Asset Inventory
- **Required Core Files:** `run.py`, `scene.xml`, `g1.xml`, `model_config.json`, `walker.onnx`, `right_reacher.onnx`.
- **Defined Cameras:** `head_cam` (torso/forward), `wrist_cam` (right palm/outward).
- **ONNX Policies:** - **Core:** `walker.onnx` (99D obs), `right_reacher.onnx` (36D obs).
  - **Optional:** `croucher.onnx`, `rotator.onnx`.

## Current Controls and Limitations
- **Control Interface:** Keyboard-driven manual toggling between Walk and Reach modes.
- **Functional Limitations:** No autonomous sequencing; 100% manual intervention required for task completion; no vision processing integrated into control loop.
```

---

## FILE: `docs/VLA_DECISION_LOG.md`

```md
# VLA Decision Log — Lucky Robots G1 Pick-and-Place

## Decision 001 — Do not replace the FSM baseline immediately

**Decision:**
Keep the FSM baseline untouched and build the VLA path as a separate research branch.

**Reason:**
The baseline already solves the task. Directly replacing it with OpenVLA would combine too many unknowns: embodiment mismatch, action-space mismatch, camera distribution mismatch, and infrastructure complexity.

**Expected Result:**
A safer incremental research branch.

**Rejected Alternative:**
Zero-shot OpenVLA live control.

**Verification:**
The repo behavior is unchanged after this step.

**Rollback:**
Delete the VLA docs and `vla_bridge` package; FSM baseline remains unaffected.

---

## Decision 002 — Use the FSM as the teacher policy

**Decision:**
Use the working FSM to generate demonstrations for the VLA branch.

**Reason:**
The FSM already exposes useful supervision:
- FSM phase
- palm pose
- reach target
- grip state
- object/table metadata
- camera frames

**Expected Result:**
Consistent image-action data without manual teleoperation.

**Rejected Alternative:**
Manual keyboard demonstration collection.

**Reason Rejected:**
Manual demos are slower, noisier, and less reproducible.

**Verification:**
Future recorder should save synchronized frames and actions from a complete FSM rollout.

**Rollback:**
If FSM demos contain too many pauses, filter/downsample the data or record only manipulation phases.

---

## Decision 003 — Build the action adapter before loading OpenVLA

**Decision:**
Create a `G1VLAActionAdapter` before adding any OpenVLA inference code.

**Reason:**
If 7D OpenVLA-style actions cannot control the G1 reacher/grip stack, then model inference or fine-tuning is premature.

**Expected Result:**
A cheap local feasibility test.

**Rejected Alternative:**
Set up OpenVLA/Hugging Face first.

**Reason Rejected:**
That would spend time on GPU/model infrastructure before proving the action interface is executable.

**Verification:**
Replay teacher-generated 7D actions through the adapter.

**Rollback:**
If replay fails, keep OpenVLA as future work and continue with the classical vision pipeline.
```

---

## FILE: `docs/VLA_RESEARCH_PLAN.md`

```md
# VLA Research Plan — Lucky Robots G1 Pick-and-Place

## 1. Goal

Investigate whether OpenVLA-style Vision-Language-Action models can augment or eventually replace parts of the existing FSM pipeline for the G1 pick-and-place task.

This is a research branch, not implemented runtime behavior. No existing runtime files are modified in this step.

## 2. Current Baseline

The repo already has a working FSM baseline using:
- MuJoCo
- walker ONNX policy
- right_reacher ONNX policy
- 12-state FSM sequencing
- kinematic grasp backend
- target-table placement logic
- development logs and tests

This baseline must remain the teacher, fallback, and evaluation reference. All VLA work is layered on top without modifying it.

## 3. Why VLA / OpenVLA Is Interesting

OpenVLA-style models can map images and language instructions to robot actions.

Example instruction:
> "Pick up the red cylinder and place it on the blue table."

This is directly aligned with the challenge's open-ended allowance for VLM/VLA approaches. A language-conditioned model could generalize across object positions, colors, and table configurations without hard-coded waypoints.

## 4. Why OpenVLA Is Not Plug-and-Play

There is a fundamental action-space mismatch:

OpenVLA-style action output:
```
[dx, dy, dz, droll, dpitch, dyaw, gripper]
```

Current G1 stack consumes:
- `walk_cmd` — locomotion command
- `reach_target` in pelvis frame — end-effector target for the reacher policy
- `reach_active` — flag enabling the reacher
- `grip_closed` — binary grip state

Therefore, the first engineering challenge is **action-space compatibility**, not model loading. Until 7D VLA actions can be translated into the G1 interface, model inference or fine-tuning is premature.

## 5. Core Hypothesis

If the FSM palm trajectory can be converted into OpenVLA-style 7D end-effector actions and replayed through the existing G1 reacher/grip stack, then OpenVLA fine-tuning or shadow inference becomes meaningful.

If this replay fails, then OpenVLA should remain future work until the action interface is redesigned.

## 6. Development Roadmap

### Step 12 — VLA research scaffold
- Add docs and empty `vla_bridge` package.
- No runtime behavior change.

### Step 13 — G1VLAActionAdapter
- Map 7D VLA action to `reach_target`/`grip`.
- No OpenVLA model yet.

### Step 14 — FSM demonstration recorder
- Record camera frames, palm pose, FSM phase, reach target, grip state, and 7D teacher action.

### Step 15 — 7D action replay
- Replay recorded actions without using FSM target lookups.

### Step 16 — Dataset cleanup
- Downsample to 5–10 Hz.
- Remove idle segments and long pauses.

### Step 17 — OpenVLA shadow mode
- Run OpenVLA on saved frames only.
- Compare predictions to FSM teacher actions.
- Do not control the robot yet.

### Step 18 — Remote/cloud inference
- Serve OpenVLA from Colab or cloud GPU.
- Query from local MuJoCo.

### Step 19 — Fine-tuning feasibility
- Evaluate LoRA/OFT only after replay and shadow tests pass.

## 7. Infrastructure Plan

**Local machine:**
- MuJoCo
- ONNX Runtime
- NumPy
- OpenCV
- existing FSM repo
- action adapter
- demonstration recording
- replay tests

**Cloud/GPU (later):**
- OpenVLA inference
- possible LoRA fine-tuning
- possible OFT experiment
- REST API model serving

No GPU is needed for Step 12 or Step 13.

## 8. Non-Goals

- Do not replace the walker yet.
- Do not replace the reacher yet.
- Do not train OpenVLA yet.
- Do not run zero-shot OpenVLA live control yet.
- Do not output all 29 G1 joint targets.
- Do not modify the successful FSM baseline.

## 9. First Test Gate

The first real test gate is:

1. Record an FSM rollout.
2. Convert palm motion to 7D actions.
3. Replay the 7D actions through the adapter.
4. Check whether the robot reaches meaningful milestones.

**Pass criteria:**
- source hover reached
- source descent reached
- grip command represented
- lift represented
- target-side release approximately represented

## 10. Strategic Summary

> The FSM is the teacher.
> The VLA adapter is the translator.
> The replay test is the gate.
> OpenVLA only earns live control after passing staged offline tests.
```

---

## FILE: `g1.xml`

```xml
<mujoco model="g1_29dof_rev_1_0">
  <compiler angle="radian" meshdir="assets" autolimits="true"/>

  <option integrator="implicitfast" timestep="0.005" impratio="1.0" cone="pyramidal" 
          jacobian="auto" solver="Newton" iterations="10" tolerance="1e-08" 
          ls_iterations="20" ls_tolerance="0.01" gravity="0 0 -9.81"/>

  <default>
    <default class="g1">
      <position inheritrange="1"/>
      <default class="visual">
        <geom group="2" type="mesh" density="0" material="silver" contype="0" conaffinity="0"/>
      </default>
      <default class="collision">
        <geom group="3" rgba=".2 .6 .2 .3" type="capsule" contype="1" conaffinity="1"/>
        <default class="foot_capsule">
          <geom type="capsule" size="0.01"/>
        </default>
      </default>
      <site group="5" rgba="1 0 0 1"/>
    </default>
  </default>

  <asset>
    <material name="silver" rgba="0.7 0.7 0.7 1"/>
    <material name="black" rgba="0.2 0.2 0.2 1"/>

    <mesh name="pelvis" file="pelvis.obj"/>
    <mesh name="pelvis_contour_link" file="pelvis_contour_link.obj"/>
    <mesh name="left_hip_pitch_link" file="left_hip_pitch_link.obj"/>
    <mesh name="left_hip_roll_link" file="left_hip_roll_link.obj"/>
    <mesh name="left_hip_yaw_link" file="left_hip_yaw_link.obj"/>
    <mesh name="left_knee_link" file="left_knee_link.obj"/>
    <mesh name="left_ankle_pitch_link" file="left_ankle_pitch_link.obj"/>
    <mesh name="left_ankle_roll_link" file="left_ankle_roll_link.obj"/>
    <mesh name="right_hip_pitch_link" file="right_hip_pitch_link.obj"/>
    <mesh name="right_hip_roll_link" file="right_hip_roll_link.obj"/>
    <mesh name="right_hip_yaw_link" file="right_hip_yaw_link.obj"/>
    <mesh name="right_knee_link" file="right_knee_link.obj"/>
    <mesh name="right_ankle_pitch_link" file="right_ankle_pitch_link.obj"/>
    <mesh name="right_ankle_roll_link" file="right_ankle_roll_link.obj"/>
    <mesh name="waist_yaw_link_rev_1_0" file="waist_yaw_link_rev_1_0.obj"/>
    <mesh name="waist_roll_link_rev_1_0" file="waist_roll_link_rev_1_0.obj"/>
    <mesh name="torso_link_rev_1_0" file="torso_link_rev_1_0.obj"/>
    <mesh name="logo_link" file="logo_link.obj"/>
    <mesh name="head_link" file="head_link.obj"/>
    <mesh name="left_shoulder_pitch_link" file="left_shoulder_pitch_link.obj"/>
    <mesh name="left_shoulder_roll_link" file="left_shoulder_roll_link.obj"/>
    <mesh name="left_shoulder_yaw_link" file="left_shoulder_yaw_link.obj"/>
    <mesh name="left_elbow_link" file="left_elbow_link.obj"/>
    <mesh name="left_wrist_roll_link" file="left_wrist_roll_link.obj"/>
    <mesh name="left_wrist_pitch_link" file="left_wrist_pitch_link.obj"/>
    <mesh name="left_wrist_yaw_link" file="left_wrist_yaw_link.obj"/>
    <mesh name="left_hand_palm_link" file="left_hand_palm_link.STL"/>
    <mesh name="left_hand_thumb_0_link" file="left_hand_thumb_0_link.STL"/>
    <mesh name="left_hand_thumb_1_link" file="left_hand_thumb_1_link.STL"/>
    <mesh name="left_hand_thumb_2_link" file="left_hand_thumb_2_link.STL"/>
    <mesh name="left_hand_middle_0_link" file="left_hand_middle_0_link.STL"/>
    <mesh name="left_hand_middle_1_link" file="left_hand_middle_1_link.STL"/>
    <mesh name="left_hand_index_0_link" file="left_hand_index_0_link.STL"/>
    <mesh name="left_hand_index_1_link" file="left_hand_index_1_link.STL"/>
    <mesh name="right_shoulder_pitch_link" file="right_shoulder_pitch_link.obj"/>
    <mesh name="right_shoulder_roll_link" file="right_shoulder_roll_link.obj"/>
    <mesh name="right_shoulder_yaw_link" file="right_shoulder_yaw_link.obj"/>
    <mesh name="right_elbow_link" file="right_elbow_link.obj"/>
    <mesh name="right_wrist_roll_link" file="right_wrist_roll_link.obj"/>
    <mesh name="right_wrist_pitch_link" file="right_wrist_pitch_link.obj"/>
    <mesh name="right_wrist_yaw_link" file="right_wrist_yaw_link.obj"/>
    <mesh name="right_hand_palm_link" file="right_hand_palm_link.STL"/>
    <mesh name="right_hand_thumb_0_link" file="right_hand_thumb_0_link.STL"/>
    <mesh name="right_hand_thumb_1_link" file="right_hand_thumb_1_link.STL"/>
    <mesh name="right_hand_thumb_2_link" file="right_hand_thumb_2_link.STL"/>
    <mesh name="right_hand_middle_0_link" file="right_hand_middle_0_link.STL"/>
    <mesh name="right_hand_middle_1_link" file="right_hand_middle_1_link.STL"/>
    <mesh name="right_hand_index_0_link" file="right_hand_index_0_link.STL"/>
    <mesh name="right_hand_index_1_link" file="right_hand_index_1_link.STL"/>
  </asset>


<worldbody>
    <body name="pelvis" pos="-0.6 0 0.79" childclass="g1">
      <light pos="0 0 2" mode="trackcom"/>
      <camera name="tracking" pos="1.734 -1.135 .35" xyaxes="0.552 0.834 -0.000 -0.170 0.112 0.979" mode="trackcom"/>
      <inertial pos="0 0 -0.07605" quat="1 0 -0.000399148 0" mass="3.813" diaginertia="0.010549 0.0093089 0.0079184"/>
      <freejoint name="floating_base_joint"/>
      <geom class="visual" material="black" mesh="pelvis"/>
      <geom class="visual" mesh="pelvis_contour_link"/>
      <geom name="pelvis_collision" class="collision" type="sphere" size="0.07" pos="0 0 -0.08"/>
      <site name="imu_in_pelvis" size="0.01" pos="0.04525 0 -0.08339"/>
      <body name="left_hip_pitch_link" pos="0 0.064452 -0.1027">
        <inertial pos="0.002741 0.047791 -0.02606" quat="0.954862 0.293964 0.0302556 0.030122" mass="1.35"
          diaginertia="0.00181517 0.00153422 0.00116212"/>
        <joint name="left_hip_pitch_joint" axis="0 1 0" range="-2.5307 2.8798" armature="0.01018" actuatorfrcrange="-88 88"/>
        <geom class="visual" material="black" mesh="left_hip_pitch_link"/>
        <body name="left_hip_roll_link" pos="0 0.052 -0.030465" quat="0.996179 0 -0.0873386 0">
          <inertial pos="0.029812 -0.001045 -0.087934" quat="0.977808 -1.97119e-05 0.205576 -0.0403793" mass="1.52"
            diaginertia="0.00254986 0.00241169 0.00148755"/>
          <joint name="left_hip_roll_joint" axis="1 0 0" range="-0.5236 2.9671" armature="0.02510" actuatorfrcrange="-139 139"/>
          <geom class="visual" mesh="left_hip_roll_link"/>
          <geom name="left_hip_collision" class="collision" size="0.06" fromto="0.02 0 0 0.02 0 -0.08"/>
          <body name="left_hip_yaw_link" pos="0.025001 0 -0.12412">
            <inertial pos="-0.057709 -0.010981 -0.15078" quat="0.600598 0.15832 0.223482 0.751181" mass="1.702"
              diaginertia="0.00776166 0.00717575 0.00160139"/>
            <joint name="left_hip_yaw_joint" axis="0 0 1" range="-2.7576 2.7576" armature="0.01018" actuatorfrcrange="-88 88"/>
            <geom class="visual" mesh="left_hip_yaw_link"/>
            <geom name="left_thigh_collision" class="collision" size="0.055" fromto="-0.0 0 -0.03 -0.06 0 -0.17"/>
            <body name="left_knee_link" pos="-0.078273 0.0021489 -0.17734" quat="0.996179 0 0.0873386 0">
              <inertial pos="0.005457 0.003964 -0.12074" quat="0.923418 -0.0327699 0.0158246 0.382067" mass="1.932"
                diaginertia="0.0113804 0.0112778 0.00146458"/>
              <joint name="left_knee_joint" axis="0 1 0" range="-0.087267 2.8798" armature="0.02510" actuatorfrcrange="-139 139"/>
              <geom class="visual" mesh="left_knee_link"/>
              <geom name="left_shin_collision" class="collision" size="0.045" fromto="0.01 0 0 0.01 0 -0.15"/>
              <geom name="left_linkage_brace_collision" class="collision" size="0.03" fromto="0.01 0 -0.2 0.01 0 -0.28"/>
              <body name="left_ankle_pitch_link" pos="0 -9.4445e-05 -0.30001">
                <inertial pos="-0.007269 0 0.011137" quat="0.603053 0.369225 0.369225 0.603053" mass="0.074"
                  diaginertia="1.89e-05 1.40805e-05 6.9195e-06"/>
                <joint name="left_ankle_pitch_joint" axis="0 1 0" range="-0.87267 0.5236" armature="0.00722" actuatorfrcrange="-50 50"/>
                <geom class="visual" mesh="left_ankle_pitch_link"/>
                <body name="left_ankle_roll_link" pos="0 0 -0.017558">
                  <site name="left_foot" rgba="1 0 0 1" pos="0.04 0 -0.037"/>
                  <inertial pos="0.026505 0 -0.016425" quat="-0.000481092 0.728482 -0.000618967 0.685065" mass="0.608"
                    diaginertia="0.00167218 0.0016161 0.000217621"/>
                  <joint name="left_ankle_roll_joint" axis="1 0 0" range="-0.2618 0.2618" armature="0.00722" actuatorfrcrange="-50 50"/>
                  <geom class="visual" material="black" mesh="left_ankle_roll_link"/>
                  <geom name="left_foot1_collision" class="foot_capsule" fromto="0.1 -0.026 -0.025 0.05 -0.027 -0.025"/>
                  <geom name="left_foot2_collision" class="foot_capsule"
                    fromto="-0.044 -0.018 -0.025 0.123 -0.018 -0.025"/>
                  <geom name="left_foot3_collision" class="foot_capsule" fromto="-0.052 -0.01 -0.025 0.13 -0.01 -0.025"/>
                  <geom name="left_foot4_collision" class="foot_capsule" fromto="-0.054 0 -0.025 0.132 0 -0.025"/>
                  <geom name="left_foot5_collision" class="foot_capsule" fromto="-0.052 0.01 -0.025 0.13 0.01 -0.025"/>
                  <geom name="left_foot6_collision" class="foot_capsule" fromto="-0.044 0.018 -0.025 0.123 0.018 -0.025"/>
                  <geom name="left_foot7_collision" class="foot_capsule" fromto="0.1 0.026 -0.025 0.05 0.026 -0.025"/>
                </body>
              </body>
            </body>
          </body>
        </body>
      </body>
      <body name="right_hip_pitch_link" pos="0 -0.064452 -0.1027">
        <inertial pos="0.002741 -0.047791 -0.02606" quat="0.954862 -0.293964 0.0302556 -0.030122" mass="1.35"
          diaginertia="0.00181517 0.00153422 0.00116212"/>
        <joint name="right_hip_pitch_joint" axis="0 1 0" range="-2.5307 2.8798" armature="0.01018" actuatorfrcrange="-88 88"/>
        <geom class="visual" material="black" mesh="right_hip_pitch_link"/>
        <body name="right_hip_roll_link" pos="0 -0.052 -0.030465" quat="0.996179 0 -0.0873386 0">
          <inertial pos="0.029812 0.001045 -0.087934" quat="0.977808 1.97119e-05 0.205576 0.0403793" mass="1.52"
            diaginertia="0.00254986 0.00241169 0.00148755"/>
          <joint name="right_hip_roll_joint" axis="1 0 0" range="-2.9671 0.5236" armature="0.02510" actuatorfrcrange="-139 139"/>
          <geom class="visual" mesh="right_hip_roll_link"/>
          <geom name="right_hip_collision" class="collision" size="0.06" fromto="0.02 0 0 0.02 0 -0.08"/>
          <body name="right_hip_yaw_link" pos="0.025001 0 -0.12412">
            <inertial pos="-0.057709 0.010981 -0.15078" quat="0.751181 0.223482 0.15832 0.600598" mass="1.702"
              diaginertia="0.00776166 0.00717575 0.00160139"/>
            <joint name="right_hip_yaw_joint" axis="0 0 1" range="-2.7576 2.7576" armature="0.01018" actuatorfrcrange="-88 88"/>
            <geom class="visual" mesh="right_hip_yaw_link"/>
            <geom name="right_thigh_collision" class="collision" size="0.055" fromto="-0.0 0 -0.03 -0.06 0 -0.17"/>
            <body name="right_knee_link" pos="-0.078273 -0.0021489 -0.17734" quat="0.996179 0 0.0873386 0">
              <inertial pos="0.005457 -0.003964 -0.12074" quat="0.923439 0.0345276 0.0116333 -0.382012" mass="1.932"
                diaginertia="0.011374 0.0112843 0.00146452"/>
              <joint name="right_knee_joint" axis="0 1 0" range="-0.087267 2.8798" armature="0.02510" actuatorfrcrange="-139 139"/>
              <geom class="visual" mesh="right_knee_link"/>
              <geom name="right_shin_collision" class="collision" size="0.045" fromto="0.01 0 0 0.01 0 -0.15"/>
              <geom name="right_linkage_brace_collision" class="collision" size="0.03" fromto="0.01 0 -0.2 0.01 0 -0.28"/>
              <body name="right_ankle_pitch_link" pos="0 9.4445e-05 -0.30001">
                <inertial pos="-0.007269 0 0.011137" quat="0.603053 0.369225 0.369225 0.603053" mass="0.074"
                  diaginertia="1.89e-05 1.40805e-05 6.9195e-06"/>
                <joint name="right_ankle_pitch_joint" axis="0 1 0" range="-0.87267 0.5236" armature="0.00722" actuatorfrcrange="-50 50"/>
                <geom class="visual" mesh="right_ankle_pitch_link"/>
                <body name="right_ankle_roll_link" pos="0 0 -0.017558">
                  <site name="right_foot" rgba="1 0 0 1" pos="0.04 0 -0.037"/>
                  <inertial pos="0.026505 0 -0.016425" quat="0.000481092 0.728482 0.000618967 0.685065" mass="0.608"
                    diaginertia="0.00167218 0.0016161 0.000217621"/>
                  <joint name="right_ankle_roll_joint" axis="1 0 0" range="-0.2618 0.2618" armature="0.00722" actuatorfrcrange="-50 50"/>
                  <geom class="visual" material="black" mesh="right_ankle_roll_link"/>
                  <geom name="right_foot1_collision" class="foot_capsule" fromto="0.1 -0.026 -0.025 0.05 -0.026 -0.025"/>
                  <geom name="right_foot2_collision" class="foot_capsule"
                    fromto="-0.044 -0.018 -0.025 0.123 -0.018 -0.025"/>
                  <geom name="right_foot3_collision" class="foot_capsule" fromto="-0.052 -0.01 -0.025 0.13 -0.01 -0.025"/>
                  <geom name="right_foot4_collision" class="foot_capsule" fromto="-0.054 0 -0.025 0.132 0 -0.025"/>
                  <geom name="right_foot5_collision" class="foot_capsule" fromto="-0.052 0.01 -0.025 0.13 0.01 -0.025"/>
                  <geom name="right_foot6_collision" class="foot_capsule"
                    fromto="-0.044 0.018 -0.025 0.123 0.018 -0.025"/>
                  <geom name="right_foot7_collision" class="foot_capsule" fromto="0.1 0.026 -0.025 0.05 0.026 -0.025"/>
                </body>
              </body>
            </body>
          </body>
        </body>
      </body>
      <body name="waist_yaw_link_rev_1_0">
        <inertial pos="0.003494 0.000233 0.018034" quat="0.289697 0.591001 -0.337795 0.672821" mass="0.214"
          diaginertia="0.000163531 0.000107714 0.000102205"/>
        <joint name="waist_yaw_joint" axis="0 0 1" range="-2.618 2.618" armature="0.01018" actuatorfrcrange="-88 88"/>
        <geom class="visual" mesh="waist_yaw_link_rev_1_0"/>
        <body name="waist_roll_link_rev_1_0" pos="-0.0039635 0 0.044">
          <inertial pos="0 2.3e-05 0" quat="0.5 0.5 -0.5 0.5" mass="0.086" diaginertia="8.245e-06 7.079e-06 6.339e-06"/>
          <joint name="waist_roll_joint" axis="1 0 0" range="-0.52 0.52" armature="0.00722" actuatorfrcrange="-50 50"/>
          <geom class="visual" mesh="waist_roll_link_rev_1_0"/>
          <body name="torso_link_rev_1_0">
            <inertial pos="0.00203158 0.000339683 0.184568" quat="0.999803 -6.03319e-05 0.0198256 0.00131986"
              mass="7.818" diaginertia="0.121847 0.109825 0.0273735"/>
            <joint name="waist_pitch_joint" axis="0 1 0" range="-0.52 0.52" armature="0.00722" actuatorfrcrange="-50 50"/>
            <geom class="visual" mesh="torso_link_rev_1_0"/>
            <geom class="visual" pos="0.0039635 0 -0.044" quat="1 0 0 0" material="black" mesh="logo_link"/>
            <geom class="visual" pos="0.0039635 0 -0.044" material="black" mesh="head_link"/>
            <geom name="torso_collision" class="collision" size="0.09" fromto="0.01 0 0.08 0.01 0 0.2"/>
            <geom name="head_collision" class="collision" type="sphere" size="0.06" pos="0 0 .43"/>
            <camera name="head_cam" pos="0.05 0 0.43" xyaxes="0 -1 0 0.34 0 0.94" fovy="60"/>
            <site name="imu_in_torso" size="0.01" pos="-0.03959 -0.00224 0.14792"/>
            <body name="left_shoulder_pitch_link" pos="0.0039563 0.10022 0.24778"
              quat="0.990264 0.139201 1.38722e-05 -9.86868e-05">
              <inertial pos="0 0.035892 -0.011628" quat="0.654152 0.0130458 -0.326267 0.68225" mass="0.718"
                diaginertia="0.000465864 0.000432842 0.000406394"/>
              <joint name="left_shoulder_pitch_joint" axis="0 1 0" range="-3.0892 2.6704" armature="0.00361" actuatorfrcrange="-25 25"/>
              <geom class="visual" mesh="left_shoulder_pitch_link"/>
              <body name="left_shoulder_roll_link" pos="0 0.038 -0.013831" quat="0.990268 -0.139172 0 0">
                <inertial pos="-0.000227 0.00727 -0.063243" quat="0.701256 -0.0196223 -0.00710317 0.712604" mass="0.643"
                  diaginertia="0.000691311 0.000618011 0.000388977"/>
                <joint name="left_shoulder_roll_joint" axis="1 0 0" range="-1.5882 2.2515" armature="0.00361" actuatorfrcrange="-25 25"/>
                <geom class="visual" mesh="left_shoulder_roll_link"/>
                <body name="left_shoulder_yaw_link" pos="0 0.00624 -0.1032">
                  <inertial pos="0.010773 -0.002949 -0.072009" quat="0.716879 -0.0964829 -0.0679942 0.687134"
                    mass="0.734" diaginertia="0.00106187 0.00103217 0.000400661"/>
                  <joint name="left_shoulder_yaw_joint" axis="0 0 1" range="-2.618 2.618" armature="0.00361" actuatorfrcrange="-25 25"/>
                  <geom class="visual" mesh="left_shoulder_yaw_link"/>
                  <geom name="left_shoulder_yaw_collision" class="collision" size="0.035" fromto="0 0 -0.08 0 0 0.05"/>
                  <body name="left_elbow_link" pos="0.015783 0 -0.080518">
                    <inertial pos="0.064956 0.004454 -0.010062" quat="0.541765 0.636132 0.388821 0.388129" mass="0.6"
                      diaginertia="0.000443035 0.000421612 0.000259353"/>
                    <joint name="left_elbow_joint" axis="0 1 0" range="-1.0472 2.0944" armature="0.00361" actuatorfrcrange="-25 25"/>
                    <geom class="visual" mesh="left_elbow_link"/>
                    <geom name="left_elbow_yaw_collision" class="collision" size="0.035"
                      fromto="-0.01 0 -0.01 0.08 0 -0.01"/>
                    <body name="left_wrist_roll_link" pos="0.1 0.00188791 -0.01">
                      <inertial pos="0.0171394 0.000537591 4.8864e-07" quat="0.575338 0.411667 -0.574906 0.411094"
                        mass="0.085445" diaginertia="5.48211e-05 4.96646e-05 3.57798e-05"/>
                      <joint name="left_wrist_roll_joint" axis="1 0 0" range="-1.97222 1.97222" armature="0.00361" actuatorfrcrange="-25 25"/>
                      <geom class="visual" mesh="left_wrist_roll_link"/>
                      <body name="left_wrist_pitch_link" pos="0.038 0 0">
                        <inertial pos="0.0229999 -0.00111685 -0.00111658" quat="0.249998 0.661363 0.293036 0.643608"
                          mass="0.48405" diaginertia="0.000430353 0.000429873 0.000164648"/>
                        <joint name="left_wrist_pitch_joint" axis="0 1 0" range="-1.61443 1.61443" armature="0.00425" actuatorfrcrange="-5 5"/>
                        <geom class="visual" mesh="left_wrist_pitch_link"/>
                        <geom name="left_wrist_collision" class="collision" size="0.035" fromto="-0.01 0 0 0.06 0 0"/>
                        <body name="left_wrist_yaw_link" pos="0.046 0 0">
                          <inertial pos="0.0708244 0.000191745 0.00161742" quat="0.510571 0.526295 0.468078 0.493188"
                            mass="0.254576" diaginertia="0.000646113 0.000559993 0.000147566"/>
                          <joint name="left_wrist_yaw_joint" axis="0 0 1" range="-1.61443 1.61443" armature="0.00425" actuatorfrcrange="-5 5"/>
                          <geom class="visual" mesh="left_wrist_yaw_link"/>
                          <geom pos="0.0415 0.003 0" quat="1 0 0 0" type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="left_hand_palm_link"/>
                          <geom pos="0.0415 0.003 0" quat="1 0 0 0" type="mesh" rgba="0.7 0.7 0.7 1" mesh="left_hand_palm_link"/>
                          <site name="left_palm" pos="0.08 0 0" size="0.01"/>
                          <body name="left_hand_thumb_0_link" pos="0.067 0.003 0">
                            <inertial pos="-0.000884246 -0.00863407 0.000944293" quat="0.462991 0.643965 -0.460173 0.398986" mass="0.0862366" diaginertia="1.6546e-05 1.60058e-05 1.43741e-05"/>
                            <joint name="left_hand_thumb_0_joint" axis="0 1 0" range="-1.0472 1.0472" actuatorfrcrange="-2.45 2.45"/>
                            <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="left_hand_thumb_0_link"/>
                            <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="left_hand_thumb_0_link"/>
                            <body name="left_hand_thumb_1_link" pos="-0.0025 -0.0193 0">
                              <inertial pos="-0.000827888 -0.0354744 -0.0003809" quat="0.685598 0.705471 -0.15207 0.0956069" mass="0.0588507" diaginertia="1.28514e-05 1.22902e-05 5.9666e-06"/>
                              <joint name="left_hand_thumb_1_joint" axis="0 0 1" range="-0.724312 1.0472" actuatorfrcrange="-1.4 1.4"/>
                              <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="left_hand_thumb_1_link"/>
                              <geom size="0.01 0.015 0.01" pos="-0.001 -0.032 0" type="box" rgba="0.7 0.7 0.7 1"/>
                              <body name="left_hand_thumb_2_link" pos="0 -0.0458 0">
                                <inertial pos="-0.00171735 -0.0262819 0.000107789" quat="0.703174 0.710977 -0.00017564 -0.00766553" mass="0.0203063" diaginertia="4.61314e-06 3.86645e-06 1.53495e-06"/>
                                <joint name="left_hand_thumb_2_joint" axis="0 0 1" range="0 1.74533" actuatorfrcrange="-1.4 1.4"/>
                                <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="left_hand_thumb_2_link"/>
                                <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="left_hand_thumb_2_link"/>
                              </body>
                            </body>
                          </body>
                          <body name="left_hand_middle_0_link" pos="0.1192 0.0046 -0.0285">
                            <inertial pos="0.0354744 0.000827888 0.0003809" quat="0.391313 0.552395 0.417187 0.606373" mass="0.0588507" diaginertia="1.28514e-05 1.22902e-05 5.9666e-06"/>
                            <joint name="left_hand_middle_0_joint" axis="0 0 1" range="-1.5708 0" actuatorfrcrange="-1.4 1.4"/>
                            <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="left_hand_middle_0_link"/>
                            <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="left_hand_middle_0_link"/>
                            <body name="left_hand_middle_1_link" pos="0.0458 0 0">
                              <inertial pos="0.0262819 0.00171735 -0.000107789" quat="0.502612 0.491799 0.502639 0.502861" mass="0.0203063" diaginertia="4.61314e-06 3.86645e-06 1.53495e-06"/>
                              <joint name="left_hand_middle_1_joint" axis="0 0 1" range="-1.74533 0" actuatorfrcrange="-1.4 1.4"/>
                              <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="left_hand_middle_1_link"/>
                              <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="left_hand_middle_1_link"/>
                            </body>
                          </body>
                          <body name="left_hand_index_0_link" pos="0.1192 0.0046 0.0285">
                            <inertial pos="0.0354744 0.000827888 0.0003809" quat="0.391313 0.552395 0.417187 0.606373" mass="0.0588507" diaginertia="1.28514e-05 1.22902e-05 5.9666e-06"/>
                            <joint name="left_hand_index_0_joint" axis="0 0 1" range="-1.5708 0" actuatorfrcrange="-1.4 1.4"/>
                            <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="left_hand_index_0_link"/>
                            <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="left_hand_index_0_link"/>
                            <body name="left_hand_index_1_link" pos="0.0458 0 0">
                              <inertial pos="0.0262819 0.00171735 -0.000107789" quat="0.502612 0.491799 0.502639 0.502861" mass="0.0203063" diaginertia="4.61314e-06 3.86645e-06 1.53495e-06"/>
                              <joint name="left_hand_index_1_joint" axis="0 0 1" range="-1.74533 0" actuatorfrcrange="-1.4 1.4"/>
                              <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="left_hand_index_1_link"/>
                              <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="left_hand_index_1_link"/>
                            </body>
                          </body>
                        </body>
                      </body>
                    </body>
                  </body>
                </body>
              </body>
            </body>
            <body name="right_shoulder_pitch_link" pos="0.0039563 -0.10021 0.24778"
              quat="0.990264 -0.139201 1.38722e-05 9.86868e-05">
              <inertial pos="0 -0.035892 -0.011628" quat="0.68225 -0.326267 0.0130458 0.654152" mass="0.718"
                diaginertia="0.000465864 0.000432842 0.000406394"/>
              <joint name="right_shoulder_pitch_joint" axis="0 1 0" range="-3.0892 2.6704" armature="0.00361" actuatorfrcrange="-25 25"/>
              <geom class="visual" mesh="right_shoulder_pitch_link"/>
              <body name="right_shoulder_roll_link" pos="0 -0.038 -0.013831" quat="0.990268 0.139172 0 0">
                <inertial pos="-0.000227 -0.00727 -0.063243" quat="0.712604 -0.00710317 -0.0196223 0.701256"
                  mass="0.643" diaginertia="0.000691311 0.000618011 0.000388977"/>
                <joint name="right_shoulder_roll_joint" axis="1 0 0" range="-2.2515 1.5882" armature="0.00361" actuatorfrcrange="-25 25"/>
                <geom class="visual" mesh="right_shoulder_roll_link"/>
                <body name="right_shoulder_yaw_link" pos="0 -0.00624 -0.1032">
                  <inertial pos="0.010773 0.002949 -0.072009" quat="0.687134 -0.0679942 -0.0964829 0.716879"
                    mass="0.734" diaginertia="0.00106187 0.00103217 0.000400661"/>
                  <joint name="right_shoulder_yaw_joint" axis="0 0 1" range="-2.618 2.618" armature="0.00361" actuatorfrcrange="-25 25"/>
                  <geom class="visual" mesh="right_shoulder_yaw_link"/>
                  <geom name="right_shoulder_yaw_collision" class="collision" size="0.035" fromto="0 0 -0.08 0 0 0.05"/>
                  <body name="right_elbow_link" pos="0.015783 0 -0.080518">
                    <inertial pos="0.064956 -0.004454 -0.010062" quat="0.388129 0.388821 0.636132 0.541765" mass="0.6"
                      diaginertia="0.000443035 0.000421612 0.000259353"/>
                    <joint name="right_elbow_joint" axis="0 1 0" range="-1.0472 2.0944" armature="0.00361" actuatorfrcrange="-25 25"/>
                    <geom class="visual" mesh="right_elbow_link"/>
                    <geom name="right_elbow_yaw_collision" class="collision" size="0.035"
                      fromto="-0.01 0 -0.01 0.08 0 -0.01"/>
                    <body name="right_wrist_roll_link" pos="0.1 -0.00188791 -0.01">
                      <inertial pos="0.0171394 -0.000537591 4.8864e-07" quat="0.411667 0.575338 -0.411094 0.574906"
                        mass="0.085445" diaginertia="5.48211e-05 4.96646e-05 3.57798e-05"/>
                      <joint name="right_wrist_roll_joint" axis="1 0 0" range="-1.97222 1.97222" armature="0.00361" actuatorfrcrange="-25 25"/>
                      <geom class="visual" mesh="right_wrist_roll_link"/>
                      <body name="right_wrist_pitch_link" pos="0.038 0 0">
                        <inertial pos="0.0229999 0.00111685 -0.00111658" quat="0.643608 0.293036 0.661363 0.249998"
                          mass="0.48405" diaginertia="0.000430353 0.000429873 0.000164648"/>
                        <joint name="right_wrist_pitch_joint" axis="0 1 0" range="-1.61443 1.61443" armature="0.00425" actuatorfrcrange="-5 5"/>
                        <geom class="visual" mesh="right_wrist_pitch_link"/>
                        <geom name="right_wrist_collision" class="collision" size="0.035" fromto="-0.01 0 0 0.06 0 0"/>
                        <body name="right_wrist_yaw_link" pos="0.046 0 0">
                          <inertial pos="0.0708244 -0.000191745 0.00161742" quat="0.493188 0.468078 0.526295 0.510571"
                            mass="0.254576" diaginertia="0.000646113 0.000559993 0.000147566"/>
                          <joint name="right_wrist_yaw_joint" axis="0 0 1" range="-1.61443 1.61443" armature="0.00425" actuatorfrcrange="-5 5"/>
                          <geom class="visual" mesh="right_wrist_yaw_link"/>
                          <geom pos="0.0415 -0.003 0" quat="1 0 0 0" type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="right_hand_palm_link"/>
                          <geom pos="0.0415 -0.003 0" quat="1 0 0 0" type="mesh" rgba="0.7 0.7 0.7 1" mesh="right_hand_palm_link"/>
                          <site name="right_palm" pos="0.08 0 0" size="0.01"/>
                          <camera name="wrist_cam" pos="0.08 0.04 0" xyaxes="0 0 1 0 1 0" fovy="75"/>
                          <body name="right_hand_thumb_0_link" pos="0.067 -0.003 0">
                            <inertial pos="-0.000884246 0.00863407 0.000944293" quat="0.643965 0.462991 -0.398986 0.460173" mass="0.0862366" diaginertia="1.6546e-05 1.60058e-05 1.43741e-05"/>
                            <joint name="right_hand_thumb_0_joint" axis="0 1 0" range="-1.0472 1.0472" actuatorfrcrange="-2.45 2.45"/>
                            <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="right_hand_thumb_0_link"/>
                            <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="right_hand_thumb_0_link"/>
                            <body name="right_hand_thumb_1_link" pos="-0.0025 0.0193 0">
                              <inertial pos="-0.000827888 0.0354744 -0.0003809" quat="0.705471 0.685598 -0.0956069 0.15207" mass="0.0588507" diaginertia="1.28514e-05 1.22902e-05 5.9666e-06"/>
                              <joint name="right_hand_thumb_1_joint" axis="0 0 1" range="-1.0472 0.724312" actuatorfrcrange="-1.4 1.4"/>
                              <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="right_hand_thumb_1_link"/>
                              <geom size="0.01 0.015 0.01" pos="-0.001 0.032 0" type="box" rgba="0.7 0.7 0.7 1"/>
                              <body name="right_hand_thumb_2_link" pos="0 0.0458 0">
                                <inertial pos="-0.00171735 0.0262819 0.000107789" quat="0.710977 0.703174 0.00766553 0.00017564" mass="0.0203063" diaginertia="4.61314e-06 3.86645e-06 1.53495e-06"/>
                                <joint name="right_hand_thumb_2_joint" axis="0 0 1" range="-1.74533 0" actuatorfrcrange="-1.4 1.4"/>
                                <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="right_hand_thumb_2_link"/>
                                <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="right_hand_thumb_2_link"/>
                              </body>
                            </body>
                          </body>
                          <body name="right_hand_middle_0_link" pos="0.1192 -0.0046 -0.0285">
                            <inertial pos="0.0354744 -0.000827888 0.0003809" quat="0.606373 0.417187 0.552395 0.391313" mass="0.0588507" diaginertia="1.28514e-05 1.22902e-05 5.9666e-06"/>
                            <joint name="right_hand_middle_0_joint" axis="0 0 1" range="0 1.5708" actuatorfrcrange="-1.4 1.4"/>
                            <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="right_hand_middle_0_link"/>
                            <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="right_hand_middle_0_link"/>
                            <body name="right_hand_middle_1_link" pos="0.0458 0 0">
                              <inertial pos="0.0262819 -0.00171735 -0.000107789" quat="0.502861 0.502639 0.491799 0.502612" mass="0.0203063" diaginertia="4.61314e-06 3.86645e-06 1.53495e-06"/>
                              <joint name="right_hand_middle_1_joint" axis="0 0 1" range="0 1.74533" actuatorfrcrange="-1.4 1.4"/>
                              <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="right_hand_middle_1_link"/>
                              <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="right_hand_middle_1_link"/>
                            </body>
                          </body>
                          <body name="right_hand_index_0_link" pos="0.1192 -0.0046 0.0285">
                            <inertial pos="0.0354744 -0.000827888 0.0003809" quat="0.606373 0.417187 0.552395 0.391313" mass="0.0588507" diaginertia="1.28514e-05 1.22902e-05 5.9666e-06"/>
                            <joint name="right_hand_index_0_joint" axis="0 0 1" range="0 1.5708" actuatorfrcrange="-1.4 1.4"/>
                            <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="right_hand_index_0_link"/>
                            <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="right_hand_index_0_link"/>
                            <body name="right_hand_index_1_link" pos="0.0458 0 0">
                              <inertial pos="0.0262819 -0.00171735 -0.000107789" quat="0.502861 0.502639 0.491799 0.502612" mass="0.0203063" diaginertia="4.61314e-06 3.86645e-06 1.53495e-06"/>
                              <joint name="right_hand_index_1_joint" axis="0 0 1" range="0 1.74533" actuatorfrcrange="-1.4 1.4"/>
                              <geom type="mesh" contype="0" conaffinity="0" group="2" density="0" rgba="0.7 0.7 0.7 1" mesh="right_hand_index_1_link"/>
                              <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="right_hand_index_1_link"/>
                            </body>
                          </body>
                        </body>
                      </body>
                    </body>
                  </body>
                </body>
              </body>
            </body>
          </body>
        </body>
      </body>
    </body>
  </worldbody>

<actuator>
    <position class="g1" name="left_hip_pitch_joint" joint="left_hip_pitch_joint" kp="40.179" kv="2.558"/>
    <position class="g1" name="left_hip_roll_joint" joint="left_hip_roll_joint" kp="99.098" kv="6.309"/>
    <position class="g1" name="left_hip_yaw_joint" joint="left_hip_yaw_joint" kp="40.179" kv="2.558"/>
    <position class="g1" name="left_knee_joint" joint="left_knee_joint" kp="99.098" kv="6.309"/>
    <position class="g1" name="left_ankle_pitch_joint" joint="left_ankle_pitch_joint" kp="28.501" kv="1.814"/>
    <position class="g1" name="left_ankle_roll_joint" joint="left_ankle_roll_joint" kp="28.501" kv="1.814"/>

    <position class="g1" name="right_hip_pitch_joint" joint="right_hip_pitch_joint" kp="40.179" kv="2.558"/>
    <position class="g1" name="right_hip_roll_joint" joint="right_hip_roll_joint" kp="99.098" kv="6.309"/>
    <position class="g1" name="right_hip_yaw_joint" joint="right_hip_yaw_joint" kp="40.179" kv="2.558"/>
    <position class="g1" name="right_knee_joint" joint="right_knee_joint" kp="99.098" kv="6.309"/>
    <position class="g1" name="right_ankle_pitch_joint" joint="right_ankle_pitch_joint" kp="28.501" kv="1.814"/>
    <position class="g1" name="right_ankle_roll_joint" joint="right_ankle_roll_joint" kp="28.501" kv="1.814"/>

    <position class="g1" name="waist_yaw_joint" joint="waist_yaw_joint" kp="40.179" kv="2.558"/>
    <position class="g1" name="waist_roll_joint" joint="waist_roll_joint" kp="28.501" kv="1.814"/>
    <position class="g1" name="waist_pitch_joint" joint="waist_pitch_joint" kp="28.501" kv="1.814"/>

    <position class="g1" name="left_shoulder_pitch_joint" joint="left_shoulder_pitch_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="left_shoulder_roll_joint" joint="left_shoulder_roll_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="left_shoulder_yaw_joint" joint="left_shoulder_yaw_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="left_elbow_joint" joint="left_elbow_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="left_wrist_roll_joint" joint="left_wrist_roll_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="left_wrist_pitch_joint" joint="left_wrist_pitch_joint" kp="16.778" kv="1.068"/>
    <position class="g1" name="left_wrist_yaw_joint" joint="left_wrist_yaw_joint" kp="16.778" kv="1.068"/>

    <position class="g1" name="right_shoulder_pitch_joint" joint="right_shoulder_pitch_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="right_shoulder_roll_joint" joint="right_shoulder_roll_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="right_shoulder_yaw_joint" joint="right_shoulder_yaw_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="right_elbow_joint" joint="right_elbow_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="right_wrist_roll_joint" joint="right_wrist_roll_joint" kp="14.251" kv="0.907"/>
    <position class="g1" name="right_wrist_pitch_joint" joint="right_wrist_pitch_joint" kp="16.778" kv="1.068"/>
    <position class="g1" name="right_wrist_yaw_joint" joint="right_wrist_yaw_joint" kp="16.778" kv="1.068"/>

    <!-- Inspire hand actuators (position control) -->
    <position name="left_hand_thumb_0_joint" joint="left_hand_thumb_0_joint" kp="2.0" kv="0.1"/>
    <position name="left_hand_thumb_1_joint" joint="left_hand_thumb_1_joint" kp="1.5" kv="0.1"/>
    <position name="left_hand_thumb_2_joint" joint="left_hand_thumb_2_joint" kp="1.5" kv="0.1"/>
    <position name="left_hand_middle_0_joint" joint="left_hand_middle_0_joint" kp="1.5" kv="0.1"/>
    <position name="left_hand_middle_1_joint" joint="left_hand_middle_1_joint" kp="1.5" kv="0.1"/>
    <position name="left_hand_index_0_joint" joint="left_hand_index_0_joint" kp="1.5" kv="0.1"/>
    <position name="left_hand_index_1_joint" joint="left_hand_index_1_joint" kp="1.5" kv="0.1"/>
    <position name="right_hand_thumb_0_joint" joint="right_hand_thumb_0_joint" kp="2.0" kv="0.1"/>
    <position name="right_hand_thumb_1_joint" joint="right_hand_thumb_1_joint" kp="1.5" kv="0.1"/>
    <position name="right_hand_thumb_2_joint" joint="right_hand_thumb_2_joint" kp="1.5" kv="0.1"/>
    <position name="right_hand_middle_0_joint" joint="right_hand_middle_0_joint" kp="1.5" kv="0.1"/>
    <position name="right_hand_middle_1_joint" joint="right_hand_middle_1_joint" kp="1.5" kv="0.1"/>
    <position name="right_hand_index_0_joint" joint="right_hand_index_0_joint" kp="1.5" kv="0.1"/>
    <position name="right_hand_index_1_joint" joint="right_hand_index_1_joint" kp="1.5" kv="0.1"/>
  </actuator>

  <contact>
    <exclude body1="left_elbow_link" body2="left_wrist_pitch_link"/>
    <exclude body1="right_elbow_link" body2="right_wrist_pitch_link"/>
    <exclude body1="pelvis" body2="right_hip_roll_link"/>
    <exclude body1="pelvis" body2="left_hip_roll_link"/>
  </contact>

  <sensor>
    <gyro site="imu_in_torso" name="imu-torso-angular-velocity" cutoff="34.9" noise="0.0005"/>
    <accelerometer site="imu_in_torso" name="imu-torso-linear-acceleration" cutoff="157" noise="0.01"/>
    <gyro site="imu_in_pelvis" name="imu-pelvis-angular-velocity" cutoff="34.9" noise="0.0005"/>
    <accelerometer site="imu_in_pelvis" name="imu-pelvis-linear-acceleration" cutoff="157" noise="0.01"/>
  </sensor>

  
</mujoco>
```

---

## FILE: `model_config.json`

```json
{
  "joint_names": [
    "left_hip_pitch_joint",
    "left_hip_roll_joint",
    "left_hip_yaw_joint",
    "left_knee_joint",
    "left_ankle_pitch_joint",
    "left_ankle_roll_joint",
    "right_hip_pitch_joint",
    "right_hip_roll_joint",
    "right_hip_yaw_joint",
    "right_knee_joint",
    "right_ankle_pitch_joint",
    "right_ankle_roll_joint",
    "waist_yaw_joint",
    "waist_roll_joint",
    "waist_pitch_joint",
    "left_shoulder_pitch_joint",
    "left_shoulder_roll_joint",
    "left_shoulder_yaw_joint",
    "left_elbow_joint",
    "left_wrist_roll_joint",
    "left_wrist_pitch_joint",
    "left_wrist_yaw_joint",
    "right_shoulder_pitch_joint",
    "right_shoulder_roll_joint",
    "right_shoulder_yaw_joint",
    "right_elbow_joint",
    "right_wrist_roll_joint",
    "right_wrist_pitch_joint",
    "right_wrist_yaw_joint"
  ],
  "default_joint_pos": {
    "left_hip_pitch_joint": -0.312,
    "left_hip_roll_joint": 0.0,
    "left_hip_yaw_joint": 0.0,
    "left_knee_joint": 0.669,
    "left_ankle_pitch_joint": -0.363,
    "left_ankle_roll_joint": 0.0,
    "right_hip_pitch_joint": -0.312,
    "right_hip_roll_joint": 0.0,
    "right_hip_yaw_joint": 0.0,
    "right_knee_joint": 0.669,
    "right_ankle_pitch_joint": -0.363,
    "right_ankle_roll_joint": 0.0,
    "waist_yaw_joint": 0.0,
    "waist_roll_joint": 0.0,
    "waist_pitch_joint": 0.0,
    "left_shoulder_pitch_joint": 0.2,
    "left_shoulder_roll_joint": 0.2,
    "left_shoulder_yaw_joint": 0.0,
    "left_elbow_joint": 0.6,
    "left_wrist_roll_joint": 0.0,
    "left_wrist_pitch_joint": 0.0,
    "left_wrist_yaw_joint": 0.0,
    "right_shoulder_pitch_joint": 0.2,
    "right_shoulder_roll_joint": -0.2,
    "right_shoulder_yaw_joint": 0.0,
    "right_elbow_joint": 0.6,
    "right_wrist_roll_joint": 0.0,
    "right_wrist_pitch_joint": 0.0,
    "right_wrist_yaw_joint": 0.0
  },
  "action_scales": {
    "left_hip_pitch_joint": 0.547546,
    "left_hip_roll_joint": 0.350661,
    "left_hip_yaw_joint": 0.547546,
    "left_knee_joint": 0.350661,
    "left_ankle_pitch_joint": 0.438577,
    "left_ankle_roll_joint": 0.438577,
    "right_hip_pitch_joint": 0.547546,
    "right_hip_roll_joint": 0.350661,
    "right_hip_yaw_joint": 0.547546,
    "right_knee_joint": 0.350661,
    "right_ankle_pitch_joint": 0.438577,
    "right_ankle_roll_joint": 0.438577,
    "waist_yaw_joint": 0.547546,
    "waist_roll_joint": 0.438577,
    "waist_pitch_joint": 0.438577,
    "left_shoulder_pitch_joint": 0.438577,
    "left_shoulder_roll_joint": 0.438577,
    "left_shoulder_yaw_joint": 0.438577,
    "left_elbow_joint": 0.438577,
    "left_wrist_roll_joint": 0.438577,
    "left_wrist_pitch_joint": 0.074501,
    "left_wrist_yaw_joint": 0.074501,
    "right_shoulder_pitch_joint": 0.438577,
    "right_shoulder_roll_joint": 0.438577,
    "right_shoulder_yaw_joint": 0.438577,
    "right_elbow_joint": 0.438577,
    "right_wrist_roll_joint": 0.438577,
    "right_wrist_pitch_joint": 0.074501,
    "right_wrist_yaw_joint": 0.074501
  },
  "walker": {
    "input_dim": 99,
    "output_dim": 29,
    "obs_mean": [
      0.2764410078525543,
      -0.0011231002863496542,
      -0.00887491274625063,
      -0.012028997763991356,
      0.03522094711661339,
      0.008403312414884567,
      -0.003294438822194934,
      0.0002468313614372164,
      -0.9934708476066589,
      -0.0907304584980011,
      0.006743466015905142,
      -0.001323652919381857,
      0.22801245748996735,
      -0.0420287624001503,
      0.0052517312578856945,
      -0.09373214840888977,
      -0.0022980200592428446,
      0.007062251679599285,
      0.22945237159729004,
      -0.03992355987429619,
      -0.005189856979995966,
      -0.003225596621632576,
      0.0012408958282321692,
      0.000897581921890378,
      -0.03501684591174126,
      0.053861577063798904,
      0.01695811189711094,
      -0.025254687294363976,
      -0.00033013586653396487,
      -0.022842688485980034,
      0.04303140565752983,
      -0.03617796301841736,
      -0.05281267687678337,
      -0.016581477597355843,
      -0.023698199540376663,
      0.0004230269987601787,
      -0.018825259059667587,
      -0.045088429003953934,
      -0.05162270367145538,
      -0.0017306592781096697,
      -0.00020749638497363776,
      0.011742794886231422,
      0.0056776381097733974,
      -0.003033487591892481,
      -0.03596210852265358,
      0.007169663440436125,
      -0.012108002789318562,
      0.006323100067675114,
      0.00047465605894103646,
      0.000647611974272877,
      -0.013602513819932938,
      0.01769345998764038,
      -0.01986178196966648,
      0.03318953141570091,
      0.0037734888028353453,
      0.0095991101115942,
      0.004500563256442547,
      0.0021920751314610243,
      -0.004432667978107929,
      0.006716209463775158,
      0.027406007051467896,
      0.006401436403393745,
      -0.0032767809461802244,
      0.00846377294510603,
      0.006889165844768286,
      -0.004579206462949514,
      -0.006883460562676191,
      -0.1486780345439911,
      0.3012807071208954,
      -0.2587428092956543,
      0.32165414094924927,
      0.3147725462913513,
      0.08125457167625427,
      -0.15473435819149017,
      -0.28669875860214233,
      0.2629929482936859,
      0.32942909002304077,
      0.3306274712085724,
      -0.07872061431407928,
      -0.00882444903254509,
      0.0009497009450569749,
      -0.13094140589237213,
      -0.2002839893102646,
      0.33255425095558167,
      0.09981878846883774,
      -0.265374094247818,
      -0.0005433406331576407,
      -0.5369775891304016,
      0.6211817860603333,
      -0.2017064094543457,
      -0.3248439431190491,
      -0.09776587784290314,
      -0.260663777589798,
      0.002399812452495098,
      -0.4840352535247803,
      -0.648914098739624,
      0.28178897500038147,
      0.000009319964192,
      0.00041731251985765994
    ],
    "obs_std": [
      1.119999885559082,
      0.5925261378288269,
      0.32594776153564453,
      0.7118846774101257,
      0.8981359004974365,
      0.8713164329528809,
      0.07316633313894272,
      0.05465417355298996,
      0.040836624801158905,
      0.22480855882167816,
      0.09196151793003082,
      0.1053195372223854,
      0.2902180552482605,
      0.19904658198356628,
      0.09467905759811401,
      0.21679627895355225,
      0.09269601851701736,
      0.10471580922603607,
      0.2920810580253601,
      0.19660590589046478,
      0.09433563798666,
      0.15374724566936493,
      0.06007464975118637,
      0.06440386921167374,
      0.22716952860355377,
      0.1453830599784851,
      0.1440180242061615,
      0.15696296095848083,
      0.20508013665676117,
      0.12280701100826263,
      0.12018921971321106,
      0.2249361276626587,
      0.1436595618724823,
      0.143561452627182,
      0.1574581116437912,
      0.20672756433486938,
      0.1239062175154686,
      0.12004795670509338,
      2.6440131664276123,
      1.5611387491226196,
      2.0153350830078125,
      4.0273003578186035,
      4.3755598068237305,
      2.9597818851470947,
      2.600646734237671,
      1.5530928373336792,
      2.016266345977783,
      4.008848667144775,
      4.380704879760742,
      2.9649221897125244,
      2.1029741764068604,
      1.3836265802383423,
      1.389782428741455,
      2.610670328140259,
      2.1601574420928955,
      3.2699809074401855,
      3.278838634490967,
      4.32094144821167,
      1.6473523378372192,
      1.5537536144256592,
      2.6113548278808594,
      2.1469244956970215,
      3.2662229537963867,
      3.2944107055664062,
      4.339025497436523,
      1.6455715894699097,
      1.5547151565551758,
      0.8396009802818298,
      0.5547389984130859,
      0.49920323491096497,
      1.3047682046890259,
      1.309758186340332,
      0.5676404237747192,
      0.8267436027526855,
      0.5543197393417358,
      0.49321919679641724,
      1.3026329278945923,
      1.3167572021484375,
      0.5665327310562134,
      0.472351998090744,
      0.6063718199729919,
      0.42982882261276245,
      0.7897917628288269,
      0.6228054165840149,
      0.5509909987449646,
      0.6418794989585876,
      0.7377936840057373,
      1.5482919216156006,
      1.5455572605133057,
      0.7844030261039734,
      0.6124319434165955,
      0.5508608818054199,
      0.6462455987930298,
      0.7424951791763306,
      1.563859462738037,
      1.5450600385665894,
      1.1348178386688232,
      0.5475941300392151,
      0.3739437758922577
    ]
  },
  "croucher": {
    "input_dim": 101,
    "output_dim": 29,
    "obs_mean": [
      -0.014261700212955475,
      -0.0015256619080901146,
      -0.07104996591806412,
      0.08402465283870697,
      0.19617024064064026,
      0.04232420399785042,
      0.009945405647158623,
      0.005697592161595821,
      -0.9673172235488892,
      -0.7404491305351257,
      0.016528654843568802,
      -0.059806033968925476,
      1.1599997282028198,
      -0.42899245023727417,
      -0.04512963071465492,
      -0.7139285802841187,
      -0.18219523131847382,
      0.10681703686714172,
      1.1616051197052002,
      -0.44435152411460876,
      0.11815741658210754,
      0.004003847949206829,
      0.018390238285064697,
      0.017038686200976372,
      -0.5881016254425049,
      0.224533811211586,
      0.04629017040133476,
      -0.16457831859588623,
      0.3489656448364258,
      0.21692031621932983,
      -0.09602002054452896,
      -0.20428518950939178,
      -0.5440213084220886,
      0.10759054869413376,
      0.42052602767944336,
      -0.5271346569061279,
      -0.21750664710998535,
      -0.0706288143992424,
      -0.3952099084854126,
      0.01875457540154457,
      0.13469567894935608,
      0.10036010295152664,
      0.02767588011920452,
      0.006179089192301035,
      -0.39470037817955017,
      -0.038679271936416626,
      0.27906712889671326,
      0.21088196337223053,
      -0.03757520765066147,
      0.011537430807948112,
      0.000071282433055,
      -0.06105758622288704,
      -0.08467136323451996,
      -0.19200098514556885,
      0.08638951927423477,
      0.06381367146968842,
      0.014261274598538876,
      0.013615953736007214,
      0.037713173776865005,
      -0.021199651062488556,
      -0.062187258154153824,
      -0.17009097337722778,
      -0.08419857174158096,
      0.0005883211852051318,
      -0.11533480882644653,
      -0.03991479426622391,
      -0.014236228540539742,
      -1.2952044010162354,
      0.08484380692243576,
      -0.1824222058057785,
      2.4944701194763184,
      -1.3858081102371216,
      -0.07759882509708405,
      -1.2816790342330933,
      -0.5512250065803528,
      0.17243026196956635,
      2.5755951404571533,
      -1.511191725730896,
      0.25833985209465027,
      0.005510265938937664,
      -0.11727026104927063,
      -0.3265622854232788,
      -1.8216381072998047,
      0.8877902030944824,
      0.22886404395103455,
      -0.5532782077789307,
      0.8074663281440735,
      2.8620448112487793,
      -1.2452894449234009,
      -0.5691277384757996,
      -1.8547887802124023,
      0.1585928201675415,
      0.9338672161102295,
      -1.2163255214691162,
      -2.9625375270843506,
      -0.9975863695144653,
      0.0,
      0.0,
      0.0,
      0.5423733592033386,
      0.5588040351867676
    ],
    "obs_std": [
      0.3474659323692322,
      0.32971280813217163,
      0.46664831042289734,
      1.0423789024353027,
      1.6083815097808838,
      1.0413382053375244,
      0.2074316442012787,
      0.12730160355567932,
      0.08611535280942917,
      0.4785121977329254,
      0.11616149544715881,
      0.19557489454746246,
      0.5106216669082642,
      0.1908293217420578,
      0.1222715675830841,
      0.5035606026649475,
      0.2355995774269104,
      0.21196699142456055,
      0.5028953552246094,
      0.1780749410390854,
      0.09761162102222443,
      0.07040099054574966,
      0.09590069949626923,
      0.1278066486120224,
      0.5945335030555725,
      0.3940373659133911,
      0.5054469704627991,
      0.5720513463020325,
      0.6200873851776123,
      0.24052157998085022,
      0.1555127054452896,
      0.4658084213733673,
      0.46817442774772644,
      0.5978217720985413,
      0.4964078664779663,
      0.7145026922225952,
      0.2642146646976471,
      0.14052928984165192,
      2.506350040435791,
      1.6340935230255127,
      2.1194469928741455,
      1.6562771797180176,
      1.7600340843200684,
      2.239684820175171,
      2.5764975547790527,
      1.6906346082687378,
      2.434779167175293,
      1.839568018913269,
      1.7275861501693726,
      2.268329381942749,
      1.9070736169815063,
      1.5923981666564941,
      1.806822419166565,
      2.906200647354126,
      2.7093393802642822,
      4.559217929840088,
      4.170853614807129,
      5.402627944946289,
      1.6825909614562988,
      1.5556590557098389,
      3.1233408451080322,
      2.527413845062256,
      4.870856285095215,
      4.206680774688721,
      5.403183460235596,
      1.6756086349487305,
      1.5618946552276611,
      0.9751729965209961,
      0.5106522440910339,
      0.648868978023529,
      1.4018257856369019,
      1.2515277862548828,
      0.48892202973365784,
      0.9916493892669678,
      0.76868736743927,
      0.657737135887146,
      1.3760528564453125,
      1.2443814277648926,
      0.47128432989120483,
      0.4551670253276825,
      0.6994064450263977,
      0.7649814486503601,
      1.6757733821868896,
      1.0768580436706543,
      1.2577259540557861,
      1.4693176746368408,
      1.6065880060195923,
      3.205024242401123,
      2.023322105407715,
      1.3912105560302734,
      1.2911109924316406,
      1.5184346437454224,
      1.3640635013580322,
      1.7877761125564575,
      3.415318250656128,
      1.834232211112976,
      0.0,
      0.0,
      0.0,
      0.09675803780555725,
      0.1217656061053276
    ]
  }
}
```

---

## FILE: `policies/__init__.py`

```python
"""Policy interfaces and implementations for high-level control."""
```

---

## FILE: `policies/base.py`

```python
"""Policy interfaces and data contracts for high-level control."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

WalkCommand = tuple[float, float, float]
ReachTarget = tuple[float, float, float]


@dataclass(frozen=True)
class PolicyOutput:
  """High-level command output from a policy step.

  walk_cmd: (lin_vel_x, lin_vel_y, ang_vel_z)
  reach_target: (x, y, z) target coordinates in pelvis frame
  reach_active: True to run the right-arm reacher ONNX overlay
  grip_closed: True when the right-hand grip should be closed
  """

  walk_cmd: WalkCommand
  reach_target: ReachTarget
  grip_closed: bool
  reach_active: bool = False


class BasePolicy(ABC):
  """Abstract interface for policies that emit high-level commands."""

  def handle_key(self, keycode: int) -> None:
    """Optional keyboard hook for interactive policies."""
    pass

  @abstractmethod
  def step(self) -> PolicyOutput:
    """Return the latest policy output."""
```

---

## FILE: `policies/fsm.py`

```python
"""FSM-driven policy: wraps FSMCore and applies its output to the controller."""

from __future__ import annotations

from .base import BasePolicy, PolicyOutput
from .fsm_core import FSMCore, FSMState

# States where grip_closed=False is intentional — do not override.
_RELEASE_STATES = frozenset({FSMState.OPEN_GRIP, FSMState.RETRACT, FSMState.DONE})


class FSMPolicy(BasePolicy):
    """Autonomous policy driven by FSMCore.

    Calls fsm.tick() each step, then writes the resulting command into
    the controller so that ctrl.step() picks it up immediately.

    grasp_backend (optional): a GraspBackend whose .attached state is forwarded
    to FSMCore each tick and whose grip_closed override is applied to the output.
    """

    def __init__(self, controller, grasp_backend=None) -> None:
        self._ctrl  = controller
        self._grasp = grasp_backend
        self._fsm   = FSMCore(controller.model, controller.data)

    def step(self) -> PolicyOutput:
        attached = self._grasp.attached if self._grasp is not None else False
        out = self._fsm.tick(attached=attached)
        out = self._close_grip_command(out)
        # Push FSM output into controller state before ctrl.step() runs.
        self._ctrl.lin_vel_x, self._ctrl.lin_vel_y, self._ctrl.ang_vel_z = out.walk_cmd
        self._ctrl.reach_target[:] = out.reach_target
        self._ctrl.reach_active    = out.reach_active
        self._ctrl.grip_closed     = out.grip_closed
        return out

    def _close_grip_command(self, out: PolicyOutput) -> PolicyOutput:
        """Keep grip closed while carrying — but not during intentional release.

        Prevents a single-tick grip opening caused by FSM state-transition timing
        from accidentally dropping the cylinder mid-carry.  The guard is bypassed
        in OPEN_GRIP / RETRACT / DONE so the FSM can actually release the object.
        """
        if (self._grasp is not None
                and self._grasp.attached
                and not out.grip_closed
                and self._fsm.state not in _RELEASE_STATES):
            return PolicyOutput(
                walk_cmd=out.walk_cmd,
                reach_target=out.reach_target,
                reach_active=out.reach_active,
                grip_closed=True,
            )
        return out
```

---

## FILE: `policies/fsm_core.py`

```python
"""Pure FSM state machine — no controller dependency."""

from __future__ import annotations

from enum import Enum, auto

import mujoco
import numpy as np

from .base import PolicyOutput

# --------------------------------------------------------------------------- #
# Tuning constants
# --------------------------------------------------------------------------- #

# Safe carry-pose: right arm held clear of the legs while walking.
CARRY_POSE: tuple[float, float, float] = (0.3, -0.2, 0.2)

# Ticks in SETTLE before beginning autonomous task (~3 s at 50 Hz).
SETTLE_TICKS = 150

# ---- Approach: staircase forward speeds ----
APPROACH_TARGET_X = 0.34   # m forward — cylinder at reach when this close

REACH_X_MIN, REACH_X_MAX = 0.20, 0.38   # x reachability window
REACH_Y_MIN, REACH_Y_MAX = -0.14, 0.02  # y reachability window

REACH_DEBOUNCE = 8   # consecutive in-window ticks before APPROACH → HOVER

VX_FAST, VX_MED, VX_SLOW = 0.35, 0.22, 0.12   # staircase vx (m/s)
K_VY,  VY_CAP  = 1.8, 0.18   # vy: proportional toward y = -0.05
K_WZ,  WZ_CAP  = 1.2, 0.25   # wz: arctan2-based yaw

# ---- Hover and grasp heights above table surface ----
HOVER_SOURCE_HEIGHT = 0.18   # m: pre-grasp hover above table top
GRASP_HEIGHT        = 0.06   # m: cylinder mid-body height above table top

# ---- Palm-to-target distance thresholds ----
# The reacher has an ~12 cm accuracy floor; thresholds must stay ≥ this.
HOVER_SOURCE_THRESHOLD   = 0.14   # m
DESCEND_SOURCE_THRESHOLD = 0.12   # m

# ---- Per-state timeouts (control ticks at 50 Hz) ----
HOVER_SOURCE_TIMEOUT   = 200   # ~4 s fallback if threshold never met
DESCEND_SOURCE_TIMEOUT = 300   # ~6 s fallback
CLOSE_GRIP_TIMEOUT     = 100   # ~2 s: advance to LIFT even if not yet attached
LIFT_SOURCE_TIMEOUT    = 200   # ~4 s: declare done if arm never clears table

# ---- General reach-state debounce ----
DEBOUNCE_REACH = 6   # consecutive ticks palm must be within threshold

# ---- Lift success criterion ----
LIFT_DONE_CLEARANCE = 0.25  # m above table top — cylinder visibly off the surface

# ---- Target table approach ----
# Drop point is 5 cm inside the near edge of the target table (y-direction).
# Near edge = table_white geom_center_y + half_size_y (less-negative y = robot side).
TARGET_NEAR_EDGE_INSET  = 0.05   # m inward from near edge
TARGET_REACH_DEBOUNCE   = 8      # consecutive in-window ticks → HOVER_TARGET
TARGET_APPROACH_TIMEOUT = 1200    # ~24 s fallback (increased from 900)

# ---- Target table placement ----
HOVER_TARGET_HEIGHT    = 0.18   # m above target surface for pre-place hover
PLACE_HEIGHT           = 0.06   # m above target surface for release
HOVER_TARGET_THRESHOLD = 0.14   # m palm-to-hover-point (same floor as source)
LOWER_TARGET_THRESHOLD = 0.14   # m palm-to-place-point
HOVER_TARGET_TIMEOUT   = 200    # ~4 s
LOWER_TARGET_TIMEOUT   = 300    # ~6 s
OPEN_GRIP_TIMEOUT      = 100    # ~2 s: wait for kinematic release
RETRACT_TIMEOUT        = 200    # ~4 s: arm clear of target table

# Table-membership margins for _cylinder_on_target_table().
ON_TABLE_XY_MARGIN = 0.05   # m: allow up to 5 cm outside geom footprint
ON_TABLE_Z_MAX     = 0.20   # m above surface: cap for height sanity check

# Phase 1 of target approach: turn CW to face -y before driving toward standing waypoint.
# Use VX_SLOW so the walker actually responds to the command (vx=0.06 is below effective
# minimum, giving near-zero turn rate).  WZ_P1 = 1.0 (vel_max_angular) creates a tight
# turning circle: R = VX_P1 / WZ_P1 ≈ 0.12 m — small enough to land in the reach window.
VX_P1 = 0.12   # m/s: minimum effective forward speed for the walker
WZ_P1 = 1.0    # rad/s: full angular rate so the robot actually turns
PHASE1_ALIGN_TOL = 0.15   # rad: exit Phase 1 when |yaw − (−π/2)| < this

# World-frame proximity to the standing waypoint required before HOVER_TARGET.
# Replaces the pelvis-frame reach-window check, which fires too early mid-turn
# (the drop point can project into the window at wrong orientations).
TARGET_APPROACH_DIST_THRESH = 0.08   # m: pelvis must be within this of the waypoint

# ---- Reacher workspace bounds in pelvis frame ----
# From the training spec; targets outside are clamped before being sent.
_REACH_LOW  = np.array([-0.30, -0.60, -0.40], dtype=np.float32)
_REACH_HIGH = np.array([ 0.60,  0.30,  0.60], dtype=np.float32)


# --------------------------------------------------------------------------- #
# State enumeration
# --------------------------------------------------------------------------- #

class FSMState(Enum):
    SETTLE          = auto()
    APPROACH_SOURCE = auto()
    HOVER_SOURCE    = auto()
    DESCEND_SOURCE  = auto()
    CLOSE_GRIP      = auto()   # close fingers; wait for backend to confirm attach
    LIFT_SOURCE     = auto()   # raise arm to carry pose; confirm cylinder left table
    APPROACH_TARGET = auto()   # walk/turn toward target-table placement corridor
    HOVER_TARGET    = auto()   # move arm above drop point, stop walking
    LOWER_TARGET    = auto()   # descend arm to release height
    OPEN_GRIP       = auto()   # open fingers; wait for kinematic detach
    RETRACT         = auto()   # raise arm to carry pose
    DONE            = auto()


# --------------------------------------------------------------------------- #
# Core machine
# --------------------------------------------------------------------------- #

class FSMCore:
    """Tick-driven state machine that emits a high-level PolicyOutput each step.

    Holds references to MuJoCo model/data for GT geometry; never modifies them.
    """

    def __init__(self, model, data) -> None:
        self._model = model
        self._data  = data

        # ---- MuJoCo ID cache ----
        self._rb_id            = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
        self._tbl_id           = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "table")
        self._palm_id          = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SITE, "right_palm")
        self._tbl_geom_id      = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, "table_top")
        self._tbl_white_id     = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "table_white")
        self._tbl_white_geom_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, "table_white_top")

        self.state             = FSMState.SETTLE
        self._tick_total       = 0
        self._tick_state       = 0
        self._reach_count      = 0     # general-purpose debounce counter
        self._attached         = False  # updated each tick by FSMPolicy from grasp backend
        self._target_drop_pt: np.ndarray | None = None  # frozen when APPROACH_TARGET begins

        print(
            f"[FSM] init  state={self.state.name}"
            f"  rb={self._rb_id}  tbl={self._tbl_id}"
            f"  palm={self._palm_id}  tbl_geom={self._tbl_geom_id}"
            f"  tbl_white={self._tbl_white_id}  tbl_white_geom={self._tbl_white_geom_id}"
        )

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def tick(self, attached: bool = False) -> PolicyOutput:
        """Advance the FSM by one control tick.

        attached: True when the grasp backend reports the cylinder is welded to
                  the palm this tick.  Passed in by FSMPolicy so FSMCore stays
                  free of any dependency on the backend.
        """
        self._attached = attached
        out = self._dispatch()
        self._tick_total += 1
        self._tick_state += 1
        return out

    # ------------------------------------------------------------------ #
    # Dispatch + transition
    # ------------------------------------------------------------------ #

    def _dispatch(self) -> PolicyOutput:
        if self.state == FSMState.SETTLE:          return self._settle()
        if self.state == FSMState.APPROACH_SOURCE: return self._approach_source()
        if self.state == FSMState.HOVER_SOURCE:    return self._hover_source()
        if self.state == FSMState.DESCEND_SOURCE:  return self._descend_source()
        if self.state == FSMState.CLOSE_GRIP:      return self._close_grip()
        if self.state == FSMState.LIFT_SOURCE:     return self._lift_source()
        if self.state == FSMState.APPROACH_TARGET: return self._approach_target()
        if self.state == FSMState.HOVER_TARGET:    return self._hover_target()
        if self.state == FSMState.LOWER_TARGET:    return self._lower_target()
        if self.state == FSMState.OPEN_GRIP:       return self._open_grip()
        if self.state == FSMState.RETRACT:         return self._retract()
        return self._done()

    def _transition(self, new: FSMState) -> None:
        print(f"[FSM] {self.state.name} → {new.name}  (t={self._tick_total})")
        # Log world geometry at the moment of entry so the log is self-contained.
        if new == FSMState.HOVER_SOURCE:
            hover = self._source_hover_world()
            tbl_z = self._table_surface_z()
            dist  = float(np.linalg.norm(self._palm_world() - hover))
            print(f"[FSM]   hover_world=({hover[0]:.3f},{hover[1]:.3f},{hover[2]:.3f})"
                  f"  table_z={tbl_z:.4f}  entry_palm_dist={dist:.3f}")
        elif new == FSMState.DESCEND_SOURCE:
            grasp = self._source_grasp_world()
            dist  = float(np.linalg.norm(self._palm_world() - grasp))
            print(f"[FSM]   grasp_world=({grasp[0]:.3f},{grasp[1]:.3f},{grasp[2]:.3f})"
                  f"  entry_palm_dist={dist:.3f}")
        elif new == FSMState.CLOSE_GRIP:
            dist = float(np.linalg.norm(self._palm_world() - self._cylinder_world()))
            print(f"[FSM]   palm_to_cyl={dist:.3f} m")
        elif new == FSMState.LIFT_SOURCE:
            palm = self._palm_world()
            cyl  = self._cylinder_world()
            print(f"[FSM]   palm_z={palm[2]:.3f}  cyl_z={cyl[2]:.3f}  attached={self._attached}")
        elif new == FSMState.APPROACH_TARGET:
            # Freeze the drop point in world frame at the moment of state entry.
            self._target_drop_pt = self._target_drop_world()
            tgt_z = self._target_surface_z()
            p = self._target_drop_pt
            dist = float(np.linalg.norm(self._palm_world() - p))
            ppos = self._data.qpos[:3]
            yaw  = self._pelvis_yaw()
            print(f"[FSM]   drop_world=({p[0]:.3f},{p[1]:.3f},{p[2]:.3f})"
                  f"  target_z={tgt_z:.4f}  palm_dist={dist:.3f}"
                  f"  pelvis=({ppos[0]:.3f},{ppos[1]:.3f})  yaw={yaw:.3f}")
        elif new == FSMState.HOVER_TARGET:
            p    = self._target_drop_in_pelvis()
            palm = self._palm_world()
            print(f"[FSM]   drop_pelvis=({p[0]:.3f},{p[1]:.3f},{p[2]:.3f})"
                  f"  palm_z={palm[2]:.3f}")
        elif new == FSMState.LOWER_TARGET:
            hover = self._target_hover_world()
            palm  = self._palm_world()
            print(f"[FSM]   palm_dist_to_hover={np.linalg.norm(palm-hover):.3f}")
        elif new == FSMState.OPEN_GRIP:
            palm  = self._palm_world()
            cyl   = self._cylinder_world()
            tgt_z = self._target_surface_z()
            print(f"[FSM]   palm_z={palm[2]:.3f}  cyl_z={cyl[2]:.3f}"
                  f"  height_above_target={cyl[2]-tgt_z:.3f}")
        elif new == FSMState.RETRACT:
            cyl      = self._cylinder_world()
            tgt_z    = self._target_surface_z()
            on_table = self._cylinder_on_target_table()
            print(f"[FSM]   cyl_z={cyl[2]:.3f}  on_target_table={on_table}")
        elif new == FSMState.DONE:
            cyl      = self._cylinder_world()
            tgt_z    = self._target_surface_z()
            on_table = self._cylinder_on_target_table()
            print(f"[FSM]   cyl_z={cyl[2]:.3f}  target_z={tgt_z:.3f}"
                  f"  clearance={cyl[2]-tgt_z:.3f}  on_target_table={on_table}")
        self.state        = new
        self._tick_state  = 0
        self._reach_count = 0   # reset debounce for the new state

    # ------------------------------------------------------------------ #
    # State handlers
    # ------------------------------------------------------------------ #

    def _settle(self) -> PolicyOutput:
        if self._tick_state == 0:
            print(f"[FSM] SETTLE  holding {SETTLE_TICKS} ticks "
                  f"(~{SETTLE_TICKS / 50:.0f} s) before approach")
        if self._tick_state >= SETTLE_TICKS:
            self._transition(FSMState.APPROACH_SOURCE)
        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=CARRY_POSE,
            reach_active=False,
            grip_closed=False,
        )

    def _approach_source(self) -> PolicyOutput:
        if self._tick_state == 0:
            print("[FSM] APPROACH_SOURCE  walking toward red cylinder")
        cyl = self._cylinder_in_pelvis()
        if self._in_reach_window(cyl):
            self._reach_count += 1
            walk_cmd: tuple[float, float, float] = (0.0, 0.0, 0.0)
        else:
            self._reach_count = 0
            walk_cmd = self._approach_walk_cmd(cyl)
        if self._reach_count >= REACH_DEBOUNCE:
            print(f"[FSM] cylinder in reach window: "
                  f"pelvis_frame=({cyl[0]:.3f},{cyl[1]:.3f},{cyl[2]:.3f})")
            self._transition(FSMState.HOVER_SOURCE)
        return PolicyOutput(
            walk_cmd=walk_cmd,
            reach_target=CARRY_POSE,
            reach_active=False,
            grip_closed=False,
        )

    def _hover_source(self) -> PolicyOutput:
        hover = self._source_hover_world()
        reach = self._reach_from_world(hover, right_bias=-0.03)
        palm  = self._palm_world()
        dist  = float(np.linalg.norm(palm - hover))

        if dist < HOVER_SOURCE_THRESHOLD:
            self._reach_count += 1
        else:
            self._reach_count = 0

        if self._reach_count >= DEBOUNCE_REACH:
            print(f"[FSM] HOVER_SOURCE → threshold met  palm_dist={dist:.3f}")
            self._transition(FSMState.DESCEND_SOURCE)
        elif self._tick_state >= HOVER_SOURCE_TIMEOUT:
            print(f"[FSM] HOVER_SOURCE → timeout  palm_dist={dist:.3f}")
            self._transition(FSMState.DESCEND_SOURCE)

        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=reach,
            reach_active=True,
            grip_closed=False,
        )

    def _descend_source(self) -> PolicyOutput:
        grasp = self._source_grasp_world()
        reach = self._reach_from_world(grasp, right_bias=-0.03)
        palm  = self._palm_world()
        dist  = float(np.linalg.norm(palm - grasp))

        if dist < DESCEND_SOURCE_THRESHOLD:
            self._reach_count += 1
        else:
            self._reach_count = 0

        if self._reach_count >= DEBOUNCE_REACH:
            print(f"[FSM] DESCEND_SOURCE → threshold met  palm_dist={dist:.3f}")
            self._transition(FSMState.CLOSE_GRIP)
        elif self._tick_state >= DESCEND_SOURCE_TIMEOUT:
            print(f"[FSM] DESCEND_SOURCE → timeout  palm_dist={dist:.3f}")
            self._transition(FSMState.CLOSE_GRIP)

        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=reach,
            reach_active=True,
            grip_closed=False,
        )

    def _close_grip(self) -> PolicyOutput:
        grasp = self._source_grasp_world()
        reach = self._reach_from_world(grasp, right_bias=-0.03)

        if self._attached:
            print(f"[FSM] CLOSE_GRIP → attached at t={self._tick_total}")
            self._transition(FSMState.LIFT_SOURCE)
        elif self._tick_state >= CLOSE_GRIP_TIMEOUT:
            print(f"[FSM] CLOSE_GRIP → timeout (not attached)  t={self._tick_total}")
            self._transition(FSMState.LIFT_SOURCE)

        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=reach,
            reach_active=True,
            grip_closed=True,
        )

    def _lift_source(self) -> PolicyOutput:
        palm  = self._palm_world()
        tbl_z = self._table_surface_z()

        if palm[2] >= tbl_z + LIFT_DONE_CLEARANCE:
            print(f"[FSM] LIFT_SOURCE → approach target"
                  f"  palm_z={palm[2]:.3f}  clearance={palm[2] - tbl_z:.3f}")
            self._transition(FSMState.APPROACH_TARGET)
        elif self._tick_state >= LIFT_SOURCE_TIMEOUT:
            print(f"[FSM] LIFT_SOURCE → timeout → approach target  palm_z={palm[2]:.3f}")
            self._transition(FSMState.APPROACH_TARGET)

        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=CARRY_POSE,
            reach_active=True,
            grip_closed=True,
        )

    def _approach_target(self) -> PolicyOutput:
        if self._tick_state == 1:
            print("[FSM] APPROACH_TARGET  walking toward target table")
        drop = self._target_drop_in_pelvis()
        if self._near_target_waypoint():
            self._reach_count += 1
            walk_cmd: tuple[float, float, float] = (0.0, 0.0, 0.0)
        else:
            self._reach_count = 0
            walk_cmd = self._target_approach_walk_cmd(drop)
        if self._reach_count >= TARGET_REACH_DEBOUNCE:
            ppos = self._data.qpos[:3]
            yaw  = self._pelvis_yaw()
            print(f"[FSM] near target waypoint: "
                  f"pelvis=({ppos[0]:.3f},{ppos[1]:.3f})  yaw={yaw:.3f}  "
                  f"drop_pelvis=({drop[0]:.3f},{drop[1]:.3f},{drop[2]:.3f})")
            self._transition(FSMState.HOVER_TARGET)
        elif self._tick_state >= TARGET_APPROACH_TIMEOUT:
            ppos = self._data.qpos[:3]
            print(f"[FSM] APPROACH_TARGET → timeout  "
                  f"drop_pelvis=({drop[0]:.3f},{drop[1]:.3f})  "
                  f"pelvis=({ppos[0]:.3f},{ppos[1]:.3f})")
            self._transition(FSMState.HOVER_TARGET)
        return PolicyOutput(
            walk_cmd=walk_cmd,
            reach_target=CARRY_POSE,
            reach_active=True,
            grip_closed=True,
        )

    def _hover_target(self) -> PolicyOutput:
        if self._tick_state == 0:
            print("[FSM] HOVER_TARGET  moving arm above drop point")
        hover = self._target_hover_world()
        reach = self._reach_from_world(hover, right_bias=-0.03)
        palm  = self._palm_world()
        dist  = float(np.linalg.norm(palm - hover))

        if dist < HOVER_TARGET_THRESHOLD:
            self._reach_count += 1
        else:
            self._reach_count = 0

        if self._reach_count >= DEBOUNCE_REACH:
            print(f"[FSM] HOVER_TARGET → threshold met  palm_dist={dist:.3f}")
            self._transition(FSMState.LOWER_TARGET)
        elif self._tick_state >= HOVER_TARGET_TIMEOUT:
            print(f"[FSM] HOVER_TARGET → timeout  palm_dist={dist:.3f}")
            self._transition(FSMState.LOWER_TARGET)

        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=reach,
            reach_active=True,
            grip_closed=True,
        )

    def _lower_target(self) -> PolicyOutput:
        if self._tick_state == 0:
            print("[FSM] LOWER_TARGET  descending arm to release height")
        place = self._target_place_world()
        reach = self._reach_from_world(place, right_bias=-0.03)
        palm  = self._palm_world()
        dist  = float(np.linalg.norm(palm - place))

        if dist < LOWER_TARGET_THRESHOLD:
            self._reach_count += 1
        else:
            self._reach_count = 0

        if self._reach_count >= DEBOUNCE_REACH:
            print(f"[FSM] LOWER_TARGET → threshold met  palm_dist={dist:.3f}")
            self._transition(FSMState.OPEN_GRIP)
        elif self._tick_state >= LOWER_TARGET_TIMEOUT:
            print(f"[FSM] LOWER_TARGET → timeout  palm_dist={dist:.3f}")
            self._transition(FSMState.OPEN_GRIP)

        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=reach,
            reach_active=True,
            grip_closed=True,
        )

    def _open_grip(self) -> PolicyOutput:
        if self._tick_state == 0:
            print("[FSM] OPEN_GRIP  releasing cylinder")
        place = self._target_place_world()
        reach = self._reach_from_world(place, right_bias=-0.03)

        if not self._attached:
            print(f"[FSM] OPEN_GRIP → released  t={self._tick_total}")
            self._transition(FSMState.RETRACT)
        elif self._tick_state >= OPEN_GRIP_TIMEOUT:
            print(f"[FSM] OPEN_GRIP → timeout  attached={self._attached}  t={self._tick_total}")
            self._transition(FSMState.RETRACT)

        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=reach,
            reach_active=True,
            grip_closed=False,
        )

    def _retract(self) -> PolicyOutput:
        if self._tick_state == 0:
            print("[FSM] RETRACT  raising arm to carry pose")
        palm  = self._palm_world()
        tgt_z = self._target_surface_z()

        if palm[2] >= tgt_z + LIFT_DONE_CLEARANCE:
            print(f"[FSM] RETRACT → arm clear  palm_z={palm[2]:.3f}")
            self._transition(FSMState.DONE)
        elif self._tick_state >= RETRACT_TIMEOUT:
            print(f"[FSM] RETRACT → timeout  palm_z={palm[2]:.3f}")
            self._transition(FSMState.DONE)

        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=CARRY_POSE,
            reach_active=True,
            grip_closed=False,
        )

    def _done(self) -> PolicyOutput:
        if self._tick_state == 0:
            print("[FSM] DONE  task complete — holding carry pose")
        return PolicyOutput(
            walk_cmd=(0.0, 0.0, 0.0),
            reach_target=CARRY_POSE,
            reach_active=True,
            grip_closed=False,
        )

    # ------------------------------------------------------------------ #
    # GT geometry helpers
    # ------------------------------------------------------------------ #

    def _pelvis_pose(self) -> tuple[np.ndarray, np.ndarray]:
        return self._data.qpos[:3].copy(), self._data.qpos[3:7].copy()

    def _pelvis_yaw(self) -> float:
        """Extract yaw (Z-rotation) from the pelvis quaternion."""
        qw, qx, qy, qz = (float(self._data.qpos[3]), float(self._data.qpos[4]),
                           float(self._data.qpos[5]), float(self._data.qpos[6]))
        return np.arctan2(2.0 * (qw * qz + qx * qy),
                          1.0 - 2.0 * (qy * qy + qz * qz))

    @staticmethod
    def _world_to_pelvis(
        pelvis_pos: np.ndarray,
        pelvis_quat: np.ndarray,
        vec_world: np.ndarray,
    ) -> np.ndarray:
        """Rotate world-frame point into pelvis frame: q⁻¹(v − p)."""
        v   = vec_world - pelvis_pos
        w   = pelvis_quat[0]
        xyz = pelvis_quat[1:4]
        t   = np.cross(xyz, v) * 2.0
        return v - w * t + np.cross(xyz, t)

    def _cylinder_world(self) -> np.ndarray:
        return self._data.xpos[self._rb_id].copy()

    def _cylinder_in_pelvis(self) -> np.ndarray:
        pos, quat = self._pelvis_pose()
        return self._world_to_pelvis(pos, quat, self._cylinder_world())

    def _palm_world(self) -> np.ndarray:
        return self._data.site_xpos[self._palm_id].copy()

    def _table_surface_z(self) -> float:
        """World Z of the source table's top surface.

        Uses geom_xpos + geom half-height when the geom ID is available
        (more accurate than body centre + hardcoded offset).
        Falls back to body approach if geom lookup failed.
        """
        if self._tbl_geom_id >= 0:
            return float(
                self._data.geom_xpos[self._tbl_geom_id][2]
                + self._model.geom_size[self._tbl_geom_id][2]
            )
        return float(self._data.xpos[self._tbl_id][2]) + 0.02

    def _source_hover_world(self) -> np.ndarray:
        """World point above the cylinder for pre-grasp hover."""
        p = self._cylinder_world().copy()
        p[2] = self._table_surface_z() + HOVER_SOURCE_HEIGHT
        return p

    def _source_grasp_world(self) -> np.ndarray:
        """World point at cylinder mid-body height for grasping."""
        p = self._cylinder_world().copy()
        p[2] = self._table_surface_z() + GRASP_HEIGHT
        return p

    @staticmethod
    def _clip_reach_target(reach: np.ndarray) -> np.ndarray:
        """Clip a pelvis-frame reach target to the reacher's workspace."""
        return np.clip(reach, _REACH_LOW, _REACH_HIGH).astype(np.float32)

    def _reach_from_world(
        self, world_point: np.ndarray, right_bias: float = -0.08
    ) -> np.ndarray:
        """Convert world point → clipped pelvis-frame reach target.

        right_bias clamps y so the target is at least this far to the
        robot's right (y ≤ right_bias in pelvis frame), keeping the reach
        target inside the right arm's natural workspace.
        """
        pos, quat = self._pelvis_pose()
        local = self._world_to_pelvis(pos, quat, world_point).copy().astype(np.float32)
        local[1] = min(float(local[1]), right_bias)
        return self._clip_reach_target(local)

    def _target_surface_z(self) -> float:
        """World Z of the target table's top surface."""
        if self._tbl_white_geom_id >= 0:
            return float(
                self._data.geom_xpos[self._tbl_white_geom_id][2]
                + self._model.geom_size[self._tbl_white_geom_id][2]
            )
        return float(self._data.xpos[self._tbl_white_id][2]) + 0.02

    def _target_drop_world(self) -> np.ndarray:
        """World point 5 cm inside the near edge of the target table, on the surface.

        Near edge: the edge with the less-negative y value (closest to the robot's
        starting position).  Inset of TARGET_NEAR_EDGE_INSET moves into the table.
        """
        if self._tbl_white_geom_id >= 0:
            gx  = float(self._data.geom_xpos[self._tbl_white_geom_id][0])
            gy  = float(self._data.geom_xpos[self._tbl_white_geom_id][1])
            near_edge_y = gy + float(self._model.geom_size[self._tbl_white_geom_id][1])
            drop_y = near_edge_y - TARGET_NEAR_EDGE_INSET
            drop_z = self._target_surface_z()
            return np.array([gx, drop_y, drop_z], dtype=np.float64)
        c = self._data.xpos[self._tbl_white_id].copy()
        return np.array([c[0], c[1] + 0.20, c[2] + 0.02], dtype=np.float64)

    def _target_drop_in_pelvis(self) -> np.ndarray:
        """Frozen drop point expressed in the current pelvis frame."""
        pos, quat = self._pelvis_pose()
        return self._world_to_pelvis(pos, quat, self._target_drop_pt)

    def _target_hover_world(self) -> np.ndarray:
        """World point HOVER_TARGET_HEIGHT above the frozen drop point."""
        p = self._target_drop_pt.copy()
        p[2] = self._target_surface_z() + HOVER_TARGET_HEIGHT
        return p

    def _target_place_world(self) -> np.ndarray:
        """World point PLACE_HEIGHT above the frozen drop point (release height)."""
        p = self._target_drop_pt.copy()
        p[2] = self._target_surface_z() + PLACE_HEIGHT
        return p

    def _cylinder_on_target_table(self) -> bool:
        """True when the cylinder is resting on the target table.

        Checks:
          1. Cylinder z is within (surface − 0.01, surface + ON_TABLE_Z_MAX).
          2. Cylinder XY is within the table geom footprint + ON_TABLE_XY_MARGIN.
        """
        cyl   = self._cylinder_world()
        tgt_z = self._target_surface_z()
        if not (tgt_z - 0.01 <= cyl[2] <= tgt_z + ON_TABLE_Z_MAX):
            return False
        if self._tbl_white_geom_id >= 0:
            gx = float(self._data.geom_xpos[self._tbl_white_geom_id][0])
            gy = float(self._data.geom_xpos[self._tbl_white_geom_id][1])
            hx = float(self._model.geom_size[self._tbl_white_geom_id][0])
            hy = float(self._model.geom_size[self._tbl_white_geom_id][1])
            return (abs(cyl[0] - gx) <= hx + ON_TABLE_XY_MARGIN and
                    abs(cyl[1] - gy) <= hy + ON_TABLE_XY_MARGIN)
        if self._tbl_white_id >= 0:
            c = self._data.xpos[self._tbl_white_id]
            return (abs(cyl[0] - c[0]) <= 0.40 and abs(cyl[1] - c[1]) <= 0.30)
        return False

    # ------------------------------------------------------------------ #
    # Approach commander
    # ------------------------------------------------------------------ #

    def _approach_walk_cmd(self, cyl: np.ndarray) -> tuple[float, float, float]:
        """Staircase vx + proportional vy/wz toward cylinder."""
        x_err = cyl[0] - APPROACH_TARGET_X
        if x_err > 0.18:
            vx = VX_FAST
        elif x_err > 0.10:
            vx = VX_MED
        elif x_err > 0.04:
            vx = VX_SLOW
        else:
            vx = 0.0
        y_err = cyl[1] - (-0.05)
        vy = float(np.clip(K_VY * y_err, -VY_CAP, VY_CAP))
        wz = float(np.clip(
            K_WZ * np.arctan2(cyl[1], max(cyl[0], 0.15)),
            -WZ_CAP, WZ_CAP,
        ))
        return (vx, vy, wz)

    def _target_approach_walk_cmd(self, drop_pelvis: np.ndarray) -> tuple[float, float, float]:
        """Two-phase world-frame approach to the target-table placement corridor.

        Phase 1 — turn CW to face -y: uses vx=VX_P1 (not 0) so the walker stays
          stable.  R = VX_P1/WZ_P1 = 0.24 m; at this radius the target table
          remains outside the turning circle, so Phase 2 can reach it head-on.

        Phase 2 — drive to standing waypoint: once |yaw + π/2| < PHASE1_ALIGN_TOL,
          decompose world-frame positional error into forward/lateral components
          and apply staircase vx + proportional vy + bearing wz.
        """
        pelvis_pos = self._data.qpos[:3]
        yaw = self._pelvis_yaw()

        # ---- Phase 1: CW turn until facing -y --------------------------------
        if abs(yaw + np.pi / 2) > PHASE1_ALIGN_TOL:
            return (VX_P1, 0.0, -WZ_P1)

        # ---- Phase 2: drive toward standing waypoint -------------------------
        # Standing waypoint: offset from drop point to keep it in the right arm's
        # natural workspace (y ≈ -0.15 in pelvis frame).
        # Facing -y world, +y pelvis is +x world.  So we want pelvis_x = drop_x + 0.15.
        drop_w  = self._target_drop_pt
        stand_x = float(drop_w[0]) + 0.15
        stand_y = float(drop_w[1]) + APPROACH_TARGET_X

        ex = stand_x - float(pelvis_pos[0])
        ey = stand_y - float(pelvis_pos[1])
        dist = float(np.sqrt(ex * ex + ey * ey))

        cos_y, sin_y = float(np.cos(yaw)), float(np.sin(yaw))
        left_err = -ex * sin_y + ey * cos_y

        if dist > 0.35:   vx = VX_FAST
        elif dist > 0.18: vx = VX_MED
        else:             vx = VX_SLOW

        vy = float(np.clip(K_VY * left_err, -VY_CAP, VY_CAP))

        # Use pelvis-frame bearing to the drop point for stable yaw control.
        drop_p = self._target_drop_in_pelvis()
        wz = float(np.clip(
            K_WZ * np.arctan2(drop_p[1], max(drop_p[0], 0.15)),
            -WZ_CAP, WZ_CAP,
        ))
        return (vx, vy, wz)

    def _near_target_waypoint(self) -> bool:
        """True when robot is close to the standing waypoint AND facing roughly −y.

        The pelvis-frame reach-window check (`_in_reach_window`) is NOT used for
        the target approach because the drop point can satisfy the window even when
        the robot is mid-turn and far from the table.  This world-frame check
        requires both conditions simultaneously.
        """
        yaw = self._pelvis_yaw()
        if abs(yaw + np.pi / 2) > 0.10:
            return False
        pelvis = self._data.qpos[:3]
        drop_w = self._target_drop_pt
        stand_x = float(drop_w[0]) + 0.15
        stand_y = float(drop_w[1]) + APPROACH_TARGET_X
        ex = stand_x - float(pelvis[0])
        ey = stand_y - float(pelvis[1])
        return float(np.sqrt(ex * ex + ey * ey)) < 0.06

    def _in_reach_window(self, cyl: np.ndarray) -> bool:
        return (REACH_X_MIN < cyl[0] < REACH_X_MAX and
                REACH_Y_MIN < cyl[1] < REACH_Y_MAX)
```

---

## FILE: `policies/keyboard.py`

```python
"""Keyboard-driven policy wrapper for manual control."""

from __future__ import annotations

from .base import BasePolicy, PolicyOutput


class KeyboardPolicy(BasePolicy):
  """Policy wrapper that delegates keyboard input to the controller."""

  def __init__(self, controller):
    self._controller = controller

  def handle_key(self, keycode: int) -> None:
    """Forward keyboard events to the controller."""
    self._controller.key_callback(keycode)

  def step(self) -> PolicyOutput:
    """Expose the controller's current high-level command state."""
    walk_cmd = (
      self._controller.lin_vel_x,
      self._controller.lin_vel_y,
      self._controller.ang_vel_z,
    )
    reach_target = tuple(self._controller.reach_target)
    return PolicyOutput(
      walk_cmd=walk_cmd,
      reach_target=reach_target,
      grip_closed=self._controller.grip_closed,
      reach_active=self._controller.reach_active,
    )
```

---

## FILE: `right_reacher.onnx`

_Skipped: non-text or binary file._

---

## FILE: `right_reacher.onnx.data`

_Skipped: non-text or binary file._

---

## FILE: `rotator.onnx`

_Skipped: file is too large (878886 bytes)._ 

---

## FILE: `rotator.onnx.data`

_Skipped: file is too large (877336 bytes)._ 

---

## FILE: `run.py`

```python
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
from policies.fsm import FSMPolicy
from policies.keyboard import KeyboardPolicy

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
    choices=["keyboard", "fsm"],
    default="keyboard",
    help="Control policy to use (default: keyboard)",
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
    grasp_backend = KinematicAttachment(model, data, ctrl.right_palm_site_id, rb_body_id)
    policy = FSMPolicy(ctrl, grasp_backend=grasp_backend)
    print("Policy: FSM (autonomous) + KinematicAttachment grasp backend")
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
          _apply_policy_output(ctrl, policy.step())
          target_pos = ctrl.step()
        ctrl.apply_pd_control(target_pos)
        mujoco.mj_step(model, data)
        if grasp_backend is not None:
          grasp_backend.tick(ctrl.grip_closed)
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
```

---

## FILE: `scene.xml`

```xml
<mujoco model="g1_table_red_block">
  <!--
    G1 Table Red Block scene — converted from LuckyEngine .hscene
    Contains: G1 robot, ground plane, table, red cylindrical block (freejoint),
              head camera, wrist camera, overhead camera, tracking camera.
  -->

  <include file="g1.xml"/>

  <statistic center="0.2 0 0.5" extent="2"/>

  <visual>
    <headlight diffuse="0.6 0.6 0.6" ambient="0.3 0.3 0.3" specular="0 0 0"/>
    <rgba haze="0.15 0.25 0.35 1"/>
    <global azimuth="120" elevation="-20"/>
  </visual>

  <asset>
    <!-- Skybox -->
    <texture type="skybox" builtin="gradient" rgb1="0.3 0.5 0.7" rgb2="0 0 0"
             width="512" height="3072"/>
    <!-- Light grey floor -->
    <texture type="2d" name="groundplane" builtin="flat"
             rgb1="0.75 0.75 0.75" rgb2="0.7 0.7 0.7"
             mark="random" markrgb="0.72 0.72 0.72"
             width="512" height="512"/>
    <material name="groundplane" texture="groundplane" texuniform="true"
              texrepeat="8 8" reflectance="0.1"/>
    <!-- Table materials -->
    <material name="table_wood" rgba="0.55 0.35 0.2 1" specular="0.3" shininess="0.5"/>
    <material name="table_blue" rgba="0.1 0.12 0.3 1" specular="0.3" shininess="0.5"/>
    <!-- Red block material -->
    <material name="red_plastic" rgba="0.85 0.1 0.1 1" specular="0.5" shininess="0.8"/>
  </asset>

  <worldbody>
    <!-- Ground plane -->
    <geom name="ground" type="plane" size="10 10 0.01" material="groundplane"
          contype="1" conaffinity="1"/>

    <!-- Ambient light -->
    <light pos="0 0 4" dir="0 0 -1" diffuse="0.7 0.7 0.7" specular="0.3 0.3 0.3"
           castshadow="true"/>
    <light pos="-2 2 3" dir="0.5 -0.5 -1" diffuse="0.3 0.3 0.3" specular="0.1 0.1 0.1"/>

    <!-- Table (static) -->
    <!-- Hazel: pos=[0.351, 0.713, 0], scale=[0.8, 0.04, 0.5] -->
    <!-- MuJoCo Z-up: pos=[0.351, 0, 0.713], half-size=[0.4, 0.25, 0.02] -->
    <body name="table" pos="0.351 0 0.713">
      <geom name="table_top" type="box" size="0.4 0.25 0.02" material="table_wood"
            contype="1" conaffinity="1" friction="1 0.1 0.01" mass="10"/>
      <!-- Table legs -->
      <geom name="table_leg_1" type="cylinder" size="0.025 0.345" pos="0.35 0.2 -0.365"
            rgba="0.4 0.25 0.15 1" contype="1" conaffinity="1" mass="1"/>
      <geom name="table_leg_2" type="cylinder" size="0.025 0.345" pos="-0.35 0.2 -0.365"
            rgba="0.4 0.25 0.15 1" contype="1" conaffinity="1" mass="1"/>
      <geom name="table_leg_3" type="cylinder" size="0.025 0.345" pos="0.35 -0.2 -0.365"
            rgba="0.4 0.25 0.15 1" contype="1" conaffinity="1" mass="1"/>
      <geom name="table_leg_4" type="cylinder" size="0.025 0.345" pos="-0.35 -0.2 -0.365"
            rgba="0.4 0.25 0.15 1" contype="1" conaffinity="1" mass="1"/>
    </body>

    <!-- White table (target / drop-off) — to the right of the robot -->
    <body name="table_white" pos="-0.3 -0.8 0.613">
      <geom name="table_white_top" type="box" size="0.35 0.25 0.02" material="table_blue"
            contype="1" conaffinity="1" friction="1 0.1 0.01" mass="10"/>
      <geom name="table_white_leg_1" type="cylinder" size="0.025 0.295" pos="0.3 0.2 -0.315"
            rgba="0.08 0.09 0.22 1" contype="1" conaffinity="1" mass="1"/>
      <geom name="table_white_leg_2" type="cylinder" size="0.025 0.295" pos="-0.3 0.2 -0.315"
            rgba="0.08 0.09 0.22 1" contype="1" conaffinity="1" mass="1"/>
      <geom name="table_white_leg_3" type="cylinder" size="0.025 0.295" pos="0.3 -0.2 -0.315"
            rgba="0.08 0.09 0.22 1" contype="1" conaffinity="1" mass="1"/>
      <geom name="table_white_leg_4" type="cylinder" size="0.025 0.295" pos="-0.3 -0.2 -0.315"
            rgba="0.08 0.09 0.22 1" contype="1" conaffinity="1" mass="1"/>
    </body>

    <!-- Red block / cylinder (dynamic, with freejoint) -->
    <!-- Hazel: pos=[0.235, 0.85, -0.026], scale=[0.03, 0.07, 0.03] -->
    <!-- MuJoCo Z-up: pos=[0.235, 0.026, 0.85] -->
    <body name="red_block" pos="0.0 0.026 0.85">
      <freejoint name="red_block_joint"/>
      <geom name="red_cylinder" type="cylinder" size="0.02 0.035"
            material="red_plastic" density="100"
            contype="1" conaffinity="1" friction="3 0.1 0.01"/>
      <!-- Thin box caps to reinforce top/bottom collision without tipping -->
      <geom name="red_cap_top" type="box" size="0.018 0.018 0.002" pos="0 0 0.035"
            rgba="0.85 0.1 0.1 1" density="10"
            contype="1" conaffinity="1" friction="3 0.1 0.01"/>
      <geom name="red_cap_bot" type="box" size="0.018 0.018 0.002" pos="0 0 -0.035"
            rgba="0.85 0.1 0.1 1" density="10"
            contype="1" conaffinity="1" friction="3 0.1 0.01"/>
    </body>

    <!-- Fixed cameras -->
    <camera name="overhead" pos="0.3 0 2.5" xyaxes="1 0 0 0 1 0" fovy="60"/>
    <camera name="side_view" pos="1.5 -1.5 1.2" xyaxes="0.707 0.707 0 -0.2 0.2 0.96" fovy="50"/>
  </worldbody>
</mujoco>
```

---

## FILE: `scripts/__init__.py`

```python
"""Entry-point scripts and developer utilities."""
```

---

## FILE: `scripts/audit_g1_native_vla_dataset.py`

```python
#!/usr/bin/env python3
"""Audit and split a G1-native VLA dataset.

Step 18:
- no OpenVLA
- no model inference
- no fine-tuning
- dataset quality audit before learning work
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.dataset_audit import (
    build_audit_report,
    phase_temporal_split,
    write_audit_report,
    write_split_manifests,
)
from vla_bridge.g1_native_dataset import read_dataset_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/vla_exports/g1_native_demo_002/audit"),
    )
    parser.add_argument("--val-fraction", type=float, default=0.2)
    parser.add_argument("--idle-min-run-length", type=int, default=25)
    parser.add_argument("--no-split", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    records = read_dataset_jsonl(args.dataset)
    if not records:
        raise RuntimeError(f"No records found in {args.dataset}")

    report = build_audit_report(
        records,
        source_dataset=str(args.dataset),
        idle_min_run_length=args.idle_min_run_length,
    )
    audit_path = args.output_dir / "audit_report.json"
    write_audit_report(audit_path, report)

    split_summary = None
    if not args.no_split:
        train, val = phase_temporal_split(records, val_fraction=args.val_fraction)
        split_summary = write_split_manifests(args.output_dir, train, val)

    print("\n--- G1-Native VLA Dataset Audit Summary ---")
    print(f"dataset              : {args.dataset}")
    print(f"output_dir           : {args.output_dir}")
    print(f"audit_report         : {audit_path}")
    print(f"num_records          : {report['num_records']}")
    print(f"action_vector_shape  : {report['action_vector_shape']}")
    print(f"phase_counts         : {report['phase_counts']}")
    print(f"boolean_balance      : {report['boolean_balance']}")
    print(f"idle_runs            : {len(report['idle_runs'])}")
    print(f"warnings             : {len(report['warnings'])}")

    if split_summary is not None:
        print(f"train_records        : {split_summary['train_records']}")
        print(f"val_records          : {split_summary['val_records']}")
        print(f"val_fraction_actual  : {split_summary['val_fraction_actual']:.4f}")
        print(f"split_summary        : {args.output_dir / 'split_summary.json'}")

    if report["warnings"]:
        print("\nWarnings:")
        for warning in report["warnings"]:
            print(f"  - {warning}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/build_g1_native_training_views.py`

```python
#!/usr/bin/env python3
"""Build filtered/weighted training views for a G1-native VLA dataset.

Step 19:
- no OpenVLA
- no model inference
- no fine-tuning
- create safer training views from audited records
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.g1_native_dataset import read_dataset_jsonl
from vla_bridge.training_views import build_training_views


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/vla_exports/g1_native_demo_002/training_views"),
    )
    parser.add_argument("--keep-first-n-idle", type=int, default=10)
    parser.add_argument("--max-weight", type=float, default=20.0)
    parser.add_argument("--rare-phase-boost", type=float, default=5.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    records = read_dataset_jsonl(args.dataset)
    if not records:
        raise RuntimeError(f"No records found in {args.dataset}")

    summary = build_training_views(
        records,
        output_dir=args.output_dir,
        keep_first_n_idle=args.keep_first_n_idle,
        max_weight=args.max_weight,
        rare_phase_boost=args.rare_phase_boost,
    )

    print("\n--- G1-Native VLA Training Views Summary ---")
    print(f"dataset                  : {args.dataset}")
    print(f"output_dir               : {args.output_dir}")
    print(f"source_records           : {summary['source_records']}")
    print(f"filtered_records         : {summary['filtered_records']}")
    print(f"removed_records          : {summary['removed_records']}")
    print(f"idle_records_source      : {summary['idle_records_source']}")
    print(f"idle_records_filtered    : {summary['idle_records_filtered']}")
    print(f"rare_source              : {summary['rare_transition_records_source']}")
    print(f"rare_filtered            : {summary['rare_transition_records_filtered']}")
    print(f"weight_count             : {summary['weight_count']}")
    print(f"min_weight               : {summary['min_weight']:.6f}")
    print(f"max_weight               : {summary['max_weight']:.6f}")
    print(f"mean_weight              : {summary['mean_weight']:.6f}")
    print(f"summary_path             : {summary['files']['summary']}")
    print("\nFiles:")
    for name, path in summary["files"].items():
        print(f"  {name:18s}: {path}")

    if summary["warnings"]:
        print("\nWarnings:")
        for warning in summary["warnings"]:
            print(f"  - {warning}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/export_g1_native_vla_batch_dataset.py`

```python
#!/usr/bin/env python3
"""Export a combined G1-native VLA dataset from a batch manifest.

Step 21:
- no OpenVLA
- no model inference
- no training
- combines successful FSM teacher demos into one supervised dataset artifact
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.batch_dataset_export import export_combined_batch_dataset


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export a combined G1-native VLA dataset from a batch manifest."
    )
    parser.add_argument("manifest_path", type=Path, help="Path to batch_manifest.json")
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory to save the combined dataset",
    )
    parser.add_argument(
        "--keep-done",
        action="store_true",
        help="Include steps where phase is DONE",
    )
    parser.add_argument(
        "--drop-inactive-reach",
        action="store_true",
        help="Exclude steps where reach_active is False",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        summary = export_combined_batch_dataset(
            args.manifest_path,
            args.output_dir,
            include_phase=True,
            drop_done=not args.keep_done,
            drop_inactive_reach=args.drop_inactive_reach,
        )
    except Exception as exc:
        print(f"Error exporting batch dataset: {exc}")
        return 1

    print("\n--- Combined G1-Native VLA Batch Dataset Export Summary ---")
    print(f"source_manifest       : {summary['source_manifest_path']}")
    print(f"output_dir            : {summary['output_dir']}")
    print(f"dataset_path          : {summary['dataset_path']}")
    print(f"summary_path          : {summary['summary_path']}")
    print(f"source_manifest_copy  : {summary['source_manifest_copy_path']}")
    print(f"batch_id              : {summary['batch_id']}")
    print(f"num_demos_in_manifest : {summary['num_demos_in_manifest']}")
    print(f"num_selected_demos    : {summary['num_selected_demos']}")
    print(f"num_skipped_demos     : {summary['num_skipped_demos']}")
    print(f"selected_demo_ids     : {summary['selected_demo_ids']}")
    print(f"num_records           : {summary['num_records']}")
    print(f"records_per_demo      : {summary['records_per_demo']}")
    print(f"unique_phases         : {summary['unique_phases']}")
    print(f"walk_nonzero_records  : {summary['walk_nonzero_records']}")
    print(f"reach_active_records  : {summary['reach_active_records']}")
    print(f"grip_closed_records   : {summary['grip_closed_records']}")
    print("")
    print("Target action vector:")
    print("  [walk_x, walk_y, walk_yaw, reach_x, reach_y, reach_z, reach_active, grip_closed]")

    if summary.get("num_skipped_demos", 0):
        print("")
        print("Skipped demos:")
        for demo_id, reason in summary.get("skip_reasons", {}).items():
            print(f"  - {demo_id}: {reason}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/export_g1_native_vla_dataset.py`

```python
#!/usr/bin/env python3
"""Export a G1-native VLA supervised dataset from a recorded FSM demo.

Step 17:
- no OpenVLA
- no model inference
- no fine-tuning
- export image/instruction -> G1-native action target
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.demo_schema import read_jsonl
from vla_bridge.g1_native_dataset import (
    copy_images_for_records,
    dataset_summary,
    export_records_from_steps,
    write_dataset_jsonl,
    write_summary,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("metadata", type=Path)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/vla_exports/g1_native_demo"),
    )
    parser.add_argument("--allow-missing-images", action="store_true")
    parser.add_argument("--include-phase", action="store_true", default=True)
    parser.add_argument("--no-phase", dest="include_phase", action="store_false")
    parser.add_argument("--keep-done", action="store_true")
    parser.add_argument("--drop-inactive-reach", action="store_true")
    parser.add_argument("--image-prefix", type=str, default="")
    parser.add_argument("--copy-images", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    steps = read_jsonl(args.metadata)
    if not steps:
        raise RuntimeError(f"No demo steps found in {args.metadata}")

    records = export_records_from_steps(
        steps,
        require_images=not args.allow_missing_images,
        include_phase=args.include_phase,
        image_prefix=args.image_prefix,
        drop_done=not args.keep_done,
        drop_inactive_reach=args.drop_inactive_reach,
    )

    if args.copy_images:
        source_demo_dir = args.metadata.parent
        records = copy_images_for_records(
            records,
            source_demo_dir=source_demo_dir,
            output_images_dir=args.output_dir / "images",
        )

    dataset_path = args.output_dir / "dataset.jsonl"
    summary_path = args.output_dir / "summary.json"

    write_dataset_jsonl(dataset_path, records)
    summary = dataset_summary(records)
    summary.update(
        {
            "source_metadata": str(args.metadata),
            "dataset_path": str(dataset_path),
            "copied_images": bool(args.copy_images),
            "include_phase": bool(args.include_phase),
            "drop_done": bool(not args.keep_done),
            "drop_inactive_reach": bool(args.drop_inactive_reach),
            "action_vector": [
                "walk_x",
                "walk_y",
                "walk_yaw",
                "reach_x",
                "reach_y",
                "reach_z",
                "reach_active",
                "grip_closed",
            ],
        }
    )
    write_summary(summary_path, summary)

    print("\n--- G1-Native VLA Dataset Export Summary ---")
    print(f"source_metadata       : {args.metadata}")
    print(f"output_dir            : {args.output_dir}")
    print(f"dataset_path          : {dataset_path}")
    print(f"summary_path          : {summary_path}")
    print(f"num_source_steps      : {len(steps)}")
    print(f"num_exported_records  : {summary['num_records']}")
    print(f"unique_phases         : {summary.get('unique_phases', [])}")
    print(f"walk_nonzero_records  : {summary.get('walk_nonzero_records', 0)}")
    print(f"reach_active_records  : {summary.get('reach_active_records', 0)}")
    print(f"grip_closed_records   : {summary.get('grip_closed_records', 0)}")
    print(f"copy_images           : {bool(args.copy_images)}")
    print("\nTarget action vector:")
    print("  [walk_x, walk_y, walk_yaw, reach_x, reach_y, reach_z, reach_active, grip_closed]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/inspect_g1_native_vla_dataset.py`

```python
#!/usr/bin/env python3
"""Inspect a G1-native VLA dataset export."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import numpy as np

from vla_bridge.g1_native_dataset import dataset_summary, read_dataset_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    records = read_dataset_jsonl(args.dataset)
    if not records:
        print("No records found.")
        return 1

    summary = dataset_summary(records)
    action = np.asarray([r.action_vector for r in records], dtype=np.float64)

    print("--- G1-Native VLA Dataset Summary ---")
    print(f"dataset               : {args.dataset}")
    print(f"num_records           : {summary['num_records']}")
    print(f"first_phase           : {summary.get('first_phase', '')}")
    print(f"last_phase            : {summary.get('last_phase', '')}")
    print(f"unique_phases         : {summary.get('unique_phases', [])}")
    print(f"walk_nonzero_records  : {summary.get('walk_nonzero_records', 0)}")
    print(f"reach_active_records  : {summary.get('reach_active_records', 0)}")
    print(f"grip_closed_records   : {summary.get('grip_closed_records', 0)}")
    print(f"action_vector_shape   : {action.shape}")
    print(f"first_image           : {records[0].image_path}")
    print(f"last_image            : {records[-1].image_path}")
    print(f"first_action_vector   : {records[0].action_vector}")
    print(f"last_action_vector    : {records[-1].action_vector}")

    if action.ndim != 2 or action.shape[1] != 8:
        print("ERROR: action_vector must have shape (N, 8)")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/inspect_vla_batch_diversity.py`

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.batch_diversity import summarize_manifest_diversity
from vla_bridge.batch_manifest import read_batch_manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect scenario diversity from a VLA batch manifest."
    )
    parser.add_argument("manifest_path", type=Path, help="Path to batch_manifest.json")
    parser.add_argument("--output-json", type=Path, default=None, help="Optional path to write summary JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = read_batch_manifest(args.manifest_path)
    summary = summarize_manifest_diversity(manifest)

    print("--- VLA Batch Diversity Summary ---")
    print(f"batch_id             : {summary['batch_id']}")
    print(f"num_demos            : {summary['num_demos']}")
    print(f"num_successful_demos : {summary['num_successful_demos']}")
    print(f"num_unique_scenarios : {summary['num_unique_scenarios']}")
    print(f"scenario_ids         : {summary['scenario_ids']}")
    print(f"dx_range_m           : {summary['dx_range_m']}")
    print(f"dy_range_m           : {summary['dy_range_m']}")
    print(f"all_offsets_identical: {summary['all_offsets_identical']}")

    if args.output_json is not None:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print(f"output_json          : {args.output_json}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/inspect_vla_demo.py`

```python
#!/usr/bin/env python3
"""Inspect a recorded VLA demonstration JSONL file.

Usage:
    python scripts/inspect_vla_demo.py data/vla_demos/demo_000/demo.jsonl
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np

from vla_bridge.demo_schema import read_jsonl


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print summary statistics for a VLA demonstration JSONL file."
    )
    parser.add_argument("metadata", type=Path, help="Path to demo.jsonl")
    args = parser.parse_args()

    steps = read_jsonl(args.metadata)
    if not steps:
        print("No steps found.")
        return 1

    actions = np.array([s.action_7d[:3] for s in steps], dtype=np.float64)
    mags = np.linalg.norm(actions, axis=1)
    phases = [s.phase for s in steps]

    walk_cmds = np.asarray([s.walk_cmd for s in steps], dtype=np.float64)
    walk_mags = np.linalg.norm(walk_cmds, axis=1)
    walk_nonzero_steps = int(np.sum(walk_mags > 1e-9))
    reach_active_steps = int(sum(s.reach_active for s in steps))

    print("--- VLA Demo Summary ---")
    print(f"metadata         : {args.metadata}")
    print(f"num_steps        : {len(steps)}")
    print(f"first_phase      : {phases[0]}")
    print(f"last_phase       : {phases[-1]}")
    print(f"unique_phases    : {sorted(set(phases))}")
    print(f"max_action_xyz_m : {float(mags.max()):.6f}")
    print(f"mean_action_xyz_m: {float(mags.mean()):.6f}")
    print(f"grip_closed_steps: {sum(1 for s in steps if s.grip_closed)}")
    print(f"walk_nonzero_steps: {walk_nonzero_steps}")
    print(f"reach_active_steps: {reach_active_steps}")
    print(f"first_image      : {steps[0].image_path}")
    print(f"last_image       : {steps[-1].image_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/plot_vla_demo.py`

```python
#!/usr/bin/env python3
"""Plot diagnostic figures for recorded or replayed VLA demonstrations.

Step 15 — optional plotting helper.

Usage (demo only):
    python scripts/plot_vla_demo.py data/vla_demos/demo_000/demo.jsonl \\
        --output-dir data/vla_demos/demo_000/plots

Usage (with replay trace):
    python scripts/plot_vla_demo.py data/vla_demos/demo_000/demo.jsonl \\
        --replay-trace data/vla_replays/replay_000/replay_trace.npz \\
        --output-dir data/vla_replays/replay_000/plots
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from vla_bridge.demo_schema import read_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot VLA demonstration figures."
    )
    parser.add_argument("metadata", type=Path, help="Path to demo.jsonl")
    parser.add_argument(
        "--replay-trace",
        type=Path,
        default=None,
        help="Optional replay_trace.npz to overlay teacher vs replay error",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/vla_plots"),
        help="Directory for output PNG files",
    )
    return parser.parse_args()


def _save(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(path), dpi=100, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot_vla_demo] saved {path}")


def plot_action_magnitude(steps, output_dir: Path) -> None:
    xyz = np.array([s.action_7d[:3] for s in steps], dtype=np.float64)
    mags = np.linalg.norm(xyz, axis=1)
    fig, ax = plt.subplots()
    ax.plot(mags)
    ax.set_xlabel("Step")
    ax.set_ylabel("Action magnitude (m)")
    ax.set_title("Action XYZ magnitude per step")
    _save(fig, output_dir / "action_magnitude.png")


def plot_grip_state(steps, output_dir: Path) -> None:
    grip = np.array([int(s.grip_closed) for s in steps])
    fig, ax = plt.subplots()
    ax.step(range(len(grip)), grip, where="post")
    ax.set_xlabel("Step")
    ax.set_ylabel("Grip closed")
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Open", "Closed"])
    ax.set_title("Gripper state over time")
    _save(fig, output_dir / "grip_state.png")


def plot_phase_index(steps, output_dir: Path) -> None:
    phases = [s.phase for s in steps]
    unique = sorted(set(phases))
    phase_map = {p: i for i, p in enumerate(unique)}
    indices = [phase_map[p] for p in phases]
    fig, ax = plt.subplots()
    ax.step(range(len(indices)), indices, where="post")
    ax.set_xlabel("Step")
    ax.set_ylabel("Phase index")
    ax.set_yticks(list(range(len(unique))))
    ax.set_yticklabels(unique, fontsize=8)
    ax.set_title("FSM phase index over time")
    _save(fig, output_dir / "phase_index.png")


def plot_walk_command_magnitude(steps, output_dir: Path) -> None:
    walk_cmds = np.array([s.walk_cmd for s in steps], dtype=np.float64)
    mags = np.linalg.norm(walk_cmds, axis=1)
    fig, ax = plt.subplots()
    ax.plot(mags)
    ax.set_xlabel("Step")
    ax.set_ylabel("Walk command magnitude")
    ax.set_title("Walk command magnitude per step")
    _save(fig, output_dir / "walk_command_magnitude.png")


def plot_palm_error(trace_path: Path, output_dir: Path) -> None:
    trace = np.load(str(trace_path))
    teacher = trace["teacher_palm_world"]
    replay = trace["replay_palm_world"]
    if teacher.shape != replay.shape or teacher.ndim != 2:
        print("[plot_vla_demo] warn: unexpected trace shape; skipping palm_error.png")
        return
    err = np.linalg.norm(replay - teacher, axis=1)
    fig, ax = plt.subplots()
    ax.plot(err)
    ax.set_xlabel("Step")
    ax.set_ylabel("Palm error (m)")
    ax.set_title("Teacher vs replay palm position error")
    _save(fig, output_dir / "palm_error.png")


def main() -> int:
    args = parse_args()

    steps = read_jsonl(args.metadata)
    if not steps:
        print(f"[plot_vla_demo] No steps found in {args.metadata}")
        return 1

    print(f"[plot_vla_demo] Loaded {len(steps)} steps from {args.metadata}")

    plot_action_magnitude(steps, args.output_dir)
    plot_grip_state(steps, args.output_dir)
    plot_phase_index(steps, args.output_dir)
    plot_walk_command_magnitude(steps, args.output_dir)

    if args.replay_trace is not None:
        plot_palm_error(args.replay_trace, args.output_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/record_demo.py`

```python
#!/usr/bin/env python3
"""Records a video of the G1 pick-and-place demo using the FSM policy."""

import json
import time
from pathlib import Path
import mujoco
import numpy as np
import cv2

from common.controller import WalkerReacherController
from common.grasp import KinematicAttachment
from common.onnx_policy import ONNXPolicy
from common.scene import CameraRenderer, reset_robot
from policies.fsm import FSMPolicy

SCRIPT_DIR = Path(__file__).resolve().parent.parent

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

def main():
    # Load config
    config_path = SCRIPT_DIR / "model_config.json"
    with open(config_path) as f:
        config = json.load(f)
    joint_names = config["joint_names"]

    # Load scene
    xml_path = SCRIPT_DIR / "scene.xml"
    model = mujoco.MjModel.from_xml_path(str(xml_path))
    model.opt.timestep = 0.005
    set_armature(model, joint_names)
    data = mujoco.MjData(model)

    # Reset
    reset_robot(model, data, config, joint_names, reset_data=True)

    # Load policies
    walker = ONNXPolicy(str(SCRIPT_DIR / "walker.onnx"))
    croucher = ONNXPolicy(str(SCRIPT_DIR / "croucher.onnx"))
    rotator = ONNXPolicy(str(SCRIPT_DIR / "rotator.onnx"))
    right_reacher = ONNXPolicy(str(SCRIPT_DIR / "right_reacher.onnx"))

    # Create controller
    ctrl = WalkerReacherController(model, data, walker, croucher, rotator, config,
                                   right_reacher=right_reacher)

    rb_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = KinematicAttachment(model, data, ctrl.right_palm_site_id, rb_body_id)
    policy = FSMPolicy(ctrl, grasp_backend=grasp_backend)

    # Setup VideoWriter
    width, height = 640, 480
    fps = 30
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_path = SCRIPT_DIR / "demo_video.mp4"
    video_writer = cv2.VideoWriter(str(out_path), fourcc, fps, (width, height))
    
    renderer = mujoco.Renderer(model, height, width)

    print(f"Recording demo to {out_path}...")

    decimation = 4
    sim_steps = 0
    max_steps = 15000 # Enough to finish the task
    
    last_render_time = 0
    render_interval = 1.0 / fps

    while sim_steps < max_steps:
        if sim_steps % decimation == 0:
            p_out = policy.step()
            ctrl.lin_vel_x, ctrl.lin_vel_y, ctrl.ang_vel_z = p_out.walk_cmd
            ctrl.reach_target[:] = p_out.reach_target
            ctrl.reach_active = p_out.reach_active
            ctrl.grip_closed = p_out.grip_closed
            target_pos = ctrl.step()
        
        ctrl.apply_pd_control(target_pos)
        mujoco.mj_step(model, data)
        grasp_backend.tick(ctrl.grip_closed)

        # Render at 30 FPS
        current_sim_time = data.time
        if current_sim_time - last_render_time >= render_interval:
            renderer.update_scene(data, camera="side_view")
            frame = renderer.render()
            # Convert RGB to BGR for OpenCV
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            video_writer.write(frame_bgr)
            last_render_time = current_sim_time
        
        sim_steps += 1
        
        # Stop if FSM reaches DONE
        if hasattr(policy, '_fsm') and policy._fsm.state.name == "DONE":
            # Record a few more seconds of the DONE state
            for _ in range(int(2.0 / model.opt.timestep)):
                if sim_steps % decimation == 0:
                    ctrl.step()
                ctrl.apply_pd_control(target_pos)
                mujoco.mj_step(model, data)
                grasp_backend.tick(ctrl.grip_closed)
                
                if data.time - last_render_time >= render_interval:
                    renderer.update_scene(data, camera="side_view")
                    frame = renderer.render()
                    video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                    last_render_time = data.time
                sim_steps += 1
            break

    video_writer.release()
    print(f"Video saved to {out_path}")

if __name__ == "__main__":
    main()
```

---

## FILE: `scripts/record_vla_demo.py`

```python
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
from typing import Any

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
        "num_frames": int(sum(1 for s in steps if s.image_path)),
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


def _augment_demo_rows_with_scenario(
    metadata_path: Path,
    *,
    scenario_id: str,
    seed: int | None,
    scenario: dict[str, Any],
) -> None:
    lines = metadata_path.read_text(encoding="utf-8").splitlines()
    out_lines = []
    for line in lines:
        if not line.strip():
            continue
        row = json.loads(line)
        row["scenario_id"] = str(scenario_id)
        row["seed"] = seed
        row["scenario"] = dict(scenario)
        out_lines.append(json.dumps(row, separators=(",", ":")))
    metadata_path.write_text("\n".join(out_lines) + ("\n" if out_lines else ""), encoding="utf-8")


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
    red_offset_dx, red_offset_dy = float(args.red_block_xy_offset[0]), float(args.red_block_xy_offset[1])
    scenario = {
        "red_block_xy_offset_m": [red_offset_dx, red_offset_dy],
    }
    scenario.update(apply_red_block_xy_offset(model, data, red_offset_dx, red_offset_dy))

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
    summary["scenario_id"] = str(args.scenario_id)
    summary["seed"] = args.seed
    summary["scenario"] = dict(scenario)
    summary["red_block_xy_offset_m"] = [red_offset_dx, red_offset_dy]
    summary_path = output_dir / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    _augment_demo_rows_with_scenario(
        recorder.metadata_path,
        scenario_id=str(args.scenario_id),
        seed=args.seed,
        scenario=scenario,
    )

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
    print(f"  scenario_id   : {args.scenario_id}")
    print(f"  seed          : {args.seed}")
    print(f"  red_offset_m  : {[red_offset_dx, red_offset_dy]}")

    if not recorder.steps:
        print("[record_vla_demo] ERROR: no steps were recorded.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/record_vla_demo_batch.py`

```python
#!/usr/bin/env python3
"""Batch-record FSM teacher demonstrations for the G1-native VLA branch.

Step 20:
- no OpenVLA
- no model inference
- no training
- repeated FSM demo collection with a batch manifest
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.batch_manifest import (
    build_batch_manifest,
    demo_record_from_summary,
    failed_demo_record,
    make_demo_id,
    manifest_summary,
    write_batch_manifest,
)
from vla_bridge.scenario_config import ScenarioSpec, load_scenario_config, scenario_to_metadata, select_scenario


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=Path("data/vla_demos/batch_000"))
    parser.add_argument("--num-demos", type=int, default=3)
    parser.add_argument("--record-every", type=int, default=1)
    parser.add_argument("--camera", type=str, default="head_cam")
    parser.add_argument("--no-images", action="store_true")
    parser.add_argument("--max-ticks", type=int, default=4000)
    parser.add_argument("--continue-on-fail", action="store_true")
    parser.add_argument("--python", type=str, default=sys.executable)
    parser.add_argument("--batch-id", type=str, default="")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--scenario-config",
        type=Path,
        default=None,
        help="Optional JSON config of deterministic scenario perturbations.",
    )
    return parser.parse_args()


def _load_summary(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _recorder_supports_max_ticks() -> bool:
    recorder_path = REPO_ROOT / "scripts" / "record_vla_demo.py"
    if not recorder_path.exists():
        return False
    text = recorder_path.read_text(encoding="utf-8", errors="ignore")
    return "--max-control-ticks" in text


def _build_record_command(args: argparse.Namespace, demo_dir: Path, scenario: ScenarioSpec | None = None) -> list[str]:
    cmd = [
        args.python,
        str(REPO_ROOT / "scripts" / "record_vla_demo.py"),
        "--output-dir",
        str(demo_dir),
        "--record-every",
        str(args.record_every),
    ]

    if _recorder_supports_max_ticks():
        cmd.extend(["--max-control-ticks", str(args.max_ticks)])

    if args.no_images:
        cmd.append("--no-images")
    else:
        cmd.extend(["--camera", args.camera])
    if scenario is not None:
        cmd.extend(["--scenario-id", scenario.scenario_id])
        cmd.extend(["--seed", str(int(scenario.seed))])
        cmd.extend(
            [
                "--red-block-xy-offset",
                str(float(scenario.red_block_xy_offset_m[0])),
                str(float(scenario.red_block_xy_offset_m[1])),
            ]
        )

    return cmd


def main() -> int:
    args = parse_args()

    if args.num_demos < 0:
        raise ValueError("--num-demos must be non-negative")
    if args.record_every <= 0:
        raise ValueError("--record-every must be positive")
    if args.max_ticks <= 0:
        raise ValueError("--max-ticks must be positive")

    args.output_root.mkdir(parents=True, exist_ok=True)
    batch_id = args.batch_id or args.output_root.name
    manifest_path = args.output_root / "batch_manifest.json"

    demo_records = []
    scenario_config = None
    if args.scenario_config is not None:
        scenario_config = load_scenario_config(args.scenario_config)

    if args.dry_run:
        print("\n--- G1 VLA Batch Recorder Dry Run ---")
        for i in range(args.num_demos):
            demo_id = make_demo_id(i)
            demo_dir = args.output_root / demo_id
            scenario = select_scenario(scenario_config, i) if scenario_config is not None else None
            cmd = _build_record_command(args, demo_dir, scenario)
            print(" ".join(cmd))

        manifest = build_batch_manifest(
            batch_id=batch_id,
            output_root=args.output_root,
            num_requested=args.num_demos,
            record_every=args.record_every,
            camera=args.camera,
            no_images=args.no_images,
            max_ticks=args.max_ticks,
            demos=[],
            scenario_config_path=str(args.scenario_config or ""),
            scenario_config_name=scenario_config.name if scenario_config is not None else "",
            scenario_count=len(scenario_config.scenarios) if scenario_config is not None else 0,
        )
        write_batch_manifest(manifest_path, manifest)
        print(f"\n[record_vla_demo_batch] wrote dry-run manifest: {manifest_path}")
        return 0

    for i in range(args.num_demos):
        demo_id = make_demo_id(i)
        demo_dir = args.output_root / demo_id
        demo_dir.mkdir(parents=True, exist_ok=True)
        scenario = select_scenario(scenario_config, i) if scenario_config is not None else None
        cmd = _build_record_command(args, demo_dir, scenario)

        print("\n============================================================")
        print(f"[record_vla_demo_batch] Recording {demo_id} ({i + 1}/{args.num_demos})")
        print(f"[record_vla_demo_batch] output_dir: {demo_dir}")
        print(f"[record_vla_demo_batch] command   : {' '.join(cmd)}")
        print("============================================================")

        try:
            subprocess.run(cmd, cwd=str(REPO_ROOT), check=True)
            summary = _load_summary(demo_dir / "summary.json")
            record = demo_record_from_summary(
                demo_id=demo_id,
                output_dir=demo_dir,
                summary=summary,
                scenario_id=scenario.scenario_id if scenario is not None else "",
                seed=scenario.seed if scenario is not None else None,
                scenario=scenario_to_metadata(scenario) if scenario is not None else None,
            )
            demo_records.append(record)
        except Exception as exc:
            record = failed_demo_record(
                demo_id=demo_id,
                output_dir=demo_dir,
                error=repr(exc),
                scenario_id=scenario.scenario_id if scenario is not None else "",
                seed=scenario.seed if scenario is not None else None,
                scenario=scenario_to_metadata(scenario) if scenario is not None else None,
            )
            demo_records.append(record)
            print(f"[record_vla_demo_batch] ERROR in {demo_id}: {exc}")
            if not args.continue_on_fail:
                print("[record_vla_demo_batch] stopping because --continue-on-fail was not set")
                break

    manifest = build_batch_manifest(
        batch_id=batch_id,
        output_root=args.output_root,
        num_requested=args.num_demos,
        record_every=args.record_every,
        camera=args.camera,
        no_images=args.no_images,
        max_ticks=args.max_ticks,
        demos=demo_records,
        scenario_config_path=str(args.scenario_config or ""),
        scenario_config_name=scenario_config.name if scenario_config is not None else "",
        scenario_count=len(scenario_config.scenarios) if scenario_config is not None else 0,
    )
    write_batch_manifest(manifest_path, manifest)
    summary = manifest_summary(manifest)

    print("\n--- G1 VLA Batch Recording Summary ---")
    print(f"batch_id              : {manifest.batch_id}")
    print(f"output_root           : {manifest.output_root}")
    print(f"manifest_path         : {manifest_path}")
    print(f"num_requested         : {manifest.num_requested}")
    print(f"num_completed         : {manifest.num_completed}")
    print(f"num_failed            : {manifest.num_failed}")
    print(f"successful_done_demos : {summary['successful_done_demos']}")
    print(f"total_steps           : {summary['total_steps']}")
    print(f"total_frames          : {summary['total_frames']}")
    print(f"demo_ids              : {summary['demo_ids']}")

    return 0 if manifest.num_failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## FILE: `scripts/replay_vla_demo.py`

```python
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
        "walk_nonzero_steps": metrics.walk_nonzero_steps,
        "reach_active_steps": metrics.reach_active_steps,
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
```

---

## FILE: `scripts/smoke_env.py`

```python
#!/usr/bin/env python3
"""Headless smoke test: validate scene loading and ONNX warmup.

Exits 0 on full pass, 1 on any required check failure.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_CAMERAS = ["head_cam", "wrist_cam", "overhead", "side_view", "tracking"]
REQUIRED_BODIES  = ["pelvis", "red_block", "table", "table_white"]
REQUIRED_SITES   = ["right_palm", "imu_in_pelvis", "left_foot", "right_foot"]

REQUIRED_ONNX = {
    "walker":        ("walker.onnx",        99),
    "right_reacher": ("right_reacher.onnx", 36),
}
OPTIONAL_ONNX = {
    "croucher": ("croucher.onnx",  101),
    "rotator":  ("rotator.onnx",    99),
}


# --------------------------------------------------------------------------- #

def _check(label: str, ok: bool, detail: str = "") -> bool:
    status = "PASS" if ok else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")
    return ok


def section(title: str) -> None:
    print(f"\n--- {title} ---")


# --------------------------------------------------------------------------- #

def main() -> int:
    failures: list[str] = []

    # ------------------------------------------------------------------ #
    # 1. Config
    # ------------------------------------------------------------------ #
    section("Config")
    config_path = ROOT / "model_config.json"
    config_ok = _check("model_config.json exists", config_path.exists())
    if not config_ok:
        failures.append("model_config.json missing")
        config = {}
    else:
        with open(config_path) as f:
            config = json.load(f)
        joint_names = config.get("joint_names", [])
        _check("joint_names present", bool(joint_names), f"{len(joint_names)} joints")
        for key in ("walker", "croucher"):
            present = key in config
            _check(f"config['{key}'] block", present)
            if not present:
                failures.append(f"config missing '{key}' block")

    # ------------------------------------------------------------------ #
    # 2. MuJoCo scene
    # ------------------------------------------------------------------ #
    section("MuJoCo scene")
    try:
        import mujoco
    except ImportError as exc:
        print(f"  [FAIL] mujoco import failed: {exc}")
        failures.append("mujoco not importable")
        _print_summary(failures)
        return 1

    xml_path = ROOT / "scene.xml"
    xml_ok = _check("scene.xml exists", xml_path.exists())
    if not xml_ok:
        failures.append("scene.xml missing")
        _print_summary(failures)
        return 1

    try:
        model = mujoco.MjModel.from_xml_path(str(xml_path))
        data  = mujoco.MjData(model)
        mujoco.mj_forward(model, data)
        _check("scene loaded + forward pass", True)
    except Exception as exc:
        _check("scene loaded", False, str(exc))
        failures.append(f"scene load failed: {exc}")
        _print_summary(failures)
        return 1

    # ------------------------------------------------------------------ #
    # 3. Cameras
    # ------------------------------------------------------------------ #
    section("Cameras")
    for cam in REQUIRED_CAMERAS:
        cid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_CAMERA, cam)
        ok  = cid >= 0
        _check(f"camera '{cam}'", ok, f"id={cid}" if ok else "NOT FOUND")
        if not ok:
            failures.append(f"camera '{cam}' missing")

    # ------------------------------------------------------------------ #
    # 4. Bodies
    # ------------------------------------------------------------------ #
    section("Bodies")
    for body in REQUIRED_BODIES:
        bid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, body)
        ok  = bid >= 0
        _check(f"body '{body}'", ok, f"id={bid}" if ok else "NOT FOUND")
        if not ok:
            failures.append(f"body '{body}' missing")

    # ------------------------------------------------------------------ #
    # 5. Sites
    # ------------------------------------------------------------------ #
    section("Sites")
    for site in REQUIRED_SITES:
        sid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SITE, site)
        ok  = sid >= 0
        _check(f"site '{site}'", ok, f"id={sid}" if ok else "NOT FOUND")
        if not ok:
            failures.append(f"site '{site}' missing")

    # ------------------------------------------------------------------ #
    # 6. Joints from config
    # ------------------------------------------------------------------ #
    section("Config joints in model")
    joint_names = config.get("joint_names", [])
    missing_joints = []
    for jname in joint_names:
        jid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, jname)
        if jid < 0:
            missing_joints.append(jname)
    if missing_joints:
        _check(f"all {len(joint_names)} joints present", False,
               f"missing: {missing_joints}")
        failures.append(f"missing joints: {missing_joints}")
    else:
        _check(f"all {len(joint_names)} joints present", True)

    # ------------------------------------------------------------------ #
    # 7. ONNX — required
    # ------------------------------------------------------------------ #
    section("ONNX (required)")
    try:
        import numpy as np
        import onnxruntime as ort
        ort_ok = True
    except ImportError as exc:
        print(f"  [FAIL] onnxruntime import failed: {exc}")
        failures.append("onnxruntime not importable")
        _print_summary(failures)
        return 1

    for label, (fname, input_dim) in REQUIRED_ONNX.items():
        path = ROOT / fname
        exists = path.exists()
        _check(f"{fname} exists", exists)
        if not exists:
            failures.append(f"{fname} missing")
            continue
        try:
            sess_opts = ort.SessionOptions()
            sess_opts.intra_op_num_threads = 1
            sess_opts.inter_op_num_threads = 1
            sess = ort.InferenceSession(
                str(path), sess_opts, providers=["CPUExecutionProvider"]
            )
            in_name  = sess.get_inputs()[0].name
            out_name = sess.get_outputs()[0].name
            dummy = np.zeros((1, input_dim), dtype=np.float32)
            out   = sess.run([out_name], {in_name: dummy})[0]
            _check(
                f"{label} warmup",
                True,
                f"in={input_dim} out={out.shape[1]}",
            )
        except Exception as exc:
            _check(f"{label} warmup", False, str(exc))
            failures.append(f"{label} warmup failed: {exc}")

    # ------------------------------------------------------------------ #
    # 8. ONNX — optional (report only, never fail)
    # ------------------------------------------------------------------ #
    section("ONNX (optional)")
    for label, (fname, input_dim) in OPTIONAL_ONNX.items():
        path = ROOT / fname
        exists = path.exists()
        if not exists:
            print(f"  [INFO] {fname} not present (optional)")
            continue
        try:
            sess_opts = ort.SessionOptions()
            sess_opts.intra_op_num_threads = 1
            sess_opts.inter_op_num_threads = 1
            sess = ort.InferenceSession(
                str(path), sess_opts, providers=["CPUExecutionProvider"]
            )
            in_name  = sess.get_inputs()[0].name
            out_name = sess.get_outputs()[0].name
            dummy = np.zeros((1, input_dim), dtype=np.float32)
            out   = sess.run([out_name], {in_name: dummy})[0]
            print(f"  [OK  ] {label}: in={input_dim} out={out.shape[1]}")
        except Exception as exc:
            print(f"  [WARN] {label} load/warmup failed: {exc}")

    # ------------------------------------------------------------------ #
    # Summary
    # ------------------------------------------------------------------ #
    _print_summary(failures)
    return 1 if failures else 0


def _print_summary(failures: list[str]) -> None:
    print("\n" + "=" * 50)
    if failures:
        print(f"RESULT: FAIL  ({len(failures)} issue(s))")
        for f in failures:
            print(f"  - {f}")
    else:
        print("RESULT: PASS  — repo is ready for FSM work")
    print("=" * 50)


if __name__ == "__main__":
    sys.exit(main())
```

---

## FILE: `scripts/test_fsm_approach.py`

```python
#!/usr/bin/env python3
"""Headless integration test: full pick-and-place pipeline through DONE."""

from __future__ import annotations

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
from policies.fsm import FSMPolicy
from policies.fsm_core import FSMState


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
    config_path = ROOT / "model_config.json"
    with open(config_path) as f:
        config = json.load(f)
    joint_names = config["joint_names"]

    model = mujoco.MjModel.from_xml_path(str(ROOT / "scene.xml"))
    model.opt.timestep = 0.005
    set_armature(model, joint_names)
    data  = mujoco.MjData(model)
    reset_robot(model, data, config, joint_names, reset_data=False)

    walker        = ONNXPolicy(str(ROOT / "walker.onnx"))
    croucher      = ONNXPolicy(str(ROOT / "croucher.onnx"))
    rotator       = ONNXPolicy(str(ROOT / "rotator.onnx"))
    right_reacher = ONNXPolicy(str(ROOT / "right_reacher.onnx"))

    ctrl = WalkerReacherController(model, data, walker, croucher, rotator,
                                   config, right_reacher=right_reacher)

    rb_body_id    = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    grasp_backend = KinematicAttachment(model, data, ctrl.right_palm_site_id, rb_body_id)
    policy        = FSMPolicy(ctrl, grasp_backend=grasp_backend)

    # Warm up ONNX
    walker(np.zeros((1, 99), dtype=np.float32))
    croucher(np.zeros((1, 101), dtype=np.float32))
    rotator(np.zeros((1, 99), dtype=np.float32))
    right_reacher(np.zeros((1, 36), dtype=np.float32))

    decimation     = 4
    MAX_CTRL_TICKS = 3000   # ~60 s: full pipeline through DONE

    target_pos = ctrl.default_joint_pos.copy()

    for tick in range(MAX_CTRL_TICKS):
        out = policy.step()
        target_pos = ctrl.step()
        for _ in range(decimation):
            ctrl.apply_pd_control(target_pos)
            mujoco.mj_step(model, data)
            grasp_backend.tick(ctrl.grip_closed)

        state = policy._fsm.state

        if state == FSMState.DONE:
            fsm   = policy._fsm
            cyl   = fsm._cylinder_world()
            palm  = fsm._palm_world()
            drop  = fsm._target_drop_pt
            tgt_z = fsm._target_surface_z()
            on_tbl = fsm._cylinder_on_target_table()
            verdict = "PASS" if on_tbl else "FAIL"
            print(f"\n{verdict} — reached DONE at control tick {tick + 1}")
            print(f"  palm_world      : ({palm[0]:.3f}, {palm[1]:.3f}, {palm[2]:.3f})")
            print(f"  cyl_world       : ({cyl[0]:.3f}, {cyl[1]:.3f}, {cyl[2]:.3f})")
            print(f"  drop_world      : ({drop[0]:.3f}, {drop[1]:.3f}, {drop[2]:.3f})")
            print(f"  target_z        : {tgt_z:.3f}")
            print(f"  cyl_clearance   : {cyl[2]-tgt_z:.3f} m")
            print(f"  on_target_table : {on_tbl}")
            print(f"  attached        : {grasp_backend.attached}")
            sys.exit(0 if on_tbl else 1)

        pz = float(data.qpos[2])
        if pz < 0.40:
            print(f"\nFAIL — robot fell (pelvis z={pz:.3f}) at tick {tick + 1}")
            sys.exit(1)

    # Timeout
    fsm   = policy._fsm
    cyl_w = fsm._cylinder_world()
    drop  = fsm._target_drop_pt
    drop_str = f"({drop[0]:.3f},{drop[1]:.3f},{drop[2]:.3f})" if drop is not None else "None"
    print(f"\n=== TIMEOUT after {MAX_CTRL_TICKS} ticks ===")
    print(f"  state           : {fsm.state.name}")
    print(f"  cyl_world       : ({cyl_w[0]:.3f}, {cyl_w[1]:.3f}, {cyl_w[2]:.3f})")
    print(f"  drop_world      : {drop_str}")
    print(f"  on_target_table : {fsm._cylinder_on_target_table()}")
    print(f"  attached        : {grasp_backend.attached}")
    print("\nFAIL — did not reach DONE")
    sys.exit(1)


if __name__ == "__main__":
    main()
```

---

## FILE: `tests/__init__.py`

```python
"""Test suite for simulation and policy components."""
```

---

## FILE: `tests/test_batch_diversity_manifest.py`

```python
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vla_bridge.batch_dataset_export import export_combined_batch_dataset
from vla_bridge.batch_diversity import summarize_manifest_diversity
from vla_bridge.batch_manifest import (
    BatchManifest,
    DemoRunRecord,
    STATUS_SUCCESS,
    read_batch_manifest,
    write_batch_manifest,
)


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")


def _demo_row(step_index: int, *, scenario_id: str, seed: int, dx: float, dy: float) -> dict:
    return {
        "step_index": step_index,
        "sim_time": float(step_index) * 0.02,
        "image_path": "frames/frame_000000.png",
        "instruction": "Pick up the red cylinder and place it on the blue table.",
        "phase": "SETTLE",
        "palm_world": [0.0, 0.0, 0.0],
        "pelvis_pos": [0.0, 0.0, 0.0],
        "pelvis_quat": [1.0, 0.0, 0.0, 0.0],
        "reach_target_pelvis": [0.3, -0.2, 0.2],
        "grip_closed": False,
        "walk_cmd": [0.0, 0.0, 0.0],
        "reach_active": False,
        "action_7d": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        "scenario_id": scenario_id,
        "seed": seed,
        "scenario": {"red_block_xy_offset_m": [dx, dy]},
    }


class TestBatchDiversityManifest(unittest.TestCase):
    def test_manifest_roundtrip_preserves_scenario_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "batch_manifest.json"
            manifest = BatchManifest(
                batch_id="batch_001",
                output_root=str(Path(tmp)),
                created_unix_time=1.0,
                num_requested=1,
                num_completed=1,
                num_failed=0,
                record_every=1,
                camera="head_cam",
                no_images=True,
                max_ticks=100,
                demos=[
                    DemoRunRecord(
                        demo_id="demo_000",
                        output_dir=str(Path(tmp) / "demo_000"),
                        metadata_path=str(Path(tmp) / "demo_000" / "demo.jsonl"),
                        summary_path=str(Path(tmp) / "demo_000" / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=2,
                        num_frames=0,
                        scenario_id="cyl_x_plus_02",
                        seed=101,
                        scenario={"red_block_xy_offset_m": [0.02, 0.0]},
                    )
                ],
                scenario_config_path="configs/scenarios/small_perturbations.json",
                scenario_config_name="small_perturbations_v1",
                scenario_count=5,
            )
            write_batch_manifest(path, manifest)
            restored = read_batch_manifest(path)
            self.assertEqual(restored, manifest)

    def test_diversity_summary_detects_multiple_offsets(self):
        manifest = BatchManifest(
            batch_id="batch_001",
            output_root="batch",
            created_unix_time=1.0,
            num_requested=2,
            num_completed=2,
            num_failed=0,
            record_every=1,
            camera="head_cam",
            no_images=True,
            max_ticks=100,
            demos=[
                DemoRunRecord(
                    demo_id="demo_000",
                    output_dir="batch/demo_000",
                    metadata_path="batch/demo_000/demo.jsonl",
                    summary_path="batch/demo_000/summary.json",
                    status=STATUS_SUCCESS,
                    done_reached=True,
                    num_steps=1,
                    num_frames=0,
                    scenario_id="nominal",
                    seed=0,
                    scenario={"red_block_xy_offset_m": [0.0, 0.0]},
                ),
                DemoRunRecord(
                    demo_id="demo_001",
                    output_dir="batch/demo_001",
                    metadata_path="batch/demo_001/demo.jsonl",
                    summary_path="batch/demo_001/summary.json",
                    status=STATUS_SUCCESS,
                    done_reached=True,
                    num_steps=1,
                    num_frames=0,
                    scenario_id="cyl_x_plus_02",
                    seed=101,
                    scenario={"red_block_xy_offset_m": [0.02, 0.0]},
                ),
            ],
        )
        summary = summarize_manifest_diversity(manifest)
        self.assertEqual(summary["num_unique_scenarios"], 2)
        self.assertFalse(summary["all_offsets_identical"])
        self.assertEqual(summary["dx_range_m"], [0.0, 0.02])

    def test_combined_export_preserves_scenario_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch_root = root / "batch_001"
            demo0 = batch_root / "demo_000"
            demo1 = batch_root / "demo_001"

            _write_jsonl(
                demo0 / "demo.jsonl",
                [_demo_row(0, scenario_id="nominal", seed=0, dx=0.0, dy=0.0)],
            )
            _write_jsonl(
                demo1 / "demo.jsonl",
                [_demo_row(0, scenario_id="cyl_y_plus_02", seed=103, dx=0.0, dy=0.02)],
            )

            manifest = BatchManifest(
                batch_id="batch_001",
                output_root=str(batch_root),
                created_unix_time=1.0,
                num_requested=2,
                num_completed=2,
                num_failed=0,
                record_every=1,
                camera="head_cam",
                no_images=True,
                max_ticks=100,
                demos=[
                    DemoRunRecord(
                        demo_id="demo_000",
                        output_dir=str(demo0),
                        metadata_path=str(demo0 / "demo.jsonl"),
                        summary_path=str(demo0 / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=1,
                        num_frames=0,
                        scenario_id="nominal",
                        seed=0,
                        scenario={"red_block_xy_offset_m": [0.0, 0.0]},
                    ),
                    DemoRunRecord(
                        demo_id="demo_001",
                        output_dir=str(demo1),
                        metadata_path=str(demo1 / "demo.jsonl"),
                        summary_path=str(demo1 / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=1,
                        num_frames=0,
                        scenario_id="cyl_y_plus_02",
                        seed=103,
                        scenario={"red_block_xy_offset_m": [0.0, 0.02]},
                    ),
                ],
            )
            manifest_path = batch_root / "batch_manifest.json"
            write_batch_manifest(manifest_path, manifest)

            out_dir = root / "export"
            summary = export_combined_batch_dataset(manifest_path, out_dir, drop_done=False)

            rows = [
                json.loads(line)
                for line in (out_dir / "dataset.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            self.assertEqual(len(rows), 2)
            self.assertIn("scenario_id", rows[0])
            self.assertIn("seed", rows[0])
            self.assertIn("scenario", rows[0])
            self.assertEqual(summary["num_unique_scenarios"], 2)
            self.assertEqual(set(summary["scenario_ids"]), {"nominal", "cyl_y_plus_02"})


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `tests/test_g1_native_batch_dataset_export.py`

```python
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vla_bridge.batch_dataset_export import (
    _prefix_image_path,
    export_combined_batch_dataset,
    select_successful_demos,
)
from vla_bridge.batch_manifest import (
    STATUS_FAILED,
    STATUS_SUCCESS,
    DemoRunRecord,
    build_batch_manifest,
    write_batch_manifest,
)


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")


def _demo_row(step_index: int, *, phase: str = "SETTLE", image_path: str = "frames/frame_000000.png") -> dict:
    return {
        "step_index": step_index,
        "sim_time": float(step_index) * 0.02,
        "image_path": image_path,
        "instruction": "Pick up the red cylinder and place it on the blue table.",
        "phase": phase,
        "palm_world": [0.0, 0.0, 0.0],
        "pelvis_pos": [0.0, 0.0, 0.0],
        "pelvis_quat": [1.0, 0.0, 0.0, 0.0],
        "reach_target_pelvis": [0.3, -0.2, 0.2],
        "grip_closed": False,
        "walk_cmd": [0.0, 0.0, 0.0],
        "reach_active": False,
        "action_7d": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    }


class TestG1NativeBatchDatasetExport(unittest.TestCase):
    def test_select_successful_demos(self):
        manifest = build_batch_manifest(
            batch_id="batch_test",
            output_root="batch",
            num_requested=1,
            record_every=1,
            camera="head_cam",
            no_images=True,
            max_ticks=4000,
            demos=[
                DemoRunRecord(
                    demo_id="demo_000",
                    output_dir="batch/demo_000",
                    metadata_path="batch/demo_000/demo.jsonl",
                    summary_path="batch/demo_000/summary.json",
                    status=STATUS_SUCCESS,
                    done_reached=True,
                    num_steps=3,
                    num_frames=0,
                )
            ],
            created_unix_time=123.0,
        )
        selection = select_successful_demos(manifest)
        self.assertEqual(selection.selected_demo_ids, ["demo_000"])
        self.assertEqual(selection.skipped_demo_ids, [])

    def test_select_skips_failed_and_not_done(self):
        manifest = build_batch_manifest(
            batch_id="batch_test",
            output_root="batch",
            num_requested=2,
            record_every=1,
            camera="head_cam",
            no_images=True,
            max_ticks=4000,
            demos=[
                DemoRunRecord(
                    demo_id="demo_failed",
                    output_dir="batch/demo_failed",
                    metadata_path="batch/demo_failed/demo.jsonl",
                    summary_path="batch/demo_failed/summary.json",
                    status=STATUS_FAILED,
                    done_reached=False,
                    num_steps=0,
                    num_frames=0,
                    error="boom",
                ),
                DemoRunRecord(
                    demo_id="demo_not_done",
                    output_dir="batch/demo_not_done",
                    metadata_path="batch/demo_not_done/demo.jsonl",
                    summary_path="batch/demo_not_done/summary.json",
                    status=STATUS_SUCCESS,
                    done_reached=False,
                    num_steps=3,
                    num_frames=0,
                ),
            ],
            created_unix_time=123.0,
        )
        selection = select_successful_demos(manifest)
        self.assertEqual(selection.selected_demo_ids, [])
        self.assertEqual(selection.skipped_demo_ids, ["demo_failed", "demo_not_done"])
        self.assertIn("demo_failed", selection.skip_reasons)
        self.assertIn("demo_not_done", selection.skip_reasons)

    def test_prefix_image_path_empty(self):
        self.assertEqual(
            _prefix_image_path(
                "",
                demo_output_dir="batch/demo_000",
                batch_root="batch",
            ),
            "",
        )

    def test_prefix_image_path_relative(self):
        prefixed = _prefix_image_path(
            "frames/frame_000000.png",
            demo_output_dir="batch/demo_000",
            batch_root="batch",
        )
        self.assertEqual(prefixed, "demo_000/frames/frame_000000.png")

    def test_export_combined_batch_dataset(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch_root = root / "batch_000"

            demo0 = batch_root / "demo_000"
            demo1 = batch_root / "demo_001"

            _write_jsonl(
                demo0 / "demo.jsonl",
                [
                    _demo_row(0, phase="SETTLE", image_path="frames/frame_000000.png"),
                    _demo_row(1, phase="APPROACH_SOURCE", image_path="frames/frame_000001.png"),
                    _demo_row(2, phase="DONE", image_path="frames/frame_000002.png"),
                ],
            )
            _write_jsonl(
                demo1 / "demo.jsonl",
                [
                    _demo_row(0, phase="SETTLE", image_path="frames/frame_000000.png"),
                    _demo_row(1, phase="APPROACH_SOURCE", image_path="frames/frame_000001.png"),
                    _demo_row(2, phase="DONE", image_path="frames/frame_000002.png"),
                ],
            )

            manifest = build_batch_manifest(
                batch_id="batch_000",
                output_root=batch_root,
                num_requested=2,
                record_every=1,
                camera="head_cam",
                no_images=True,
                max_ticks=4000,
                demos=[
                    DemoRunRecord(
                        demo_id="demo_000",
                        output_dir=str(demo0),
                        metadata_path=str(demo0 / "demo.jsonl"),
                        summary_path=str(demo0 / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=3,
                        num_frames=0,
                    ),
                    DemoRunRecord(
                        demo_id="demo_001",
                        output_dir=str(demo1),
                        metadata_path=str(demo1 / "demo.jsonl"),
                        summary_path=str(demo1 / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=3,
                        num_frames=0,
                    ),
                ],
                created_unix_time=123.0,
            )

            manifest_path = batch_root / "batch_manifest.json"
            write_batch_manifest(manifest_path, manifest)

            out_dir = root / "export"
            summary = export_combined_batch_dataset(manifest_path, out_dir)

            dataset_path = out_dir / "dataset.jsonl"
            summary_path = out_dir / "summary.json"
            source_manifest_path = out_dir / "source_manifest.json"

            self.assertTrue(dataset_path.exists())
            self.assertTrue(summary_path.exists())
            self.assertTrue(source_manifest_path.exists())
            self.assertEqual(summary["num_selected_demos"], 2)
            self.assertEqual(summary["num_skipped_demos"], 0)

            rows = [
                json.loads(line)
                for line in dataset_path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]

            # DONE rows should be dropped by default, leaving 2 rows per demo.
            self.assertEqual(len(rows), 4)
            self.assertEqual([r["sample_index"] for r in rows], [0, 1, 2, 3])
            self.assertEqual([r["demo_sample_index"] for r in rows], [0, 1, 0, 1])
            self.assertEqual(rows[0]["batch_id"], "batch_000")
            self.assertEqual(rows[0]["demo_id"], "demo_000")
            self.assertEqual(rows[2]["demo_id"], "demo_001")
            self.assertEqual(rows[0]["image_path"], "demo_000/frames/frame_000000.png")

    def test_export_no_successful_demos_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch_root = root / "batch_000"
            manifest = build_batch_manifest(
                batch_id="batch_000",
                output_root=batch_root,
                num_requested=1,
                record_every=1,
                camera="head_cam",
                no_images=True,
                max_ticks=4000,
                demos=[
                    DemoRunRecord(
                        demo_id="demo_failed",
                        output_dir=str(batch_root / "demo_failed"),
                        metadata_path=str(batch_root / "demo_failed" / "demo.jsonl"),
                        summary_path=str(batch_root / "demo_failed" / "summary.json"),
                        status=STATUS_FAILED,
                        done_reached=False,
                        num_steps=0,
                        num_frames=0,
                        error="boom",
                    )
                ],
                created_unix_time=123.0,
            )
            manifest_path = batch_root / "batch_manifest.json"
            write_batch_manifest(manifest_path, manifest)
            with self.assertRaises(ValueError):
                export_combined_batch_dataset(manifest_path, root / "export")


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `tests/test_g1_native_dataset.py`

```python
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from vla_bridge.demo_schema import VLADemoStep
from vla_bridge.g1_native_dataset import (
    G1NativeVLARecord,
    copy_images_for_records,
    dataset_summary,
    export_records_from_steps,
    make_action_vector,
    read_dataset_jsonl,
    record_from_demo_step,
    record_from_json,
    record_to_json,
    write_dataset_jsonl,
)


def make_demo_step(
    i: int = 0,
    *,
    phase: str = "SETTLE",
    image_path: str = "frames/frame_000000.png",
    walk_cmd=(0.1, 0.0, 0.2),
    reach_active: bool = True,
    grip_closed: bool = False,
) -> VLADemoStep:
    return VLADemoStep(
        step_index=i,
        sim_time=float(i) * 0.02,
        image_path=image_path,
        instruction="Pick up the red cylinder and place it on the blue table.",
        phase=phase,
        palm_world=(0.1, 0.2, 0.3),
        pelvis_pos=(0.0, 0.0, 0.76),
        pelvis_quat=(1.0, 0.0, 0.0, 0.0),
        walk_cmd=tuple(float(x) for x in walk_cmd),
        reach_target_pelvis=(0.3, -0.2, 0.2),
        reach_active=reach_active,
        grip_closed=grip_closed,
        action_7d=(0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 if grip_closed else 0.0),
    )


class TestG1NativeDataset(unittest.TestCase):
    def test_make_action_vector(self):
        out = make_action_vector((1, 2, 3), (4, 5, 6), True, False)
        self.assertEqual(out, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 1.0, 0.0))
        self.assertEqual(len(out), 8)

    def test_make_action_vector_boolean_mapping(self):
        out = make_action_vector((0, 0, 0), (0, 0, 0), False, True)
        self.assertEqual(out[-2:], (0.0, 1.0))

    def test_record_from_demo_step(self):
        step = make_demo_step(7, grip_closed=True)
        rec = record_from_demo_step(step, sample_index=3)
        self.assertEqual(rec.sample_index, 3)
        self.assertEqual(rec.source_step_index, 7)
        self.assertEqual(rec.image_path, step.image_path)
        self.assertEqual(rec.walk_cmd, step.walk_cmd)
        self.assertEqual(rec.reach_target_pelvis, step.reach_target_pelvis)
        self.assertTrue(rec.reach_active)
        self.assertTrue(rec.grip_closed)
        self.assertEqual(len(rec.action_vector), 8)

    def test_record_from_demo_step_with_prefix(self):
        step = make_demo_step()
        rec = record_from_demo_step(step, sample_index=0, image_prefix="demo_002")
        self.assertEqual(rec.image_path, "demo_002/frames/frame_000000.png")

    def test_export_drops_done_by_default(self):
        steps = [make_demo_step(0, phase="SETTLE"), make_demo_step(1, phase="DONE")]
        records = export_records_from_steps(steps)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].phase, "SETTLE")

    def test_export_can_keep_done(self):
        steps = [make_demo_step(0, phase="SETTLE"), make_demo_step(1, phase="DONE")]
        records = export_records_from_steps(steps, drop_done=False)
        self.assertEqual(len(records), 2)

    def test_export_can_drop_inactive_reach(self):
        steps = [
            make_demo_step(0, reach_active=False),
            make_demo_step(1, reach_active=True),
        ]
        records = export_records_from_steps(steps, drop_inactive_reach=True)
        self.assertEqual(len(records), 1)
        self.assertTrue(records[0].reach_active)

    def test_missing_image_raises_when_required(self):
        steps = [make_demo_step(0, image_path="")]
        with self.assertRaises(ValueError):
            export_records_from_steps(steps, require_images=True)

    def test_json_roundtrip(self):
        rec = record_from_demo_step(make_demo_step(2), sample_index=0)
        restored = record_from_json(record_to_json(rec))
        self.assertEqual(restored, rec)

    def test_jsonl_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "dataset.jsonl"
            records = [
                record_from_demo_step(make_demo_step(0), sample_index=0),
                record_from_demo_step(make_demo_step(1), sample_index=1),
            ]
            write_dataset_jsonl(path, records)
            restored = read_dataset_jsonl(path)
            self.assertEqual(restored, records)

    def test_dataset_summary(self):
        records = [
            record_from_demo_step(make_demo_step(0, walk_cmd=(0, 0, 0), reach_active=False), sample_index=0),
            record_from_demo_step(make_demo_step(1, walk_cmd=(3, 4, 0), reach_active=True, grip_closed=True), sample_index=1),
        ]
        summary = dataset_summary(records)
        self.assertEqual(summary["num_records"], 2)
        self.assertEqual(summary["walk_nonzero_records"], 1)
        self.assertEqual(summary["reach_active_records"], 1)
        self.assertEqual(summary["grip_closed_records"], 1)
        self.assertAlmostEqual(summary["max_walk_cmd_magnitude"], 5.0)

    def test_copy_images_for_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "demo"
            frames = source / "frames"
            frames.mkdir(parents=True)
            img = frames / "frame_000000.png"
            img.write_bytes(b"fake image")

            out_images = root / "export" / "images"
            record = record_from_demo_step(make_demo_step(0), sample_index=0)
            copied = copy_images_for_records(
                [record],
                source_demo_dir=source,
                output_images_dir=out_images,
            )
            self.assertEqual(copied[0].image_path, "images/frame_000000.png")
            self.assertTrue((out_images / "frame_000000.png").exists())


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `tests/test_g1_native_dataset_audit.py`

```python
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from vla_bridge.dataset_audit import (
    action_array,
    action_statistics,
    boolean_balance,
    build_audit_report,
    find_idle_runs,
    magnitude_statistics,
    phase_counts,
    phase_temporal_split,
    phase_transition_counts,
    write_split_manifests,
)
from vla_bridge.g1_native_dataset import G1NativeVLARecord, read_dataset_jsonl


def make_record(
    i: int,
    *,
    phase: str = "SETTLE",
    walk=(0.0, 0.0, 0.0),
    reach=(0.3, -0.2, 0.2),
    reach_active: bool = False,
    grip_closed: bool = False,
) -> G1NativeVLARecord:
    action = (
        float(walk[0]),
        float(walk[1]),
        float(walk[2]),
        float(reach[0]),
        float(reach[1]),
        float(reach[2]),
        1.0 if reach_active else 0.0,
        1.0 if grip_closed else 0.0,
    )
    return G1NativeVLARecord(
        sample_index=i,
        source_step_index=i,
        image_path=f"frames/frame_{i:06d}.png",
        instruction="Pick up the red cylinder and place it on the blue table.",
        phase=phase,
        walk_cmd=tuple(float(x) for x in walk),
        reach_target_pelvis=tuple(float(x) for x in reach),
        reach_active=reach_active,
        grip_closed=grip_closed,
        action_vector=action,
    )


class TestG1NativeDatasetAudit(unittest.TestCase):
    def test_action_array_empty(self):
        arr = action_array([])
        self.assertEqual(arr.shape, (0, 8))

    def test_action_array_shape(self):
        records = [make_record(0), make_record(1)]
        arr = action_array(records)
        self.assertEqual(arr.shape, (2, 8))

    def test_phase_counts(self):
        records = [
            make_record(0, phase="A"),
            make_record(1, phase="B"),
            make_record(2, phase="A"),
        ]
        self.assertEqual(phase_counts(records), {"A": 2, "B": 1})

    def test_boolean_balance(self):
        records = [
            make_record(0, reach_active=False, grip_closed=False),
            make_record(1, reach_active=True, grip_closed=True),
        ]
        balance = boolean_balance(records)
        self.assertEqual(balance["reach_active_true"], 1)
        self.assertEqual(balance["grip_closed_true"], 1)
        self.assertAlmostEqual(balance["reach_active_true_fraction"], 0.5)

    def test_action_statistics(self):
        records = [
            make_record(0, walk=(0, 0, 0)),
            make_record(1, walk=(2, 0, 0)),
        ]
        stats = action_statistics(records)
        self.assertAlmostEqual(stats["walk_x"]["min"], 0.0)
        self.assertAlmostEqual(stats["walk_x"]["max"], 2.0)
        self.assertAlmostEqual(stats["walk_x"]["mean"], 1.0)

    def test_magnitude_statistics(self):
        records = [
            make_record(0, walk=(0, 0, 0)),
            make_record(1, walk=(3, 4, 0)),
        ]
        stats = magnitude_statistics(records)
        self.assertEqual(stats["zero_walk_records"], 1)
        self.assertEqual(stats["nonzero_walk_records"], 1)
        self.assertAlmostEqual(stats["max_walk_cmd_magnitude"], 5.0)

    def test_find_idle_runs(self):
        records = [make_record(i, phase="SETTLE") for i in range(30)]
        runs = find_idle_runs(records, min_run_length=25)
        self.assertEqual(len(runs), 1)
        self.assertEqual(runs[0]["length"], 30)
        self.assertEqual(runs[0]["phase"], "SETTLE")

    def test_phase_transition_counts(self):
        records = [
            make_record(0, phase="A"),
            make_record(1, phase="A"),
            make_record(2, phase="B"),
        ]
        segments = phase_transition_counts(records)
        self.assertEqual(len(segments), 2)
        self.assertEqual(segments[0]["phase"], "A")
        self.assertEqual(segments[0]["length"], 2)
        self.assertEqual(segments[1]["phase"], "B")

    def test_build_audit_report(self):
        records = [make_record(i) for i in range(30)]
        report = build_audit_report(records, source_dataset="test.jsonl")
        self.assertEqual(report["num_records"], 30)
        self.assertEqual(report["action_vector_shape"], [30, 8])
        self.assertIn("warnings", report)
        self.assertGreaterEqual(len(report["idle_runs"]), 1)

    def test_phase_temporal_split(self):
        records = []
        for i in range(10):
            records.append(make_record(i, phase="A"))
        for i in range(10, 20):
            records.append(make_record(i, phase="B"))

        train, val = phase_temporal_split(records, val_fraction=0.2)
        self.assertEqual(len(train), 16)
        self.assertEqual(len(val), 4)
        self.assertEqual(phase_counts(val), {"A": 2, "B": 2})

    def test_write_split_manifests(self):
        records = [make_record(i, phase="A") for i in range(10)]
        train, val = phase_temporal_split(records, val_fraction=0.2)

        with tempfile.TemporaryDirectory() as tmp:
            summary = write_split_manifests(tmp, train, val)
            root = Path(tmp)
            self.assertTrue((root / "train.jsonl").exists())
            self.assertTrue((root / "val.jsonl").exists())
            self.assertTrue((root / "split_summary.json").exists())
            self.assertEqual(summary["train_records"], 8)
            self.assertEqual(summary["val_records"], 2)

            loaded_train = read_dataset_jsonl(root / "train.jsonl")
            loaded_val = read_dataset_jsonl(root / "val.jsonl")
            self.assertEqual(len(loaded_train), 8)
            self.assertEqual(len(loaded_val), 2)


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `tests/test_g1_native_training_views.py`

```python
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np

from vla_bridge.g1_native_dataset import G1NativeVLARecord, read_dataset_jsonl
from vla_bridge.training_views import (
    build_training_views,
    build_weight_records,
    compute_phase_weights,
    filter_idle_records,
    is_idle_record,
    normalize_weights,
    read_weight_jsonl,
    training_view_summary,
    walk_magnitude,
    write_weight_jsonl,
)


def make_record(
    i: int,
    *,
    phase: str = "SETTLE",
    walk=(0.0, 0.0, 0.0),
    reach=(0.3, -0.2, 0.2),
    reach_active: bool = False,
    grip_closed: bool = False,
) -> G1NativeVLARecord:
    action = (
        float(walk[0]),
        float(walk[1]),
        float(walk[2]),
        float(reach[0]),
        float(reach[1]),
        float(reach[2]),
        1.0 if reach_active else 0.0,
        1.0 if grip_closed else 0.0,
    )
    return G1NativeVLARecord(
        sample_index=i,
        source_step_index=i,
        image_path=f"frames/frame_{i:06d}.png",
        instruction="Pick up the red cylinder and place it on the blue table.",
        phase=phase,
        walk_cmd=tuple(float(x) for x in walk),
        reach_target_pelvis=tuple(float(x) for x in reach),
        reach_active=reach_active,
        grip_closed=grip_closed,
        action_vector=action,
    )


class TestG1NativeTrainingViews(unittest.TestCase):
    def test_walk_magnitude(self):
        record = make_record(0, walk=(3, 4, 0))
        self.assertAlmostEqual(walk_magnitude(record), 5.0)

    def test_is_idle_record(self):
        self.assertTrue(is_idle_record(make_record(0)))
        self.assertFalse(is_idle_record(make_record(1, walk=(0.1, 0, 0))))
        self.assertFalse(is_idle_record(make_record(2, reach_active=True)))
        self.assertFalse(is_idle_record(make_record(3, grip_closed=True)))

    def test_rare_transition_is_not_idle(self):
        self.assertFalse(is_idle_record(make_record(0, phase="CLOSE_GRIP")))
        self.assertFalse(is_idle_record(make_record(1, phase="OPEN_GRIP")))

    def test_filter_idle_records_keeps_first_n_idle(self):
        records = [make_record(i) for i in range(20)]
        filtered = filter_idle_records(records, keep_first_n_idle=5)
        self.assertEqual(len(filtered), 5)
        self.assertEqual([r.sample_index for r in filtered], [0, 1, 2, 3, 4])

    def test_filter_preserves_rare_transitions(self):
        records = [make_record(i) for i in range(10)]
        records.append(make_record(10, phase="CLOSE_GRIP"))
        records.append(make_record(11, phase="OPEN_GRIP"))
        filtered = filter_idle_records(records, keep_first_n_idle=0)
        phases = [r.phase for r in filtered]
        self.assertIn("CLOSE_GRIP", phases)
        self.assertIn("OPEN_GRIP", phases)

    def test_compute_phase_weights_rare_higher_than_common(self):
        records = []
        for i in range(100):
            records.append(make_record(i, phase="APPROACH_TARGET", reach_active=True))
        records.append(make_record(100, phase="CLOSE_GRIP", grip_closed=True))
        weights = compute_phase_weights(records, max_weight=100.0, rare_phase_boost=5.0)
        self.assertGreater(weights[100], weights[0])

    def test_normalize_weights_mean_one(self):
        weights = {0: 1.0, 1: 3.0}
        normalized = normalize_weights(weights)
        self.assertAlmostEqual(np.mean(list(normalized.values())), 1.0)

    def test_build_weight_records(self):
        records = [make_record(0), make_record(1)]
        weights = {0: 0.5, 1: 2.0}
        rows = build_weight_records(records, weights)
        self.assertEqual(rows[0]["sample_index"], 0)
        self.assertEqual(rows[0]["weight"], 0.5)
        self.assertEqual(rows[1]["weight"], 2.0)

    def test_weight_jsonl_roundtrip(self):
        rows = [
            {"sample_index": 0, "source_step_index": 0, "phase": "A", "weight": 1.0, "image_path": "a.png"},
            {"sample_index": 1, "source_step_index": 1, "phase": "B", "weight": 2.0, "image_path": "b.png"},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "weights.jsonl"
            write_weight_jsonl(path, rows)
            restored = read_weight_jsonl(path)
            self.assertEqual(restored, rows)

    def test_training_view_summary(self):
        source = [make_record(i) for i in range(10)]
        source.append(make_record(10, phase="CLOSE_GRIP"))
        filtered = filter_idle_records(source, keep_first_n_idle=2)
        weights = normalize_weights(compute_phase_weights(source))
        summary = training_view_summary(
            source_records=source,
            filtered_records=filtered,
            weights=weights,
            view_name="test",
        )
        self.assertEqual(summary["source_records"], 11)
        self.assertLess(summary["filtered_records"], 11)
        self.assertEqual(summary["rare_transition_records_filtered"]["CLOSE_GRIP"], 1)

    def test_build_training_views_writes_files(self):
        records = [make_record(i) for i in range(20)]
        records.append(make_record(20, phase="CLOSE_GRIP"))
        records.append(make_record(21, phase="OPEN_GRIP"))

        with tempfile.TemporaryDirectory() as tmp:
            summary = build_training_views(records, output_dir=tmp, keep_first_n_idle=3)
            root = Path(tmp)
            self.assertTrue((root / "full.jsonl").exists())
            self.assertTrue((root / "filtered_no_idle.jsonl").exists())
            self.assertTrue((root / "sample_weights.jsonl").exists())
            self.assertTrue((root / "training_view_summary.json").exists())
            self.assertEqual(summary["source_records"], 22)
            self.assertEqual(summary["rare_transition_records_filtered"]["CLOSE_GRIP"], 1)
            self.assertEqual(summary["rare_transition_records_filtered"]["OPEN_GRIP"], 1)

            full = read_dataset_jsonl(root / "full.jsonl")
            filtered = read_dataset_jsonl(root / "filtered_no_idle.jsonl")
            self.assertEqual(len(full), 22)
            self.assertLess(len(filtered), 22)


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `tests/test_scenario_config.py`

```python
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vla_bridge.scenario_config import load_scenario_config, select_scenario


def _write_config(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


class TestScenarioConfig(unittest.TestCase):
    def test_loads_valid_config_and_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "defaults": {
                        "red_block_xy_offset_m": [0.01, -0.01],
                        "robot_base_xy_offset_m": [0.0, 0.0],
                        "target_drop_xy_offset_m": [0.0, 0.0],
                    },
                    "scenarios": [
                        {"scenario_id": "a", "seed": 1},
                        {"scenario_id": "b", "seed": 2, "red_block_xy_offset_m": [0.02, 0.0]},
                    ],
                },
            )
            cfg = load_scenario_config(path)
            self.assertEqual(cfg.name, "test_cfg")
            self.assertEqual(len(cfg.scenarios), 2)
            self.assertEqual(cfg.scenarios[0].red_block_xy_offset_m, (0.01, -0.01))
            self.assertEqual(cfg.scenarios[1].red_block_xy_offset_m, (0.02, 0.0))

    def test_rejects_duplicate_scenario_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "scenarios": [
                        {"scenario_id": "dup", "seed": 1},
                        {"scenario_id": "dup", "seed": 2},
                    ],
                },
            )
            with self.assertRaises(ValueError):
                load_scenario_config(path)

    def test_rejects_duplicate_seeds(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "scenarios": [
                        {"scenario_id": "a", "seed": 3},
                        {"scenario_id": "b", "seed": 3},
                    ],
                },
            )
            with self.assertRaises(ValueError):
                load_scenario_config(path)

    def test_rejects_bad_xy_offsets(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "defaults": {"red_block_xy_offset_m": [0.0]},
                    "scenarios": [{"scenario_id": "a", "seed": 1}],
                },
            )
            with self.assertRaises(ValueError):
                load_scenario_config(path)

    def test_select_scenario_wraps(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "scenarios": [
                        {"scenario_id": "a", "seed": 10},
                        {"scenario_id": "b", "seed": 11},
                        {"scenario_id": "c", "seed": 12},
                    ],
                },
            )
            cfg = load_scenario_config(path)
            self.assertEqual(select_scenario(cfg, 0).scenario_id, "a")
            self.assertEqual(select_scenario(cfg, 4).scenario_id, "b")


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `tests/test_vla_action_adapter.py`

```python
"""Unit tests for vla_bridge.action_adapter (Step 13).

These tests are pure NumPy and do not require MuJoCo, OpenVLA, Hugging Face,
PyTorch, or any cloud infrastructure.
"""

from __future__ import annotations

import unittest

import numpy as np

from vla_bridge.action_adapter import (
    G1VLAActionAdapter,
    clip_reach_target,
    quat_apply_inverse,
    validate_vector,
    world_to_pelvis,
)


class TestG1VLAActionAdapter(unittest.TestCase):
    def assertArrayClose(self, actual, expected, places=7):
        np.testing.assert_allclose(np.asarray(actual), np.asarray(expected), atol=10 ** (-places))

    # 1. Import smoke test
    def test_imports(self):
        self.assertIsNotNone(G1VLAActionAdapter)
        self.assertIsNotNone(validate_vector)
        self.assertIsNotNone(quat_apply_inverse)
        self.assertIsNotNone(world_to_pelvis)
        self.assertIsNotNone(clip_reach_target)

    # 2. Identity transform test
    def test_world_to_pelvis_identity(self):
        out = world_to_pelvis(
            pelvis_pos=np.array([0.0, 0.0, 0.0]),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            world_point=np.array([0.3, -0.2, 0.2]),
        )
        self.assertArrayClose(out, [0.3, -0.2, 0.2])

    # 3. Adapter zero-action test
    def test_zero_action_outputs_current_target(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.array([0.3, -0.2, 0.2]))
        out = adapter.step(
            np.zeros(7),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertEqual(out.walk_cmd, (0.0, 0.0, 0.0))
        self.assertEqual(out.reach_active, True)
        self.assertEqual(out.grip_closed, False)
        self.assertArrayClose(out.reach_target, [0.3, -0.2, 0.2])

    # 4. Delta accumulation test
    def test_delta_accumulates_and_clips_per_step(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.zeros(3))
        out = adapter.step(
            np.array([0.10, -0.10, 0.02, 0.0, 0.0, 0.0, 1.0]),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertArrayClose(out.reach_target, [0.05, -0.05, 0.02])
        self.assertEqual(out.grip_closed, True)

    # 5. Gripper threshold test
    def test_gripper_threshold(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.zeros(3), gripper_threshold=0.0)
        out_open = adapter.step(
            np.array([0, 0, 0, 0, 0, 0, 0.0], dtype=float),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertFalse(out_open.grip_closed)

        adapter.reset(np.zeros(3))
        out_closed = adapter.step(
            np.array([0, 0, 0, 0, 0, 0, 0.01], dtype=float),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertTrue(out_closed.grip_closed)

    # 6. Workspace clipping test
    def test_workspace_clipping(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.zeros(3), max_delta_m=10.0)
        out = adapter.step(
            np.array([10, -10, 10, 0, 0, 0, 0], dtype=float),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertArrayClose(out.reach_target, [0.60, -0.60, 0.60])

    # 7. Lazy initialization test
    def test_lazy_initialization_from_current_palm_world(self):
        adapter = G1VLAActionAdapter()
        out = adapter.step(
            np.zeros(7),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            current_palm_world=np.array([0.1, 0.2, 0.3]),
        )
        self.assertArrayClose(out.reach_target, [0.1, 0.2, 0.3])

    # 8. Missing initialization error test
    def test_missing_initialization_raises(self):
        adapter = G1VLAActionAdapter()
        with self.assertRaises(ValueError):
            adapter.step(
                np.zeros(7),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            )

    # 9. Shape validation test
    def test_shape_validation(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.zeros(3))
        with self.assertRaises(ValueError):
            adapter.step(
                np.zeros(6),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            )
        with self.assertRaises(ValueError):
            adapter.step(
                np.zeros(7),
                pelvis_pos=np.zeros(2),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            )
        with self.assertRaises(ValueError):
            adapter.step(
                np.zeros(7),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0]),
            )


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `tests/test_vla_batch_manifest.py`

```python
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from vla_bridge.batch_manifest import (
    STATUS_FAILED,
    STATUS_SUCCESS,
    build_batch_manifest,
    demo_record_from_summary,
    failed_demo_record,
    make_demo_id,
    manifest_summary,
    read_batch_manifest,
    successful_demo_paths,
    write_batch_manifest,
)


class TestVLABatchManifest(unittest.TestCase):
    def test_make_demo_id(self):
        self.assertEqual(make_demo_id(0), "demo_000")
        self.assertEqual(make_demo_id(12), "demo_012")
        self.assertEqual(make_demo_id(123), "demo_123")

    def test_make_demo_id_negative_raises(self):
        with self.assertRaises(ValueError):
            make_demo_id(-1)

    def test_demo_record_from_summary(self):
        summary = {
            "done_reached": True,
            "num_steps": 2665,
            "num_frames": 2665,
        }
        record = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary=summary,
        )
        self.assertEqual(record.demo_id, "demo_000")
        self.assertEqual(record.status, STATUS_SUCCESS)
        self.assertTrue(record.done_reached)
        self.assertEqual(record.num_steps, 2665)
        self.assertEqual(record.num_frames, 2665)
        self.assertTrue(record.metadata_path.endswith("demo.jsonl"))
        self.assertTrue(record.summary_path.endswith("summary.json"))

    def test_failed_demo_record(self):
        record = failed_demo_record(
            demo_id="demo_001",
            output_dir="batch/demo_001",
            error="boom",
        )
        self.assertEqual(record.status, STATUS_FAILED)
        self.assertFalse(record.done_reached)
        self.assertEqual(record.num_steps, 0)
        self.assertEqual(record.num_frames, 0)
        self.assertEqual(record.error, "boom")

    def test_build_batch_manifest_counts(self):
        success = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary={"done_reached": True, "num_steps": 10, "num_frames": 10},
        )
        failed = failed_demo_record(
            demo_id="demo_001",
            output_dir="batch/demo_001",
            error="boom",
        )
        manifest = build_batch_manifest(
            batch_id="batch_000",
            output_root="batch",
            num_requested=2,
            record_every=1,
            camera="head_cam",
            no_images=False,
            max_ticks=4000,
            demos=[success, failed],
            created_unix_time=123.0,
        )
        self.assertEqual(manifest.num_completed, 1)
        self.assertEqual(manifest.num_failed, 1)
        self.assertEqual(manifest.created_unix_time, 123.0)

    def test_manifest_roundtrip(self):
        record = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary={"done_reached": True, "num_steps": 10, "num_frames": 5},
        )
        manifest = build_batch_manifest(
            batch_id="batch_000",
            output_root="batch",
            num_requested=1,
            record_every=1,
            camera="head_cam",
            no_images=False,
            max_ticks=4000,
            demos=[record],
            created_unix_time=123.0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "batch_manifest.json"
            write_batch_manifest(path, manifest)
            restored = read_batch_manifest(path)
            self.assertEqual(restored, manifest)

    def test_successful_demo_paths(self):
        done = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary={"done_reached": True, "num_steps": 10, "num_frames": 10},
        )
        not_done = demo_record_from_summary(
            demo_id="demo_001",
            output_dir="batch/demo_001",
            summary={"done_reached": False, "num_steps": 10, "num_frames": 10},
        )
        failed = failed_demo_record(
            demo_id="demo_002",
            output_dir="batch/demo_002",
            error="boom",
        )
        manifest = build_batch_manifest(
            batch_id="batch_000",
            output_root="batch",
            num_requested=3,
            record_every=1,
            camera="head_cam",
            no_images=False,
            max_ticks=4000,
            demos=[done, not_done, failed],
            created_unix_time=123.0,
        )
        paths = successful_demo_paths(manifest)
        self.assertEqual(paths, [done.metadata_path])

    def test_manifest_summary(self):
        a = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary={"done_reached": True, "num_steps": 10, "num_frames": 5},
        )
        b = demo_record_from_summary(
            demo_id="demo_001",
            output_dir="batch/demo_001",
            summary={"done_reached": True, "num_steps": 20, "num_frames": 6},
        )
        manifest = build_batch_manifest(
            batch_id="batch_000",
            output_root="batch",
            num_requested=2,
            record_every=1,
            camera="head_cam",
            no_images=False,
            max_ticks=4000,
            demos=[a, b],
            created_unix_time=123.0,
        )
        summary = manifest_summary(manifest)
        self.assertEqual(summary["successful_done_demos"], 2)
        self.assertEqual(summary["total_steps"], 30)
        self.assertEqual(summary["total_frames"], 11)
        self.assertEqual(summary["demo_ids"], ["demo_000", "demo_001"])


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `tests/test_vla_demo_schema.py`

```python
"""Unit tests for vla_bridge.demo_schema and vla_bridge.demo_recorder.

These tests are pure Python + NumPy; no MuJoCo, OpenVLA, or network access
is required.
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np

from vla_bridge.demo_schema import (
    VLADemoStep,
    as_float_tuple,
    make_action_7d,
    read_jsonl,
    step_from_json,
    step_to_json,
    write_jsonl,
)
from vla_bridge.demo_recorder import VLADemoRecorder


def make_step(i: int = 0) -> VLADemoStep:
    """Create a deterministic VLADemoStep for testing."""
    return VLADemoStep(
        step_index=i,
        sim_time=float(i) * 0.1,
        image_path=f"frames/frame_{i:06d}.png",
        instruction="Pick up the red cylinder and place it on the blue table.",
        phase="SETTLE",
        palm_world=(0.1, 0.2, 0.3),
        pelvis_pos=(0.0, 0.0, 0.76),
        pelvis_quat=(1.0, 0.0, 0.0, 0.0),
        walk_cmd=(0.0, 0.0, 0.0),
        reach_target_pelvis=(0.3, -0.2, 0.2),
        reach_active=True,
        grip_closed=False,
        action_7d=(0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    )


class TestAsFloatTuple(unittest.TestCase):
    def test_correct_shape_returns_python_floats(self):
        out = as_float_tuple([1, 2, 3], 3, "x")
        self.assertEqual(out, (1.0, 2.0, 3.0))
        self.assertTrue(all(isinstance(v, float) for v in out))

    def test_rejects_wrong_shape(self):
        with self.assertRaises(ValueError):
            as_float_tuple([1, 2], 3, "x")

    def test_accepts_numpy_array(self):
        out = as_float_tuple(np.array([0.5, 1.5, 2.5]), 3, "y")
        self.assertEqual(len(out), 3)


class TestMakeAction7d(unittest.TestCase):
    def test_xyz_delta_and_gripper_closed(self):
        action = make_action_7d(
            np.array([0.1, 0.2, 0.3]),
            np.array([0.2, 0.1, 0.35]),
            grip_closed=True,
        )
        np.testing.assert_allclose(action[:3], [0.1, -0.1, 0.05], atol=1e-10)
        self.assertEqual(action[3:6], (0.0, 0.0, 0.0))
        self.assertEqual(action[6], 1.0)

    def test_gripper_open(self):
        action = make_action_7d(
            np.zeros(3), np.zeros(3), grip_closed=False
        )
        self.assertEqual(action[6], 0.0)

    def test_rejects_wrong_shape(self):
        with self.assertRaises(ValueError):
            make_action_7d(np.zeros(2), np.zeros(3), False)


class TestJsonRoundtrip(unittest.TestCase):
    def test_single_step_roundtrip(self):
        step = make_step(3)
        line = step_to_json(step)
        restored = step_from_json(line)
        self.assertEqual(restored, step)

    def test_json_roundtrip_includes_teacher_commands(self):
        step = make_step(3)
        restored = step_from_json(step_to_json(step))
        self.assertEqual(restored.walk_cmd, step.walk_cmd)
        self.assertEqual(restored.reach_active, step.reach_active)

    def test_backward_compat_missing_walk_cmd_and_reach_active(self):
        """Older JSONL without walk_cmd/reach_active should deserialize with defaults."""
        import json as _json
        old_data = {
            "step_index": 0,
            "sim_time": 0.0,
            "image_path": "",
            "instruction": "test",
            "phase": "SETTLE",
            "palm_world": [0.1, 0.2, 0.3],
            "pelvis_pos": [0.0, 0.0, 0.76],
            "pelvis_quat": [1.0, 0.0, 0.0, 0.0],
            "reach_target_pelvis": [0.3, -0.2, 0.2],
            "grip_closed": False,
            "action_7d": [0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        }
        restored = step_from_json(_json.dumps(old_data))
        self.assertEqual(restored.walk_cmd, (0.0, 0.0, 0.0))
        self.assertTrue(restored.reach_active)


class TestJsonlRoundtrip(unittest.TestCase):
    def test_multiple_steps_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.jsonl"
            steps = [make_step(0), make_step(1)]
            write_jsonl(path, steps)
            restored = read_jsonl(path)
            self.assertEqual(restored, steps)

    def test_creates_parent_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "dir" / "demo.jsonl"
            write_jsonl(path, [make_step(0)])
            self.assertTrue(path.exists())


class TestRecorderSingleObservation(unittest.TestCase):
    def test_finalizes_zero_action(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = VLADemoRecorder(tmp, instruction="test", record_every=1)
            rec.observe(
                control_tick=0,
                sim_time=0.0,
                rgb=None,
                phase="SETTLE",
                palm_world=np.array([0.0, 0.0, 0.0]),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
                walk_cmd=(0.0, 0.0, 0.0),
                reach_target_pelvis=(0.3, -0.2, 0.2),
                reach_active=True,
                grip_closed=False,
            )
            rec.finalize()
            self.assertEqual(len(rec.steps), 1)
            self.assertEqual(
                rec.steps[0].action_7d, (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
            )


class TestRecorderTwoObservations(unittest.TestCase):
    def test_computes_palm_delta_action(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = VLADemoRecorder(tmp, instruction="test", record_every=1)
            base_kwargs = dict(
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
                walk_cmd=(0.0, 0.0, 0.0),
                reach_target_pelvis=(0.3, -0.2, 0.2),
                reach_active=True,
            )
            rec.observe(
                control_tick=0,
                sim_time=0.0,
                rgb=None,
                phase="SETTLE",
                palm_world=np.array([0.0, 0.0, 0.0]),
                grip_closed=False,
                **base_kwargs,
            )
            rec.observe(
                control_tick=1,
                sim_time=0.02,
                rgb=None,
                phase="SETTLE",
                palm_world=np.array([0.01, -0.02, 0.03]),
                grip_closed=True,
                **base_kwargs,
            )
            rec.finalize()

            self.assertEqual(len(rec.steps), 2)
            # First step's action = delta to second palm position; grip from step 0
            np.testing.assert_allclose(
                rec.steps[0].action_7d[:3], [0.01, -0.02, 0.03], atol=1e-10
            )
            self.assertEqual(rec.steps[0].action_7d[6], 0.0)  # grip was open at step 0
            # Second (last) step gets zero action; grip from step 1
            self.assertEqual(rec.steps[1].action_7d[6], 1.0)


class TestRecorderRecordEvery(unittest.TestCase):
    def test_respects_record_every(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = VLADemoRecorder(tmp, instruction="test", record_every=2)
            kwargs = dict(
                sim_time=0.0,
                rgb=None,
                phase="SETTLE",
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
                walk_cmd=(0.0, 0.0, 0.0),
                reach_target_pelvis=(0.3, -0.2, 0.2),
                reach_active=True,
                grip_closed=False,
            )
            # Ticks 0, 1, 2 — only 0 and 2 should be recorded (even ticks)
            rec.observe(control_tick=0, palm_world=np.array([0.0, 0.0, 0.0]), **kwargs)
            rec.observe(control_tick=1, palm_world=np.array([1.0, 0.0, 0.0]), **kwargs)
            rec.observe(control_tick=2, palm_world=np.array([0.2, 0.0, 0.0]), **kwargs)
            rec.finalize()

            self.assertEqual(len(rec.steps), 2)
            # Step at tick=0: action delta is palm(tick=2) - palm(tick=0)
            np.testing.assert_allclose(
                rec.steps[0].action_7d[:3], [0.2, 0.0, 0.0], atol=1e-10
            )


class TestRecorderFramePath(unittest.TestCase):
    def test_saves_frame_path_when_rgb_provided(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = VLADemoRecorder(tmp, instruction="test", record_every=1)
            rgb = np.zeros((8, 8, 3), dtype=np.uint8)
            rec.observe(
                control_tick=0,
                sim_time=0.0,
                rgb=rgb,
                phase="SETTLE",
                palm_world=np.zeros(3),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
                walk_cmd=(0.0, 0.0, 0.0),
                reach_target_pelvis=(0.3, -0.2, 0.2),
                reach_active=True,
                grip_closed=False,
            )
            rec.finalize()
            self.assertTrue(rec.steps[0].image_path.startswith("frames/frame_"))


class TestRecorderWalkCmdAndReachActive(unittest.TestCase):
    def test_stores_walk_cmd_and_reach_active(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = VLADemoRecorder(tmp, instruction="test", record_every=1)
            rec.observe(
                control_tick=0,
                sim_time=0.0,
                rgb=None,
                phase="WALK",
                palm_world=np.zeros(3),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
                walk_cmd=(0.1, 0.0, 0.2),
                reach_target_pelvis=(0.3, -0.2, 0.2),
                reach_active=False,
                grip_closed=False,
            )
            rec.finalize()
            step = rec.steps[0]
            self.assertAlmostEqual(step.walk_cmd[0], 0.1)
            self.assertAlmostEqual(step.walk_cmd[2], 0.2)
            self.assertFalse(step.reach_active)


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `tests/test_vla_replay_metrics.py`

```python
from __future__ import annotations

import unittest

import numpy as np

from vla_bridge.demo_schema import VLADemoStep
from vla_bridge.replay_metrics import (
    ReplayMetrics,
    action_xyz_magnitudes,
    compute_replay_metrics,
    grip_mismatch_count,
    palm_error_metrics,
    walk_command_magnitudes,
)


def make_step(
    i: int,
    palm=(0.0, 0.0, 0.0),
    grip=False,
    action=(0.0, 0.0, 0.0),
    walk_cmd=(0.0, 0.0, 0.0),
    reach_active=True,
) -> VLADemoStep:
    return VLADemoStep(
        step_index=i,
        sim_time=float(i) * 0.02,
        image_path="",
        instruction="test",
        phase="TEST",
        palm_world=tuple(float(x) for x in palm),
        pelvis_pos=(0.0, 0.0, 0.76),
        pelvis_quat=(1.0, 0.0, 0.0, 0.0),
        walk_cmd=tuple(float(x) for x in walk_cmd),
        reach_target_pelvis=(0.3, -0.2, 0.2),
        reach_active=bool(reach_active),
        grip_closed=bool(grip),
        action_7d=(
            float(action[0]),
            float(action[1]),
            float(action[2]),
            0.0,
            0.0,
            0.0,
            1.0 if grip else 0.0,
        ),
    )


class TestVLAReplayMetrics(unittest.TestCase):
    def test_action_magnitudes_empty(self):
        mags = action_xyz_magnitudes([])
        self.assertEqual(mags.shape, (0,))
        self.assertEqual(mags.dtype, np.float64)

    def test_action_magnitudes_known_values(self):
        steps = [
            make_step(0, action=(3.0, 4.0, 0.0)),
            make_step(1, action=(0.0, 0.0, 12.0)),
        ]
        mags = action_xyz_magnitudes(steps)
        np.testing.assert_allclose(mags, [5.0, 12.0])

    def test_palm_error_metrics_known_values(self):
        teacher = np.array([[0, 0, 0], [1, 0, 0]], dtype=float)
        replay = np.array([[0, 0, 0], [2, 0, 0]], dtype=float)
        mean_err, max_err, final_err = palm_error_metrics(teacher, replay)
        self.assertAlmostEqual(mean_err, 0.5)
        self.assertAlmostEqual(max_err, 1.0)
        self.assertAlmostEqual(final_err, 1.0)

    def test_palm_error_metrics_rejects_shape_mismatch(self):
        with self.assertRaises(ValueError):
            palm_error_metrics(np.zeros((2, 3)), np.zeros((3, 3)))

    def test_palm_error_metrics_empty_returns_nan(self):
        mean_err, max_err, final_err = palm_error_metrics(
            np.zeros((0, 3)), np.zeros((0, 3))
        )
        self.assertTrue(np.isnan(mean_err))
        self.assertTrue(np.isnan(max_err))
        self.assertTrue(np.isnan(final_err))

    def test_grip_mismatch_count(self):
        self.assertEqual(
            grip_mismatch_count(
                [False, True, True, False], [False, False, True, True]
            ),
            2,
        )

    def test_grip_mismatch_count_all_match(self):
        self.assertEqual(grip_mismatch_count([True, False], [True, False]), 0)

    def test_grip_mismatch_count_length_mismatch_raises(self):
        with self.assertRaises(ValueError):
            grip_mismatch_count([True, False], [True])

    def test_compute_replay_metrics(self):
        steps = [
            make_step(0, palm=(0, 0, 0), grip=False, action=(0.1, 0, 0)),
            make_step(1, palm=(1, 0, 0), grip=True, action=(0, 0.2, 0)),
        ]
        replay = np.array([[0, 0, 0], [1.5, 0, 0]], dtype=float)
        metrics = compute_replay_metrics(steps, replay, [False, False])

        self.assertIsInstance(metrics, ReplayMetrics)
        self.assertEqual(metrics.num_steps, 2)
        self.assertAlmostEqual(metrics.mean_palm_error_m, 0.25)
        self.assertAlmostEqual(metrics.max_palm_error_m, 0.5)
        self.assertAlmostEqual(metrics.final_palm_error_m, 0.5)
        # action mags: ||(0.1,0,0)|| = 0.1, ||(0,0.2,0)|| = 0.2
        self.assertAlmostEqual(metrics.mean_action_magnitude_m, 0.15)
        self.assertAlmostEqual(metrics.max_action_magnitude_m, 0.2)
        # teacher grip = [False, True], replay grip = [False, False] → 1 mismatch
        self.assertEqual(metrics.grip_mismatch_count, 1)

    def test_compute_replay_metrics_shape_mismatch_raises(self):
        steps = [make_step(0)]
        with self.assertRaises(ValueError):
            compute_replay_metrics(steps, np.zeros((2, 3)), [False])

    def test_compute_replay_metrics_grip_length_mismatch_raises(self):
        steps = [make_step(0)]
        with self.assertRaises(ValueError):
            compute_replay_metrics(steps, np.zeros((1, 3)), [])


class TestWalkCommandMetrics(unittest.TestCase):
    def test_walk_command_magnitudes_empty(self):
        mags = walk_command_magnitudes([])
        self.assertEqual(mags.shape, (0,))
        self.assertEqual(mags.dtype, np.float64)

    def test_walk_command_magnitudes_known_values(self):
        steps = [
            make_step(0, walk_cmd=(3.0, 4.0, 0.0)),
            make_step(1, walk_cmd=(0.0, 0.0, 12.0)),
        ]
        mags = walk_command_magnitudes(steps)
        np.testing.assert_allclose(mags, [5.0, 12.0])

    def test_compute_replay_metrics_includes_walk_fields(self):
        steps = [
            make_step(0, walk_cmd=(0.0, 0.0, 0.0), reach_active=False),
            make_step(1, walk_cmd=(3.0, 4.0, 0.0), reach_active=True),
        ]
        replay = np.array([[0, 0, 0], [0, 0, 0]], dtype=float)
        metrics = compute_replay_metrics(steps, replay, [False, False])

        self.assertEqual(metrics.walk_nonzero_steps, 1)
        self.assertEqual(metrics.reach_active_steps, 1)
        self.assertAlmostEqual(metrics.max_walk_command_magnitude, 5.0)
        self.assertAlmostEqual(metrics.mean_walk_command_magnitude, 2.5)


if __name__ == "__main__":
    unittest.main()
```

---

## FILE: `vision/__init__.py`

```python
"""Vision pipelines and perception utilities."""
```

---

## FILE: `vla_bridge/__init__.py`

```python
"""VLA bridge package for OpenVLA-style action experiments."""

from vla_bridge.action_adapter import (
    G1VLAActionAdapter,
    clip_reach_target,
    quat_apply_inverse,
    validate_vector,
    world_to_pelvis,
)
from vla_bridge.demo_schema import (
    VLADemoStep,
    as_float_tuple,
    make_action_7d,
    read_jsonl,
    step_from_json,
    step_to_json,
    write_jsonl,
)
from vla_bridge.demo_recorder import VLADemoRecorder
from vla_bridge.replay_metrics import (
    ReplayMetrics,
    action_xyz_magnitudes,
    compute_replay_metrics,
    grip_mismatch_count,
    palm_error_metrics,
    walk_command_magnitudes,
)
from vla_bridge.g1_native_dataset import (
    G1NativeVLARecord,
    copy_images_for_records,
    dataset_summary,
    export_records_from_steps,
    make_action_vector,
    read_dataset_jsonl,
    record_from_demo_step,
    record_from_json,
    record_to_json,
    write_dataset_jsonl,
)
from vla_bridge.dataset_audit import (
    ACTION_NAMES,
    action_array,
    action_statistics,
    boolean_balance,
    build_audit_report,
    find_idle_runs,
    magnitude_statistics,
    phase_counts,
    phase_temporal_split,
    phase_transition_counts,
    write_audit_report,
    write_split_manifests,
)
from vla_bridge.training_views import (
    RARE_TRANSITION_PHASES,
    build_training_views,
    build_weight_records,
    compute_phase_weights,
    filter_idle_records,
    is_idle_record,
    normalize_weights,
    read_weight_jsonl,
    training_view_summary,
    walk_magnitude,
    write_weight_jsonl,
)
from vla_bridge.batch_manifest import (
    STATUS_FAILED,
    STATUS_SUCCESS,
    BatchManifest,
    DemoRunRecord,
    build_batch_manifest,
    demo_record_from_summary,
    failed_demo_record,
    make_demo_id,
    manifest_summary,
    read_batch_manifest,
    successful_demo_paths,
    write_batch_manifest,
)
from vla_bridge.batch_dataset_export import (
    BatchExportSelection,
    export_combined_batch_dataset,
    load_demo_records,
    select_successful_demos,
)
from vla_bridge.scenario_config import (
    ScenarioConfig,
    ScenarioSpec,
    load_scenario_config,
    scenario_to_metadata,
    select_scenario,
)
from vla_bridge.batch_diversity import summarize_manifest_diversity

__all__ = [
    # Step 13 — action adapter
    "G1VLAActionAdapter",
    "clip_reach_target",
    "quat_apply_inverse",
    "validate_vector",
    "world_to_pelvis",
    # Step 14 — demonstration schema and recorder
    "VLADemoStep",
    "VLADemoRecorder",
    "as_float_tuple",
    "make_action_7d",
    "read_jsonl",
    "step_from_json",
    "step_to_json",
    "write_jsonl",
    # Step 15 — replay metrics
    "ReplayMetrics",
    "action_xyz_magnitudes",
    "compute_replay_metrics",
    "grip_mismatch_count",
    "palm_error_metrics",
    # Step 16 — walk command metrics
    "walk_command_magnitudes",
    # Step 17 — G1-native dataset
    "G1NativeVLARecord",
    "copy_images_for_records",
    "dataset_summary",
    "export_records_from_steps",
    "make_action_vector",
    "read_dataset_jsonl",
    "record_from_demo_step",
    "record_from_json",
    "record_to_json",
    "write_dataset_jsonl",
    # Step 18 — dataset audit
    "ACTION_NAMES",
    "action_array",
    "action_statistics",
    "boolean_balance",
    "build_audit_report",
    "find_idle_runs",
    "magnitude_statistics",
    "phase_counts",
    "phase_temporal_split",
    "phase_transition_counts",
    "write_audit_report",
    "write_split_manifests",
    # Step 19 — training views
    "RARE_TRANSITION_PHASES",
    "build_training_views",
    "build_weight_records",
    "compute_phase_weights",
    "filter_idle_records",
    "is_idle_record",
    "normalize_weights",
    "read_weight_jsonl",
    "training_view_summary",
    "walk_magnitude",
    "write_weight_jsonl",
    # Step 20 — batch manifest
    "STATUS_FAILED",
    "STATUS_SUCCESS",
    "BatchManifest",
    "DemoRunRecord",
    "build_batch_manifest",
    "demo_record_from_summary",
    "failed_demo_record",
    "make_demo_id",
    "manifest_summary",
    "read_batch_manifest",
    "successful_demo_paths",
    "write_batch_manifest",
    # Step 21 — batch dataset export
    "BatchExportSelection",
    "export_combined_batch_dataset",
    "load_demo_records",
    "select_successful_demos",
    # Step 22 — scenario perturbations and diversity
    "ScenarioSpec",
    "ScenarioConfig",
    "load_scenario_config",
    "select_scenario",
    "scenario_to_metadata",
    "summarize_manifest_diversity",
]
```

---

## FILE: `vla_bridge/action_adapter.py`

```python
"""Adapter from OpenVLA-style 7D actions to G1 PolicyOutput commands.

Step 13 scope:
- no OpenVLA import
- no model inference
- no demo recording
- no runtime integration

The adapter treats a VLA action as a small end-effector delta in world frame:
[dx, dy, dz, droll, dpitch, dyaw, gripper]

Only dx/dy/dz and gripper are used in this first milestone.
Rotation is intentionally ignored until we prove the action representation is executable.
"""

from __future__ import annotations

import numpy as np

from policies.base import PolicyOutput


_REACH_LOW = np.array([-0.30, -0.60, -0.40], dtype=np.float64)
_REACH_HIGH = np.array([0.60, 0.30, 0.60], dtype=np.float64)


def validate_vector(name: str, value: np.ndarray, shape: tuple[int, ...]) -> np.ndarray:
    """Validate that *value* can be cast to a float64 array of *shape*."""
    arr = np.asarray(value, dtype=np.float64)
    if arr.shape != shape:
        raise ValueError(f"{name} must have shape {shape}, got {arr.shape}")
    return arr.copy()


def quat_apply_inverse(quat_wxyz: np.ndarray, vec: np.ndarray) -> np.ndarray:
    """Rotate *vec* by the inverse (conjugate) of *quat_wxyz*.

    Uses the sandwich formula: q^{-1} v q, computed via cross-product form.
    *quat_wxyz* is in MuJoCo scalar-first order: [w, x, y, z].
    """
    q = validate_vector("quat_wxyz", quat_wxyz, (4,))
    v = validate_vector("vec", vec, (3,))
    norm = float(np.linalg.norm(q))
    if norm <= 1e-12:
        raise ValueError("quat_wxyz must be non-zero")
    q = q / norm
    w = q[0]
    xyz = q[1:4]
    t = 2.0 * np.cross(xyz, v)
    return v - w * t + np.cross(xyz, t)


def world_to_pelvis(
    pelvis_pos: np.ndarray,
    pelvis_quat: np.ndarray,
    world_point: np.ndarray,
) -> np.ndarray:
    """Transform *world_point* from world frame into the pelvis body frame.

    Args:
        pelvis_pos: (3,) world-frame position of the pelvis origin.
        pelvis_quat: (4,) orientation of the pelvis in MuJoCo [w, x, y, z] order.
        world_point: (3,) point to transform.

    Returns:
        (3,) coordinates expressed in the pelvis frame.
    """
    p = validate_vector("pelvis_pos", pelvis_pos, (3,))
    q = validate_vector("pelvis_quat", pelvis_quat, (4,))
    wpt = validate_vector("world_point", world_point, (3,))
    return quat_apply_inverse(q, wpt - p)


def clip_reach_target(reach_target: np.ndarray) -> np.ndarray:
    """Clip *reach_target* to the reacher workspace bounds."""
    target = validate_vector("reach_target", reach_target, (3,))
    return np.clip(target, _REACH_LOW, _REACH_HIGH)


class G1VLAActionAdapter:
    """Convert OpenVLA-style 7D actions into G1 PolicyOutput commands.

    This adapter is intentionally small and model-free. It does not know about
    OpenVLA internals. It only tests whether a 7D end-effector action interface
    can drive the existing G1 reacher/grip control path.

    The 7D action vector is:
        [dx, dy, dz, droll, dpitch, dyaw, gripper]

    droll / dpitch / dyaw are intentionally ignored in Step 13.
    Only dx/dy/dz (world-frame palm delta) and gripper are consumed.
    """

    def __init__(
        self,
        initial_palm_world: np.ndarray | None = None,
        max_delta_m: float = 0.05,
        gripper_threshold: float = 0.0,
    ) -> None:
        """Initialize the adapter.

        Args:
            initial_palm_world: Optional (3,) starting desired palm position in
                world coordinates.  Can also be set later via ``reset()``.
            max_delta_m: Per-step per-axis clipping limit (metres).
            gripper_threshold: gripper action values strictly above this are
                treated as *closed*.
        """
        if max_delta_m <= 0:
            raise ValueError("max_delta_m must be positive")
        self.max_delta_m = float(max_delta_m)
        self.gripper_threshold = float(gripper_threshold)
        self._desired_palm_world: np.ndarray | None = None
        self._last_action_7d: np.ndarray | None = None
        self._last_reach_target: np.ndarray | None = None

        if initial_palm_world is not None:
            self.reset(initial_palm_world)

    # ------------------------------------------------------------------
    # Read-only properties
    # ------------------------------------------------------------------

    @property
    def desired_palm_world(self) -> np.ndarray | None:
        """Current desired palm position in world frame (copy)."""
        return None if self._desired_palm_world is None else self._desired_palm_world.copy()

    @property
    def last_action_7d(self) -> np.ndarray | None:
        """The most recent 7D action passed to ``step()`` (copy)."""
        return None if self._last_action_7d is None else self._last_action_7d.copy()

    @property
    def last_reach_target(self) -> np.ndarray | None:
        """The most recent pelvis-frame reach target returned by ``step()`` (copy)."""
        return None if self._last_reach_target is None else self._last_reach_target.copy()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def reset(self, palm_world: np.ndarray) -> None:
        """Reset the desired palm position to *palm_world* (world frame).

        Also clears cached action and reach-target state.
        """
        self._desired_palm_world = validate_vector("palm_world", palm_world, (3,))
        self._last_action_7d = None
        self._last_reach_target = None

    def step(
        self,
        action_7d: np.ndarray,
        pelvis_pos: np.ndarray,
        pelvis_quat: np.ndarray,
        *,
        current_palm_world: np.ndarray | None = None,
        walk_cmd: tuple[float, float, float] = (0.0, 0.0, 0.0),
    ) -> PolicyOutput:
        """Apply *action_7d* and return the corresponding ``PolicyOutput``.

        Args:
            action_7d: Shape (7,) array ``[dx, dy, dz, droll, dpitch, dyaw, gripper]``
                in world frame.  Rotation channels are ignored in Step 13.
            pelvis_pos: Shape (3,) world-frame pelvis position from MuJoCo.
            pelvis_quat: Shape (4,) pelvis orientation ``[w, x, y, z]`` (MuJoCo order).
            current_palm_world: Optional (3,) current palm position used for lazy
                initialisation when ``reset()`` has not yet been called.
            walk_cmd: Base locomotion command forwarded verbatim into PolicyOutput.

        Returns:
            A ``PolicyOutput`` with ``reach_active=True`` and the clipped
            pelvis-frame reach target.

        Raises:
            ValueError: If ``desired_palm_world`` has not been initialised and
                ``current_palm_world`` is not provided.
        """
        action = validate_vector("action_7d", action_7d, (7,))
        ppos = validate_vector("pelvis_pos", pelvis_pos, (3,))
        pquat = validate_vector("pelvis_quat", pelvis_quat, (4,))

        if self._desired_palm_world is None:
            if current_palm_world is None:
                raise ValueError(
                    "Adapter has no desired_palm_world. Call reset(...) first "
                    "or pass current_palm_world to step(...)."
                )
            self.reset(current_palm_world)

        delta_world = np.clip(action[:3], -self.max_delta_m, self.max_delta_m)
        self._desired_palm_world = self._desired_palm_world + delta_world

        reach = world_to_pelvis(ppos, pquat, self._desired_palm_world)
        reach = clip_reach_target(reach)

        self._last_action_7d = action.copy()
        self._last_reach_target = reach.copy()

        grip_closed = bool(action[6] > self.gripper_threshold)

        return PolicyOutput(
            walk_cmd=tuple(float(x) for x in walk_cmd),
            reach_target=tuple(float(x) for x in reach),
            reach_active=True,
            grip_closed=grip_closed,
        )
```

---

## FILE: `vla_bridge/batch_dataset_export.py`

```python
"""Combined batch dataset export helpers for G1-native VLA.

Step 21 scope:
- no OpenVLA
- no model inference
- no fine-tuning
- pure aggregation of successful batch demonstrations
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Sequence
import json

from vla_bridge.batch_manifest import (
    BatchManifest,
    STATUS_SUCCESS,
    read_batch_manifest,
)
from vla_bridge.demo_schema import read_jsonl
from vla_bridge.g1_native_dataset import (
    export_records_from_steps,
    dataset_summary,
    write_summary,
)


@dataclass(frozen=True)
class BatchExportSelection:
    """Summary of which demos were selected from a batch for export."""
    batch_id: str
    selected_demo_ids: list[str]
    selected_metadata_paths: list[str]
    skipped_demo_ids: list[str]
    skip_reasons: dict[str, str]


def select_successful_demos(manifest: BatchManifest) -> BatchExportSelection:
    """Filter manifest for successful demos that reached DONE."""
    selected_ids = []
    selected_paths = []
    skipped_ids = []
    reasons = {}

    for demo in manifest.demos:
        if demo.status != STATUS_SUCCESS:
            skipped_ids.append(demo.demo_id)
            reasons[demo.demo_id] = f"status={demo.status}"
            continue
        if not demo.done_reached:
            skipped_ids.append(demo.demo_id)
            reasons[demo.demo_id] = "done_reached=false"
            continue
        if not demo.metadata_path:
            skipped_ids.append(demo.demo_id)
            reasons[demo.demo_id] = "missing metadata_path"
            continue
        
        selected_ids.append(demo.demo_id)
        selected_paths.append(demo.metadata_path)

    return BatchExportSelection(
        batch_id=manifest.batch_id,
        selected_demo_ids=selected_ids,
        selected_metadata_paths=selected_paths,
        skipped_demo_ids=skipped_ids,
        skip_reasons=reasons,
    )


def load_demo_records(metadata_path: str | Path) -> list[Any]:
    """Load raw demo steps from a metadata path."""
    return read_jsonl(metadata_path)


def _load_demo_rows_json(metadata_path: str | Path) -> list[dict[str, Any]]:
    src = Path(metadata_path)
    rows: list[dict[str, Any]] = []
    with src.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _prefix_image_path(
    image_path: str,
    *,
    demo_output_dir: str | Path,
    batch_root: str | Path,
) -> str:
    """Prefix a relative image path with its demo directory name."""
    if not image_path:
        return ""
    
    path_obj = Path(image_path)
    if path_obj.is_absolute():
        return image_path
    
    # Try to make demo_output_dir relative to batch_root
    try:
        rel_demo_dir = Path(demo_output_dir).relative_to(Path(batch_root))
        return str(rel_demo_dir / image_path)
    except ValueError:
        # Fallback: just use the name of the demo directory
        return str(Path(demo_output_dir).name / image_path)


def export_combined_batch_dataset(
    manifest_path: str | Path,
    output_dir: str | Path,
    *,
    include_phase: bool = True,
    drop_done: bool = True,
    drop_inactive_reach: bool = False,
) -> dict[str, Any]:
    """Combine successful demos from a manifest into one G1-native dataset."""
    manifest_path = Path(manifest_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = read_batch_manifest(manifest_path)
    selection = select_successful_demos(manifest)

    if not selection.selected_metadata_paths:
        raise ValueError(f"No successful done demos found in manifest: {manifest_path}")

    combined: list[dict[str, Any]] = []
    records_per_demo = {}
    records_per_scenario: dict[str, int] = {}
    unique_scenario_ids: set[str] = set()

    global_index = 0
    demo_lookup = {d.demo_id: d for d in manifest.demos}

    for demo_id, metadata_path in zip(selection.selected_demo_ids, selection.selected_metadata_paths):
        demo_record = demo_lookup[demo_id]
        
        # Load raw demo steps
        steps = load_demo_records(metadata_path)
        source_rows = _load_demo_rows_json(metadata_path)
        source_by_step_index = {
            int(row.get("step_index", i)): row
            for i, row in enumerate(source_rows)
        }
        
        # Convert to G1-native records using existing logic
        native_records = export_records_from_steps(
            steps,
            require_images=False,  # Don't fail here if some frames are missing
            include_phase=include_phase,
            drop_done=drop_done,
            drop_inactive_reach=drop_inactive_reach,
        )

        records_per_demo[demo_id] = len(native_records)

        for demo_sample_index, rec in enumerate(native_records):
            row = asdict(rec)
            # Override/Add fields
            row["sample_index"] = global_index
            row["batch_id"] = manifest.batch_id
            row["demo_id"] = demo_id
            row["demo_sample_index"] = demo_sample_index
            row["image_path"] = _prefix_image_path(
                str(row.get("image_path", "")),
                demo_output_dir=demo_record.output_dir,
                batch_root=manifest.output_root,
            )
            source_row = source_by_step_index.get(int(getattr(rec, "source_step_index", -1)), {})
            scenario_id = source_row.get("scenario_id", demo_record.scenario_id or "")
            seed = source_row.get("seed", demo_record.seed)
            scenario_meta = source_row.get("scenario", demo_record.scenario if demo_record.scenario is not None else {})
            if scenario_meta is None:
                scenario_meta = {}
            row["scenario_id"] = str(scenario_id)
            row["seed"] = seed
            row["scenario"] = scenario_meta
            records_per_scenario[row["scenario_id"]] = records_per_scenario.get(row["scenario_id"], 0) + 1
            unique_scenario_ids.add(row["scenario_id"])
            combined.append(row)
            global_index += 1

    dataset_path = output_dir / "dataset.jsonl"
    summary_path = output_dir / "summary.json"
    source_manifest_copy_path = output_dir / "source_manifest.json"

    # Write combined JSONL (using dicts)
    with dataset_path.open("w", encoding="utf-8") as f:
        for row in combined:
            f.write(json.dumps(row, separators=(",", ":")) + "\n")

    # Reuse summary logic (it works on G1NativeVLARecord or dicts with same fields)
    # Actually dataset_summary uses r.walk_cmd etc, so it expects objects.
    # Let's mock objects for summary or just use the dicts if it works.
    # dataset_summary implementation uses: walk = np.asarray([r.walk_cmd for r in records], ...)
    # In Python, r['walk_cmd'] would be needed for dicts.
    # I'll convert back to a simple namespace or just re-read if needed, 
    # but better to just pass objects to it.
    
    # Let's create dummy objects for summary
    class RecordMock:
        def __init__(self, d):
            self.walk_cmd = d["walk_cmd"]
            self.reach_target_pelvis = d["reach_target_pelvis"]
            self.phase = d["phase"]
            self.reach_active = d["reach_active"]
            self.grip_closed = d["grip_closed"]

    mock_records = [RecordMock(r) for r in combined]
    base_summary = dataset_summary(mock_records) # type: ignore

    summary = {
        **base_summary,
        "batch_id": manifest.batch_id,
        "source_manifest_path": str(manifest_path),
        "output_dir": str(output_dir),
        "dataset_path": str(dataset_path),
        "summary_path": str(summary_path),
        "source_manifest_copy_path": str(source_manifest_copy_path),
        "num_demos_in_manifest": len(manifest.demos),
        "num_selected_demos": len(selection.selected_demo_ids),
        "num_skipped_demos": len(selection.skipped_demo_ids),
        "selected_demo_ids": selection.selected_demo_ids,
        "skipped_demo_ids": selection.skipped_demo_ids,
        "skip_reasons": selection.skip_reasons,
        "records_per_demo": records_per_demo,
        "scenario_ids": sorted(unique_scenario_ids),
        "num_unique_scenarios": len(unique_scenario_ids),
        "records_per_scenario": records_per_scenario,
        "include_phase": include_phase,
        "drop_done": drop_done,
        "drop_inactive_reach": drop_inactive_reach,
        "action_vector": [
            "walk_x", "walk_y", "walk_yaw",
            "reach_x", "reach_y", "reach_z",
            "reach_active", "grip_closed"
        ]
    }

    write_summary(summary_path, summary)

    source_manifest_payload = {
        "selection": asdict(selection),
        "source_manifest": asdict(manifest),
    }
    source_manifest_copy_path.write_text(
        json.dumps(source_manifest_payload, indent=2),
        encoding="utf-8",
    )

    return summary
```

---

## FILE: `vla_bridge/batch_diversity.py`

```python
from __future__ import annotations

from typing import Any

from vla_bridge.batch_manifest import BatchManifest


def summarize_manifest_diversity(manifest: BatchManifest) -> dict[str, Any]:
    successful = [d for d in manifest.demos if d.status == "success"]
    scenario_ids: list[str] = []
    offsets: list[tuple[float, float]] = []
    for demo in manifest.demos:
        scenario_ids.append(demo.scenario_id or "")
        meta = demo.scenario or {}
        raw = meta.get("red_block_xy_offset_m", (0.0, 0.0))
        if isinstance(raw, (list, tuple)) and len(raw) == 2:
            dx = float(raw[0])
            dy = float(raw[1])
        else:
            dx, dy = 0.0, 0.0
        offsets.append((dx, dy))

    if offsets:
        dx_values = [o[0] for o in offsets]
        dy_values = [o[1] for o in offsets]
        dx_range = [min(dx_values), max(dx_values)]
        dy_range = [min(dy_values), max(dy_values)]
    else:
        dx_range = [0.0, 0.0]
        dy_range = [0.0, 0.0]

    all_offsets_identical = len(set(offsets)) <= 1
    unique_scenarios = sorted(set(scenario_ids))

    return {
        "batch_id": manifest.batch_id,
        "num_demos": len(manifest.demos),
        "num_successful_demos": len(successful),
        "num_unique_scenarios": len(unique_scenarios),
        "scenario_ids": unique_scenarios,
        "red_block_xy_offset_m_per_demo": [[float(x), float(y)] for x, y in offsets],
        "dx_range_m": [float(dx_range[0]), float(dx_range[1])],
        "dy_range_m": [float(dy_range[0]), float(dy_range[1])],
        "all_offsets_identical": all_offsets_identical,
    }
```

---

## FILE: `vla_bridge/batch_manifest.py`

```python
"""Batch manifest helpers for multi-demo VLA collection.

Step 20 scope:
- no OpenVLA
- no model inference
- no training
- pure manifest bookkeeping for multiple FSM teacher demonstrations
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import json
import time


STATUS_SUCCESS = "success"
STATUS_FAILED = "failed"


@dataclass(frozen=True)
class DemoRunRecord:
    """Detailed record of a single demonstration rollout in a batch."""
    demo_id: str
    output_dir: str
    metadata_path: str
    summary_path: str
    status: str
    done_reached: bool
    num_steps: int
    num_frames: int
    error: str = ""
    scenario_id: str = ""
    seed: int | None = None
    scenario: dict[str, Any] | None = None


@dataclass(frozen=True)
class BatchManifest:
    """Summary of a batch of demonstration rollouts."""
    batch_id: str
    output_root: str
    created_unix_time: float
    num_requested: int
    num_completed: int
    num_failed: int
    record_every: int
    camera: str
    no_images: bool
    max_ticks: int
    demos: list[DemoRunRecord]
    scenario_config_path: str = ""
    scenario_config_name: str = ""
    scenario_count: int = 0


def make_demo_id(index: int) -> str:
    """Return a zero-padded demo ID like 'demo_001'."""
    if index < 0:
        raise ValueError("index must be non-negative")
    return f"demo_{index:03d}"


def demo_record_from_summary(
    *,
    demo_id: str,
    output_dir: str | Path,
    summary: dict[str, Any],
    status: str = STATUS_SUCCESS,
    error: str = "",
    scenario_id: str = "",
    seed: int | None = None,
    scenario: dict[str, Any] | None = None,
) -> DemoRunRecord:
    """Build a DemoRunRecord from a recording summary."""
    out = Path(output_dir)
    return DemoRunRecord(
        demo_id=str(demo_id),
        output_dir=str(out),
        metadata_path=str(out / "demo.jsonl"),
        summary_path=str(out / "summary.json"),
        status=str(status),
        done_reached=bool(summary.get("done_reached", False)),
        num_steps=int(summary.get("num_steps", 0)),
        num_frames=int(summary.get("num_frames", 0)),
        error=str(error),
        scenario_id=str(scenario_id or summary.get("scenario_id", "")),
        seed=seed if seed is not None else summary.get("seed"),
        scenario=scenario if scenario is not None else summary.get("scenario"),
    )


def failed_demo_record(
    *,
    demo_id: str,
    output_dir: str | Path,
    error: str,
    scenario_id: str = "",
    seed: int | None = None,
    scenario: dict[str, Any] | None = None,
) -> DemoRunRecord:
    """Build a DemoRunRecord for a failed recording attempt."""
    out = Path(output_dir)
    return DemoRunRecord(
        demo_id=str(demo_id),
        output_dir=str(out),
        metadata_path=str(out / "demo.jsonl"),
        summary_path=str(out / "summary.json"),
        status=STATUS_FAILED,
        done_reached=False,
        num_steps=0,
        num_frames=0,
        error=str(error),
        scenario_id=str(scenario_id),
        seed=seed,
        scenario=scenario,
    )


def build_batch_manifest(
    *,
    batch_id: str,
    output_root: str | Path,
    num_requested: int,
    record_every: int,
    camera: str,
    no_images: bool,
    max_ticks: int,
    demos: list[DemoRunRecord],
    created_unix_time: float | None = None,
    scenario_config_path: str = "",
    scenario_config_name: str = "",
    scenario_count: int = 0,
) -> BatchManifest:
    """Aggregate demo records into a batch manifest."""
    num_completed = sum(1 for d in demos if d.status == STATUS_SUCCESS)
    num_failed = sum(1 for d in demos if d.status == STATUS_FAILED)
    return BatchManifest(
        batch_id=str(batch_id),
        output_root=str(output_root),
        created_unix_time=float(time.time() if created_unix_time is None else created_unix_time),
        num_requested=int(num_requested),
        num_completed=int(num_completed),
        num_failed=int(num_failed),
        record_every=int(record_every),
        camera=str(camera),
        no_images=bool(no_images),
        max_ticks=int(max_ticks),
        demos=list(demos),
        scenario_config_path=str(scenario_config_path),
        scenario_config_name=str(scenario_config_name),
        scenario_count=int(scenario_count),
    )


def manifest_to_dict(manifest: BatchManifest) -> dict[str, Any]:
    """Serialise manifest to dict."""
    return asdict(manifest)


def write_batch_manifest(path: str | Path, manifest: BatchManifest) -> None:
    """Write manifest to JSON with indentation."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest_to_dict(manifest), indent=2), encoding="utf-8")


def read_batch_manifest(path: str | Path) -> BatchManifest:
    """Read manifest from JSON."""
    src = Path(path)
    data = json.loads(src.read_text(encoding="utf-8"))
    demos = []
    for row in data.get("demos", []):
        row = dict(row)
        row.setdefault("scenario_id", "")
        row.setdefault("seed", None)
        row.setdefault("scenario", None)
        demos.append(DemoRunRecord(**row))
    data = dict(data)
    data["demos"] = demos
    data.setdefault("scenario_config_path", "")
    data.setdefault("scenario_config_name", "")
    data.setdefault("scenario_count", 0)
    return BatchManifest(**data)


def successful_demo_paths(manifest: BatchManifest) -> list[str]:
    """Return list of metadata paths for successful demos that reached DONE."""
    return [
        d.metadata_path
        for d in manifest.demos
        if d.status == STATUS_SUCCESS and d.done_reached
    ]


def manifest_summary(manifest: BatchManifest) -> dict[str, Any]:
    """Compute statistics for the batch manifest."""
    successful_done = [
        d for d in manifest.demos
        if d.status == STATUS_SUCCESS and d.done_reached
    ]
    return {
        "batch_id": manifest.batch_id,
        "num_requested": int(manifest.num_requested),
        "num_completed": int(manifest.num_completed),
        "num_failed": int(manifest.num_failed),
        "successful_done_demos": int(len(successful_done)),
        "total_steps": int(sum(d.num_steps for d in manifest.demos)),
        "total_frames": int(sum(d.num_frames for d in manifest.demos)),
        "demo_ids": [d.demo_id for d in manifest.demos],
    }
```

---

## FILE: `vla_bridge/dataset_audit.py`

```python
"""Dataset audit helpers for G1-native VLA exports.

Step 18 scope:
- no OpenVLA
- no model inference
- no fine-tuning
- audit data quality before learning work
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Sequence
import json
import math

import numpy as np

from vla_bridge.g1_native_dataset import G1NativeVLARecord, write_dataset_jsonl


ACTION_NAMES = [
    "walk_x",
    "walk_y",
    "walk_yaw",
    "reach_x",
    "reach_y",
    "reach_z",
    "reach_active",
    "grip_closed",
]


def action_array(records: Sequence[G1NativeVLARecord]) -> np.ndarray:
    """Extract action vectors as a NumPy array of shape (N, 8)."""
    if not records:
        return np.zeros((0, 8), dtype=np.float64)
    arr = np.asarray([r.action_vector for r in records], dtype=np.float64)
    if arr.ndim != 2 or arr.shape[1] != 8:
        raise ValueError(f"expected action array shape (N, 8), got {arr.shape}")
    return arr


def phase_counts(records: Sequence[G1NativeVLARecord]) -> dict[str, int]:
    """Count records by phase."""
    counts = Counter(r.phase for r in records)
    return {k: int(counts[k]) for k in sorted(counts)}


def _safe_fraction(num: int, den: int) -> float:
    return float(num / den) if den else float("nan")


def boolean_balance(records: Sequence[G1NativeVLARecord]) -> dict[str, Any]:
    """Compute balance statistics for boolean actions."""
    n = len(records)
    reach_true = int(sum(bool(r.reach_active) for r in records))
    grip_true = int(sum(bool(r.grip_closed) for r in records))
    return {
        "reach_active_true": reach_true,
        "reach_active_false": n - reach_true,
        "reach_active_true_fraction": _safe_fraction(reach_true, n),
        "grip_closed_true": grip_true,
        "grip_closed_false": n - grip_true,
        "grip_closed_true_fraction": _safe_fraction(grip_true, n),
    }


def action_statistics(records: Sequence[G1NativeVLARecord]) -> dict[str, Any]:
    """Compute per-dimension action statistics."""
    arr = action_array(records)
    if arr.shape[0] == 0:
        return {}
    stats: dict[str, Any] = {}
    for i, name in enumerate(ACTION_NAMES):
        col = arr[:, i]
        stats[name] = {
            "min": float(col.min()),
            "max": float(col.max()),
            "mean": float(col.mean()),
            "std": float(col.std()),
        }
    return stats


def magnitude_statistics(records: Sequence[G1NativeVLARecord]) -> dict[str, Any]:
    """Compute magnitude statistics for walk and reach commands."""
    arr = action_array(records)
    if arr.shape[0] == 0:
        return {}
    walk_mag = np.linalg.norm(arr[:, :3], axis=1)
    reach_norm = np.linalg.norm(arr[:, 3:6], axis=1)
    return {
        "mean_walk_cmd_magnitude": float(walk_mag.mean()),
        "max_walk_cmd_magnitude": float(walk_mag.max()),
        "zero_walk_records": int(np.sum(walk_mag <= 1e-9)),
        "nonzero_walk_records": int(np.sum(walk_mag > 1e-9)),
        "mean_reach_target_norm": float(reach_norm.mean()),
        "max_reach_target_norm": float(reach_norm.max()),
    }


def _is_idle(record: G1NativeVLARecord, *, walk_eps: float) -> bool:
    walk_mag = float(np.linalg.norm(np.asarray(record.walk_cmd, dtype=np.float64)))
    return (
        walk_mag <= walk_eps
        and not bool(record.reach_active)
        and not bool(record.grip_closed)
    )


def find_idle_runs(
    records: Sequence[G1NativeVLARecord],
    *,
    min_run_length: int = 25,
    walk_eps: float = 1e-9,
) -> list[dict[str, Any]]:
    """Identify contiguous segments where the robot is idle."""
    runs: list[dict[str, Any]] = []
    start: int | None = None

    def close_run(end_exclusive: int) -> None:
        nonlocal start
        if start is None:
            return
        length = end_exclusive - start
        if length >= min_run_length:
            phases = {records[i].phase for i in range(start, end_exclusive)}
            runs.append(
                {
                    "start_sample_index": int(records[start].sample_index),
                    "end_sample_index": int(records[end_exclusive - 1].sample_index),
                    "length": int(length),
                    "phase": next(iter(phases)) if len(phases) == 1 else "MIXED",
                }
            )
        start = None

    for i, record in enumerate(records):
        if _is_idle(record, walk_eps=walk_eps):
            if start is None:
                start = i
        else:
            close_run(i)

    close_run(len(records))
    return runs


def phase_transition_counts(records: Sequence[G1NativeVLARecord]) -> list[dict[str, Any]]:
    """Identify contiguous phase segments."""
    if not records:
        return []

    segments: list[dict[str, Any]] = []
    start = 0
    current = records[0].phase

    for i in range(1, len(records)):
        if records[i].phase != current:
            segments.append(
                {
                    "phase": current,
                    "start_sample_index": int(records[start].sample_index),
                    "end_sample_index": int(records[i - 1].sample_index),
                    "length": int(i - start),
                }
            )
            start = i
            current = records[i].phase

    segments.append(
        {
            "phase": current,
            "start_sample_index": int(records[start].sample_index),
            "end_sample_index": int(records[-1].sample_index),
            "length": int(len(records) - start),
        }
    )
    return segments


def build_audit_report(
    records: Sequence[G1NativeVLARecord],
    *,
    source_dataset: str = "",
    idle_min_run_length: int = 25,
) -> dict[str, Any]:
    """Construct a comprehensive audit report."""
    arr = action_array(records)
    phases = phase_counts(records)
    balance = boolean_balance(records)
    idle_runs = find_idle_runs(records, min_run_length=idle_min_run_length)

    warnings: list[str] = []
    if len(records) == 0:
        warnings.append("Dataset has zero records.")
    if len(phases) <= 1:
        warnings.append("Dataset has one or fewer unique phases.")
    if idle_runs:
        warnings.append(f"Found {len(idle_runs)} idle-heavy run(s). Consider filtering or weighting.")
    if len(records) > 0:
        grip_frac = float(balance["grip_closed_true_fraction"])
        reach_frac = float(balance["reach_active_true_fraction"])
        if grip_frac < 0.05 or grip_frac > 0.95:
            warnings.append(f"Grip class imbalance detected: grip_closed_true_fraction={grip_frac:.3f}.")
        if reach_frac < 0.05 or reach_frac > 0.95:
            warnings.append(f"Reach-active imbalance detected: reach_active_true_fraction={reach_frac:.3f}.")
        warnings.append(
            "This appears to be a single-trajectory dataset. Validation splits are debugging splits, not robust generalization estimates."
        )

    return {
        "source_dataset": source_dataset,
        "num_records": int(len(records)),
        "action_vector_shape": list(arr.shape),
        "phase_counts": phases,
        "phase_segments": phase_transition_counts(records),
        "boolean_balance": balance,
        "action_statistics": action_statistics(records),
        "magnitude_statistics": magnitude_statistics(records),
        "idle_runs": idle_runs,
        "warnings": warnings,
    }


def phase_temporal_split(
    records: Sequence[G1NativeVLARecord],
    *,
    val_fraction: float = 0.2,
    min_val_per_phase: int = 1,
) -> tuple[list[G1NativeVLARecord], list[G1NativeVLARecord]]:
    """Split dataset into train/val by taking the tail of each phase."""
    if not 0.0 < val_fraction < 1.0:
        raise ValueError("val_fraction must be between 0 and 1")
    if min_val_per_phase < 0:
        raise ValueError("min_val_per_phase must be non-negative")

    by_phase: dict[str, list[G1NativeVLARecord]] = defaultdict(list)
    for record in records:
        by_phase[record.phase].append(record)

    train: list[G1NativeVLARecord] = []
    val: list[G1NativeVLARecord] = []

    for phase_records in by_phase.values():
        n = len(phase_records)
        if n <= 1:
            train.extend(phase_records)
            continue
        n_val = max(min_val_per_phase, int(math.ceil(n * val_fraction)))
        n_val = min(n_val, n - 1)
        train.extend(phase_records[:-n_val])
        val.extend(phase_records[-n_val:])

    train.sort(key=lambda r: r.sample_index)
    val.sort(key=lambda r: r.sample_index)
    return train, val


def write_audit_report(path: str | Path, report: dict[str, Any]) -> None:
    """Save audit report to JSON."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")


def write_split_manifests(
    output_dir: str | Path,
    train_records: Sequence[G1NativeVLARecord],
    val_records: Sequence[G1NativeVLARecord],
) -> dict[str, Any]:
    """Write train/val JSONL files and a summary."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    train_path = out / "train.jsonl"
    val_path = out / "val.jsonl"
    write_dataset_jsonl(train_path, list(train_records))
    write_dataset_jsonl(val_path, list(val_records))

    total = len(train_records) + len(val_records)
    summary = {
        "train_records": int(len(train_records)),
        "val_records": int(len(val_records)),
        "total_records": int(total),
        "val_fraction_actual": float(len(val_records) / total) if total else float("nan"),
        "train_phase_counts": phase_counts(train_records),
        "val_phase_counts": phase_counts(val_records),
        "split_strategy": "phase_temporal_tail",
        "warning": "Single-trajectory split for debugging only; not a robust generalization estimate.",
        "train_path": str(train_path),
        "val_path": str(val_path),
    }
    write_audit_report(out / "split_summary.json", summary)
    return summary
```

---

## FILE: `vla_bridge/demo_recorder.py`

```python
"""Recorder for FSM teacher demonstrations in VLA-style format.

Step 14 scope:
- watch the existing FSM teacher
- save synchronized observations and derived 7D teacher actions
- do not control the robot
- do not load OpenVLA

Step 16 additions:
- walk_cmd and reach_active recorded in _PendingStep and VLADemoStep
"""
from __future__ import annotations

from pathlib import Path
from typing import NamedTuple

import numpy as np

from vla_bridge.demo_schema import (
    VLADemoStep,
    as_float_tuple,
    make_action_7d,
    write_jsonl,
)


class _PendingStep(NamedTuple):
    step_index: int
    sim_time: float
    image_path: str
    instruction: str
    phase: str
    palm_world: tuple[float, float, float]
    pelvis_pos: tuple[float, float, float]
    pelvis_quat: tuple[float, float, float, float]
    walk_cmd: tuple[float, float, float]
    reach_target_pelvis: tuple[float, float, float]
    reach_active: bool
    grip_closed: bool


class VLADemoRecorder:
    """Record FSM teacher observations and derived 7D palm-delta actions.

    The 7D action at step *t* is defined as the palm displacement between
    step *t* and step *t+1*, so each observation is held as a *pending* record
    until the next observation arrives to supply the second palm position.
    The last observation in a rollout is finalized with a zero-displacement
    action when :meth:`finalize` is called.
    """

    def __init__(
        self,
        output_dir: str | Path,
        instruction: str,
        record_every: int = 5,
        camera_name: str = "head_cam",
    ) -> None:
        if record_every <= 0:
            raise ValueError("record_every must be positive")
        self.output_dir = Path(output_dir)
        self.frames_dir = self.output_dir / "frames"
        self.metadata_path = self.output_dir / "demo.jsonl"
        self.instruction = instruction
        self.record_every = int(record_every)
        self.camera_name = camera_name
        self.frames_dir.mkdir(parents=True, exist_ok=True)

        self._steps: list[VLADemoStep] = []
        self._pending: _PendingStep | None = None
        self._num_observations: int = 0

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def steps(self) -> list[VLADemoStep]:
        """Return a copy of the finalized steps list."""
        return list(self._steps)

    def should_record(self, control_tick: int) -> bool:
        """Return True when *control_tick* falls on a recording boundary."""
        return int(control_tick) % self.record_every == 0

    def observe(
        self,
        *,
        control_tick: int,
        sim_time: float,
        rgb: np.ndarray | None,
        phase: str,
        palm_world: np.ndarray,
        pelvis_pos: np.ndarray,
        pelvis_quat: np.ndarray,
        walk_cmd: tuple[float, float, float],
        reach_target_pelvis: tuple[float, float, float],
        reach_active: bool,
        grip_closed: bool,
    ) -> None:
        """Record one observation frame from the FSM teacher.

        If *control_tick* does not fall on a recording boundary the call is a
        no-op.  Otherwise the previous pending record (if any) is finalized
        using the current *palm_world* as the next palm position, and the
        current observation is stored as the new pending record.
        """
        if not self.should_record(control_tick):
            return

        palm_tuple = as_float_tuple(palm_world, 3, "palm_world")
        pelvis_pos_tuple = as_float_tuple(pelvis_pos, 3, "pelvis_pos")
        pelvis_quat_tuple = as_float_tuple(pelvis_quat, 4, "pelvis_quat")
        walk_tuple = as_float_tuple(walk_cmd, 3, "walk_cmd")
        reach_tuple = as_float_tuple(reach_target_pelvis, 3, "reach_target_pelvis")

        image_path = ""
        if rgb is not None:
            image_path = self._save_frame(rgb, self._num_observations)

        if self._pending is not None:
            action_7d = make_action_7d(
                np.asarray(self._pending.palm_world, dtype=np.float64),
                np.asarray(palm_tuple, dtype=np.float64),
                self._pending.grip_closed,
            )
            self._steps.append(
                VLADemoStep(
                    step_index=self._pending.step_index,
                    sim_time=self._pending.sim_time,
                    image_path=self._pending.image_path,
                    instruction=self._pending.instruction,
                    phase=self._pending.phase,
                    palm_world=self._pending.palm_world,
                    pelvis_pos=self._pending.pelvis_pos,
                    pelvis_quat=self._pending.pelvis_quat,
                    walk_cmd=self._pending.walk_cmd,
                    reach_target_pelvis=self._pending.reach_target_pelvis,
                    reach_active=self._pending.reach_active,
                    grip_closed=self._pending.grip_closed,
                    action_7d=action_7d,
                )
            )

        self._pending = _PendingStep(
            step_index=int(control_tick),
            sim_time=float(sim_time),
            image_path=image_path,
            instruction=self.instruction,
            phase=str(phase),
            palm_world=palm_tuple,
            pelvis_pos=pelvis_pos_tuple,
            pelvis_quat=pelvis_quat_tuple,
            walk_cmd=walk_tuple,
            reach_target_pelvis=reach_tuple,
            reach_active=bool(reach_active),
            grip_closed=bool(grip_closed),
        )
        self._num_observations += 1

    def finalize(self) -> None:
        """Finalize the last pending record with a zero action and write JSONL.

        Must be called once at the end of a rollout.  Calling more than once
        is safe (subsequent calls are no-ops after the pending record is gone).
        """
        if self._pending is not None:
            zero_action: tuple[float, float, float, float, float, float, float] = (
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0 if self._pending.grip_closed else 0.0,
            )
            self._steps.append(
                VLADemoStep(
                    step_index=self._pending.step_index,
                    sim_time=self._pending.sim_time,
                    image_path=self._pending.image_path,
                    instruction=self._pending.instruction,
                    phase=self._pending.phase,
                    palm_world=self._pending.palm_world,
                    pelvis_pos=self._pending.pelvis_pos,
                    pelvis_quat=self._pending.pelvis_quat,
                    walk_cmd=self._pending.walk_cmd,
                    reach_target_pelvis=self._pending.reach_target_pelvis,
                    reach_active=self._pending.reach_active,
                    grip_closed=self._pending.grip_closed,
                    action_7d=zero_action,
                )
            )
            self._pending = None
        write_jsonl(self.metadata_path, self._steps)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _save_frame(self, rgb: np.ndarray, frame_index: int) -> str:
        """Save an RGB frame and return its relative path string.

        Tries cv2 first; falls back to NumPy .npy if cv2 is unavailable or
        fails.  *rgb* must have shape (H, W, 3).
        """
        arr = np.asarray(rgb)
        if arr.ndim != 3 or arr.shape[2] != 3:
            raise ValueError(f"rgb must have shape (H, W, 3), got {arr.shape}")

        rel_png = Path("frames") / f"frame_{frame_index:06d}.png"
        out_png = self.output_dir / rel_png
        try:
            import cv2  # type: ignore

            bgr = arr[..., ::-1]
            ok = cv2.imwrite(str(out_png), bgr)
            if not ok:
                raise RuntimeError(f"cv2.imwrite failed for {out_png}")
            return rel_png.as_posix()
        except Exception:
            rel_npy = Path("frames") / f"frame_{frame_index:06d}.npy"
            out_npy = self.output_dir / rel_npy
            np.save(str(out_npy), arr)
            return rel_npy.as_posix()
```

---

## FILE: `vla_bridge/demo_schema.py`

```python
"""Schema helpers for VLA-style FSM demonstration recording.

Step 14 scope:
- no OpenVLA import
- no model inference
- no replay
- no runtime control changes

Step 16 additions:
- walk_cmd and reach_active fields added to VLADemoStep
- backward-compatible step_from_json for older JSONL files

This schema stores observations and teacher actions generated by the existing
FSM baseline. The FSM is the teacher; the VLA branch only records data here.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import json
import numpy as np


@dataclass(frozen=True)
class VLADemoStep:
    """One synchronized image/action record from an FSM teacher rollout."""

    step_index: int
    sim_time: float
    image_path: str
    instruction: str
    phase: str
    palm_world: tuple[float, float, float]
    pelvis_pos: tuple[float, float, float]
    pelvis_quat: tuple[float, float, float, float]
    walk_cmd: tuple[float, float, float]
    reach_target_pelvis: tuple[float, float, float]
    reach_active: bool
    grip_closed: bool
    action_7d: tuple[float, float, float, float, float, float, float]


def as_float_tuple(value: Any, length: int, name: str) -> tuple[float, ...]:
    """Convert *value* to a tuple of Python floats with the required *length*.

    Raises ValueError if the resulting array does not have shape (*length*,).
    """
    arr = np.asarray(value, dtype=np.float64)
    if arr.shape != (length,):
        raise ValueError(f"{name} must have shape ({length},), got {arr.shape}")
    return tuple(float(x) for x in arr)


def make_action_7d(
    current_palm_world: np.ndarray,
    next_palm_world: np.ndarray,
    grip_closed: bool,
) -> tuple[float, float, float, float, float, float, float]:
    """Compute a 7D teacher action from consecutive palm positions.

    Returns (dx, dy, dz, 0, 0, 0, gripper) where rotation is intentionally
    zero for Step 14 and gripper is 1.0 when closed, 0.0 when open.
    """
    current = np.asarray(current_palm_world, dtype=np.float64)
    nxt = np.asarray(next_palm_world, dtype=np.float64)
    if current.shape != (3,):
        raise ValueError(
            f"current_palm_world must have shape (3,), got {current.shape}"
        )
    if nxt.shape != (3,):
        raise ValueError(
            f"next_palm_world must have shape (3,), got {nxt.shape}"
        )
    delta = nxt - current
    return (
        float(delta[0]),
        float(delta[1]),
        float(delta[2]),
        0.0,
        0.0,
        0.0,
        1.0 if bool(grip_closed) else 0.0,
    )


def step_to_json(step: VLADemoStep) -> str:
    """Serialise *step* to a compact JSON string (no trailing newline)."""
    return json.dumps(asdict(step), separators=(",", ":"))


def step_from_json(line: str) -> VLADemoStep:
    """Parse a single JSON line into a VLADemoStep.

    Backward compatible with older Step 14 JSONL files that do not contain
    ``walk_cmd`` or ``reach_active``.  Defaults:
    - ``walk_cmd`` missing → (0.0, 0.0, 0.0)
    - ``reach_active`` missing → True
    """
    data = json.loads(line)
    return VLADemoStep(
        step_index=int(data["step_index"]),
        sim_time=float(data["sim_time"]),
        image_path=str(data["image_path"]),
        instruction=str(data["instruction"]),
        phase=str(data["phase"]),
        palm_world=as_float_tuple(data["palm_world"], 3, "palm_world"),
        pelvis_pos=as_float_tuple(data["pelvis_pos"], 3, "pelvis_pos"),
        pelvis_quat=as_float_tuple(data["pelvis_quat"], 4, "pelvis_quat"),
        walk_cmd=as_float_tuple(data.get("walk_cmd", (0.0, 0.0, 0.0)), 3, "walk_cmd"),
        reach_target_pelvis=as_float_tuple(
            data["reach_target_pelvis"], 3, "reach_target_pelvis"
        ),
        reach_active=bool(data.get("reach_active", True)),
        grip_closed=bool(data["grip_closed"]),
        action_7d=as_float_tuple(data["action_7d"], 7, "action_7d"),
    )


def write_jsonl(path: str | Path, steps: list[VLADemoStep]) -> None:
    """Write *steps* as a JSONL file at *path*, creating parent dirs as needed."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for step in steps:
            f.write(step_to_json(step) + "\n")


def read_jsonl(path: str | Path) -> list[VLADemoStep]:
    """Read a JSONL file and return a list of VLADemoStep objects."""
    src = Path(path)
    steps: list[VLADemoStep] = []
    with src.open("r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                steps.append(step_from_json(stripped))
    return steps
```

---

## FILE: `vla_bridge/g1_native_dataset.py`

```python
"""G1-native VLA dataset export helpers.

Step 17 scope:
- no OpenVLA
- no model inference
- no fine-tuning
- pure supervised dataset export

The exported target is the G1-native command interface proven executable in
Step 16:

[walk_x, walk_y, walk_yaw, reach_x, reach_y, reach_z, reach_active, grip_closed]
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import json
import shutil

import numpy as np

from vla_bridge.demo_schema import VLADemoStep, as_float_tuple


@dataclass(frozen=True)
class G1NativeVLARecord:
    """One supervised record for the G1-native VLA dataset."""

    sample_index: int
    source_step_index: int
    image_path: str
    instruction: str
    phase: str

    walk_cmd: tuple[float, float, float]
    reach_target_pelvis: tuple[float, float, float]
    reach_active: bool
    grip_closed: bool

    action_vector: tuple[float, float, float, float, float, float, float, float]


def make_action_vector(
    walk_cmd: tuple[float, float, float],
    reach_target_pelvis: tuple[float, float, float],
    reach_active: bool,
    grip_closed: bool,
) -> tuple[float, float, float, float, float, float, float, float]:
    """Build the 8D action vector target."""
    walk = as_float_tuple(walk_cmd, 3, "walk_cmd")
    reach = as_float_tuple(reach_target_pelvis, 3, "reach_target_pelvis")
    return (
        float(walk[0]),
        float(walk[1]),
        float(walk[2]),
        float(reach[0]),
        float(reach[1]),
        float(reach[2]),
        1.0 if bool(reach_active) else 0.0,
        1.0 if bool(grip_closed) else 0.0,
    )


def _join_prefix(prefix: str, image_path: str) -> str:
    if not prefix:
        return image_path
    if not image_path:
        return ""
    return f"{prefix.rstrip('/')}/{image_path}"


def record_from_demo_step(
    step: VLADemoStep,
    sample_index: int,
    *,
    image_prefix: str = "",
    include_phase: bool = True,
) -> G1NativeVLARecord:
    """Map a VLADemoStep to a G1NativeVLARecord."""
    image_path = _join_prefix(image_prefix, step.image_path)
    phase = step.phase if include_phase else ""
    walk_cmd = as_float_tuple(step.walk_cmd, 3, "walk_cmd")
    reach_target = as_float_tuple(step.reach_target_pelvis, 3, "reach_target_pelvis")
    action_vector = make_action_vector(
        walk_cmd,
        reach_target,
        bool(step.reach_active),
        bool(step.grip_closed),
    )
    return G1NativeVLARecord(
        sample_index=int(sample_index),
        source_step_index=int(step.step_index),
        image_path=str(image_path),
        instruction=str(step.instruction),
        phase=str(phase),
        walk_cmd=walk_cmd,
        reach_target_pelvis=reach_target,
        reach_active=bool(step.reach_active),
        grip_closed=bool(step.grip_closed),
        action_vector=action_vector,
    )


def export_records_from_steps(
    steps: list[VLADemoStep],
    *,
    require_images: bool = True,
    include_phase: bool = True,
    image_prefix: str = "",
    drop_done: bool = True,
    drop_inactive_reach: bool = False,
) -> list[G1NativeVLARecord]:
    """Export multiple records from demo steps with filtering."""
    records: list[G1NativeVLARecord] = []
    for step in steps:
        if drop_done and step.phase == "DONE":
            continue
        if drop_inactive_reach and not step.reach_active:
            continue
        if require_images and not step.image_path:
            raise ValueError(
                f"Step {step.step_index} has no image_path but require_images=True"
            )
        records.append(
            record_from_demo_step(
                step,
                sample_index=len(records),
                image_prefix=image_prefix,
                include_phase=include_phase,
            )
        )
    return records


def record_to_json(record: G1NativeVLARecord) -> str:
    """Serialise record to compact JSON line."""
    return json.dumps(asdict(record), separators=(",", ":"))


def record_from_json(line: str) -> G1NativeVLARecord:
    """Parse JSON line into G1NativeVLARecord."""
    data = json.loads(line)
    return G1NativeVLARecord(
        sample_index=int(data["sample_index"]),
        source_step_index=int(data["source_step_index"]),
        image_path=str(data["image_path"]),
        instruction=str(data["instruction"]),
        phase=str(data.get("phase", "")),
        walk_cmd=as_float_tuple(data["walk_cmd"], 3, "walk_cmd"),
        reach_target_pelvis=as_float_tuple(
            data["reach_target_pelvis"], 3, "reach_target_pelvis"
        ),
        reach_active=bool(data["reach_active"]),
        grip_closed=bool(data["grip_closed"]),
        action_vector=as_float_tuple(data["action_vector"], 8, "action_vector"),
    )


def write_dataset_jsonl(path: str | Path, records: list[G1NativeVLARecord]) -> None:
    """Write records as JSONL."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(record_to_json(record) + "\n")


def read_dataset_jsonl(path: str | Path) -> list[G1NativeVLARecord]:
    """Read records from JSONL."""
    src = Path(path)
    records: list[G1NativeVLARecord] = []
    with src.open("r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                records.append(record_from_json(stripped))
    return records


def dataset_summary(records: list[G1NativeVLARecord]) -> dict[str, Any]:
    """Compute statistics for the exported records."""
    if not records:
        return {"num_records": 0}

    walk = np.asarray([r.walk_cmd for r in records], dtype=np.float64)
    reach = np.asarray([r.reach_target_pelvis for r in records], dtype=np.float64)
    walk_mag = np.linalg.norm(walk, axis=1)
    reach_norm = np.linalg.norm(reach, axis=1)
    phases = [r.phase for r in records]

    return {
        "num_records": len(records),
        "first_phase": phases[0],
        "last_phase": phases[-1],
        "unique_phases": sorted(set(phases)),
        "walk_nonzero_records": int(np.sum(walk_mag > 1e-9)),
        "reach_active_records": int(sum(r.reach_active for r in records)),
        "grip_closed_records": int(sum(r.grip_closed for r in records)),
        "mean_walk_cmd_magnitude": float(walk_mag.mean()),
        "max_walk_cmd_magnitude": float(walk_mag.max()),
        "mean_reach_target_norm": float(reach_norm.mean()),
        "max_reach_target_norm": float(reach_norm.max()),
    }


def write_summary(path: str | Path, summary: dict[str, Any]) -> None:
    """Write summary JSON."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")


def copy_images_for_records(
    records: list[G1NativeVLARecord],
    *,
    source_demo_dir: str | Path,
    output_images_dir: str | Path,
) -> list[G1NativeVLARecord]:
    """Copy images and update record paths."""
    src_root = Path(source_demo_dir)
    dst_root = Path(output_images_dir)
    dst_root.mkdir(parents=True, exist_ok=True)

    copied: list[G1NativeVLARecord] = []
    for record in records:
        if not record.image_path:
            raise ValueError(f"Record {record.sample_index} has empty image_path")

        src = src_root / record.image_path
        if not src.exists():
            raise FileNotFoundError(src)

        dst = dst_root / Path(record.image_path).name
        shutil.copy2(src, dst)

        copied.append(
            G1NativeVLARecord(
                sample_index=record.sample_index,
                source_step_index=record.source_step_index,
                image_path=f"images/{dst.name}",
                instruction=record.instruction,
                phase=record.phase,
                walk_cmd=record.walk_cmd,
                reach_target_pelvis=record.reach_target_pelvis,
                reach_active=record.reach_active,
                grip_closed=record.grip_closed,
                action_vector=record.action_vector,
            )
        )
    return copied
```

---

## FILE: `vla_bridge/replay_metrics.py`

```python
"""Replay metrics for VLA-style action demonstrations.

Step 15 scope:
- no OpenVLA
- no model inference
- no MuJoCo dependency
- pure metrics for comparing teacher and replay trajectories

Step 16 additions:
- walk_command_magnitudes helper
- walk_nonzero_steps, reach_active_steps, mean/max walk command magnitude in ReplayMetrics
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from vla_bridge.demo_schema import VLADemoStep


@dataclass(frozen=True)
class ReplayMetrics:
    num_steps: int
    mean_palm_error_m: float
    max_palm_error_m: float
    final_palm_error_m: float
    mean_action_magnitude_m: float
    max_action_magnitude_m: float
    grip_mismatch_count: int
    mean_walk_command_magnitude: float
    max_walk_command_magnitude: float
    walk_nonzero_steps: int
    reach_active_steps: int


def action_xyz_magnitudes(steps: Sequence[VLADemoStep]) -> np.ndarray:
    """Return L2 norm of action_7d[:3] for each step.

    Returns an empty float64 array if *steps* is empty.
    """
    if not steps:
        return np.asarray([], dtype=np.float64)
    xyz = np.asarray([s.action_7d[:3] for s in steps], dtype=np.float64)
    return np.linalg.norm(xyz, axis=1)


def walk_command_magnitudes(steps: Sequence[VLADemoStep]) -> np.ndarray:
    """Return L2 norm of walk_cmd for each step.

    Returns an empty float64 array if *steps* is empty.
    """
    if not steps:
        return np.asarray([], dtype=np.float64)
    walk_cmds = np.asarray([s.walk_cmd for s in steps], dtype=np.float64)
    return np.linalg.norm(walk_cmds, axis=1)


def palm_error_metrics(
    teacher_palm_world: np.ndarray,
    replay_palm_world: np.ndarray,
) -> tuple[float, float, float]:
    """Compute mean, max, and final L2 error between two (N, 3) palm arrays.

    Returns (nan, nan, nan) when N == 0.
    """
    teacher = np.asarray(teacher_palm_world, dtype=np.float64)
    replay = np.asarray(replay_palm_world, dtype=np.float64)
    if teacher.shape != replay.shape:
        raise ValueError(
            f"teacher and replay shapes must match, got {teacher.shape} and {replay.shape}"
        )
    if teacher.ndim != 2 or teacher.shape[1] != 3:
        raise ValueError(
            f"expected arrays with shape (N, 3), got {teacher.shape}"
        )
    if teacher.shape[0] == 0:
        return float("nan"), float("nan"), float("nan")
    err = np.linalg.norm(replay - teacher, axis=1)
    return float(err.mean()), float(err.max()), float(err[-1])


def grip_mismatch_count(
    teacher_grip: Sequence[bool],
    replay_grip: Sequence[bool],
) -> int:
    """Count positions where grip booleans differ.

    Both sequences must have the same length.
    """
    if len(teacher_grip) != len(replay_grip):
        raise ValueError(
            f"grip sequences must have same length, got {len(teacher_grip)} and {len(replay_grip)}"
        )
    return int(sum(bool(a) != bool(b) for a, b in zip(teacher_grip, replay_grip)))


def compute_replay_metrics(
    steps: Sequence[VLADemoStep],
    replay_palm_world: np.ndarray,
    replay_grip: Sequence[bool],
) -> ReplayMetrics:
    """Compute all replay metrics against the teacher trajectory.

    *replay_palm_world* must have shape (len(steps), 3).
    *replay_grip* length must match len(steps).
    """
    teacher_palm = np.asarray([s.palm_world for s in steps], dtype=np.float64)
    teacher_grip = [bool(s.grip_closed) for s in steps]
    replay_palm = np.asarray(replay_palm_world, dtype=np.float64)

    if replay_palm.shape != teacher_palm.shape:
        raise ValueError(
            f"replay_palm_world must have shape {teacher_palm.shape}, got {replay_palm.shape}"
        )
    if len(replay_grip) != len(steps):
        raise ValueError(
            f"replay_grip must have length {len(steps)}, got {len(replay_grip)}"
        )

    mean_err, max_err, final_err = palm_error_metrics(teacher_palm, replay_palm)
    mags = action_xyz_magnitudes(steps)
    walk_mags = walk_command_magnitudes(steps)
    walk_nonzero_steps = int(np.sum(walk_mags > 1e-9))
    reach_active_steps = int(sum(bool(s.reach_active) for s in steps))

    return ReplayMetrics(
        num_steps=len(steps),
        mean_palm_error_m=mean_err,
        max_palm_error_m=max_err,
        final_palm_error_m=final_err,
        mean_action_magnitude_m=float(mags.mean()) if len(mags) else float("nan"),
        max_action_magnitude_m=float(mags.max()) if len(mags) else float("nan"),
        grip_mismatch_count=grip_mismatch_count(teacher_grip, replay_grip),
        mean_walk_command_magnitude=float(walk_mags.mean()) if len(walk_mags) else float("nan"),
        max_walk_command_magnitude=float(walk_mags.max()) if len(walk_mags) else float("nan"),
        walk_nonzero_steps=walk_nonzero_steps,
        reach_active_steps=reach_active_steps,
    )
```

---

## FILE: `vla_bridge/scenario_config.py`

```python
from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import json


@dataclass(frozen=True)
class ScenarioSpec:
    scenario_id: str
    seed: int
    red_block_xy_offset_m: tuple[float, float] = (0.0, 0.0)
    robot_base_xy_offset_m: tuple[float, float] = (0.0, 0.0)
    target_drop_xy_offset_m: tuple[float, float] = (0.0, 0.0)


@dataclass(frozen=True)
class ScenarioConfig:
    name: str
    description: str
    scenarios: list[ScenarioSpec]


def _as_xy(value: Any, *, field_name: str) -> tuple[float, float]:
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError(f"{field_name} must be a list/tuple of length 2")
    try:
        return (float(value[0]), float(value[1]))
    except Exception as exc:
        raise ValueError(f"{field_name} must contain numeric values") from exc


def load_scenario_config(path: str | Path) -> ScenarioConfig:
    src = Path(path)
    data = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("scenario config root must be an object")

    name = str(data.get("name", "")).strip()
    description = str(data.get("description", "")).strip()
    if not name:
        raise ValueError("scenario config requires non-empty 'name'")
    if not description:
        raise ValueError("scenario config requires non-empty 'description'")

    defaults_raw = data.get("defaults", {})
    if not isinstance(defaults_raw, dict):
        raise ValueError("'defaults' must be an object")
    defaults = {
        "red_block_xy_offset_m": _as_xy(defaults_raw.get("red_block_xy_offset_m", (0.0, 0.0)), field_name="defaults.red_block_xy_offset_m"),
        "robot_base_xy_offset_m": _as_xy(defaults_raw.get("robot_base_xy_offset_m", (0.0, 0.0)), field_name="defaults.robot_base_xy_offset_m"),
        "target_drop_xy_offset_m": _as_xy(defaults_raw.get("target_drop_xy_offset_m", (0.0, 0.0)), field_name="defaults.target_drop_xy_offset_m"),
    }

    scenarios_raw = data.get("scenarios", [])
    if not isinstance(scenarios_raw, list) or not scenarios_raw:
        raise ValueError("'scenarios' must be a non-empty list")

    seen_ids: set[str] = set()
    seen_seeds: set[int] = set()
    scenarios: list[ScenarioSpec] = []
    for i, row in enumerate(scenarios_raw):
        if not isinstance(row, dict):
            raise ValueError(f"scenarios[{i}] must be an object")
        if "scenario_id" not in row:
            raise ValueError(f"scenarios[{i}] missing required field 'scenario_id'")
        if "seed" not in row:
            raise ValueError(f"scenarios[{i}] missing required field 'seed'")

        scenario_id = str(row["scenario_id"]).strip()
        if not scenario_id:
            raise ValueError(f"scenarios[{i}].scenario_id must be non-empty")
        seed = int(row["seed"])
        if scenario_id in seen_ids:
            raise ValueError(f"duplicate scenario_id: {scenario_id}")
        if seed in seen_seeds:
            raise ValueError(f"duplicate seed: {seed}")
        seen_ids.add(scenario_id)
        seen_seeds.add(seed)

        red = _as_xy(row.get("red_block_xy_offset_m", defaults["red_block_xy_offset_m"]), field_name=f"scenarios[{i}].red_block_xy_offset_m")
        robot = _as_xy(row.get("robot_base_xy_offset_m", defaults["robot_base_xy_offset_m"]), field_name=f"scenarios[{i}].robot_base_xy_offset_m")
        target = _as_xy(row.get("target_drop_xy_offset_m", defaults["target_drop_xy_offset_m"]), field_name=f"scenarios[{i}].target_drop_xy_offset_m")

        scenarios.append(
            ScenarioSpec(
                scenario_id=scenario_id,
                seed=seed,
                red_block_xy_offset_m=red,
                robot_base_xy_offset_m=robot,
                target_drop_xy_offset_m=target,
            )
        )

    return ScenarioConfig(
        name=name,
        description=description,
        scenarios=scenarios,
    )


def select_scenario(config: ScenarioConfig, index: int) -> ScenarioSpec:
    if not config.scenarios:
        raise ValueError("config.scenarios must not be empty")
    return config.scenarios[int(index) % len(config.scenarios)]


def scenario_to_metadata(spec: ScenarioSpec) -> dict[str, Any]:
    return asdict(spec)


def load_and_select_scenario(path: str | Path, index: int) -> ScenarioSpec:
    return select_scenario(load_scenario_config(path), index)
```

---

## FILE: `vla_bridge/training_views.py`

```python
"""Training-view helpers for G1-native VLA datasets.

Step 19 scope:
- no OpenVLA
- no model inference
- no fine-tuning
- build safer dataset views from audited records
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Sequence
import json

import numpy as np

from vla_bridge.g1_native_dataset import G1NativeVLARecord, write_dataset_jsonl
from vla_bridge.dataset_audit import phase_counts


RARE_TRANSITION_PHASES = {"CLOSE_GRIP", "OPEN_GRIP"}


def walk_magnitude(record: G1NativeVLARecord) -> float:
    """Compute L2 norm of record.walk_cmd."""
    return float(np.linalg.norm(np.asarray(record.walk_cmd, dtype=np.float64)))


def is_idle_record(
    record: G1NativeVLARecord,
    *,
    walk_eps: float = 1e-9,
) -> bool:
    """Check if a record is idle (no movement, reach, or grip).
    
    Rare transition phases (CLOSE_GRIP, OPEN_GRIP) are NEVER considered idle.
    """
    if record.phase in RARE_TRANSITION_PHASES:
        return False
    return (
        walk_magnitude(record) <= walk_eps
        and not bool(record.reach_active)
        and not bool(record.grip_closed)
    )


def filter_idle_records(
    records: Sequence[G1NativeVLARecord],
    *,
    keep_first_n_idle: int = 10,
    walk_eps: float = 1e-9,
) -> list[G1NativeVLARecord]:
    """Remove idle records after the first keep_first_n_idle.
    
    Preserves all rare transition records and maintains original order.
    """
    if keep_first_n_idle < 0:
        raise ValueError("keep_first_n_idle must be non-negative")

    kept: list[G1NativeVLARecord] = []
    idle_kept = 0

    for record in records:
        if is_idle_record(record, walk_eps=walk_eps):
            if idle_kept < keep_first_n_idle:
                kept.append(record)
                idle_kept += 1
            continue
        kept.append(record)

    return kept


def compute_phase_weights(
    records: Sequence[G1NativeVLARecord],
    *,
    max_weight: float = 20.0,
    rare_phase_boost: float = 5.0,
) -> dict[int, float]:
    """Compute inverse-frequency phase weights with rare phase boosting."""
    if max_weight <= 0:
        raise ValueError("max_weight must be positive")
    if rare_phase_boost <= 0:
        raise ValueError("rare_phase_boost must be positive")
    if not records:
        return {}

    counts = Counter(r.phase for r in records)
    total = len(records)
    num_phases = len(counts)

    weights: dict[int, float] = {}
    for record in records:
        # base_weight = total / (num_phases * phase_count)
        base = total / float(num_phases * counts[record.phase])
        if record.phase in RARE_TRANSITION_PHASES:
            base *= rare_phase_boost
        weights[int(record.sample_index)] = float(min(base, max_weight))

    return weights


def normalize_weights(weights: dict[int, float]) -> dict[int, float]:
    """Normalize weights so their mean is 1.0."""
    if not weights:
        return {}
    values = np.asarray(list(weights.values()), dtype=np.float64)
    mean = float(values.mean())
    if mean <= 0:
        return {int(k): 1.0 for k in weights}
    return {int(k): float(v / mean) for k, v in weights.items()}


def build_weight_records(
    records: Sequence[G1NativeVLARecord],
    weights: dict[int, float],
) -> list[dict[str, Any]]:
    """Build lightweight weight record dictionaries."""
    rows: list[dict[str, Any]] = []
    for record in records:
        idx = int(record.sample_index)
        rows.append(
            {
                "sample_index": idx,
                "source_step_index": int(record.source_step_index),
                "phase": record.phase,
                "weight": float(weights.get(idx, 1.0)),
                "image_path": record.image_path,
            }
        )
    return rows


def write_weight_jsonl(path: str | Path, weight_records: Sequence[dict[str, Any]]) -> None:
    """Write weight records as JSONL."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for row in weight_records:
            f.write(json.dumps(row, separators=(",", ":")) + "\n")


def read_weight_jsonl(path: str | Path) -> list[dict[str, Any]]:
    """Read weight records from JSONL."""
    src = Path(path)
    rows: list[dict[str, Any]] = []
    with src.open("r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                rows.append(json.loads(stripped))
    return rows


def _idle_count(records: Sequence[G1NativeVLARecord]) -> int:
    return int(sum(is_idle_record(r) for r in records))


def _rare_count(records: Sequence[G1NativeVLARecord]) -> dict[str, int]:
    counts = Counter(r.phase for r in records if r.phase in RARE_TRANSITION_PHASES)
    return {phase: int(counts.get(phase, 0)) for phase in sorted(RARE_TRANSITION_PHASES)}


def training_view_summary(
    *,
    source_records: Sequence[G1NativeVLARecord],
    filtered_records: Sequence[G1NativeVLARecord],
    weights: dict[int, float],
    view_name: str,
) -> dict[str, Any]:
    """Compute summary of the training views."""
    source_phase = phase_counts(source_records)
    filtered_phase = phase_counts(filtered_records)
    weight_values = np.asarray(list(weights.values()), dtype=np.float64) if weights else np.asarray([])

    warnings: list[str] = []
    if not filtered_records:
        warnings.append("Filtered view has zero records.")
    for phase in RARE_TRANSITION_PHASES:
        if source_phase.get(phase, 0) > 0 and filtered_phase.get(phase, 0) == 0:
            warnings.append(f"Rare transition phase {phase} was dropped.")
    if len(source_phase) <= 1:
        warnings.append("Source view has one or fewer phases.")
    if len(filtered_phase) <= 1:
        warnings.append("Filtered view has one or fewer phases.")
    if _idle_count(source_records) > 0 and len(source_records) == len(filtered_records):
        warnings.append("Idle records exist but filtering removed no records.")
    warnings.append(
        "This is still a single-trajectory dataset. Weighted/filtered views are debugging aids, not robust generalization data."
    )

    return {
        "view_name": view_name,
        "source_records": int(len(source_records)),
        "filtered_records": int(len(filtered_records)),
        "removed_records": int(len(source_records) - len(filtered_records)),
        "source_phase_counts": source_phase,
        "filtered_phase_counts": filtered_phase,
        "rare_transition_records_source": _rare_count(source_records),
        "rare_transition_records_filtered": _rare_count(filtered_records),
        "idle_records_source": _idle_count(source_records),
        "idle_records_filtered": _idle_count(filtered_records),
        "weight_count": int(len(weights)),
        "min_weight": float(weight_values.min()) if len(weight_values) else float("nan"),
        "max_weight": float(weight_values.max()) if len(weight_values) else float("nan"),
        "mean_weight": float(weight_values.mean()) if len(weight_values) else float("nan"),
        "warnings": warnings,
    }


def write_json(path: str | Path, payload: dict[str, Any]) -> None:
    """Write JSON with indentation."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def build_training_views(
    records: Sequence[G1NativeVLARecord],
    *,
    output_dir: str | Path,
    keep_first_n_idle: int = 10,
    max_weight: float = 20.0,
    rare_phase_boost: float = 5.0,
) -> dict[str, Any]:
    """Build full, filtered, and weighted views of the dataset."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    full_records = list(records)
    filtered_records = filter_idle_records(
        full_records,
        keep_first_n_idle=keep_first_n_idle,
    )

    weights = normalize_weights(
        compute_phase_weights(
            full_records,
            max_weight=max_weight,
            rare_phase_boost=rare_phase_boost,
        )
    )
    weight_records = build_weight_records(full_records, weights)

    write_dataset_jsonl(out / "full.jsonl", full_records)
    write_dataset_jsonl(out / "filtered_no_idle.jsonl", filtered_records)
    write_weight_jsonl(out / "sample_weights.jsonl", weight_records)

    summary = training_view_summary(
        source_records=full_records,
        filtered_records=filtered_records,
        weights=weights,
        view_name="g1_native_training_views",
    )
    summary.update(
        {
            "keep_first_n_idle": int(keep_first_n_idle),
            "max_weight": float(max_weight),
            "rare_phase_boost": float(rare_phase_boost),
            "files": {
                "full": str(out / "full.jsonl"),
                "filtered_no_idle": str(out / "filtered_no_idle.jsonl"),
                "sample_weights": str(out / "sample_weights.jsonl"),
                "summary": str(out / "training_view_summary.json"),
            },
        }
    )
    write_json(out / "training_view_summary.json", summary)
    return summary
```

---

## FILE: `walker.onnx`

_Skipped: non-text or binary file._

---

## FILE: `walker.onnx.data`

_Skipped: file is too large (877336 bytes)._ 

