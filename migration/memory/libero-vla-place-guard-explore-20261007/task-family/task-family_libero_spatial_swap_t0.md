---
id: task-family_libero_spatial_swap_t0
scope: task-family
suite: libero_spatial
regime: swap
task_id: 0
task_language: Pick the akita black bowl between the plate and the ramekin and place
  it on the plate
evidence:
  cells:
  - spatial_swap_t0_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Duplicate-bowl spatial disambiguation plus hard bowl-on-plate seating. In the swap variant, choose the black bowl that is physically between the red-rim plate and the gray ramekin, not a named instance or the duplicate that looks easier to reach.


## Re-localization per scene
Target bowl: description `the patterned black bowl between the red-rim plate and the gray/silver ramekin`. It is visually identical to the other black bowl except for its relation; reject any candidate whose xy is not between the plate and ramekin landmarks. Wrist refinement is accepted only if it is still the same agentview-selected bowl.

Plate: description `red-rim white ceramic plate`. It is a white disc with red concentric rings. In kitchen scenes, do not confuse it with the dark gray stove burner; RGB semantics decide the destination before depth.

Ramekin: description `small silver gray ridged cup/dish`. It is only a relation landmark. Use it to disambiguate which duplicate bowl is between the two surfaces.

