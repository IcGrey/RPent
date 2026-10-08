---
id: place-order-never-carry-over-placed-object
scope: global
kind: strategy
title: Order multi-place tasks so nothing is carried or re-grasped over an already-placed
  fragile object
applies_when: a task requires placing two or more objects and one placement (e.g.
  an upright mug on a plate) is easily tipped by a later carry
symptom:
- tipped mug
- knocked over placed object
- second carry clipped first placement
- unrecoverable side-lying cylinder
evidence:
  cells:
  - 10_task_t6_s0
  attempts: 3
confidence: single-shot
related:
- predicate-gated-by-eef-proximity-retreat-clear
---


Sequence multi-object placements so that the LAST thing you place is the most
tip-prone one, and never route a later carry (or a pi0 re-grasp) over/near an
already-placed upright object.

**Why:** An object carried below the gripper hangs ~5-20 cm down; passing that
payload over an upright placed object at carry height clips and tips it, and a
side-lying mug/cup is unrecoverable (no side-grasp primitive; pi0 won't engage
it). In this cell, placing the mug first then carrying the pudding box across the
plate's y at the mug's x tipped the mug (A1); later, a pi0 re-grasp of a small
object ~0.15 m from the placed mug drifted into the mug and tipped it (A2).
**How to apply:** Put the tip-prone object (mug/cup) LAST. Place the flat/robust
object (box) first, on the side that clears the later path. Plan every later
waypoint so the payload never crosses the placed object's footprint (route
around the front at high x, or behind at low x, keeping |Δxy|<0.30 per step).
Do NOT pi0-re-grasp any small object within ~0.15 m of the placed object; pi0
drifts toward the larger/nearer body. If you must reposition, use a scripted
grasp, or reset and re-order.
**Falsify:** A scene where the later carry demonstrably cannot avoid the placed
object's footprint even with front/behind routing, or where pi0 re-grasps a
neighbor without drifting into the placed object.
**Related:** [[pi0-grasp-tall-mug-by-handle]]
