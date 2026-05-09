"""Tests for ContactAwarePhysicalGrasp and make_grasp_backend factory.

Nine test cases A–I:
  A — instantiation with auto-detected finger bodies
  B — instantiation with explicit finger_body_names
  C — no contact when block is far from finger
  D — contact detected when geoms overlap
  E — stable contact requires stable_ticks consecutive ticks
  F — object qpos is never modified by tick()
  G — lift detection when object rises above threshold
  H — summary() returns all expected keys with correct types
  I — release() clears grip/stable state
"""

from __future__ import annotations

import unittest

import mujoco
import numpy as np

from common.grasp import (
    ContactAwarePhysicalGrasp,
    GraspBackend,
    GraspContactStats,
    KinematicAttachment,
    make_grasp_backend,
)

# ---------------------------------------------------------------------------
# Minimal test scene XML strings
# ---------------------------------------------------------------------------

# Scene with a FREE red_block overlapping the right_finger (static).
# Finger top (z=+0.02) vs block bottom (z=0.025-0.02=0.005): 15 mm overlap.
# The block has a freejoint so MuJoCo detects contacts (static-static pairs are skipped).
# No gravity → block stays put if we call tick() without mj_step, keeping contacts stable.
_XML_CONTACT = """\
<mujoco>
  <option gravity="0 0 0" timestep="0.005"/>
  <worldbody>
    <body name="right_finger" pos="0 0 0">
      <geom name="finger_geom" type="box" size="0.02 0.02 0.02"
            contype="1" conaffinity="1"/>
      <site name="palm_site" pos="0 0 0"/>
    </body>
    <body name="red_block" pos="0 0 0.025">
      <joint name="block_free" type="free"/>
      <geom name="block_geom" type="box" size="0.02 0.02 0.02"
            contype="1" conaffinity="1"/>
    </body>
  </worldbody>
</mujoco>"""

# Scene with a FREE red_block starting far above the right_finger.
# No contact in the initial state.
_XML_FREE = """\
<mujoco>
  <option gravity="0 0 0" timestep="0.005"/>
  <worldbody>
    <body name="right_finger" pos="0 0 0">
      <geom name="finger_geom" type="box" size="0.02 0.02 0.02"
            contype="1" conaffinity="1"/>
      <site name="palm_site" pos="0 0 0"/>
    </body>
    <body name="red_block" pos="0 0 0.50">
      <joint name="block_free" type="free"/>
      <geom name="block_geom" type="box" size="0.02 0.02 0.02"
            contype="1" conaffinity="1"/>
    </body>
  </worldbody>
</mujoco>"""


# ---------------------------------------------------------------------------
# Scene helpers
# ---------------------------------------------------------------------------

def _make_contact_scene():
    model = mujoco.MjModel.from_xml_string(_XML_CONTACT)
    data = mujoco.MjData(model)
    mujoco.mj_forward(model, data)
    palm_site_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SITE, "palm_site")
    obj_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    return model, data, palm_site_id, obj_body_id


def _make_free_scene():
    model = mujoco.MjModel.from_xml_string(_XML_FREE)
    data = mujoco.MjData(model)
    mujoco.mj_forward(model, data)
    palm_site_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SITE, "palm_site")
    obj_body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "red_block")
    return model, data, palm_site_id, obj_body_id


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

