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
related: []
---
## Applicable pattern

Put an upright tall bottle into an open bowl. The task is mostly a close-range contact/placement problem: ordinary Pi0 bottle grasping may not engage from above, while a task-language contact skill can finish once the gripper is staged directly at the bottle beside the bowl.


## Re-localization per scene



Wrist refinement: after moving over the bottle, accept wrist confirmation only if the same upright bottle appears below the gripper and the bowl is adjacent in the expected direction. Do not let the wrist relabel the cream-cheese box or plate as a target; they are distractors.
