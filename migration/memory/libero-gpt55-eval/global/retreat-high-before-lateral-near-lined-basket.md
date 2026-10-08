---
id: retreat-high-before-lateral-near-lined-basket
scope: global
kind: strategy
title: After releasing into a lined basket, retreat straight up before moving laterally
applies_when: placing items into a woven/cloth-lined basket or any container with
  a soft rim/liner that stands above the rigid rim; especially multi-item drop-ins
  where you must traverse away between placements
symptom:
- basket dragged
- basket lifted
- container moved
- liner snagged
- gripper hooked cloth
- object displaced between placements
- OSC cannot lower loaded arm
evidence:
  cells:
  - 10_task_t1_s0
  attempts: 2
  solved_seeds:
  - 0
confidence: single-shot
related: []
---


The open gripper finger tips hang ~8-10cm BELOW the eef reference point, so a
lateral move at eef z<=0.62 drags the tips through basket-rim height (~z0.52-0.54)
and hooks the tall soft liner, dragging or lifting the whole basket.

**Why:** eef_pos is the wrist/flange point; the extended open fingers reach well
below it. A basket's cloth liner stands proud of the woven rim, presenting a soft
lip right at that finger-tip height. A lateral velocity there catches the lip;
a purely vertical retreat does not (the tips exit along the same corridor they
entered).

**How to apply:**
- After `release` into a basket, `move_to` STRAIGHT UP (same xy) to eef z>=0.72
  BEFORE any lateral motion; traverse between items at a high carry z (~0.72).
- Sequence multi-item drop-ins so the FINAL action is a place at the container
  (pick the far item first, place the near/last item last) — eliminates the
  fragile post-basket lateral traverse entirely.
- If a low lateral move near the container is unavoidable, keep the gripper
  CLOSED (+1) so the fingers are narrow, and route >15cm from the rim.

**Falsify:** if on a scene a lateral move at eef z~0.60 within 10cm of a lined
basket does NOT disturb it (e.g. a rigid rim with no proud liner), this
constraint is over-tight for that container.

**Related:** [[task-family_libero10_task_t1]]
