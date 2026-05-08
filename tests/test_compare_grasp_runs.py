"""Tests for scripts/compare_grasp_runs.py."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Import helpers directly so we don't need subprocess.
from scripts.compare_grasp_runs import _extract_row, _get_nested, _load_summary


def _make_summary(**overrides) -> dict:
    base = {
        "script_name": "nominal_v1",
        "task_success": False,
        "ever_attached": False,
        "object_lifted": False,
        "object_on_target_table": False,
        "failure_reason": "never_attached",
        "stopped_early": False,
        "stop_reason": "",
        "num_steps": 100,
        "grasp_summary": {
            "backend": "kinematic",
            "n_contact_ticks": 0,
            "n_stable_contact_ticks": 0,
            "lift_height_m": 0.0,
            "ever_lifted": False,
        },
        "object_motion_summary": {
            "max_xy_displacement_from_initial": 0.01,
            "lift_height_from_initial": 0.0,
            "possible_knockover_or_push": False,
        },
        "uses_continuous_grip": False,
        "max_commanded_grip_fraction": None,
        "caging_plan": False,
    }
    base.update(overrides)
    return base


class TestGetNested(unittest.TestCase):
    def test_top_level(self):
        self.assertEqual(_get_nested({"a": 1}, "a"), 1)

    def test_nested(self):
        self.assertEqual(_get_nested({"a": {"b": 42}}, "a.b"), 42)

    def test_missing_key_returns_none(self):
        self.assertIsNone(_get_nested({"a": 1}, "b"))

    def test_missing_nested_key_returns_none(self):
        self.assertIsNone(_get_nested({"a": {}}, "a.b"))

    def test_not_a_dict_mid_path(self):
        self.assertIsNone(_get_nested({"a": "string"}, "a.b"))


class TestExtractRow(unittest.TestCase):
    def test_extracts_expected_fields(self):
        s = _make_summary(task_success=True, ever_attached=True)
        row = _extract_row(Path("fake/summary.json"), s)
        self.assertEqual(row["task_success"], True)
        self.assertEqual(row["ever_attached"], True)
        self.assertEqual(row["script_name"], "nominal_v1")
        self.assertEqual(row["grasp_backend"], "kinematic")

    def test_missing_fields_return_none(self):
        row = _extract_row(Path("x.json"), {})
        self.assertIsNone(row["task_success"])
        self.assertIsNone(row["ever_attached"])
        self.assertIsNone(row["grasp_backend"])

    def test_path_stored_as_string(self):
        row = _extract_row(Path("some/path/summary.json"), {})
        self.assertIn("path", row)
        self.assertIn("summary.json", row["path"])

    def test_caging_plan_field(self):
        s = _make_summary(caging_plan=True, max_commanded_grip_fraction=0.82)
        row = _extract_row(Path("c.json"), s)
        self.assertTrue(row["caging_plan"])
        self.assertAlmostEqual(row["max_commanded_grip_fraction"], 0.82)

    def test_object_motion_fields(self):
        s = _make_summary(object_motion_summary={
            "max_xy_displacement_from_initial": 0.20,
            "lift_height_from_initial": 0.05,
            "possible_knockover_or_push": True,
        })
        row = _extract_row(Path("d.json"), s)
        self.assertAlmostEqual(row["max_xy_displacement_m"], 0.20)
        self.assertAlmostEqual(row["lift_height_from_initial_m"], 0.05)
        self.assertTrue(row["possible_knockover_or_push"])


class TestLoadSummary(unittest.TestCase):
    def test_loads_valid_json(self):
        s = _make_summary(task_success=True)
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "summary.json"
            p.write_text(json.dumps(s), encoding="utf-8")
            loaded = _load_summary(p)
        self.assertEqual(loaded["task_success"], True)

    def test_missing_file_returns_empty_dict(self):
        result = _load_summary(Path("/nonexistent/summary.json"))
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)


class TestOutputJson(unittest.TestCase):
    def test_write_output_json(self):
        summaries = [
            _make_summary(script_name="run_a", task_success=False),
            _make_summary(script_name="run_b", task_success=True),
        ]
        rows = [
            _extract_row(Path(f"run_{i}/summary.json"), s)
            for i, s in enumerate(summaries)
        ]
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "compare.json"
            out.write_text(json.dumps(rows, indent=2, default=str), encoding="utf-8")
            loaded = json.loads(out.read_text())
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]["script_name"], "run_a")
        self.assertEqual(loaded[1]["task_success"], True)


if __name__ == "__main__":
    unittest.main()
