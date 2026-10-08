---
id: task-family_libero10_task_t9
scope: task-family
suite: libero10
regime: task
task_id: 9
task_language: put the white mug in the microwave and close it
evidence:
  cells:
  - 10_task_t9_s0
  attempts: 90
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- support-guided-weak-hook-translation
- reverse-entry-corridor-clearance
---


## Applicable pattern

Insert a wide mug through an open microwave/door threshold, disengage an internal rim hook without extracting the mug, clear the wrist, then close the hinged door physically.

## Winning technique

Semantically select the textured all-white mug and localize mug/handle, cavity, free door edge, and hinge from RGB plus back-projection. Acquire at yaw about 0.8 and pitch about 0.15 with a concise Pi0 grasp. Firm briefly, lower to near support, shift to a positive-x lane while still behind obstacles, and translate upright under +1 hold. At the door plane, modestly lift and co-vary pitch 0.3→0.5→0.8→1.3 while advancing. Release deep, pivot open to about 1.55, then neutralize 1.2→0.8→0.4. Clear by reversing the successful positive-x corridor. Compact and yaw the empty wrist 90 degrees; approach the low exterior free edge, establish normal contact, and sweep +x/+y along the hinge arc until termination.

Success criteria: verified object-sized grip after pick; mug stays upright through supported translation; mug is RGB-visible cavity-side after release; fingers are symmetric/open before reverse clearance; door becomes edge-on and final arc fires the predicate.

## Magic numbers

- Pi0 max_chunks=20 (usable band 16-20); lift_thresh=0.05 (band 0.05-0.08); closed threshold=0.06.
- Initial grasp pose: yaw≈0.8 (band 0.75-0.85), pitch≈0.15 (band 0.10-0.20).
- Supported/lightly-supported carry z≈1.02-1.03 in this kitchen frame; re-derive floor height per scene.
- Threshold pitch ladder: 0.3, 0.5, 0.8, 1.3 (bands ±0.1); step_clip=0.004-0.006.
- Release pivot≈1.55 (band 1.50-1.60); neutralization 1.2→0.8→0.4.
- Door tool yaw≈1.57 (band 1.52-1.62); compact +1 for 8 steps (band 6-10).
- Exterior closure uses low z≈1.04 (band 1.02-1.06), first normal contact then +x/+y arc.
- NEVER carry with gripper -1.
- NEVER use the negative-x exterior detour beyond x≈-0.30.
- NEVER cache absolute xyz from this seed.

## Failure modes

| symptom | root cause (attempt) | fix |
|---|---|---|
| rim/handle insertion or release failed | A4: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A5: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A6: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A7: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A8: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A9: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A10: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A11: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A12: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A13: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A14: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A15: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A16: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A17: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A18: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A19: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| rim/handle insertion or release failed | A20: grasp-offset, slip, hook, or shallow insertion | support mug early; use positive-x threshold route |
| alternate lane/release/door contact failed | A21: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A22: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A23: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A24: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A25: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A26: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A27: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A28: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A29: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A30: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A31: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A32: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A33: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| alternate lane/release/door contact failed | A34: side wall, hook retention, or missed door torque | advance cavity-side first; clear via reverse corridor |
| post-release clearance or door closure failed | A35: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A36: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A37: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A38: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A39: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A40: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A41: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A42: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A43: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A44: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A45: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A46: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A47: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A48: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| post-release clearance or door closure failed | A49: extraction, wrist trap, or wrong contact face | neutralize then reverse the entry corridor; close from exterior low edge |
| external pinch/retainer/ram failed | A50: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A51: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A52: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A53: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A54: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A55: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A56: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A57: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A58: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A59: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A60: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A61: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A62: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A63: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A64: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A65: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| external pinch/retainer/ram failed | A66: unstable pinch or frame wedging | retain narrow hook and use table/light support |
| door/window/frame coupling failed | A67: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A68: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A69: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A70: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A71: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A72: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A73: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A74: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A75: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A76: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A77: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A78: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A79: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A80: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A81: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| door/window/frame coupling failed | A82: mug remained exterior or hook re-engaged | establish cavity-side ordering before door sweep |
| push/slide acquisition failed | A83: pinch collapse, tipping, or rolling loss | hold a verified Pi0 hook during supported translation |
| push/slide acquisition failed | A84: pinch collapse, tipping, or rolling loss | hold a verified Pi0 hook during supported translation |
| push/slide acquisition failed | A85: pinch collapse, tipping, or rolling loss | hold a verified Pi0 hook during supported translation |
| push/slide acquisition failed | A86: pinch collapse, tipping, or rolling loss | hold a verified Pi0 hook during supported translation |
| open U-cage did not translate mug | A87: fingers rode cup; yawed cage stalled | use a held hook, not an open cage |
| handle-loop method never realized | A88: vertical aperture and IK divergence | avoid high-pitch/yaw side branch |
| negative-x supported detour stalled | A89: door corner/workspace wall at x≈-0.33 | use positive-x lane and modest lift/pitch |

## Re-localization per scene

- Target mug: agentview semantic authority; choose the textured all-white mug, reject the smooth yellow/white distractor. Use rim/body/handle RGB pixels and 3-8 back-projections; wrist accepts only geometry within 3-5cm of the anchor. No SAM score was used in the winning run.
- Microwave cavity: identify the black appliance opening in agentview RGB; flat/dark depth alone is insufficient. Reject wrist views that show the distractor or exterior.
- Door: back-project free vertical edge and hinge from agentview; derive the closing tangent from their current locations.
- This run's absolute coordinates are counter-examples only and must not be cached; every reset/seed requires re-localization.

## Fragility flags

Most fragile is the threshold crossing: low supported motion stalls at the door plane. Fallback is a modest z unload plus co-varied pitch≈0.3 on the positive-x lane. Second is wrist extraction after release; reverse the same corridor rather than axial retreat. Learned door closure was non-causal in the win; scripted low-edge hinge arc finished it.

## Difficulty and reliability

Solved on the named A90 trajectory after extensive prior exploration. Single-shot reliability is low because Pi0 grasp transform and threshold contacts vary, but the winning mechanism cleanly separated insertion, corridor reversal, and exterior door closure. One seed solved; no claim beyond single-shot evidence.

## Cross-refs

[[support-guided-weak-hook-translation]]
[[reverse-entry-corridor-clearance]]
