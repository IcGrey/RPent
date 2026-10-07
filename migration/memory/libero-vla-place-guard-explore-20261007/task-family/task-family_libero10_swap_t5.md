---
id: task-family_libero10_swap_t5
scope: task-family
suite: libero10
regime: swap
task_id: 5
task_language: pick up the book and place it in the back compartment of the caddy
evidence:
  cells:
  - vla-place-pilot-20261006/explore
  - vla-place-pilot-20261006/explore-r2
confidence: single-shot
related:
- vla-place-guard-policy
---
## Retained identity and spatial knowledge
The target is the upright black book/binder, identifiable by its page block and
cover holes. The caddy target is the rear cell of the split middle column, paired
with the smaller front cell; full-depth side pockets are distractors. Use visible
partition topology, not image depth alone, to assign front/back. Wrist views may
be rotated; cross-check the same cavity against the agentview anchor. Interior
pixels are more useful than a mask median biased by rim/divider surfaces.

## Retained collision lessons
Lift until the entire hanging book clears the caddy rim before lateral motion.
Preserve its upright insertion orientation. Do not rotate a low held book inside
the dividers. Check object-to-gripper offset and the actual entry direction.

## Current exploration
Previous 40- and 80-step local VLA calls did not release and drifted/pitched into
partitions; those do not establish that every handoff will fail. A later seed used
only 20 VLA steps then scripted fallback successfully, not a VLA release success.
Test upright, rim-clear handoff and short observed increments. Prompt candidates
are 'place the book in the back compartment of the caddy' and, on a changed trial,
'put the book in the back compartment of the caddy'. Change one main variable at
reset and report other incidental changes. Do not script the insertion before VLA.
Read global/vla-place-guard-policy.md for the guard, stop criteria and audit fields.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_swap_t5_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_swap_t5.json`.
