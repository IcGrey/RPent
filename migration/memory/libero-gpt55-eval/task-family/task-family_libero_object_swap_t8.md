---
id: task-family_libero_object_swap_t8
scope: task-family
suite: libero_object
regime: swap
task_id: 8
task_language: Pick the chocolate pudding and place it in the basket
evidence:
  cells:
  - object_swap_t8_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- flat-box-basket-interior-drop
---


## Applicable pattern
Flat grocery box into a woven basket under object-swap perturbation. The hard part is not the pick; it is choosing a basket-interior drop point that lets a long, flat box fall inside instead of perching on the liner or being pushed out over a rim.

## Winning technique
Identify the chocolate pudding semantically in `agentview_high.png` as the flat brown box with the readable label, then back-project several label/top pixels for the anchor. Move over that anchor at low-object-frame z around 0.18 and use `pi0_pick("pick up the chocolate pudding", max_chunks=20, lift_thresh=0.05, gripper_closed_thresh=0.06)`. Accept the grasp only when gripper opening is about 0.046 and wrist view shows the pudding label raised in the fingers.

After `set_gripper +1` for 8 steps, carry through a central high waypoint around z=0.20, then move over a basket point biased toward the visual interior/back rather than the front rim. In the solved attempt, the successful drop target was shifted from the first attempt's rim-biased x≈0.065,y≈0.245 to x≈0.035,y≈0.225 before descending. Descend slowly with `gripper:+1`, `step_clip=0.006`, and enough steps to reach the basket floor limit; OSC may stall around eef z≈0.14, but release there can still satisfy `In` if the box is centered inside the liner. Open with `release(max_steps=40)` and rely on the official termination signal.

## Magic numbers
`pi0_pick max_chunks=20` (band 16-24); successful picks used 8 chunks.
`lift_thresh=0.05` (band 0.05-0.08) and `gripper_closed_thresh=0.06`; held pudding gave final opening ≈0.0466.
`set_gripper +1 steps=8` (band 5-12) after pick.
Carry z `0.20` in low object frame (band 0.18-0.22).
Basket approach target should be visually interior/back: solved around x≈0.035,y≈0.225 for this scene; do not cache these absolutes.
Descent `step_clip=0.006` (band 0.005-0.008), `max_steps=180` (band 150-220).
Release `max_steps=40` (band 30-50).
Never carry with omitted gripper or `gripper:-1`; it opens and drops the box.
Never use post-release pushes toward the basket front wall for this flat box; A1 ejected it.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Pudding visibly at basket mouth but `terminated=false` after release | A1 used a rim/front-biased basket target around x≈0.065,y≈0.245; the flat box perched on the liner rather than entering the predicate volume | Shift the held-box release toward the visual interior/back of the basket and descend slowly before release |
| Open-gripper nudges make the box leave the basket | A1 pushed laterally after release toward x≈0.02,y≈0.27 and levered the box out over the front wall | Prefer solving placement before opening; if nudging is needed, avoid front-wall directions and keep the box inside the liner |

## Re-localization per scene
Chocolate pudding: in `agentview_high.png`, look for the flat brown rectangular box with large `CHOCOLATE PUDDING` label. It may be confused with other box/carton groceries only if the label is ignored; the readable brown label disambiguates it from the orange juice carton. Manual pixel back-projection on the top/label worked; SAM was not needed.

Basket: look for the woven rectangular basket with a white cloth liner and open cavity. Agentview region or mask medians can be rim/liner-biased; sample the visible opening and then refine by wrist/visual confirmation during carry. The useful target is not the rim centroid but the interior point where the long box can clear both front and side walls. This run's absolute xyz values are counter-examples only and must not be cached across scenes.

Reject rule: if a basket point puts the held box visually over the front wall or liner lip, reject it and shift toward the interior/back before descending. If a wrist estimate jumps to another grocery item, reject it; wrist is geometry-only after agentview chooses identity.

## Fragility flags
The fragile step is the final basket descent/release. OSC may stall above the requested z because the box and rim collide, but success is still possible if the object is centered in the liner. If release does not terminate and the box remains inside, a very small seating adjustment may be reasonable; if the box is perched on the front wall, reset rather than recording a messy push recipe.

## Difficulty and reliability
Solved in 2 attempts. Expected single-shot rate is moderate once the basket release is interior-biased, because the Pi0 pudding grasp was repeatable and completed in 8 chunks both times. The only observed failure was placement geometry, not target identity or grasping.

## Cross-refs
[[flat-box-basket-interior-drop]]
