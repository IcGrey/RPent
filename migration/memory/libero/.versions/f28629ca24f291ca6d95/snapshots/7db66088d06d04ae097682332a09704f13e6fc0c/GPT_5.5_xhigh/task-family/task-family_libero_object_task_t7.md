---
id: task-family_libero_object_task_t7
scope: task-family
suite: libero_object
regime: task
task_id: 7
task_language: Pick the butter and place it in the basket
evidence:
  cells:
  - object_task_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- high-drop-over-cavity
---


## Applicable pattern

Single flat grocery-box into the white-lined basket on the low object-frame table. The task is mainly semantic discrimination between butter and nearby cream cheese, followed by a controlled high release over the basket cavity.

## Winning technique

Use `agentview_high.png` as the identity source: choose the red/yellow Farm Fresh Butter box and reject the blue/white cream cheese box. Back-project several pixels on the butter, then move above that anchor and accept wrist refinement only if it still sees the same red/yellow box within a few centimeters. Use `pi0_pick` only for the grasp, confirm by gripper gap plus wrist image, firm with `set_gripper +1`, and carry at z around 0.20 through a midpoint.

For placement, identify the woven basket and aim at the visible white liner/cavity rather than the rim. Release from a high over-cavity pose; in this run a small deeper +y nudge before release put the flat box fully over the liner and termination fired immediately.

## Magic numbers

Low object-frame home eef z about 0.26; butter pre-pose z=0.18 (usable band 0.17-0.19).

`pi0_pick` prompt `pick up the butter`, `max_chunks=20` (observed success at 7 chunks; usable band 16-24), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Confirm hold by gripper opening around 0.039 rather than fully shut, plus wrist image of the butter in the fingers.

Firm grip with `set_gripper +1`, steps=8 (band 5-12).

Carry and release z=0.20 (usable band 0.19-0.21) with `gripper:1`; split long y travel into waypoints under about 0.30 m.

Use slow carry for a flat box: `step_clip=0.010-0.012`, and a final small placement nudge with `step_clip=0.006-0.010`.

Never carry with `gripper:-1`; it opens and drops the object.

Never let wrist re-identify among butter/cream cheese; it only refines the agentview-chosen butter candidate.

## Failure modes

| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| none observed | A1 solved on first release | keep the agentview identity pass and high over-cavity release; likely failures would be butter/cream-cheese confusion or front-rim perch |

## Re-localization per scene

Butter: look for the red/yellow rectangular Farm Fresh Butter box, often near the front of the clutter. It can be confused with cream cheese only by shape; RGB label separates them clearly. SAM prompt `the red and yellow butter box` worked from agentview (score 0.535) and wrist (score 0.887), but use the overlay only after checking it covers the red/yellow box. This run's absolute butter xy around (0.11, -0.20) is a counter-example only and must not be cached.

Cream cheese distractor: blue/white rectangular box with readable Cream Cheese label. Reject it for this task even if it is close to the butter in wrist view.

Basket cavity: woven rectangular basket with white liner. Segment or broad region estimates can bias toward the rim/liner folds; choose the visible open liner center and prefer a slightly deeper point inside the cavity. This run's successful release eef near (-0.035, 0.292, 0.200) is a counter-example only and must not be cached.

## Fragility flags

Most fragile step is placing a flat box over the basket without catching the front rim. If wrist view shows the held box at the near lip, keep z high and nudge deeper into the visible liner before release rather than descending into the rim.

Second fragile step is identity: butter and cream cheese are both small boxes, so read the red/yellow versus blue/white label in agentview before Pi0.

## Difficulty and reliability

Solved in 1 attempt. Expected single-shot rate is high if target identity is fixed from agentview and the placement uses high over-cavity release. No unresolved mechanism remained in this run.

## Cross-refs

[[high-drop-over-cavity]]
