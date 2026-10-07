---
id: task-family_libero_goal_task_t7
scope: task-family
suite: libero_goal
regime: task
task_id: 7
task_language: Turn off the stove
evidence:
  cells:
  - goal_task_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
A fixture state-change task where the goal is to turn a stove knob off, not to move any loose object. The correct primitive is controlled contact with the stove control, with object localization used only to identify the fixture and knob.


## Re-localization per scene
Stove: in agentview RGB, look for the white rectangular stove fixture with the gray concentric-ring burner. It can be confused with plates because both are circular/ringed; classify the surrounding rectangular metal stove base before acting.

Control knob: look for the black upright oval/vertical control just behind or above the burner on the stove fixture. Prompt `the black stove control knob` worked with a low but valid score. If SAM score is low, accept only when the overlay covers the visible knob body; manual back-project on the lower knob body is safer than the top silhouette, which can hit background.

Burner: prompt `the stove burner` is reliable for fixture confirmation. Do not use burner center as the contact target for turning the stove off.

Wrist: after the contact skill, wrist shows the gripper near the stove control/burner, but no wrist refinement was needed before acting in this seed. If pre-staging is needed in another seed, accept wrist knob refinement only if it stays within about 3-5 cm of the agentview knob anchor.



## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/goal_task_t7_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_goal_task_t7.json`.
