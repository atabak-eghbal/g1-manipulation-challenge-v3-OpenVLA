"""Batch manifest helpers for multi-demo VLA collection.

Step 20 scope:
- no OpenVLA
- no model inference
- no training
- pure manifest bookkeeping for multiple FSM teacher demonstrations
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import json
import time


STATUS_SUCCESS = "success"
STATUS_FAILED = "failed"


@dataclass(frozen=True)
class DemoRunRecord:
    """Detailed record of a single demonstration rollout in a batch.

    Includes scenario provenance (scenario_id/seed/scenario metadata) so
    downstream export/audit tools can track which perturbation produced each run.
    """
    demo_id: str
    output_dir: str
    metadata_path: str
    summary_path: str
    status: str
    done_reached: bool
    num_steps: int
    num_frames: int
    error: str = ""
    scenario_id: str = ""
    seed: int | None = None
    scenario: dict[str, Any] | None = None


@dataclass(frozen=True)
class BatchManifest:
    """Summary of a batch of demonstration rollouts."""
    batch_id: str
    output_root: str
    created_unix_time: float
    num_requested: int
    num_completed: int
    num_failed: int
    record_every: int
    camera: str
    no_images: bool
    max_ticks: int
    demos: list[DemoRunRecord]
    scenario_config_path: str = ""
    scenario_config_name: str = ""
    scenario_count: int = 0


def make_demo_id(index: int) -> str:
    """Return a zero-padded demo ID like 'demo_001'."""
    if index < 0:
        raise ValueError("index must be non-negative")
    return f"demo_{index:03d}"


def demo_record_from_summary(
    *,
    demo_id: str,
    output_dir: str | Path,
    summary: dict[str, Any],
    status: str = STATUS_SUCCESS,
    error: str = "",
    scenario_id: str = "",
    seed: int | None = None,
    scenario: dict[str, Any] | None = None,
) -> DemoRunRecord:
    """Build a DemoRunRecord from a recording summary."""
    out = Path(output_dir)
    return DemoRunRecord(
        demo_id=str(demo_id),
        output_dir=str(out),
        metadata_path=str(out / "demo.jsonl"),
        summary_path=str(out / "summary.json"),
        status=str(status),
        done_reached=bool(summary.get("done_reached", False)),
        num_steps=int(summary.get("num_steps", 0)),
        num_frames=int(summary.get("num_frames", 0)),
        error=str(error),
        scenario_id=str(scenario_id or summary.get("scenario_id", "")),
        seed=seed if seed is not None else summary.get("seed"),
        scenario=scenario if scenario is not None else summary.get("scenario"),
    )


def failed_demo_record(
    *,
    demo_id: str,
    output_dir: str | Path,
    error: str,
    scenario_id: str = "",
    seed: int | None = None,
    scenario: dict[str, Any] | None = None,
) -> DemoRunRecord:
    """Build a DemoRunRecord for a failed recording attempt."""
    out = Path(output_dir)
    return DemoRunRecord(
        demo_id=str(demo_id),
        output_dir=str(out),
        metadata_path=str(out / "demo.jsonl"),
        summary_path=str(out / "summary.json"),
        status=STATUS_FAILED,
        done_reached=False,
        num_steps=0,
        num_frames=0,
        error=str(error),
        scenario_id=str(scenario_id),
        seed=seed,
        scenario=scenario,
    )


def build_batch_manifest(
    *,
    batch_id: str,
    output_root: str | Path,
    num_requested: int,
    record_every: int,
    camera: str,
    no_images: bool,
    max_ticks: int,
    demos: list[DemoRunRecord],
    created_unix_time: float | None = None,
    scenario_config_path: str = "",
    scenario_config_name: str = "",
    scenario_count: int = 0,
) -> BatchManifest:
    """Aggregate demo records into a batch manifest."""
    num_completed = sum(1 for d in demos if d.status == STATUS_SUCCESS)
    num_failed = sum(1 for d in demos if d.status == STATUS_FAILED)
    return BatchManifest(
        batch_id=str(batch_id),
        output_root=str(output_root),
        created_unix_time=float(time.time() if created_unix_time is None else created_unix_time),
        num_requested=int(num_requested),
        num_completed=int(num_completed),
        num_failed=int(num_failed),
        record_every=int(record_every),
        camera=str(camera),
        no_images=bool(no_images),
        max_ticks=int(max_ticks),
        demos=list(demos),
        scenario_config_path=str(scenario_config_path),
        scenario_config_name=str(scenario_config_name),
        scenario_count=int(scenario_count),
    )


def manifest_to_dict(manifest: BatchManifest) -> dict[str, Any]:
    """Serialise manifest to dict."""
    return asdict(manifest)


def write_batch_manifest(path: str | Path, manifest: BatchManifest) -> None:
    """Write manifest to JSON with indentation."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest_to_dict(manifest), indent=2), encoding="utf-8")


def read_batch_manifest(path: str | Path) -> BatchManifest:
    """Read manifest from JSON."""
    src = Path(path)
    data = json.loads(src.read_text(encoding="utf-8"))
    demos = []
    for row in data.get("demos", []):
        row = dict(row)
        row.setdefault("scenario_id", "")
        row.setdefault("seed", None)
        row.setdefault("scenario", None)
        demos.append(DemoRunRecord(**row))
    data = dict(data)
    data["demos"] = demos
    data.setdefault("scenario_config_path", "")
    data.setdefault("scenario_config_name", "")
    data.setdefault("scenario_count", 0)
    return BatchManifest(**data)


def successful_demo_paths(manifest: BatchManifest) -> list[str]:
    """Return list of metadata paths for successful demos that reached DONE."""
    return [
        d.metadata_path
        for d in manifest.demos
        if d.status == STATUS_SUCCESS and d.done_reached
    ]


def manifest_summary(manifest: BatchManifest) -> dict[str, Any]:
    """Compute statistics for the batch manifest."""
    successful_done = [
        d for d in manifest.demos
        if d.status == STATUS_SUCCESS and d.done_reached
    ]
    return {
        "batch_id": manifest.batch_id,
        "num_requested": int(manifest.num_requested),
        "num_completed": int(manifest.num_completed),
        "num_failed": int(manifest.num_failed),
        "successful_done_demos": int(len(successful_done)),
        "total_steps": int(sum(d.num_steps for d in manifest.demos)),
        "total_frames": int(sum(d.num_frames for d in manifest.demos)),
        "demo_ids": [d.demo_id for d in manifest.demos],
    }
