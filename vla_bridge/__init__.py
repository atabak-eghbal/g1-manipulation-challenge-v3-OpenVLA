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
from vla_bridge.scripted_keyboard import (
    ScriptedKeyboardStep,
    ScriptedKeyboardPlan,
    ExpandedScriptedCommand,
    load_scripted_keyboard_plan,
    validate_scripted_keyboard_plan,
    expand_scripted_keyboard_plan,
    command_for_tick,
    plan_summary,
)
from vla_bridge.task_success import TaskSuccessTracker

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
    # Step 23 — scripted keyboard
    "ScriptedKeyboardStep",
    "ScriptedKeyboardPlan",
    "ExpandedScriptedCommand",
    "load_scripted_keyboard_plan",
    "validate_scripted_keyboard_plan",
    "expand_scripted_keyboard_plan",
    "command_for_tick",
    "plan_summary",
    # Step 23B — task success tracking
    "TaskSuccessTracker",
]
