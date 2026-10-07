---
id: task-family_libero10_task_t4
scope: task-family
suite: libero10
regime: task
task_id: 4
task_language: put the yellow and white mug on the left plate and put the white mug
  on the right plate
evidence:
  cells:
  - vla-place-pilot-20261006/explore
  - vla-place-pilot-20261006/explore-r2
confidence: single-shot
related:
- vla-place-guard-policy
---
## Retained identity and spatial knowledge
Select the bicolor yellow-white mug and white textured mug; leave the tall red mug
alone. The historical task evidence maps yellow-white to the agentview-left plate
and white to the agentview-right plate in this scene. Identify both actual plates
from current RGB. Plate masks can be clipped/low confidence; use visible plate
interior pixels and wrist refinement rather than blindly using rim centroids.

## Retained grasp and collision lessons
Handle/rim grasps may be hooks rather than stable clamps. A false pick heuristic
can coexist with a held mug, and a closed-looking gripper can still be empty.
Verify retention after lift and rotation. Measure the held mug offset again after
carry; cup-center mask is not necessarily its base/support footprint. Keep routes
clear of the red mug and previously placed cup; rotate with full payload clearance.

## Current exploration
Use short handle-specific pi0_pick prompts and bounded pick budgets, visually
inspect retention, then carry high to a pre-contact view of the intended plate.
Use pi0_place for final centering, descent and release. The first mug previously
released after 48 VLA steps, but release alone did not solve the two-mug task.
For the white mug a prior 80+80-step continuation drifted far beyond its plate.
Test a fresh held-offset-aligned handoff, single-object destination prompt, and
short observed continuations. Inspect actual support, tilt and stability after
release and after open vertical retreat; a side-lying cup can overlap a plate yet
remain unsuccessful. Do not diagnose an unfulfilled predicate solely as gripper
proximity or left/right confusion without checking these images.

Prompt candidates: 'place the yellow and white mug on the left plate' and
'place the white mug on the right plate'. Explore changed handoff geometry first;
if prompt grounding selects the wrong plate, record that and change the prompt
on a distinct attempt. Read global/vla-place-guard-policy.md. No old action sequence
is provided or needed. Archive unsuccessful attempts without inventing success.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_task_t4_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_task_t4.json`.
