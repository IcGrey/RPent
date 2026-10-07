---
id: task-family_libero_spatial_swap_t6
scope: task-family
suite: libero_spatial
regime: swap
task_id: 6
task_language: Pick the akita black bowl next to the cookies box and place it on the
  plate
evidence:
  cells:
  - spatial_swap_t6_s0
  attempts: 49
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
A duplicate-object spatial-relation pick where the correct patterned bowl is the one adjacent to the cookies box, followed by a cramped bowl-on-plate placement onto a red-ring plate partly hidden by cabinet/metal support geometry.


## Re-localization per scene
Target bowl: visually the patterned black-and-white bowl whose rim is adjacent to the cookies box. Segment phrasing can be `the black patterned bowl next to the cookies box`, but manual agentview pixels were more reliable here. Reject the duplicate by relation to cookies and global layout.

Cookies box: red/white/yellow oatmeal-raisin cookies package between the bowls; use it only as a relation landmark and avoid disturbing it.

Plate: white ceramic disc with red concentric rings on a square silver/metal support near the cabinet. It is semantically a plate, not the gray support or ramekin. Back-project pixels on the red-ring/white ceramic surface and region-filter z around the plate surface. The visible fragment is edge-biased; use several samples.



## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/spatial_swap_t6_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_spatial_swap_t6.json`.
