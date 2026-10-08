---
id: task-family_libero10_swap_t8
scope: task-family
suite: libero10
regime: swap
task_id: 8
task_language: put both moka pots on the stove
evidence:
  cells:
  - 10_swap_t8_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- moka-pot-grasp-the-handle-not-the-body
- co-vary-pitch-clears-yawed-reach-wall
- libero-in-predicate-fires-while-grasped
---


## Applicable pattern
Place two wide moka pots on one stove plate. The core difficulty is grasping thin side handles and reaching both swapped handle locations at a cross-handle yaw without losing the first placement.

## Winning technique
1. Identify both moka pots globally in agentview and refine each black handle tube with wrist back-projection. Semantically classify the red concentric coil as the stove destination.
2. Grasp the easier/reachable handle first. Use yaw about +1.57 rad so fingers close across the tube; descend to eef z about 1.00 and close for 12 steps. Require gap about 0.021 m and visible lift.
3. Measure the held body offset per pick. Carry low with gripper +1; when yaw-held move_to stalls, use move_pose with pitch about 0.15 while preserving yaw.
4. Put the first pot on one half of the stove, descend until support stalls, and release. Retreat vertically.
5. Approach the second handle with pitch about 0.15 and yaw +1.57; this crossed the reach wall that blocked pitch 0. Repeat the handle close/lift.
6. Carry in short low hops to the unoccupied half. Descend slowly while still holding; success fired as soon as the second body was supported in the stove region.

## Magic numbers
- Handle cross-grasp yaw: 1.57 rad (usable band 1.4-1.7).
- Reach-clearing pitch: 0.15 rad (observed usable band 0.15-0.22 for localization/carry; only 0.15 tested for handle grasp).
- Handle hover eef z: 1.08 (band 1.07-1.10 in KITCHEN frame).
- Handle close eef z: 1.00-1.008; close +1 for 12 steps (band 10-14).
- Good initial handle gap: 0.021 m (band 0.016-0.024).
- Low lift/carry eef z: 1.046-1.052 (band 1.04-1.06).
- Fine descent step_clip: 0.003-0.004; carry step_clip: 0.005-0.006.
- NEVER use pi0_pick on this moka-pot geometry when it descends without closing.
- NEVER use yaw -1.57 at the image-left handle in this layout; it drove y to -0.404.
- NEVER carry with gripper -1.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Pi0 descends but opening stays 0.074-0.077 | A1: Pi0 did not issue a close on the wide pot | manually grasp the thin handle |
| scripted close reaches gap ~0.0045 | A1: body/top approach closed on air after Pi0 tilted the wrist | reset cleanly; handle grasp from a controlled pose |
| +1.57 yaw hover stalls 5.05 cm short at pitch 0 | A2: observed yawed OSC reach wall, cause unknown | co-vary pitch about 0.15 in move_pose |
| -1.57 yaw sends eef to y=-0.404 | A2: opposite yaw branch diverged | recover centrally; use +1.57 |
| yaw-held carry stalls at x=0.083 | A2: observed carry reach wall, cause unknown | move_pose with pitch 0.15 reached x=0.141 |
| first pot settles sideways after release | A2: pitched handle placement was not upright-stable | keep its body fully on the stove; reserve separate space for pot two; success can still hold |
| final descent terminates before release | A2: On predicate fired while object remained grasped | stop immediately; release is unnecessary |

## Re-localization per scene
- Pot bodies: agentview authority; silver octagonal two-tier vessels with white lids, black knobs, and curved black side handles. Sample 3-8 lid/body pixels, reject table/edge depths.
- Handles: wrist geometry only after moving above the agentview-selected pot. Use the visible black free tube segment, not the cap knob or white hinge. Direct pixel back-projection worked; no SAM3 score was used, so no score floor is established.
- Stove: agentview semantic authority; choose the red concentric coil on the gray metal plate, not the nearby black knob or any plate-like disc. Wrist center refinement is accepted only when it agrees within a few cm.
- Absolute coordinates from this seed must not be cached; they are counter-examples only. Recompute every body, handle, stove center, and held offset.

## Fragility flags
The most fragile step is reaching the image-left handle at cross-handle yaw: pitch 0 stalled, but pitch 0.15 succeeded. Fallback: recover to a central high pose and use co-varied move_pose, then wrist-refine again. The second fragility is first-pot stability; avoid carrying over it and use the remaining stove half.

## Difficulty and reliability
Solved on attempt 2 after attempt 1 failed to grasp. The validated manual-handle route succeeded for both pots in one episode, but first-pot tipping makes single-shot reliability moderate rather than high. The On predicate tolerated the tipped first pot and fired with the second still held.

## Cross-refs
- [[moka-pot-grasp-the-handle-not-the-body]]
- [[co-vary-pitch-clears-yawed-reach-wall]]
- [[libero-in-predicate-fires-while-grasped]]
