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
    """Build full, filtered, and weighted views of the dataset.

    Outputs:
    - full.jsonl (unaltered records),
    - filtered_no_idle.jsonl (idle-pruned view),
    - sample_weights.jsonl (phase-balancing weights).
    """
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
