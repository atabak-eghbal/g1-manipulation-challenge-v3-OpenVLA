"""Replay metrics for VLA-style action demonstrations.

Step 15 scope:
- no OpenVLA
- no model inference
- no MuJoCo dependency
- pure metrics for comparing teacher and replay trajectories

Step 16 additions:
- walk_command_magnitudes helper
- walk_nonzero_steps, reach_active_steps, mean/max walk command magnitude in ReplayMetrics
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from vla_bridge.demo_schema import VLADemoStep


@dataclass(frozen=True)
class ReplayMetrics:
    num_steps: int
    mean_palm_error_m: float
    max_palm_error_m: float
    final_palm_error_m: float
    mean_action_magnitude_m: float
    max_action_magnitude_m: float
    grip_mismatch_count: int
    mean_walk_command_magnitude: float
    max_walk_command_magnitude: float
    walk_nonzero_steps: int
    reach_active_steps: int


def action_xyz_magnitudes(steps: Sequence[VLADemoStep]) -> np.ndarray:
    """Return L2 norm of action_7d[:3] for each step.

    Returns an empty float64 array if *steps* is empty.
    """
    if not steps:
        return np.asarray([], dtype=np.float64)
    xyz = np.asarray([s.action_7d[:3] for s in steps], dtype=np.float64)
    return np.linalg.norm(xyz, axis=1)


def walk_command_magnitudes(steps: Sequence[VLADemoStep]) -> np.ndarray:
    """Return L2 norm of walk_cmd for each step.

    Returns an empty float64 array if *steps* is empty.
    """
    if not steps:
        return np.asarray([], dtype=np.float64)
    walk_cmds = np.asarray([s.walk_cmd for s in steps], dtype=np.float64)
    return np.linalg.norm(walk_cmds, axis=1)


def palm_error_metrics(
    teacher_palm_world: np.ndarray,
    replay_palm_world: np.ndarray,
) -> tuple[float, float, float]:
    """Compute mean, max, and final L2 error between two (N, 3) palm arrays.

    Returns (nan, nan, nan) when N == 0.
    """
    teacher = np.asarray(teacher_palm_world, dtype=np.float64)
    replay = np.asarray(replay_palm_world, dtype=np.float64)
    if teacher.shape != replay.shape:
        raise ValueError(
            f"teacher and replay shapes must match, got {teacher.shape} and {replay.shape}"
        )
    if teacher.ndim != 2 or teacher.shape[1] != 3:
        raise ValueError(
            f"expected arrays with shape (N, 3), got {teacher.shape}"
        )
    if teacher.shape[0] == 0:
        return float("nan"), float("nan"), float("nan")
    err = np.linalg.norm(replay - teacher, axis=1)
    return float(err.mean()), float(err.max()), float(err[-1])


def grip_mismatch_count(
    teacher_grip: Sequence[bool],
    replay_grip: Sequence[bool],
) -> int:
    """Count positions where grip booleans differ.

    Both sequences must have the same length.
    """
    if len(teacher_grip) != len(replay_grip):
        raise ValueError(
            f"grip sequences must have same length, got {len(teacher_grip)} and {len(replay_grip)}"
        )
    return int(sum(bool(a) != bool(b) for a, b in zip(teacher_grip, replay_grip)))


def compute_replay_metrics(
    steps: Sequence[VLADemoStep],
    replay_palm_world: np.ndarray,
    replay_grip: Sequence[bool],
) -> ReplayMetrics:
    """Compute all replay metrics against the teacher trajectory.

    *replay_palm_world* must have shape (len(steps), 3).
    *replay_grip* length must match len(steps).

    This function is the main teacher-vs-replay diagnostic entry point used to
    quantify action-interface fidelity before model training.
    """
    teacher_palm = np.asarray([s.palm_world for s in steps], dtype=np.float64)
    teacher_grip = [bool(s.grip_closed) for s in steps]
    replay_palm = np.asarray(replay_palm_world, dtype=np.float64)

    if replay_palm.shape != teacher_palm.shape:
        raise ValueError(
            f"replay_palm_world must have shape {teacher_palm.shape}, got {replay_palm.shape}"
        )
    if len(replay_grip) != len(steps):
        raise ValueError(
            f"replay_grip must have length {len(steps)}, got {len(replay_grip)}"
        )

    mean_err, max_err, final_err = palm_error_metrics(teacher_palm, replay_palm)
    mags = action_xyz_magnitudes(steps)
    walk_mags = walk_command_magnitudes(steps)
    walk_nonzero_steps = int(np.sum(walk_mags > 1e-9))
    reach_active_steps = int(sum(bool(s.reach_active) for s in steps))

    return ReplayMetrics(
        num_steps=len(steps),
        mean_palm_error_m=mean_err,
        max_palm_error_m=max_err,
        final_palm_error_m=final_err,
        mean_action_magnitude_m=float(mags.mean()) if len(mags) else float("nan"),
        max_action_magnitude_m=float(mags.max()) if len(mags) else float("nan"),
        grip_mismatch_count=grip_mismatch_count(teacher_grip, replay_grip),
        mean_walk_command_magnitude=float(walk_mags.mean()) if len(walk_mags) else float("nan"),
        max_walk_command_magnitude=float(walk_mags.max()) if len(walk_mags) else float("nan"),
        walk_nonzero_steps=walk_nonzero_steps,
        reach_active_steps=reach_active_steps,
    )
