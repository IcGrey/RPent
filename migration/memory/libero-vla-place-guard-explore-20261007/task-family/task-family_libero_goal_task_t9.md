---
id: task-family_libero_goal_task_t9
scope: task-family
suite: libero_goal
regime: task
task_id: 9
task_language: Put the cream cheese on the rack
evidence:
  cells:
  - goal_task_t9_s0
  attempts: 15
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
A flat cream-cheese box must be placed on the slatted wooden rack in the kitchen frame. The grasp is easy; the task tests recognizing the rack's true support region and using learned held contact to cross an OSC placement wall.


## Re-localization per scene
Cream cheese: blue rectangular `Cream Cheese` box near the bowl/stove. Agentview_high can read the label; wrist overhead confirms the same candidate. Back-project firm pixels on the top/label face, but do not cache this run's absolute xy.
Rack: tan slatted inclined wooden fixture beside the dark cabinet, with red/brown end-cap boards and gray side rails. Segment phrase fallback: `the wooden rack`, `the tan slatted wooden rack`, or use manual pixels. The valid target in this run was reached by emphasizing the top of the rack, not the lower red board. Back-project top/end-cap/ridge pixels as support landmarks; sample examples in this run included upper ridge pixels around rows 189-246 and cols 116-180, but these absolutes are counter-examples only.
Confusers: stove burner/metal disc and cabinet handles are nearby surfaces; reject any plan whose wrist view shows the box over the metal burner/white stove top instead of tan slats.
