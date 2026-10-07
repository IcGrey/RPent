---
id: task-family_libero10_swap_t1
scope: task-family
suite: libero10
regime: swap
task_id: 1
task_language: put both the cream cheese box and the butter in the basket
evidence:
  cells:
  - 10_swap_t1_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Two named BOXES (cream_cheese "Cream Cheese / Fresh Taste" blue-oval box, butter
"FARM FRESH BUTTER" red box) must both go into a table-right basket, among 4
distractor groceries (alphabet_soup can, tomato_sauce can, ketchup bottle, milk
carton, OJ carton). LIVING_ROOM frame. Tests brand-noun disambiguation (SAM3 and
Pi0 grounding both fail on the brand) and multi-object basket placement. Because
both items are BOXES, placement is far easier than the sibling 2-CAN task (t0).


## Re-localization per scene
- butter: RGB "FARM FRESH BUTTER" red/orange box with a cow; standing. Confused
  with tomato_sauce can lid in agentview z-scan — reject any candidate whose
  wrist view shows a round metal lid; keep only the box face. Score floor N/A
- cream_cheese: RGB blue "Cream Cheese / Fresh Taste" oval on white box; standing,
  tucked behind the OJ carton. Distinguish from OJ (orange) and milk (white/red).
  Cavity center from liner pixels; re-derive per scene, movable.
