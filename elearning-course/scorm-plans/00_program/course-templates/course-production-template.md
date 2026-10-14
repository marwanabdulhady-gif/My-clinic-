# Course production worksheet — <package number and title>

> Copy one prefilled package worksheet or duplicate this blank template. This is an execution handoff, not an approved course script. The phase plans and approved client decisions remain the source of truth.

## Package identity

- Commercial course group: <HSE / HR / Operations / RCM / Clinical Governance / IT-EHR>
- Package id / prefix: <package and prefix>
- Audience: <from package README>
- Seat-time estimate: <from proposal and package plan>
- Source file: <path and version/date>
- Proposal revision: <Rev01>
- SCORM/completion/pass mark: <Phase 4 setting; mark D9 dependency>
- SME owner / status / next review date: <role / draft, blocked, approved / date>

## Learning design baseline

- Learning outcomes and on-the-job actions: <link to Phase 1 action map>
- Screen list and counts: <Phase 2 list; confirm screens, scored items and points match the proposal>
- Dependencies/open decisions: <B*/D*/NEW ids; do not fill values until written approval>
- Current objective-evidence risks: <from scorm-structure.md §5>

## Storyboard and interactions

- Storyboard: <storyboard.md and version>
- Scenario/game/simulation plan: <scenario-design-plan.md and package-specific IDs>
- Gamification mechanics: <gamification-plan.md; current scoring/hints/lives/retry only>
- SME questions: <review-register rows and Phase 0 questions>
- Changes proposed: <write only; preserve current cards until approved>

## Visual and character handoff

- Visual plan: <storyboard/visual-plan.json and review-board link>
- Package colour/layout: <from brand-identity.md>
- Lead character / co-host: <Noor / Dr. Omar; exact placements in Phase 3 table>
- Asset register: <storyboard/asset-register.md>
- Prompt set: <visual-generation-prompts.md; use only matching asset IDs>
- Planned AI image/video assets: <asset ids, screen ids, status; video prompts are optional and out of Rev01 scope>
- Authored SVG / test-capture assets: <requirements and owner>
- Privacy/accessibility checks: <no identifiers; alt text; no colour-only meaning; keyboard alternative>

## Narration and audio-agent handoff

- Script: <storyboard/narration-script.json>
- Export: <storyboard/audio-script-export.json>
- Voice/lexicon: <narration-and-lexicon.md; D10 approval required>
- Character speaker assignments: <Phase 3 table; one fixed approved voice per guide>
- Audio outputs: <segment id, screen id, part, filename, status; do not create final audio before D10>
- Captions, transcript, normalization and provenance: <status>
- Source-media restrictions: <where relevant>

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