class TestContactAwarePhysicalGrasp(unittest.TestCase):

    # A ------------------------------------------------------------------ #
    def test_A_instantiation_auto_detect(self):
        """ContactAwarePhysicalGrasp can be instantiated with auto-detection."""
        model, data, palm_site_id, obj_body_id = _make_contact_scene()
        backend = ContactAwarePhysicalGrasp(model, data, palm_site_id, obj_body_id)
        self.assertIsInstance(backend, GraspBackend)
        self.assertIsInstance(backend.stats, GraspContactStats)
        self.assertFalse(backend.attached)
        # Auto-detection should find "right_finger" body.
        self.assertGreater(backend.summary()["n_finger_geoms"], 0)

    # B ------------------------------------------------------------------ #
    def test_B_instantiation_explicit_finger_bodies(self):
        """Explicit finger_body_names are accepted and produce non-empty geom set."""
        model, data, palm_site_id, obj_body_id = _make_contact_scene()
        backend = ContactAwarePhysicalGrasp(
            model, data, palm_site_id, obj_body_id,
            finger_body_names=["right_finger"],
        )
        self.assertEqual(backend.summary()["n_finger_geoms"], 1)
        self.assertEqual(backend.summary()["n_obj_geoms"], 1)

    # C ------------------------------------------------------------------ #
    def test_C_no_contact_when_block_is_far(self):
        """tick() returns False and records no contact when block is away."""
        model, data, palm_site_id, obj_body_id = _make_free_scene()
        backend = ContactAwarePhysicalGrasp(
            model, data, palm_site_id, obj_body_id,
            finger_body_names=["right_finger"],
        )
        result = backend.tick(grip_closed=True)
        self.assertFalse(result)
        self.assertFalse(backend.attached)
        self.assertEqual(backend.stats.n_contact_ticks, 0)
        self.assertEqual(backend.stats.first_contact_tick, -1)

    # D ------------------------------------------------------------------ #
    def test_D_contact_detected_on_geom_overlap(self):
        """tick() registers contact when finger geom overlaps block geom."""
        model, data, palm_site_id, obj_body_id = _make_contact_scene()
        backend = ContactAwarePhysicalGrasp(
            model, data, palm_site_id, obj_body_id,
            finger_body_names=["right_finger"],
            stable_ticks=100,  # very high so we're not yet stable
        )
        # Geoms overlap after mj_forward — contacts should be present.
        self.assertGreater(data.ncon, 0, "Expected geom overlap to produce contacts")
        backend.tick(grip_closed=True)
        self.assertGreater(backend.stats.n_contact_ticks, 0)
        self.assertEqual(backend.stats.first_contact_tick, 0)

    # E ------------------------------------------------------------------ #
    def test_E_stable_requires_consecutive_ticks(self):
        """attached is False before stable_ticks, True at and after stable_ticks."""
        model, data, palm_site_id, obj_body_id = _make_contact_scene()
        backend = ContactAwarePhysicalGrasp(
            model, data, palm_site_id, obj_body_id,
            finger_body_names=["right_finger"],
            stable_ticks=3,
        )
        self.assertGreater(data.ncon, 0, "Need contacts for this test")

        # Ticks 0, 1 — not yet stable.
        self.assertFalse(backend.tick(grip_closed=True))
        self.assertFalse(backend.tick(grip_closed=True))
        # Tick 2 — stable_ticks=3 reached (streak=3).
        self.assertTrue(backend.tick(grip_closed=True))
        self.assertTrue(backend.attached)
        self.assertGreater(backend.stats.n_stable_contact_ticks, 0)

    # F ------------------------------------------------------------------ #
    def test_F_object_qpos_not_altered(self):
        """tick() must not modify the block's free-joint qpos."""
        model, data, palm_site_id, obj_body_id = _make_free_scene()
        backend = ContactAwarePhysicalGrasp(
            model, data, palm_site_id, obj_body_id,
            finger_body_names=["right_finger"],
        )
        # Locate free-joint qpos address.
        jnt_id = int(model.body_jntadr[obj_body_id])
        qposadr = int(model.jnt_qposadr[jnt_id])
        qpos_before = data.qpos[qposadr:qposadr + 7].copy()

        backend.tick(grip_closed=True)

        np.testing.assert_array_equal(
            data.qpos[qposadr:qposadr + 7], qpos_before,
            err_msg="ContactAwarePhysicalGrasp must not alter block qpos",
        )

    # G ------------------------------------------------------------------ #
    def test_G_lift_detected_when_object_rises(self):
        """ever_lifted becomes True when object rises above lift_threshold_m."""
        model, data, palm_site_id, obj_body_id = _make_free_scene()
        backend = ContactAwarePhysicalGrasp(
            model, data, palm_site_id, obj_body_id,
            finger_body_names=["right_finger"],
            lift_threshold_m=0.02,
        )
        init_z = float(data.xpos[obj_body_id][2])  # ≈ 0.50

        # Lift block by 0.03 m (> threshold of 0.02).
        jnt_id = int(model.body_jntadr[obj_body_id])
        qposadr = int(model.jnt_qposadr[jnt_id])
        data.qpos[qposadr + 2] = init_z + 0.03
        mujoco.mj_forward(model, data)

        backend.tick(grip_closed=False)  # grip irrelevant for lift detection

        self.assertTrue(backend.stats.ever_lifted)
        self.assertAlmostEqual(backend.stats.lift_height_m, 0.03, places=4)

    # H ------------------------------------------------------------------ #
    def test_H_summary_has_expected_keys(self):
        """summary() returns a dict with all required keys and correct types."""
        model, data, palm_site_id, obj_body_id = _make_contact_scene()
        backend = ContactAwarePhysicalGrasp(
            model, data, palm_site_id, obj_body_id,
            finger_body_names=["right_finger"],
            stable_ticks=2,
        )
        for _ in range(3):
            backend.tick(grip_closed=True)

        s = backend.summary()
        required_keys = {
            "backend", "n_contact_ticks", "n_stable_contact_ticks",
            "max_consecutive_contact", "first_contact_tick",
            "grip_attempted_ticks", "lift_height_m", "ever_lifted",
            "stable_ticks_threshold", "lift_threshold_m",
            "n_finger_geoms", "n_obj_geoms",
        }
        self.assertEqual(required_keys, set(s.keys()))
        self.assertEqual(s["backend"], "contact_aware_physical")
        self.assertIsInstance(s["n_contact_ticks"], int)
        self.assertIsInstance(s["lift_height_m"], float)
        self.assertIsInstance(s["ever_lifted"], bool)
        self.assertEqual(s["grip_attempted_ticks"], 3)

    # I ------------------------------------------------------------------ #
    def test_I_release_clears_grip_and_stable_state(self):
        """release() clears grip/stable state; attached becomes False immediately."""
        model, data, palm_site_id, obj_body_id = _make_contact_scene()
        backend = ContactAwarePhysicalGrasp(
            model, data, palm_site_id, obj_body_id,
            finger_body_names=["right_finger"],
            stable_ticks=2,
        )
        self.assertGreater(data.ncon, 0)

        # Reach stable state.
        for _ in range(3):
            backend.tick(grip_closed=True)
        self.assertTrue(backend.attached)

        # Release should drop attached immediately.
        backend.release()
        self.assertFalse(backend.attached)


