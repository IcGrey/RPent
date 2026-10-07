---
id: pregrasp-yaw-recenter
scope: global
kind: strategy
title: Recenter after pre-grasp yaw before trusting Pi0.
applies_when: A pre-grasp wrist yaw is used to change a bowl or cup rim-hook geometry,
  and the rotation shifts the wrist or EEF away from the visually selected target
symptom:
- yaw drift
- wrong neighborhood
- rim hook
- bowl beside plate
- pre-grasp rotation
evidence:
  cells:
  - spatial_task_t9_s0
  attempts: 11
confidence: single-shot
related:
- post-grasp-yaw-offset
- visual-over-pick-heuristic
---


Pre-grasp yaw can make an awkward rim-hook placement solvable, but only if the EEF is explicitly moved back over the perceived target before Pi0 is invoked.

**Why:** In this cell, rotating yaw +1.57 from home translated the wrist view from the stove bowl to nearby distractors. Attempt 10 stopped there. The winning attempt kept the same +1.57 yaw but re-centered over the stove bowl anchor before `pi0_pick`, producing a different held offset that could be placed on the plate.
**How to apply:** Select the target in agentview, rotate yaw by about +/-1.57, inspect the new wrist/global view, then `move_to` the original perceived target xy at a safe pre-pick z while preserving yaw. Use Pi0 only after the target is again under the gripper. Carry with `move_pose(..., gripper=1, target_yaw=<same yaw>)` so the useful held offset is preserved.
**Falsify:** If the yaw rotation does not shift the EEF/wrist off target, or if re-centering with the new yaw repeatedly causes Pi0 to miss while the unrotated grasp succeeds, this lesson is not the right lever.
**Related:** [[post-grasp-yaw-offset]] [[visual-over-pick-heuristic]]
