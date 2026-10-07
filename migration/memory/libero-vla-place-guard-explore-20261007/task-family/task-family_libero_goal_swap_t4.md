---
id: task-family_libero_goal_swap_t4
scope: task-family
suite: libero_goal
regime: swap
task_id: 4
task_language: Put the bowl on the top of the drawer
evidence:
  cells:
  - goal_swap_t4_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Move a patterned bowl from the tabletop onto a visually relocated drawer/cabinet top in a `libero_goal_swap` kitchen-frame scene. The hard part is classifying the dark drawer top as the destination surface and carrying the bowl without letting Pi0 perform a learned placement.


## Re-localization per scene
Bowl: prompt `the patterned bowl`; fallback prompt `the black and white patterned bowl`. It looks like a black/white floral-pattern bowl with a yellow rim. Confusions are the plate rim and stove burner rings; reject masks not centered on the bowl body.

Drawer top: prompt `the black top of the drawer cabinet`; fallback manual pixels on the dark horizontal top surface at the left fixture, avoiding vertical handles and the wooden rack slats. It looks like a dark rectangular cabinet top next to drawer handles and partly occluded by a slatted rack. Confusions are the stove cook region, black handle bars, and vertical cabinet faces; reject masks whose z/appearance correspond to handles or stove metal.

