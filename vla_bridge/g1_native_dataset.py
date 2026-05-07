"""G1-native VLA dataset export helpers.

Step 17 scope:
- no OpenVLA
- no model inference
- no fine-tuning
- pure supervised dataset export

The exported target is the G1-native command interface proven executable in
Step 16:

[walk_x, walk_y, walk_yaw, reach_x, reach_y, reach_z, reach_active, grip_closed]
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import json
import shutil

import numpy as np

from vla_bridge.demo_schema import VLADemoStep, as_float_tuple


@dataclass(frozen=True)
class G1NativeVLARecord:
    """One supervised record for the G1-native VLA dataset."""

    sample_index: int
    source_step_index: int
    image_path: str
    instruction: str
    phase: str

    walk_cmd: tuple[float, float, float]
    reach_target_pelvis: tuple[float, float, float]
    reach_active: bool
    grip_closed: bool

    action_vector: tuple[float, float, float, float, float, float, float, float]


def make_action_vector(
    walk_cmd: tuple[float, float, float],
    reach_target_pelvis: tuple[float, float, float],
    reach_active: bool,
    grip_closed: bool,
) -> tuple[float, float, float, float, float, float, float, float]:
    """Build the 8D action vector target."""
    walk = as_float_tuple(walk_cmd, 3, "walk_cmd")
    reach = as_float_tuple(reach_target_pelvis, 3, "reach_target_pelvis")
    return (
        float(walk[0]),
        float(walk[1]),
        float(walk[2]),
        float(reach[0]),
        float(reach[1]),
        float(reach[2]),
        1.0 if bool(reach_active) else 0.0,
        1.0 if bool(grip_closed) else 0.0,
    )


def _join_prefix(prefix: str, image_path: str) -> str:
    if not prefix:
        return image_path
    if not image_path:
        return ""
    return f"{prefix.rstrip('/')}/{image_path}"


def record_from_demo_step(
    step: VLADemoStep,
    sample_index: int,
    *,
    image_prefix: str = "",
    include_phase: bool = True,
) -> G1NativeVLARecord:
    """Map a VLADemoStep to a G1NativeVLARecord."""
    image_path = _join_prefix(image_prefix, step.image_path)
    phase = step.phase if include_phase else ""
    walk_cmd = as_float_tuple(step.walk_cmd, 3, "walk_cmd")
    reach_target = as_float_tuple(step.reach_target_pelvis, 3, "reach_target_pelvis")
    action_vector = make_action_vector(
        walk_cmd,
        reach_target,
        bool(step.reach_active),
        bool(step.grip_closed),
    )
    return G1NativeVLARecord(
        sample_index=int(sample_index),
        source_step_index=int(step.step_index),
        image_path=str(image_path),
        instruction=str(step.instruction),
        phase=str(phase),
        walk_cmd=walk_cmd,
        reach_target_pelvis=reach_target,
        reach_active=bool(step.reach_active),
        grip_closed=bool(step.grip_closed),
        action_vector=action_vector,
    )


def export_records_from_steps(
    steps: list[VLADemoStep],
    *,
    require_images: bool = True,
    include_phase: bool = True,
    image_prefix: str = "",
    drop_done: bool = True,
    drop_inactive_reach: bool = False,
) -> list[G1NativeVLARecord]:
    """Export multiple records from demo steps with filtering."""
    records: list[G1NativeVLARecord] = []
    for step in steps:
        if drop_done and step.phase == "DONE":
            continue
        if drop_inactive_reach and not step.reach_active:
            continue
        if require_images and not step.image_path:
            raise ValueError(
                f"Step {step.step_index} has no image_path but require_images=True"
            )
        records.append(
            record_from_demo_step(
                step,
                sample_index=len(records),
                image_prefix=image_prefix,
                include_phase=include_phase,
            )
        )
    return records


def record_to_json(record: G1NativeVLARecord) -> str:
    """Serialise record to compact JSON line."""
    return json.dumps(asdict(record), separators=(",", ":"))


def record_from_json(line: str) -> G1NativeVLARecord:
    """Parse JSON line into G1NativeVLARecord."""
    data = json.loads(line)
    return G1NativeVLARecord(
        sample_index=int(data["sample_index"]),
        source_step_index=int(data["source_step_index"]),
        image_path=str(data["image_path"]),
        instruction=str(data["instruction"]),
        phase=str(data.get("phase", "")),
        walk_cmd=as_float_tuple(data["walk_cmd"], 3, "walk_cmd"),
        reach_target_pelvis=as_float_tuple(
            data["reach_target_pelvis"], 3, "reach_target_pelvis"
        ),
        reach_active=bool(data["reach_active"]),
        grip_closed=bool(data["grip_closed"]),
        action_vector=as_float_tuple(data["action_vector"], 8, "action_vector"),
    )


def write_dataset_jsonl(path: str | Path, records: list[G1NativeVLARecord]) -> None:
    """Write records as JSONL."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(record_to_json(record) + "\n")


def read_dataset_jsonl(path: str | Path) -> list[G1NativeVLARecord]:
    """Read records from JSONL."""
    src = Path(path)
    records: list[G1NativeVLARecord] = []
    with src.open("r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                records.append(record_from_json(stripped))
    return records


def dataset_summary(records: list[G1NativeVLARecord]) -> dict[str, Any]:
    """Compute statistics for the exported records."""
    if not records:
        return {"num_records": 0}

    walk = np.asarray([r.walk_cmd for r in records], dtype=np.float64)
    reach = np.asarray([r.reach_target_pelvis for r in records], dtype=np.float64)
    walk_mag = np.linalg.norm(walk, axis=1)
    reach_norm = np.linalg.norm(reach, axis=1)
    phases = [r.phase for r in records]

    return {
        "num_records": len(records),
        "first_phase": phases[0],
        "last_phase": phases[-1],
        "unique_phases": sorted(set(phases)),
        "walk_nonzero_records": int(np.sum(walk_mag > 1e-9)),
        "reach_active_records": int(sum(r.reach_active for r in records)),
        "grip_closed_records": int(sum(r.grip_closed for r in records)),
        "mean_walk_cmd_magnitude": float(walk_mag.mean()),
        "max_walk_cmd_magnitude": float(walk_mag.max()),
        "mean_reach_target_norm": float(reach_norm.mean()),
        "max_reach_target_norm": float(reach_norm.max()),
    }


def write_summary(path: str | Path, summary: dict[str, Any]) -> None:
    """Write summary JSON."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")


def copy_images_for_records(
    records: list[G1NativeVLARecord],
    *,
    source_demo_dir: str | Path,
    output_images_dir: str | Path,
) -> list[G1NativeVLARecord]:
    """Copy images and update record paths."""
    src_root = Path(source_demo_dir)
    dst_root = Path(output_images_dir)
    dst_root.mkdir(parents=True, exist_ok=True)

    copied: list[G1NativeVLARecord] = []
    for record in records:
        if not record.image_path:
            raise ValueError(f"Record {record.sample_index} has empty image_path")

        src = src_root / record.image_path
        if not src.exists():
            raise FileNotFoundError(src)

        dst = dst_root / Path(record.image_path).name
        shutil.copy2(src, dst)

        copied.append(
            G1NativeVLARecord(
                sample_index=record.sample_index,
                source_step_index=record.source_step_index,
                image_path=f"images/{dst.name}",
                instruction=record.instruction,
                phase=record.phase,
                walk_cmd=record.walk_cmd,
                reach_target_pelvis=record.reach_target_pelvis,
                reach_active=record.reach_active,
                grip_closed=record.grip_closed,
                action_vector=record.action_vector,
            )
        )
    return copied
