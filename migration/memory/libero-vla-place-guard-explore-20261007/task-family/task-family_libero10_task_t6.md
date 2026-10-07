---
id: task-family_libero10_task_t6
scope: task-family
suite: libero10
regime: task
task_id: 6
task_language: put the red mug on the plate and put the chocolate pudding to the right
  of the plate
evidence:
  cells:
  - 10_task_t6_s0
  attempts: 3
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Two-clause LIVING_ROOM tabletop task: (1) place a TALL red mug On a plate, and
(2) place a chocolate-pudding box "to the right of" the plate. The real
difficulties are NOT the grasps — they are (a) the tall mug's grasp geometry,
(b) the ordering so the second carry does not tip the first placement, and


## Re-localization per scene
- red mug: agentview hi-res, tall red-with-white-pattern mug. Grasp target is the
  thin curved HANDLE (offset to one side). Do NOT trust wrist to re-identify.
- plate: white disc with red concentric rings; use region back_project over the
- pudding: brown box reading "CHOCOLATE PUDDING". Distinct; pi0 grasps top-down.
- porcelain mug: white dimpled mug = DISTRACTOR, never named. Ignore.
- This run's absolute xyz MUST NOT be cached (task perturbation re-randomizes);
  they are counter-examples only.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_task_t6_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_task_t6.json`.
