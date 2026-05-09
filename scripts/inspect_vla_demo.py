#!/usr/bin/env python3
"""Inspect a recorded VLA demonstration JSONL file.

Usage:
    python scripts/inspect_vla_demo.py data/vla_demos/demo_000/demo.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np

from vla_bridge.demo_schema import read_jsonl


_TASK_SUCCESS_FIELDS = (
    "teacher_type",
    "ever_attached",
    "task_success",
    "failure_reason",
    "object_on_target_table",
    "final_height_above_target",
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print summary statistics for a VLA demonstration JSONL file."
    )
    parser.add_argument("metadata", type=Path, help="Path to demo.jsonl")
    args = parser.parse_args()

    steps = read_jsonl(args.metadata)
    if not steps:
        print("No steps found.")
        return 1

    actions = np.array([s.action_7d[:3] for s in steps], dtype=np.float64)
    mags = np.linalg.norm(actions, axis=1)
    phases = [s.phase for s in steps]

    walk_cmds = np.asarray([s.walk_cmd for s in steps], dtype=np.float64)
    walk_mags = np.linalg.norm(walk_cmds, axis=1)
    walk_nonzero_steps = int(np.sum(walk_mags > 1e-9))
    reach_active_steps = int(sum(s.reach_active for s in steps))

    print("--- VLA Demo Summary ---")
    print(f"metadata         : {args.metadata}")
    print(f"num_steps        : {len(steps)}")
    print(f"first_phase      : {phases[0]}")
    print(f"last_phase       : {phases[-1]}")
    print(f"unique_phases    : {sorted(set(phases))}")
    print(f"max_action_xyz_m : {float(mags.max()):.6f}")
    print(f"mean_action_xyz_m: {float(mags.mean()):.6f}")
    print(f"grip_closed_steps: {sum(1 for s in steps if s.grip_closed)}")
    print(f"walk_nonzero_steps: {walk_nonzero_steps}")
    print(f"reach_active_steps: {reach_active_steps}")
    print(f"first_image      : {steps[0].image_path}")
    print(f"last_image       : {steps[-1].image_path}")

    # Print task-success fields from sibling summary.json if present
    summary_path = args.metadata.parent / "summary.json"
    if summary_path.exists():
        try:
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            any_printed = False
            for key in _TASK_SUCCESS_FIELDS:
                if key in summary:
                    if not any_printed:
                        print("\n--- Task Success (from summary.json) ---")
                        any_printed = True
                    print(f"{key:<28}: {summary[key]}")
        except Exception:
            pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
