#!/usr/bin/env python3
"""Export a G1-native VLA supervised dataset from a recorded FSM demo.

Step 17:
- no OpenVLA
- no model inference
- no fine-tuning
- export image/instruction -> G1-native action target
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.demo_schema import read_jsonl
from vla_bridge.g1_native_dataset import (
    copy_images_for_records,
    dataset_summary,
    export_records_from_steps,
    write_dataset_jsonl,
    write_summary,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("metadata", type=Path)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/vla_exports/g1_native_demo"),
    )
    parser.add_argument("--allow-missing-images", action="store_true")
    parser.add_argument("--include-phase", action="store_true", default=True)
    parser.add_argument("--no-phase", dest="include_phase", action="store_false")
    parser.add_argument("--keep-done", action="store_true")
    parser.add_argument("--drop-inactive-reach", action="store_true")
    parser.add_argument("--image-prefix", type=str, default="")
    parser.add_argument("--copy-images", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    steps = read_jsonl(args.metadata)
    if not steps:
        raise RuntimeError(f"No demo steps found in {args.metadata}")

    records = export_records_from_steps(
        steps,
        require_images=not args.allow_missing_images,
        include_phase=args.include_phase,
        image_prefix=args.image_prefix,
        drop_done=not args.keep_done,
        drop_inactive_reach=args.drop_inactive_reach,
    )

    if args.copy_images:
        source_demo_dir = args.metadata.parent
        records = copy_images_for_records(
            records,
            source_demo_dir=source_demo_dir,
            output_images_dir=args.output_dir / "images",
        )

    dataset_path = args.output_dir / "dataset.jsonl"
    summary_path = args.output_dir / "summary.json"

    write_dataset_jsonl(dataset_path, records)
    summary = dataset_summary(records)
    summary.update(
        {
            "source_metadata": str(args.metadata),
            "dataset_path": str(dataset_path),
            "copied_images": bool(args.copy_images),
            "include_phase": bool(args.include_phase),
            "drop_done": bool(not args.keep_done),
            "drop_inactive_reach": bool(args.drop_inactive_reach),
            "action_vector": [
                "walk_x",
                "walk_y",
                "walk_yaw",
                "reach_x",
                "reach_y",
                "reach_z",
                "reach_active",
                "grip_closed",
            ],
        }
    )
    write_summary(summary_path, summary)

    print("\n--- G1-Native VLA Dataset Export Summary ---")
    print(f"source_metadata       : {args.metadata}")
    print(f"output_dir            : {args.output_dir}")
    print(f"dataset_path          : {dataset_path}")
    print(f"summary_path          : {summary_path}")
    print(f"num_source_steps      : {len(steps)}")
    print(f"num_exported_records  : {summary['num_records']}")
    print(f"unique_phases         : {summary.get('unique_phases', [])}")
    print(f"walk_nonzero_records  : {summary.get('walk_nonzero_records', 0)}")
    print(f"reach_active_records  : {summary.get('reach_active_records', 0)}")
    print(f"grip_closed_records   : {summary.get('grip_closed_records', 0)}")
    print(f"copy_images           : {bool(args.copy_images)}")
    print("\nTarget action vector:")
    print("  [walk_x, walk_y, walk_yaw, reach_x, reach_y, reach_z, reach_active, grip_closed]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
