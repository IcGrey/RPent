---
id: predicate-gated-by-eef-proximity-retreat-clear
scope: global
kind: failure
title: Retreat the eef fully clear of a placement before concluding the predicate
  failed
applies_when: after a geometrically-correct place, libero_terminated stays false for
  many steps while the gripper hovers over the just-placed object
symptom:
- placed object looks correct
- mug on plate centered
- libero_terminated false
- gripper hovering over placement
- no fire after dwell
evidence:
  cells:
  - 10_task_t6_s0
  attempts: 3
confidence: single-shot
related:
- place-order-never-carry-over-placed-object
---


A correct final configuration can fail to fire the goal predicate while the open
gripper is still hovering directly over the just-placed object; moving the eef
laterally away let it fire on the very next step.

**Why:** observed, cause unknown. Plausibly the hovering gripper maintains a
contact/near-contact with the placed object (or the plate stack) that the On/
relation check treats as unsettled, or the object micro-shifts under the gripper.
Whatever the cause, retreating the eef clear removed the block deterministically
in this cell (steps 48-49 no fire with eef at (0.09,0.012,0.64) over the mug;
step 50 fired the instant the eef moved to (0.18,0.14,0.55)).
**How to apply:** After the final release, do NOT judge failure while the eef is
above the placement. Retreat straight up, then LATERALLY away from all placed
objects (several cm), and re-check libero_terminated. Only after the eef is
clearly clear should you treat a still-false predicate as a real failure and
start re-diagnosing target/side/physics.
**Falsify:** A cell that fires immediately on release with the gripper still
directly overhead, or one that stays false even after the eef fully retreats.
**Related:** [[libero10-left-right-sign-verify-empirically]]
