---
id: knob-side-front-zone
scope: global
kind: strategy
title: Treat fixture front as the control/handle side when edge placements fail.
applies_when: A task asks for an object at the front of a stove or appliance and visible
  edge or surface placements look correct but remain nonterminal.
symptom:
- front of stove
- burner edge nonterminal
- under platform
- wrong surface
- hidden region
evidence:
  cells:
  - goal_swap_t5_s0
  attempts: 74
confidence: single-shot
related: []
---


Some appliance-front predicates can correspond to the control or handle side of the fixture, not the visually nearest burner/platform edge in the camera image.

**Why:** Observed in `goal_swap_t5_s0`: dozens of low pushes and held releases onto the visible stove platform, burner edge, table-adjacent edge, and negative-y side stayed nonterminal; a high held carry toward the black knob/handle side terminated before release.
**How to apply:** First classify the fixture in RGB and explicitly locate its control/handle side. If edge/cooktop placements stay false, keep the object held, carry high enough to avoid base-lip jams, and move toward the control/handle-side front zone with `move_pose(..., gripper=1)` rather than scraping under the platform.
**Falsify:** A future cell where a correctly localized handle-side/front carry remains nonterminal while a visible-edge placement terminates would contradict the general rule or narrow it to this fixture orientation.
**Related:** []
