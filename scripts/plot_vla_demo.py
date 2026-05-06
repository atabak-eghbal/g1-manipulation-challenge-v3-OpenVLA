#!/usr/bin/env python3
"""Plot diagnostic figures for recorded or replayed VLA demonstrations.

Step 15 — optional plotting helper.

Usage (demo only):
    python scripts/plot_vla_demo.py data/vla_demos/demo_000/demo.jsonl \\
        --output-dir data/vla_demos/demo_000/plots

Usage (with replay trace):
    python scripts/plot_vla_demo.py data/vla_demos/demo_000/demo.jsonl \\
        --replay-trace data/vla_replays/replay_000/replay_trace.npz \\
        --output-dir data/vla_replays/replay_000/plots
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from vla_bridge.demo_schema import read_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot VLA demonstration figures."
    )
    parser.add_argument("metadata", type=Path, help="Path to demo.jsonl")
    parser.add_argument(
        "--replay-trace",
        type=Path,
        default=None,
        help="Optional replay_trace.npz to overlay teacher vs replay error",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/vla_plots"),
        help="Directory for output PNG files",
    )
    return parser.parse_args()


def _save(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(path), dpi=100, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot_vla_demo] saved {path}")


def plot_action_magnitude(steps, output_dir: Path) -> None:
    xyz = np.array([s.action_7d[:3] for s in steps], dtype=np.float64)
    mags = np.linalg.norm(xyz, axis=1)
    fig, ax = plt.subplots()
    ax.plot(mags)
    ax.set_xlabel("Step")
    ax.set_ylabel("Action magnitude (m)")
    ax.set_title("Action XYZ magnitude per step")
    _save(fig, output_dir / "action_magnitude.png")


def plot_grip_state(steps, output_dir: Path) -> None:
    grip = np.array([int(s.grip_closed) for s in steps])
    fig, ax = plt.subplots()
    ax.step(range(len(grip)), grip, where="post")
    ax.set_xlabel("Step")
    ax.set_ylabel("Grip closed")
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Open", "Closed"])
    ax.set_title("Gripper state over time")
    _save(fig, output_dir / "grip_state.png")


def plot_phase_index(steps, output_dir: Path) -> None:
    phases = [s.phase for s in steps]
    unique = sorted(set(phases))
    phase_map = {p: i for i, p in enumerate(unique)}
    indices = [phase_map[p] for p in phases]
    fig, ax = plt.subplots()
    ax.step(range(len(indices)), indices, where="post")
    ax.set_xlabel("Step")
    ax.set_ylabel("Phase index")
    ax.set_yticks(list(range(len(unique))))
    ax.set_yticklabels(unique, fontsize=8)
    ax.set_title("FSM phase index over time")
    _save(fig, output_dir / "phase_index.png")


def plot_walk_command_magnitude(steps, output_dir: Path) -> None:
    walk_cmds = np.array([s.walk_cmd for s in steps], dtype=np.float64)
    mags = np.linalg.norm(walk_cmds, axis=1)
    fig, ax = plt.subplots()
    ax.plot(mags)
    ax.set_xlabel("Step")
    ax.set_ylabel("Walk command magnitude")
    ax.set_title("Walk command magnitude per step")
    _save(fig, output_dir / "walk_command_magnitude.png")


def plot_palm_error(trace_path: Path, output_dir: Path) -> None:
    trace = np.load(str(trace_path))
    teacher = trace["teacher_palm_world"]
    replay = trace["replay_palm_world"]
    if teacher.shape != replay.shape or teacher.ndim != 2:
        print("[plot_vla_demo] warn: unexpected trace shape; skipping palm_error.png")
        return
    err = np.linalg.norm(replay - teacher, axis=1)
    fig, ax = plt.subplots()
    ax.plot(err)
    ax.set_xlabel("Step")
    ax.set_ylabel("Palm error (m)")
    ax.set_title("Teacher vs replay palm position error")
    _save(fig, output_dir / "palm_error.png")


def main() -> int:
    args = parse_args()

    steps = read_jsonl(args.metadata)
    if not steps:
        print(f"[plot_vla_demo] No steps found in {args.metadata}")
        return 1

    print(f"[plot_vla_demo] Loaded {len(steps)} steps from {args.metadata}")

    plot_action_magnitude(steps, args.output_dir)
    plot_grip_state(steps, args.output_dir)
    plot_phase_index(steps, args.output_dir)
    plot_walk_command_magnitude(steps, args.output_dir)

    if args.replay_trace is not None:
        plot_palm_error(args.replay_trace, args.output_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
