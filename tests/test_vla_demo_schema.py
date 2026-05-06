"""Unit tests for vla_bridge.demo_schema and vla_bridge.demo_recorder.

These tests are pure Python + NumPy; no MuJoCo, OpenVLA, or network access
is required.
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np

from vla_bridge.demo_schema import (
    VLADemoStep,
    as_float_tuple,
    make_action_7d,
    read_jsonl,
    step_from_json,
    step_to_json,
    write_jsonl,
)
from vla_bridge.demo_recorder import VLADemoRecorder


def make_step(i: int = 0) -> VLADemoStep:
    """Create a deterministic VLADemoStep for testing."""
    return VLADemoStep(
        step_index=i,
        sim_time=float(i) * 0.1,
        image_path=f"frames/frame_{i:06d}.png",
        instruction="Pick up the red cylinder and place it on the blue table.",
        phase="SETTLE",
        palm_world=(0.1, 0.2, 0.3),
        pelvis_pos=(0.0, 0.0, 0.76),
        pelvis_quat=(1.0, 0.0, 0.0, 0.0),
        reach_target_pelvis=(0.3, -0.2, 0.2),
        grip_closed=False,
        action_7d=(0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    )


class TestAsFloatTuple(unittest.TestCase):
    def test_correct_shape_returns_python_floats(self):
        out = as_float_tuple([1, 2, 3], 3, "x")
        self.assertEqual(out, (1.0, 2.0, 3.0))
        self.assertTrue(all(isinstance(v, float) for v in out))

    def test_rejects_wrong_shape(self):
        with self.assertRaises(ValueError):
            as_float_tuple([1, 2], 3, "x")

    def test_accepts_numpy_array(self):
        out = as_float_tuple(np.array([0.5, 1.5, 2.5]), 3, "y")
        self.assertEqual(len(out), 3)


class TestMakeAction7d(unittest.TestCase):
    def test_xyz_delta_and_gripper_closed(self):
        action = make_action_7d(
            np.array([0.1, 0.2, 0.3]),
            np.array([0.2, 0.1, 0.35]),
            grip_closed=True,
        )
        np.testing.assert_allclose(action[:3], [0.1, -0.1, 0.05], atol=1e-10)
        self.assertEqual(action[3:6], (0.0, 0.0, 0.0))
        self.assertEqual(action[6], 1.0)

    def test_gripper_open(self):
        action = make_action_7d(
            np.zeros(3), np.zeros(3), grip_closed=False
        )
        self.assertEqual(action[6], 0.0)

    def test_rejects_wrong_shape(self):
        with self.assertRaises(ValueError):
            make_action_7d(np.zeros(2), np.zeros(3), False)


class TestJsonRoundtrip(unittest.TestCase):
    def test_single_step_roundtrip(self):
        step = make_step(3)
        line = step_to_json(step)
        restored = step_from_json(line)
        self.assertEqual(restored, step)


class TestJsonlRoundtrip(unittest.TestCase):
    def test_multiple_steps_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.jsonl"
            steps = [make_step(0), make_step(1)]
            write_jsonl(path, steps)
            restored = read_jsonl(path)
            self.assertEqual(restored, steps)

    def test_creates_parent_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "dir" / "demo.jsonl"
            write_jsonl(path, [make_step(0)])
            self.assertTrue(path.exists())


class TestRecorderSingleObservation(unittest.TestCase):
    def test_finalizes_zero_action(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = VLADemoRecorder(tmp, instruction="test", record_every=1)
            rec.observe(
                control_tick=0,
                sim_time=0.0,
                rgb=None,
                phase="SETTLE",
                palm_world=np.array([0.0, 0.0, 0.0]),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
                reach_target_pelvis=(0.3, -0.2, 0.2),
                grip_closed=False,
            )
            rec.finalize()
            self.assertEqual(len(rec.steps), 1)
            self.assertEqual(
                rec.steps[0].action_7d, (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
            )


class TestRecorderTwoObservations(unittest.TestCase):
    def test_computes_palm_delta_action(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = VLADemoRecorder(tmp, instruction="test", record_every=1)
            base_kwargs = dict(
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
                reach_target_pelvis=(0.3, -0.2, 0.2),
            )
            rec.observe(
                control_tick=0,
                sim_time=0.0,
                rgb=None,
                phase="SETTLE",
                palm_world=np.array([0.0, 0.0, 0.0]),
                grip_closed=False,
                **base_kwargs,
            )
            rec.observe(
                control_tick=1,
                sim_time=0.02,
                rgb=None,
                phase="SETTLE",
                palm_world=np.array([0.01, -0.02, 0.03]),
                grip_closed=True,
                **base_kwargs,
            )
            rec.finalize()

            self.assertEqual(len(rec.steps), 2)
            # First step's action = delta to second palm position; grip from step 0
            np.testing.assert_allclose(
                rec.steps[0].action_7d[:3], [0.01, -0.02, 0.03], atol=1e-10
            )
            self.assertEqual(rec.steps[0].action_7d[6], 0.0)  # grip was open at step 0
            # Second (last) step gets zero action; grip from step 1
            self.assertEqual(rec.steps[1].action_7d[6], 1.0)


class TestRecorderRecordEvery(unittest.TestCase):
    def test_respects_record_every(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = VLADemoRecorder(tmp, instruction="test", record_every=2)
            kwargs = dict(
                sim_time=0.0,
                rgb=None,
                phase="SETTLE",
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
                reach_target_pelvis=(0.3, -0.2, 0.2),
                grip_closed=False,
            )
            # Ticks 0, 1, 2 — only 0 and 2 should be recorded (even ticks)
            rec.observe(control_tick=0, palm_world=np.array([0.0, 0.0, 0.0]), **kwargs)
            rec.observe(control_tick=1, palm_world=np.array([1.0, 0.0, 0.0]), **kwargs)
            rec.observe(control_tick=2, palm_world=np.array([0.2, 0.0, 0.0]), **kwargs)
            rec.finalize()

            self.assertEqual(len(rec.steps), 2)
            # Step at tick=0: action delta is palm(tick=2) - palm(tick=0)
            np.testing.assert_allclose(
                rec.steps[0].action_7d[:3], [0.2, 0.0, 0.0], atol=1e-10
            )


class TestRecorderFramePath(unittest.TestCase):
    def test_saves_frame_path_when_rgb_provided(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = VLADemoRecorder(tmp, instruction="test", record_every=1)
            rgb = np.zeros((8, 8, 3), dtype=np.uint8)
            rec.observe(
                control_tick=0,
                sim_time=0.0,
                rgb=rgb,
                phase="SETTLE",
                palm_world=np.zeros(3),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
                reach_target_pelvis=(0.3, -0.2, 0.2),
                grip_closed=False,
            )
            rec.finalize()
            self.assertTrue(rec.steps[0].image_path.startswith("frames/frame_"))


if __name__ == "__main__":
    unittest.main()
