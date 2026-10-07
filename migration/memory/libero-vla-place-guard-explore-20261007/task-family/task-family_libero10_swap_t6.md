---
id: task-family_libero10_swap_t6
scope: task-family
suite: libero10
regime: swap
task_id: 6
task_language: put the white mug on the plate and put the chocolate pudding to the
  right of the plate
evidence:
  cells:
  - 10_swap_t6_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Two-clause LIVING_ROOM tabletop conjunction: (1) place the WHITE mug
(porcelain_mug_1, gray/white DIMPLED mug) On the plate, and (2) place the
chocolate-pudding box "to the right of" the plate. A RED mug (red_coffee_mug_1)
is a DISTRACTOR — "white mug" is the target; do not grab the red one. This is the
same base task as libero10 task-t6 (there the target was the RED mug and the
white/porcelain mug was the distractor — the swap perturbation flips which mug
is named). The real difficulties are the two predicate subtleties, not the grasps:
the "right" side SIGN, and confirming the mug On() half.


## Re-localization per scene
- white mug: agentview hi-res, gray/white DIMPLED-texture mug. `segment "the white
- red mug: tall red-with-white-pattern mug = DISTRACTOR (this task). Ignore.
- plate: white disc with red concentric rings; region back_project the rings for a
- pudding: small brown box reading "CHOCOLATE PUDDING"; pi0 grasps top-down; the
- This run's absolute xyz MUST NOT be cached (swap re-randomizes); counter-examples only.
