---
id: task-family_libero_spatial_swap_t0
scope: task-family
suite: libero_spatial
regime: swap
task_id: 0
task_language: Pick the akita black bowl between the plate and the ramekin and place
  it on the plate
evidence:
  cells:
  - spatial_swap_t0_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- visual-over-pick-heuristic
---


## Applicable pattern
Duplicate-bowl spatial disambiguation plus hard bowl-on-plate seating. In the swap variant, choose the black bowl that is physically between the red-rim plate and the gray ramekin, not a named instance or the duplicate that looks easier to reach.

## Winning technique
Use agentview high-resolution RGB as the semantic authority: identify the red-rim white plate, the silver/gray ramekin, and the patterned black bowl whose xy lies between them. Sample several firm pixels on each and use `back_project` medians; use wrist only to confirm that the selected bowl is under the gripper.

Start over the selected bowl around kitchen-frame `z=1.06` and use grasp-only Pi0 prompts. If the first carry/release does not seat the bowl, keep the episode if the bowl is upright and near the plate: re-pick with the spatial qualifier, then if still offset, stage it beside the plate and issue `pick up the raised black bowl`. The final winning step was not a clean center drop; it was a low closed-gripper contact move that visibly slid/held the bowl footprint over the plate, followed immediately by release. Treat visible bowl footprint overlap with the plate interior/rim as the success criterion.

## Magic numbers
`pre_pos_z=1.055-1.06` in kitchen frame for the bowl cluster.
`target_bowl back_project`: sample 3-8 high-res pixels on the patterned interior/rim; reject the duplicate not between plate and ramekin.
`plate center`: sample white interior and red rings; use the semantic plate, not the stove burner.
`pi0_pick max_chunks=14-18` for bowl grasp/recovery prompts; `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.
`carry/place z=1.08-1.11` for travel; `low contact z=0.995-1.01` for final seating.
`step_clip=0.010-0.012` for carry; `step_clip=0.004-0.006` for low contact seating.
NEVER omit `gripper:1` while carrying or doing low contact with a held bowl.
NEVER rely on EEF-at-plate-center for this bowl: the held offset can put the bowl beside the plate.
NEVER cache this run's absolute xyz; they are counter-examples only.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Plate remains empty after apparent first grasp/carry | A1 first grasp plus firm close did not maintain a useful transport state despite initial visual engagement | Re-inspect after open retreat; if bowl is upright, re-pick with spatial qualifier rather than resetting. |
| Bowl released beside/adjacent to plate, predicate false | A1 held-bowl offset was much larger than the EEF-to-plate-center plan assumed | Use wrist/agentview visual footprint, compensate with low closed-gripper contact, and release only after visible overlap. |
| Staged bowl near plate still not On after release | A1 low release alone did not seat enough of the footprint on the plate | Use `pick up the raised black bowl` from the staged state, then a very slow low contact move before release. |

## Re-localization per scene
Target bowl: description `the patterned black bowl between the red-rim plate and the gray/silver ramekin`. It is visually identical to the other black bowl except for its relation; reject any candidate whose xy is not between the plate and ramekin landmarks. Wrist refinement is accepted only if it is still the same agentview-selected bowl.

Plate: description `red-rim white ceramic plate`. It is a white disc with red concentric rings. In kitchen scenes, do not confuse it with the dark gray stove burner; RGB semantics decide the destination before depth.

Ramekin: description `small silver gray ridged cup/dish`. It is only a relation landmark. Use it to disambiguate which duplicate bowl is between the two surfaces.

This run's absolutes were target bowl about [-0.075, 0.20], plate about [0.09, 0.03], ramekin about [-0.17, 0.17], and the other bowl about [-0.10, 0.30]. These numbers must not be reused; rederive them from the current scene.

## Fragility flags
The fragile step is final seating, not semantic identification. If a clean carry ends with the bowl beside the plate, do not repeat the same center-drop geometry; change class to staged re-pick or slow low contact. If the wrong duplicate is moved first, reset because the relation and destination may be disturbed.

## Difficulty and reliability
Solved on attempt 1, but only after in-episode recovery from two nonterminal releases. Expected single-shot reliability is medium if the agent uses relation-based identification and visual low-contact seating; low if it assumes plate-center release is sufficient.

## Cross-refs
[[visual-over-pick-heuristic]]
