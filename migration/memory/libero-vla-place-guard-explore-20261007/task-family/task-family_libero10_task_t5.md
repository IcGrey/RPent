---
id: task-family_libero10_task_t5
scope: task-family
suite: libero10
regime: task
task_id: 5
task_language: pick up the cup and place it in the back compartment of the caddy
evidence:
  cells:
  - 10_task_t5_s0
  attempts: 4
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Pick a white/yellow mug ("cup") from the open table and place it into a NAMED
compartment of a brown multi-compartment desk caddy (a fixture). The whole
difficulty is TARGET IDENTITY: the caddy has several look-alike pockets and the
task names one ("back compartment"). The manipulation itself is a trivial
pick + lower-into-pocket. This is a disambiguation task, not a dexterity task.


## Re-localization per scene
- Caddy: brown leather desk organizer, fixture (not in object_names). Segment
  "caddy"/"brown organizer"; back_project pocket floors/rims. Long axis = world-y
- "back compartment": DO NOT cache this run's absolutes. Re-derive per scene: it is
  the caddy's local-back pocket = the shallow pocket on the NEAR-robot side (the
  one with smallest |world-x|, in front of the tall deep row). Confirm the near
  pocket in RGB (a low-walled open pocket, distinct from the tall deep pockets and
  from the raised solid platform). Deep far pockets are DECOYS for this task.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_task_t5_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_task_t5.json`.