# ---------------------------------------------------------------------------
# Tests for make_grasp_backend factory
# ---------------------------------------------------------------------------

class TestMakeGraspBackend(unittest.TestCase):

    def _scene(self):
        return _make_contact_scene()

    def test_factory_kinematic(self):
        model, data, palm_site_id, obj_body_id = self._scene()
        backend = make_grasp_backend("kinematic", model, data, palm_site_id, obj_body_id)
        self.assertIsInstance(backend, KinematicAttachment)

    def test_factory_contact_aware_physical(self):
        model, data, palm_site_id, obj_body_id = self._scene()
        backend = make_grasp_backend(
            "contact-aware-physical", model, data, palm_site_id, obj_body_id,
            finger_body_names=["right_finger"],
        )
        self.assertIsInstance(backend, ContactAwarePhysicalGrasp)

    def test_factory_invalid_raises(self):
        model, data, palm_site_id, obj_body_id = self._scene()
        with self.assertRaises(ValueError):
            make_grasp_backend("nonexistent", model, data, palm_site_id, obj_body_id)

    def test_kinematic_summary(self):
        model, data, palm_site_id, obj_body_id = self._scene()
        backend = make_grasp_backend("kinematic", model, data, palm_site_id, obj_body_id)
        s = backend.summary()
        self.assertIn("backend", s)
        self.assertEqual(s["backend"], "kinematic")


if __name__ == "__main__":
    unittest.main()
