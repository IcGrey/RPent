---
id: task-family_libero_spatial_swap_t3
scope: task-family
suite: libero_spatial
regime: swap
task_id: 3
task_language: Pick the akita black bowl on the cookies box and place it on the plate
evidence:
  cells:
  - spatial_swap_t3_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Pick the duplicate patterned black bowl that satisfies an elevated support relation, here the bowl visibly sitting on the cookies box, and place it on the semantically classified plate.

## Winning technique
Use agentview_high to choose the relation-satisfying bowl by elevation and support: the correct bowl is on the red/white cookies box, while the distractor bowl is table/cabinet-level. Back-project several target-bowl pixels, reject edge/table outliers, move above that anchor, and use wrist_high only to refine the same visible bowl.

For grasping, a generic visual prompt worked after two failed relation/brand prompts: pre-position on the open/table side of the bowl and call `pi0_pick` with `prompt="pick up the patterned bowl"`, `max_chunks=16`, `lift_thresh=0.05`, `gripper_closed_thresh=0.06`. Confirm a narrow gripper gap and the bowl raised in the wrist view, then `set_gripper +1` before carrying.

For placement, classify the red-rim white disc as the plate and reject the gray stove burner. Carry closed at kitchen height, descend slowly until the bowl is low on the plate, and release. If the bowl lands partly on the plate and the predicate does not fire, a short second `pi0_pick` from that low, already-on-plate pose can settle/lift it enough for the official predicate to become true.

## Magic numbers
Kitchen frame: home eef z about 1.17; use carry/pre-position z 1.05-1.10 for this bowl.

Target bowl pre-position: first successful approach was near the wrist-refined bowl xy but shifted toward the open/table side by about 3-5 cm in y from the cabinet/front obstruction.

Pi0 successful grasp: `max_chunks=16` (usable band 14-18), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Grip lock: `set_gripper(gripper=1, steps=10)` after the successful pick.

Carry: `step_clip=0.015` (band 0.012-0.020) with `gripper=1`.

Placement descent: eef z about 0.96-0.98 before opening. Do not release high.

Never let the stove burner count as the plate; it is a gray ring disc at similar height but is not the named destination.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Pi0 contacts bowl but reopens with no lift | A1 step2 and step4: relation/brand prompts from a cabinet-crowded pre-position did not complete the grasp; final gripper opening about 0.073-0.078 and peak lift about 0.03 m | Re-pre-position from the open/table side and use the simpler visual prompt `pick up the patterned bowl` with max_chunks around 16 |
| Release leaves bowl partly on plate but predicate remains false | A1 step10: placement used an eef y offset that left the bowl biased to the plate rim rather than fully centered | Re-engage from the low-on-plate pose with a short `pi0_pick`, or on a clean rerun use less y offset / a more centered plate target before release |

## Re-localization per scene
Target bowl: identify in agentview_high as the patterned black bowl elevated on the oatmeal-raisin cookies box. Segment phrase to try: `the patterned bowl on the cookies box`; fallback: manual pixels firmly inside the bowl and on the visible rim. Reject samples that land at table z or far from the visible bowl cluster.

Distractor bowl: identical patterned bowl on the cabinet/table surface. It is useful only as a negative example; do not select by object name suffix.

Cookies box: red/white package under the target bowl. Use it as a relation/elevation landmark, not as a grasp target.

Plate: white ceramic disc with red concentric rim, on the left side of agentview. Segment phrase to try: `the red rim white plate`; fallback: manual pixels on the white interior and red rim. Reject the gray stove burner as a flat-disc look-alike.

This run's absolute coordinates are counter-examples only and must not be cached: target bowl coarse samples around x 0.01-0.03, y 0.01-0.025 with a rejected outlier; plate samples around x 0.02-0.08, y -0.30 to -0.24.

## Fragility flags
The most fragile step is the first grasp because the bowl is next to the cabinet handle and identical to a distractor. If Pi0 contacts but does not lift, change contact geometry toward the open/table side before changing max_chunks upward.

The second fragile step is release alignment. If the bowl is visibly on the correct plate but not terminated, do not assume wrong target; first try a low-pose settle/regrasp or use a more centered plate target on reset.

## Difficulty and reliability
Solved in one episode with in-place recovery. Expected single-shot reliability is moderate: identity is easy from agentview_high, but grasp and placement are sensitive to approach side and plate centering.

## Cross-refs
None.
