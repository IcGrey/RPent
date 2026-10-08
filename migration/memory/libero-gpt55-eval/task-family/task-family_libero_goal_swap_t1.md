---
id: task-family_libero_goal_swap_t1
scope: task-family
suite: libero_goal
regime: swap
task_id: 1
task_language: Put the bowl on the stove
evidence:
  cells:
  - goal_swap_t1_s0
  attempts: 4
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- learned-contact-after-near-placement
- visual-over-pick-heuristic
---


## Applicable pattern

Move a patterned bowl onto a visually similar gray stove cook region in a swapped kitchen layout where the stove fixture is near the workspace edge and the bowl starts beside clutter.

## Winning technique

Use agentview RGB as the semantic authority: the target is the patterned gray bowl beside the wine bottle, and the destination is the gray ringed cook region on the metal stove base, not the red-ring plate. Back-project several pixels on the bowl and stove only to plan the local approach; do not cache absolute xyz across scenes.

For this seed, Pi0 grasped reliably only from the default home pose with a short prompt. After the home-start pick, visually confirm the bowl is lifted, firm the grip, then keep `gripper:1` throughout the carry. Drive the held bowl to a compensated stove-side pose, lower until the bowl is visibly supported near the cook region, release, then use one local `pi0_doubled("put the bowl on the stove")` contact call if the release is close but non-terminal.

## Magic Numbers

`pi0_pick` prompt `pick up the bowl`, `max_chunks=20` (band 18-22), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Firm grip with `set_gripper +1` for 10 steps (band 8-12) after visual lift.

Kitchen-frame held carry/placement used z around `0.97` then low support around actual eef z `0.95-0.96` (commanded `0.94` may stop higher). Keep `gripper:1` on every held `move_to`.

Use slow placement moves with `step_clip=0.006-0.008` near the stove edge. Large negative-y targets may stall at actual y around `-0.04..-0.06`; compensate primarily through x and held-object footprint, then finish with learned contact.

`pi0_doubled` final recovery prompt `put the bowl on the stove`, `max_chunks=30` (band 24-32); success occurred at 17 chunks from a visibly near/on-edge bowl state.

Never pre-position over the bowl/stove boundary before Pi0 on this layout; A1/A2 produced false-success air/contact grasps.

Never release when the held bowl is merely beside the stove and still high; release only after a low held contact/support pose, then use learned contact if needed.

## Failure Modes

| symptom | root cause (A<N>) | fix |
|---|---|---|
| Pi0 reports pick success but bowl remains on the table and gripper nearly fully closes | A1 center/above pre-position near the stove/fixture side biased Pi0 into contact/air | Use Pi0 from home for this scene; judge by images, not the success flag alone |
| Open-side/rim-offset pre-position still reports success with no lifted bowl | A2 offset pose remained dominated by stove-side clutter and wrist could not refine the bowl | Remove pre-positioning entirely; do not keep tuning offsets at the bowl/stove boundary |
| Scripted carry stalls before the requested negative-y stove target | A3 workspace/fixture geometry limited actual eef y near `-0.06` under this held pose | Use x-negative compensated held placement and low support, then learned contact, rather than forcing y |
| Release leaves upright bowl close to stove but predicate false | A3/A4 release was near the cook region but not centered enough for `On` | Call `pi0_doubled("put the bowl on the stove")` from the near state; in A4 it terminated |
| Open-gripper manual pushes barely move the upright bowl | A3 gripper contact was too high/poorly positioned after release | Prefer learned contact from a near-state instead of long manual nudges |

## Re-localization Per Scene

Bowl: look for the gray/white patterned bowl with a yellowish rim. Segment phrasing fallback: `the gray patterned bowl`; manual agentview pixels on the interior pattern and rim were more reliable than wrist refinement because the close wrist view was often occluded by the stove knob/fixture. It can be confused with the plate only by depth, not RGB.

Stove cook region: look for the gray circular coil/ring on a square metal stove base. Segment phrasing fallback: `the gray stove burner` or `the stove cook region`. Reject samples on the metal base edge or wooden rack that jump outside the reachable cook-region band; classify the red-ring plate as a distractor before using any flat-disc depth samples.

Wine bottle: only a clutter landmark; it sits between the bowl and plate and can block line-of-sight. Do not let Pi0 target it from the task prompt.

This run's absolute coordinates are counterexamples only: bowl samples were around x≈0.02, y≈-0.224, top/rim z≈0.96; stove visible samples included x≈-0.08, y≈-0.29, z≈0.926, while actual held-placement EEF targets that worked were farther x-negative and not reusable.

## Fragility Flags

The fragile step is the initial bowl grasp. In this layout, pre-positioning over the bowl made the learned policy worse, while a home-start prompt grasped successfully. If home-start fails, do not immediately return to center pre-positioning; try a different prompt or yaw/open-side setup only after confirming the bowl moved.

The second fragile step is placement at the stove edge. If a clean release is close but non-terminal and the bowl remains upright, use `pi0_doubled` as a local contact/recovery skill before resetting.

## Difficulty And Reliability

Solved in 4 attempts in this session. Expected single-shot rate is moderate if using the home-start grasp and learned-contact finish; lower if scripted release is expected to finish alone. No unsolved subgoal remained, but exact manual centering on the stove cook region remained unreliable near the workspace edge.

## Cross-refs

[[learned-contact-after-near-placement]]
[[visual-over-pick-heuristic]]
