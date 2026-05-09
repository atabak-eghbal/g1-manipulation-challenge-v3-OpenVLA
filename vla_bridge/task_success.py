"""Task-outcome tracking for scripted keyboard demos.

Pure helper — no MuJoCo, no OpenCV, no ONNX.
stdlib + math only.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from typing import Any


@dataclass
class TaskSuccessTracker:
    """Tracks grasp and placement outcome for one rollout."""

    source_table_z: float | None = None
    target_table_z: float | None = None
    lift_threshold_m: float = 0.05
    on_table_xy_tolerance_m: float = 0.35
    on_table_z_tolerance_m: float = 0.08

    ever_attached: bool = False
    attach_tick: int | None = None
    attach_phase: str = ""

    max_red_block_z: float | None = None
    final_red_block_world: tuple[float, float, float] | None = None
    final_target_center_world: tuple[float, float, float] | None = None

    object_lifted: bool = False
    object_on_target_table: bool = False
    task_success: bool = False
    failure_reason: str = ""

    def update_attachment(self, *, attached_now: bool, tick: int, phase: str) -> None:
        if attached_now and not self.ever_attached:
            self.ever_attached = True
            self.attach_tick = tick
            self.attach_phase = phase

    def update_object_position(self, red_block_world: tuple[float, float, float]) -> None:
        z = float(red_block_world[2])
        if self.max_red_block_z is None or z > self.max_red_block_z:
            self.max_red_block_z = z
        self.final_red_block_world = (
            float(red_block_world[0]),
            float(red_block_world[1]),
            float(red_block_world[2]),
        )

    def finalize(
        self,
        *,
        final_red_block_world: tuple[float, float, float],
        target_center_world: tuple[float, float, float],
        target_table_z: float,
    ) -> dict[str, Any]:
        self.final_red_block_world = tuple(float(x) for x in final_red_block_world)
        self.final_target_center_world = tuple(float(x) for x in target_center_world)
        self.target_table_z = float(target_table_z)

        height_above_target = float(final_red_block_world[2]) - float(target_table_z)
        xy_dist = math.sqrt(
            (float(final_red_block_world[0]) - float(target_center_world[0])) ** 2
            + (float(final_red_block_world[1]) - float(target_center_world[1])) ** 2
        )

        # object_lifted: must have attached and risen enough above source (or target) table
        if self.ever_attached and self.max_red_block_z is not None:
            lift_base = (
                self.source_table_z
                if self.source_table_z is not None
                else float(target_table_z)
            )
            self.object_lifted = self.max_red_block_z >= lift_base + self.lift_threshold_m
        else:
            self.object_lifted = False

        # object_on_target_table: z just above table surface, xy within tolerance
        on_z = 0.0 <= height_above_target <= self.on_table_z_tolerance_m
        on_xy = xy_dist <= self.on_table_xy_tolerance_m
        self.object_on_target_table = on_z and on_xy

        self.task_success = (
            self.ever_attached and self.object_lifted and self.object_on_target_table
        )

        if self.task_success:
            self.failure_reason = ""
        elif not self.ever_attached:
            self.failure_reason = "never_attached"
        elif not self.object_lifted:
            self.failure_reason = "object_not_lifted"
        elif not self.object_on_target_table:
            self.failure_reason = "object_not_on_target_table"
        else:
            self.failure_reason = "unknown_failure"

        return {
            "ever_attached": self.ever_attached,
            "attach_tick": self.attach_tick,
            "attach_phase": self.attach_phase,
            "object_lifted": self.object_lifted,
            "object_on_target_table": self.object_on_target_table,
            "task_success": self.task_success,
            "failure_reason": self.failure_reason,
            "max_red_block_z": self.max_red_block_z,
            "final_red_block_world": list(self.final_red_block_world),
            "final_target_center_world": list(self.final_target_center_world),
            "final_target_table_z": float(target_table_z),
            "final_height_above_target": float(height_above_target),
            "final_xy_distance_to_target": float(xy_dist),
        }
