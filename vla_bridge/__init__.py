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
]
