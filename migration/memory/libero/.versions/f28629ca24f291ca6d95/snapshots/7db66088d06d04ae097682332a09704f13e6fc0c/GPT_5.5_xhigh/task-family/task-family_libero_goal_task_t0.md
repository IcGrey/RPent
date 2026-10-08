---
id: task-family_libero_goal_task_t0
scope: task-family
suite: libero_goal
regime: task
task_id: 0
task_language: open the bottom drawer of the cabinet
evidence:
  cells:
  - goal_task_t0_s0
  attempts: 62
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- contact-skill-state-change
---


## Applicable pattern
Fixture state-change task with a visually ambiguous cabinet front: several gray horizontal handles are visible, but the instruction requires the bottom drawer only.

## Winning technique
Use RGB to select the lowest gray handle, then approach low enough that the wrist frame includes the lowest handle instead of centering the upper/middle handles. From that low pose, use `pi0_doubled` as a learned contact pull with the spatial prompt `pull the lowest gray drawer handle outward`; success is the official termination signal and the visibly opened bottom drawer.

## Magic numbers
`move_pose` pre-contact z=1.025 (usable band 1.02-1.04 in this kitchen frame), target_pitch=-1.15 (band -1.25 to -1.05), target_yaw=0.95 (band 0.85-1.05), step_clip=0.005 (band 0.004-0.006), max_steps=180 (band 160-200).
`pi0_doubled` max_chunks=35 (observed termination at 11 chunks; useful band 20-40).
Never start high enough that the wrist view centers on the upper/middle handle pair when using the bottom-drawer prompt.
Never repeat the high-braced opener plus post-opener handle/front/mouth/side pushes as the primary plan; many attempts plateaued below predicate.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| drawer opens visibly far but predicate remains false | A1-A60 repeatedly used high-braced opener families or post-opener pushes that plateaued below the official bottom-drawer threshold | change the first contact grounding and use a low lowest-handle learned contact |
| plate clearing attempt fails before drawer work | A57 and A60 tried Pi0/scripted plate clearing but did not reliably move the obstruction | do not clear the plate unless a new reliable clearing method is available |
| upper drawer opens instead of bottom drawer | A61 high z=1.155 centered the wrist on the upper/middle handles, and verbatim prompt opened the upper drawer | lower the pre-contact z to about 1.025 and prompt `lowest gray drawer handle` |
| low/front pose reaches poor x and slips | A59 lower/front setup still missed x by about 18 cm and did not open enough | use the A62 low pose/yaw that reaches the handle region and let `pi0_doubled` execute the pull |

## Re-localization per scene
Cabinet: dark rectangular cabinet at table edge; identify by RGB, not depth alone. It can be confused with the stove block or tabletop shadows.
Bottom drawer handle: lowest gray horizontal cylinder on the cabinet face. In this seed it is partly near the plate corridor; absolute coordinates must not be cached.
Upper/middle handles: gray cylinders above the bottom handle and wrong targets for this instruction. If the wrist frame centers these handles, reject the setup and move lower before contact.
Plate: white disc with red rings in front of the cabinet; it is an obstruction/distractor, not a destination.

## Fragility flags
Most fragile step is pre-contact height/yaw. If `pi0_doubled` opens the wrong drawer or fails to terminate, reset if needed and re-approach lower so the lowest handle is dominant in the wrist view, then use the spatial prompt rather than the verbatim task prompt.

## Difficulty and reliability
Converged after 62 archived attempts. Expected single-shot reliability is moderate once the low pose and lowest-handle prompt are used, but untested across seeds. The prior high-braced opener family is strongly unreliable for this task despite large visible drawer travel.

## Cross-refs
[[contact-skill-state-change]]
