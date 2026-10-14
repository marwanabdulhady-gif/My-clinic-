# Course production worksheet — 03 — Welcome On Board: My Clinic & HR Essentials

> Copy one prefilled package worksheet or duplicate this blank template. This is an execution handoff, not an approved course script. The phase plans and approved client decisions remain the source of truth.

## Package identity

- Commercial course group: HR
- Package id / prefix: 03 / 03_hr-employee-induction / `03`
- Audience: All new employees (clinical and non-clinical), day 1–3
- Seat-time estimate: ~45 minutes
- Source file: [`03_hr-employee-induction.md`](../../../md/03_hr-employee-induction.md); pages/slides/timestamps are mapped in that file and the package Phase 2 plan
- Proposal revision: Rev01 · e2026-MC01
- SCORM/completion/pass mark: SCORM 2004; completion/pass mark `70%` (pending D9 confirmation)
- SME owner / status / next review date: <SME role> / Draft for review / <date>

## Learning design baseline

- Learning outcomes and on-the-job actions: [`phase-1-action-map.md`](../../03_hr-employee-induction/phase-1-action-map.md)
- Screen list and counts: [`phase-2-storyboard.md`](../../03_hr-employee-induction/phase-2-storyboard.md); 36 planned screens, 15 scored screens, 145 points; verify against Rev01 before release
- Dependencies/open decisions: [`phase-0-source-lock.md`](../../03_hr-employee-induction/phase-0-source-lock.md); use open B/D/NEW ids and the generated decision sheet; a recommendation is not an approval
- Current objective-evidence risks: [`scorm-structure.md`](../../03_hr-employee-induction/scorm-structure.md) §5; current flagged objectives: none flagged

## Storyboard and interactions

- Storyboard: [`storyboard/storyboard.md`](../../03_hr-employee-induction/storyboard/storyboard.md) · v0.2 draft
- Scenario/game/simulation plan: [`scenario-design-plan.md`](../scenario-design-plan.md) · 4 experiences · ids: hr-031, hr-044, hr-045, hr-061
- Gamification mechanics: [`gamification-plan.md`](../gamification-plan.md); preserve pass mark 70%, points and existing retry rules
- SME questions: [`storyboard-review-register.md`](../storyboard-review-register.md); see source lock for open questions
- Changes proposed: <write only; preserve current cards until approved>

## Visual and character handoff

- Visual plan: [`storyboard/visual-plan.json`](../../03_hr-employee-induction/storyboard/visual-plan.json) · [`storyboard/screen-visuals.html`](../../03_hr-employee-induction/storyboard/screen-visuals.html)
- Package colour/layout: Caring purple #652D8C
- Lead character / co-host: Dr. Omar leads; Noor co-hosts only on mapped screens. See [`phase-3-narration-and-assets.md`](../../03_hr-employee-induction/phase-3-narration-and-assets.md).
- Asset register: [`storyboard/asset-register.md`](../../03_hr-employee-induction/storyboard/asset-register.md)
- Prompt set: [`visual-generation-prompts.md`](../visual-generation-prompts.md); use matching asset ids only
- Planned AI image/video assets: See asset register; optional motion is not in Rev01 scope.
- Authored SVG / test-capture assets: See asset register; close relevant B/D decision before capture or illustration.
- Privacy/accessibility checks: No real identifiers; meaningful alt text; no colour-only meaning; keyboard alternative required.

## Narration and audio-agent handoff

- Script: [`storyboard/narration-script.json`](../../03_hr-employee-induction/storyboard/narration-script.json)
- Export: [`storyboard/audio-script-export.json`](../../03_hr-employee-induction/storyboard/audio-script-export.json)
- Voice/lexicon: [`narration-production-plan.md`](../narration-production-plan.md) and [`narration-and-lexicon.md`](../narration-and-lexicon.md); D10 approval required
- Character speaker assignments: Dr. Omar lead; Noor co-host as mapped in Phase 3; final voice ids await D10.
- Audio outputs: Scripts/exports prepared; final audio not started. Do not generate until D10 voice approval.
- Captions, transcript, normalization and provenance: Scripts prepared; final audio, captions and provenance remain Phase 3 work.
- Source-media restrictions: See Phase 3 privacy notes; package 08 is restricted to approved test-patient captures.

## Build and QA gates

- [ ] Phase 0 facts and decisions closed for this package, or unresolved inputs visibly marked.
- [ ] Proposal/package screen, score, pass-mark, time and scenario totals reconcile.
- [ ] Storyboard cards match the Phase 2 screen list and Phase 4 points/objectives.
- [ ] SME review rows closed; one-check objectives accepted or given a second assessment.
- [ ] Visual prompts/assets reviewed; companions are the approved versions; asset provenance exists.
- [ ] Script lint passes; D10 voice samples approved; final audio and captions reviewed.
- [ ] Build/lint/preview pass using the D9-agreed LMS/SCORM settings.
- [ ] All applicable QA test cases pass; DPO/SME/client sign-off recorded.

## Agent handoff record

- Agent/tool/provider: <name>
- Exact input paths and commit: <paths/hash>
- Output file ids/paths: <list>
- Prompt/model/settings/date: <record>
- Reviewer and decision: <name/role, approved/rework, date>
- Change log: <date — change — reason>


## Package-specific notes

- **SCORM summary:** 10 sections; 6 objectives; current weak evidence list: none.
- **Planned scenario/guided-practice ids:** hr-031, hr-044, hr-045, hr-061. Use exact branches and mechanics from Phase 2/3.
- **Visual identity:** Caring purple #652D8C; shared companion artwork only.
- **Next owner action:** close Phase 0 and package SME/build-detail questions before production.
