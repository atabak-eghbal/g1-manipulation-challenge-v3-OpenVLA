from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import json


@dataclass(frozen=True)
class ScenarioSpec:
    scenario_id: str
    seed: int
    red_block_xy_offset_m: tuple[float, float] = (0.0, 0.0)
    robot_base_xy_offset_m: tuple[float, float] = (0.0, 0.0)
    target_drop_xy_offset_m: tuple[float, float] = (0.0, 0.0)


@dataclass(frozen=True)
class ScenarioConfig:
    name: str
    description: str
    scenarios: list[ScenarioSpec]


def _as_xy(value: Any, *, field_name: str) -> tuple[float, float]:
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError(f"{field_name} must be a list/tuple of length 2")
    try:
        return (float(value[0]), float(value[1]))
    except Exception as exc:
        raise ValueError(f"{field_name} must contain numeric values") from exc


def load_scenario_config(path: str | Path) -> ScenarioConfig:
    src = Path(path)
    data = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("scenario config root must be an object")

    name = str(data.get("name", "")).strip()
    description = str(data.get("description", "")).strip()
    if not name:
        raise ValueError("scenario config requires non-empty 'name'")
    if not description:
        raise ValueError("scenario config requires non-empty 'description'")

    defaults_raw = data.get("defaults", {})
    if not isinstance(defaults_raw, dict):
        raise ValueError("'defaults' must be an object")
    defaults = {
        "red_block_xy_offset_m": _as_xy(defaults_raw.get("red_block_xy_offset_m", (0.0, 0.0)), field_name="defaults.red_block_xy_offset_m"),
        "robot_base_xy_offset_m": _as_xy(defaults_raw.get("robot_base_xy_offset_m", (0.0, 0.0)), field_name="defaults.robot_base_xy_offset_m"),
        "target_drop_xy_offset_m": _as_xy(defaults_raw.get("target_drop_xy_offset_m", (0.0, 0.0)), field_name="defaults.target_drop_xy_offset_m"),
    }

    scenarios_raw = data.get("scenarios", [])
    if not isinstance(scenarios_raw, list) or not scenarios_raw:
        raise ValueError("'scenarios' must be a non-empty list")

    seen_ids: set[str] = set()
    seen_seeds: set[int] = set()
    scenarios: list[ScenarioSpec] = []
    for i, row in enumerate(scenarios_raw):
        if not isinstance(row, dict):
            raise ValueError(f"scenarios[{i}] must be an object")
        if "scenario_id" not in row:
            raise ValueError(f"scenarios[{i}] missing required field 'scenario_id'")
        if "seed" not in row:
            raise ValueError(f"scenarios[{i}] missing required field 'seed'")

        scenario_id = str(row["scenario_id"]).strip()
        if not scenario_id:
            raise ValueError(f"scenarios[{i}].scenario_id must be non-empty")
        seed = int(row["seed"])
        if scenario_id in seen_ids:
            raise ValueError(f"duplicate scenario_id: {scenario_id}")
        if seed in seen_seeds:
            raise ValueError(f"duplicate seed: {seed}")
        seen_ids.add(scenario_id)
        seen_seeds.add(seed)

        red = _as_xy(row.get("red_block_xy_offset_m", defaults["red_block_xy_offset_m"]), field_name=f"scenarios[{i}].red_block_xy_offset_m")
        robot = _as_xy(row.get("robot_base_xy_offset_m", defaults["robot_base_xy_offset_m"]), field_name=f"scenarios[{i}].robot_base_xy_offset_m")
        target = _as_xy(row.get("target_drop_xy_offset_m", defaults["target_drop_xy_offset_m"]), field_name=f"scenarios[{i}].target_drop_xy_offset_m")

        scenarios.append(
            ScenarioSpec(
                scenario_id=scenario_id,
                seed=seed,
                red_block_xy_offset_m=red,
                robot_base_xy_offset_m=robot,
                target_drop_xy_offset_m=target,
            )
        )

    return ScenarioConfig(
        name=name,
        description=description,
        scenarios=scenarios,
    )


def select_scenario(config: ScenarioConfig, index: int) -> ScenarioSpec:
    if not config.scenarios:
        raise ValueError("config.scenarios must not be empty")
    return config.scenarios[int(index) % len(config.scenarios)]


def scenario_to_metadata(spec: ScenarioSpec) -> dict[str, Any]:
    return asdict(spec)


def load_and_select_scenario(path: str | Path, index: int) -> ScenarioSpec:
    return select_scenario(load_scenario_config(path), index)
