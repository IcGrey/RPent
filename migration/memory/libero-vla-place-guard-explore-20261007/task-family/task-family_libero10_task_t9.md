---
id: task-family_libero10_task_t9
scope: task-family
suite: libero10
regime: task
task_id: 9
task_language: put the white mug in the microwave and close it
evidence:
  cells:
  - 10_task_t9_s0
  attempts: 90
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern

Insert a wide mug through an open microwave/door threshold, disengage an internal rim hook without extracting the mug, clear the wrist, then close the hinged door physically.


## Re-localization per scene

- Target mug: agentview semantic authority; choose the textured all-white mug, reject the smooth yellow/white distractor. Use rim/body/handle RGB pixels and 3-8 back-projections; wrist accepts only geometry within 3-5cm of the anchor. No SAM score was used in the winning run.
- Microwave cavity: identify the black appliance opening in agentview RGB; flat/dark depth alone is insufficient. Reject wrist views that show the distractor or exterior.
- Door: back-project free vertical edge and hinge from agentview; derive the closing tangent from their current locations.
- This run's absolute coordinates are counter-examples only and must not be cached; every reset/seed requires re-localization.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_task_t9_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_task_t9.json`.
