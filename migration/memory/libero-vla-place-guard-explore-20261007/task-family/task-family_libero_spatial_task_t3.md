---
id: task-family_libero_spatial_task_t3
scope: task-family
suite: libero_spatial
regime: task
task_id: 3
task_language: Pick the akita black bowl on the top of the cabinet and place it on
  the plate
evidence:
  cells:
  - spatial_task_t3_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Duplicate patterned-bowl spatial task where the target bowl is elevated on a dark cabinet top and must be placed on the red-ring ceramic plate. The main test is semantic relation grounding before a difficult edge-of-workspace cabinet-top grasp.


## Re-localization per scene
Target bowl: describe as `the black patterned bowl on top of the dark cabinet`; it is partly image-clipped at the far negative-y/left side and sits on the dark cabinet, not on the cookie box. The segmentation may include cabinet pixels, so use the overlay for identity and wrist for geometry.
Cabinet top landmark: dark rectangular wooden surface with silver drawer handles beneath it; used only to identify the relation and elevation.
Plate destination: `the white plate with red rings`; white ceramic disc with red concentric rings. Do not confuse it with the gray stove burner disc.
Distractor bowl: `the black patterned bowl on the cookie box`; visually identical bowl on the red/yellow cookie box. Reject it by support relation.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/spatial_task_t3_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_spatial_task_t3.json`.
