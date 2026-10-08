---
id: task-family_libero_spatial_swap_t4
scope: task-family
suite: libero_spatial
regime: swap
task_id: 4
task_language: Pick the akita black bowl in the top layer of the wooden cabinet and
  place it on the plate
evidence:
  cells:
  - spatial_swap_t4_s0
  attempts: 34
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
LIBERO spatial swap t4 presents two identical patterned bowls near a cabinet and a red-ring plate. In this swap cell, the successful predicate followed the drawer/open-cabinet bowl from the seed-0 reference, while many visually plausible cabinet-top-bowl placements did not terminate.

## Winning technique
Use agentview RGB for identity and wrist only to confirm geometry. Select the patterned bowl sitting in the open drawer/cabinet cavity, not the elevated duplicate on the cabinet top, then place it on the red-ring plate.

Winning sequence: move above the drawer bowl at safe kitchen z, run full task-language `pi0_pick` with a long enough budget for the drawer-context grasp, keep `gripper=1`, slow-lift, travel to the plate with eef y biased about +0.03 to +0.04 beyond the plate center, descend to z around 1.10, and release. Success criterion is `terminated:true` immediately after release.

## Magic numbers
`max_chunks=30` for the source drawer pick; usable band observed 28-32. `max_chunks=20` or 30 on the wrong top-bowl semantic route can let Pi0 self-deliver to a non-terminal state.
`move_to` source prepose z=1.20; usable band 1.19-1.22.
Slow lift after grasp: `step_clip=0.008` to z=1.22; usable band 0.006-0.010.
Plate travel/release eef xy around `[plate_x, plate_y + 0.035]`; solved release used `[0.078, 0.071, 1.10]` in this scene.
Never carry with `gripper=-1`; every held `move_to` used `gripper=1`.
Never cache this run's absolute xyz; re-localize per scene.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Pi0 misses or grips air at the elevated cabinet-top bowl | A1-A8 used close prepose, short prompts, side rim grasps, yaw, move_pose, or contact nudges on the elevated duplicate | Treat the drawer/open-cabinet bowl as the swap target unless new predicate evidence contradicts it; use full-context drawer pick |
| Upright bowl visibly overlaps the plate but predicate stays false | A9-A32 repeatedly placed the elevated duplicate or tuned non-terminal placements | Re-check target semantics before tuning contact mechanics |
| Lower/drawer semantic probe fails with short drawer prompt | A33 used a drawer-specific prompt but did not reproduce the solved full-context recipe | Use the full task-language prompt from a precise drawer-bowl prepose and allow `max_chunks=30` |

## Re-localization per scene
Drawer/open-cabinet bowl: looks like the black floral patterned bowl sitting inside the pulled-out wooden drawer/cabinet cavity. Agentview phrase: `the patterned black bowl in the open drawer of the wooden cabinet`; fallback: manually sample pixels on the visible interior/bottom of that bowl. Reject wrist refinements that jump to the elevated cabinet-top duplicate.

Cabinet-top duplicate: same patterned bowl on the upper dark wooden top. It is a distractor for this solved swap predicate despite matching the literal phrase in the task text in prior failed runs.

Plate: white ceramic disc with red concentric rings. Agentview phrase: `the white plate with red rings`; fallback: sample the white interior and ring midpoint, not the rim edge. Confused with none in this scene except fixture discs in other kitchen scenes.

## Fragility flags
Most fragile step is semantic target selection. If a clean placement does not terminate, suspect wrong duplicate before spending attempts on small final nudges.

Second fragile step is drawer grasp reliability. Use the full task-language prompt and `max_chunks=30`; confirm by wrist that the drawer bowl lifted and the top duplicate remains behind.

## Difficulty and reliability
This converged after 34 archived attempts because earlier runs optimized placement of the wrong duplicate. Expected single-shot reliability is moderate once the drawer-bowl semantic correction is applied; the drawer Pi0 grasp can still be stochastic, but this solved run completed in one recipe pass.

## Cross-refs
None yet.
