"""Grasp backend interface and implementations.

Backends:
  KinematicAttachment       — teleports cylinder to palm while grip is closed.
  ContactAwarePhysicalGrasp — observe-only; detects MuJoCo contacts, never
                               teleports or disables collisions.

Factory:
  make_grasp_backend(name, model, data, palm_site_id, obj_body_id, **kw)
"""

from __future__ import annotations

import warnings
from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np


@dataclass
class GraspContactStats:
    """Cumulative contact/lift metrics for a ContactAwarePhysicalGrasp rollout."""

    n_contact_ticks: int = 0          # physics ticks with ≥1 finger–object contact
    n_stable_contact_ticks: int = 0   # ticks where contact streak ≥ stable_ticks
    max_consecutive_contact: int = 0  # longest unbroken contact streak (ticks)
    first_contact_tick: int = -1      # global tick of first contact (-1 = never)
    grip_attempted_ticks: int = 0     # ticks when grip_closed=True was passed
    lift_height_m: float = 0.0        # max height object rose above initial world-Z
    ever_lifted: bool = False         # True once lift_height_m ≥ lift_threshold_m


class GraspBackend(ABC):
    """Abstract grasp backend — called every physics tick from the main loop."""

    @property
    @abstractmethod
    def attached(self) -> bool:
        """True while the object is kinematically attached."""

    @abstractmethod
    def tick(self, grip_closed: bool) -> bool:
        """Update attachment state. Returns True if currently attached.

        Must be called after every mujoco.mj_step() so the cylinder pose is
        corrected before the next integration step.
        """

    @abstractmethod
    def release(self) -> None:
        """Force-detach the object and restore its physics."""

    def summary(self) -> dict:
        """Return a JSON-serialisable summary dict (override for richer output)."""
        return {"backend": type(self).__name__}


