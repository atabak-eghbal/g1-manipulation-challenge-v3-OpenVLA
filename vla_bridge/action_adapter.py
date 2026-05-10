"""Adapter from OpenVLA-style 7D actions to G1 PolicyOutput commands.

Step 13 scope:
- no OpenVLA import
- no model inference
- no demo recording
- no runtime integration

The adapter treats a VLA action as a small end-effector delta in world frame:
[dx, dy, dz, droll, dpitch, dyaw, gripper]

Only dx/dy/dz and gripper are used in this first milestone.
Rotation is intentionally ignored until we prove the action representation is executable.

Review note:
Raw 7D replay alone was not sufficient for the full humanoid task, so this
adapter is now mainly a research baseline/reference path beside teacher-command
replay and G1-native command export.
"""

from __future__ import annotations

import numpy as np

from policies.base import PolicyOutput


_REACH_LOW = np.array([-0.30, -0.60, -0.40], dtype=np.float64)
_REACH_HIGH = np.array([0.60, 0.30, 0.60], dtype=np.float64)


def validate_vector(name: str, value: np.ndarray, shape: tuple[int, ...]) -> np.ndarray:
    """Validate that *value* can be cast to a float64 array of *shape*."""
    arr = np.asarray(value, dtype=np.float64)
    if arr.shape != shape:
        raise ValueError(f"{name} must have shape {shape}, got {arr.shape}")
    return arr.copy()


def quat_apply_inverse(quat_wxyz: np.ndarray, vec: np.ndarray) -> np.ndarray:
    """Rotate *vec* by the inverse (conjugate) of *quat_wxyz*.

    Uses the sandwich formula: q^{-1} v q, computed via cross-product form.
    *quat_wxyz* is in MuJoCo scalar-first order: [w, x, y, z].
    """
    q = validate_vector("quat_wxyz", quat_wxyz, (4,))
    v = validate_vector("vec", vec, (3,))
    norm = float(np.linalg.norm(q))
    if norm <= 1e-12:
        raise ValueError("quat_wxyz must be non-zero")
    q = q / norm
    w = q[0]
    xyz = q[1:4]
    t = 2.0 * np.cross(xyz, v)
    return v - w * t + np.cross(xyz, t)


def world_to_pelvis(
    pelvis_pos: np.ndarray,
    pelvis_quat: np.ndarray,
    world_point: np.ndarray,
) -> np.ndarray:
    """Transform *world_point* from world frame into the pelvis body frame.

    Args:
        pelvis_pos: (3,) world-frame position of the pelvis origin.
        pelvis_quat: (4,) orientation of the pelvis in MuJoCo [w, x, y, z] order.
        world_point: (3,) point to transform.

    Returns:
        (3,) coordinates expressed in the pelvis frame.
    """
    p = validate_vector("pelvis_pos", pelvis_pos, (3,))
    q = validate_vector("pelvis_quat", pelvis_quat, (4,))
    wpt = validate_vector("world_point", world_point, (3,))
    return quat_apply_inverse(q, wpt - p)


def clip_reach_target(reach_target: np.ndarray) -> np.ndarray:
    """Clip *reach_target* to the reacher workspace bounds.

    Hard clipping is intentional so adapter outputs stay executable even when
    world-frame deltas drift outside the arm's trained workspace.
    """
    target = validate_vector("reach_target", reach_target, (3,))
    return np.clip(target, _REACH_LOW, _REACH_HIGH)


