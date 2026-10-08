---
id: high-drop-over-cavity
scope: global
kind: strategy
title: Release box-like objects high over a container cavity instead of descending
  into the rim.
applies_when: Placing a rectangular or box-like object into a soft/rimmed open container
  where low descent catches the front rim.
symptom:
- rim-perched
- basket
- box
- release-false
- cannot-descend
evidence:
  cells:
  - object_task_t0_s0
  attempts: 2
confidence: single-shot
related: []
---


A box that perches on a basket rim after low release can succeed by being carried fully over the visible cavity and released from a higher pose so gravity drops it inside.

**Why:** The basket rim and liner contact stalled scripted downward motion near z~0.15 and trapped the box across the front lip. Releasing from z~0.20 while horizontally over the liner avoided the rim contact state and terminated immediately.
**How to apply:** Identify the container semantically in agentview, use wrist to align over the interior liner/cavity, keep gripper closed during carry, and release from a high over-cavity pose around 4-6 cm above the rim rather than forcing a low descent. For low object-frame basket tasks, z~0.19-0.21 worked here.
**Falsify:** If a high over-cavity release repeatedly bounces the object out while a lower straight-down placement terminates, this lesson should be narrowed to this basket/box geometry.
**Related:** [[task-family_libero_object_task_t0]]
