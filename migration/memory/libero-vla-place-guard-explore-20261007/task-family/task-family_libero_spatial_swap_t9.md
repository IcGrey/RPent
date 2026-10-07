---
id: task-family_libero_spatial_swap_t9
scope: task-family
suite: libero_spatial
regime: swap
task_id: 9
task_language: Pick the akita black bowl on the wooden cabinet and place it on the
  plate
evidence:
  cells:
  - spatial_swap_t9_s0
  attempts: 6
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Pick one of two visually identical patterned bowls by a support relation, then place it on a nearby plate in the kitchen frame. The hard part is not semantic target choice once relation-grounded; it is the large held-bowl offset from Pi0's cabinet-rim grasp.


## Re-localization per scene
Target bowl: identify the patterned akita black bowl on top of the wooden cabinet in agentview_high. It looks like a grey/white patterned bowl with a yellow rim, partially clipped by the cabinet edge. Confused with the identical patterned bowl on the stove; use the support relation, not name suffix. Back-project only pixels clearly inside the bowl surface or use wrist confirmation; pixels on the clipped cabinet edge can return impossible off-table xyz and must be rejected.


Distractors: the stove bowl is identical but sits on the metal stove support; the ramekin is a white fluted cup on the table; the cookies box is flat and irrelevant except as a wrist-view landmark.
