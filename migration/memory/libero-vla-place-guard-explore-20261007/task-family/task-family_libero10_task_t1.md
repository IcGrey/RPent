---
id: task-family_libero10_task_t1
scope: task-family
suite: libero10
regime: task
task_id: 1
task_language: put both the alphabet soup and the butter in the basket
evidence:
  cells:
  - 10_task_t1_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Two-items-into-a-lined-basket. Pick two distinct table groceries (a can + a box)
and place BOTH inside a woven basket that has a tall soft cloth liner standing
above its rim. Predicate = In(soup,basket) AND In(butter,basket); it fires when
the second item enters the basket volume (fired on descent, no explicit release
needed for the final item). The real difficulty is NOT the grasps (both easy) —
it is not disturbing the basket between the two placements.


## Re-localization per scene
- alphabet_soup: blue can with silver lid, "AL"/sunflower art, sits behind the
  orange-juice carton on the LEFT. Confuser: the tomato_sauce can (red/green,
  oranges) elsewhere on the table — do NOT grab that one. Prompt for pi0 by
  position (pre-position over it), not by brand. SAM prompt "the blue can" ok.
  "pick up the butter box" grasps it top-down cleanly.
- basket: woven, on the RIGHT, partly off the right frame edge (segment box
  clipped at col 1024) -> its true center is slightly more +y than the visible
- THIS RUN'S ABSOLUTE XYZ ARE COUNTER-EXAMPLES ONLY — re-derive every coordinate
  from the current scene's back_project.
