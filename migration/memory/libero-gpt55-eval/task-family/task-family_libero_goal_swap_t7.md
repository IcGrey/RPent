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
related:
- contact-skill-state-change
---


## Applicable pattern
A swapped-fixture state-change task: the goal is to turn on the stove, not to move any loose object. The run tests visual recognition of the relocated stove fixture and its black control knob, then use of a contact primitive.

## Winning technique
Classify the stove in `agentview_high.png` by RGB and geometry: a rectangular metal stove base with a gray concentric-ring burner and a black upright knob. Segment or manually back-project both the black knob and the cooktop to confirm the fixture; use the knob as the contact target and the burner/base only as semantic context.

From the initial home pose, call `pi0_pick` as a closed-loop contact skill with prompt `turn on the stove`, `max_chunks=20`, `lift_thresh=999`, and `gripper_closed_thresh=0`. Success is the official `terminated:true` predicate, not object lift. In this run the skill descended to the knob/control area and fired termination in 15 chunks, with no release or transport step.

## Magic numbers
Kitchen frame: initial eef z about `1.17` (usable band 1.15-1.20) confirms the stove/cabinet scene; knob and cooktop visible surfaces were around z `0.92-0.94` in this run, as examples only.

Knob segmentation: prompt `the black stove knob` worked at score `0.228` (usable low-score band about 0.10-0.30 when the overlay is visually correct). Manual point checks on the knob body should agree within a few cm.

Cooktop segmentation: prompt `the stove cooktop` worked at score `0.836` and is useful for fixture confirmation. Do not aim the state-change contact at the burner center unless testing a fallback; the control knob is the relevant contact target.

Winning contact call: `pi0_pick(prompt="turn on the stove", max_chunks=20, lift_thresh=999, gripper_closed_thresh=0)`. Usable `max_chunks` band is 16-24; `lift_thresh` should be deliberately unreachable for contact use.

Never require positive lift for this task; peak lift can remain zero because the task is contact, not grasp.
Never run a pick/place/release sequence for a loose object; the named goal contains no transported object.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| None observed | A1 solved directly with home-pose contact skill | Keep the minimal contact path. If it fails on another seed, first pre-stage 10-15 cm above the visually localized knob and repeat the same contact prompt before trying scripted pushes. |

## Re-localization per scene
Stove: in RGB, find the rectangular metal/white stove fixture with the gray concentric-ring burner. It can be confused with a plate because both are circular/ringed; reject the nearby red-rimmed ceramic plate by checking for the rectangular stove base and black control knob.

Control knob: look for the black upright oval/vertical knob just behind or beside the burner. Prompt `the black stove knob` worked. Accept low SAM scores only when the overlay visibly covers the knob body; fallback to manual point back-projection on the lower knob body, not the top silhouette or table gap.

Cooktop/burner: prompt `the stove cooktop` worked reliably. Use it to confirm the fixture and orientation, not as the primary contact point for turning on the stove.

Wrist: no wrist refinement was needed before acting from home in this seed. If another seed fails, move to a safe staged pose over the agentview knob anchor and accept wrist refinement only if it stays within about 3-5 cm of that anchor.

This run's absolute examples, including knob segment near `[-0.0419, 0.1255, 0.9219]` and cooktop segment near `[0.1232, 0.1315, 0.9253]`, must not be cached; re-localize every scene.

## Fragility flags
The likely break point is semantic confusion between the stove burner and a plate-like ringed surface. Always classify the rectangular stove base and black knob before invoking contact.

A second possible break point is low-confidence black-knob segmentation. If the overlay is wrong or absent, use manual knob pixels from `agentview_high.png`; if contact from home fails, pre-stage above the knob and retry Pi0 contact before scripted pushes.

## Difficulty and reliability
Solved in 1 attempt on seed 0. Expected single-shot reliability is high when the stove and knob are visible from agentview because Pi0 has a learned stove-contact behavior. Remaining uncertainty is robustness when a swap seed places the stove/control farther from the home-pose contact trajectory.

## Cross-refs
[[contact-skill-state-change]]
