---
id: predicate-fires-after-gripper-retreat
scope: global
kind: strategy
title: After releasing an object into a container, retreat the gripper straight up
  before judging the predicate
applies_when: you released a held object into/onto a target and libero_terminated
  is still false
symptom:
- predicate false after release
- release did not terminate
- placed but not registered
- In predicate not firing
evidence:
  cells:
  - 10_swap_t5_s0
  attempts: 1
confidence: single-shot
related: []
---


Releasing an object into a container often does NOT flip libero_terminated on the
release step itself; the predicate fired only after the gripper retreated clear
of the settled object.

**Why:** observed, cause likely that the object is still resting between/against
the fingers (or the fingers occupy the container opening) at release, so the
settle/contact check does not pass until the gripper is withdrawn and the object
sits freely. Cause not confirmed.

**How to apply:** After `release`, if libero_terminated is false, do a small
`move_to` STRAIGHT UP (gripper=-1, step_clip~0.02) and re-check before concluding
failure. Do not immediately re-grasp or reposition — the placement may already be
correct and just needs the gripper out of the way.

**Falsify:** a case where the predicate fires on the release step and then goes
false after retreat (object dragged out), or one where retreat never changes the
flag despite a visually correct placement.

**Related:** [[task-family_libero10_swap_t5]]
