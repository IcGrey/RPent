---
id: pi0-pick-may-place-at-trained-left
scope: global
kind: primitive
title: pi0_pick often carries the grasped object toward its trained place pose; exploit
  or cap it
applies_when: using pi0_pick for a grasp and it lifts then drifts in +y (robot-left)
  instead of stopping at lift
symptom:
- pi0 lifted but eef moved sideways
- gripper still holding
- success flag false
- can carried
- drifted to left
evidence:
  cells:
  - 10_task_t0_s0
  attempts: 1
confidence: single-shot
related: []
---


pi0_pick runs Pi0's trained pick-AND-place policy; after grasping it may keep
driving toward its trained drop location (typically robot-left, +y) rather than
halting at lift.

**Why:** Pi0 was trained on full pick-and-place; the "pick" wrapper only stops it
by a lift/chunk heuristic. With enough chunks it continues its learned trajectory,
which tends toward a +y place pose. `success=false` here just meant the
lift+close heuristic didn't latch (a can's diameter keeps opening >0.06), NOT
that the grasp failed.

**How to apply:** Judge the grasp from perception (wrist cam + gripper opening
consistent with the object's width), not from the success flag. If the trained
drift happens to carry the object over your true target (e.g. a basket at
robot-left), let it finish and just settle/release there. If it drifts AWAY from
the target, cap max_chunks (<=16, even <=8 for fragile items) so Pi0 stops near
lift, then script the carry yourself. Never assume the drop location is safe —
check where it went.

**Falsify:** If pi0_pick consistently halts at lift with no lateral drift across
scenes, this no longer applies.

**Related:** [[sam3-brand-noun-can-collision]]
