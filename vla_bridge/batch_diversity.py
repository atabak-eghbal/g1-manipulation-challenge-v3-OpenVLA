"""Diversity summary helpers for scenario-perturbed batch manifests.

This module is a lightweight analytics layer over manifest metadata; it does
not inspect MuJoCo trajectories directly.
"""
from __future__ import annotations

from typing import Any

from vla_bridge.batch_manifest import BatchManifest


def summarize_manifest_diversity(manifest: BatchManifest) -> dict[str, Any]:
    """Summarize scenario and perturbation spread for one batch manifest."""
    successful = [d for d in manifest.demos if d.status == "success"]
    scenario_ids: list[str] = []
    offsets: list[tuple[float, float]] = []
    for demo in manifest.demos:
        scenario_ids.append(demo.scenario_id or "")
        meta = demo.scenario or {}
        raw = meta.get("red_block_xy_offset_m", (0.0, 0.0))
        if isinstance(raw, (list, tuple)) and len(raw) == 2:
            dx = float(raw[0])
            dy = float(raw[1])
        else:
            dx, dy = 0.0, 0.0
        offsets.append((dx, dy))

    if offsets:
        dx_values = [o[0] for o in offsets]
        dy_values = [o[1] for o in offsets]
        dx_range = [min(dx_values), max(dx_values)]
        dy_range = [min(dy_values), max(dy_values)]
    else:
        dx_range = [0.0, 0.0]
        dy_range = [0.0, 0.0]

    all_offsets_identical = len(set(offsets)) <= 1
    unique_scenarios = sorted(set(scenario_ids))

    return {
        "batch_id": manifest.batch_id,
        "num_demos": len(manifest.demos),
        "num_successful_demos": len(successful),
        "num_unique_scenarios": len(unique_scenarios),
        "scenario_ids": unique_scenarios,
        "red_block_xy_offset_m_per_demo": [[float(x), float(y)] for x, y in offsets],
        "dx_range_m": [float(dx_range[0]), float(dx_range[1])],
        "dy_range_m": [float(dy_range[0]), float(dy_range[1])],
        "all_offsets_identical": all_offsets_identical,
    }
