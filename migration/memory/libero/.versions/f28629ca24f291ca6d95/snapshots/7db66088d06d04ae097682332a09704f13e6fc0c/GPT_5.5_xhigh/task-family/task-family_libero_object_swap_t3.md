---
id: task-family_libero_object_swap_t3
scope: task-family
suite: libero_object
regime: swap
task_id: 3
task_language: Pick the bbq sauce and place it in the basket
evidence:
  cells:
  - object_swap_t3_s0
  attempts: 12
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- held-contact-container-insertion
- rim-perch-contact-seat
---


## Applicable pattern
Grocery-label disambiguation plus basket insertion for a tall bottle whose held offset makes scripted static releases miss the cavity. The task is solved by using agentview for BBQ identity, Pi0 only for the initial grasp, and a trained contact/placement skill while still holding near the basket.

## Winning technique
Identify BBQ sauce in agentview_high as the short brown BBQ-labeled bottle behind the green salad dressing bottle; do not confuse it with the center-right ketchup bottle. Pre-position above that candidate at low-table object-frame height, confirm in wrist, then run grasp-only `pi0_pick` with `pick up the brown BBQ labeled bottle behind the green bottle`. Firm the grip, carry near the basket mouth with `gripper:+1`, and call `pi0_doubled("put the bbq sauce into the basket")` before opening. In the solved run the contact skill moved the still-held bottle into the white-lined basket and `terminated=true` at the contact step.

## Magic numbers
`move_to` pre-position z `0.18` (usable band `0.17-0.20`) over the BBQ bottle; avoid y targets beyond about `-0.34` because A5 hit the negative-y workspace edge.
`pi0_pick max_chunks=12` (usable band `7-12`) with `lift_thresh=0.05` and `gripper_closed_thresh=0.06`; longer generic/default picks risk wrong-object selection or unstable placement behavior.
`set_gripper +1` for `8` steps (band `8-12`) after the pick.
Carry with `gripper:+1`; never omit gripper on `move_pose`/carry moves.
Use `pi0_doubled max_chunks=12` (band `10-14`) from a clean held pre-release pose near the basket, before opening.
NEVER use default/home Pi0 grounding for this swap layout; A6 selected salad dressing.
NEVER assume a gripper-center release at basket center is enough; A1-A3 and A7-A10 repeatedly left the bottle outside the liner.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Correct BBQ grasp, release at eef y≈0.20-0.25 leaves bottle outside/right of basket | A1-A3, A7-A10: held bottle offset projects outside the liner even when gripper approaches the basket | Use trained contact insertion while still holding from a clean pre-release pose |
| Pi0 default/home pick grabs or targets salad dressing instead of BBQ | A6: prompt grounding is unreliable among similar bottles in swap layout | Use agentview semantic ID, pre-position over BBQ at `[-0.15,-0.29,0.18]`, prompt brown BBQ-labeled bottle behind green bottle |
| Body-grasp pre-position at extreme negative y fails or traps the bottle | A5: y≈-0.38 is outside clean workspace; Pi0 contacts but does not produce durable lift | Stay near y≈-0.29 to -0.31 and let Pi0 execute learned grasp path |
| Positive/negative yaw or pitch side-entry still leaves bottle outside basket | A9-A11: orientation changes alone did not put bottle projection past the basket wall | Do not spend more static side scrapes; use `pi0_doubled` held-contact insertion |
| Short scripted pushes after a bad outside drop do not recover | A1, A7: pushes shift basket/object but do not seat the bottle | Reset for a clean trace, or use contact skill before opening while object is still controlled |

## Re-localization per scene
BBQ sauce: use agentview_high RGB label and layout. It is a short brown/orange bottle with readable `BBQ` on the label, behind the green-capped salad dressing bottle and left of the center ketchup bottle in this seed. Segment prompts by brand nouns are fragile; manual pixels on the label/body worked better than relying on free segmentation. Reject any wrist/free-Pi0 identity that jumps to the green-capped dressing or the `Fancy Tomato Ketchup` bottle.
Basket: white fabric-lined woven square container at image-right. Agentview back-projection of the rim/interior is biased by the wall and liner folds; use RGB to classify the cavity, and wrist only to confirm the true white-lined opening. This run's absolute positions are counter-examples only and must not be cached.
Ketchup/salad dressing: both are distractors. Ketchup is the taller center-right bottle with `Fancy Tomato Ketchup`; salad dressing is the front-left green-capped bottle. They are the main wrong-target risks.

## Fragility flags
Most fragile step is the transition from held bottle near the basket to valid `In`: scripted releases and pushes repeatedly missed despite correct target identity. Fallback is `pi0_doubled("put the bbq sauce into the basket", max_chunks=10-14)` from a clean held pre-release pose before opening.
Second fragility is target identity: default Pi0 can choose salad dressing. Always pre-position over the agentview-identified BBQ bottle and verify the wrist/agentview after pick.

## Difficulty and reliability
Converged in 12 archived attempts across agents. The reliable subroutine is the pre-positioned BBQ pick; the unreliable part is scripted placement. Expected single-shot rate should be substantially higher if the run goes directly to held-contact insertion after the pick, but this is still single-seed evidence.

## Cross-refs
[[held-contact-container-insertion]] [[rim-perch-contact-seat]]
