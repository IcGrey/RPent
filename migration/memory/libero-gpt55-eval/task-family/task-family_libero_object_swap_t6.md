---
id: task-family_libero_object_swap_t6
scope: task-family
suite: libero_object
regime: swap
task_id: 6
task_language: Pick the butter and place it in the basket
evidence:
  cells:
  - object_swap_t6_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- object-frame-box-to-basket
---


## Applicable pattern
Object-frame grocery placement: identify a flat rectangular butter box among similar grocery distractors, grasp it with Pi0 only, and script the carry into a woven basket cavity.

## Winning technique
Use agentview_high for semantic identity: the butter is the small red/yellow/blue Farm Fresh Butter box, distinct from the nearby chocolate pudding box. Back-project several label/top pixels, then move above the candidate and accept wrist_high refinement only if it stays within the same few-centimeter neighborhood. Use `pi0_pick` with the short prompt `pick up the butter`; once the gripper gap confirms a held box, lock with `set_gripper +1`, lift, carry with `gripper:+1`, aim into the basket liner rather than the woven rim, and release while visually inside the cavity.

## Magic numbers
`pre_pick_z=0.18` in object frame (band 0.17-0.20) above the butter.
`pi0_pick max_chunks=20` (observed success at 8 chunks; usable band 8-20) with `lift_thresh=0.05` and `gripper_closed_thresh=0.06`.
`set_gripper +1 steps=8` (band 5-10) after the grasp.
`carry_z=0.22` (band 0.20-0.24) with `step_clip=0.012` for the held butter box.
Basket drop can terminate from eef z about 0.15 when visually inside the liner; do not require reaching the requested 0.105 if OSC stalls but the object is already over the cavity.
NEVER carry with `gripper:-1`; it opens the gripper and drops the box.
NEVER use basket rim pixels as the placement point; choose the white liner interior.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| none observed | A1 solved | Keep the short butter prompt, wrist-confirmed target identity, and basket interior release. |

## Re-localization per scene
Butter: identify by the red/yellow/blue Farm Fresh Butter label and flat box shape. Confused with chocolate pudding because both are rectangular boxes; reject if the label reads Chocolate Pudding or if wrist refinement jumps away from the agentview-identified butter.
Basket: identify by the white cloth liner and woven walls. Use a region over the open liner/cavity; rim and sidewall depth are biased and should not be cached as the center.
This run's absolute coordinates are counter-examples only and must not be reused: butter was near `(0.05,-0.089)` and basket interior was around positive y `(roughly -0.06,0.245)` in seed 0.

## Fragility flags
Most likely breakage is semantic confusion between butter and another grocery box in the wrist view. Agentview must choose the target first; wrist only refines geometry for that same candidate. If release misses, re-localize the basket liner center after any bump because the basket can move.

## Difficulty and reliability
Solved in 1 attempt on seed 0. Expected single-shot reliability is good when the butter label is visible and the basket interior is used; untested on occluded label layouts.

## Cross-refs
[[object-frame-box-to-basket]]
