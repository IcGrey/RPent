---
id: basket-insertion-open-retreat
scope: global
kind: strategy
title: Retreat open after seating objects inside baskets.
applies_when: placing a held object into a rimmed or fabric-lined basket and release
  does not immediately terminate
symptom:
- basket
- perched
- rim
- liner
- release false
- object inside
evidence:
  cells:
  - object_task_t4_s0
  attempts: 1
confidence: single-shot
related: []
---


A basket placement can become valid only after a short open-gripper retreat lets a seated object settle inside the volume.

**Why:** observed, cause unknown; in this run the milk carton looked inside the basket after release but `terminated` stayed false until an open-gripper upward retreat began.
**How to apply:** localize the basket cavity visually, release only after the object is past the rim, and if it is perched reclose and make a short diagonal/downward seating correction first. Then release and retreat upward with `gripper:-1` using a small `step_clip` such as `0.008-0.012`.
**Falsify:** a future run where the object is visibly inside, the gripper retreats open without contact, and termination remains false despite correct target identity would weaken this lesson.
**Related:**
