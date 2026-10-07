---
id: task-family_libero10_swap_t8
scope: task-family
suite: libero10
regime: swap
task_id: 8
task_language: put both moka pots on the stove
evidence:
  cells:
  - 10_swap_t8_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Place two wide moka pots on one stove plate. The core difficulty is grasping thin side handles and reaching both swapped handle locations at a cross-handle yaw without losing the first placement.


## Re-localization per scene
- Pot bodies: agentview authority; silver octagonal two-tier vessels with white lids, black knobs, and curved black side handles. Sample 3-8 lid/body pixels, reject table/edge depths.
- Handles: wrist geometry only after moving above the agentview-selected pot. Use the visible black free tube segment, not the cap knob or white hinge. Direct pixel back-projection worked; no SAM3 score was used, so no score floor is established.
- Stove: agentview semantic authority; choose the red concentric coil on the gray metal plate, not the nearby black knob or any plate-like disc. Wrist center refinement is accepted only when it agrees within a few cm.
- Absolute coordinates from this seed must not be cached; they are counter-examples only. Recompute every body, handle, stove center, and held offset.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_swap_t8_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_swap_t8.json`.
