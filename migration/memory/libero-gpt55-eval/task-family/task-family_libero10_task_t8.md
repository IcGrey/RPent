---
id: task-family_libero10_task_t8
scope: task-family
suite: libero10
regime: task
task_id: 8
task_language: put the left moka pot on the stove
evidence:
  cells:
  - 10_task_t8_s0
  attempts: 3
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Pick one of two identical moka pots (disambiguated by RELATION: "left" = robot-left
= +y = image-RIGHT) and place it on the stove burner (red-coil cook region). The real
test is the GRASP: a moka pot is a wide, low-poly object that top-down body grasps and
Pi0 both fail on. The place is easy once the pot is in hand.

## Winning technique
Pure MANUAL grasp of the thin SIDE HANDLE — do NOT use Pi0 for the pick here.
1. Agentview hi-res: identify the +y (image-right) pot = the "left" pot. Back-project its
   body (median xy) and its black side-handle tube (top of the curve).
2. move_to above the handle top, vertical wrist. Success: eef ~1.5-2cm above handle, gripper open.
3. rotate_wrist yaw ~90deg (1.57) so the fingers close ACROSS the handle tube (tube runs along
   world-Y at the top of its curve; default yaw would slide along it). WARNING: a 90deg
   rotate_wrist DRIFTS the eef ~0.1-0.15m — re-center over the handle afterward.
4. Descend to the tube level (~z 1.00). No stall expected (handle is offset from the wide body).
5. set_gripper +1 (~12 steps). Success criterion: resulting gap ~0.018-0.022 (gripped the tube).
   A gap ~0.012 means you caught only the thin cap knob (will slip); ~0.078 means blocked open.
6. Lift straight up; confirm pot clears table and hangs upright, gap holds ~0.015-0.02.
7. Carry with gripper +1 in <0.30 xy hops at safe height (~1.14).
8. Place: the pot BODY hangs at eef + (~+0.038 x, +0.067 y); target eef xy = burner_center - that
   offset so the base lands on the burner. Descend until the base rests (OSC stalls) then release.
   Success: libero_terminated on release.

## Magic numbers
- yaw for cross-tube grasp: ~1.57 rad (band 1.4-1.7; sign either way is symmetric).
- set_gripper close: +1, steps 12 (band 10-14). GOOD grip gap ~0.020 (band 0.016-0.024).
- pot base -> eef(handle-grip) vertical offset: ~0.108 m (measure per scene).
- pot body center relative to handle-grip: (+0.038 x, +0.067 y) — MEASURE per pick, pot can swing.
- carry height z ~1.14; place eef z ~1.045 (base on burner at surface z ~0.931).
- burner surface only ~3cm above the table (~0.931 vs table ~0.90).
- NEVER use pi0_pick for the moka-pot grasp on this cell (0/3).
- NEVER descend open fingers onto the pot body top-down (stalls on ~7.8cm shoulder).

## Failure modes
| symptom | root cause (A<N>) | fix |
| pi0_pick descends but gripper never closes (opening ~0.078) | A1,A2: Pi0 won't commit on wide moka pot | abandon Pi0; manual handle grasp |
| pi0_pick goes to wrong pot + tilts wrist unrecoverably | A2: Pi0 grounding of "left" + trained tilt | reset; manual, identify target in agentview |
| open-finger top-down descent stalls z~1.03-1.04 | A1: ~7.8cm upper-chamber shoulder ~ gripper max span | grasp the offset handle instead |
| close at z~1.00 gives gap 0.012, slips on lift | A1: caught thin cap knob only | grasp the handle tube (gap ~0.020) |
| rotate_pitch(0) leaves wrist rolled/tilted | A1,A2: Pi0-induced roll not fixable by pitch tool | reset to restore clean vertical wrist |

## Re-localization per scene
- Two moka pots, visually identical: DISAMBIGUATE by relation only. "left" = robot-left = +y =
  IMAGE-RIGHT pot. Back-project 3+ body pixels, median xy.
- Handle: black curved tube on the pot's side; back-project its top-of-curve segment; note the
  tube axis to choose the cross-tube yaw. SAM3 not needed — back_project pixels directly.
- Stove burner cook region: darker gray disc with RED concentric coil rings on the stove block;
  distinct from any plate. Center via back_project (surface z ~0.93).
- Do NOT cache this run's absolute xyz; positions re-randomize per seed. Values above are
  counter-examples/ranges only.

## Fragility flags
- Most fragile step: the 90deg rotate_wrist eef DRIFT (~0.15m). Always re-center over the handle
  AFTER the yaw before descending. Fallback: iterate move_to until eef xy matches handle xy.
- Second: handle is close (~2cm) to the wide body; keep the +x finger clear of the body y-band.

## Difficulty and reliability
Solved on attempt 3 (2 wasted attempts proving Pi0 cannot grasp these pots). Expected single-shot
rate LOW if you start with Pi0; HIGH if you go straight to the manual handle grasp. Nothing left
unsolved.

## Cross-refs
- [[moka-pot-grasp-the-handle-not-the-body]]
