---
id: task-family_libero_goal_swap_t4
scope: task-family
suite: libero_goal
regime: swap
task_id: 4
task_language: Put the bowl on the top of the drawer
evidence:
  cells:
  - goal_swap_t4_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- drawer-top-contact-before-release
---


## Applicable pattern
Move a patterned bowl from the tabletop onto a visually relocated drawer/cabinet top in a `libero_goal_swap` kitchen-frame scene. The hard part is classifying the dark drawer top as the destination surface and carrying the bowl without letting Pi0 perform a learned placement.

## Winning technique
Use agentview RGB as the semantic authority: identify the patterned bowl and the black top surface of the drawer cabinet, not the plate or stove burner. Localize the bowl with `segment` prompt `the patterned bowl` in agentview, move above it, then accept a wrist `the patterned bowl` refinement only if it stays within about 3-5 cm of the agentview anchor. Localize the drawer top with `the black top of the drawer cabinet` in agentview; the top surface is dark and partly adjacent to rack geometry, so prefer a centered top-surface mask or multiple firm top pixels.

Grasp with `pi0_pick` using a short grasp-only prompt, then immediately `set_gripper +1`. Carry at high kitchen-frame z, stage the long y move through a midpoint, and keep `gripper: 1` on every carry/descent command. Place by moving above the drawer top with a bowl-rim y compensation of roughly +0.04 to +0.05 m relative to the top center, then descend slowly with the gripper still closed. In this run the official predicate fired during the slow closed-gripper descent before any explicit `release`.

## Magic numbers
Kitchen frame home z is about 1.17; use carry z=1.18 (band 1.16-1.20) for this compact fixture-top carry.

Bowl pre-position z=1.08 (band 1.06-1.10) from above the tabletop bowl.

`pi0_pick max_chunks=12` (band 8-14) with prompt `pick up the patterned bowl`; stop at lift and do not allow Pi0 to place.

`set_gripper +1` for 8 steps (band 5-12) immediately after the pick.

Carry step_clip=0.012-0.018; final descent step_clip=0.008-0.012 with `gripper: 1`.

Use bowl/destination y compensation of about +0.045 m when aligning the EEF over the drawer-top target.

NEVER omit `gripper: 1` from carry or descent while holding the bowl.

NEVER classify the stove burner or plate as the drawer top; RGB surface identity comes before flat-disc geometry.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| none observed | A1 solved | Keep Pi0 grasp-only, carry closed, and use slow closed-gripper descent over the drawer top. |

## Re-localization per scene
Bowl: prompt `the patterned bowl`; fallback prompt `the black and white patterned bowl`. It looks like a black/white floral-pattern bowl with a yellow rim. Confusions are the plate rim and stove burner rings; reject masks not centered on the bowl body.

Drawer top: prompt `the black top of the drawer cabinet`; fallback manual pixels on the dark horizontal top surface at the left fixture, avoiding vertical handles and the wooden rack slats. It looks like a dark rectangular cabinet top next to drawer handles and partly occluded by a slatted rack. Confusions are the stove cook region, black handle bars, and vertical cabinet faces; reject masks whose z/appearance correspond to handles or stove metal.

Absolute coordinates from this run, such as bowl wrist xyz near [-0.0669, 0.1307, 0.9277] and drawer top xyz near [-0.2793, -0.2571, 1.127], are counter-examples only and must not be cached.

## Fragility flags
The most fragile step is the destination alignment: the visible drawer top can be partly occluded by the rack and the held bowl. If the predicate does not fire on descent, reclassify the destination in agentview RGB and try a nearby top-surface point before assuming the bowl grasp failed.

A gripper reading near closed can still be a valid rim pinch for this bowl if the wrist/agentview image shows the bowl lifted. Use visual evidence plus immediate `set_gripper +1`.

## Difficulty and reliability
Solved in 1 attempt on seed 0. Expected single-shot rate is moderate when the drawer top is correctly segmented and the carry stays closed; reliability is lower if Pi0 is allowed more chunks or if destination identity is delegated to depth alone.

## Cross-refs
[[drawer-top-contact-before-release]]
