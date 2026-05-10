"""Tests for combined G1-native batch dataset export.

These tests protect demo-selection, provenance fields, and merged dataset
schema contracts consumed by downstream audit/training-view tools.
"""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vla_bridge.batch_dataset_export import (
    _prefix_image_path,
    export_combined_batch_dataset,
    select_successful_demos,
)
from vla_bridge.batch_manifest import (
    STATUS_FAILED,
    STATUS_SUCCESS,
    DemoRunRecord,
    build_batch_manifest,
    write_batch_manifest,
)


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")


def _demo_row(step_index: int, *, phase: str = "SETTLE", image_path: str = "frames/frame_000000.png") -> dict:
    return {
        "step_index": step_index,
        "sim_time": float(step_index) * 0.02,
        "image_path": image_path,
        "instruction": "Pick up the red cylinder and place it on the blue table.",
        "phase": phase,
        "palm_world": [0.0, 0.0, 0.0],
        "pelvis_pos": [0.0, 0.0, 0.0],
        "pelvis_quat": [1.0, 0.0, 0.0, 0.0],
        "reach_target_pelvis": [0.3, -0.2, 0.2],
        "grip_closed": False,
        "walk_cmd": [0.0, 0.0, 0.0],
        "reach_active": False,
        "action_7d": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    }


