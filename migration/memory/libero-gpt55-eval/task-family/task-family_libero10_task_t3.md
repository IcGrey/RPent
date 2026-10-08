---
id: task-family_libero10_task_t3
scope: task-family
suite: libero10
regime: task
task_id: 3
task_language: put the bottle in the bottom drawer of the cabinet and close it
evidence:
  cells:
  - 10_task_t3_s0
  attempts: 73
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- co-vary-pitch-clears-yawed-reach-wall
- support-assisted-axis-reorientation
---


## Applicable pattern

Place a tall bottle into a shallow bottom drawer and close it. The hard parts are a stochastic bottle grasp, avoiding handle wedges, orienting the long axis within the drawer footprint, crossing a yawed low-carry reach wall, and seating before closure.

## Winning technique

1. Localize the bottle, drawer floor/cavity, bottom handle, and cabinet body from agentview RGB plus multi-pixel back-projection; accept wrist refinements only within 3–5 cm.
2. Create only a shallow fixture-state change with `pi0_doubled("close the bottom drawer of the cabinet", max_chunks=4)`; keep most of the cavity open.
3. Return to neutral home and call the verbatim task prompt with `pi0_pick(max_chunks=20, lift_thresh=0.05, gripper_closed_thresh=0.06)`. Require visible suspension and a nonzero gap; then firm with `set_gripper(+1, steps=8)`.
4. Carry upright at z≈1.24–1.25 to the perceived cavity, then descend to base support near eef z≈1.10–1.12.
5. While supported and holding +1, execute yaw +1.57, pitch +1.40, yaw +1.57. Verify the held bottle axis by back-projecting endpoints; do not trust image orientation alone.
6. If position-only +y carry stalls, use `move_pose` with pitch≈1.05 and yaw≈2.585, step_clip≈0.003–0.004, to reach the cavity.
7. Descend to support near eef z≈1.00–1.01, release, and retreat straight up/open.
8. Run `pi0_doubled("push the wine bottle deeper into the bottom drawer", max_chunks=20)`, inspect that the mouth is clear, then `pi0_doubled("close the bottom drawer of the cabinet", max_chunks=24)`. Success criterion is `libero_terminated=true`.

## Magic numbers

- `pi0_pick max_chunks=20` (usable band 15–20); stop on retained lift.
- `lift_thresh=0.05` (usable band 0.05–0.08).
- Firm grip `steps=8` (usable band 5–10).
- Shallow fixture perturbation `max_chunks=4` (tested winning value; broader band not established).
- High carry z=1.24–1.25 (usable band 1.23–1.25).
- Supported orientation: yaw +1.57, pitch +1.40, yaw +1.57 (usable tolerance about ±0.05 rad).
- Yawed insertion `move_pose step_clip=0.0035` (usable band 0.003–0.004), `max_steps=220` (band 180–220).
- Deeper-seat skill `max_chunks=20` (tested value); close skill `max_chunks=24` (tested value).
- NEVER call a learned drawer skill while holding the bottle unless explicitly testing gripper release; prior rollouts opened the fingers.
- NEVER carry with gripper −1.
- NEVER judge a static nonzero gap as retention without a load test and wrist/world-z evidence.

## Failure modes

