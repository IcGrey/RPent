---
id: task-family_libero_object_swap_t0
scope: task-family
suite: libero_object
regime: swap
task_id: 0
task_language: Pick the alphabet soup and place it in the basket
evidence:
  cells:
  - object_swap_t0_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- can-pick-visual-confirmation
- basket-release-retreat-settle
---


## Applicable pattern
Pick a specific grocery can by label/color under object-swap perturbation and place it into a movable woven basket. The task tests semantic disambiguation among look-alike groceries plus basket interior placement from perception rather than cached positions.

## Winning technique
Identify the alphabet soup in `agentview_high.png` as the blue/yellow cylindrical can, not the front red/green tomato sauce can. Use agentview/SAM for semantic identity, move above that anchor, and accept wrist geometry only when it remains within about 3-5 cm of the agentview anchor. Use `pi0_pick` only for grasping, then judge the pick visually: in this run Pi0 reported `success=false`, but the can was visibly held and lifted, so the run continued. Firm with `set_gripper +1`, move into the basket interior at low object-frame z while holding closed, open with `release`, then retreat upward with gripper open so the can can settle fully inside.

## Magic numbers
Object-frame home eef z about 0.26; use object-frame can pre-position z=0.18 (band 0.17-0.20) above a wrist-refined can anchor.
`pi0_pick`: max_chunks=20 (band 18-24), lift_thresh=0.05 (band 0.04-0.06), gripper_closed_thresh=0.06 (but treat as heuristic only).
Can wrist-refinement accept radius: 3-5 cm from the agentview semantic anchor; reject larger jumps as look-alike/background.
Basket descent eef z about 0.15 target, observed stall/settle around 0.17 (band 0.15-0.18) with step_clip=0.01 (band 0.008-0.015).
After release, always retreat upward with gripper=-1 to z about 0.24 (band 0.22-0.26); predicate may fire during retreat/settle.
NEVER let the wrist choose between alphabet soup and tomato sauce semantically; it is only geometry after agentview identity.
NEVER drop at rim height if the can is angled against the basket lip; descend into the visible cavity first.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Pi0 `success=false` although peak lift is high | A1: closure threshold stayed at about 0.0688, above `gripper_closed_thresh`, while the wrist image showed the soup can held | Judge grasp from wrist plus gripper gap, not the boolean alone; continue if target is visibly held, then `set_gripper +1`. |
| Release does not immediately terminate with can at basket mouth | A1: can was still angled/pressed near the front-left lip after low release | Retreat upward with gripper open; in A1 termination fired during settle/retreat. |
| Basket SAM mask returns liner/rim-biased xyz | A1: prompt `the inside of the basket` highlighted the white liner, not a clean geometric cavity center | Use RGB cavity center and low vertical insertion; treat mask as semantic confirmation, not exact place xyz. |

## Re-localization per scene
Alphabet soup: use agentview phrase `the blue and yellow alphabet soup can`; in this scene SAM score was 0.707 and the overlay correctly marked the rear-center blue/yellow can. Confusions: tomato sauce is another cylinder but red/green and closer to the camera; do not pick it. Wrist fallback phrase: `the blue and yellow can`; in this run score was 0.224 after pre-position and was accepted because it stayed near the agentview anchor. Score floor: accept low wrist scores around 0.2 only if the overlay and xy consistency agree.
Basket cavity: agentview phrase `the inside of the basket` confirmed the open white-lined woven basket, but returned a liner/rim-biased site. Use the visible open interior center, then confirm in wrist as the gripper approaches. The absolutes from this run, such as basket y near +0.28 to +0.37 and soup x/y near -0.19/-0.08, are counter-examples only and must not be cached.

## Fragility flags
Most fragile step: interpreting Pi0's false-negative pick. Fallback is visual confirmation: if the exact target can is in the gripper and its original spot is empty, firm grip and continue. If the can is not visible in the gripper, re-pre-position over the agentview-identified target and retry with the full task language.
Second fragile step: basket lip snag. Fallback is low, small-step descent into the cavity and open-gripper upward retreat; if still non-terminal, re-localize the settled can and use a short inward/downward push only after confirming it is partly inside.

## Difficulty and reliability
Solved in 1 attempt. Expected single-shot rate should be good when the alphabet soup is identified from agentview before wrist refinement. Remaining risk is Pi0 grasp variability and angled can/basket rim contact; the run demonstrated that release plus open retreat can resolve one such angled contact.

## Cross-refs
[[can-pick-visual-confirmation]]
[[basket-release-retreat-settle]]
