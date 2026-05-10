# G1 Pick & Place Challenge — Autonomous Baseline + VLA Roadmap

This repository contains my engineering solution and research branch for the Lucky Robots Unitree G1 pick-and-place challenge. The original challenge provided a manual keyboard-controlled MuJoCo demo. This repo turns it into a modular autonomous system with FSM control, scripted teachers, VLA-style data tooling, grasp experiments, replay/evaluation utilities, and a working hybrid contact-guided grasp.

**Technical Case Study:** [Blog](https://atabak-eghbal.github.io/lucky-robots-g1-pick-place-case-study/index.html)  
**VLA Roadmap:** [Roadmap](https://atabak-eghbal.github.io/lucky-robots-g1-pick-place-case-study/pages/vla-roadmap.html)  
**Latest Demo Video:** [Hybrid contact-guided grasp](https://www.youtube.com/watch?v=rhKuY6O_H5o)

## Latest Demo

[![Latest hybrid contact-guided grasp demo](https://img.youtube.com/vi/rhKuY6O_H5o/hqdefault.jpg)](https://www.youtube.com/watch?v=rhKuY6O_H5o)

The latest working result uses a hybrid contact-guided grasp. The robot first performs a staged contact/cage-style probe around the red cylinder, then switches to kinematic attachment during transport to prevent slipping. This is intentionally documented as a simulation-engineering compromise, not a pure physical dexterous grasp.

## Video Evidence

| Work | What it shows | Link |
|---|---|---|
| Work 1 — FSM baseline | Original autonomous FSM/kinematic pick-and-place baseline | https://youtu.be/4FKgn35iU-Y?si=TiO-xRAxPQBCLsaj |
| Work 2 — Scripted keyboard teacher | Automated keyboard-style teacher experiment | https://youtu.be/Lw88uj7FiFo?si=Bw5gZGO6kQ3KBkY4 |
| Work 3 — Physical grasp experiment | Contact/caging physical-grasp branch; near pickup but slipping remained | https://youtu.be/tIisPTbTaQo?si=AseZ2_7o_rqtnKLQ |
| Work 4 — Hybrid contact-guided grasp | Latest working hybrid result | https://www.youtube.com/watch?v=rhKuY6O_H5o |

> GitHub does not render embedded YouTube players in Markdown, so videos are linked through thumbnails/URLs. Local GIFs can be added later under `assets/readme/`.

## Current Status

| Area | Status | Notes |
|---|---|---|
| FSM baseline | Working | 12-state autonomous controller completes the task with kinematic grasp backend. |
| Scripted keyboard teacher | Working as infrastructure | Automates the original keyboard-control idea; useful for teacher experiments. |
| VLA data pipeline | Implemented as infrastructure | Records demos, exports G1-native datasets, audits data, builds training views, and combines batches. |
| Scenario perturbations | Partially validated | Batch/scenario metadata works, but perturbations expose teacher fragility. |
| Contact-aware physical grasp | Implemented as diagnostic branch | Measures contact/lift behavior without teleporting the object. |
| Physical-only grasp | Experimental | Explored but not reliable; slipping/contact stability remains hard. |
| Hybrid contact-guided grasp | Current best result | Contact/cage probe first, then kinematic attachment for transport. |
| OpenVLA integration | Roadmap/infrastructure only | Dataset/action-adapter groundwork exists, but no trained OpenVLA policy is deployed here. |

The current best result is not a pure physical force-closure grasp. It is a hybrid approach: physical/contact-guided probe first, kinematic transport after confirmation. This is the strongest practical result so far and is documented honestly as a simulation shortcut.

## Architecture Overview

```text
MuJoCo Scene
   |
   |-- walker.onnx / right_reacher.onnx
   |
WalkerReacherController
   |
   |-- KeyboardPolicy
   |-- FSMPolicy
   |-- ScriptedKeyboardPolicy / teacher recorder
   |-- ContactGuidedGraspPolicy
   |
Grasp Backends
   |-- KinematicAttachment
   |-- ContactAwarePhysicalGrasp
   |-- Hybrid contact-gated transport
   |
VLA Bridge
   |-- demo recorder
   |-- action adapter
   |-- replay harness
   |-- dataset exporter
   |-- audit/split tools
   |-- training views
   |-- batch manifests
```

- `run.py` is the main interactive entry point.
- `common/controller.py` owns walker/reacher inference and grip fraction control.
- `common/grasp.py` owns kinematic and contact-aware grasp machinery.
- `policies/fsm.py` and `policies/fsm_core.py` own the autonomous FSM.
- `vla_bridge/` contains action adapters, schema, replay metrics, dataset export, training views, and batch utilities.
- `scripts/` contains smoke tests, recorders, replay, plotting, dataset export, audit, and comparison tools.
- `configs/scripts/` contains scripted teacher/caging plans.
- `configs/scenarios/` contains perturbation configs.

## Repository Structure

```text
.
├── run.py                         # Main MuJoCo entry point
├── scene.xml                      # Pick-and-place scene
├── g1.xml                         # Unitree G1 model
├── model_config.json              # Joint/action/controller configuration
├── common/
│   ├── controller.py              # Walker/reacher control + grip fraction support
│   ├── grasp.py                   # Kinematic + contact-aware grasp backends
│   ├── onnx_policy.py             # ONNX policy wrapper
│   └── scene.py                   # Reset/render helpers
├── policies/
│   ├── fsm.py                     # FSM policy wrapper
│   ├── fsm_core.py                # 12-state task logic
│   └── keyboard.py                # Manual keyboard policy
├── vla_bridge/
│   ├── action_adapter.py          # 7D/G1 action adapters
│   ├── demo_recorder.py           # Demo recording helpers
│   ├── demo_schema.py             # JSONL schema tools
│   ├── replay_metrics.py          # Replay metrics
│   ├── g1_native_dataset.py       # G1-native export schema
│   ├── batch_manifest.py          # Batch recording manifest logic
│   ├── batch_dataset_export.py    # Combined dataset export
│   ├── dataset_audit.py           # Dataset audit/splits
│   ├── training_views.py          # Filtered/weighted training views
│   ├── scenario_config.py         # Scenario perturbation metadata
│   └── task_success.py            # Task-success metrics
├── scripts/
│   ├── smoke_env.py
│   ├── record_vla_demo.py
│   ├── replay_vla_demo.py
│   ├── export_g1_native_vla_dataset.py
│   ├── audit_g1_native_vla_dataset.py
│   ├── build_g1_native_training_views.py
│   ├── record_vla_demo_batch.py
│   ├── export_g1_native_vla_batch_dataset.py
│   ├── record_scripted_keyboard_demo.py
│   ├── compare_grasp_runs.py
│   └── test_contact_guided_grasp.py
├── configs/
│   ├── scripts/                  # Scripted keyboard / caging plans
│   └── scenarios/                # Scenario perturbations
├── tests/                        # Unit tests for controller, VLA, datasets, grasp, etc.
├── docs/                         # Research/decision logs
└── DEV_LOG.md                    # Detailed engineering chronology
```

## Setup

### Python environment

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip

pip install mujoco onnxruntime numpy opencv-python
```

On macOS, MuJoCo UI runs are often more reliable with:

```bash
mjpython run.py --policy keyboard
```

If `mjpython` is unavailable, use:

```bash
python run.py --policy keyboard
```

Do not add heavy dependencies unless already required.

## Running the System

### 1. Environment smoke test

```bash
python scripts/smoke_env.py
```

Validates scene load, cameras, bodies, sites, model_config joints, and ONNX warmup.

### 2. Manual keyboard mode

```bash
mjpython run.py --policy keyboard
```

or:

```bash
python run.py --policy keyboard
```

### 3. FSM baseline

```bash
mjpython run.py --policy fsm
```

Headless:

```bash
python run.py --policy fsm --no-cameras
```

### 4. Contact-guided / hybrid grasp policy

```bash
mjpython run.py --policy contact-guided-grasp
```

Headless:

```bash
python run.py --policy contact-guided-grasp --no-cameras
```

If available in your workflow/branch, backend flags can be used as explicit experiments:

```bash
python run.py --policy contact-guided-grasp --grasp-backend kinematic --no-cameras
python run.py --policy contact-guided-grasp --grasp-backend contact-aware-physical --no-cameras
```

### 5. Scripted keyboard teacher

```bash
python scripts/inspect_scripted_keyboard_plan.py configs/scripts/nominal_scripted_keyboard_v2.json

python scripts/record_scripted_keyboard_demo.py \
  --script-config configs/scripts/nominal_scripted_keyboard_v2.json \
  --output-dir data/vla_demos/scripted_keyboard_v2_test \
  --record-every 5 \
  --camera head_cam
```

### 6. VLA demo recording

```bash
python scripts/record_vla_demo.py \
  --output-dir data/vla_demos/demo_002_every_tick \
  --record-every 1 \
  --camera head_cam
```

### 7. Replay

```bash
python scripts/replay_vla_demo.py \
  data/vla_demos/demo_002_every_tick/demo.jsonl \
  --output-dir data/vla_replays/replay_002_teacher \
  --mode teacher-command
```

### 8. Plotting

```bash
python scripts/plot_vla_demo.py \
  data/vla_demos/demo_002_every_tick/demo.jsonl \
  --output-dir data/vla_demos/demo_002_every_tick/plots
```

### 9. Dataset export

```bash
python scripts/export_g1_native_vla_dataset.py \
  data/vla_demos/demo_002_every_tick/demo.jsonl \
  --output-dir data/vla_exports/g1_native_demo_002
```

### 10. Dataset audit and training views

```bash
python scripts/audit_g1_native_vla_dataset.py \
  data/vla_exports/g1_native_demo_002/dataset.jsonl \
  --output-dir data/vla_exports/g1_native_demo_002/audit

python scripts/build_g1_native_training_views.py \
  data/vla_exports/g1_native_demo_002/dataset.jsonl \
  --output-dir data/vla_exports/g1_native_demo_002/training_views
```

### 11. Batch collection

```bash
python scripts/record_vla_demo_batch.py \
  --output-root data/vla_demos/batch_000_no_images \
  --num-demos 2 \
  --record-every 1 \
  --no-images \
  --continue-on-fail
```

### 12. Scenario perturbations

```bash
python scripts/record_vla_demo_batch.py \
  --output-root data/vla_demos/batch_001_perturbed_no_images \
  --num-demos 5 \
  --record-every 1 \
  --no-images \
  --scenario-config configs/scenarios/small_perturbations.json \
  --continue-on-fail
```

### 13. Combined batch dataset export

```bash
python scripts/export_g1_native_vla_batch_dataset.py \
  data/vla_demos/batch_000_no_images/batch_manifest.json \
  --output-dir data/vla_exports/batch_000_no_images_g1_native
```

### 14. Grasp comparison

```bash
python scripts/compare_grasp_runs.py \
  data/vla_demos/scripted_keyboard_step26_kinematic/summary.json \
  data/vla_demos/scripted_keyboard_step26_caging_physical/summary.json
```

### 15. Contact-guided grasp diagnostic

```bash
python scripts/test_contact_guided_grasp.py
```

## Test Suite

The project has tests around controller behavior, grasp backends, scripted teacher plans, VLA schemas, replay metrics, dataset exports, batch manifests, perturbation metadata, and training views.

```bash
python -m unittest tests/test_vla_action_adapter.py
python -m unittest tests/test_vla_demo_schema.py
python -m unittest tests/test_vla_replay_metrics.py
python -m unittest tests/test_g1_native_dataset.py
python -m unittest tests/test_g1_native_dataset_audit.py
python -m unittest tests/test_g1_native_training_views.py
python -m unittest tests/test_vla_batch_manifest.py
python -m unittest tests/test_g1_native_batch_dataset_export.py
python -m unittest tests/test_batch_diversity_manifest.py
python -m unittest tests/test_scenario_config.py
python -m unittest tests/test_scripted_keyboard.py
python -m unittest tests/test_task_success.py
python -m unittest tests/test_contact_aware_grasp.py
python -m unittest tests/test_grip_fraction_controller.py
python -m unittest tests/test_compare_grasp_runs.py
python scripts/smoke_env.py
```

One-liner discovery (useful for broad checks):

```bash
python -m unittest discover -s tests
```

Targeted tests are often easier to debug when iterating.

| Test area | Representative files |
|---|---|
| FSM/environment readiness | `scripts/smoke_env.py` |
| VLA action/schema/replay | `test_vla_action_adapter.py`, `test_vla_demo_schema.py`, `test_vla_replay_metrics.py` |
| Dataset export/audit/views | `test_g1_native_dataset.py`, `test_g1_native_dataset_audit.py`, `test_g1_native_training_views.py` |
| Batch/scenario tools | `test_vla_batch_manifest.py`, `test_g1_native_batch_dataset_export.py`, `test_batch_diversity_manifest.py`, `test_scenario_config.py` |
| Scripted teacher | `test_scripted_keyboard.py` |
| Grasp/controller | `test_contact_aware_grasp.py`, `test_grip_fraction_controller.py`, `test_compare_grasp_runs.py` |
| Task success metrics | `test_task_success.py` |

## Development Timeline

| Step | Milestone | Status |
|---|---|---|
| 1–4 | Baseline audit, modular skeleton, ONNX/controller extraction, smoke test | Verified |
| 5–12 | FSM sequencing, object lookup, approach/hover/grasp/place, VLA research scaffold | Working baseline |
| 13 | G1 VLA action adapter | Unit-tested |
| 14 | FSM demonstration recorder | Validated |
| 15 | 7D replay harness | Diagnosed missing locomotion context |
| 16 | Teacher-command / hybrid replay schema | Teacher replay validated; relative 7D replay insufficient |
| 17 | G1-native dataset exporter | Validated |
| 18 | Dataset audit + train/validation split | Validated |
| 19 | Filtered/weighted training views | Validated |
| 20 | Multi-demo collection + batch manifest | Validated infrastructure |
| 21 | Combined batch dataset export | Validated |
| 22 | Scenario perturbations | Metadata validated; teacher fragility exposed |
| 23 | Scripted keyboard teacher | Implemented as second teacher source |
| 24–26 | Contact-aware physical grasp, contact-guided closure, table-assisted caging | Diagnostic/partial physical progress |
| 27 | Hybrid contact-gated grasp | Current best working result |
| 28+ | Physical-only multi-finger realism track | Experimental / future branch |

## Policy Modes

| Policy / mode | Purpose | Current role |
|---|---|---|
| `keyboard` | Original manual control | Baseline comparison and debugging |
| `fsm` | Autonomous finite-state task controller | Reliable baseline/teacher |
| `contact-guided-grasp` | Contact/cage-guided grasp logic | Current best hybrid result |
| scripted keyboard plans | Deterministic macro teacher | Teacher-data experiment |
| VLA bridge adapters | Convert teacher data into model-ready action formats | Infrastructure for future learning |

If some policy names differ, adjust based on the actual `run.py` parser. Do not invent unsupported CLI flags.

## Known Limitations

- **Kinematic transport shortcut:** The latest hybrid grasp still uses kinematic attachment during transport. The improvement is that attachment is now contact/probe-gated rather than blind.
- **Pure physical grasp not solved:** Physical/contact-only caging was explored, but slipping during lift remains difficult.
- **VLA model not trained/deployed:** The repo contains OpenVLA-style data infrastructure, not a trained OpenVLA policy controlling the G1.
- **Scenario perturbation fragility:** Perturbed cylinder positions expose teacher reliability issues; not every DONE state equals task success.
- **Sim-only validation:** The work is in MuJoCo and is not sim-to-real validated.

## Next Work

1. Record more hybrid contact-guided demonstrations with images.
2. Export hybrid demonstrations into the same G1-native dataset format.
3. Add stricter task-success labels for object-on-target, not just FSM `DONE`.
4. Continue the physical-only multi-finger branch with named fingertip contacts, micro-lift checks, and slip metrics.
5. Replace ground-truth object pose with a Visual Oracle using RGB-D segmentation/back-projection.
6. Test OpenVLA-style shadow inference or fine-tuning once the teacher dataset is cleaner and more diverse.

## Adding GIFs or Images

GitHub README files support images and GIFs:

```md
![Hybrid contact-guided grasp](assets/readme/hybrid_contact_guided_grasp.gif)
<img src="assets/readme/hybrid_contact_guided_grasp.gif" alt="Hybrid contact-guided grasp" width="720" />
```

Recommended layout:

```text
assets/readme/
└── hybrid_contact_guided_grasp.gif
```

Large videos should stay on YouTube; short compressed GIFs are best for README previews.
