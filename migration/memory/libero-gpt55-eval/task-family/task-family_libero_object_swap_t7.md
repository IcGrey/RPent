---
id: task-family_libero_object_swap_t7
scope: task-family
suite: libero_object
regime: swap
task_id: 7
task_language: Pick the milk and place it in the basket
evidence:
  cells:
  - object_swap_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- pi0-prepositioned-simple-basket
---


## Applicable pattern
Single-object grocery-to-basket task in the low object frame. The main risks are confusing milk with other carton/box groceries and biasing the basket target to a rim instead of the interior.

## Winning technique
Use agentview_high for identity: choose the red Dairy Fresh Milk carton, not the orange juice carton or butter box. Back-project several pixels on the carton to get a stable xy anchor, move the open gripper above that anchor at low-frame pre-position height, verify the same carton in the wrist view, then call `pi0_pick` with the short prompt `pick up the milk`. In this seed, Pi0 completed the carry into the basket and triggered termination without an explicit scripted release.

Success criteria: after pre-positioning, wrist shows the milk directly below the gripper; after `pi0_pick`, agentview/wrist show the milk inside the white-lined basket and `terminated=true`.

## Magic numbers
`move_to` pre-position z=0.18 in the low object frame (usable band 0.17-0.20 for tall cartons).
`move_to` step_clip=0.015 (usable band 0.012-0.020) for precise pre-positioning around groceries.
`pi0_pick` max_chunks=20 (observed success at 18 chunks). For stricter grasp-only behavior, prefer max_chunks=8-12 and script the basket carry yourself.
`lift_thresh=0.05`, `gripper_closed_thresh=0.06` worked with the standard prompt.
Never cache absolute xy from this seed; swap scenes require re-localization.
Never let wrist identity override agentview for grocery labels; use wrist only to confirm the same chosen carton is under the gripper.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| none observed | A1 solved | Keep the pre-position plus short milk prompt; if future Pi0 carries to a wrong site, reduce max_chunks and script the basket drop. |

## Re-localization per scene
Milk: in agentview_high, look for the red upright Dairy Fresh Milk carton with readable white `Milk` text and cow graphic. It can be confused with the red/orange butter box; reject boxes that are flat and say butter, and reject the taller orange juice carton by its orange/yellow front.

Basket cavity: in agentview_high, identify the open woven basket with a white liner. Back-project a region over the visible interior, but expect rim/interior mixing; if scripting placement, move above the basket and use wrist_high to choose the true cavity center before release.

This run's absolute counter-example coordinates were milk xy about [0.078,-0.094] and basket region median xy about [0.088,0.226]. These are evidence only and must not be reused.

## Fragility flags
Most likely break: Pi0 may continue beyond grasp and place according to its learned policy. This was acceptable here because it put the milk into the basket, but if it heads elsewhere, reset with a changed plan using shorter `max_chunks` and script the carry to wrist-confirmed basket center.

Second risk: basket localization from agentview can be rim-biased. Fallback is wrist region confirmation from above the basket cavity.

## Difficulty and reliability
Solved on A1. Expected single-shot rate is moderate for this exact simple milk-to-basket case when the target is semantically verified first; lower if Pi0's end-to-end carry is disallowed by the benchmark harness, in which case use the same perception pass but stop Pi0 earlier and script the release.

## Cross-refs
[[pi0-prepositioned-simple-basket]]
