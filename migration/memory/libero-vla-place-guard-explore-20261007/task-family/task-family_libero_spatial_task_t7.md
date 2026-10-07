---
id: task-family_libero_spatial_task_t7
scope: task-family
suite: libero_spatial
regime: task
task_id: 7
task_language: Pick the akita black bowl on the top of the cabinet and place it on
  the plate
evidence:
  cells:
  - spatial_task_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Pick the spatially qualified black bowl from the top of the cabinet and place it on the visually classified plate. The task tests relation-grounded duplicate-bowl selection plus a stable bowl carry from an elevated cabinet surface.


## Re-localization per scene
Target bowl: in agentview_high, look for the patterned black bowl with yellow rim sitting on the dark cabinet top. It can be confused with the identical bowl on the metal cook region; reject candidates not physically on the cabinet surface. Segment phrasing to try: `the black bowl on the cabinet`; fallback: manual pixels on the interior/rim surface of the cabinet-top bowl.

Plate: in agentview_high, use RGB semantics for the white ceramic plate with red concentric rings. It can be confused geometrically with the metal cook region under the distractor bowl; reject dark/metal ring discs and fixture surfaces. Segment phrasing to try: `the white plate with red rings`; fallback: manual pixels on the visible inner plate surface.

Cabinet landmark: dark rectangular cabinet at image-left/side with silver handles. Use only as a relation landmark, not as a place target.

