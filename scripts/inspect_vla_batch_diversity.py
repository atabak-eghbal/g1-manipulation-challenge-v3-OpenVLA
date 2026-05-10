#!/usr/bin/env python3
"""Inspect scenario diversity statistics from a batch manifest.

Reads:
- batch_manifest.json produced by batch recording.

Writes:
- optional summary JSON when --output-json is provided.

Role: diagnostic/reporting helper (no simulation or training changes).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.batch_diversity import summarize_manifest_diversity
from vla_bridge.batch_manifest import read_batch_manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect scenario diversity from a VLA batch manifest."
    )
    parser.add_argument("manifest_path", type=Path, help="Path to batch_manifest.json")
    parser.add_argument("--output-json", type=Path, default=None, help="Optional path to write summary JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = read_batch_manifest(args.manifest_path)
    summary = summarize_manifest_diversity(manifest)

    print("--- VLA Batch Diversity Summary ---")
    print(f"batch_id             : {summary['batch_id']}")
    print(f"num_demos            : {summary['num_demos']}")
    print(f"num_successful_demos : {summary['num_successful_demos']}")
    print(f"num_unique_scenarios : {summary['num_unique_scenarios']}")
    print(f"scenario_ids         : {summary['scenario_ids']}")
    print(f"dx_range_m           : {summary['dx_range_m']}")
    print(f"dy_range_m           : {summary['dy_range_m']}")
    print(f"all_offsets_identical: {summary['all_offsets_identical']}")

    if args.output_json is not None:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print(f"output_json          : {args.output_json}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
