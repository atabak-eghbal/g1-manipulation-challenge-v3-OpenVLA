from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vla_bridge.scripted_keyboard import (
    ScriptedKeyboardPlan,
    ScriptedKeyboardStep,
    command_for_tick,
    expand_scripted_keyboard_plan,
    load_scripted_keyboard_plan,
    plan_summary,
    validate_scripted_keyboard_plan,
)

NOMINAL_JSON_PATH = Path(__file__).resolve().parent.parent / "configs" / "scripts" / "nominal_scripted_keyboard_v1.json"
CAGING_JSON_PATH  = Path(__file__).resolve().parent.parent / "configs" / "scripts" / "table_assisted_caging_v1.json"


def _make_step(**overrides) -> ScriptedKeyboardStep:
    defaults = dict(
        name="settle",
        duration_ticks=10,
        walk_cmd=(0.0, 0.0, 0.0),
        reach_target=(0.3, -0.2, 0.2),
        reach_active=False,
        grip_closed=False,
    )
    defaults.update(overrides)
    return ScriptedKeyboardStep(**defaults)


def _make_plan(**overrides) -> ScriptedKeyboardPlan:
    defaults = dict(
        name="test_plan",
        teacher_type="scripted_keyboard",
        description="A test plan",
        control_dt=0.02,
        steps=[
            _make_step(name="settle", duration_ticks=10, walk_cmd=(0.0, 0.0, 0.0), reach_active=False, grip_closed=False),
            _make_step(name="walk", duration_ticks=5, walk_cmd=(0.1, 0.0, 0.0), reach_active=True, grip_closed=False),
            _make_step(name="grip", duration_ticks=3, walk_cmd=(0.0, 0.0, 0.0), reach_active=True, grip_closed=True),
        ],
    )
    defaults.update(overrides)
    return ScriptedKeyboardPlan(**defaults)


