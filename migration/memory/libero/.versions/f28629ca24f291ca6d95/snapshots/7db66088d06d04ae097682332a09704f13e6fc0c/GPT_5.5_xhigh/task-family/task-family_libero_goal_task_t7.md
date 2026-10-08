---
id: task-family_libero_goal_task_t7
scope: task-family
suite: libero_goal
regime: task
task_id: 7
task_language: Turn off the stove
evidence:
  cells:
  - goal_task_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- contact-skill-state-change
---


## Applicable pattern
A fixture state-change task where the goal is to turn a stove knob off, not to move any loose object. The correct primitive is controlled contact with the stove control, with object localization used only to identify the fixture and knob.

## Winning technique
From `agentview_high.png`, identify the stove by RGB as the white square fixture with a gray coil burner and black upright control knob. Segment or manually back-project the black control knob to confirm it is the task-relevant contact target; segment the burner only as fixture context, not as the contact point.

Use `pi0_pick` as a closed-loop contact skill with prompt `turn off the stove`, `lift_thresh=999`, and `gripper_closed_thresh=0`. Success criterion is benchmark termination, not lift. In this run the skill descended from the initial home pose to the knob/control area and fired `terminated:true` in 11 chunks.

## Magic numbers
Kitchen frame: initial eef z around `1.17` (band 1.15-1.20) confirms the stove/cabinet table, with knob and burner surface z around `0.92-0.94`; these absolute values are examples only and must not be cached.

Knob segmentation: prompt `the black stove control knob`, accepted at score `0.155` (usable band about 0.10-0.25 when the overlay is visually correct). Do not require a high SAM score for black-on-dark controls if RGB overlay matches the knob.

Burner segmentation: prompt `the stove burner`, score `0.938` in this run; use it to verify the fixture, not to aim the state-change contact.

Winning contact call: `pi0_pick(prompt="turn off the stove", max_chunks=20, lift_thresh=999, gripper_closed_thresh=0)`. Usable band: `max_chunks=16-24`; `lift_thresh` should be deliberately unreachable for contact use, and `gripper_closed_thresh=0` prevents grasp-closure heuristics from blocking success.

Never use object-transport logic for this task; there is no target object to pick or release.
Never treat a lack of lift as failure for this repurposed contact skill; lift is intentionally disabled.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| none observed | A1 solved directly with contact-skill Pi0 from home | Keep the solve path minimal; if it fails on another seed, localize the knob and try a staged close-pose contact call before scripted pushes |

## Re-localization per scene
Stove: in agentview RGB, look for the white rectangular stove fixture with the gray concentric-ring burner. It can be confused with plates because both are circular/ringed; classify the surrounding rectangular metal stove base before acting.

Control knob: look for the black upright oval/vertical control just behind or above the burner on the stove fixture. Prompt `the black stove control knob` worked with a low but valid score. If SAM score is low, accept only when the overlay covers the visible knob body; manual back-project on the lower knob body is safer than the top silhouette, which can hit background.

Burner: prompt `the stove burner` is reliable for fixture confirmation. Do not use burner center as the contact target for turning the stove off.

Wrist: after the contact skill, wrist shows the gripper near the stove control/burner, but no wrist refinement was needed before acting in this seed. If pre-staging is needed in another seed, accept wrist knob refinement only if it stays within about 3-5 cm of the agentview knob anchor.

This run's absolute positions, such as knob mask around `[-0.404, 0.201, 0.922]` and burner around `[-0.261, 0.207, 0.931]`, are counter-examples only; do not cache them.

## Fragility flags
The fragile perception step is knob localization: black knob surfaces and background can produce noisy single-pixel depths. Use the RGB overlay and fixture context, and fall back to a staged contact prompt rather than overfitting a scripted push point.

If the home-pose contact call fails, next try moving to a safe pose 10-15 cm above the visually localized knob, then repeat the same `turn off the stove` contact call. If that still fails, test short scripted contacts on different knob faces, archiving each contact geometry separately.

## Difficulty and reliability
Solved in 1 attempt. Expected single-shot rate is high when the stove and knob are visible from agentview, because Pi0 already has an appropriate closed-loop state-change behavior. Remaining uncertainty is how robust the same home-pose contact call is when a different seed moves the stove/knob farther from the initial reach envelope.

## Cross-refs
[[contact-skill-state-change]]
