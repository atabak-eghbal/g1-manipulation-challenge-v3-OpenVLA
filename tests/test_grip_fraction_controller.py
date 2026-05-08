"""Tests for the controller's continuous grip fraction logic.

Tests the pure _next_grip_fraction helper and the set/clear helpers
without requiring MuJoCo or a full controller.
"""
from __future__ import annotations

import unittest


class TestNextGripFraction(unittest.TestCase):
    """Tests for WalkerReacherController._next_grip_fraction (static, pure)."""

    @staticmethod
    def _f(current, target, speed):
        from common.controller import WalkerReacherController
        return WalkerReacherController._next_grip_fraction(current, target, speed)

    def test_instant_open_to_closed(self):
        """Speed=1.0 snaps 0→1 in one step."""
        result = self._f(0.0, 1.0, 1.0)
        self.assertAlmostEqual(result, 1.0)

    def test_instant_closed_to_open(self):
        """Speed=1.0 snaps 1→0 in one step."""
        result = self._f(1.0, 0.0, 1.0)
        self.assertAlmostEqual(result, 0.0)

    def test_slow_ramp_upward(self):
        """Speed=0.1 advances by exactly 0.1 per step."""
        result = self._f(0.0, 1.0, 0.1)
        self.assertAlmostEqual(result, 0.1)

    def test_slow_ramp_downward(self):
        """Speed=0.1 decreases by exactly 0.1 per step."""
        result = self._f(0.5, 0.0, 0.1)
        self.assertAlmostEqual(result, 0.4)

    def test_clamp_at_one(self):
        """Result is clamped to 1.0."""
        result = self._f(0.95, 1.0, 0.5)
        self.assertAlmostEqual(result, 1.0)

    def test_clamp_at_zero(self):
        """Result is clamped to 0.0."""
        result = self._f(0.05, 0.0, 0.5)
        self.assertAlmostEqual(result, 0.0)

    def test_already_at_target(self):
        """No movement when already at target."""
        result = self._f(0.6, 0.6, 0.1)
        self.assertAlmostEqual(result, 0.6)

    def test_partial_target(self):
        """Ramps toward a partial target, not past it."""
        result = self._f(0.0, 0.3, 1.0)
        self.assertAlmostEqual(result, 0.3)

    def test_partial_target_slow(self):
        """Slow ramp stops at the partial target rather than overshooting."""
        result = self._f(0.28, 0.3, 0.05)
        self.assertAlmostEqual(result, 0.3)


if __name__ == "__main__":
    unittest.main()
