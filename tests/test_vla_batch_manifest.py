from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from vla_bridge.batch_manifest import (
    STATUS_FAILED,
    STATUS_SUCCESS,
    build_batch_manifest,
    demo_record_from_summary,
    failed_demo_record,
    make_demo_id,
    manifest_summary,
    read_batch_manifest,
    successful_demo_paths,
    write_batch_manifest,
)


class TestVLABatchManifest(unittest.TestCase):
    def test_make_demo_id(self):
        self.assertEqual(make_demo_id(0), "demo_000")
        self.assertEqual(make_demo_id(12), "demo_012")
        self.assertEqual(make_demo_id(123), "demo_123")

    def test_make_demo_id_negative_raises(self):
        with self.assertRaises(ValueError):
            make_demo_id(-1)

    def test_demo_record_from_summary(self):
        summary = {
            "done_reached": True,
            "num_steps": 2665,
            "num_frames": 2665,
        }
        record = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary=summary,
        )
        self.assertEqual(record.demo_id, "demo_000")
        self.assertEqual(record.status, STATUS_SUCCESS)
        self.assertTrue(record.done_reached)
        self.assertEqual(record.num_steps, 2665)
        self.assertEqual(record.num_frames, 2665)
        self.assertTrue(record.metadata_path.endswith("demo.jsonl"))
        self.assertTrue(record.summary_path.endswith("summary.json"))

    def test_failed_demo_record(self):
        record = failed_demo_record(
            demo_id="demo_001",
            output_dir="batch/demo_001",
            error="boom",
        )
        self.assertEqual(record.status, STATUS_FAILED)
        self.assertFalse(record.done_reached)
        self.assertEqual(record.num_steps, 0)
        self.assertEqual(record.num_frames, 0)
        self.assertEqual(record.error, "boom")

    def test_build_batch_manifest_counts(self):
        success = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary={"done_reached": True, "num_steps": 10, "num_frames": 10},
        )
        failed = failed_demo_record(
            demo_id="demo_001",
            output_dir="batch/demo_001",
            error="boom",
        )
        manifest = build_batch_manifest(
            batch_id="batch_000",
            output_root="batch",
            num_requested=2,
            record_every=1,
            camera="head_cam",
            no_images=False,
            max_ticks=4000,
            demos=[success, failed],
            created_unix_time=123.0,
        )
        self.assertEqual(manifest.num_completed, 1)
        self.assertEqual(manifest.num_failed, 1)
        self.assertEqual(manifest.created_unix_time, 123.0)

    def test_manifest_roundtrip(self):
        record = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary={"done_reached": True, "num_steps": 10, "num_frames": 5},
        )
        manifest = build_batch_manifest(
            batch_id="batch_000",
            output_root="batch",
            num_requested=1,
            record_every=1,
            camera="head_cam",
            no_images=False,
            max_ticks=4000,
            demos=[record],
            created_unix_time=123.0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "batch_manifest.json"
            write_batch_manifest(path, manifest)
            restored = read_batch_manifest(path)
            self.assertEqual(restored, manifest)

    def test_successful_demo_paths(self):
        done = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary={"done_reached": True, "num_steps": 10, "num_frames": 10},
        )
        not_done = demo_record_from_summary(
            demo_id="demo_001",
            output_dir="batch/demo_001",
            summary={"done_reached": False, "num_steps": 10, "num_frames": 10},
        )
        failed = failed_demo_record(
            demo_id="demo_002",
            output_dir="batch/demo_002",
            error="boom",
        )
        manifest = build_batch_manifest(
            batch_id="batch_000",
            output_root="batch",
            num_requested=3,
            record_every=1,
            camera="head_cam",
            no_images=False,
            max_ticks=4000,
            demos=[done, not_done, failed],
            created_unix_time=123.0,
        )
        paths = successful_demo_paths(manifest)
        self.assertEqual(paths, [done.metadata_path])

    def test_manifest_summary(self):
        a = demo_record_from_summary(
            demo_id="demo_000",
            output_dir="batch/demo_000",
            summary={"done_reached": True, "num_steps": 10, "num_frames": 5},
        )
        b = demo_record_from_summary(
            demo_id="demo_001",
            output_dir="batch/demo_001",
            summary={"done_reached": True, "num_steps": 20, "num_frames": 6},
        )
        manifest = build_batch_manifest(
            batch_id="batch_000",
            output_root="batch",
            num_requested=2,
            record_every=1,
            camera="head_cam",
            no_images=False,
            max_ticks=4000,
            demos=[a, b],
            created_unix_time=123.0,
        )
        summary = manifest_summary(manifest)
        self.assertEqual(summary["successful_done_demos"], 2)
        self.assertEqual(summary["total_steps"], 30)
        self.assertEqual(summary["total_frames"], 11)
        self.assertEqual(summary["demo_ids"], ["demo_000", "demo_001"])


if __name__ == "__main__":
    unittest.main()
