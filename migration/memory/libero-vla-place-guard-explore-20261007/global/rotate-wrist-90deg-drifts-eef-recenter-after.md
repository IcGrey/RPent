---
id: rotate-wrist-90deg-drifts-eef-recenter-after
scope: global
kind: primitive
title: A large rotate_wrist yaw drifts the eef ~0.1-0.15m; re-center before descending
applies_when: you rotate_wrist by a large yaw (e.g. 90deg) to align fingers, then
  need a precise xy over a target
symptom:
- rotate_wrist moved eef
- yaw rotation drift
- gripper off target after yaw
- position changed after rotate_wrist
evidence:
  cells:
  - 10_task_t8_s0
  attempts: 1
  solved_seeds:
  - 0
confidence: single-shot
related:
- moka-pot-grasp-the-handle-not-the-body
---

Although rotate_wrist is documented to hold xyz fixed, a large yaw change (~90deg) can move the eef by ~0.1-0.15m in xy; always re-issue a move_to to the target after the rotation and before descending.

**Why:** observed, cause likely OSC/IK: holding eef position while commanding a big wrist reorientation drives the arm through a configuration where the position controller cannot fully compensate, so the eef settles offset. (Mechanism not verified beyond the observation.)

**How to apply:**
- Order operations as: rotate_wrist to the needed yaw FIRST (accept the drift), THEN move_to the
  precise xy target, THEN descend. Do not descend immediately after a large rotate_wrist.
- Budget one extra move_to. Small yaw tweaks (<~20deg) drift much less and may not need it.

**Falsify:** If large rotate_wrist yaw changes on other cells leave the eef within ~1cm of its
pre-rotation xy, the drift is scene-specific and this can be narrowed.

**Related:** [[moka-pot-grasp-the-handle-not-the-body]]
