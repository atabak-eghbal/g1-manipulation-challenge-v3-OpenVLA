#!/usr/bin/env python3
"""Build filtered/weighted training views for a G1-native VLA dataset.

Step 19:
- no OpenVLA
- no model inference
- no fine-tuning
- create safer training views from audited records
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.g1_native_dataset import read_dataset_jsonl
from vla_bridge.training_views import build_training_views


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/vla_exports/g1_native_demo_002/training_views"),
    )
    parser.add_argument("--keep-first-n-idle", type=int, default=10)
    parser.add_argument("--max-weight", type=float, default=20.0)
    parser.add_argument("--rare-phase-boost", type=float, default=5.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    records = read_dataset_jsonl(args.dataset)
    if not records:
        raise RuntimeError(f"No records found in {args.dataset}")

    summary = build_training_views(
        records,
        output_dir=args.output_dir,
        keep_first_n_idle=args.keep_first_n_idle,
        max_weight=args.max_weight,
        rare_phase_boost=args.rare_phase_boost,
    )

    print("\n--- G1-Native VLA Training Views Summary ---")
    print(f"dataset                  : {args.dataset}")
    print(f"output_dir               : {args.output_dir}")
    print(f"source_records           : {summary['source_records']}")
    print(f"filtered_records         : {summary['filtered_records']}")
    print(f"removed_records          : {summary['removed_records']}")
    print(f"idle_records_source      : {summary['idle_records_source']}")
    print(f"idle_records_filtered    : {summary['idle_records_filtered']}")
    print(f"rare_source              : {summary['rare_transition_records_source']}")
    print(f"rare_filtered            : {summary['rare_transition_records_filtered']}")
    print(f"weight_count             : {summary['weight_count']}")
    print(f"min_weight               : {summary['min_weight']:.6f}")
    print(f"max_weight               : {summary['max_weight']:.6f}")
    print(f"mean_weight              : {summary['mean_weight']:.6f}")
    print(f"summary_path             : {summary['files']['summary']}")
    print("\nFiles:")
    for name, path in summary["files"].items():
        print(f"  {name:18s}: {path}")

    if summary["warnings"]:
        print("\nWarnings:")
        for warning in summary["warnings"]:
            print(f"  - {warning}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
