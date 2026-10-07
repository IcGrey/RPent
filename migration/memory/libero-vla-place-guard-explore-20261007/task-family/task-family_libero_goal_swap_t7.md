---
id: task-family_libero_goal_swap_t7
scope: task-family
suite: libero_goal
regime: swap
task_id: 7
task_language: Turn on the stove
evidence:
  cells:
  - goal_swap_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
A swapped-fixture state-change task: the goal is to turn on the stove, not to move any loose object. The run tests visual recognition of the relocated stove fixture and its black control knob, then use of a contact primitive.


## Re-localization per scene
Stove: in RGB, find the rectangular metal/white stove fixture with the gray concentric-ring burner. It can be confused with a plate because both are circular/ringed; reject the nearby red-rimmed ceramic plate by checking for the rectangular stove base and black control knob.

Control knob: look for the black upright oval/vertical knob just behind or beside the burner. Prompt `the black stove knob` worked. Accept low SAM scores only when the overlay visibly covers the knob body; fallback to manual point back-projection on the lower knob body, not the top silhouette or table gap.

Cooktop/burner: prompt `the stove cooktop` worked reliably. Use it to confirm the fixture and orientation, not as the primary contact point for turning on the stove.

Wrist: no wrist refinement was needed before acting from home in this seed. If another seed fails, move to a safe staged pose over the agentview knob anchor and accept wrist refinement only if it stays within about 3-5 cm of that anchor.

