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
related:
- pitched-side-grasp-overedge-release
---


## Applicable pattern
Open a swapped top drawer and insert a wide bowl whose held rim profile collides with the cabinet face. The task is less about deep y insertion than about creating a stable over-edge state above the top drawer tray.

## Winning technique
Use agentview_high to identify the patterned bowl and the top drawer handle/cavity; sample several bowl interior/rim pixels and drawer handle/front pixels with `back_project`, but do not cache absolute xyz across scenes.

First, a short full task-language `pi0_pick` can be useful even when it fails to pick: in this solved run it opened the top drawer partway. Then move to a pitched side pre-position over the bowl, use `pi0_pick("pick up the bowl from the side")` only until lift, verify the wrist image and gripper gap, and keep `gripper:+1` for all carries. Carry high to the open drawer side, then use a small-step `move_pose` inward/down until the bowl is partly over the drawer edge. Release from that over-edge state; do not wait for a geometrically perfect deep insertion pose.

## Magic numbers
`pi0_pick` task-language contact/open: `max_chunks=10` (band 8-12), `lift_thresh=0.04` (band 0.04-0.05), expected pick failure is acceptable if drawer opens.

Side pre-position: eef near the bowl agentview anchor, z about 1.06 (band 1.055-1.075), `target_pitch=0.45` (band 0.35-0.50), `target_yaw=0.2` (band 0.1-0.3), `step_clip=0.008` (band 0.006-0.010).

Side pick: `prompt="pick up the bowl from the side"`, `max_chunks=16` (band 14-18), `lift_thresh=0.04`, accept only if wrist shows bowl in gripper and final opening is clearly nonzero, about 0.01-0.02 m in this run.

Carry: hold `gripper:+1`; lift/carry z about 1.17-1.21; high drawer-side target around the visually localized open tray side, not the plate corridor.

Final inward/down pose: use `move_pose` with `step_clip=0.0035` (band 0.003-0.005), `target_pitch=0.55` (band 0.50-0.60), long `max_steps=220` (band 180-240). A nonzero final distance can still be success-ready if the bowl is visibly over the drawer edge.

NEVER release from the plate/front corridor; it drops outside.

NEVER use `move_pose` while holding without `gripper:1`.

NEVER keep forcing negative-y pushes after the bowl is braced outside; switch to a fresh grasp/over-edge release plan.

## Failure modes
| symptom | root cause (attempt) | fix |
| --- | --- | --- |
| Drawer opens but bowl release lands on plate/table/lip | A1, A3-A7: front/lip insertion geometry tried to drive the wide held bowl too deep through collision-heavy space | Use pitched side grasp and release from a high over-edge state instead of deep y insertion |
| Bowl slips during high carry | A2: grip and carry path did not preserve a stable held offset | Verify wrist/gripper after pick, then lift with `gripper:+1` and small clips |
| Staging bowl at closed drawer mouth does not get scooped by opening drawer | A8 | Open/contact step is useful, but still pick and carry the bowl; do not rely on drawer motion to pull it in |
| Pitch after grasp stalls far short | A9: post-grasp pitch/carry did not create the needed approach profile | Pitch/yaw before the side pick so Pi0 grasps with a different approach |
| Short standard bowl pick is marginal or near-air | A10, A13-A15 | Use side prompt from pitched pre-position; require visible wrist-held bowl and ~0.01-0.02 m opening |
| High side release drops outside rather than perching | A14: release before the bowl was sufficiently over the drawer edge | Move inward/down with very small step_clip until the bowl overlaps the open tray edge, then release |
| Held scrape/strip does not reach deep enough | A15 | Do not depend on stripping; success came from over-edge release |

## Re-localization per scene
Bowl: visually the large black/white patterned bowl with a yellow rim. Agentview prompt/description: patterned bowl or akita black bowl. Sample firm interior/rim pixels, avoiding table gaps and the thin yellow rim alone; wrist may refine only if it sees the same bowl near the agentview anchor. Confused with plate/stove as circular surfaces; use RGB pattern and bowl depth/curvature.

Top drawer: visually the dark cabinet on robot-left/image-left with stacked gray horizontal handles. The target is the top layer/top handle and the open dark tray behind it, not the stove burner or plate. Sample the top handle/front face and inspect RGB for the rectangular drawer body. In swap scenes, fixture positions must be re-derived visually.

Counter-example absolutes from this run only: bowl samples included agentview pixels near (579,682), (616,694), (633,642), (602,649); drawer handle/front samples near (542,208), (588,236), (631,238), (680,235). Do not reuse these coordinates on another seed.

## Fragility flags
Most fragile step is the grasp: a standard centered prompt often produces a tiny rim pinch or no useful offset. Fallback is to pre-position with pitch/yaw before calling the side-grasp prompt, then verify with wrist imagery before carrying.

Second fragile step is the final insertion. If the inward/down `move_pose` stalls, inspect the image: if the bowl is partly over the open drawer tray, release immediately; if it is still outside/front, retreat high, re-localize, and approach from a more side-biased x/y rather than pushing straight inward.

## Difficulty and reliability
Solved on attempt 16 after 15 failed archived attempts across several strategy classes. Expected single-shot reliability is modest until the side-pick and over-edge visual criteria are reproduced on more seeds. The successful mechanism contradicts the apparent earlier wall that the drawer had to be reached deeply in y; the winning run went around it by releasing once the bowl overlapped the drawer edge.

## Cross-refs
[[pitched-side-grasp-overedge-release]]
