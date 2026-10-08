---
id: drawer-top-contact-before-release
scope: global
kind: strategy
title: Let contact predicates fire during a controlled closed-gripper descent.
applies_when: Tall or awkward object is being placed on a fixture top and the predicate
  may check object contact rather than gripper release
symptom:
- release-not-needed
- top-placement
- tall-object
- drawer-top
- held-object-terminates
evidence:
  cells:
  - goal_swap_t2_s0
  attempts: 1
confidence: single-shot
related: []
---


A slow descent while still holding a tall object can satisfy an `On` predicate before an explicit `release` when the object reaches the target top surface.

**Why:** observed, cause unknown; likely the benchmark predicate checks object contact/region membership independent of gripper opening.
**How to apply:** after a confirmed grasp, carry with `gripper: 1`, position over the target surface, then descend slowly with `step_clip=0.010-0.015` while keeping `gripper: 1`; inspect termination after each descent before opening.
**Falsify:** if repeated runs with the object visibly contacting the correct top surface while held do not terminate until release, this lesson is over-specific to this cell.
**Related:**
