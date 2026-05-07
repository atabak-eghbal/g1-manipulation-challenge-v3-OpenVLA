#!/usr/bin/env python3
"""Inspect a G1-native VLA dataset export."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import numpy as np

from vla_bridge.g1_native_dataset import dataset_summary, read_dataset_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    records = read_dataset_jsonl(args.dataset)
    if not records:
        print("No records found.")
        return 1

    summary = dataset_summary(records)
    action = np.asarray([r.action_vector for r in records], dtype=np.float64)

    print("--- G1-Native VLA Dataset Summary ---")
    print(f"dataset               : {args.dataset}")
    print(f"num_records           : {summary['num_records']}")
    print(f"first_phase           : {summary.get('first_phase', '')}")
    print(f"last_phase            : {summary.get('last_phase', '')}")
    print(f"unique_phases         : {summary.get('unique_phases', [])}")
    print(f"walk_nonzero_records  : {summary.get('walk_nonzero_records', 0)}")
    print(f"reach_active_records  : {summary.get('reach_active_records', 0)}")
    print(f"grip_closed_records   : {summary.get('grip_closed_records', 0)}")
    print(f"action_vector_shape   : {action.shape}")
    print(f"first_image           : {records[0].image_path}")
    print(f"last_image            : {records[-1].image_path}")
    print(f"first_action_vector   : {records[0].action_vector}")
    print(f"last_action_vector    : {records[-1].action_vector}")

    if action.ndim != 2 or action.shape[1] != 8:
        print("ERROR: action_vector must have shape (N, 8)")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
