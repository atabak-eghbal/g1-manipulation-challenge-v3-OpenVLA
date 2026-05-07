from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from vla_bridge.dataset_audit import (
    action_array,
    action_statistics,
    boolean_balance,
    build_audit_report,
    find_idle_runs,
    magnitude_statistics,
    phase_counts,
    phase_temporal_split,
    phase_transition_counts,
    write_split_manifests,
)
from vla_bridge.g1_native_dataset import G1NativeVLARecord, read_dataset_jsonl


def make_record(
    i: int,
    *,
    phase: str = "SETTLE",
    walk=(0.0, 0.0, 0.0),
    reach=(0.3, -0.2, 0.2),
    reach_active: bool = False,
    grip_closed: bool = False,
) -> G1NativeVLARecord:
    action = (
        float(walk[0]),
        float(walk[1]),
        float(walk[2]),
        float(reach[0]),
        float(reach[1]),
        float(reach[2]),
        1.0 if reach_active else 0.0,
        1.0 if grip_closed else 0.0,
    )
    return G1NativeVLARecord(
        sample_index=i,
        source_step_index=i,
        image_path=f"frames/frame_{i:06d}.png",
        instruction="Pick up the red cylinder and place it on the blue table.",
        phase=phase,
        walk_cmd=tuple(float(x) for x in walk),
        reach_target_pelvis=tuple(float(x) for x in reach),
        reach_active=reach_active,
        grip_closed=grip_closed,
        action_vector=action,
    )


class TestG1NativeDatasetAudit(unittest.TestCase):
    def test_action_array_empty(self):
        arr = action_array([])
        self.assertEqual(arr.shape, (0, 8))

    def test_action_array_shape(self):
        records = [make_record(0), make_record(1)]
        arr = action_array(records)
        self.assertEqual(arr.shape, (2, 8))

    def test_phase_counts(self):
        records = [
            make_record(0, phase="A"),
            make_record(1, phase="B"),
            make_record(2, phase="A"),
        ]
        self.assertEqual(phase_counts(records), {"A": 2, "B": 1})

    def test_boolean_balance(self):
        records = [
            make_record(0, reach_active=False, grip_closed=False),
            make_record(1, reach_active=True, grip_closed=True),
        ]
        balance = boolean_balance(records)
        self.assertEqual(balance["reach_active_true"], 1)
        self.assertEqual(balance["grip_closed_true"], 1)
        self.assertAlmostEqual(balance["reach_active_true_fraction"], 0.5)

    def test_action_statistics(self):
        records = [
            make_record(0, walk=(0, 0, 0)),
            make_record(1, walk=(2, 0, 0)),
        ]
        stats = action_statistics(records)
        self.assertAlmostEqual(stats["walk_x"]["min"], 0.0)
        self.assertAlmostEqual(stats["walk_x"]["max"], 2.0)
        self.assertAlmostEqual(stats["walk_x"]["mean"], 1.0)

    def test_magnitude_statistics(self):
        records = [
            make_record(0, walk=(0, 0, 0)),
            make_record(1, walk=(3, 4, 0)),
        ]
        stats = magnitude_statistics(records)
        self.assertEqual(stats["zero_walk_records"], 1)
        self.assertEqual(stats["nonzero_walk_records"], 1)
        self.assertAlmostEqual(stats["max_walk_cmd_magnitude"], 5.0)

    def test_find_idle_runs(self):
        records = [make_record(i, phase="SETTLE") for i in range(30)]
        runs = find_idle_runs(records, min_run_length=25)
        self.assertEqual(len(runs), 1)
        self.assertEqual(runs[0]["length"], 30)
        self.assertEqual(runs[0]["phase"], "SETTLE")

    def test_phase_transition_counts(self):
        records = [
            make_record(0, phase="A"),
            make_record(1, phase="A"),
            make_record(2, phase="B"),
        ]
        segments = phase_transition_counts(records)
        self.assertEqual(len(segments), 2)
        self.assertEqual(segments[0]["phase"], "A")
        self.assertEqual(segments[0]["length"], 2)
        self.assertEqual(segments[1]["phase"], "B")

    def test_build_audit_report(self):
        records = [make_record(i) for i in range(30)]
        report = build_audit_report(records, source_dataset="test.jsonl")
        self.assertEqual(report["num_records"], 30)
        self.assertEqual(report["action_vector_shape"], [30, 8])
        self.assertIn("warnings", report)
        self.assertGreaterEqual(len(report["idle_runs"]), 1)

    def test_phase_temporal_split(self):
        records = []
        for i in range(10):
            records.append(make_record(i, phase="A"))
        for i in range(10, 20):
            records.append(make_record(i, phase="B"))

        train, val = phase_temporal_split(records, val_fraction=0.2)
        self.assertEqual(len(train), 16)
        self.assertEqual(len(val), 4)
        self.assertEqual(phase_counts(val), {"A": 2, "B": 2})

    def test_write_split_manifests(self):
        records = [make_record(i, phase="A") for i in range(10)]
        train, val = phase_temporal_split(records, val_fraction=0.2)

        with tempfile.TemporaryDirectory() as tmp:
            summary = write_split_manifests(tmp, train, val)
            root = Path(tmp)
            self.assertTrue((root / "train.jsonl").exists())
            self.assertTrue((root / "val.jsonl").exists())
            self.assertTrue((root / "split_summary.json").exists())
            self.assertEqual(summary["train_records"], 8)
            self.assertEqual(summary["val_records"], 2)

            loaded_train = read_dataset_jsonl(root / "train.jsonl")
            loaded_val = read_dataset_jsonl(root / "val.jsonl")
            self.assertEqual(len(loaded_train), 8)
            self.assertEqual(len(loaded_val), 2)


if __name__ == "__main__":
    unittest.main()
