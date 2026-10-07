---
id: task-family_libero_object_task_t3
scope: task-family
suite: libero_object
regime: task
task_id: 3
task_language: Pick the ketchup and place it in the basket
evidence:
  cells:
  - object_task_t3_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Single tall labeled grocery bottle into a soft/rimmed basket in the low object-table frame. The task tests brand/label identity among similar condiment bottles and cavity-centered placement.


## Re-localization per scene
Ketchup: identify by readable orange/red Tomato Ketchup label and gray cap in agentview_high.png. It can be confused with BBQ sauce because both are condiment-shaped; reject masks on the lower orange BBQ bottle or green-capped salad dressing. Prompt `the tomato ketchup bottle` worked; fallback is manual point prompting on the readable label or cap/body pixels.
Basket cavity: identify the woven basket with white cloth liner. Use `the basket interior` and verify overlay covers the inner liner, not just the rim. If mask centroid is rim-biased, use the visible cavity center from wrist/agentview and bias inward from front/side walls.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/object_task_t3_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_object_task_t3.json`.