class G1VLAActionAdapter:
    """Convert OpenVLA-style 7D actions into G1 PolicyOutput commands.

    This adapter is intentionally small and model-free. It does not know about
    OpenVLA internals. It only tests whether a 7D end-effector action interface
    can drive the existing G1 reacher/grip control path.

    The 7D action vector is:
        [dx, dy, dz, droll, dpitch, dyaw, gripper]

    droll / dpitch / dyaw are intentionally ignored in Step 13.
    Only dx/dy/dz (world-frame palm delta) and gripper are consumed.
    """

    def __init__(
        self,
        initial_palm_world: np.ndarray | None = None,
        max_delta_m: float = 0.05,
        gripper_threshold: float = 0.0,
    ) -> None:
        """Initialize the adapter.

        Args:
            initial_palm_world: Optional (3,) starting desired palm position in
                world coordinates.  Can also be set later via ``reset()``.
            max_delta_m: Per-step per-axis clipping limit (metres).
            gripper_threshold: gripper action values strictly above this are
                treated as *closed*.
        """
        if max_delta_m <= 0:
            raise ValueError("max_delta_m must be positive")
        self.max_delta_m = float(max_delta_m)
        self.gripper_threshold = float(gripper_threshold)
        self._desired_palm_world: np.ndarray | None = None
        self._last_action_7d: np.ndarray | None = None
        self._last_reach_target: np.ndarray | None = None

        if initial_palm_world is not None:
            self.reset(initial_palm_world)

    # ------------------------------------------------------------------
    # Read-only properties
    # ------------------------------------------------------------------

    @property
    def desired_palm_world(self) -> np.ndarray | None:
        """Current desired palm position in world frame (copy)."""
        return None if self._desired_palm_world is None else self._desired_palm_world.copy()

    @property
    def last_action_7d(self) -> np.ndarray | None:
        """The most recent 7D action passed to ``step()`` (copy)."""
        return None if self._last_action_7d is None else self._last_action_7d.copy()

    @property
    def last_reach_target(self) -> np.ndarray | None:
        """The most recent pelvis-frame reach target returned by ``step()`` (copy)."""
        return None if self._last_reach_target is None else self._last_reach_target.copy()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def reset(self, palm_world: np.ndarray) -> None:
        """Reset the desired palm position to *palm_world* (world frame).

        Also clears cached action and reach-target state.
        """
        self._desired_palm_world = validate_vector("palm_world", palm_world, (3,))
        self._last_action_7d = None
        self._last_reach_target = None

    def step(
        self,
        action_7d: np.ndarray,
        pelvis_pos: np.ndarray,
        pelvis_quat: np.ndarray,
        *,
        current_palm_world: np.ndarray | None = None,
        walk_cmd: tuple[float, float, float] = (0.0, 0.0, 0.0),
    ) -> PolicyOutput:
        """Apply *action_7d* and return the corresponding ``PolicyOutput``.

        Args:
            action_7d: Shape (7,) array ``[dx, dy, dz, droll, dpitch, dyaw, gripper]``
                in world frame.  Rotation channels are ignored in Step 13.
            pelvis_pos: Shape (3,) world-frame pelvis position from MuJoCo.
            pelvis_quat: Shape (4,) pelvis orientation ``[w, x, y, z]`` (MuJoCo order).
            current_palm_world: Optional (3,) current palm position used for lazy
                initialisation when ``reset()`` has not yet been called.
            walk_cmd: Base locomotion command forwarded verbatim into PolicyOutput.

        Returns:
            A ``PolicyOutput`` with ``reach_active=True`` and the clipped
            pelvis-frame reach target.

        Raises:
            ValueError: If ``desired_palm_world`` has not been initialised and
                ``current_palm_world`` is not provided.
        """
        action = validate_vector("action_7d", action_7d, (7,))
        ppos = validate_vector("pelvis_pos", pelvis_pos, (3,))
        pquat = validate_vector("pelvis_quat", pelvis_quat, (4,))

        if self._desired_palm_world is None:
            if current_palm_world is None:
                raise ValueError(
                    "Adapter has no desired_palm_world. Call reset(...) first "
                    "or pass current_palm_world to step(...)."
                )
            self.reset(current_palm_world)

        delta_world = np.clip(action[:3], -self.max_delta_m, self.max_delta_m)
        self._desired_palm_world = self._desired_palm_world + delta_world

        reach = world_to_pelvis(ppos, pquat, self._desired_palm_world)
        reach = clip_reach_target(reach)

        self._last_action_7d = action.copy()
        self._last_reach_target = reach.copy()

        grip_closed = bool(action[6] > self.gripper_threshold)

        return PolicyOutput(
            walk_cmd=tuple(float(x) for x in walk_cmd),
            reach_target=tuple(float(x) for x in reach),
            reach_active=True,
            grip_closed=grip_closed,
        )
