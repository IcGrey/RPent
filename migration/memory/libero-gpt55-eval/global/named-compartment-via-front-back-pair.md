---
id: named-compartment-via-front-back-pair
scope: global
kind: perception
title: Disambiguate a "back/front compartment" by finding the divided front/back PAIR,
  not by absolute depth
applies_when: task names a "back" or "front" compartment of a multi-cell container
  (caddy/organizer/tray)
symptom:
- back compartment
- front compartment
- which compartment
- caddy
- desk organizer
- multiple openings
evidence:
  cells:
  - 10_swap_t5_s0
  attempts: 1
confidence: single-shot
related: []
---


When a container has several openings but the task says "the BACK/FRONT
compartment", the intended target is the opening whose sibling is the explicit
opposite — i.e. the column/region that is actually split into a front cell and a
back cell — not merely whichever opening is furthest from (or nearest to) the
robot.

**Why:** "front/back" is a relational label the BDDL region attaches to a
front-back divided sub-structure. A caddy can have full-depth side compartments
(neither front nor back) plus one middle column split into front+back; only that
middle pair carries the front/back names. Choosing by raw x-depth would wrongly
pick a full-depth side cell that sits at the same back x.

**How to apply:** In the hi-res agentview RGB, find the region that has a
front/back DIVIDER (two stacked cells). The rear cell of that pair = "back
compartment", the near cell = "front compartment". Get the target cell's interior
center with region `back_project` over its dark interior pixels. Confirm the book
fits at the current wrist yaw; rotate_wrist 90deg only if the held object's long
axis lies along the cell's short axis.

**Falsify:** a caddy task where "back compartment" resolves to a full-depth side
cell (no front sibling), or where the predicate region is the whole rear row
rather than the divided pair's rear cell.

**Related:** [[task-family_libero10_swap_t5]]
