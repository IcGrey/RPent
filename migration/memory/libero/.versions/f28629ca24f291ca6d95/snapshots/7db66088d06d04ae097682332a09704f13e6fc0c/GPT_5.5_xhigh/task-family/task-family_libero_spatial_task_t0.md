---
id: task-family_libero_spatial_task_t0
scope: task-family
suite: libero_spatial
regime: task
task_id: 0
task_language: Pick the akita black bowl not between the plate and the ramekin and
  place it on the plate
evidence:
  cells:
  - spatial_task_t0_s0
  attempts: 8
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- rim-perch-contact-seat
---


## Applicable pattern
Duplicate bowl disambiguation plus hard rimmed-surface placement. The target is the patterned black bowl that does not lie between the red-rim plate and gray ramekin; final success requires the bowl to be seated on the plate, not merely visually overlapping a rim.

## Winning technique
Use agentview high-resolution RGB for identity: the lower/front duplicate is between the plate and ramekin, so pick the upper/right duplicate. Use wrist only to confirm geometry near the y workspace edge.

The successful run did not win with a clean scripted carry. It first disturbed and lifted the target with repeated Pi0 picks, staging it near the plate, then a third Pi0 recovery prompt `pick up the raised black bowl` physically moved/seated the raised target onto the red-rim plate and triggered termination. Sequence: move near the target at z around 1.06, accept that y may stall around 0.25; call `pi0_pick` with `grasp the upper right black bowl by the rim`; if it moves but does not hold, reissue `pi0_pick` with `pick up the black bowl`; close briefly with `set_gripper +1`; then call `pi0_pick` with `pick up the raised black bowl` while the target is staged near the plate. Stop immediately when `terminated:true` appears.

## Magic numbers
`pre_pos_z=1.055-1.06` in kitchen frame for this bowl cluster.
`move_to step_clip=0.010` for the initial approach; expect y workspace stall near y=0.25 when commanding the upper/right bowl.
`pi0_pick max_chunks=10` for the first rim prompt; treat it as a staging attempt if it disturbs but does not secure.
`pi0_pick max_chunks=14` for the simple recovery prompt after the bowl is disturbed.
`set_gripper +1 steps=10` can hold/shape the staged contact state, but a nearly shut gripper is not proof of a stable carry.
`pi0_pick max_chunks=18` with `pick up the raised black bowl` succeeded from the staged state.
NEVER infer that visible rim overlap is enough; release can remain false even when the bowl appears partly on the red-rim plate.
NEVER repeat offset-only placement after it has failed; the held-bowl centroid is side-biased and changes by grasp.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Bowl visibly overlaps plate but release false | A1 placed rim/front-biased with simple remembered +y offset | Re-localize plate and avoid relying on a fixed bowl offset. |
| Plate-centered EEF targets still drop bowl beside plate | A2 ignored large held-object offset from Pi0 rim grasp | Measure or change the contact class. |
| Large compensation drags bowl beside plate | A3 had tight side/edge pinch, making low contact compensation unstable | Avoid low closed-gripper dragging under a tight pinch. |
| Suspended release drops off lower/right edge | A4 used high release but still had tight side/rim pinch | Change grasp or recovery class, not just drop height. |
| Wider rim grasp still misses | A5 showed stable gripper gap alone does not solve placement | Do not assume grasp quality fixes footprint offset. |
| Numeric held-mask correction leaves rim perch | A6 measured visible held-bowl mask, but mask centroid was not contact footprint | Treat mask correction as approximate; use contact/re-pick recovery. |
| Manual open-gripper side push clears target away | A7 pushed from the wrong exposed edge or too aggressively | Prefer Pi0 recovery/contact behavior from a staged raised bowl over manual sweep. |

## Re-localization per scene
Target bowl: agentview prompt/description `upper right black patterned bowl`; visually patterned black/white bowl with yellow rim, not the duplicate between the plate and ramekin. Reject any wrist-only re-identification that jumps to the lower/front duplicate.
Plate: `red rim white plate`; white ceramic disc with red rings. Do not confuse with stove burner in kitchen scenes. Back-project several pixels on the white interior and rim; this run saw plate surface around z=0.907.
Ramekin: gray/silver cup-like dish beside the duplicate bowls; use it only as a relation landmark to identify which bowl is between plate and ramekin.
This run's absolute coordinates are counter-examples only and must not be cached; object positions must be re-derived from the current seed's images.

## Fragility flags
The fragile step is final seating on the plate. If the first grasp is unstable but moves the correct target near the plate, this can be useful rather than unrecoverable: re-pick the raised/staged target with a direct prompt. If Pi0 instead grabs the wrong duplicate or tips the lower/front bowl into the plate relation, reset and change the semantic pre-positioning.

## Difficulty and reliability
Solved on attempt 8 after seven placement failures. Expected single-shot reliability is low until the staged re-pick behavior is better characterized; this should be treated as a recovery recipe, not a clean primary placement method.

## Cross-refs
[[rim-perch-contact-seat]]
