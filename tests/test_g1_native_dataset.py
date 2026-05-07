from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from vla_bridge.demo_schema import VLADemoStep
from vla_bridge.g1_native_dataset import (
    G1NativeVLARecord,
    copy_images_for_records,
    dataset_summary,
    export_records_from_steps,
    make_action_vector,
    read_dataset_jsonl,
    record_from_demo_step,
    record_from_json,
    record_to_json,
    write_dataset_jsonl,
)


def make_demo_step(
    i: int = 0,
    *,
    phase: str = "SETTLE",
    image_path: str = "frames/frame_000000.png",
    walk_cmd=(0.1, 0.0, 0.2),
    reach_active: bool = True,
    grip_closed: bool = False,
) -> VLADemoStep:
    return VLADemoStep(
        step_index=i,
        sim_time=float(i) * 0.02,
        image_path=image_path,
        instruction="Pick up the red cylinder and place it on the blue table.",
        phase=phase,
        palm_world=(0.1, 0.2, 0.3),
        pelvis_pos=(0.0, 0.0, 0.76),
        pelvis_quat=(1.0, 0.0, 0.0, 0.0),
        walk_cmd=tuple(float(x) for x in walk_cmd),
        reach_target_pelvis=(0.3, -0.2, 0.2),
        reach_active=reach_active,
        grip_closed=grip_closed,
        action_7d=(0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 if grip_closed else 0.0),
    )


class TestG1NativeDataset(unittest.TestCase):
    def test_make_action_vector(self):
        out = make_action_vector((1, 2, 3), (4, 5, 6), True, False)
        self.assertEqual(out, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 1.0, 0.0))
        self.assertEqual(len(out), 8)

    def test_make_action_vector_boolean_mapping(self):
        out = make_action_vector((0, 0, 0), (0, 0, 0), False, True)
        self.assertEqual(out[-2:], (0.0, 1.0))

    def test_record_from_demo_step(self):
        step = make_demo_step(7, grip_closed=True)
        rec = record_from_demo_step(step, sample_index=3)
        self.assertEqual(rec.sample_index, 3)
        self.assertEqual(rec.source_step_index, 7)
        self.assertEqual(rec.image_path, step.image_path)
        self.assertEqual(rec.walk_cmd, step.walk_cmd)
        self.assertEqual(rec.reach_target_pelvis, step.reach_target_pelvis)
        self.assertTrue(rec.reach_active)
        self.assertTrue(rec.grip_closed)
        self.assertEqual(len(rec.action_vector), 8)

    def test_record_from_demo_step_with_prefix(self):
        step = make_demo_step()
        rec = record_from_demo_step(step, sample_index=0, image_prefix="demo_002")
        self.assertEqual(rec.image_path, "demo_002/frames/frame_000000.png")

    def test_export_drops_done_by_default(self):
        steps = [make_demo_step(0, phase="SETTLE"), make_demo_step(1, phase="DONE")]
        records = export_records_from_steps(steps)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].phase, "SETTLE")

    def test_export_can_keep_done(self):
        steps = [make_demo_step(0, phase="SETTLE"), make_demo_step(1, phase="DONE")]
        records = export_records_from_steps(steps, drop_done=False)
        self.assertEqual(len(records), 2)

    def test_export_can_drop_inactive_reach(self):
        steps = [
            make_demo_step(0, reach_active=False),
            make_demo_step(1, reach_active=True),
        ]
        records = export_records_from_steps(steps, drop_inactive_reach=True)
        self.assertEqual(len(records), 1)
        self.assertTrue(records[0].reach_active)

    def test_missing_image_raises_when_required(self):
        steps = [make_demo_step(0, image_path="")]
        with self.assertRaises(ValueError):
            export_records_from_steps(steps, require_images=True)

    def test_json_roundtrip(self):
        rec = record_from_demo_step(make_demo_step(2), sample_index=0)
        restored = record_from_json(record_to_json(rec))
        self.assertEqual(restored, rec)

    def test_jsonl_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "dataset.jsonl"
            records = [
                record_from_demo_step(make_demo_step(0), sample_index=0),
                record_from_demo_step(make_demo_step(1), sample_index=1),
            ]
            write_dataset_jsonl(path, records)
            restored = read_dataset_jsonl(path)
            self.assertEqual(restored, records)

    def test_dataset_summary(self):
        records = [
            record_from_demo_step(make_demo_step(0, walk_cmd=(0, 0, 0), reach_active=False), sample_index=0),
            record_from_demo_step(make_demo_step(1, walk_cmd=(3, 4, 0), reach_active=True, grip_closed=True), sample_index=1),
        ]
        summary = dataset_summary(records)
        self.assertEqual(summary["num_records"], 2)
        self.assertEqual(summary["walk_nonzero_records"], 1)
        self.assertEqual(summary["reach_active_records"], 1)
        self.assertEqual(summary["grip_closed_records"], 1)
        self.assertAlmostEqual(summary["max_walk_cmd_magnitude"], 5.0)

    def test_copy_images_for_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "demo"
            frames = source / "frames"
            frames.mkdir(parents=True)
            img = frames / "frame_000000.png"
            img.write_bytes(b"fake image")

            out_images = root / "export" / "images"
            record = record_from_demo_step(make_demo_step(0), sample_index=0)
            copied = copy_images_for_records(
                [record],
                source_demo_dir=source,
                output_images_dir=out_images,
            )
            self.assertEqual(copied[0].image_path, "images/frame_000000.png")
            self.assertTrue((out_images / "frame_000000.png").exists())


if __name__ == "__main__":
    unittest.main()
