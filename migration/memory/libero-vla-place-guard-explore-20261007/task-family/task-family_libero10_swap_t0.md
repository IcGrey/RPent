---
id: task-family_libero10_swap_t0
scope: task-family
suite: libero10
regime: swap
task_id: 0
task_language: put both the alphabet soup and the tomato sauce in the basket
evidence:
  cells:
  - 10_swap_t0_s0
  attempts: 4
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Two grocery CANS (alphabet soup + tomato sauce) both go into ONE small basket. The
grasps are easy and reliable; the ENTIRE difficulty is fitting BOTH cans so each
one's center stays inside the basket rim box. The basket interior floor is a
single-can pocket, so the second can cannot sit flat beside the first — it must be
wedged/leaned and, critically, kept from rolling out over the low front rim.


## Re-localization per scene
- tomato_sauce can: RED/tomato + GREEN band label. SAM3 'tomato sauce can' or
- alphabet_soup can: BLUE label, silver "Melissa & Doug" lid. Often OCCLUDED behind
  the ketchup 'Fancy' bottle. SAM3 brand nouns FAIL (collapse onto the other can);
  instead crop hi-res around the ketchup, find the blue can body + silver lid, and
  back-project lid pixels. Reject a candidate whose top z is table-level (that's the
- basket cavity: fully visible OR clipped at the +y frame edge depending on seed.
  The +y interior can extend OFF-FRAME. Find the FLOOR pocket by descend-until-stall
  probing, not by trusting a segment centroid (rim/liner biased). Floor pocket is
  ~single-can sized. DO NOT cache this run's absolute xyz; re-derive per scene.