| symptom | root cause (attempt) | fix |
|---|---|---|
| grasp/place/closure failure | Localized the upright dark-green bottle at agentview xy≈(-0.111,0.030), wrist-refined≈(-0.118,0.034); drawer floor z≈0.924 with usable mouth y≈0.14-0.19 and cabinet toward +x. (A1) | Episode abandoned because the upright-grasp route was destroyed. |
| grasp/place/closure failure | Re-localized the restored scene. (A2) | Reset chosen to keep recipe clean and change semantic grounding to exact class name 'wine bottle'. |
| grasp/place/closure failure | Exact-class prompt drove a tilted approach to the bottle but never closed or lifted. (A3) | Next attempt changes wrist yaw/contact geometry. |
| grasp/place/closure failure | Orthogonal wrist contact geometry did not trigger closure. (A4) | Next attempt isolates the true pristine-home full-task-language seed-0 method; prior attempt-1 full-language call had inherited a tilted wrist orientation. |
| grasp/place/closure failure | Pristine-home full task prompt is the reliable grasp lever. (A5) | Next attempt adds wrist yaw 90° after pitch so bottle lies along x. |
| grasp/place/closure failure | Full task-language Pi0 prompt was the only rung that produced a stable grasp. (A6) | Next attempt changes an EARLIER step: carry the grasped bottle UPRIGHT to the drawer mouth while the wrist is in a reachable vertical orientation, then rotate flat only after x/y p |
| grasp/place/closure failure | Re-localized bottle at agentview xy≈(-0.107,0.028), with wrist points consistent within 3–4 cm, and drawer cavity center≈(-0.030,0.166), floor z≈0.924. (A7) | Next plan removes the destructive home-start Pi0 call: pre-position neutral directly from reset, then use full task language. |
| grasp/place/closure failure | Pi0 did not lift autonomously but placed the open fingers around the cork. (A8) | Next attempt changes pre-position x side to bias Pi0 toward shoulder/body contact instead of cork. |
| grasp/place/closure failure | Opposite-x pre-position changed contact from cork to body, but Pi0 leaned the bottle into the drawer handle before lift. (A9) | Next attempt changes fixture state first: open the bottom drawer farther so its handle is outside the bottle grasp corridor, then grasp. |
| grasp/place/closure failure | Fixture-first farther-open approach preserved the upright bottle and appeared to move the drawer front outward slightly, but the subsequent exact archived grasp setup stayed fully  (A10) | Next attempt tests the complementary fixture state: close drawer completely before grasp, then reopen after retained carry. |
| grasp/place/closure failure | Confirmed a reliable grasp from perception-refined pre-position with the short exact wine-bottle prompt, but repeated the pitch-only orientation that earlier A5 had already identif (A11) | Next attempt changes the earlier orientation: carry upright to mouth, then pitch+yaw so bottle spans drawer x before release. |
| grasp/place/closure failure | The planned orientation correction was not reached. (A12) | Next attempt removes the drawer handle from the grasp corridor by closing the fixture before grasp. |
| grasp/place/closure failure | Fixture-first closure solved the handle interference and yielded an x-aligned retained grasp. (A13) | Next attempt stops after the first open and scripts placement using re-localized cavity geometry. |
| grasp/place/closure failure | Fixture-first close and singularity escape repeated cleanly, but the full-task grasp was stochastic and destructive, tipping the bottle before the planned one-open-plus-scripted-pl (A14) | Next attempt uses short exact-object prompt first after fixture closure. |
| grasp/place/closure failure | Clearing the drawer handle and changing prompt order did not overcome stochastic open-finger refusal in this episode. (A15) | Next lever is an opposite-x/body-biased neutral pre-position with drawer closed. |
| grasp/place/closure failure | Opposite-x/body-biased grasp was the key new success: Pi0 ended with a 5.17cm body-contact gap and no lift, but five-step firming plus a 2.5cm retention lift proved load-bearing; t (A16) | Next plan must alter the release geometry earlier: use the retained body grasp and one reopen, then carry higher/deeper in +y before descending so the entire bottle is above the ca |
| grasp/place/closure failure | The changed deeper-placement plan was not reached. (A17) | Next attempt changes ordering earlier: open drawer before grasp and use a handle-cleared body-side approach, avoiding any contact-skill rollout while carrying. |
| grasp/place/closure failure | Opening/keeping the drawer open before grasp did not improve Pi0: from the negative-y handle-cleared pose, the verbatim task prompt remained fully open and tipped the bottle side-l (A18) | Next attempt returns to fixture-first closed drawer for grasp, but opens the drawer script/contact-wise before bringing the held bottle close, preventing policy contact with the he |
| grasp/place/closure failure | A strong body grasp was achieved (official pick success, 0.089m lift, 0.046m gap), but the learned drawer-open rollout explicitly opened the gripper to ~0.0797m and dropped the bot (A19) | Use the observed opener endpoint displacement as a scripted +1-held motion so the gripper cannot open. |
| grasp/place/closure failure | The untried safety lever worked: avoiding pi0_doubled while carrying preserved the grasp. (A20) | Next attempt changes the earlier state: leave the drawer fully open, grasp from pristine home with the verbatim task prompt, then orient and gravity-drop into the unobstructed cavi |
| grasp/place/closure failure | Keeping the drawer fully open prevented the immediate high-release bridge and allowed a slipped bottle to land inside. (A21) | Next attempt changes orientation ordering: yaw the retained upright bottle first, re-firm, then pitch flat, re-firm, and verify endpoint alignment before release. |
| grasp/place/closure failure | The sequential orientation experiment was not reached because both grasp rungs stayed fully open from the body-biased pose in this stochastic trial. (A22) | Next attempt changes the grasp start/order: short exact-object prompt directly from pristine home with no pre-position or preceding full-task call; after confirmed lift, retain the |
| grasp/place/closure failure | Pristine-home short exact prompt was destructive in this trial: fingers stayed fully open and the bottle tipped side-lying beside the open drawer. (A23) | Next attempt changes grasp class: body-biased Pi0 centering followed by explicit five-step firming and a 2.5cm scripted retention lift, rather than requiring autonomous Pi0 closure |
| grasp/place/closure failure | This attempt successfully established the A16-style manual-firming grasp from an open-finger Pi0 centering state and proved it load-bearing by imagery. (A24) | Next attempt avoids explicit rotations and seeks Pi0's naturally horizontal x-aligned body grasp with the drawer already fully open. |
| grasp/place/closure failure | Avoiding in-hand rotation preserved the grasp. (A25) | Next attempt changes pre-contact geometry: pre-pitch the empty gripper and attempt a horizontal side/body clamp so no in-hand rotation is required. |
| grasp/place/closure failure | Pre-pitching from home traps the arm at z~1.188 with negligible translation. (A26) | Next lever, if budget remains: use reliable upright-in-drawer placement and scripted +y drawer-front closure so fixture motion, not a lateral pusher or learned skill, supplies the  |
| grasp/place/closure failure | This attempt did not reach the changed scripted drawer-front closure. (A27) | Next attempt changes grasp setup to A11's higher perception-refined pose with short exact prompt max20; downstream scripted +y closure remains untested. |
| grasp/place/closure failure | Agentview/wrist localized bottle at xy≈(-0.116,0.032), cavity center≈(0.001,0.156), floor z≈0.924, and cabinet body at larger y, proving close axis +y. (A28) | Next attempt changes the earlier placement to the shallow mouth y≈0.13 from the seed-0 method so the closure stroke seats the bottle while closing. |
| grasp/place/closure failure | Fresh perception identified the shallow floor strip at y≈0.122-0.132. (A29) | Next attempt changes the grasp state: obtain a naturally horizontal x-aligned body grasp with Pi0, then carry flat into a slightly deeper mouth target (between A28 deep jam and A29 |
| grasp/place/closure failure | The planned naturally horizontal grasp was not achieved. (A30) | Next attempt changes fixture state before grasp: partially close the empty drawer, a condition that previously produced strong naturally x-aligned body grasps, then target the inte |
| grasp/place/closure failure | The fixture-state lever worked mechanically: a short +y face push partially closed the empty drawer by ~5.8cm. (A31) | Next attempt returns to the reliable manual upright grasp but targets the untested intermediate placement depth y≈0.143 exactly, between the measured A29 outside-fall and A28 deep- |
| grasp/place/closure failure | Agentview localized bottle xy≈(-0.111,0.027), wrist accepted≈(-0.118,0.031), floor z≈0.924, intermediate y≈0.143, cabinet body y≈0.226. (A32) | The likely remaining lever is x footprint: the offset-corrected bottle center was x≈-0.066 rather than the cavity midpoint≈0.01; after toppling along x, part of its footprint may l |
| grasp/place/closure failure | X-centering improved sidewall margin but the released bottle consistently lay along drawer depth y, so closing jammed at eef y≈0.190. (A33) | Next lever changes the earlier release mechanics: yaw the retained upright bottle 90 degrees only (no pitch) at the cavity, then release so gravity/topple bias may align the long a |
| grasp/place/closure failure | Yaw-only rotation retained the bottle (grasp gap ~0.016 m) but induced ~2.2 cm x and ~2.3 cm y EEF drift; after recentering and release the bottle remained stably upright, falsifyi (A34) | Next approach should change the earlier flattening mechanism: pitch while the bottle is floor-supported so gravity/support carry the load, then yaw/recenter only after it is flat,  |
| grasp/place/closure failure | Perception localized bottle at wrist-refined xy≈(-0.118,0.032), drawer floor center≈(0.018,0.166,z0.924), and cabinet body at +y. (A35) | Next attempt changes orientation to floor-supported simultaneous pitch+yaw with tiny steps so the flat bottle settles across world x. |
| grasp/place/closure failure | Short exact Pi0 produced a visually retained grasp despite success=false; firming and an 8cm load test confirmed retention. (A36) | Next lever: floor-supported sequential yaw-first, re-firm, then pitch-second, rather than simultaneous rotation. |
| grasp/place/closure failure | Manual clamp after a Pi0 miss produced a verified grasp. (A37) | Next lever: floor-supported pure negative pitch -1.57 so the cork lands toward +y/deeper, opposite A35's outward cork. |
| grasp/place/closure failure | Attempt 38 never reached the placement experiment. (A38) | Next attempt should carry immediately after the first visually retained grasp, with no long re-clamp (or at most 3–5 steps), then execute the negative-pitch test. |
| grasp/place/closure failure | The grasp/carry/place stage was the cleanest observed: task-language Pi0 produced a 0.0331m gap and 0.180m ascent; no firming was used; yaw +1.57 preserved retention; cavity-center (A39) | Next episode should preserve the winning grasp/place sequence, normalize yaw to 0 immediately after release/retreat while still near the normal branch, and use only scripted sequen |
| grasp/place/closure failure | The grasp ladder produced a real retained grasp, but the cavity carry stalled at x=-0.067,z=1.057 and release placed the bottle upright outside. (A40) | Next attempt changes class to floor-supported pure negative pitch without yaw, so the cork is biased toward +y/deeper. |
| grasp/place/closure failure | The unexecuted negative-pitch test was reached. (A41) | Next attempt changes the toppling contact class: after upright floor placement, clamp the neck while base-supported and pull laterally to generate tipping torque along x. |
| grasp/place/closure failure | The changed downstream neck-clamp class was not reached. (A42) | Next attempt retains the neck-clamp plan but changes grasp setup to the successful A11 high perception-refined pre-position (-0.113,0.030,1.16) before the short exact prompt, avoid |
| grasp/place/closure failure | High A11 pre-position reliably produced a strong 12.3cm-lift grasp. (A43) | Next agent should try changing the earlier grasp itself to a load-bearing side/body grasp whose long axis is already world-x, then release without any post-place toppling. |
| grasp/place/closure failure | Closing the fixture first again produced a strong grasp, but the held bottle orientation was occluded. (A44) | Next agent should retain high A11 grasp reliability and seek a direct world-x body grasp with the drawer already open, or devise a recoverable two-stage park/open/regrasp sequence. |
| grasp/place/closure failure | New class succeeded at the hard grasp/orientation subgoal: explicit side-body Pi0 re-grasp of the deliberately side-lying bottle produced a retained horizontal grasp already aligne (A45) | Next attempt changes the earlier carry altitude to z≈1.25 before translating to the offset-compensated EEF x≈-0.07, then descends vertically; this tests whether the x wall is altit |
| grasp/place/closure failure | High-altitude translation solved A45's x reach wall: at z≈1.24 the EEF reached x=-0.065 within 9mm, versus stalling at x=-0.123 at z≈1.10. (A46) | Next attempt targets EEF x≈+0.02 at high altitude, biasing settled center positive so endpoints fit. |
| grasp/place/closure failure | Positive-x bias improved the settled footprint relative to A46 but support-state drift was still about -4.7cm: EEF x≈+0.010 produced bottle center≈-0.037. (A47) | Next attempt targets EEF x≈+0.08 at high altitude, predicting settled center≈+0.03 and endpoints safely inside. |
| grasp/place/closure failure | Strong positive bias overshot the drawer. (A48) | Combined with A47 (EEF +0.010 stayed inside but negative-side pinched), viable target is bracketed; next uses midpoint EEF x≈+0.04 with y≈0.13. |
| grasp/place/closure failure | The new midpoint bracket put the released bottle fully within the visible drawer footprint. (A49) | Next attempt should change the earlier placement geometry, not repeat closure force variants. |
| grasp/place/closure failure | Fresh perception localized bottle at wrist-refined xy≈(-0.117,0.032), drawer full-floor center≈(-0.020,0.156,z0.924), shallow band≈(-0.009,0.134,z0.924), with close direction +y. (A50) | Next lever: recreate the scripted world-x topple, retreat high, pre-position directly above the perceived body midpoint, then use the verbatim full task language as the grasp promp |
| grasp/place/closure failure | Fresh scene localization confirmed bottle xy≈(-0.108,0.029), drawer shallow band≈(-0.009,0.134,z0.924). (A51) | Obtain the strong upright-to-horizontal grasp, lift straight up first, re-localize the still-fully-open drawer immediately before high carry, then place against current cavity geom |
| grasp/place/closure failure | Clean reset preserved the fully open drawer. (A52) | Next lever changes fixture state before grasp: partially close the empty drawer to alter Pi0's approach and seek the stronger horizontal body grasp observed in earlier archives, th |
| grasp/place/closure failure | A clean pitched central-handle approach plus short +y stroke partially closed the empty drawer to eef y≈0.143. (A53) | Next class: keep partial closure, but use perception-refined high/body-biased pre-position before prompt rather than home-start grounding. |
| grasp/place/closure failure | Reproduced partial empty-drawer closure to eef y≈0.142. (A54) | Next classes for a fresh agent: vary yaw/contact geometry at this high pose without pitch; or obtain a strong upright grasp before altering fixture, park bottle side-lying away fro |
| grasp/place/closure failure | The A11 high preposition plus short exact prompt produced an immediately load-bearing grasp. (A55) | Next lever should change how the movable face is engaged: grasp/pull the actual vertical handle with a closed gripper from below/outside, or use an orthogonal x contact on the hand |
| grasp/place/closure failure | The side-body recovery prompt can rescue a tipped bottle with a strong retained grasp. (A56) | Next lever must prevent handle occlusion earlier—place the bottle fully behind the handle plane before any handle approach, or close the empty drawer first and use a two-stage park |
| grasp/place/closure failure | The no-yaw side-body carry hypothesis was not reached. (A57) | Next lever: obtain a retained upright grasp, park at a clear negative-y tabletop point, and use a controlled high release or base-offset landing to force a free side-lying pose awa |
| grasp/place/closure failure | Controlled elevated park/release successfully created the previously missing free side-lying state away from drawer and handle. (A58) | Next class should avoid regrasp entirely: use a retained upright grasp and change placement/fixture interaction, or pre-shape wrist orientation before initial contact rather than a |
| grasp/place/closure failure | This attempt tested an untried grasp-frame class: rotate the empty wrist to the opposite yaw before approaching the upright bottle, then let Pi0 grasp in that frame. (A59) | A future agent should prioritize a genuinely non-planar handle capture from below with co-varied pitch/yaw, or change an earlier placement/contact geometry so the cork cannot occlu |
| grasp/place/closure failure | Read all 59 prior archives and WIP notes. (A60) | Next changes grasp geometry/prompt: slight positive-x shoulder bias plus a short wide-body-specific prompt; if retained, continue to a handle-unoccluded placement and the untried n |
| grasp/place/closure failure | Re-localized bottle and drawer from the restored scene. (A61) | Next lever: independent 8-chunk grasp-only bursts from pristine home, resetting pose between misses to avoid destructive tails. |
| grasp/place/closure failure | Re-localized bottle and drawer and wrist-confirmed both. (A62) | Next lever: fully close the empty drawer before grasp, then high short prompt; if retained, reopen only with gripper=+1 scripted motion. |
| grasp/place/closure failure | Partial empty-drawer closure plus high short prompt produced a confirmed 11.95cm-lift grasp with 0.0149m gap. (A63) | Next lever: leave drawer fully open, obtain strong upright grasp, perform the same support-pivot at deeper cavity y, and release without a second high lift. |
| grasp/place/closure failure | Re-localized bottle and full open drawer; wrist confirmed bottle xy≈(-0.119,0.031), cavity center≈(0.020,0.158,z0.924), deep floor to y≈0.195. (A64) | Suggested continuation if budget exists: repeat full-open scene until a confirmed grasp, then carry high only to shallow y, descend, advance low to deep y≈0.18, base-supported +x p |
| grasp/place/closure failure | Bottle and drawer were perception-localized (bottle wrist xy≈(-0.118,0.032); drawer floor center≈(0.005,0.145,z0.924)). (A65) | Observation is bounded to +x pivot direction and this deep placement; next attempt reverses/biases pivot toward -x before release so gravity topples across drawer width away from t |
| grasp/place/closure failure | Perception reconfirmed bottle wrist xy≈(-0.119,0.032) and drawer floor center≈(-0.004,0.143,z0.924). (A66) | Next attempt changes geometry to a simultaneous lateral-and-downward support pivot to maintain base friction and force toppling. |
| grasp/place/closure failure | Re-localized bottle≈(-0.119,0.032), drawer floor center≈(-0.004,0.145,z0.924). (A67) | Next lever: pristine-home verbatim-task grasp, no post-pick firming if visually retained, then diagonal lateral+down pivot. |
| grasp/place/closure failure | Bottle and drawer re-localized from agentview+wrist. (A68) | Next lever if reset allowed: partially close empty drawer first, then high short-prompt body grasp; reopen script-wise with gripper +1 held and test diagonal lateral+down pivot. |
| grasp/place/closure failure | Perception localized bottle wrist xy≈(-0.119,0.032), drawer floor center≈(-0.004,0.149,z0.924). (A69) | Next agent should try a non-planar below-handle capture after a placement that keeps the handle unoccluded, or a wrist-pose/contact-height class that contacts the bottle below eef  |
| handle/grasp failure | Yawed below-handle clamps at z1.014-1.022 closed on air; under-bar hook and trained pull did not open the fully closed drawer. (A70) | Use over-bar geometry or avoid fully closing before placement. |
| handle/grasp failure | Open-drawer side-body contact became hooked around the handle; vertical and -y/pitched clearance stalled. (A71) | Acquire away from the handle or change earlier fixture state. |
| handle/grasp failure | Pre-yawed +y-side grasp drove to x≈-0.274 and closed on air. (A72) | Avoid this approach; use a shallow fixture-state change. |

## Re-localization per scene

- Bottle: agentview semantic authority is the single upright dark-green wine bottle with tan cork. Prompt fallback order: `wine bottle`, `dark green bottle with tan cork`, then a positive point on the body. Wrist refinement is accepted only within 3–5 cm of the agentview anchor. SAM score floor was not established because point/back-project localization was sufficient.
- Drawer cavity: identify the white floor bounded by the black cabinet sidewalls. Use several interior pixels and floor z, not the rim/handle centroid. Wrist region samples across the floor are useful for x-range and y-depth.
- Bottom handle: distinguish the lower handle by vertical image ordering; the open handle is toward robot/front and the cabinet body is toward +y. Wrist RGB can reveal the bar orientation, but the handle is not the bottle target.
- Cabinet body: use RGB fixture semantics; it determines close direction toward +y in this scene.
- Absolute values from this run are counter-examples only and must not be cached: bottle xy≈(-0.118,0.033), floor center≈(0.002,0.153,z0.924), open handle≈(0.008,0.040,z0.948–0.955). Re-localize every seed.

## Fragility flags

The grasp is the highest-variance step. If the verbatim prompt stays open or tips the bottle, do not extend a destructive rollout; reset pose or episode. The second fragility is the low yawed +y carry: when `move_to` stalls, switch immediately to co-varied `move_pose` rather than pushing harder. After release, use the trained deeper-seat skill before closure; direct closure on a shallow cork repeatedly pinched.

## Difficulty and reliability

Solved on attempt 73 after 72 failed episodes across multiple agents. Single-shot reliability is low because grasp retention is stochastic and small fixture/orientation differences create handle or mouth wedges. The winning sequence is physically validated on seed 0, but its shallow-close and support-rotation values have single-shot evidence only.

## Cross-refs

[[co-vary-pitch-clears-yawed-reach-wall]] [[support-assisted-axis-reorientation]]
