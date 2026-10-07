---
id: task-family_libero_spatial_swap_t3
scope: task-family
suite: libero_spatial
regime: swap
task_id: 3
task_language: Pick the akita black bowl on the cookies box and place it on the plate
evidence:
  cells:
  - spatial_swap_t3_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Pick the duplicate patterned black bowl that satisfies an elevated support relation, here the bowl visibly sitting on the cookies box, and place it on the semantically classified plate.


## Re-localization per scene
Target bowl: identify in agentview_high as the patterned black bowl elevated on the oatmeal-raisin cookies box. Segment phrase to try: `the patterned bowl on the cookies box`; fallback: manual pixels firmly inside the bowl and on the visible rim. Reject samples that land at table z or far from the visible bowl cluster.

Distractor bowl: identical patterned bowl on the cabinet/table surface. It is useful only as a negative example; do not select by object name suffix.

Cookies box: red/white package under the target bowl. Use it as a relation/elevation landmark, not as a grasp target.

Plate: white ceramic disc with red concentric rim, on the left side of agentview. Segment phrase to try: `the red rim white plate`; fallback: manual pixels on the white interior and red rim. Reject the gray stove burner as a flat-disc look-alike.

