"""Scripted keyboard plan helpers for G1-native VLA.

Step 23 scope:
- no MuJoCo
- no OpenCV
- pure plan parsing, validation, expansion, and summary

Step 26 additions:
- optional grip_fraction and grip_close_speed per step
- plan_summary reports uses_continuous_grip, min/max grip_fraction
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
    grip_fraction: float | None = None      # continuous override [0, 1]; None = binary
    grip_close_speed: float | None = None   # ramp speed override; None = keep current


@dataclass(frozen=True)
class ScriptedKeyboardPlan:
    """A complete scripted keyboard plan.

    reach_frame: "pelvis" (default) — reach_target values are already in pelvis
                 frame and written to the controller as-is.
                 "world" — reach_target values are world-frame coordinates;
                 the recording/viewer code must convert to pelvis frame each tick
                 using the robot's current pose.

    This plan acts as an automated keyboard-style teacher macro, not as runtime
    autonomy; it reproduces staged human-like command sequences deterministically.
    """

    name: str
    teacher_type: str
    description: str
    control_dt: float
    steps: list[ScriptedKeyboardStep]
    reach_frame: str = "pelvis"


@dataclass(frozen=True)
class ExpandedScriptedCommand:
    """A single command at a specific tick, after plan expansion."""

    tick_index: int
    phase: str
    walk_cmd: tuple[float, float, float]
    reach_target: tuple[float, float, float]
    reach_active: bool
    grip_closed: bool
    grip_fraction: float | None = None
    grip_close_speed: float | None = None


def _parse_step(raw: dict) -> ScriptedKeyboardStep:
    """Build a ScriptedKeyboardStep, accepting optional new fields gracefully."""
    known = {
        "name", "duration_ticks", "walk_cmd", "reach_target",
        "reach_active", "grip_closed", "grip_fraction", "grip_close_speed",
    }
    filtered = {k: v for k, v in raw.items() if k in known}
    # Convert list reach_target/walk_cmd to tuple
    if "walk_cmd" in filtered:
        filtered["walk_cmd"] = tuple(filtered["walk_cmd"])
    if "reach_target" in filtered:
        filtered["reach_target"] = tuple(filtered["reach_target"])
    return ScriptedKeyboardStep(**filtered)


def load_scripted_keyboard_plan(path: str | Path) -> ScriptedKeyboardPlan:
    """Load a scripted keyboard plan from a JSON file."""
    src = Path(path)
    data = json.loads(src.read_text(encoding="utf-8"))
    steps = [_parse_step(s) for s in data.pop("steps")]
    return ScriptedKeyboardPlan(steps=steps, **data)


def validate_scripted_keyboard_plan(plan: ScriptedKeyboardPlan) -> None:
    """Validate a scripted keyboard plan."""
    if not plan.steps:
        raise ValueError("Plan must contain at least one step.")
    if plan.teacher_type != "scripted_keyboard":
        raise ValueError(f"Expected teacher_type 'scripted_keyboard', got '{plan.teacher_type}'")
    if plan.reach_frame not in ("pelvis", "world"):
        raise ValueError(f"reach_frame must be 'pelvis' or 'world', got '{plan.reach_frame}'")

    for i, step in enumerate(plan.steps):
        if step.duration_ticks <= 0:
            raise ValueError(f"Step {i} ({step.name}) has non-positive duration_ticks: {step.duration_ticks}")
        if len(step.walk_cmd) != 3:
            raise ValueError(f"Step {i} ({step.name}) walk_cmd must be length 3, got {len(step.walk_cmd)}")
        if len(step.reach_target) != 3:
            raise ValueError(f"Step {i} ({step.name}) reach_target must be length 3, got {len(step.reach_target)}")
        if step.grip_fraction is not None:
            if not (0.0 <= float(step.grip_fraction) <= 1.0):
                raise ValueError(
                    f"Step {i} ({step.name}) grip_fraction={step.grip_fraction} is outside [0, 1]"
                )
        if step.grip_close_speed is not None:
            if float(step.grip_close_speed) <= 0.0:
                raise ValueError(
                    f"Step {i} ({step.name}) grip_close_speed={step.grip_close_speed} must be positive"
                )


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
                    grip_fraction=step.grip_fraction,
                    grip_close_speed=step.grip_close_speed,
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
            "uses_continuous_grip": False,
            "min_grip_fraction": None,
            "max_grip_fraction": None,
            "warnings": ["Plan has no expanded commands."],
        }

    phases_counter = Counter(cmd.phase for cmd in expanded)

    grip_closed_ticks = sum(1 for cmd in expanded if cmd.grip_closed)
    reach_active_ticks = sum(1 for cmd in expanded if cmd.reach_active)
    walk_nonzero_ticks = sum(
        1 for cmd in expanded if np.linalg.norm(cmd.walk_cmd) > 1e-9
    )

    # Continuous grip stats
    fractions = [cmd.grip_fraction for cmd in expanded if cmd.grip_fraction is not None]
    uses_continuous_grip = len(fractions) > 0
    min_grip_fraction: float | None = float(min(fractions)) if fractions else None
    max_grip_fraction: float | None = float(max(fractions)) if fractions else None

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
        "uses_continuous_grip": uses_continuous_grip,
        "min_grip_fraction": min_grip_fraction,
        "max_grip_fraction": max_grip_fraction,
        "warnings": [],
    }
