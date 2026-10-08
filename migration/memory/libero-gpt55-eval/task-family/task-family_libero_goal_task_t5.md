---
id: task-family_libero_goal_task_t5
scope: task-family
suite: libero_goal
regime: task
task_id: 5
task_language: Push the cream cheese to the front of the stove
evidence:
  cells:
  - goal_task_t5_s0
  attempts: 10
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- right-front-perimeter-contact
---


## Applicable pattern
This task is a tight stove-relative final-region task disguised as a push. The successful region was the right/front perimeter of the stove platform, not the visually obvious center/front band or far/back side.

## Winning technique
Identify the blue cream-cheese box by readable RGB label in agentview_high and the stove by the gray burner/platform. Use Pi0 only to grasp the box, then script the transport.

Winning sequence: `pi0_pick("pick up the cream cheese", max_chunks=12, lift_thresh=0.05, gripper_closed_thresh=0.06)`, confirm the box in the wrist view and gripper gap around 0.042 m, carry with `gripper:+1` to the stove right/front perimeter, then descend while still holding. Termination fired during the held descent before release, when OSC stalled/contacted around z≈1.01.

## Magic numbers
`pi0_pick max_chunks=12` (band 10-14) was enough for grasp-only; longer full-task/contact prompts were not needed.

`carry_z=1.08` (band 1.06-1.10) with `gripper:+1` kept the box held.

`right/front perimeter target xy` should be derived per scene; in this seed the counter-example absolute was near x≈-0.02,y≈0.22. Do not cache it.

`descend target z=0.965` (band 0.96-0.98) with `gripper:+1`; actual EEF may stall near z≈1.01 and still terminate.

NEVER carry with omitted gripper or `gripper:-1`; it opens and drops the box.

NEVER use low closed-fingertip pushes around z≈0.93; A3 tipped the box.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Box moved but predicate false after -x/+y pushes | A1 mixed wrong initial axis with contaminated recovery and high-stall contact | Reset and avoid contaminated multi-stage recovery |
| Pi0 contact moved/wedged the box near cabinet side | A2 used full-task contact as delivery | Use Pi0 only for grasp, not delivery |
| Box tipped onto its side | A3 used low closed-fingertip push | Use broad mid-height open contact or held transport |
| Upright box slid but stopped short | A4 pushed pure +y without enough target-zone precision | Change target-zone hypothesis, not just push distance |
| Upright x-aligned box still false | A5 targeted the wrong visual band | Do not trust vertical stove-face samples as target-region evidence |
| Negative-y semantic test false | A6 tested robot-front/plate-side band | Reject simple negative-y interpretation |
| Diagonal stove-edge push false | A7 reached front/platform neighborhood but not right perimeter | Use held transport to right/front perimeter |
| Held placement near/front band false | A8 final placement in central front/platform band not enough | Target right/front perimeter, not center/front |
| Held placement far/back side false | A9 far/back stove-side region not enough | Target right/front perimeter and descend while holding |

## Re-localization per scene
Cream cheese: use agentview_high RGB first; it is the blue rectangular package with readable `Cream Cheese` label. Back-project several top/face pixels for a rough anchor, then use wrist only to confirm the same object is in the gripper. Avoid table pixels next to the box; they return z≈0.90 and bias xy.

Stove: classify semantically in RGB as the gray metal platform with dark circular burner. Do not confuse with the red-ring plate or flat table bands. The successful target is the perimeter near the stove front/right edge relative to the visible platform, not the burner center.

Counter-example absolutes from this seed: cream-cheese samples around x≈-0.06,y≈0.11; failed central stove-front band around x≈-0.12,y≈0.21; winning held descent target near x≈-0.02,y≈0.22. These are not reusable coordinates.

## Fragility flags
Most fragile step: descending while holding at the right/front perimeter. If the EEF stalls above the requested z but the box is still held and in contact, do not abort; termination may fire from that contact state.

Fallback: if Pi0 reports `success:false` but the gripper gap and wrist image show the box held, continue. This is covered by [[visual-over-pick-heuristic]].

## Difficulty and reliability
Solved after 10 total attempts, including five prior-agent failures and four failures in this session. Expected single-shot rate is moderate if the target region is chosen correctly; low if the agent treats this as a pure push to the visually central front band.

## Cross-refs
[[right-front-perimeter-contact]]
[[visual-over-pick-heuristic]]