class TestG1NativeBatchDatasetExport(unittest.TestCase):
    def test_select_successful_demos(self):
        manifest = build_batch_manifest(
            batch_id="batch_test",
            output_root="batch",
            num_requested=1,
            record_every=1,
            camera="head_cam",
            no_images=True,
            max_ticks=4000,
            demos=[
                DemoRunRecord(
                    demo_id="demo_000",
                    output_dir="batch/demo_000",
                    metadata_path="batch/demo_000/demo.jsonl",
                    summary_path="batch/demo_000/summary.json",
                    status=STATUS_SUCCESS,
                    done_reached=True,
                    num_steps=3,
                    num_frames=0,
                )
            ],
            created_unix_time=123.0,
        )
        selection = select_successful_demos(manifest)
        self.assertEqual(selection.selected_demo_ids, ["demo_000"])
        self.assertEqual(selection.skipped_demo_ids, [])

    def test_select_skips_failed_and_not_done(self):
        manifest = build_batch_manifest(
            batch_id="batch_test",
            output_root="batch",
            num_requested=2,
            record_every=1,
            camera="head_cam",
            no_images=True,
            max_ticks=4000,
            demos=[
                DemoRunRecord(
                    demo_id="demo_failed",
                    output_dir="batch/demo_failed",
                    metadata_path="batch/demo_failed/demo.jsonl",
                    summary_path="batch/demo_failed/summary.json",
                    status=STATUS_FAILED,
                    done_reached=False,
                    num_steps=0,
                    num_frames=0,
                    error="boom",
                ),
                DemoRunRecord(
                    demo_id="demo_not_done",
                    output_dir="batch/demo_not_done",
                    metadata_path="batch/demo_not_done/demo.jsonl",
                    summary_path="batch/demo_not_done/summary.json",
                    status=STATUS_SUCCESS,
                    done_reached=False,
                    num_steps=3,
                    num_frames=0,
                ),
            ],
            created_unix_time=123.0,
        )
        selection = select_successful_demos(manifest)
        self.assertEqual(selection.selected_demo_ids, [])
        self.assertEqual(selection.skipped_demo_ids, ["demo_failed", "demo_not_done"])
        self.assertIn("demo_failed", selection.skip_reasons)
        self.assertIn("demo_not_done", selection.skip_reasons)

    def test_prefix_image_path_empty(self):
        self.assertEqual(
            _prefix_image_path(
                "",
                demo_output_dir="batch/demo_000",
                batch_root="batch",
            ),
            "",
        )

    def test_prefix_image_path_relative(self):
        prefixed = _prefix_image_path(
            "frames/frame_000000.png",
            demo_output_dir="batch/demo_000",
            batch_root="batch",
        )
        self.assertEqual(prefixed, "demo_000/frames/frame_000000.png")

    def test_export_combined_batch_dataset(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch_root = root / "batch_000"

            demo0 = batch_root / "demo_000"
            demo1 = batch_root / "demo_001"

            _write_jsonl(
                demo0 / "demo.jsonl",
                [
                    _demo_row(0, phase="SETTLE", image_path="frames/frame_000000.png"),
                    _demo_row(1, phase="APPROACH_SOURCE", image_path="frames/frame_000001.png"),
                    _demo_row(2, phase="DONE", image_path="frames/frame_000002.png"),
                ],
            )
            _write_jsonl(
                demo1 / "demo.jsonl",
                [
                    _demo_row(0, phase="SETTLE", image_path="frames/frame_000000.png"),
                    _demo_row(1, phase="APPROACH_SOURCE", image_path="frames/frame_000001.png"),
                    _demo_row(2, phase="DONE", image_path="frames/frame_000002.png"),
                ],
            )

            manifest = build_batch_manifest(
                batch_id="batch_000",
                output_root=batch_root,
                num_requested=2,
                record_every=1,
                camera="head_cam",
                no_images=True,
                max_ticks=4000,
                demos=[
                    DemoRunRecord(
                        demo_id="demo_000",
                        output_dir=str(demo0),
                        metadata_path=str(demo0 / "demo.jsonl"),
                        summary_path=str(demo0 / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=3,
                        num_frames=0,
                    ),
                    DemoRunRecord(
                        demo_id="demo_001",
                        output_dir=str(demo1),
                        metadata_path=str(demo1 / "demo.jsonl"),
                        summary_path=str(demo1 / "summary.json"),
                        status=STATUS_SUCCESS,
                        done_reached=True,
                        num_steps=3,
                        num_frames=0,
                    ),
                ],
                created_unix_time=123.0,
            )

            manifest_path = batch_root / "batch_manifest.json"
            write_batch_manifest(manifest_path, manifest)

            out_dir = root / "export"
            summary = export_combined_batch_dataset(manifest_path, out_dir)

            dataset_path = out_dir / "dataset.jsonl"
            summary_path = out_dir / "summary.json"
            source_manifest_path = out_dir / "source_manifest.json"

            self.assertTrue(dataset_path.exists())
            self.assertTrue(summary_path.exists())
            self.assertTrue(source_manifest_path.exists())
            self.assertEqual(summary["num_selected_demos"], 2)
            self.assertEqual(summary["num_skipped_demos"], 0)

            rows = [
                json.loads(line)
                for line in dataset_path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]

            # DONE rows should be dropped by default, leaving 2 rows per demo.
            self.assertEqual(len(rows), 4)
            self.assertEqual([r["sample_index"] for r in rows], [0, 1, 2, 3])
            self.assertEqual([r["demo_sample_index"] for r in rows], [0, 1, 0, 1])
            self.assertEqual(rows[0]["batch_id"], "batch_000")
            self.assertEqual(rows[0]["demo_id"], "demo_000")
            self.assertEqual(rows[2]["demo_id"], "demo_001")
            self.assertEqual(rows[0]["image_path"], "demo_000/frames/frame_000000.png")

    def test_export_no_successful_demos_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch_root = root / "batch_000"
            manifest = build_batch_manifest(
                batch_id="batch_000",
                output_root=batch_root,
                num_requested=1,
                record_every=1,
                camera="head_cam",
                no_images=True,
                max_ticks=4000,
                demos=[
                    DemoRunRecord(
                        demo_id="demo_failed",
                        output_dir=str(batch_root / "demo_failed"),
                        metadata_path=str(batch_root / "demo_failed" / "demo.jsonl"),
                        summary_path=str(batch_root / "demo_failed" / "summary.json"),
                        status=STATUS_FAILED,
                        done_reached=False,
                        num_steps=0,
                        num_frames=0,
                        error="boom",
                    )
                ],
                created_unix_time=123.0,
            )
            manifest_path = batch_root / "batch_manifest.json"
            write_batch_manifest(manifest_path, manifest)
            with self.assertRaises(ValueError):
                export_combined_batch_dataset(manifest_path, root / "export")


if __name__ == "__main__":
    unittest.main()
