---
id: task-family_libero_goal_swap_t3
scope: task-family
suite: libero_goal
regime: swap
task_id: 3
task_language: Open the top layer of the drawer and put the bowl inside
evidence:
  cells:
  - goal_swap_t3_s0
  attempts: 16
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Open a swapped top drawer and insert a wide bowl whose held rim profile collides with the cabinet face. The task is less about deep y insertion than about creating a stable over-edge state above the top drawer tray.


## Re-localization per scene
Bowl: visually the large black/white patterned bowl with a yellow rim. Agentview prompt/description: patterned bowl or akita black bowl. Sample firm interior/rim pixels, avoiding table gaps and the thin yellow rim alone; wrist may refine only if it sees the same bowl near the agentview anchor. Confused with plate/stove as circular surfaces; use RGB pattern and bowl depth/curvature.

Top drawer: visually the dark cabinet on robot-left/image-left with stacked gray horizontal handles. The target is the top layer/top handle and the open dark tray behind it, not the stove burner or plate. Sample the top handle/front face and inspect RGB for the rectangular drawer body. In swap scenes, fixture positions must be re-derived visually.

Counter-example absolutes from this run only: bowl samples included agentview pixels near (579,682), (616,694), (633,642), (602,649); drawer handle/front samples near (542,208), (588,236), (631,238), (680,235). Do not reuse these coordinates on another seed.
