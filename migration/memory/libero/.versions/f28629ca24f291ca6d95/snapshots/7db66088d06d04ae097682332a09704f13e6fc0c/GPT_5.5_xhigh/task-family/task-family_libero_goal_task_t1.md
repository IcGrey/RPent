---
id: task-family_libero_goal_task_t1
scope: task-family
suite: libero_goal
regime: task
task_id: 1
task_language: Put the plate on the stove
evidence:
  cells:
  - goal_task_t1_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- visual-over-pick-heuristic
---


## Applicable pattern

Move a flat ceramic plate onto a visually similar gray circular stove cook region. The core issue is semantic surface classification plus compensating the large offset caused by Pi0 rim-grasping a thin plate.

## Winning technique

Identify the plate by RGB as the white ceramic disc with red rings, and the stove destination as the gray ringed cook region on the metal stove base. Pre-position above the plate, accept wrist refinement only if it agrees with the agentview plate anchor, then call `pi0_pick` with `pick up the plate`. After a visible rim grasp, run `set_gripper +1` and carry with `gripper:1` throughout.

Do not aim the EEF at the burner center. The plate center trails the gripper by a large offset after rim grasp. In this solved run, the predicate fired during a compensated closed-gripper carry farther beyond the burner, before `release`: the EEF moved first near the stove edge, then farther outward until the held plate footprint covered the cook region.

## Magic numbers

`pi0_pick` prompt `pick up the plate`, `max_chunks=20` (band 16-24), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Firm grip with `set_gripper +1` for 8 steps (band 6-10) after the plate rim is visibly clamped.

Carry with `gripper:1`; never omit gripper on a carry primitive.

Kitchen-frame carry/release altitude around `z=1.03-1.04` worked (band 1.03-1.05). Attempts to descend toward `z=0.94` from the stove edge stalled near `z≈1.03`.

Use slow compensated stove-side moves with `step_clip=0.008-0.012`. The final successful command targeted beyond the reachable edge and terminated at the actual final EEF near `x=-0.186, y=0.317, z=1.036`; treat those absolutes as this-scene counterexamples only, not reusable coordinates.

Never release when the plate is only at the front/table edge of the stove base; repick recovery is possible but dirty and unreliable.

## Failure modes

| symptom | root cause (A<N>) | fix |
|---|---|---|
| Plate released on the table/front edge beside the stove, predicate false | A1 aimed EEF near the perceived burner center or only slightly beyond it, ignoring the rim-grasp offset between gripper and plate center | Keep the first clean grasp and compensate much farther past the burner before release; watch the plate footprint, not the EEF |
| Local repick reports `success:false` but the plate is visibly held | A1 Pi0 heuristic failed on a thin/rim grasp even though wrist and agentview showed the plate in hand | Trust visual evidence and gripper/image state over the boolean; continue if the target is clearly held |
| Lowering toward the stove stalls high | A1 commanded `z=0.94` at the stove edge; OSC stopped near `z≈1.03` | Do not require low descent; terminate by lateral compensated carry at `z≈1.03-1.04` |
| Open retreat after false release does not fix placement | A1 plate was only partly on the stove, not merely unsettled | Recenter the plate footprint; do not apply basket-style settle logic to a wrong-surface plate |

## Re-localization per scene

Plate: look for the white ceramic disc with red concentric rings. Segment phrasing fallback: `the white plate with red rings`; manual pixels on the white interior and red rim are reliable. It can be confused with the gray stove ring if using depth only, so classify by RGB first. In this run, plate pixels around (711,493), (733,454), (733,535) back-projected near x 0.03-0.05, y -0.04..0.02, z 0.907; do not cache those absolutes.

Stove cook region: look for the dark gray circular coil/ring on the square metal stove base, not the white plate. Segment phrasing fallback: `the gray stove burner` or `the stove cook region`. Sample pixels on the inner gray disc/rings; reject outer rim/base samples that jump to the stove edge. In this run, accepted cook-region samples were around x -0.09..-0.05, y 0.23..0.28, z 0.900, while an outer sample at y≈0.327 was edge-biased.

Wrist refinement: useful for plate geometry before grasp because the plate fills the wrist view. For the stove, agentview RGB is the semantic authority; wrist is useful only after carrying near the stove to judge overlap between held plate footprint and burner.

## Fragility flags

The fragile step is placing a rim-held plate: the gripper pose is not the plate center. If a direct placement/release fails, do not grind low descents; regrasp only if the plate is upright and close, then compensate farther in the direction that moves the visible plate footprint over the burner.

## Difficulty and reliability

Solved in 2 attempts. Expected single-shot rate is moderate after this offset lesson: the grasp is reliable, but the final placement depends on visually compensating a large held-object offset near the workspace edge. No unsolved subgoal remained; termination fired before release once the held plate covered the stove cook region.

## Cross-refs

[[visual-over-pick-heuristic]]