class KinematicAttachment(GraspBackend):
    """Teleport-weld the cylinder to the palm while the grip is closed.

    Simulation shortcut: bypasses contact forces. The cylinder is placed at a
    fixed palm-local offset (snapped to SNAP_DIST if the hand closed far away)
    and its freejoint velocity is zeroed every tick so it does not drift between
    teleportations.

    Collisions are disabled while attached to prevent geom-overlap impulses from
    destabilising the robot.
    """

    ATTACH_DIST:   float = 0.13  # m: auto-attach when palm is within this distance
    SNAP_DIST:     float = 0.03  # m: clamp palm-local offset so object sits in hand
    # Short release delay avoids immediate re-collision impulses at detach time.
    RELEASE_TICKS: int   = 15    # physics ticks (~0.075s) to wait before restoring geoms

    def __init__(
        self,
        model,
        data,
        palm_site_id: int,
        obj_body_id: int,
    ) -> None:
        self._model    = model
        self._data     = data
        self._palm_id  = palm_site_id
        self._obj_id   = obj_body_id

        # Freejoint addressing (first joint of the body; must be a freejoint).
        jnt_id = int(model.body_jntadr[obj_body_id])
        self._qposadr = int(model.jnt_qposadr[jnt_id])
        self._qveladr = int(model.jnt_dofadr[jnt_id])

        # Geoms belonging to this body — used to toggle collisions.
        self._geom_ids = [
            i for i in range(model.ngeom)
            if int(model.geom_bodyid[i]) == obj_body_id
        ]
        self._orig_contype     = {g: int(model.geom_contype[g])     for g in self._geom_ids}
        self._orig_conaffinity = {g: int(model.geom_conaffinity[g]) for g in self._geom_ids}

        self._is_attached    = False
        self._release_timer  = 0
        self._local_offset   = np.zeros(3, dtype=np.float64)

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    @property
    def attached(self) -> bool:
        return self._is_attached

    def tick(self, grip_closed: bool) -> bool:
        if not self._is_attached:
            if self._release_timer > 0:
                self._release_timer -= 1
                if self._release_timer == 0:
                    self._restore_geoms()
            if grip_closed:
                palm = self._data.site_xpos[self._palm_id].copy()
                obj  = self._data.xpos[self._obj_id].copy()
                if float(np.linalg.norm(palm - obj)) <= self.ATTACH_DIST:
                    self._attach(palm, obj)
        else:
            if not grip_closed:
                self._release()
            else:
                self._update_pose()
        return self._is_attached

    def release(self) -> None:
        if self._is_attached:
            self._release()

    # ------------------------------------------------------------------ #
    # Private helpers
    # ------------------------------------------------------------------ #

    def _attach(self, palm_pos: np.ndarray, obj_pos: np.ndarray) -> None:
        palm_rot = self._data.site_xmat[self._palm_id].reshape(3, 3).copy()
        local = palm_rot.T @ (obj_pos - palm_pos)
        d = float(np.linalg.norm(local))
        if d > self.SNAP_DIST:
            local = local * (self.SNAP_DIST / d)
        self._local_offset = local

        for g in self._geom_ids:
            self._model.geom_contype[g]     = 0
            self._model.geom_conaffinity[g] = 0

        self._is_attached = True
        self._release_timer = 0
        snap = float(np.linalg.norm(self._local_offset))
        print(f"[GRASP] attached  dist={float(np.linalg.norm(palm_pos - obj_pos)):.3f} m"
              f"  snap_offset={snap:.3f} m")
        self._update_pose()

    def _update_pose(self) -> None:
        palm_pos = self._data.site_xpos[self._palm_id].copy()
        palm_rot = self._data.site_xmat[self._palm_id].reshape(3, 3).copy()
        new_pos  = palm_pos + palm_rot @ self._local_offset
        self._data.qpos[self._qposadr    :self._qposadr + 3] = new_pos
        self._data.qpos[self._qposadr + 3:self._qposadr + 7] = [1.0, 0.0, 0.0, 0.0]
        self._data.qvel[self._qveladr    :self._qveladr + 6] = 0.0

    def _release(self) -> None:
        self._data.qvel[self._qveladr:self._qveladr + 6] = 0.0
        self._is_attached = False
        self._release_timer = self.RELEASE_TICKS
        print(f"[GRASP] released — waiting {self.RELEASE_TICKS} ticks to restore geoms")

    def _restore_geoms(self) -> None:
        for g in self._geom_ids:
            self._model.geom_contype[g]     = self._orig_contype[g]
            self._model.geom_conaffinity[g] = self._orig_conaffinity[g]
        print("[GRASP] geoms restored")

    def summary(self) -> dict:
        return {"backend": "kinematic", "attached": self._is_attached}


# --------------------------------------------------------------------------- #
# ContactAwarePhysicalGrasp
# --------------------------------------------------------------------------- #

