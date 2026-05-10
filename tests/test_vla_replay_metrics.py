"""Tests for teacher-vs-replay metric computation.

These checks keep replay diagnostics stable so adapter/teacher replay fidelity
can be compared consistently across experiments.
"""
from __future__ import annotations

import unittest

import numpy as np

from vla_bridge.demo_schema import VLADemoStep
from vla_bridge.replay_metrics import (
    ReplayMetrics,
    action_xyz_magnitudes,
    compute_replay_metrics,
    grip_mismatch_count,
    palm_error_metrics,
    walk_command_magnitudes,
)


def make_step(
    i: int,
    palm=(0.0, 0.0, 0.0),
    grip=False,
    action=(0.0, 0.0, 0.0),
    walk_cmd=(0.0, 0.0, 0.0),
    reach_active=True,
) -> VLADemoStep:
    return VLADemoStep(
        step_index=i,
        sim_time=float(i) * 0.02,
        image_path="",
        instruction="test",
        phase="TEST",
        palm_world=tuple(float(x) for x in palm),
        pelvis_pos=(0.0, 0.0, 0.76),
        pelvis_quat=(1.0, 0.0, 0.0, 0.0),
        walk_cmd=tuple(float(x) for x in walk_cmd),
        reach_target_pelvis=(0.3, -0.2, 0.2),
        reach_active=bool(reach_active),
        grip_closed=bool(grip),
        action_7d=(
            float(action[0]),
            float(action[1]),
            float(action[2]),
            0.0,
            0.0,
            0.0,
            1.0 if grip else 0.0,
        ),
    )


class TestVLAReplayMetrics(unittest.TestCase):
    def test_action_magnitudes_empty(self):
        mags = action_xyz_magnitudes([])
        self.assertEqual(mags.shape, (0,))
        self.assertEqual(mags.dtype, np.float64)

    def test_action_magnitudes_known_values(self):
        steps = [
            make_step(0, action=(3.0, 4.0, 0.0)),
            make_step(1, action=(0.0, 0.0, 12.0)),
        ]
        mags = action_xyz_magnitudes(steps)
        np.testing.assert_allclose(mags, [5.0, 12.0])

    def test_palm_error_metrics_known_values(self):
        teacher = np.array([[0, 0, 0], [1, 0, 0]], dtype=float)
        replay = np.array([[0, 0, 0], [2, 0, 0]], dtype=float)
        mean_err, max_err, final_err = palm_error_metrics(teacher, replay)
        self.assertAlmostEqual(mean_err, 0.5)
        self.assertAlmostEqual(max_err, 1.0)
        self.assertAlmostEqual(final_err, 1.0)

    def test_palm_error_metrics_rejects_shape_mismatch(self):
        with self.assertRaises(ValueError):
            palm_error_metrics(np.zeros((2, 3)), np.zeros((3, 3)))

    def test_palm_error_metrics_empty_returns_nan(self):
        mean_err, max_err, final_err = palm_error_metrics(
            np.zeros((0, 3)), np.zeros((0, 3))
        )
        self.assertTrue(np.isnan(mean_err))
        self.assertTrue(np.isnan(max_err))
        self.assertTrue(np.isnan(final_err))

    def test_grip_mismatch_count(self):
        self.assertEqual(
            grip_mismatch_count(
                [False, True, True, False], [False, False, True, True]
            ),
            2,
        )

    def test_grip_mismatch_count_all_match(self):
        self.assertEqual(grip_mismatch_count([True, False], [True, False]), 0)

    def test_grip_mismatch_count_length_mismatch_raises(self):
        with self.assertRaises(ValueError):
            grip_mismatch_count([True, False], [True])

    def test_compute_replay_metrics(self):
        steps = [
            make_step(0, palm=(0, 0, 0), grip=False, action=(0.1, 0, 0)),
            make_step(1, palm=(1, 0, 0), grip=True, action=(0, 0.2, 0)),
        ]
        replay = np.array([[0, 0, 0], [1.5, 0, 0]], dtype=float)
        metrics = compute_replay_metrics(steps, replay, [False, False])

        self.assertIsInstance(metrics, ReplayMetrics)
        self.assertEqual(metrics.num_steps, 2)
        self.assertAlmostEqual(metrics.mean_palm_error_m, 0.25)
        self.assertAlmostEqual(metrics.max_palm_error_m, 0.5)
        self.assertAlmostEqual(metrics.final_palm_error_m, 0.5)
        # action mags: ||(0.1,0,0)|| = 0.1, ||(0,0.2,0)|| = 0.2
        self.assertAlmostEqual(metrics.mean_action_magnitude_m, 0.15)
        self.assertAlmostEqual(metrics.max_action_magnitude_m, 0.2)
        # teacher grip = [False, True], replay grip = [False, False] → 1 mismatch
        self.assertEqual(metrics.grip_mismatch_count, 1)

    def test_compute_replay_metrics_shape_mismatch_raises(self):
        steps = [make_step(0)]
        with self.assertRaises(ValueError):
            compute_replay_metrics(steps, np.zeros((2, 3)), [False])

    def test_compute_replay_metrics_grip_length_mismatch_raises(self):
        steps = [make_step(0)]
        with self.assertRaises(ValueError):
            compute_replay_metrics(steps, np.zeros((1, 3)), [])


class TestWalkCommandMetrics(unittest.TestCase):
    def test_walk_command_magnitudes_empty(self):
        mags = walk_command_magnitudes([])
        self.assertEqual(mags.shape, (0,))
        self.assertEqual(mags.dtype, np.float64)

    def test_walk_command_magnitudes_known_values(self):
        steps = [
            make_step(0, walk_cmd=(3.0, 4.0, 0.0)),
            make_step(1, walk_cmd=(0.0, 0.0, 12.0)),
        ]
        mags = walk_command_magnitudes(steps)
        np.testing.assert_allclose(mags, [5.0, 12.0])

    def test_compute_replay_metrics_includes_walk_fields(self):
        steps = [
            make_step(0, walk_cmd=(0.0, 0.0, 0.0), reach_active=False),
            make_step(1, walk_cmd=(3.0, 4.0, 0.0), reach_active=True),
        ]
        replay = np.array([[0, 0, 0], [0, 0, 0]], dtype=float)
        metrics = compute_replay_metrics(steps, replay, [False, False])

        self.assertEqual(metrics.walk_nonzero_steps, 1)
        self.assertEqual(metrics.reach_active_steps, 1)
        self.assertAlmostEqual(metrics.max_walk_command_magnitude, 5.0)
        self.assertAlmostEqual(metrics.mean_walk_command_magnitude, 2.5)


if __name__ == "__main__":
    unittest.main()
