---
id: task-family_libero_spatial_swap_t6
scope: task-family
suite: libero_spatial
regime: swap
task_id: 6
task_language: Pick the akita black bowl next to the cookies box and place it on the
  plate
evidence:
  cells:
  - spatial_swap_t6_s0
  attempts: 49
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- near-goal-contact-regrasp
---


## Applicable pattern
A duplicate-object spatial-relation pick where the correct patterned bowl is the one adjacent to the cookies box, followed by a cramped bowl-on-plate placement onto a red-ring plate partly hidden by cabinet/metal support geometry.

## Winning technique
Use agentview_high for identity: target is the bowl adjacent to the cookies box; the other patterned bowl is a distractor. Back-project several target, cookies, and plate pixels, but do not cache absolute xyz across scenes.

If an initial relation-prompt pick only catches the rim without lifting, open and recover while the bowl is still upright. Move to a more offset source prepose that frames the same target bowl from the cookies side, then use `pi0_pick` with `pick up the akita black bowl` and a moderate chunk budget. Carry high with `gripper:1`; descend using `move_pose` in two closed-gripper stages until the bowl body visibly overlaps the red-ring plate. Release once. If the bowl is visibly on or partly on the plate but the predicate does not fire, immediately use a very short local `pi0_pick`/contact prompt naming the current relation, `pick up the bowl on the plate`; in A49 this regrasp/contact nudged the bowl into the accepted plate region and terminated.

## Magic numbers
Kitchen-frame source prepose z=1.06-1.08; carry z=1.12-1.13.

Reliable source prepose observed in this seed: eef near x=0.148, y=-0.034, z=1.06. Treat as a seed-local counterexample, not a reusable coordinate.

First pick prompt: `pick up the akita black bowl`, `max_chunks=12` (band 10-12), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Closed descent over plate: `move_pose`, `gripper:1`, `step_clip=0.004` then `0.0025`, z=1.015 then 1.00 (band 1.00-1.02).

Near-plate terminal contact: `pi0_pick` prompt `pick up the bowl on the plate`, `max_chunks=6` (band 5-6), `lift_thresh=0.03` (band 0.03-0.04). This is a local contact/regrasp after visible plate overlap, not a free semantic placement skill.

Never use generic `pick up the black bowl` after a failed off-plate release around duplicate bowls unless the wrist/agentview already constrains the current bowl; A1 grabbed the wrong duplicate.

Never let `move_pose` omit `gripper:1` while carrying.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Bowl released beside or on edge of plate, predicate false | A1-A5 direct offsets and biased releases did not account for held rim offset and cramped plate/support geometry | Use closed-gripper staged descent, then local near-plate contact/regrasp only after visible overlap |
| Generic recovery grabs duplicate bowl | A1 used ambiguous `pick up the black bowl` after a failed placement | Preserve semantic identity from agentview; if recovering near the plate, prompt by current local relation (`bowl on the plate`) |
| Extreme yaw source grasp misses or frames wrong object | A17/A47/A48 yawed source poses can show the duplicate/ramekin or miss the bowl | Use wrist as geometry check for the same agentview target; reject wrong candidate and return to known source prepose |
| Pi0 fixture/contact prompt moves toward cookies/cabinet instead of plate | A14/A19/A44 showed trained contact grounding is unreliable as a standalone fixture or semantic placement tool | Use Pi0 only for source grasp and the final short local contact when the bowl is already visibly on the plate |
| Support/cabinet/plate sweeps expose the plate but still do not fire | A18/A43/A45 manipulated visible support faces but the bowl still settled at the accepted-region edge | Do not spend more attempts on larger versions of the same visible-edge sweep; change to constrained local regrasp/contact |
| Cookies-box auxiliary attempts pollute the target | A46 Pi0 box pickup pushed the box into/on the target bowl | Avoid top-down Pi0 box pickup; only scripted side pushes remain a bounded but risky alternative |

## Re-localization per scene
Target bowl: visually the patterned black-and-white bowl whose rim is adjacent to the cookies box. Segment phrasing can be `the black patterned bowl next to the cookies box`, but manual agentview pixels were more reliable here. Reject the duplicate by relation to cookies and global layout.

Cookies box: red/white/yellow oatmeal-raisin cookies package between the bowls; use it only as a relation landmark and avoid disturbing it.

Plate: white ceramic disc with red concentric rings on a square silver/metal support near the cabinet. It is semantically a plate, not the gray support or ramekin. Back-project pixels on the red-ring/white ceramic surface and region-filter z around the plate surface. The visible fragment is edge-biased; use several samples.

Absolute coordinates from this run, such as target samples around (0.05-0.07, 0.18-0.19) and plate samples around (-0.22, -0.09), are counterexamples only and must not be reused.

## Fragility flags
The fragile step is the transition from visible plate overlap to predicate satisfaction. If release is nonterminal but the bowl remains upright and visibly on/partly on the red-ring plate, try one short local `pi0_pick` contact/regrasp with `max_chunks<=6` before any open-gripper push. If the bowl topples or slides off the plate, reset rather than generic-repick in a duplicate-bowl scene.

## Difficulty and reliability
Solved on attempt 49 after many failures. Expected single-shot rate is low unless the final local contact/regrasp is used only after clear plate overlap. The source grasp is reliable from a verified prepose, but the final placement is sensitive to the held rim offset and cabinet/support contact.

## Cross-refs
[[near-goal-contact-regrasp]]
