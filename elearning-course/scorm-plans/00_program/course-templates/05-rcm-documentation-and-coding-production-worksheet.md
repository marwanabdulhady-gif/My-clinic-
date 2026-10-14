# Course production worksheet — 05 — RCM Part A: Documentation & ICD-10 Coding That Gets Approved

> Copy one prefilled package worksheet or duplicate this blank template. This is an execution handoff, not an approved course script. The phase plans and approved client decisions remain the source of truth.

## Package identity

- Commercial course group: RCM
- Package id / prefix: 05 / 05_rcm-documentation-and-coding / `05`
- Audience: Physicians and dentists; optional for nurses, coders and RCM staff
- Seat-time estimate: ~25 minutes
- Source file: [`05_rcm-billing-documentation-script.md`](../../../md/05_rcm-billing-documentation-script.md); pages/slides/timestamps are mapped in that file and the package Phase 2 plan
- Proposal revision: Rev01 · e2026-MC01
- SCORM/completion/pass mark: SCORM 1.2; completion/pass mark `80%` (pending D9 confirmation)
- SME owner / status / next review date: <SME role> / Draft for review / <date>

## Learning design baseline

- Learning outcomes and on-the-job actions: [`phase-1-action-map.md`](../../05_rcm-documentation-and-coding/phase-1-action-map.md)
- Screen list and counts: [`phase-2-storyboard.md`](../../05_rcm-documentation-and-coding/phase-2-storyboard.md); 21 planned screens, 10 scored screens, 100 points; verify against Rev01 before release
- Dependencies/open decisions: [`phase-0-source-lock.md`](../../05_rcm-documentation-and-coding/phase-0-source-lock.md); use open B/D/NEW ids and the generated decision sheet; a recommendation is not an approval
- Current objective-evidence risks: [`scorm-structure.md`](../../05_rcm-documentation-and-coding/scorm-structure.md) §5; current flagged objectives: rcma-o5

## Storyboard and interactions

- Storyboard: [`storyboard/storyboard.md`](../../05_rcm-documentation-and-coding/storyboard/storyboard.md) · v0.2 draft
- Scenario/game/simulation plan: [`scenario-design-plan.md`](../scenario-design-plan.md) · 2 experiences · ids: rcma-031, rcma-050
- Gamification mechanics: [`gamification-plan.md`](../gamification-plan.md); preserve pass mark 80%, points and existing retry rules
- SME questions: [`storyboard-review-register.md`](../storyboard-review-register.md); see source lock for open questions
- Changes proposed: <write only; preserve current cards until approved>

## Visual and character handoff

- Visual plan: [`storyboard/visual-plan.json`](../../05_rcm-documentation-and-coding/storyboard/visual-plan.json) · [`storyboard/screen-visuals.html`](../../05_rcm-documentation-and-coding/storyboard/screen-visuals.html)
- Package colour/layout: Collaborative burgundy #7C0041
- Lead character / co-host: Dr. Omar leads; Noor co-hosts only on mapped screens. See [`phase-3-narration-and-assets.md`](../../05_rcm-documentation-and-coding/phase-3-narration-and-assets.md).
- Asset register: [`storyboard/asset-register.md`](../../05_rcm-documentation-and-coding/storyboard/asset-register.md)
- Prompt set: [`visual-generation-prompts.md`](../visual-generation-prompts.md); use matching asset ids only
- Planned AI image/video assets: See asset register; optional motion is not in Rev01 scope.
- Authored SVG / test-capture assets: See asset register; close relevant B/D decision before capture or illustration.
- Privacy/accessibility checks: No real identifiers; meaningful alt text; no colour-only meaning; keyboard alternative required.

## Narration and audio-agent handoff

- Script: [`storyboard/narration-script.json`](../../05_rcm-documentation-and-coding/storyboard/narration-script.json)
- Export: [`storyboard/audio-script-export.json`](../../05_rcm-documentation-and-coding/storyboard/audio-script-export.json)
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

- **SCORM summary:** 6 sections; 5 objectives; current weak evidence list: rcma-o5.
- **Planned scenario/guided-practice ids:** rcma-031, rcma-050. Use exact branches and mechanics from Phase 2/3.
- **Visual identity:** Collaborative burgundy #7C0041; shared companion artwork only.
- **Next owner action:** close Phase 0 and package SME/build-detail questions before production.