class ContactAwarePhysicalGrasp(GraspBackend):
    """Observe-only grasp backend: detects contacts, tracks lift, never teleports.

    The object's pose is never modified and its collision geoms are never
    disabled.  `attached` returns True when the grip is closed *and* stable
    finger–object contact has persisted for at least `stable_ticks` consecutive
    physics ticks.
    """

    # Sub-strings that identify right-hand/wrist bodies by name.
    # "right_wrist" is included because the wrist collision capsule (radius 3.5 cm)
    # is often the first part of the hand to press against the cylinder and its contact
    # should count toward grasp stability.
    _FINGER_NAME_PATTERNS = (
        "right_hand", "right_finger", "right_palm",
        "right_thumb", "right_index", "right_middle",
        "right_ring", "right_pinky", "right_zero",
        "right_one",  "right_two",   "right_three",
        "right_four", "right_five",  "right_wrist",
    )

    def __init__(
        self,
        model,
        data,
        palm_site_id: int,
        obj_body_id: int,
        *,
        finger_body_names: list[str] | None = None,
        stable_ticks: int = 3,
        lift_threshold_m: float = 0.02,
    ) -> None:
        self._model = model
        self._data  = data
        self._palm_id  = palm_site_id
        self._obj_id   = obj_body_id
        self._stable_ticks = stable_ticks
        self._lift_threshold = lift_threshold_m

        # Object geom IDs (for contact matching).
        self._obj_geom_ids: frozenset[int] = frozenset(
            i for i in range(model.ngeom)
            if int(model.geom_bodyid[i]) == obj_body_id
        )

        # Finger geom IDs — explicit or auto-detected.
        if finger_body_names is not None:
            import mujoco as _mj
            finger_body_ids: set[int] = {
                int(_mj.mj_name2id(model, _mj.mjtObj.mjOBJ_BODY, n))
                for n in finger_body_names
            }
            finger_body_ids.discard(-1)
        else:
            import mujoco as _mj
            finger_body_ids = set()
            for bid in range(model.nbody):
                bname = _mj.mj_id2name(model, _mj.mjtObj.mjOBJ_BODY, bid) or ""
                if any(pat in bname.lower() for pat in self._FINGER_NAME_PATTERNS):
                    finger_body_ids.add(bid)

        self._finger_geom_ids: frozenset[int] = frozenset(
            i for i in range(model.ngeom)
            if int(model.geom_bodyid[i]) in finger_body_ids
        )

        if not self._finger_geom_ids:
            warnings.warn(
                "ContactAwarePhysicalGrasp: no finger geoms found. "
                "Pass finger_body_names explicitly.",
                stacklevel=2,
            )

        # Internal state.
        self._grip_closed    = False
        self._contact_streak = 0
        self._is_stable      = False
        self._global_tick    = 0
        self._obj_init_z: float = float(data.xpos[obj_body_id][2])
        self._stats = GraspContactStats()

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    @property
    def attached(self) -> bool:
        """True when grip is closed and stable contact has been maintained."""
        return self._grip_closed and self._is_stable

    @property
    def stats(self) -> GraspContactStats:
        return self._stats

    @property
    def contact_streak(self) -> int:
        """Current consecutive finger–object contact streak (physics ticks)."""
        return self._contact_streak

    def tick(self, grip_closed: bool) -> bool:
        self._grip_closed = grip_closed
        if grip_closed:
            self._stats.grip_attempted_ticks += 1

        # Contact detection.
        in_contact = self._has_finger_object_contact()
        if in_contact:
            self._contact_streak += 1
            self._stats.n_contact_ticks += 1
            if self._stats.first_contact_tick < 0:
                self._stats.first_contact_tick = self._global_tick
            if self._contact_streak > self._stats.max_consecutive_contact:
                self._stats.max_consecutive_contact = self._contact_streak
        else:
            self._contact_streak = 0

        # Stability — requires grip closed + enough consecutive contacts.
        self._is_stable = (
            grip_closed and self._contact_streak >= self._stable_ticks
        )
        if self._is_stable:
            self._stats.n_stable_contact_ticks += 1

        # Lift tracking — compare current object Z to initial Z.
        obj_z = float(self._data.xpos[self._obj_id][2])
        height_above = obj_z - self._obj_init_z
        if height_above > self._stats.lift_height_m:
            self._stats.lift_height_m = height_above
        if not self._stats.ever_lifted and height_above >= self._lift_threshold:
            self._stats.ever_lifted = True

        self._global_tick += 1
        return self.attached

    def release(self) -> None:
        """Reset grip/contact state (object physics are unaffected)."""
        self._grip_closed    = False
        self._contact_streak = 0
        self._is_stable      = False

    def summary(self) -> dict:
        s = self._stats
        return {
            "backend": "contact_aware_physical",
            "n_contact_ticks": s.n_contact_ticks,
            "n_stable_contact_ticks": s.n_stable_contact_ticks,
            "max_consecutive_contact": s.max_consecutive_contact,
            "first_contact_tick": s.first_contact_tick,
            "grip_attempted_ticks": s.grip_attempted_ticks,
            "lift_height_m": round(s.lift_height_m, 6),
            "ever_lifted": s.ever_lifted,
            "stable_ticks_threshold": self._stable_ticks,
            "lift_threshold_m": self._lift_threshold,
            "n_finger_geoms": len(self._finger_geom_ids),
            "n_obj_geoms": len(self._obj_geom_ids),
        }

    # ------------------------------------------------------------------ #
    # Private helpers
    # ------------------------------------------------------------------ #

    def _has_finger_object_contact(self) -> bool:
        for i in range(self._data.ncon):
            c = self._data.contact[i]
            g1, g2 = int(c.geom1), int(c.geom2)
            if (g1 in self._finger_geom_ids and g2 in self._obj_geom_ids) or \
               (g2 in self._finger_geom_ids and g1 in self._obj_geom_ids):
                return True
        return False

    def contact_count(self) -> int:
        """Number of distinct finger–object contact pairs right now."""
        count = 0
        for i in range(self._data.ncon):
            c = self._data.contact[i]
            g1, g2 = int(c.geom1), int(c.geom2)
            if (g1 in self._finger_geom_ids and g2 in self._obj_geom_ids) or \
               (g2 in self._finger_geom_ids and g1 in self._obj_geom_ids):
                count += 1
        return count


