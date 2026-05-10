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
    """Construct a comprehensive audit report.

    The report explicitly includes single-trajectory caveats so downstream
    train/val consumers do not over-interpret these debugging splits.
    """
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