class TestScriptedKeyboard(unittest.TestCase):
    def setUp(self):
        self.plan = _make_plan()

    # ------------------------------------------------------------------
    # 1. Loads the nominal JSON plan
    # ------------------------------------------------------------------
    def test_load_nominal_json_plan(self):
        plan = load_scripted_keyboard_plan(NOMINAL_JSON_PATH)
        self.assertEqual(plan.name, "nominal_scripted_keyboard_v1")
        self.assertGreater(len(plan.steps), 0)
        self.assertIsInstance(plan.steps[0], ScriptedKeyboardStep)

    # ------------------------------------------------------------------
    # 2. Validates teacher_type == scripted_keyboard
    # ------------------------------------------------------------------
    def test_validate_teacher_type(self):
        validate_scripted_keyboard_plan(self.plan)  # should not raise

        bad = _make_plan(teacher_type="fsm")
        with self.assertRaisesRegex(ValueError, "scripted_keyboard"):
            validate_scripted_keyboard_plan(bad)

    # ------------------------------------------------------------------
    # 3. Rejects empty steps
    # ------------------------------------------------------------------
    def test_rejects_empty_steps(self):
        bad = _make_plan(steps=[])
        with self.assertRaisesRegex(ValueError, "at least one step"):
            validate_scripted_keyboard_plan(bad)

    # ------------------------------------------------------------------
    # 4. Rejects zero duration
    # ------------------------------------------------------------------
    def test_rejects_zero_duration(self):
        bad_step = _make_step(name="settle", duration_ticks=0)
        bad = _make_plan(steps=[bad_step])
        with self.assertRaisesRegex(ValueError, "non-positive duration_ticks"):
            validate_scripted_keyboard_plan(bad)

    # ------------------------------------------------------------------
    # 5. Rejects wrong walk_cmd shape
    # ------------------------------------------------------------------
    def test_rejects_wrong_walk_cmd_shape(self):
        bad_step = _make_step(walk_cmd=(0.0, 0.0))
        bad = _make_plan(steps=[bad_step])
        with self.assertRaisesRegex(ValueError, "walk_cmd must be length 3"):
            validate_scripted_keyboard_plan(bad)

    # ------------------------------------------------------------------
    # 6. Rejects wrong reach_target shape
    # ------------------------------------------------------------------
    def test_rejects_wrong_reach_target_shape(self):
        bad_step = _make_step(reach_target=(0.0, 0.0))
        bad = _make_plan(steps=[bad_step])
        with self.assertRaisesRegex(ValueError, "reach_target must be length 3"):
            validate_scripted_keyboard_plan(bad)

    # ------------------------------------------------------------------
    # 7. Expands to total duration equal to sum(duration_ticks)
    # ------------------------------------------------------------------
    def test_expand_total_duration(self):
        expanded = expand_scripted_keyboard_plan(self.plan)
        expected = sum(s.duration_ticks for s in self.plan.steps)
        self.assertEqual(len(expanded), expected)

    # ------------------------------------------------------------------
    # 8. First expanded command has phase "settle"
    # ------------------------------------------------------------------
    def test_first_expanded_phase_is_settle(self):
        expanded = expand_scripted_keyboard_plan(self.plan)
        self.assertEqual(expanded[0].phase, "settle")

    # ------------------------------------------------------------------
    # 9. Last expanded command has phase "retract" (nominal plan)
    # ------------------------------------------------------------------
    def test_last_expanded_phase_nominal(self):
        plan = load_scripted_keyboard_plan(NOMINAL_JSON_PATH)
        expanded = expand_scripted_keyboard_plan(plan)
        self.assertEqual(expanded[-1].phase, "retract")

    # ------------------------------------------------------------------
    # 10. command_for_tick returns final command after plan end
    # ------------------------------------------------------------------
    def test_command_for_tick_past_end(self):
        total = sum(s.duration_ticks for s in self.plan.steps)
        cmd_last = command_for_tick(self.plan, total - 1)
        cmd_past = command_for_tick(self.plan, total + 100)
        self.assertEqual(cmd_past.phase, cmd_last.phase)
        self.assertEqual(cmd_past.tick_index, cmd_last.tick_index)

    # ------------------------------------------------------------------
    # 11. plan_summary returns correct total tick count
    # ------------------------------------------------------------------
    def test_plan_summary_total_ticks(self):
        summary = plan_summary(self.plan)
        expected = sum(s.duration_ticks for s in self.plan.steps)
        self.assertEqual(summary["total_ticks"], expected)

    # ------------------------------------------------------------------
    # 12. plan_summary reports some reach_active ticks
    # ------------------------------------------------------------------
    def test_plan_summary_reach_active_ticks(self):
        summary = plan_summary(self.plan)
        self.assertGreater(summary["reach_active_ticks"], 0)

    # ------------------------------------------------------------------
    # 13. plan_summary reports some grip_closed ticks
    # ------------------------------------------------------------------
    def test_plan_summary_grip_closed_ticks(self):
        summary = plan_summary(self.plan)
        self.assertGreater(summary["grip_closed_ticks"], 0)

    # ------------------------------------------------------------------
    # 14. plan_summary reports some walk_nonzero ticks
    # ------------------------------------------------------------------
    def test_plan_summary_walk_nonzero_ticks(self):
        summary = plan_summary(self.plan)
        self.assertGreater(summary["walk_nonzero_ticks"], 0)

    # ------------------------------------------------------------------
    # Extra: load via tempfile round-trip
    # ------------------------------------------------------------------
    def test_load_from_tempfile(self):
        plan_data = {
            "name": "rt_plan",
            "teacher_type": "scripted_keyboard",
            "description": "round-trip",
            "control_dt": 0.02,
            "steps": [
                {"name": "settle", "duration_ticks": 5, "walk_cmd": [0.0, 0.0, 0.0],
                 "reach_target": [0.3, -0.2, 0.2], "reach_active": False, "grip_closed": False},
            ],
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "plan.json"
            path.write_text(json.dumps(plan_data))
            plan = load_scripted_keyboard_plan(path)
        self.assertEqual(plan.name, "rt_plan")
        self.assertEqual(len(plan.steps), 1)
        self.assertIsInstance(plan.steps[0], ScriptedKeyboardStep)


    # ------------------------------------------------------------------
    # Step 26 — continuous grip fraction tests
    # ------------------------------------------------------------------

    def test_nominal_plan_loads(self):
        """Old nominal plan still loads and parses without errors."""
        plan = load_scripted_keyboard_plan(NOMINAL_JSON_PATH)
        validate_scripted_keyboard_plan(plan)
        self.assertGreater(len(plan.steps), 0)

    def test_caging_plan_loads(self):
        """New caging plan loads and validates without errors."""
        plan = load_scripted_keyboard_plan(CAGING_JSON_PATH)
        validate_scripted_keyboard_plan(plan)
        self.assertGreater(len(plan.steps), 0)

    def test_caging_plan_uses_continuous_grip(self):
        """Caging plan summary reports uses_continuous_grip=True."""
        plan = load_scripted_keyboard_plan(CAGING_JSON_PATH)
        summary = plan_summary(plan)
        self.assertTrue(summary["uses_continuous_grip"])
        self.assertIsNotNone(summary["min_grip_fraction"])
        self.assertIsNotNone(summary["max_grip_fraction"])

    def test_caging_plan_max_grip_fraction_gt_half(self):
        """Caging plan max grip fraction is greater than 0.5."""
        plan = load_scripted_keyboard_plan(CAGING_JSON_PATH)
        summary = plan_summary(plan)
        self.assertGreater(summary["max_grip_fraction"], 0.5)

    def test_nominal_plan_no_continuous_grip(self):
        """Old nominal plan does not use continuous grip."""
        plan = load_scripted_keyboard_plan(NOMINAL_JSON_PATH)
        summary = plan_summary(plan)
        self.assertFalse(summary["uses_continuous_grip"])
        self.assertIsNone(summary["min_grip_fraction"])
        self.assertIsNone(summary["max_grip_fraction"])

    def test_invalid_grip_fraction_low_raises(self):
        """grip_fraction below 0 raises ValueError."""
        bad_step = _make_step(grip_fraction=-0.1)
        bad = _make_plan(steps=[bad_step])
        with self.assertRaisesRegex(ValueError, "grip_fraction"):
            validate_scripted_keyboard_plan(bad)

    def test_invalid_grip_fraction_high_raises(self):
        """grip_fraction above 1 raises ValueError."""
        bad_step = _make_step(grip_fraction=1.01)
        bad = _make_plan(steps=[bad_step])
        with self.assertRaisesRegex(ValueError, "grip_fraction"):
            validate_scripted_keyboard_plan(bad)

    def test_invalid_grip_close_speed_raises(self):
        """grip_close_speed <= 0 raises ValueError."""
        bad_step = _make_step(grip_close_speed=0.0)
        bad = _make_plan(steps=[bad_step])
        with self.assertRaisesRegex(ValueError, "grip_close_speed"):
            validate_scripted_keyboard_plan(bad)

    def test_expanded_commands_carry_grip_fraction(self):
        """Expanded commands carry grip_fraction and grip_close_speed from steps."""
        step = _make_step(duration_ticks=3, grip_fraction=0.4, grip_close_speed=0.01)
        plan = _make_plan(steps=[step])
        expanded = expand_scripted_keyboard_plan(plan)
        for cmd in expanded:
            self.assertAlmostEqual(cmd.grip_fraction, 0.4)
            self.assertAlmostEqual(cmd.grip_close_speed, 0.01)

    def test_expanded_commands_none_grip_fraction_when_absent(self):
        """Expanded commands have grip_fraction=None when not in step."""
        plan = load_scripted_keyboard_plan(NOMINAL_JSON_PATH)
        expanded = expand_scripted_keyboard_plan(plan)
        for cmd in expanded:
            self.assertIsNone(cmd.grip_fraction)
            self.assertIsNone(cmd.grip_close_speed)

    def test_valid_grip_fraction_boundary_values(self):
        """0.0 and 1.0 are valid grip_fraction values."""
        for frac in (0.0, 1.0):
            step = _make_step(grip_fraction=frac)
            plan = _make_plan(steps=[step])
            validate_scripted_keyboard_plan(plan)  # should not raise


if __name__ == "__main__":
    unittest.main()