# --------------------------------------------------------------------------- #
# HybridGraspBackend
# --------------------------------------------------------------------------- #

class HybridGraspBackend(GraspBackend):
    """Physical contact detection + kinematic transport.

    Phase 1 (pre-confirm): ContactAwarePhysicalGrasp detects finger-object
      contacts and accumulates stats.  `attached` reflects physical stability.

    Phase 2 (transport): After `confirm_contact()` is called, KinematicAttachment
      teleports the cylinder to the palm every tick so it survives long walking
      manoeuvres.  ContactAwarePhysical continues ticking (stats only).

    Exposes `contact_streak` and `contact_count()` from the physical sub-backend
    so cage-probe code can read them without knowing about the wrapper.
    """

    def __init__(
        self,
        model,
        data,
        palm_site_id: int,
        obj_body_id: int,
        **kwargs,
    ) -> None:
        self._contact   = ContactAwarePhysicalGrasp(
            model, data, palm_site_id, obj_body_id, **kwargs
        )
        self._kinematic = KinematicAttachment(model, data, palm_site_id, obj_body_id)
        self._confirmed = False

    def confirm_contact(self) -> None:
        """Switch to kinematic transport once physical contact is confirmed."""
        if not self._confirmed:
            self._confirmed = True
            print("[HYBRID-GRASP] physical contact confirmed — switching to kinematic transport")

    @property
    def confirmed(self) -> bool:
        return self._confirmed

    @property
    def attached(self) -> bool:
        if self._confirmed:
            return self._kinematic.attached
        return self._contact.attached

    @property
    def contact_streak(self) -> int:
        return self._contact._contact_streak

    def contact_count(self) -> int:
        return self._contact.contact_count()

    @property
    def stats(self):
        return self._contact.stats

    def tick(self, grip_closed: bool) -> bool:
        self._contact.tick(grip_closed)
        if self._confirmed:
            return self._kinematic.tick(grip_closed)
        return self._contact.attached

    def release(self) -> None:
        self._kinematic.release()
        self._contact.release()

    def summary(self) -> dict:
        d = self._contact.summary()
        d["backend"]           = "hybrid"
        d["confirmed"]         = self._confirmed
        d["kinematic_attached"] = self._kinematic.attached
        return d


# --------------------------------------------------------------------------- #
# Factory
# --------------------------------------------------------------------------- #

def make_grasp_backend(
    backend: str,
    model,
    data,
    palm_site_id: int,
    obj_body_id: int,
    **kwargs,
) -> GraspBackend:
    """Instantiate a grasp backend by name.

    backend: "kinematic"              → KinematicAttachment
             "contact-aware-physical" → ContactAwarePhysicalGrasp
             "hybrid"                 → HybridGraspBackend

    This keeps runtime policy selection independent from grasp mechanics so
    the same high-level controller can be evaluated under different assumptions.
    """
    if backend == "kinematic":
        return KinematicAttachment(model, data, palm_site_id, obj_body_id)
    if backend == "contact-aware-physical":
        return ContactAwarePhysicalGrasp(model, data, palm_site_id, obj_body_id, **kwargs)
    if backend == "hybrid":
        return HybridGraspBackend(model, data, palm_site_id, obj_body_id, **kwargs)
    raise ValueError(
        f"Unknown grasp backend: {backend!r}. "
        "Valid choices: 'kinematic', 'contact-aware-physical', 'hybrid'."
    )
