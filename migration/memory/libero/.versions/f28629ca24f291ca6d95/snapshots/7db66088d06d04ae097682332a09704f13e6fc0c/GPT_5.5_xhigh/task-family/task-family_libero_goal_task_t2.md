---
id: task-family_libero_goal_task_t2
scope: task-family
suite: libero_goal
regime: task
task_id: 2
task_language: put the wine bottle in the bowl
evidence:
  cells:
  - goal_task_t2_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- near-target-repick
---


## Applicable pattern

Put an upright tall bottle into an open bowl. The task is mostly a close-range contact/placement problem: ordinary Pi0 bottle grasping may not engage from above, while a task-language contact skill can finish once the gripper is staged directly at the bottle beside the bowl.

## Winning technique

Identify the wine bottle in agentview_high as the dark green upright bottle with a cork, and the destination as the black-and-white patterned open bowl with yellow rim. Back-project multiple pixels on the bottle and use a region window on the bowl interior to anchor the cavity; use the wrist only to confirm that the same bottle and bowl are under the gripper.

From a fresh scene, move open above the bottle neck/body so the wrist sees the upright bottle directly below the gripper. If the low `move_to` stalls high but leaves the gripper aligned over the bottle, close briefly with `set_gripper +1`, then call `pi0_pick` with the full task language `put the wine bottle in the bowl`. In this solved run, that close-pose task-language Pi0 call moved the bottle into the bowl and terminated before any scripted release.

## Magic numbers

Bottle/bowl kitchen frame: pre-position around `z=1.02-1.09` (band 1.02-1.10); commands lower than this may stall at the kitchen floor/fixture limit near `z≈1.02` in this local geometry.

`move_to` over bottle with `step_clip=0.008` (band 0.006-0.012), `max_steps=120`, `tol=0.012`. A final distance around 0.038 was still usable because the wrist showed correct alignment.

`set_gripper +1` for 12 steps (band 8-12) can stage contact, but a fully closed gap around 0.006 means it did not securely hold the bottle by itself.

Winning `pi0_pick`: prompt `put the wine bottle in the bowl`, `max_chunks=24` (band 20-24), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`; terminated in 15 chunks from the close aligned pose.

Never assume the simple prompt `pick up the wine bottle` is best here; in A1 it failed to close and knocked the bottle sideways.

Never release a weak neck-held bottle at the near bowl lip; A1 releases around y 0.05-0.09 left it upright outside the bowl.

## Failure modes

| symptom | root cause (A<N>) | fix |
|---|---|---|
| `pi0_pick` with `pick up the wine bottle` descends but leaves the gripper open and bottle disturbed | A1 used a generic pick prompt from above; Pi0 contacted the bottle but did not close/lift | Stage the gripper close to the upright bottle and switch to the full task-language prompt |
| Bottle remains upright just outside or against the bowl after release | A1 used a weak neck clamp and released at the near lip without enough body-offset compensation | Avoid relying on scripted neck carry/release; use close-pose task-language Pi0 contact to seat the bottle |
| Fully closed scripted gripper gap after `set_gripper +1` | A2 scripted clamp around the neck/body closed on air or only brushed the bottle | Treat the clamp as staging only; do not infer a secure grasp unless wrist/gripper show the bottle rising |
| Low `move_to` toward bottle reports final_dist around 0.038 | A2 target z was below what OSC reached in this local pose | If the wrist image confirms alignment, continue with the contact skill instead of grinding lower |

## Re-localization per scene

Wine bottle: use RGB first. It is the dark green bottle with tan cork and cream label beside the bowl; there was no similar distractor in this scene. Manual agentview pixels on the visible cork/neck/body worked better than category segmentation. In this run, samples such as (560,472), (515,455), and (482,450) back-projected around x -0.17..-0.13, y -0.053..-0.034, z 0.92..0.97; do not cache these absolutes.

Bowl cavity: use RGB/shape as the patterned black-and-white open bowl with yellow rim. A region window over the visible interior is better than a single rim pixel. In this run, the interior region around rows 520-640 and cols 470-610, filtered to z 0.90-1.05, centered around x -0.129, y 0.026, z 0.907; do not cache these absolutes.

Wrist refinement: after moving over the bottle, accept wrist confirmation only if the same upright bottle appears below the gripper and the bowl is adjacent in the expected direction. Do not let the wrist relabel the cream-cheese box or plate as a target; they are distractors.

## Fragility flags

The fragile step is the first bottle engagement. Generic Pi0 pick prompts can knock the bottle into a rim-adjacent pose without grasping it. The fallback is not repeated generic picks; stage from a clean or still-upright pose and use the full task-language prompt as a contact/insertion skill.

If a release leaves the bottle upright just outside the bowl, this is recoverable only while the bottle remains upright and close. A close-pose Pi0 task-language call is more promising than side pushes from the rim.

## Difficulty and reliability

Solved in 2 attempts. Expected single-shot rate is moderate: perception is easy, but bottle engagement is prompt- and pose-sensitive. The winning run contradicted the A1 impression that a scripted neck clamp/release was required; the actual solve used Pi0 task-language behavior from a staged close pose. No unsolved subgoal remained.

## Cross-refs

[[near-target-repick]]
