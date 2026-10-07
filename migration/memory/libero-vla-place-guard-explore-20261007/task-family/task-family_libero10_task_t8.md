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


## Re-localization per scene
- Two moka pots, visually identical: DISAMBIGUATE by relation only. "left" = robot-left = +y =
  IMAGE-RIGHT pot. Back-project 3+ body pixels, median xy.
- Handle: black curved tube on the pot's side; back-project its top-of-curve segment; note the
  tube axis to choose the cross-tube yaw. SAM3 not needed — back_project pixels directly.
- Stove burner cook region: darker gray disc with RED concentric coil rings on the stove block;
- Do NOT cache this run's absolute xyz; positions re-randomize per seed. Values above are
  counter-examples/ranges only.
