---
id: task-family_libero10_swap_t3
scope: task-family
suite: libero10
regime: swap
task_id: 3
task_language: put the black bowl in the bottom drawer of the cabinet and close it
evidence:
  cells:
  - 10_swap_t3_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Pick a bowl off the tabletop, place it into an already-OPEN bottom drawer, then
CLOSE the drawer. KITCHEN frame (eef home z~1.17, drawer floor z~0.92). The swap
relocates the CABINET; the whole difficulty is (a) reaching into/around the
cabinet where OSC move_to hits an IK singularity, and (b) discovering which way
the drawer slides to close — it is NOT necessarily toward the robot.

## Winning technique
1. Localize: bowl xy from image_cam_hi back_project; drawer floor z and cavity
   center from a few floor pixels (z~0.92 band). Note WHERE the cabinet body is —
   the drawer retracts TOWARD it.
2. Grasp: pre-position move_to ~7cm above the bowl, then pi0_pick
   "pick up the black bowl" (max_chunks~14). Success = eef lift >=0.05 and finger
   gap ~0.005-0.02 (holding the rim). set_gripper +1 to firm.
3. Carry + seat FLAT with move_pose (move_to walls near the cabinet): stage over
   the cavity above the rim, then descend until the bowl rests flat on the floor
   (eef stall z ~0.98-0.99). Release; retreat straight up with move_pose. Verify in
   the wrist that the bowl rim is horizontal (a corner placement tilts it — cosmetic
   here, but seat it flat anyway).
4. CLOSE along the correct axis: push the drawer's front face along the slide axis
   TOWARD THE CABINET BODY. Put the CLOSED gripper on the near (open-side) face at
   face height (z ~0.95-0.96) and move_to along the closing axis with gripper=+1,
   step_clip 0.02-0.025, max_steps 120-150. Confirm motion by the floor-edge pixel
   changing (z jumps off the floor value). One or two pushes seat it; the In+Closed
   predicate fires ON the push step (no retreat needed here).

## Magic numbers
- pi0_pick max_chunks=14 (band 12-16); lift_thresh=0.05.
- Carry/seat: move_pose step_clip=0.015-0.02, tol=0.015-0.02, max_steps=120-150.
- Bowl seats flat at eef z~0.96-0.99 (drawer floor ~0.924).
- Close push: z~0.95-0.958, step_clip 0.02-0.025, max_steps 120-150, gripper=+1.
- NEVER assume the drawer closes toward the robot (-x); derive the axis from the
  cabinet position each seed.
- NEVER trust a single move_to near this cabinet — it stalls at the IK singularity;
  use move_pose.

## Failure modes
| symptom | root cause (attempt) | fix |
|---|---|---|
| Drawer floor-edge pixel IDENTICAL to 4 decimals across many pushes; pi0_doubled also does nothing (A1 & most of A2) | Pushing PERPENDICULAR to the rails (pushed -x while the drawer slides -y toward the cabinet) | Re-derive slide axis from cabinet position; push toward the cabinet body. Zero-motion + pi0_doubled-fails = wrong axis. |
| Bowl settles tilted against a wall (A1) | Placed at a drawer corner against the side wall | Place at floor CENTER, descend until flat. (NOTE: the tilt did NOT block closing — do not over-fit this as the blocker.) |
| move_to stalls, eef stuck, final_dist stays high near the cabinet (throughout) | OSC IK singularity for forward(+x)/deep reaches | Use move_pose (co-varies pitch/yaw); it threads the singularity. |
| Handle grip slips during pull (A2) | Thin round handle; default fingers separated ALONG the bar; also the surface-push force cap | 90deg yaw to pinch across the bar — but simpler: just PUSH the front face toward the cabinet (grip not needed once the axis is right). |
| Scripted -x push sails over the rim, no contact (A2) | Fingertips ~= eef_z; pushing at eef_z=0.99 clears a rim top ~0.978 | Push at eef_z <= ~0.96 so the fingers engage the face. |

## Re-localization per scene
- Bowl (akita_black_bowl): agentview hi-res, patterned bowl with a thin yellow rim;
  back_project 3-5 top-surface pixels, median xy. Grasp works from a ~7cm-above
  pre-position + pi0_pick.
- Drawer floor/cavity: sample pixels in the z~0.90-0.96 band; median for the cavity
  center. Floor-edge pixel is the CLOSING PROGRESS SIGNAL — watch its world z/xy.
- Cabinet body: find it in agentview; the drawer closes TOWARD it. This run: cabinet
  at image-left (-y), so close = push -y. DO NOT cache this sign; re-derive per seed.
- Absolute xyz from this run are counter-examples only, never cache them.

## Fragility flags
- The single most fragile step is choosing the CLOSE axis. If the first push moves
  the drawer 0 mm, STOP and rotate the push 90 deg rather than pushing harder.
- Forward/deep reaches near the cabinet stall move_to; always have move_pose ready.

## Difficulty and reliability
- 2 attempts to converge (attempt 1 wasted ~15 closing tries on the wrong -x axis).
  Expected single-shot rate LOW unless the agent derives the slide axis up front from
  the cabinet position. With that insight, the pick+flat-place+axis-push is reliable.
- Honest note: pi0_doubled "close the drawer" NEVER moved this swapped drawer (4
  calls) — it pushed the wrong axis. Scripted axis-correct push is what worked.

## Cross-refs
- [[container-slide-axis-toward-fixture-body]]
- [[rotate-wrist-90deg-drifts-eef-recenter-after]]
- [[probe-container-floor-by-stall-height]]
