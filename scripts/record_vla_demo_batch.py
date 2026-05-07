#!/usr/bin/env python3
"""Batch-record FSM teacher demonstrations for the G1-native VLA branch.

Step 20:
- no OpenVLA
- no model inference
- no training
- repeated FSM demo collection with a batch manifest
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from vla_bridge.batch_manifest import (
    build_batch_manifest,
    demo_record_from_summary,
    failed_demo_record,
    make_demo_id,
    manifest_summary,
    write_batch_manifest,
)
from vla_bridge.scenario_config import ScenarioSpec, load_scenario_config, scenario_to_metadata, select_scenario


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=Path("data/vla_demos/batch_000"))
    parser.add_argument("--num-demos", type=int, default=3)
    parser.add_argument("--record-every", type=int, default=1)
    parser.add_argument("--camera", type=str, default="head_cam")
    parser.add_argument("--no-images", action="store_true")
    parser.add_argument("--max-ticks", type=int, default=4000)
    parser.add_argument("--continue-on-fail", action="store_true")
    parser.add_argument("--python", type=str, default=sys.executable)
    parser.add_argument("--batch-id", type=str, default="")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--scenario-config",
        type=Path,
        default=None,
        help="Optional JSON config of deterministic scenario perturbations.",
    )
    return parser.parse_args()


def _load_summary(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _recorder_supports_max_ticks() -> bool:
    recorder_path = REPO_ROOT / "scripts" / "record_vla_demo.py"
    if not recorder_path.exists():
        return False
    text = recorder_path.read_text(encoding="utf-8", errors="ignore")
    return "--max-control-ticks" in text


def _build_record_command(args: argparse.Namespace, demo_dir: Path, scenario: ScenarioSpec | None = None) -> list[str]:
    cmd = [
        args.python,
        str(REPO_ROOT / "scripts" / "record_vla_demo.py"),
        "--output-dir",
        str(demo_dir),
        "--record-every",
        str(args.record_every),
    ]

    if _recorder_supports_max_ticks():
        cmd.extend(["--max-control-ticks", str(args.max_ticks)])

    if args.no_images:
        cmd.append("--no-images")
    else:
        cmd.extend(["--camera", args.camera])
    if scenario is not None:
        cmd.extend(["--scenario-id", scenario.scenario_id])
        cmd.extend(["--seed", str(int(scenario.seed))])
        cmd.extend(
            [
                "--red-block-xy-offset",
                str(float(scenario.red_block_xy_offset_m[0])),
                str(float(scenario.red_block_xy_offset_m[1])),
            ]
        )

    return cmd


def main() -> int:
    args = parse_args()

    if args.num_demos < 0:
        raise ValueError("--num-demos must be non-negative")
    if args.record_every <= 0:
        raise ValueError("--record-every must be positive")
    if args.max_ticks <= 0:
        raise ValueError("--max-ticks must be positive")

    args.output_root.mkdir(parents=True, exist_ok=True)
    batch_id = args.batch_id or args.output_root.name
    manifest_path = args.output_root / "batch_manifest.json"

    demo_records = []
    scenario_config = None
    if args.scenario_config is not None:
        scenario_config = load_scenario_config(args.scenario_config)

    if args.dry_run:
        print("\n--- G1 VLA Batch Recorder Dry Run ---")
        for i in range(args.num_demos):
            demo_id = make_demo_id(i)
            demo_dir = args.output_root / demo_id
            scenario = select_scenario(scenario_config, i) if scenario_config is not None else None
            cmd = _build_record_command(args, demo_dir, scenario)
            print(" ".join(cmd))

        manifest = build_batch_manifest(
            batch_id=batch_id,
            output_root=args.output_root,
            num_requested=args.num_demos,
            record_every=args.record_every,
            camera=args.camera,
            no_images=args.no_images,
            max_ticks=args.max_ticks,
            demos=[],
            scenario_config_path=str(args.scenario_config or ""),
            scenario_config_name=scenario_config.name if scenario_config is not None else "",
            scenario_count=len(scenario_config.scenarios) if scenario_config is not None else 0,
        )
        write_batch_manifest(manifest_path, manifest)
        print(f"\n[record_vla_demo_batch] wrote dry-run manifest: {manifest_path}")
        return 0

    for i in range(args.num_demos):
        demo_id = make_demo_id(i)
        demo_dir = args.output_root / demo_id
        demo_dir.mkdir(parents=True, exist_ok=True)
        scenario = select_scenario(scenario_config, i) if scenario_config is not None else None
        cmd = _build_record_command(args, demo_dir, scenario)

        print("\n============================================================")
        print(f"[record_vla_demo_batch] Recording {demo_id} ({i + 1}/{args.num_demos})")
        print(f"[record_vla_demo_batch] output_dir: {demo_dir}")
        print(f"[record_vla_demo_batch] command   : {' '.join(cmd)}")
        print("============================================================")

        try:
            subprocess.run(cmd, cwd=str(REPO_ROOT), check=True)
            summary = _load_summary(demo_dir / "summary.json")
            record = demo_record_from_summary(
                demo_id=demo_id,
                output_dir=demo_dir,
                summary=summary,
                scenario_id=scenario.scenario_id if scenario is not None else "",
                seed=scenario.seed if scenario is not None else None,
                scenario=scenario_to_metadata(scenario) if scenario is not None else None,
            )
            demo_records.append(record)
        except Exception as exc:
            record = failed_demo_record(
                demo_id=demo_id,
                output_dir=demo_dir,
                error=repr(exc),
                scenario_id=scenario.scenario_id if scenario is not None else "",
                seed=scenario.seed if scenario is not None else None,
                scenario=scenario_to_metadata(scenario) if scenario is not None else None,
            )
            demo_records.append(record)
            print(f"[record_vla_demo_batch] ERROR in {demo_id}: {exc}")
            if not args.continue_on_fail:
                print("[record_vla_demo_batch] stopping because --continue-on-fail was not set")
                break

    manifest = build_batch_manifest(
        batch_id=batch_id,
        output_root=args.output_root,
        num_requested=args.num_demos,
        record_every=args.record_every,
        camera=args.camera,
        no_images=args.no_images,
        max_ticks=args.max_ticks,
        demos=demo_records,
        scenario_config_path=str(args.scenario_config or ""),
        scenario_config_name=scenario_config.name if scenario_config is not None else "",
        scenario_count=len(scenario_config.scenarios) if scenario_config is not None else 0,
    )
    write_batch_manifest(manifest_path, manifest)
    summary = manifest_summary(manifest)

    print("\n--- G1 VLA Batch Recording Summary ---")
    print(f"batch_id              : {manifest.batch_id}")
    print(f"output_root           : {manifest.output_root}")
    print(f"manifest_path         : {manifest_path}")
    print(f"num_requested         : {manifest.num_requested}")
    print(f"num_completed         : {manifest.num_completed}")
    print(f"num_failed            : {manifest.num_failed}")
    print(f"successful_done_demos : {summary['successful_done_demos']}")
    print(f"total_steps           : {summary['total_steps']}")
    print(f"total_frames          : {summary['total_frames']}")
    print(f"demo_ids              : {summary['demo_ids']}")

    return 0 if manifest.num_failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
