#!/usr/bin/env python3
"""Inspect a scripted keyboard plan JSON file.

Usage:
    python scripts/inspect_scripted_keyboard_plan.py configs/scripts/nominal_scripted_keyboard_v1.json
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from vla_bridge.scripted_keyboard import (
    command_for_tick,
    load_scripted_keyboard_plan,
    plan_summary,
    validate_scripted_keyboard_plan,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect a scripted keyboard plan.")
    parser.add_argument("script_config", type=Path, help="Path to the script config JSON file.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        plan = load_scripted_keyboard_plan(args.script_config)
        validate_scripted_keyboard_plan(plan)
    except Exception as exc:
        print(f"Error loading or validating plan: {exc}")
        return 1

    summary = plan_summary(plan)

    print(f"\n--- Scripted Keyboard Plan: {plan.name} ---")
    print(f"Description        : {plan.description}")
    print(f"Teacher Type       : {plan.teacher_type}")
    print(f"Control dt         : {plan.control_dt:.4f} s")
    print(f"Number of steps    : {summary['num_steps']}")
    print(f"Total Ticks        : {summary['total_ticks']}")
    print(f"Total Seconds      : {summary['total_seconds']:.2f} s")
    print(f"Phases             : {summary['phases']}")
    print(f"Grip Closed Ticks  : {summary['grip_closed_ticks']}")
    print(f"Reach Active Ticks : {summary['reach_active_ticks']}")
    print(f"Walk Nonzero Ticks : {summary['walk_nonzero_ticks']}")

    if summary["total_ticks"] > 0:
        first_command = command_for_tick(plan, 0)
        last_command = command_for_tick(plan, summary["total_ticks"] - 1)

        print("\nFirst Command:")
        print(f"  Tick Index     : {first_command.tick_index}")
        print(f"  Phase          : {first_command.phase}")
        print(f"  Walk Cmd       : {first_command.walk_cmd}")
        print(f"  Reach Target   : {first_command.reach_target}")
        print(f"  Reach Active   : {first_command.reach_active}")
        print(f"  Grip Closed    : {first_command.grip_closed}")

        print("\nLast Command:")
        print(f"  Tick Index     : {last_command.tick_index}")
        print(f"  Phase          : {last_command.phase}")
        print(f"  Walk Cmd       : {last_command.walk_cmd}")
        print(f"  Reach Target   : {last_command.reach_target}")
        print(f"  Reach Active   : {last_command.reach_active}")
        print(f"  Grip Closed    : {last_command.grip_closed}")

    if summary["warnings"]:
        print("\nWarnings:")
        for warning in summary["warnings"]:
            print(f"  - {warning}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
