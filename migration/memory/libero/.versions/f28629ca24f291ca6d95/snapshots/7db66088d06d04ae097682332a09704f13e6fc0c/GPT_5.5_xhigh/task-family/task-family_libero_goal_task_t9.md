---
id: task-family_libero_goal_task_t9
scope: task-family
suite: libero_goal
regime: task
task_id: 9
task_language: Put the cream cheese on the rack
evidence:
  cells:
  - goal_task_t9_s0
  attempts: 15
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- learned-contact-after-near-placement
---


## Applicable pattern
A flat cream-cheese box must be placed on the slatted wooden rack in the kitchen frame. The grasp is easy; the task tests recognizing the rack's true support region and using learned held contact to cross an OSC placement wall.

## Winning technique
Identify the cream-cheese box in agentview_high as the small blue rectangular package and confirm with wrist from overhead. Identify the destination as the tan slatted wooden rack beside the cabinet, but target its upper/top slat region rather than the lower red board, cabinet handle side, or stove look-alike. Use the standard Pi0 grasp from an unrotated overhead pose, then firm the gripper. Carry high near the rack's upper ridge. Before opening, call `pi0_doubled("put the cream cheese on the top of the wooden rack", max_chunks=12)` while holding; it can move the held box from a reachable staging pose onto the slat surface. Release only after the wrist/agentview show the box over the wooden rack surface; in this solved run release fired termination after 8 steps.

## Magic numbers
`move_to` over box: z=1.12 (band 1.10-1.13), gripper -1, step_clip 0.02.
`pi0_pick("pick up the cream cheese")`: max_chunks=20 (band 18-22), lift_thresh=0.05, gripper_closed_thresh=0.06.
Firm grip: `set_gripper(+1, steps=10)` (band 8-12).
High rack staging: z=1.28 (band 1.26-1.30), near the upper rack ridge; keep gripper +1.
Held top-rack contact: `pi0_doubled("put the cream cheese on the top of the wooden rack", max_chunks=12)` (band 10-14).
Release: max_steps=100; solved after 8 release steps.
Never target the stove/ringed metal surface; it is a flat look-alike and not the rack.
Never use unusual pre-pick yaw 1.57 with Pi0 here; A7 closed nearly empty.
Never continue free Pi0 near the wine bottle after dropping the box; A6 repicked the bottle.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Box held correctly but release beside/front of rack does not terminate | A1, A2, A4, A10: scripted top/front drops did not put the box on the official rack support | Use held learned contact targeting the top of the wooden rack before release |
| Full task or generic rack contact biases toward cabinet/handle or stove/table area | A3, A11: prompt lacked the top-rack support cue and confused adjacent flat/fixture surfaces | Prompt `put the cream cheese on the top of the wooden rack`; verify wrist sees slats under the box |
| Lower board/rail targets stall shallow or release false | A5, A11: lower red/brown board is not the valid support under tested poses | Treat lower board as a visual landmark, not the primary placement target |
| Positive-x sweep or passive backstop leaves the box short of support | A9, A12: standard held offset does not protrude far enough with scripted sweep | Let Pi0 contact move the held object onto the rack surface |
| Inclined-face lean reaches deep but release still false | A13, A14: high vertical lean/downslide places near a side/edge, not on top support | Use the `top of the wooden rack` prompt from high staging instead of `lean` |
| Pre-yawed Pi0 grasp misses | A7: unusual yaw broke the trained cream-cheese grasp | Keep Pi0 grasp from an unrotated overhead pose |
| Scripted pinch misses flat box | A8: closing at z about 1.01 collapsed around/above the box | Use Pi0 for acquisition |

## Re-localization per scene
Cream cheese: blue rectangular `Cream Cheese` box near the bowl/stove. Agentview_high can read the label; wrist overhead confirms the same candidate. Back-project firm pixels on the top/label face, but do not cache this run's absolute xy.
Rack: tan slatted inclined wooden fixture beside the dark cabinet, with red/brown end-cap boards and gray side rails. Segment phrase fallback: `the wooden rack`, `the tan slatted wooden rack`, or use manual pixels. The valid target in this run was reached by emphasizing the top of the rack, not the lower red board. Back-project top/end-cap/ridge pixels as support landmarks; sample examples in this run included upper ridge pixels around rows 189-246 and cols 116-180, but these absolutes are counter-examples only.
Confusers: stove burner/metal disc and cabinet handles are nearby surfaces; reject any plan whose wrist view shows the box over the metal burner/white stove top instead of tan slats.

## Fragility flags
Most fragile step: the held contact prompt. If `pi0_doubled("put the cream cheese on the top of the wooden rack")` does not move the box over visible tan slats within 10-14 chunks, do not release blindly. Re-stage high near the upper ridge and retry with the same top-rack semantics, or reset if the box has dropped near the wine bottle.

## Difficulty and reliability
Solved after 15 total attempts, including extensive failed exploration of lower-board, side-face, sweep, and lean strategies. Expected single-shot reliability is moderate only if the top-rack support hypothesis is used; standard grasp is reliable, but the contact move is policy-dependent.

## Cross-refs
[[learned-contact-after-near-placement]]
