---
id: task-family_libero_object_swap_t4
scope: task-family
suite: libero_object
regime: swap
task_id: 4
task_language: Pick the ketchup and place it in the basket
evidence:
  cells:
  - object_swap_t4_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Object-frame grocery-to-basket task with a tall-ish sauce bottle target among look-alike condiment bottles. The task tests semantic target identification from agentview, conservative wrist refinement of the same candidate, and basket-cavity placement without over-descending into the low-frame floor.

## Winning technique
Identify ketchup in `agentview_high.png` by label/color as the red/orange tomato ketchup bottle with gray cap; reject the darker BBQ bottle and green salad dressing. Back-project 3 firm pixels on the bottle, move above that anchor at low-object-frame pre-pos height, then accept wrist refinement only if it remains within about 3-5 cm of the agentview anchor.

Use `pi0_pick` only for grasping with prompt `pick up the ketchup`. Treat Pi0 `success:false` as non-fatal when the gripper gap and wrist/agentview show the bottle held. Hold `gripper:+1` during the carry. Place over the woven basket's cloth-lined interior center from an agentview region back-project, release, then retreat straight up/open; the predicate may fire on retreat after the bottle settles.

## Magic numbers
Object frame: initial eef z≈0.26; use pre-pick eef z=0.18 (band 0.17-0.20) for ketchup.

Ketchup wrist refinement accept band: ≤0.05 m from agentview anchor; this run accepted ≈0.01 m.

`pi0_pick`: `max_chunks=20` (band 16-24), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Carry/place into basket: hold `gripper=+1`; `step_clip=0.012` (band 0.010-0.015) for the tall bottle.

Basket cavity target: use region back-project over the open interior/liner, not rim pixels. In this run the absolute center was about `[0.066,0.256]`; do not cache it across seeds.

Release: `release(max_steps=30)` (band 20-40), then open-gripper vertical retreat. Do not force lower when the bottle is already inside and the eef stalls at the low-frame floor.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Pi0 returns `success:false` despite the bottle being held | A1: `descent_done:false` made the heuristic fail although gripper opening ~0.034 and images confirmed the ketchup was grasped | Judge grasp from gripper gap plus wrist/agentview, not the boolean alone |
| Release inside basket does not immediately terminate | A1: bottle remained high/wedged near the open gripper and needed to settle | Retreat straight up with `gripper=-1`; predicate fired during the retreat |
| Basket descent stalls above requested z | A1: low object-frame floor/geometry stopped eef at z≈0.244 while target z was 0.18 | If RGB shows bottle inside the cavity, release and retreat instead of forcing lower |

## Re-localization per scene
Ketchup: prompt/description for perception is `red tomato ketchup bottle with gray cap`, not just `sauce`. It looks like the orange-red bottle with a white/green label reading Tomato Ketchup. Confusable with BBQ sauce (darker brown/orange bottle) and salad dressing (green cap/green label). Agentview identity is mandatory; wrist only refines the already chosen candidate.

Basket: woven rectangular basket with white cloth liner. Use region-mode `back_project` over the visible interior cloth/open cavity. Rim pixels and outside wall pixels are biased; the true placement point is the cavity center.

Absolute coordinates from this run (`ketchup≈[0.171,0.027]`, basket≈[0.066,0.256]`) are counter-examples only and must not be cached.

## Fragility flags
Most fragile step is after release: the object can still appear held or wedged. Fallback is an open-gripper straight-up retreat, not a lateral scrape.

Second fragile step is semantic target choice among condiment bottles. Use the readable label/color in agentview before moving; do not let the wrist choose between ketchup/BBQ/salad dressing.

## Difficulty and reliability
Solved in 1 attempt. Expected single-shot rate is high if target identity is grounded in agentview and the open retreat is included after release. Remaining uncertainty: no failed attempts tested alternate Pi0 prompts or lower placement heights.

## Cross-refs

