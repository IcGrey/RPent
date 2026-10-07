---
id: task-family_libero_goal_task_t0
scope: task-family
suite: libero_goal
regime: task
task_id: 0
task_language: open the bottom drawer of the cabinet
evidence:
  cells:
  - goal_task_t0_s0
  attempts: 62
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Fixture state-change task with a visually ambiguous cabinet front: several gray horizontal handles are visible, but the instruction requires the bottom drawer only.


## Re-localization per scene
Cabinet: dark rectangular cabinet at table edge; identify by RGB, not depth alone. It can be confused with the stove block or tabletop shadows.
Bottom drawer handle: lowest gray horizontal cylinder on the cabinet face. In this seed it is partly near the plate corridor; absolute coordinates must not be cached.
Upper/middle handles: gray cylinders above the bottom handle and wrong targets for this instruction. If the wrist frame centers these handles, reject the setup and move lower before contact.
Plate: white disc with red rings in front of the cabinet; it is an obstruction/distractor, not a destination.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/goal_task_t0_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_goal_task_t0.json`.
