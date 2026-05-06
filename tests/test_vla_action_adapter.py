"""Unit tests for vla_bridge.action_adapter (Step 13).

These tests are pure NumPy and do not require MuJoCo, OpenVLA, Hugging Face,
PyTorch, or any cloud infrastructure.
"""

from __future__ import annotations

import unittest

import numpy as np

from vla_bridge.action_adapter import (
    G1VLAActionAdapter,
    clip_reach_target,
    quat_apply_inverse,
    validate_vector,
    world_to_pelvis,
)


class TestG1VLAActionAdapter(unittest.TestCase):
    def assertArrayClose(self, actual, expected, places=7):
        np.testing.assert_allclose(np.asarray(actual), np.asarray(expected), atol=10 ** (-places))

    # 1. Import smoke test
    def test_imports(self):
        self.assertIsNotNone(G1VLAActionAdapter)
        self.assertIsNotNone(validate_vector)
        self.assertIsNotNone(quat_apply_inverse)
        self.assertIsNotNone(world_to_pelvis)
        self.assertIsNotNone(clip_reach_target)

    # 2. Identity transform test
    def test_world_to_pelvis_identity(self):
        out = world_to_pelvis(
            pelvis_pos=np.array([0.0, 0.0, 0.0]),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            world_point=np.array([0.3, -0.2, 0.2]),
        )
        self.assertArrayClose(out, [0.3, -0.2, 0.2])

    # 3. Adapter zero-action test
    def test_zero_action_outputs_current_target(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.array([0.3, -0.2, 0.2]))
        out = adapter.step(
            np.zeros(7),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertEqual(out.walk_cmd, (0.0, 0.0, 0.0))
        self.assertEqual(out.reach_active, True)
        self.assertEqual(out.grip_closed, False)
        self.assertArrayClose(out.reach_target, [0.3, -0.2, 0.2])

    # 4. Delta accumulation test
    def test_delta_accumulates_and_clips_per_step(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.zeros(3))
        out = adapter.step(
            np.array([0.10, -0.10, 0.02, 0.0, 0.0, 0.0, 1.0]),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertArrayClose(out.reach_target, [0.05, -0.05, 0.02])
        self.assertEqual(out.grip_closed, True)

    # 5. Gripper threshold test
    def test_gripper_threshold(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.zeros(3), gripper_threshold=0.0)
        out_open = adapter.step(
            np.array([0, 0, 0, 0, 0, 0, 0.0], dtype=float),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertFalse(out_open.grip_closed)

        adapter.reset(np.zeros(3))
        out_closed = adapter.step(
            np.array([0, 0, 0, 0, 0, 0, 0.01], dtype=float),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertTrue(out_closed.grip_closed)

    # 6. Workspace clipping test
    def test_workspace_clipping(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.zeros(3), max_delta_m=10.0)
        out = adapter.step(
            np.array([10, -10, 10, 0, 0, 0, 0], dtype=float),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertArrayClose(out.reach_target, [0.60, -0.60, 0.60])

    # 7. Lazy initialization test
    def test_lazy_initialization_from_current_palm_world(self):
        adapter = G1VLAActionAdapter()
        out = adapter.step(
            np.zeros(7),
            pelvis_pos=np.zeros(3),
            pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            current_palm_world=np.array([0.1, 0.2, 0.3]),
        )
        self.assertArrayClose(out.reach_target, [0.1, 0.2, 0.3])

    # 8. Missing initialization error test
    def test_missing_initialization_raises(self):
        adapter = G1VLAActionAdapter()
        with self.assertRaises(ValueError):
            adapter.step(
                np.zeros(7),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            )

    # 9. Shape validation test
    def test_shape_validation(self):
        adapter = G1VLAActionAdapter(initial_palm_world=np.zeros(3))
        with self.assertRaises(ValueError):
            adapter.step(
                np.zeros(6),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            )
        with self.assertRaises(ValueError):
            adapter.step(
                np.zeros(7),
                pelvis_pos=np.zeros(2),
                pelvis_quat=np.array([1.0, 0.0, 0.0, 0.0]),
            )
        with self.assertRaises(ValueError):
            adapter.step(
                np.zeros(7),
                pelvis_pos=np.zeros(3),
                pelvis_quat=np.array([1.0, 0.0, 0.0]),
            )


if __name__ == "__main__":
    unittest.main()
