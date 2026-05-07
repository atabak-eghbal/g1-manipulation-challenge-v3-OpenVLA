"""Scripted keyboard plan helpers for G1-native VLA.

Step 23 scope:
- no MuJoCo
- no OpenCV
- pure plan parsing, validation, expansion, and summary
"""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Sequence
import json

import numpy as np


@dataclass(frozen=True)
class ScriptedKeyboardStep:
    """A single step in a scripted keyboard plan."""

    name: str
    duration_ticks: int
    walk_cmd: tuple[float, float, float]
    reach_target: tuple[float, float, float]
    reach_active: bool
    grip_closed: bool


@dataclass(frozen=True)
class ScriptedKeyboardPlan:
    """A complete scripted keyboard plan."""

    name: str
    teacher_type: str
    description: str
    control_dt: float
    steps: list[ScriptedKeyboardStep]


@dataclass(frozen=True)
class ExpandedScriptedCommand:
    """A single command at a specific tick, after plan expansion."""

    tick_index: int
    phase: str
    walk_cmd: tuple[float, float, float]
    reach_target: tuple[float, float, float]
    reach_active: bool
    grip_closed: bool


def load_scripted_keyboard_plan(path: str | Path) -> ScriptedKeyboardPlan:
    """Load a scripted keyboard plan from a JSON file."""
    src = Path(path)
    data = json.loads(src.read_text(encoding="utf-8"))
    steps = [ScriptedKeyboardStep(**s) for s in data.pop("steps")]
    return ScriptedKeyboardPlan(steps=steps, **data)


def validate_scripted_keyboard_plan(plan: ScriptedKeyboardPlan) -> None:
    """Validate a scripted keyboard plan."""
    if not plan.steps:
        raise ValueError("Plan must contain at least one step.")
    if plan.teacher_type != "scripted_keyboard":
        raise ValueError(f"Expected teacher_type 'scripted_keyboard', got '{plan.teacher_type}'")
    
    for i, step in enumerate(plan.steps):
        if step.duration_ticks <= 0:
            raise ValueError(f"Step {i} ({step.name}) has non-positive duration_ticks: {step.duration_ticks}")
        if len(step.walk_cmd) != 3:
            raise ValueError(f"Step {i} ({step.name}) walk_cmd must be length 3, got {len(step.walk_cmd)}")
        if len(step.reach_target) != 3:
            raise ValueError(f"Step {i} ({step.name}) reach_target must be length 3, got {len(step.reach_target)}")


def expand_scripted_keyboard_plan(plan: ScriptedKeyboardPlan) -> list[ExpandedScriptedCommand]:
    """Expand a scripted keyboard plan into a list of per-tick commands."""
    validate_scripted_keyboard_plan(plan)
    expanded_commands: list[ExpandedScriptedCommand] = []
    current_tick = 0
    for step in plan.steps:
        for _ in range(step.duration_ticks):
            expanded_commands.append(
                ExpandedScriptedCommand(
                    tick_index=current_tick,
                    phase=step.name,
                    walk_cmd=step.walk_cmd,
                    reach_target=step.reach_target,
                    reach_active=step.reach_active,
                    grip_closed=step.grip_closed,
                )
            )
            current_tick += 1
    return expanded_commands


def command_for_tick(plan: ScriptedKeyboardPlan, tick: int) -> ExpandedScriptedCommand:
    """Return the command for a given tick. If tick is past the end, return the final command."""
    expanded = expand_scripted_keyboard_plan(plan)
    if not expanded:
        raise ValueError("Cannot get command for an empty plan.")
    if tick < 0:
        raise ValueError("Tick must be non-negative.")
    if tick >= len(expanded):
        return expanded[-1]
    return expanded[tick]


def plan_summary(plan: ScriptedKeyboardPlan) -> dict[str, Any]:
    """Return a summary of the scripted keyboard plan."""
    expanded = expand_scripted_keyboard_plan(plan)
    total_ticks = len(expanded)
    
    if not expanded:
        return {
            "name": plan.name,
            "teacher_type": plan.teacher_type,
            "description": plan.description,
            "control_dt": plan.control_dt,
            "num_steps": len(plan.steps),
            "total_ticks": 0,
            "total_seconds": 0.0,
            "phases": {},
            "grip_closed_ticks": 0,
            "reach_active_ticks": 0,
            "walk_nonzero_ticks": 0,
            "warnings": ["Plan has no expanded commands."],
        }

    phases_counter = Counter(cmd.phase for cmd in expanded)
    
    grip_closed_ticks = sum(1 for cmd in expanded if cmd.grip_closed)
    reach_active_ticks = sum(1 for cmd in expanded if cmd.reach_active)
    walk_nonzero_ticks = sum(
        1 for cmd in expanded if np.linalg.norm(cmd.walk_cmd) > 1e-9
    )

    return {
        "name": plan.name,
        "teacher_type": plan.teacher_type,
        "description": plan.description,
        "control_dt": plan.control_dt,
        "num_steps": len(plan.steps),
        "total_ticks": total_ticks,
        "total_seconds": float(total_ticks * plan.control_dt),
        "phases": {k: v for k, v in sorted(phases_counter.items())},
        "grip_closed_ticks": grip_closed_ticks,
        "reach_active_ticks": reach_active_ticks,
        "walk_nonzero_ticks": walk_nonzero_ticks,
        "warnings": [],
    }
