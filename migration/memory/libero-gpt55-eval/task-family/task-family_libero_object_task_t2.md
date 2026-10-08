---
id: task-family_libero_object_task_t2
scope: task-family
suite: libero_object
regime: task
task_id: 2
task_language: Pick the tomato sauce and place it in the basket
evidence:
  cells:
  - object_task_t2_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- brand-label-over-segmentation
- rim-perch-contact-seat
---


## Applicable pattern
Grocery-label can into a soft/rimmed basket. The task tests semantic disambiguation between similar red/orange grocery packages and physical seating of a cylindrical can into a flexible basket cavity.

## Winning technique
Identify the tomato sauce in agentview_high by the red/green cylindrical can label, then use wrist only to refine that same candidate. Use Pi0 for the grasp, but judge it visually: in the solved run Pi0 returned success=false while the tomato can was plainly held. Firm the grip, carry/accept Pi0's carry over the basket if it happens, then lower toward the basket interior/back half with gripper closed. If release leaves the can perched on the rim, re-close and use a short `pi0_doubled` contact prompt, `push the tomato sauce can into the basket`, to seat it.

## Magic numbers
`pi0_pick max_chunks=20` (band 18-22), `lift_thresh=0.05` (band 0.04-0.06), `gripper_closed_thresh=0.06` (band 0.055-0.065). Treat `success=false` as non-authoritative; visual held-object evidence wins.

`set_gripper +1 steps=8` (band 5-10) after the pick before any scripted carry/lowering.

Low-table pre-position/carry above can: eef z around 0.20 (band 0.19-0.22). Can top back-projects around z=0.06-0.08 on this frame.

Controlled basket descent: `step_clip=0.004-0.006`, target z about 0.155-0.17, but expect OSC/contact to stall near eef z≈0.195 when the can/rim contacts.

`pi0_doubled max_chunks=12` (band 10-14) from the rim-perched state was enough; stop when termination fires.

NEVER release a cylindrical can high over the basket from eef z≈0.21 unless the can is fully over the cavity; A1 bounced it out.

NEVER assume basket region medians are the cavity center; the white liner/rim and table pixels bias the estimate.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Correct can bounces out after release | A1 released a cylindrical can high at eef z≈0.21 near the front/right basket lip | Bias placement deeper/backer and avoid high drop for cans |
| Lower release still leaves can perched | A1 and A2 scripted lowering/pushing contacted the rim/can but did not create the final seating motion | From the perched state run capped `pi0_doubled` with an explicit push-into-basket prompt |
| Pi0 reports pick failure although object is held | A2 gripper threshold did not classify the grasp as success, but wrist/agentview showed the tomato can in the fingers | Use image + gripper state as the grasp judge, not the Pi0 success flag |

## Re-localization per scene
Tomato sauce: in agentview_high, choose the red/green cylindrical can with tomato graphics. It can be confused with the orange ketchup bottle by the word tomato and with the blue/yellow alphabet soup can by shape. Prefer manual pixels on the metal lid/upper colored band; reject lower side pixels that back-project to table z. Wrist refinement is accepted only if it stays within about 3-5 cm of the agentview identity anchor.

Basket: visually identify the white-lined woven square container. Use agentview for identity and wrist for geometry when close. The true useful target is the open liner/cavity, not the woven rim or outside wall. In this solved run, absolute basket/can coordinates are counter-examples only and must not be cached.

## Fragility flags
Most fragile step is post-release seating. If the can is perched and not terminated, do not grind many long scripted pushes; re-close, make at most a short controlled inward/downward contact, then use `pi0_doubled` with a direct seating prompt.

Second fragility is Pi0 over-executing the pick into a partial place. If it carries the correct can over the basket, salvage by firming the grip and lowering/releasing; do not reset just because the pick skill moved farther than expected.

## Difficulty and reliability
Solved on attempt 2 after one failed high-release/perch episode. Expected single-shot reliability is moderate if the contact-skill fallback is used immediately after a rim perch; lower if relying only on scripted OSC pushes. Remaining uncertainty: whether a pure low release can terminate without `pi0_doubled` from other seeds was not established.

## Cross-refs
[[brand-label-over-segmentation]]
[[rim-perch-contact-seat]]
