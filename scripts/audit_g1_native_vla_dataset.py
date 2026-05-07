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
