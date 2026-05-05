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
