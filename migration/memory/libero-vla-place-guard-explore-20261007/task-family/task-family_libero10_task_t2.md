---
id: task-family_libero10_task_t2
scope: task-family
suite: libero10
regime: task
task_id: 2
task_language: turn on the stove and put the pan on it
evidence:
  cells:
  - 10_task_t2_s0
  attempts: 107
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern

Activate a stove knob with learned contact control, grasp a frying-pan handle, and center a large asymmetric payload on a cook region despite yaw-dependent reach walls and changing held offsets.


## Re-localization per scene

- Pan/handle: agentview phrase “the black frying pan on the left” and “its long black handle”; distinguish from the moka pot’s curved black handle. Wrist geometry prompt is the already-chosen pan handle root, never free semantic selection. No SAM score was used; manual RGB plus back_projection was more reliable.
- Cook region: agentview phrase “the gray spiral metal coil on the rectangular stove”; distinguish from plates and the black knob. Wrist refine the concentric center and reject points outside 5 cm of the agentview anchor.
- Knob: agentview phrase “the black vertical stove control above the spiral coil”; distinguish from the moka lid knob. Wrist may be clipped, in which case retain agentview geometry.
- Moka distractor: silver faceted moka pot with black curved handle between pan and stove; explicitly exclude it from pan targeting.
