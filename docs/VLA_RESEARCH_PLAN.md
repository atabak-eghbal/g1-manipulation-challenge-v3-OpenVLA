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
