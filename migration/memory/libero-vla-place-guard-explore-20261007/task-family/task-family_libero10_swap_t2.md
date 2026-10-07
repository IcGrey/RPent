---
id: task-family_libero10_swap_t2
scope: task-family
suite: libero10
regime: swap
task_id: 2
task_language: turn on the stove and put the moka pot on it
evidence:
  cells:
  - 10_swap_t2_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Two-part kitchen task: (a) turn on the stove (knob), and (b) place the MOKA POT on
the stove cook-region. Both predicates must hold for termination. The SWAP variant
makes the placed object the moka pot (a chefmate frypan sits on the table center as
a DISTRACTOR with its handle over the burner — do NOT move it). KITCHEN frame


## Re-localization per scene
- moka pot: agentview hi-res, silver octagonal pot with black knob + black side
  handle; back_project its top surface (avoid the knob hole). Confusable only with
  the black frypan by shape — but the pot is silver/white, the pan is a flat black
  re-derive per scene; swap moves them.
- cook-region: darker gray coil disc on the stove fixture (RGB); when turned on it
  glows red — a strong confirmation the knob worked. Its center is the place target,
  NOT the frypan and NOT the flat metal to the right of the coil.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_swap_t2_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_swap_t2.json`.
