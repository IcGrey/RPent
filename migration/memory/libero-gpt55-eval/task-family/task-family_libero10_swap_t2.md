---
id: task-family_libero10_swap_t2
scope: task-family
suite: libero10
regime: swap
task_id: 2
task_language: turn on the stove and put the moka pot on it
evidence:
  cells:
  - 10_swap_t2_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Two-part kitchen task: (a) turn on the stove (knob), and (b) place the MOKA POT on
the stove cook-region. Both predicates must hold for termination. The SWAP variant
makes the placed object the moka pot (a chefmate frypan sits on the table center as
a DISTRACTOR with its handle over the burner — do NOT move it). KITCHEN frame
(eef home z ~1.17, table z ~0.90, cook-region surface z ~0.93).

## Winning technique
Order matters: GRASP THE MOKA POT FIRST (clean vertical wrist), THEN turn the knob.
1. move_to ~15cm above the moka pot with the fresh home wrist (quat ~identity);
   re-center on the pot's back-projected top center. Success: wrist quat stays
   near-vertical (no big x/y quat components).
2. pi0_pick("pick up the moka pot", max_chunks~24, lift_thresh 0.05). Success:
   gripper closes to ~0.045-0.05 and eef lifts >0.1m. NOTE pi0_pick.success may
   report false even on a good grasp — verify by gripper width + wrist/agentview.
   Pi0 typically also carries the pot toward +y (its trained place side), which for
   this scene is toward the stove — let it.
3. set_gripper(+1, ~6) to firm.
4. move_to over the cook-region center at carry z (~1.06), then descend
   (move_to to z~1.02). The pot base seats on the burner and OSC stalls with the
   eef ~0.14-0.15m above the surface (that is the grasp-to-base offset, expected).
5. release. (On(moka_pot, cook_region) is now satisfied; task predicate still
   waits on the stove being on.)
6. move_to straight up to clear, then move_to near the knob (~(-0.19,0.19) at z~1.05).
7. pi0_doubled("turn on the stove", max_chunks 20) — one call turns the knob; coil
   glows red; libero_terminated fires because BOTH predicates now hold.

## Magic numbers
- pi0_pick moka pot: max_chunks=24 (band 20-32), lift_thresh=0.05, from a VERTICAL wrist.
- set_gripper firm: +1, steps 6 (band 5-8).
- carry z ~1.06; place descend target z ~1.02 (OSC will stall ~1.076 when seated).
- pi0_doubled knob turn: max_chunks=20 (worked in 10 chunks).
- NEVER run pi0_pick on the moka pot from a wrist already tilted by a prior
  pi0_doubled/pi0_pick — it will not close.
- Do NOT move / grasp the frypan — it is a distractor.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| pi0_pick descends onto pot but gripper never closes (stays 0.06-0.078) | A1: wrist had a persistent ~30deg tilt (quat y~-0.26) inherited from doing pi0_doubled knob-turn FIRST; rotate_pitch/rotate_wrist/move_pose could not null it | A2 fix: grasp the pot FIRST from the clean home vertical wrist, before any contact skill |
| manual set_gripper close slips off the pot on lift (grabs air) | A1: smooth wide octagon + tilted/angled fingers | grasp from vertical wrist via pi0_pick (A2 succeeded first try) |

## Re-localization per scene
- moka pot: agentview hi-res, silver octagonal pot with black knob + black side
  handle; back_project its top surface (avoid the knob hole). Confusable only with
  the black frypan by shape — but the pot is silver/white, the pan is a flat black
  disc. This run's xy (pot ~(-0.02,-0.23), coil ~(-0.04,0.17)) are examples ONLY —
  re-derive per scene; swap moves them.
- cook-region: darker gray coil disc on the stove fixture (RGB); when turned on it
  glows red — a strong confirmation the knob worked. Its center is the place target,
  NOT the frypan and NOT the flat metal to the right of the coil.
- knob: black cylindrical knob at the back-left of the stove fixture (~x-0.19). Let
  pi0_doubled find/turn it; just pre-position the eef near it.

## Fragility flags
- Most-likely break: moka-pot grasp. Fallback if pi0_pick won't close: RESET (explore
  mode) and re-do with pot-first ordering; or a manual vertical grasp on the upper
  octagon lifting slowly with re-clamp; or a handle grasp (bar axis ~along y, yaw
  ~90deg so fingers straddle it).
- Placement: confirm the pot is on the COIL, not off-center on the flat stove metal,
  before release (otherwise On(cook_region) won't fire even with stove on).

## Difficulty and reliability
Solved in 2 attempts (1 reset). The single hard step is the moka-pot grasp, which is
essentially a coin-flip UNLESS the wrist is clean vertical — with pot-first ordering
it succeeded on the first pi0_pick. Expected single-shot rate: high IF you order
pick-before-knob-turn; low if you turn the knob first.

## Cross-refs
[[pick-before-contact-skill-keeps-wrist-clean]]
