---
id: task-family_libero10_swap_t7
scope: task-family
suite: libero10
regime: swap
task_id: 7
task_language: put both the alphabet soup and the cream cheese box in the basket
evidence:
  cells:
  - 10_swap_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Two-target pick-and-place into ONE basket. The test is (a) DISAMBIGUATION — one of
the two cans (alphabet soup) is a target, the other (tomato sauce) is a distractor,
plus a ketchup bottle; and (b) sequencing two placements into the same container.
Under `_swap` the object positions are re-randomized per seed, so re-derive every xyz.


## Re-localization per scene
- alphabet_soup: agentview hi-res, BLUE label can, prompt/crop-read "alphabet soup".
  Confused with tomato_sauce (red/green tomatoes) — reject the red-label can. Score
  floors on brand nouns are low; identify by colour+label, not SAM3 brand score.
- cream_cheese: blue rectangular box, distinct shape (only box on table).
- basket: woven basket, silver cloth liner; interior center via region back_project;
