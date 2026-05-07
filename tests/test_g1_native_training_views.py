from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np

from vla_bridge.g1_native_dataset import G1NativeVLARecord, read_dataset_jsonl
from vla_bridge.training_views import (
    build_training_views,
    build_weight_records,
    compute_phase_weights,
    filter_idle_records,
    is_idle_record,
    normalize_weights,
    read_weight_jsonl,
    training_view_summary,
    walk_magnitude,
    write_weight_jsonl,
)


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


class TestG1NativeTrainingViews(unittest.TestCase):
    def test_walk_magnitude(self):
        record = make_record(0, walk=(3, 4, 0))
        self.assertAlmostEqual(walk_magnitude(record), 5.0)

    def test_is_idle_record(self):
        self.assertTrue(is_idle_record(make_record(0)))
        self.assertFalse(is_idle_record(make_record(1, walk=(0.1, 0, 0))))
        self.assertFalse(is_idle_record(make_record(2, reach_active=True)))
        self.assertFalse(is_idle_record(make_record(3, grip_closed=True)))

    def test_rare_transition_is_not_idle(self):
        self.assertFalse(is_idle_record(make_record(0, phase="CLOSE_GRIP")))
        self.assertFalse(is_idle_record(make_record(1, phase="OPEN_GRIP")))

    def test_filter_idle_records_keeps_first_n_idle(self):
        records = [make_record(i) for i in range(20)]
        filtered = filter_idle_records(records, keep_first_n_idle=5)
        self.assertEqual(len(filtered), 5)
        self.assertEqual([r.sample_index for r in filtered], [0, 1, 2, 3, 4])

    def test_filter_preserves_rare_transitions(self):
        records = [make_record(i) for i in range(10)]
        records.append(make_record(10, phase="CLOSE_GRIP"))
        records.append(make_record(11, phase="OPEN_GRIP"))
        filtered = filter_idle_records(records, keep_first_n_idle=0)
        phases = [r.phase for r in filtered]
        self.assertIn("CLOSE_GRIP", phases)
        self.assertIn("OPEN_GRIP", phases)

    def test_compute_phase_weights_rare_higher_than_common(self):
        records = []
        for i in range(100):
            records.append(make_record(i, phase="APPROACH_TARGET", reach_active=True))
        records.append(make_record(100, phase="CLOSE_GRIP", grip_closed=True))
        weights = compute_phase_weights(records, max_weight=100.0, rare_phase_boost=5.0)
        self.assertGreater(weights[100], weights[0])

    def test_normalize_weights_mean_one(self):
        weights = {0: 1.0, 1: 3.0}
        normalized = normalize_weights(weights)
        self.assertAlmostEqual(np.mean(list(normalized.values())), 1.0)

    def test_build_weight_records(self):
        records = [make_record(0), make_record(1)]
        weights = {0: 0.5, 1: 2.0}
        rows = build_weight_records(records, weights)
        self.assertEqual(rows[0]["sample_index"], 0)
        self.assertEqual(rows[0]["weight"], 0.5)
        self.assertEqual(rows[1]["weight"], 2.0)

    def test_weight_jsonl_roundtrip(self):
        rows = [
            {"sample_index": 0, "source_step_index": 0, "phase": "A", "weight": 1.0, "image_path": "a.png"},
            {"sample_index": 1, "source_step_index": 1, "phase": "B", "weight": 2.0, "image_path": "b.png"},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "weights.jsonl"
            write_weight_jsonl(path, rows)
            restored = read_weight_jsonl(path)
            self.assertEqual(restored, rows)

    def test_training_view_summary(self):
        source = [make_record(i) for i in range(10)]
        source.append(make_record(10, phase="CLOSE_GRIP"))
        filtered = filter_idle_records(source, keep_first_n_idle=2)
        weights = normalize_weights(compute_phase_weights(source))
        summary = training_view_summary(
            source_records=source,
            filtered_records=filtered,
            weights=weights,
            view_name="test",
        )
        self.assertEqual(summary["source_records"], 11)
        self.assertLess(summary["filtered_records"], 11)
        self.assertEqual(summary["rare_transition_records_filtered"]["CLOSE_GRIP"], 1)

    def test_build_training_views_writes_files(self):
        records = [make_record(i) for i in range(20)]
        records.append(make_record(20, phase="CLOSE_GRIP"))
        records.append(make_record(21, phase="OPEN_GRIP"))

        with tempfile.TemporaryDirectory() as tmp:
            summary = build_training_views(records, output_dir=tmp, keep_first_n_idle=3)
            root = Path(tmp)
            self.assertTrue((root / "full.jsonl").exists())
            self.assertTrue((root / "filtered_no_idle.jsonl").exists())
            self.assertTrue((root / "sample_weights.jsonl").exists())
            self.assertTrue((root / "training_view_summary.json").exists())
            self.assertEqual(summary["source_records"], 22)
            self.assertEqual(summary["rare_transition_records_filtered"]["CLOSE_GRIP"], 1)
            self.assertEqual(summary["rare_transition_records_filtered"]["OPEN_GRIP"], 1)

            full = read_dataset_jsonl(root / "full.jsonl")
            filtered = read_dataset_jsonl(root / "filtered_no_idle.jsonl")
            self.assertEqual(len(full), 22)
            self.assertLess(len(filtered), 22)


if __name__ == "__main__":
    unittest.main()
