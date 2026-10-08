---
id: task-family_libero_goal_swap_t6
scope: task-family
suite: libero_goal
regime: swap
task_id: 6
task_language: Put the cream cheese on the bowl
evidence:
  cells:
  - goal_swap_t6_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- flat-box-rigid-bowl-seat
---


## Applicable pattern
Move a flat rectangular grocery box into a rigid bowl in a cluttered kitchen-frame scene. The main risks are box edge/back-projection bias and collision with the nearby wine bottle during the carry.

## Winning technique
Use agentview for identity: the cream cheese is the blue rectangular box with readable label, and the destination is the black/white patterned bowl. Move above the box and use wrist geometry to refine the footprint, then run one grasp-only Pi0 prompt. Carry with `gripper:+1` through a high waypoint that clears the wine bottle, refine/confirm the bowl interior from the wrist view, center the box over the bowl mouth, descend until the lower part of the held box is visibly inside the rim, and release.

## Magic numbers
Kitchen frame: home eef z about 1.17; table z about 0.90.
Cream-cheese pre-grasp: eef z=1.12 (band 1.10-1.13).
Pi0 grasp: prompt "pick up the cream cheese", `max_chunks=12` (band 10-14), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.
Carry: keep `gripper:+1`; use `step_clip=0.012-0.015` around nearby tall objects.
Placement: bowl-center eef target from wrist, release after descending to eef z about 1.015 (band 1.01-1.04).
NEVER omit gripper while carrying; `move_pose`/`move_to` default-open mistakes drop the box.
NEVER trust a single agentview pixel on the cream-cheese edge; it can back-project to table height beside the box.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| none observed | A1 solved | Keep the grasp prompt short, carry closed, and seat the box below the bowl rim before release. |

## Re-localization per scene
Cream cheese: agentview RGB shows a small blue rectangular package with "Cream Cheese" label; use it as the semantic authority. If top/edge pixels return table z, move above the same candidate and wrist-sample the visible rectangular face/edges, accepting only points within a few cm of the agentview candidate.
Bowl: black/white patterned round bowl with a yellowish rim, not the nearby white/red plate or stove burner. Agentview identifies the destination; wrist samples on the visible patterned interior and rim estimate center. Use the interior midpoint, not a rim-only mask median.
Counter-example absolutes from this seed only: cream cheese wrist footprint near [-0.386,0.214], bowl center near [-0.206,-0.032]. Do not cache these.

## Fragility flags
The most fragile step is the carry path: the wine bottle sits between the source and bowl. Use at least one safe high waypoint and small `step_clip`; if the box drifts, stop over the table, re-check wrist/agentview, and only continue while the gripper gap shows a held object.

## Difficulty and reliability
Converged in 1 attempt for seed 0. Expected single-shot rate is good when the wrist refinement confirms the box footprint and the release is made after low seating inside the bowl. No unresolved substep remained.

## Cross-refs
[[flat-box-rigid-bowl-seat]]
