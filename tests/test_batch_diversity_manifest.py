"""Tests for batch manifest diversity summaries.

These checks protect scenario-provenance reporting so batch perturbation
coverage can be audited without loading MuJoCo trajectories.
"""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vla_bridge.batch_dataset_export import export_combined_batch_dataset
from vla_bridge.batch_diversity import summarize_manifest_diversity
from vla_bridge.batch_manifest import (
    BatchManifest,
    DemoRunRecord,
    STATUS_SUCCESS,
    read_batch_manifest,
    write_batch_manifest,
)


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")


def _demo_row(step_index: int, *, scenario_id: str, seed: int, dx: float, dy: float) -> dict:
    return {
        "step_index": step_index,
        "sim_time": float(step_index) * 0.02,
        "image_path": "frames/frame_000000.png",
        "instruction": "Pick up the red cylinder and place it on the blue table.",
        "phase": "SETTLE",
        "palm_world": [0.0, 0.0, 0.0],
        "pelvis_pos": [0.0, 0.0, 0.0],
        "pelvis_quat": [1.0, 0.0, 0.0, 0.0],
        "reach_target_pelvis": [0.3, -0.2, 0.2],
        "grip_closed": False,
        "walk_cmd": [0.0, 0.0, 0.0],
        "reach_active": False,
        "action_7d": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        "scenario_id": scenario_id,
        "seed": seed,
        "scenario": {"red_block_xy_offset_m": [dx, dy]},
    }


class TestBatchDiversityManifest(unittest.TestCase):
    def test_manifest_roundtrip_preserves_scenario_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "batch_manifest.json"
            manifest = BatchManifest(
                batch_id="batch_001",
                output_root=str(Path(tmp)),
                created_unix_time=1.0,
                num_requested=1,
                num_completed=1,
                num_failed=0,
                record_every=1,
                camera="head_cam",
                no_images=True,
                max_ticks=100,
                demos=[
                    DemoRunRecord(
                        demo_id="demo_000",
                        output_dir=str(Path(tmp) / "demo_000"),
                        metadata_path=str(Path(tmp) / "demo_000" / "demo.jsonl"),
                        summary_path=str(Path(tmp) / "demo_000" / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=2,
                        num_frames=0,
                        scenario_id="cyl_x_plus_02",
                        seed=101,
                        scenario={"red_block_xy_offset_m": [0.02, 0.0]},
                    )
                ],
                scenario_config_path="configs/scenarios/small_perturbations.json",
                scenario_config_name="small_perturbations_v1",
                scenario_count=5,
            )
            write_batch_manifest(path, manifest)
            restored = read_batch_manifest(path)
            self.assertEqual(restored, manifest)

    def test_diversity_summary_detects_multiple_offsets(self):
        manifest = BatchManifest(
            batch_id="batch_001",
            output_root="batch",
            created_unix_time=1.0,
            num_requested=2,
            num_completed=2,
            num_failed=0,
            record_every=1,
            camera="head_cam",
            no_images=True,
            max_ticks=100,
            demos=[
                DemoRunRecord(
                    demo_id="demo_000",
                    output_dir="batch/demo_000",
                    metadata_path="batch/demo_000/demo.jsonl",
                    summary_path="batch/demo_000/summary.json",
                    status=STATUS_SUCCESS,
                    done_reached=True,
                    num_steps=1,
                    num_frames=0,
                    scenario_id="nominal",
                    seed=0,
                    scenario={"red_block_xy_offset_m": [0.0, 0.0]},
                ),
                DemoRunRecord(
                    demo_id="demo_001",
                    output_dir="batch/demo_001",
                    metadata_path="batch/demo_001/demo.jsonl",
                    summary_path="batch/demo_001/summary.json",
                    status=STATUS_SUCCESS,
                    done_reached=True,
                    num_steps=1,
                    num_frames=0,
                    scenario_id="cyl_x_plus_02",
                    seed=101,
                    scenario={"red_block_xy_offset_m": [0.02, 0.0]},
                ),
            ],
        )
        summary = summarize_manifest_diversity(manifest)
        self.assertEqual(summary["num_unique_scenarios"], 2)
        self.assertFalse(summary["all_offsets_identical"])
        self.assertEqual(summary["dx_range_m"], [0.0, 0.02])

    def test_combined_export_preserves_scenario_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch_root = root / "batch_001"
            demo0 = batch_root / "demo_000"
            demo1 = batch_root / "demo_001"

            _write_jsonl(
                demo0 / "demo.jsonl",
                [_demo_row(0, scenario_id="nominal", seed=0, dx=0.0, dy=0.0)],
            )
            _write_jsonl(
                demo1 / "demo.jsonl",
                [_demo_row(0, scenario_id="cyl_y_plus_02", seed=103, dx=0.0, dy=0.02)],
            )

            manifest = BatchManifest(
                batch_id="batch_001",
                output_root=str(batch_root),
                created_unix_time=1.0,
                num_requested=2,
                num_completed=2,
                num_failed=0,
                record_every=1,
                camera="head_cam",
                no_images=True,
                max_ticks=100,
                demos=[
                    DemoRunRecord(
                        demo_id="demo_000",
                        output_dir=str(demo0),
                        metadata_path=str(demo0 / "demo.jsonl"),
                        summary_path=str(demo0 / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=1,
                        num_frames=0,
                        scenario_id="nominal",
                        seed=0,
                        scenario={"red_block_xy_offset_m": [0.0, 0.0]},
                    ),
                    DemoRunRecord(
                        demo_id="demo_001",
                        output_dir=str(demo1),
                        metadata_path=str(demo1 / "demo.jsonl"),
                        summary_path=str(demo1 / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=1,
                        num_frames=0,
                        scenario_id="cyl_y_plus_02",
                        seed=103,
                        scenario={"red_block_xy_offset_m": [0.0, 0.02]},
                    ),
                ],
            )
            manifest_path = batch_root / "batch_manifest.json"
            write_batch_manifest(manifest_path, manifest)

            out_dir = root / "export"
            summary = export_combined_batch_dataset(manifest_path, out_dir, drop_done=False)

            rows = [
                json.loads(line)
                for line in (out_dir / "dataset.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            self.assertEqual(len(rows), 2)
            self.assertIn("scenario_id", rows[0])
            self.assertIn("seed", rows[0])
            self.assertIn("scenario", rows[0])
            self.assertEqual(summary["num_unique_scenarios"], 2)
            self.assertEqual(set(summary["scenario_ids"]), {"nominal", "cyl_y_plus_02"})


if __name__ == "__main__":
    unittest.main()
