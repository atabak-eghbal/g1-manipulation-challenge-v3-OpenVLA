"""Tests for scripted-rollout task success evaluation.

These checks protect attachment/lift/placement outcome classification so
summary.json success reporting remains consistent.
"""
from __future__ import annotations

import json
import unittest

from vla_bridge.task_success import TaskSuccessTracker

SOURCE_TABLE_Z = 0.73
TARGET_TABLE_Z = 0.63
TARGET_CENTER = (-0.3, -0.6, 0.63)
SUCCESS_BLOCK = (-0.3, -0.6, 0.65)
LIFTED_MAX_Z = 0.85


def _success_tracker() -> TaskSuccessTracker:
    t = TaskSuccessTracker(source_table_z=SOURCE_TABLE_Z, target_table_z=TARGET_TABLE_Z)
    t.update_attachment(attached_now=True, tick=50, phase="close_grip")
    t.update_object_position((0.0, 0.0, LIFTED_MAX_Z))
    return t


class TestTaskSuccessTracker(unittest.TestCase):

    # 1. New tracker starts clean
    def test_initial_state(self):
        t = TaskSuccessTracker()
        self.assertFalse(t.ever_attached)
        self.assertFalse(t.task_success)
        self.assertIsNone(t.attach_tick)
        self.assertEqual(t.attach_phase, "")

    # 2. update_attachment records first attach
    def test_update_attachment_records_first(self):
        t = TaskSuccessTracker()
        t.update_attachment(attached_now=True, tick=42, phase="close_grip")
        self.assertTrue(t.ever_attached)
        self.assertEqual(t.attach_tick, 42)
        self.assertEqual(t.attach_phase, "close_grip")

    # 3. update_attachment does not overwrite first attach
    def test_update_attachment_no_overwrite(self):
        t = TaskSuccessTracker()
        t.update_attachment(attached_now=True, tick=10, phase="close_grip")
        t.update_attachment(attached_now=True, tick=99, phase="lift_source")
        self.assertEqual(t.attach_tick, 10)
        self.assertEqual(t.attach_phase, "close_grip")

    # 4. update_object_position tracks max z
    def test_update_object_position_max_z(self):
        t = TaskSuccessTracker()
        t.update_object_position((0.0, 0.0, 0.5))
        t.update_object_position((0.0, 0.0, 0.9))
        t.update_object_position((0.0, 0.0, 0.7))
        self.assertAlmostEqual(t.max_red_block_z, 0.9)
        # final_red_block_world is last update
        self.assertAlmostEqual(t.final_red_block_world[2], 0.7)

    # 5. finalize returns never_attached if no attachment
    def test_finalize_never_attached(self):
        t = TaskSuccessTracker(source_table_z=SOURCE_TABLE_Z, target_table_z=TARGET_TABLE_Z)
        result = t.finalize(
            final_red_block_world=SUCCESS_BLOCK,
            target_center_world=TARGET_CENTER,
            target_table_z=TARGET_TABLE_Z,
        )
        self.assertFalse(result["ever_attached"])
        self.assertFalse(result["task_success"])
        self.assertEqual(result["failure_reason"], "never_attached")

    # 6. finalize returns object_not_lifted if attached but z never rises enough
    def test_finalize_not_lifted(self):
        t = TaskSuccessTracker(source_table_z=SOURCE_TABLE_Z, target_table_z=TARGET_TABLE_Z)
        t.update_attachment(attached_now=True, tick=50, phase="close_grip")
        # max z only slightly above source table (not >= source_z + 0.05)
        t.update_object_position((0.0, 0.0, SOURCE_TABLE_Z + 0.01))
        result = t.finalize(
            final_red_block_world=SUCCESS_BLOCK,
            target_center_world=TARGET_CENTER,
            target_table_z=TARGET_TABLE_Z,
        )
        self.assertTrue(result["ever_attached"])
        self.assertFalse(result["object_lifted"])
        self.assertFalse(result["task_success"])
        self.assertEqual(result["failure_reason"], "object_not_lifted")

    # 7. finalize returns object_not_on_target_table if attached/lifted but xy too far
    def test_finalize_not_on_target_table(self):
        t = _success_tracker()
        far_block = (5.0, 5.0, TARGET_TABLE_Z + 0.03)  # lifted but far away
        result = t.finalize(
            final_red_block_world=far_block,
            target_center_world=TARGET_CENTER,
            target_table_z=TARGET_TABLE_Z,
        )
        self.assertTrue(result["object_lifted"])
        self.assertFalse(result["object_on_target_table"])
        self.assertFalse(result["task_success"])
        self.assertEqual(result["failure_reason"], "object_not_on_target_table")

    # 8. finalize returns task_success true when attached, lifted, on target
    def test_finalize_task_success(self):
        t = _success_tracker()
        result = t.finalize(
            final_red_block_world=SUCCESS_BLOCK,
            target_center_world=TARGET_CENTER,
            target_table_z=TARGET_TABLE_Z,
        )
        self.assertTrue(result["ever_attached"])
        self.assertTrue(result["object_lifted"])
        self.assertTrue(result["object_on_target_table"])
        self.assertTrue(result["task_success"])
        self.assertEqual(result["failure_reason"], "")

    # 9. final_height_above_target is computed correctly
    def test_final_height_above_target(self):
        t = _success_tracker()
        result = t.finalize(
            final_red_block_world=SUCCESS_BLOCK,
            target_center_world=TARGET_CENTER,
            target_table_z=TARGET_TABLE_Z,
        )
        expected = SUCCESS_BLOCK[2] - TARGET_TABLE_Z  # 0.65 - 0.63 = 0.02
        self.assertAlmostEqual(result["final_height_above_target"], expected, places=6)

    # 10. final_xy_distance_to_target is computed correctly
    def test_final_xy_distance_to_target(self):
        import math
        t = _success_tracker()
        block = (-0.1, -0.4, TARGET_TABLE_Z + 0.03)
        result = t.finalize(
            final_red_block_world=block,
            target_center_world=TARGET_CENTER,
            target_table_z=TARGET_TABLE_Z,
        )
        expected = math.sqrt((-0.1 - (-0.3)) ** 2 + (-0.4 - (-0.6)) ** 2)
        self.assertAlmostEqual(result["final_xy_distance_to_target"], expected, places=6)

    # 11. output is JSON serializable
    def test_json_serializable(self):
        t = _success_tracker()
        result = t.finalize(
            final_red_block_world=SUCCESS_BLOCK,
            target_center_world=TARGET_CENTER,
            target_table_z=TARGET_TABLE_Z,
        )
        serialized = json.dumps(result)
        self.assertIsInstance(serialized, str)
        parsed = json.loads(serialized)
        self.assertEqual(parsed["failure_reason"], "")


if __name__ == "__main__":
    unittest.main()
