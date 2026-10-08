---
id: task-family_libero_goal_swap_t2
scope: task-family
suite: libero_goal
regime: swap
task_id: 2
task_language: Put the wine bottle on the top of the drawer
evidence:
  cells:
  - goal_swap_t2_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- drawer-top-contact-before-release
---


## Applicable pattern
Place a tall bottle onto a swapped drawer/cabinet top surface. The task tests visual fixture re-localization under swap: the destination is the dark drawer top, not the nearby slatted wine rack or stove.

## Winning technique
Identify the wine bottle in agentview_high by its dark green vertical body, then back-project a body pixel rather than cap/table-edge pixels. Identify the drawer top as the dark planar surface above the visible handles and beside the slatted rack; sample several pixels across that surface and use the middle of the span. Pre-position above the bottle, use `pi0_pick` only for the grasp, confirm by gripper opening and wrist view, firm with `set_gripper +1`, then carry closed through one high waypoint to the drawer top. Descend slowly toward the top while still holding the bottle; in this run the predicate fired during descent before release.

## Magic numbers
Kitchen frame: home eef z about 1.17; use carry/pre-place z=1.20-1.22.
`pi0_pick`: prompt `pick up the wine bottle`, max_chunks=20 (band 15-24), lift_thresh=0.08 (band 0.05-0.08), gripper_closed_thresh=0.06.
Grip confirmation: final gripper opening around 0.033 m indicated a held bottle; fully closed would indicate air.
Carry step_clip=0.015-0.020; slower is preferred near the drawer/rack fixture.
Descent step_clip=0.010; target z can be below reachable contact, because termination may fire as the held bottle reaches the top.
Never omit `gripper: 1` while carrying or descending with the bottle.
Never use the slatted rack pixels as the drawer-top target; choose the dark horizontal planar top above handles.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| None observed | A1 solved | Keep the high carry path and slow closed-gripper descent; no release was required in this successful trace. |

## Re-localization per scene
Wine bottle: look for the single dark green bottle with a tan cap. Agentview cap or upper-edge pixels may back-project to table depth; use visible bottle-body pixels and confirm in wrist after pre-position. In this run, table-biased samples at rows 430 and 450 were rejected and the lower body sample near (470,505) was used; do not cache these absolute pixels or xyz.
Drawer top: look for the dark flat horizontal cabinet/drawer top above the handles, adjacent to the slatted rack. Back-project multiple top-surface pixels and take the middle of the span. Reject slatted rack wood strips and vertical handle pixels; they are not the placement surface. This run used a center near the middle of three top samples, but absolute coordinates must not be reused.

## Fragility flags
The likely break point is confusing the drawer top with the slatted wine rack. If the wrist shows wood slats under the bottle, move back toward the dark planar top before descending.
A second break point is cap/table edge localization for the bottle; if the back-projected z is near table height, resample on the bottle body or use wrist visual confirmation after pre-position.

## Difficulty and reliability
Solved in 1 attempt on seed 0. Expected single-shot reliability is moderate if the destination surface is semantically classified before motion and the bottle is carried with `gripper: 1`. No unsolved step remained.

## Cross-refs
[[drawer-top-contact-before-release]]
