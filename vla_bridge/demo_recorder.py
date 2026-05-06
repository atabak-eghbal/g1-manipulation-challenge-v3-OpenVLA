"""Recorder for FSM teacher demonstrations in VLA-style format.

Step 14 scope:
- watch the existing FSM teacher
- save synchronized observations and derived 7D teacher actions
- do not control the robot
- do not load OpenVLA

Step 16 additions:
- walk_cmd and reach_active recorded in _PendingStep and VLADemoStep
"""
from __future__ import annotations

from pathlib import Path
from typing import NamedTuple

import numpy as np

from vla_bridge.demo_schema import (
    VLADemoStep,
    as_float_tuple,
    make_action_7d,
    write_jsonl,
)


class _PendingStep(NamedTuple):
    step_index: int
    sim_time: float
    image_path: str
    instruction: str
    phase: str
    palm_world: tuple[float, float, float]
    pelvis_pos: tuple[float, float, float]
    pelvis_quat: tuple[float, float, float, float]
    walk_cmd: tuple[float, float, float]
    reach_target_pelvis: tuple[float, float, float]
    reach_active: bool
    grip_closed: bool


class VLADemoRecorder:
    """Record FSM teacher observations and derived 7D palm-delta actions.

    The 7D action at step *t* is defined as the palm displacement between
    step *t* and step *t+1*, so each observation is held as a *pending* record
    until the next observation arrives to supply the second palm position.
    The last observation in a rollout is finalized with a zero-displacement
    action when :meth:`finalize` is called.
    """

    def __init__(
        self,
        output_dir: str | Path,
        instruction: str,
        record_every: int = 5,
        camera_name: str = "head_cam",
    ) -> None:
        if record_every <= 0:
            raise ValueError("record_every must be positive")
        self.output_dir = Path(output_dir)
        self.frames_dir = self.output_dir / "frames"
        self.metadata_path = self.output_dir / "demo.jsonl"
        self.instruction = instruction
        self.record_every = int(record_every)
        self.camera_name = camera_name
        self.frames_dir.mkdir(parents=True, exist_ok=True)

        self._steps: list[VLADemoStep] = []
        self._pending: _PendingStep | None = None
        self._num_observations: int = 0

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def steps(self) -> list[VLADemoStep]:
        """Return a copy of the finalized steps list."""
        return list(self._steps)

    def should_record(self, control_tick: int) -> bool:
        """Return True when *control_tick* falls on a recording boundary."""
        return int(control_tick) % self.record_every == 0

    def observe(
        self,
        *,
        control_tick: int,
        sim_time: float,
        rgb: np.ndarray | None,
        phase: str,
        palm_world: np.ndarray,
        pelvis_pos: np.ndarray,
        pelvis_quat: np.ndarray,
        walk_cmd: tuple[float, float, float],
        reach_target_pelvis: tuple[float, float, float],
        reach_active: bool,
        grip_closed: bool,
    ) -> None:
        """Record one observation frame from the FSM teacher.

        If *control_tick* does not fall on a recording boundary the call is a
        no-op.  Otherwise the previous pending record (if any) is finalized
        using the current *palm_world* as the next palm position, and the
        current observation is stored as the new pending record.
        """
        if not self.should_record(control_tick):
            return

        palm_tuple = as_float_tuple(palm_world, 3, "palm_world")
        pelvis_pos_tuple = as_float_tuple(pelvis_pos, 3, "pelvis_pos")
        pelvis_quat_tuple = as_float_tuple(pelvis_quat, 4, "pelvis_quat")
        walk_tuple = as_float_tuple(walk_cmd, 3, "walk_cmd")
        reach_tuple = as_float_tuple(reach_target_pelvis, 3, "reach_target_pelvis")

        image_path = ""
        if rgb is not None:
            image_path = self._save_frame(rgb, self._num_observations)

        if self._pending is not None:
            action_7d = make_action_7d(
                np.asarray(self._pending.palm_world, dtype=np.float64),
                np.asarray(palm_tuple, dtype=np.float64),
                self._pending.grip_closed,
            )
            self._steps.append(
                VLADemoStep(
                    step_index=self._pending.step_index,
                    sim_time=self._pending.sim_time,
                    image_path=self._pending.image_path,
                    instruction=self._pending.instruction,
                    phase=self._pending.phase,
                    palm_world=self._pending.palm_world,
                    pelvis_pos=self._pending.pelvis_pos,
                    pelvis_quat=self._pending.pelvis_quat,
                    walk_cmd=self._pending.walk_cmd,
                    reach_target_pelvis=self._pending.reach_target_pelvis,
                    reach_active=self._pending.reach_active,
                    grip_closed=self._pending.grip_closed,
                    action_7d=action_7d,
                )
            )

        self._pending = _PendingStep(
            step_index=int(control_tick),
            sim_time=float(sim_time),
            image_path=image_path,
            instruction=self.instruction,
            phase=str(phase),
            palm_world=palm_tuple,
            pelvis_pos=pelvis_pos_tuple,
            pelvis_quat=pelvis_quat_tuple,
            walk_cmd=walk_tuple,
            reach_target_pelvis=reach_tuple,
            reach_active=bool(reach_active),
            grip_closed=bool(grip_closed),
        )
        self._num_observations += 1

    def finalize(self) -> None:
        """Finalize the last pending record with a zero action and write JSONL.

        Must be called once at the end of a rollout.  Calling more than once
        is safe (subsequent calls are no-ops after the pending record is gone).
        """
        if self._pending is not None:
            zero_action: tuple[float, float, float, float, float, float, float] = (
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0 if self._pending.grip_closed else 0.0,
            )
            self._steps.append(
                VLADemoStep(
                    step_index=self._pending.step_index,
                    sim_time=self._pending.sim_time,
                    image_path=self._pending.image_path,
                    instruction=self._pending.instruction,
                    phase=self._pending.phase,
                    palm_world=self._pending.palm_world,
                    pelvis_pos=self._pending.pelvis_pos,
                    pelvis_quat=self._pending.pelvis_quat,
                    walk_cmd=self._pending.walk_cmd,
                    reach_target_pelvis=self._pending.reach_target_pelvis,
                    reach_active=self._pending.reach_active,
                    grip_closed=self._pending.grip_closed,
                    action_7d=zero_action,
                )
            )
            self._pending = None
        write_jsonl(self.metadata_path, self._steps)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _save_frame(self, rgb: np.ndarray, frame_index: int) -> str:
        """Save an RGB frame and return its relative path string.

        Tries cv2 first; falls back to NumPy .npy if cv2 is unavailable or
        fails.  *rgb* must have shape (H, W, 3).
        """
        arr = np.asarray(rgb)
        if arr.ndim != 3 or arr.shape[2] != 3:
            raise ValueError(f"rgb must have shape (H, W, 3), got {arr.shape}")

        rel_png = Path("frames") / f"frame_{frame_index:06d}.png"
        out_png = self.output_dir / rel_png
        try:
            import cv2  # type: ignore

            bgr = arr[..., ::-1]
            ok = cv2.imwrite(str(out_png), bgr)
            if not ok:
                raise RuntimeError(f"cv2.imwrite failed for {out_png}")
            return rel_png.as_posix()
        except Exception:
            rel_npy = Path("frames") / f"frame_{frame_index:06d}.npy"
            out_npy = self.output_dir / rel_npy
            np.save(str(out_npy), arr)
            return rel_npy.as_posix()
