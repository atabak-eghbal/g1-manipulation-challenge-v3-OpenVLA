"""Tests for deterministic scenario configuration parsing and selection.

These checks protect perturbation schema validation and modulo-based scenario
selection used by batch data collection.
"""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vla_bridge.scenario_config import load_scenario_config, select_scenario


def _write_config(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


class TestScenarioConfig(unittest.TestCase):
    def test_loads_valid_config_and_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "defaults": {
                        "red_block_xy_offset_m": [0.01, -0.01],
                        "robot_base_xy_offset_m": [0.0, 0.0],
                        "target_drop_xy_offset_m": [0.0, 0.0],
                    },
                    "scenarios": [
                        {"scenario_id": "a", "seed": 1},
                        {"scenario_id": "b", "seed": 2, "red_block_xy_offset_m": [0.02, 0.0]},
                    ],
                },
            )
            cfg = load_scenario_config(path)
            self.assertEqual(cfg.name, "test_cfg")
            self.assertEqual(len(cfg.scenarios), 2)
            self.assertEqual(cfg.scenarios[0].red_block_xy_offset_m, (0.01, -0.01))
            self.assertEqual(cfg.scenarios[1].red_block_xy_offset_m, (0.02, 0.0))

    def test_rejects_duplicate_scenario_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "scenarios": [
                        {"scenario_id": "dup", "seed": 1},
                        {"scenario_id": "dup", "seed": 2},
                    ],
                },
            )
            with self.assertRaises(ValueError):
                load_scenario_config(path)

    def test_rejects_duplicate_seeds(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "scenarios": [
                        {"scenario_id": "a", "seed": 3},
                        {"scenario_id": "b", "seed": 3},
                    ],
                },
            )
            with self.assertRaises(ValueError):
                load_scenario_config(path)

    def test_rejects_bad_xy_offsets(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "defaults": {"red_block_xy_offset_m": [0.0]},
                    "scenarios": [{"scenario_id": "a", "seed": 1}],
                },
            )
            with self.assertRaises(ValueError):
                load_scenario_config(path)

    def test_select_scenario_wraps(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scenarios.json"
            _write_config(
                path,
                {
                    "name": "test_cfg",
                    "description": "desc",
                    "scenarios": [
                        {"scenario_id": "a", "seed": 10},
                        {"scenario_id": "b", "seed": 11},
                        {"scenario_id": "c", "seed": 12},
                    ],
                },
            )
            cfg = load_scenario_config(path)
            self.assertEqual(select_scenario(cfg, 0).scenario_id, "a")
            self.assertEqual(select_scenario(cfg, 4).scenario_id, "b")


if __name__ == "__main__":
    unittest.main()
