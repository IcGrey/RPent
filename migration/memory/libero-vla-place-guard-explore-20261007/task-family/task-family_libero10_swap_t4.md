---
id: task-family_libero10_swap_t4
scope: task-family
suite: libero10
regime: swap
task_id: 4
task_language: put the white mug on the left plate and put the yellow and white mug
  on the right plate
evidence:
  cells:
  - 10_swap_t4_s0
  attempts: 24
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern

Two visually distinct mugs must remain upright on two look-alike plates while a tall distractor constrains the carry corridor. In this swap cell, the successful predicate binding used visual image sides, not the previously assumed robot-frame left/right mapping.


## Re-localization per scene

- Yellow/white target mug: agentview authority; short two-tone yellow body with white interior, distinct from the tall red patterned mug and textured white mug. Manual RGB points plus 3-8 interior/body back-projections worked. If using segmentation, try `yellow and white mug`, then `short yellow cup with white rim`; reject any mask >5 cm from the agentview anchor or on the red mug.
- White target mug: agentview authority; short textured/pebbled white porcelain body with a side handle. Prompts `white textured mug` or `white mug by the handle`; reject smooth red/yellow candidates and wrist jumps >5 cm.
- Plates: ceramic white discs with concentric red rings, not generic flat circular surfaces. Agentview identifies both semantics; wrist region midpoint refines the visible well/rim. Use the entire visible plate well, not one rim pixel.
- Red distractor: tall red patterned mug between the carry lanes; localize its top/footprint to design a far-negative-x route.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_swap_t4_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_swap_t4.json`.
