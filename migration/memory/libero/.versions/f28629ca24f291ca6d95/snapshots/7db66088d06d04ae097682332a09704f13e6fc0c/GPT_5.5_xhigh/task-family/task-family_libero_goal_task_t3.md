---
id: task-family_libero_goal_task_t3
scope: task-family
suite: libero_goal
regime: task
task_id: 3
task_language: Open the top layer of the drawer and put the cream cheese inside
evidence:
  cells:
  - goal_task_t3_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Open the top drawer, grasp a flat cream-cheese box, and insert it into the shallow drawer mouth. The task checks `In` once the box crosses into the drawer volume; a separate release was not required in this seed.

## Winning technique
Identify the blue labeled cream-cheese box in `agentview_high.png`, then accept wrist refinement only if it remains close to the same agentview candidate. Open the top drawer with `pi0_doubled("open the top drawer")`; inspect that the drawer front moved out and the interior is visible. Use `pi0_pick("pick up the cream cheese box")` for the grasp only, confirm by a nonzero gripper gap and wrist view of the upright held box, then `set_gripper(+1)` before carrying. Insert at the top-drawer mouth/interior with gripper still closed using a slow `move_to`; in this run the predicate fired during the insertion move before `release`.

## Magic numbers
`pi0_doubled` drawer open: `max_chunks=20` (band 16-24); success flag will stay false unless the whole benchmark terminates, so inspect the image.

`pi0_pick` cream cheese: `max_chunks=20` (band 16-24), `lift_thresh=0.05` (band 0.05-0.08), `gripper_closed_thresh=0.06` (default band 0.05-0.06). Treat `success=false` as acceptable when `peak_lift` is large and wrist/gripper prove the grasp.

`set_gripper`: `gripper=+1`, `steps=8` (band 5-12) after the pick.

Insertion target: shallow drawer mouth/interior, not the back wall. This seed used `[0.02, -0.09, 1.08]`; do not cache it. Use visual drawer state and wrist view per scene.

Insertion servo: `step_clip=0.012` (band 0.010-0.015), `max_steps=120` (band 100-150), `tol=0.015` (band 0.012-0.018), `gripper=+1`.

NEVER omit `gripper=+1` while moving the held box.

NEVER assume `pi0_doubled.success=false` means the drawer failed to open; inspect the drawer image.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| No failed attempts in this cell | A1 solved | N/A |

## Re-localization per scene
Cream cheese: prompt `the cream cheese box` worked in agentview with score 0.34 and wrist with score 0.438. It appears as a small blue rectangular box with readable Cream Cheese label. Confusions are other blue/white rectangular labels if present; reject wrist refinement if it jumps more than about 3-5 cm from the agentview identity anchor. This run's absolute coordinates `[-0.0472, 0.1328, 0.9185]` agentview and `[-0.0594, 0.1322, 0.918]` wrist are counter-examples only and must not be cached.

Top drawer: prompt `the top drawer handle` segmented the upper gray horizontal handle with score 0.277 at the cabinet front. The placement site is the visible opened drawer mouth/interior after contact, not the handle centroid itself. The low-score `open top drawer` segmentation highlighted unrelated rack geometry and should not be used as a placement coordinate.

Drawer interior: after `pi0_doubled`, use RGB/wrist evidence: dark rectangular cavity with side walls and front lip. Place into the shallow mouth to avoid the back wall.

## Fragility flags
The likely break point is drawer opening: `pi0_doubled` reports benchmark success only, so a false result can still be the correct intermediate action. If the top drawer does not visibly open, retry with a more specific contact prompt such as `pull open the top drawer handle` from a clean pose near the handle, or script a short front-handle pull.

The second likely break point is insertion height. If the gripper stalls high, use `move_pose` with `gripper=+1` to co-vary pose, or target a slightly higher/shallower mouth point and let the held box cross the volume.

## Difficulty and reliability
Solved in 1 attempt on seed 0. Expected single-shot rate is moderate because Pi0 opened the drawer and grasped the cream cheese cleanly from the post-open pose, but the method relies on visual confirmation of the drawer state and shallow insertion rather than a fixed coordinate.

## Cross-refs
None.
