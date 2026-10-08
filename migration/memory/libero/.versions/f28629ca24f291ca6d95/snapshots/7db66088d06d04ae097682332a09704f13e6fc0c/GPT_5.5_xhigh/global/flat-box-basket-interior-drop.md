---
id: flat-box-basket-interior-drop
scope: global
kind: strategy
title: Drop flat boxes into basket interiors before opening.
applies_when: placing a long flat grocery box into a woven basket or cloth-lined container
symptom:
- basket
- flat box
- perched
- liner
- release false
- pushed out
evidence:
  cells:
  - object_swap_t8_s0
  attempts: 2
confidence: single-shot
related: []
---


A long, flat box that visually reaches the basket mouth may still fail `In` unless the held object is centered inside the liner before the gripper opens.

**Why:** observed, cause unknown. In this run, a front/rim-biased release left the chocolate pudding perched and post-release pushes ejected it, while a more interior/back held release at the same reachable z triggered termination.

**How to apply:** localize the basket cavity visually, bias the held-box release away from the front rim, carry with `gripper:+1`, descend slowly with `step_clip` about 0.005-0.008 until OSC stalls or reaches the basket floor, then use `release(max_steps=30-50)`. Avoid lateral pushes toward the front wall after opening.

**Falsify:** if a future run repeatedly terminates from a rim-biased hover release with the same flat-box geometry, or if interior/back releases fail while front-rim pushes solve without ejecting the box.

**Related:**
