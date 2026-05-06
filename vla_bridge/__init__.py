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
]
