---
id: flat-box-rigid-bowl-seat
scope: global
kind: strategy
title: Seat flat boxes below a rigid bowl rim before release.
applies_when: placing a flat rectangular object into or on a rigid bowl whose rim
  can catch the lower edge
symptom:
- flat box
- bowl rim
- release false
- perched
- edge bias
evidence:
  cells:
  - goal_swap_t6_s0
confidence: single-shot
related:
- flat-box-basket-interior-drop
---


A flat rectangular object should be centered and lowered until visibly inside the rigid bowl rim before opening the gripper.

**Why:** observed, cause unknown. In this solved run, the predicate fired only after the held cream-cheese box was visually below/inside the patterned bowl rim at release.
**How to apply:** Localize the bowl interior from agentview identity plus wrist geometry. Carry with `gripper:+1`, center the held box over the bowl mouth, descend slowly with `step_clip` about 0.006-0.008 to eef z roughly 2-4 cm above the table surface in kitchen-frame bowl tasks, then call `release(max_steps=30-50)`.
**Falsify:** A future run repeatedly fires the predicate from a high hover release above the rim, or low seating inside the rim fails while a different placement geometry succeeds.
**Related:** [[flat-box-basket-interior-drop]]
