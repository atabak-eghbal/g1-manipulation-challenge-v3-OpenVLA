"""Combined batch dataset export helpers for G1-native VLA.

Step 21 scope:
- no OpenVLA
- no model inference
- no fine-tuning
- pure aggregation of successful batch demonstrations
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Sequence
import json

from vla_bridge.batch_manifest import (
    BatchManifest,
    STATUS_SUCCESS,
    read_batch_manifest,
)
from vla_bridge.demo_schema import read_jsonl
from vla_bridge.g1_native_dataset import (
    export_records_from_steps,
    dataset_summary,
    write_summary,
)


@dataclass(frozen=True)
class BatchExportSelection:
    """Summary of which demos were selected from a batch for export."""
    batch_id: str
    selected_demo_ids: list[str]
    selected_metadata_paths: list[str]
    skipped_demo_ids: list[str]
    skip_reasons: dict[str, str]


def select_successful_demos(manifest: BatchManifest) -> BatchExportSelection:
    """Filter manifest for successful demos that reached DONE."""
    selected_ids = []
    selected_paths = []
    skipped_ids = []
    reasons = {}

    for demo in manifest.demos:
        if demo.status != STATUS_SUCCESS:
            skipped_ids.append(demo.demo_id)
            reasons[demo.demo_id] = f"status={demo.status}"
            continue
        if not demo.done_reached:
            skipped_ids.append(demo.demo_id)
            reasons[demo.demo_id] = "done_reached=false"
            continue
        if not demo.metadata_path:
            skipped_ids.append(demo.demo_id)
            reasons[demo.demo_id] = "missing metadata_path"
            continue
        
        selected_ids.append(demo.demo_id)
        selected_paths.append(demo.metadata_path)

    return BatchExportSelection(
        batch_id=manifest.batch_id,
        selected_demo_ids=selected_ids,
        selected_metadata_paths=selected_paths,
        skipped_demo_ids=skipped_ids,
        skip_reasons=reasons,
    )


def load_demo_records(metadata_path: str | Path) -> list[Any]:
    """Load raw demo steps from a metadata path."""
    return read_jsonl(metadata_path)


def _load_demo_rows_json(metadata_path: str | Path) -> list[dict[str, Any]]:
    src = Path(metadata_path)
    rows: list[dict[str, Any]] = []
    with src.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _prefix_image_path(
    image_path: str,
    *,
    demo_output_dir: str | Path,
    batch_root: str | Path,
) -> str:
    """Prefix a relative image path with its demo directory name."""
    if not image_path:
        return ""
    
    path_obj = Path(image_path)
    if path_obj.is_absolute():
        return image_path
    
    # Try to make demo_output_dir relative to batch_root
    try:
        rel_demo_dir = Path(demo_output_dir).relative_to(Path(batch_root))
        return str(rel_demo_dir / image_path)
    except ValueError:
        # Fallback: just use the name of the demo directory
        return str(Path(demo_output_dir).name / image_path)


def export_combined_batch_dataset(
    manifest_path: str | Path,
    output_dir: str | Path,
    *,
    include_phase: bool = True,
    drop_done: bool = True,
    drop_inactive_reach: bool = False,
) -> dict[str, Any]:
    """Combine successful demos from a manifest into one G1-native dataset.

    Preserves per-sample provenance (batch/demo/sample/scenario identifiers) so
    later audits can trace each record back to its original rollout.
    """
    manifest_path = Path(manifest_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = read_batch_manifest(manifest_path)
    selection = select_successful_demos(manifest)

    if not selection.selected_metadata_paths:
        raise ValueError(f"No successful done demos found in manifest: {manifest_path}")

    combined: list[dict[str, Any]] = []
    records_per_demo = {}
    records_per_scenario: dict[str, int] = {}
    unique_scenario_ids: set[str] = set()

    global_index = 0
    demo_lookup = {d.demo_id: d for d in manifest.demos}

    for demo_id, metadata_path in zip(selection.selected_demo_ids, selection.selected_metadata_paths):
        demo_record = demo_lookup[demo_id]
        
        # Load raw demo steps
        steps = load_demo_records(metadata_path)
        source_rows = _load_demo_rows_json(metadata_path)
        source_by_step_index = {
            int(row.get("step_index", i)): row
            for i, row in enumerate(source_rows)
        }
        
        # Convert to G1-native records using existing logic
        native_records = export_records_from_steps(
            steps,
            require_images=False,  # Don't fail here if some frames are missing
            include_phase=include_phase,
            drop_done=drop_done,
            drop_inactive_reach=drop_inactive_reach,
        )

        records_per_demo[demo_id] = len(native_records)

        for demo_sample_index, rec in enumerate(native_records):
            row = asdict(rec)
            # Override/Add fields
            row["sample_index"] = global_index
            row["batch_id"] = manifest.batch_id
            row["demo_id"] = demo_id
            row["demo_sample_index"] = demo_sample_index
            row["image_path"] = _prefix_image_path(
                str(row.get("image_path", "")),
                demo_output_dir=demo_record.output_dir,
                batch_root=manifest.output_root,
            )
            source_row = source_by_step_index.get(int(getattr(rec, "source_step_index", -1)), {})
            scenario_id = source_row.get("scenario_id", demo_record.scenario_id or "")
            seed = source_row.get("seed", demo_record.seed)
            scenario_meta = source_row.get("scenario", demo_record.scenario if demo_record.scenario is not None else {})
            if scenario_meta is None:
                scenario_meta = {}
            row["scenario_id"] = str(scenario_id)
            row["seed"] = seed
            row["scenario"] = scenario_meta
            records_per_scenario[row["scenario_id"]] = records_per_scenario.get(row["scenario_id"], 0) + 1
            unique_scenario_ids.add(row["scenario_id"])
            combined.append(row)
            global_index += 1

    dataset_path = output_dir / "dataset.jsonl"
    summary_path = output_dir / "summary.json"
    source_manifest_copy_path = output_dir / "source_manifest.json"

    # Write combined JSONL (using dicts)
    with dataset_path.open("w", encoding="utf-8") as f:
        for row in combined:
            f.write(json.dumps(row, separators=(",", ":")) + "\n")

    # Reuse summary logic (it works on G1NativeVLARecord or dicts with same fields)
    # Actually dataset_summary uses r.walk_cmd etc, so it expects objects.
    # Let's mock objects for summary or just use the dicts if it works.
    # dataset_summary implementation uses: walk = np.asarray([r.walk_cmd for r in records], ...)
    # In Python, r['walk_cmd'] would be needed for dicts.
    # I'll convert back to a simple namespace or just re-read if needed, 
    # but better to just pass objects to it.
    
    # Let's create dummy objects for summary
    class RecordMock:
        def __init__(self, d):
            self.walk_cmd = d["walk_cmd"]
            self.reach_target_pelvis = d["reach_target_pelvis"]
            self.phase = d["phase"]
            self.reach_active = d["reach_active"]
            self.grip_closed = d["grip_closed"]

    mock_records = [RecordMock(r) for r in combined]
    base_summary = dataset_summary(mock_records) # type: ignore

    summary = {
        **base_summary,
        "batch_id": manifest.batch_id,
        "source_manifest_path": str(manifest_path),
        "output_dir": str(output_dir),
        "dataset_path": str(dataset_path),
        "summary_path": str(summary_path),
        "source_manifest_copy_path": str(source_manifest_copy_path),
        "num_demos_in_manifest": len(manifest.demos),
        "num_selected_demos": len(selection.selected_demo_ids),
        "num_skipped_demos": len(selection.skipped_demo_ids),
        "selected_demo_ids": selection.selected_demo_ids,
        "skipped_demo_ids": selection.skipped_demo_ids,
        "skip_reasons": selection.skip_reasons,
        "records_per_demo": records_per_demo,
        "scenario_ids": sorted(unique_scenario_ids),
        "num_unique_scenarios": len(unique_scenario_ids),
        "records_per_scenario": records_per_scenario,
        "include_phase": include_phase,
        "drop_done": drop_done,
        "drop_inactive_reach": drop_inactive_reach,
        "action_vector": [
            "walk_x", "walk_y", "walk_yaw",
            "reach_x", "reach_y", "reach_z",
            "reach_active", "grip_closed"
        ]
    }

    write_summary(summary_path, summary)

    source_manifest_payload = {
        "selection": asdict(selection),
        "source_manifest": asdict(manifest),
    }
    source_manifest_copy_path.write_text(
        json.dumps(source_manifest_payload, indent=2),
        encoding="utf-8",
    )

    return summary
