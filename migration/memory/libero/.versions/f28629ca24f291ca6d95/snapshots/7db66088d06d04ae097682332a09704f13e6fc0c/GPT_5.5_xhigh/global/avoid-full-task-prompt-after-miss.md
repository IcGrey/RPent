---
id: avoid-full-task-prompt-after-miss
scope: global
kind: strategy
title: Keep Pi0 recovery prompts grasp-only after a missed pick.
applies_when: A Pi0 pick misses or only partially engages and the task still needs
  the LLM to script placement.
symptom:
- missed grasp
- rogue place
- full task prompt
- tipped object
- pi0 opened gripper
evidence:
  cells:
  - goal_task_t6_s0
  attempts:
  - 2
  - 3
confidence: single-shot
related: []
---


After a missed pick, escalating to the full task language can make Pi0 resume an end-to-end pick/place habit; retry with a short grasp-only prompt and a changed chunk budget instead.

**Why:** Pi0 is trained for complete language-conditioned behaviors, so full goal text can cause it to move toward the destination and open the gripper before the LLM has control. In this cell, the full prompt knocked the bottle and bowl over, while a grasp-only retry with max_chunks=14 produced a usable hold.

**How to apply:** If the scene is still clean after a miss, keep the prompt as `pick up the <object>` and change one controlled lever: lower/shift pre-position by 1-3 cm or use max_chunks around 12-16. Once the gripper gap and image show a hold, immediately `set_gripper +1` and script all carry/release commands yourself.

**Falsify:** A future run where the full task prompt reliably grasps without moving toward the destination or opening the gripper, while grasp-only retries fail under the same pre-position and chunk budgets.

**Related:** [[task-family_libero_goal_task_t6]]
