#!/usr/bin/env python3
"""Compare summary.json outputs from multiple grasp recording runs.

Usage:
    python scripts/compare_grasp_runs.py \\
        data/vla_demos/run_a/summary.json \\
        data/vla_demos/run_b/summary.json \\
        [--output-json path/to/comparison.json]

Reads per-run summary JSON files and prints a table focused on grasp outcomes;
optionally writes a comparison JSON artifact for reporting.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


# Fields extracted from each summary.json, with their dotted-path and display label.
# Format: (display_label, dotted_path_in_dict)
_FIELDS = [
    ("script_name",                  "script_name"),
    ("grasp_backend",                "grasp_summary.backend"),
    ("task_success",                 "task_success"),
    ("ever_attached",                "ever_attached"),
    ("object_lifted",                "object_lifted"),
    ("object_on_target_table",       "object_on_target_table"),
    ("failure_reason",               "failure_reason"),
    ("ever_contacted",               "grasp_summary.n_contact_ticks"),
    ("stable_contact_ticks",         "grasp_summary.n_stable_contact_ticks"),
    ("lift_height_m",                "grasp_summary.lift_height_m"),
    ("physical_ever_lifted",         "grasp_summary.ever_lifted"),
    ("max_xy_displacement_m",        "object_motion_summary.max_xy_displacement_from_initial"),
    ("lift_height_from_initial_m",   "object_motion_summary.lift_height_from_initial"),
    ("possible_knockover_or_push",   "object_motion_summary.possible_knockover_or_push"),
    ("max_commanded_grip_fraction",  "max_commanded_grip_fraction"),
    ("uses_continuous_grip",         "uses_continuous_grip"),
    ("caging_plan",                  "caging_plan"),
    ("stopped_early",                "stopped_early"),
    ("stop_reason",                  "stop_reason"),
    ("num_steps",                    "num_steps"),
]


def _get_nested(d: dict, dotted_path: str):
    """Retrieve a value from a nested dict using dot-separated key path."""
    keys = dotted_path.split(".")
    cur = d
    for k in keys:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(k)
    return cur


def _load_summary(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"[warn] Could not load {path}: {exc}", file=sys.stderr)
        return {}


def _extract_row(path: Path, summary: dict) -> dict:
    row: dict = {"path": str(path)}
    for label, dotted in _FIELDS:
        row[label] = _get_nested(summary, dotted)
    return row


def _fmt(val) -> str:
    if val is None:
        return "-"
    if isinstance(val, bool):
        return str(val)
    if isinstance(val, float):
        return f"{val:.4f}"
    return str(val)


def _print_table(rows: list[dict]) -> None:
    if not rows:
        print("No rows to display.")
        return

    col_width = 32
    labels = ["path"] + [label for label, _ in _FIELDS]

    # Header
    print()
    for label in labels:
        print(f"  {label:<{col_width}}", end="")
    print()
    print("  " + "-" * (col_width * len(labels)))

    # One column per run (transposed view)
    for row in rows:
        for label in labels:
            print(f"  {_fmt(row.get(label)):<{col_width}}", end="")
        print()
    print()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare multiple grasp-run summary.json files."
    )
    parser.add_argument(
        "summaries",
        nargs="+",
        type=Path,
        metavar="SUMMARY_JSON",
        help="One or more summary.json paths to compare.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=None,
        help="If given, write the comparison table as a JSON array to this path.",
    )
    args = parser.parse_args()

    rows = []
    for path in args.summaries:
        summary = _load_summary(path)
        row = _extract_row(path, summary)
        rows.append(row)

    _print_table(rows)

    if args.output_json is not None:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(
            json.dumps(rows, indent=2, default=str), encoding="utf-8"
        )
        print(f"Comparison written to {args.output_json}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
