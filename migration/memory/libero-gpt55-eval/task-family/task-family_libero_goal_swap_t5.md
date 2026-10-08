---
id: task-family_libero_goal_swap_t5
scope: task-family
suite: libero_goal
regime: swap
task_id: 5
task_language: Push the plate to the front of the stove
evidence:
  cells:
  - goal_swap_t5_s0
  attempts: 74
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- knob-side-front-zone
---


## Applicable pattern
This task tests whether the agent can visually localize a swapped stove fixture and discover the semantic front-of-stove region. The visible burner/platform edge is a strong decoy: many placements there look plausible but do not satisfy the predicate.

## Winning technique
Use agentview_high for identity: target is the white plate with red rings; destination is the gray stove base/burner with the black knob/handle. Back-project several plate pixels and use the median as the plate anchor; in this seed, pixel [520,505] was a representative counter-example anchor and must not be cached.

Pre-position above the plate at about 12-14 cm over table height, with gripper open and yaw near 0. Use `pi0_pick("pick up the red plate")` as a short grasp-only rim/contact skill. Accept a grasp when the final gripper opening is about 0.017-0.025 and the wrist image shows the red-rim plate held at the fingers.

After grasp, do not release on the burner/cooktop edge. Carry high with `move_pose` and gripper held closed to the knob-side/+y front region beside the stove, offset toward the black knob/handle rather than the lower metal platform edge. In the winning run the requested target was approximately `x=-0.07,y=0.23,z=1.02`, and termination fired during the carry when the eef reached about `y=0.19`; these absolutes are counter-examples only, not reusable coordinates.

## Magic numbers
`pi0_pick` max_chunks=14 (band 12-16), lift_thresh=0.025 (band 0.02-0.035), gripper_closed_thresh=0.06.
`move_pose` carry to front zone: z=1.02 (band 1.00-1.04), step_clip=0.01 (band 0.008-0.012), pitch=0, yaw=0, gripper=+1.
Never omit `gripper: 1` in `move_pose` while holding the plate.
Never treat the visible burner/cooktop disk as the target surface for this language; it was repeatedly nonterminal.
Never grind low pushes into the stove base lip after the plate goes partly under the platform.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Plate moved under/against burner platform but predicate stayed false | A57, A60, A62, A65, A71, A73 aimed at the visible stove base/burner perimeter | Aim for the knob-side/+y front region, not under the platform edge |
| Robot-front/negative-y push moved the plate away from the stove and stayed false | A58 and A72 tested negative-y/cabinet-side front interpretations | Do not use negative-y as front for this swapped stove; it is a decoy interpretation |
| Short bowl clearance left clutter; long clearance shoved bowl onto stove | A57-A59 | Skip clearance if using the high rim-hold carry; the winning run did not need obstacle relocation |
| Learned contact from full-task prompt dragged toward the same under-platform wall | A69 and A73 | Use Pi0 only for the plate rim grasp, then script the high carry to the knob-side zone |
| Held placements over cooktop, table-adjacent front band, left/right front edges all nonterminal | A67-A71 | Change the destination semantics; the hidden accepted region is farther toward the black knob/handle side |

## Re-localization per scene
Plate: prompt/visual phrase `red-rim white plate` or `white plate with red rings`; confused with the gray burner only in depth, not RGB. Reject any candidate without red rings.
Stove: visual phrase `gray burner on metal square base with black knob/handle`; distinguish from the red-rim plate by gray coil rings and metal base. The winning front zone is semantically tied to the black knob/handle side, so first classify the knob/handle in RGB, then aim beside that side.
Bowl, wine bottle, cream cheese: distractors around the plate. Do not let wrist identity choose among them; wrist only confirms the already selected plate geometry.
Do not cache this run's absolute xyz. Use them only as counter-examples showing which bands failed and which semantic side won.

## Fragility flags
The fragile step is the destination interpretation. If a release/carry over the burner edge is nonterminal, reclassify the black knob/handle side as the likely front before changing grasp mechanics.
The second fragile step is the Pi0 plate grasp. If final gripper opening collapses near zero, treat it as contact/air and reset or retry; the winning carry needs a rim hold around 0.017-0.025 opening.

## Difficulty and reliability
This took 74 archived attempts to converge because the visually obvious stove edge and cooktop are decoys. With the knob-side/+y front interpretation and the reliable short plate rim grasp, expected single-shot reliability should be moderate, but only one solved seed is confirmed.

## Cross-refs
[[knob-side-front-zone]]
