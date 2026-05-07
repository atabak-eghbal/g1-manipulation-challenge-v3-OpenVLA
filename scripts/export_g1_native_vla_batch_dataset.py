#!/usr/bin/env python3
"""Export a combined G1-native VLA dataset from a batch manifest.

Step 21:
- no OpenVLA
- no model inference
- no training
- combines successful FSM teacher demos into one supervised dataset artifact
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.batch_dataset_export import export_combined_batch_dataset


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export a combined G1-native VLA dataset from a batch manifest."
    )
    parser.add_argument("manifest_path", type=Path, help="Path to batch_manifest.json")
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory to save the combined dataset",
    )
    parser.add_argument(
        "--keep-done",
        action="store_true",
        help="Include steps where phase is DONE",
    )
    parser.add_argument(
        "--drop-inactive-reach",
        action="store_true",
        help="Exclude steps where reach_active is False",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        summary = export_combined_batch_dataset(
            args.manifest_path,
            args.output_dir,
            include_phase=True,
            drop_done=not args.keep_done,
            drop_inactive_reach=args.drop_inactive_reach,
        )
    except Exception as exc:
        print(f"Error exporting batch dataset: {exc}")
        return 1

    print("\n--- Combined G1-Native VLA Batch Dataset Export Summary ---")
    print(f"source_manifest       : {summary['source_manifest_path']}")
    print(f"output_dir            : {summary['output_dir']}")
    print(f"dataset_path          : {summary['dataset_path']}")
    print(f"summary_path          : {summary['summary_path']}")
    print(f"source_manifest_copy  : {summary['source_manifest_copy_path']}")
    print(f"batch_id              : {summary['batch_id']}")
    print(f"num_demos_in_manifest : {summary['num_demos_in_manifest']}")
    print(f"num_selected_demos    : {summary['num_selected_demos']}")
    print(f"num_skipped_demos     : {summary['num_skipped_demos']}")
    print(f"selected_demo_ids     : {summary['selected_demo_ids']}")
    print(f"num_records           : {summary['num_records']}")
    print(f"records_per_demo      : {summary['records_per_demo']}")
    print(f"unique_phases         : {summary['unique_phases']}")
    print(f"walk_nonzero_records  : {summary['walk_nonzero_records']}")
    print(f"reach_active_records  : {summary['reach_active_records']}")
    print(f"grip_closed_records   : {summary['grip_closed_records']}")
    print("")
    print("Target action vector:")
    print("  [walk_x, walk_y, walk_yaw, reach_x, reach_y, reach_z, reach_active, grip_closed]")

    if summary.get("num_skipped_demos", 0):
        print("")
        print("Skipped demos:")
        for demo_id, reason in summary.get("skip_reasons", {}).items():
            print(f"  - {demo_id}: {reason}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
