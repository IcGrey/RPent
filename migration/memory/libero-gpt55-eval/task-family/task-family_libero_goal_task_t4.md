---
id: task-family_libero_goal_task_t4
scope: task-family
suite: libero_goal
regime: task
task_id: 4
task_language: Put the plate on the top of the drawer
evidence:
  cells:
  - goal_task_t4_s0
  attempts: 13
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- leaned-contact-before-policy-push
---


## Applicable pattern
This task tests placing a flat plate onto a raised cabinet/drawer top where direct airborne placement is blocked by the held plate offset and the drawer-front geometry.

## Winning technique
Identify the red-ring white ceramic plate in agentview and the destination as the dark horizontal top of the drawer/cabinet, not the stove burner. Use the home/no-preposition Pi0 grasp with the full task prompt to get the reliable upright rim hold. Firm the gripper, then do not try to release from an airborne over-top pose. Instead, move the held plate low into the drawer-front/top boundary so it is leaned in contact, then run `pi0_doubled("push the plate onto the top of the drawer")`. In the solved run, the contact skill terminated in 7 chunks without a separate release.

Success criteria: gripper opening after pick about 0.010-0.015 m and wrist/agentview show the plate upright in the fingers; after the low staging move, the plate visibly contacts the cabinet/front boundary; `pi0_doubled` reports official termination.

## Magic numbers
`pi0_pick` prompt: `Put the plate on the top of the drawer`, `max_chunks=20` (band 16-24), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

`set_gripper +1`: 8 steps (band 6-10) immediately after the pick.

Low contact staging: target near `[x≈0.055, y≈-0.07, z≈1.04]`, `target_yaw≈0.6`, `step_clip=0.004` (band 0.003-0.006), `max_steps=150` (band 130-170), keep `gripper:+1`.

`pi0_doubled` prompt: `push the plate onto the top of the drawer`, `max_chunks=24` (band 20-28).

Never release early at `y≈-0.07,z≈1.11-1.15`: A11/A12 dropped the plate back to the table.

Never rely on high inward lift above `z>1.16` with the upright hold: A10 slipped/dropped the plate.

Never yaw before the Pi0 grasp: A2/A7 made acquisition unreliable.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Plate held upright but release leaves it wedged/off the drawer front | A1: direct top alignment ignored the held-plate offset | Use contact staging and learned push, not center-to-top release |
| Pi0 cannot acquire the plate after yawed pre-position | A2/A7: yaw-before-grasp breaks the trained plate grasp | Start Pi0 from home/default orientation with full task prompt |
| Post-grasp yaw plus long carry drops or destabilizes the plate | A3/A10: large yaw/high lift changes offset and slip risk | Use only moderate yaw around 0.6 for the low contact staging |
| Aggressive xy offsets still leave the plate hanging below/front-left of top | A4/A12: upright plate cannot get enough center over top before release | Press/lean the plate into the front/top boundary and let contact skill push |
| Learned contact from a poor staging pose leaves plate on table | A5: contact skill started too far from useful drawer contact | Stage low with visible plate-to-cabinet contact before `pi0_doubled` |
| Direct scripted table-height clamp/drag stalls | A9: vertical gripper rim drag gives no usable translation | Use Pi0 rim hold first, then contact skill |

## Re-localization per scene
Plate: visually identify the white ceramic disc with red concentric rings in `agentview_high.png`. Avoid confusing it with the gray stove burner; RGB semantics matter because both are circular flat surfaces. Back-project several pixels on the plate face, not on the rim; in this seed one example was pixel (735,470) -> `[0.0508,-0.0311,0.9072]`, but these absolutes must not be cached.

Drawer top: identify the dark horizontal top surface of the cabinet/drawer on image-left/robot-right. Do not use the vertical front face or handle pixels as the target. Prior top samples were around z≈1.126 and y≈-0.26; front/edge samples gave lower z and were rejected. These are counter-examples only, not reusable coordinates.

Wrist: use it mainly to confirm the held plate and contact state. It is not needed to semantically classify the destination.

## Fragility flags
Most fragile step: acquiring the correct upright rim hold. If the gripper is fully closed or the wrist does not show the plate in the fingers, reset or re-pick from home with the full task prompt rather than continuing.

Second fragile step: contact staging. If the plate is not visibly touching/leaning at the cabinet boundary after the low move, do not call the contact skill yet; nudge lower/closer with `gripper:+1` and small clips.

## Difficulty and reliability
Solved on attempt 13 after many airborne-placement failures. Expected single-shot rate is moderate if the home Pi0 grasp succeeds and the contact staging pose is reproduced; direct scripted release is low reliability for this task.

## Cross-refs
[[leaned-contact-before-policy-push]]
