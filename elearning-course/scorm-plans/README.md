# My Clinic — SCORM Module Plans (edumints-scorm-mcp)

![My Clinic logo](00_program/brand/logo-preview.png)

This folder holds the **production plans** for turning each source Markdown file in `../md/` into an interactive SCORM package with the [edumints-scorm-mcp](https://github.com/marwanabdulhady-gif/edumints-scorm-mcp) server.

This remains **planning and draft review**, not a production course build. A [local branded screen generator](00_program/screen-generator.md) now renders review previews from storyboard cards; no SCORM package has been built, voiced, or uploaded to an LMS yet. Every plan follows the server's authoring playbook (`playbook/README.md` in the edumints repo): brand → visual plan → narration → assets → approval → build → QA.

- **Author** = the AI client (Claude) plus the course team.
- **Compiler** = the edumints server. It validates, renders and packages. It never generates content.
- **Approver** = the My Clinic subject-matter experts (SMEs) named in each Phase 0.

---

## 1. Package map (one SCORM package per source file)

| # | Source Markdown | Plan folder | SCORM package (working title) | Audience | Seat time | Storyboard status |
|---|---|---|---|---|---|---|
| 01 | `md/01_health-and-safety-1_facility-management-and-safety.md` | [`01_health-and-safety-1/`](01_health-and-safety-1/) | Facility Management & Safety (9 sections) | All new staff | ~55 min | Storyboard v0.2 complete — SME/source-lock review |
| 02 | `md/02_health-and-safety-2_safety-hazards-fire-and-chemicals.md` | [`02_health-and-safety-2/`](02_health-and-safety-2/) | Safety in Practice: Hazard, Fire & Chemical Lab | All new staff (after 01) | ~33 min | Storyboard v0.2 complete — SME/source-lock review |
| 03 | `md/03_hr-employee-induction.md` | [`03_hr-employee-induction/`](03_hr-employee-induction/) | Welcome On Board: My Clinic & HR Essentials | All new employees | ~45 min | Storyboard v0.2 complete (companions retrofitted) — SME review |
| 04 | `md/04_operations-and-my-care-structure.md` | [`04_operations-and-my-care/`](04_operations-and-my-care/) | Who Does What: Operations & My Care | Front-line, PX, clinical staff | ~15 min | Storyboard v0.2 complete — SME/source-lock review |
| 05 | `md/05_rcm-billing-documentation-script.md` | [`05_rcm-documentation-and-coding/`](05_rcm-documentation-and-coding/) | RCM Part A: Documentation & ICD-10 Coding That Gets Approved | Physicians, dentists | ~25 min | Storyboard v0.2 complete — SME/source-lock review |
| 06 | `md/06_rcm-billing-documentation-slides-2026.md` | [`06_rcm-ebp-benefits-and-rejections/`](06_rcm-ebp-benefits-and-rejections/) | RCM Part B: New EBP Benefits & Claim-Rejection Analysis | Physicians, RCM staff | ~20 min | Storyboard v0.2 complete — SME/source-lock review |
| 07 | `md/07_video-quality-safety-and-risk-orientation.md` | [`07_quality-safety-and-risk/`](07_quality-safety-and-risk/) | Clinical Governance: Quality, Patient Safety & Risk | All clinical staff | ~25 min | Storyboard v0.2 complete — SME/source-lock review |
| 08 | `md/08_video-it-ehr-consultation-walkthrough.md` | [`08_it-ehr-consultation/`](08_it-ehr-consultation/) | EHR Consultation Workflow: Guided Simulation | Physicians, clinical staff | ~25 min | Storyboard v0.2 complete — SME/source-lock/DPO review |

**Why 05 and 06 are two packages, not one.** Both files come from the same RCM session, but they carry different content: 05 (the script) teaches documentation and coding; 06 (the 2026 deck) adds the new EBP benefits and the rejection log. Splitting them avoids repeating the same screens and lets RCM staff take Part B alone.

**Why 01 and 02 are two packages.** 01 is the full knowledge course (nine CBAHI/FMS plans). 02 overlaps on fire and chemicals, so it is planned as an **applied practice lab** (hazard spotting, fire drill game, spill triage, chemical-store escape room) that assumes 01 is done. No screen is copied from 01 into 02.

**Status, gaps and next steps:** [`00_program/programme-status.md`](00_program/programme-status.md) (module × phase grid, proposal check, ordered next actions).

**SCORM structure:** [`00_program/scorm-structure.md`](00_program/scorm-structure.md) (LMS curriculum, zip contents, manifest, outline → screen model, LMS data) and one generated `scorm-structure.md` in each module folder.

### Repository tools (deterministic, rerunnable)

| Tool | Produces | Notes |
|---|---|---|
| `tools/assemble_storyboard_docs.py` | The six generated review packs (01, 02, 04, 05, 06, 08): cards, visual plan, narration, audio export, voice table, asset register, visual board; plus the production board and SME register | Never touches the hand-authored 03/07 storyboards; [G10 restoration](00_program/g10-visual-restoration.md) adds 02 drill and 08 capture manifests |
| `tools/normalise_narration.py` | Canonical narration/audio outputs for the hand-authored packs (03, 07) | Same rules as the generator, via `tools/audio_export.py` |
| `tools/audio_export.py` | Shared rules: speaker labels out of TTS input, one segment per spoken line, lexicon + SSML, voice table | Imported by both tools above |
| `tools/lint_planning.py` | `storyboard/lint-report.json` for all eight packs | Local port of the edumints `lint_visual_plan` / `lint_narration_script` rules (rev `4bbf4591`); the report states the server lint must still be rerun before Phase 4 |
| `tools/build_scorm_structure.py` | `<module>/scorm-structure.md` + `00_program/scorm-structure-summary.json` | Rerun after any storyboard change |
| `tools/generate_screens.py` | Ignored `.generated/screens/`: offline branded HTML preview + generation report | [Usage and coverage](00_program/screen-generator.md); draft review only, not SCORM or approval |
| `tools/prepare_asset_approval_handoff.py` | [G10 approval packet](00_program/asset-approval-handoff/README.md), 44-row response template and request JSON | Prepared, not submitted or approved; preserves human responses |
| `tools/export_storyboard_docx.py` | The nine client-review Word documents | Supplied client logo in the running header, cover band, document control, page numbers |
| `tools/make_companion_avatars.py` | Interim transparent avatar PNGs in `00_program/characters/assets/` | Crops of approved poses; full-size Canva downloads still outstanding (G6) |
| `tools/audit_assets.py` | `00_program/asset-template-audit.md` + `asset-audit.json` | Hard failures (missing referenced asset, broken link, label in TTS, incomplete card) exit non-zero |
| `tools/build_decision_sheet.py` | `00_program/decision-sheet.md` + `decision-sheet.csv` | Parses the eight `phase-0-source-lock.md` files, `cross-module-decisions.md` and `scorm-structure-summary.json`; lists **open** rows only (102 as at 2026-10-14) with owner role, due date and write-back target. Rerun after any Phase 0 write-back — closed rows drop out |
| `tools/export_kickoff_docx.py` | `00_program/kickoff-pack.docx` (`MC-KO-01 v0.1`) | Kick-off run sheet + decision sheet as one branded Word file; reuses the header, footer and Markdown renderer from `export_storyboard_docx.py` |

Recommended order after any approved edit: generator or normaliser → `lint_planning.py` →
`build_scorm_structure.py` → `export_storyboard_docx.py` → `build_decision_sheet.py` →
`export_kickoff_docx.py` → `audit_assets.py`.

Suggested learning path (matches `../README.md` §4):
`03 → 07 → 01 → 02 → 04 → 05 → 06 → 08`

### Storyboard-review artefacts (14 October 2026)

Six newly completed packs — **01, 02, 04, 05, 06 and 08** — are indexed on the
[programme production board](00_program/storyboard-production-board.md). Each provides a complete
screen-card storyboard, branded HTML visual board, editable narration script, visual plan, voice-talent
export, asset register and planning lint report. The visual-plan and narration-script reports are clean
for those six packs; this is a **documentation-quality result only**, not SME/policy approval or a build
release. Client-shareable Word renderings for all eight modules are in
[`client-review/`](client-review/). The screen-level authoring and visual sign-off queue is in
[`00_program/storyboard-review-register.md`](00_program/storyboard-review-register.md) with a
[tracker-import CSV](00_program/storyboard-review-register.csv).

---

## 2. The phase model used in every module folder

Every module folder has the same files, so the team can track all eight packages on one board. `scorm-structure.md` in each folder is generated from the storyboard by `tools/build_scorm_structure.py`: the package tree, manifest, every section and screen, objectives and tracking.

**Phase 2 is two steps.** `phase-2-storyboard.md` is the *screen list*: one row per screen — id, type, purpose, points, source. Once the list is approved, the [storyboard template](00_program/storyboard-template/) turns each row into a finished **screen card** in `<module folder>/storyboard/storyboard.md`: full on-screen wording, visual brief, animation/reveal behaviour, interaction and scoring with feedback, the complete narration script, accessibility notes, review build metadata, and companion visual/narration JSON. Write one module per run. The cards, not the list, are what the developer builds from after source lock; type-specific production JSON is completed in Phase 4.

| Phase | File | What it produces | Exit gate (must be true to move on) |
|---|---|---|---|
| **0 — Source lock** | `phase-0-source-lock.md` | Resolved conflicts, verified facts, permissions, SME owners | Every **blocking** item has a written decision from the named owner |
| **1 — Action map & objectives** | `phase-1-action-map.md` | Business goal, observable behaviours, practice activities, objective → evidence map, seat-time budget | SME agrees the objectives and the assessed evidence |
| **2a — Screen list** | `phase-2-storyboard.md` | Screen-by-screen plan: id, section, edumints screen type, content, interaction, scoring, source page | `lint_visual_plan` clean (errors fixed, warnings justified); SME and course owner approve |
| **2b — Storyboard cards** | `storyboard/storyboard.md` | One finished card per Phase 2 screen: on-screen text, visual design and animation/reveal, interaction and scoring, full narration script, accessibility, review build metadata | Every Phase 2 screen has a card (same ids, same order); the visual plan and narration script validate against the server models; every card passes the structural template audit; the human/SME checklist is the next hand-off. Type-specific build JSON follows approved source lock in Phase 4. |
| **3 — Narration & assets** | `phase-3-narration-and-assets.md` | Narration outline per screen, pronunciation lexicon, asset manifest with provenance, characters, video plan | `lint_narration_script` and `lint_authoring_plan(stage="planning")` clean; voice and visuals approved |
| **4 — Build** | `phase-4-build.md` | Course settings, outline, objectives, tracking, spec snippets for the key interactions, MCP tool sequence | `lint_course` has no errors; preview reviewed |
| **5 — QA & delivery** | `phase-5-qa-and-delivery.md` | Module-specific test cases, LMS test, pilot, sign-off, maintenance triggers | `validate_package` passes, SCORM Cloud / LMS test passes, SME sign-off recorded |

Shared rules that apply to every phase live in [`00_program/`](00_program/):

- [`00_program/brand/brand-identity.md`](00_program/brand/brand-identity.md) — **My Clinic brand identity**: logo files and rules, colours, font, icons, illustration style, AI image prompt template, screen layouts L1–L6 with mockups
- [`00_program/brand-and-theme.md`](00_program/brand-and-theme.md) — brand summary, theme decision, Arabic/RTL plan
- [`00_program/characters/companions.md`](00_program/characters/companions.md) — **the two course companions, Noor and Dr. Omar**: character bible, poses and AI prompts, placement on screens, voices and script rules, per-module plan
- [`00_program/scorm-structure.md`](00_program/scorm-structure.md) — **structure of the SCORM packages**: LMS learning path, zip contents, manifest, course outline model, tracking data, versioning
- [`00_program/programme-status.md`](00_program/programme-status.md) — what is done, gaps, proposal check, next steps
- [`00_program/asset-template-audit.md`](00_program/asset-template-audit.md) — evidence-based inventory of brand files, companion art, module assets, Word renderings and card templates (regenerate with `tools/audit_assets.py`)
- [`00_program/next-phases-roadmap.md`](00_program/next-phases-roadmap.md) — the remaining work cut into PR-sized chunks with acceptance criteria
- [`00_program/decision-sheet.md`](00_program/decision-sheet.md) — **every open decision in one list** (generated): id, owner role, due date, write-back file. Tier 1 = 28 safety/PHI/incident rows (due 2026-10-22), tier 3 = D9/D10/D11 (2026-10-26), tier 2 = 71 module facts (2026-10-30). Regenerate with `tools/build_decision_sheet.py`
- [`00_program/kickoff-pack.md`](00_program/kickoff-pack.md) — **Phase 0 kick-off pack `MC-KO-01 v0.1`**: 90-minute run sheet, who must be in the room and which decisions they own, pre-reads, the same-day write-back procedure; rendered to [`kickoff-pack.docx`](00_program/kickoff-pack.docx) for the client
- [`00_program/build-pipeline.md`](00_program/build-pipeline.md) — exact edumints tool sequence, SCORM settings, naming, file layout, known server limits
- [`00_program/narration-and-lexicon.md`](00_program/narration-and-lexicon.md) — voice, pace, writing rules, master pronunciation lexicon
- [`00_program/narration-production-plan.md`](00_program/narration-production-plan.md) — production workflow and copy-ready external audio-agent handoff; final voices remain blocked by D10
- [`00_program/visual-production-plan.md`](00_program/visual-production-plan.md) and [`00_program/visual-generation-prompts.md`](00_program/visual-generation-prompts.md) — character-aware visual handoff, image prompts, pending assets and optional video prompt
- [`00_program/visual-and-motion-agent-brief.md`](00_program/visual-and-motion-agent-brief.md) — recommended cast, minimal asset list, video-count decision, HyperFrames/Remotion choice and copy-ready image/audio/motion-agent instructions
- [`00_program/scenario-design-plan.md`](00_program/scenario-design-plan.md) and [`00_program/gamification-plan.md`](00_program/gamification-plan.md) — proposal-aligned scenario inventory, game mechanics, retries, scoring and accessibility
- [`00_program/client-context.md`](00_program/client-context.md) — researched public context for My Clinic KSA, with current website discrepancies and approval cautions
- [`00_program/plan-audit.md`](00_program/plan-audit.md) — proposal-to-plan verdict, current test results and remaining release blockers
- [`00_program/course-templates/`](00_program/course-templates/) — blank production worksheet plus one prefilled handoff template for each of the eight SCORM packages
- [`00_program/qa-checklist.md`](00_program/qa-checklist.md) — common QA checklist and sign-off record
- [`00_program/cross-module-decisions.md`](00_program/cross-module-decisions.md) — decisions that affect several modules (emergency codes, Code Orange threshold, branch names, regulator name, personal data)
- [`00_program/storyboard-template/`](00_program/storyboard-template/) — full storyboard template, screen-type guide, worked examples and review checklist for the agent that writes each module's screen-by-screen storyboard

---

## 3. Master timeline (follows the proposal)

The phases and weeks match the proposal (`../proposal/`, Project Phases). Week 1 starts at the kick-off meeting. Courses are staggered so SME reviews are spread out; build order **03 → 07 → 01 → 02 → 04 → 05 → 06 → 08**.

| Weeks | Phase | L2S | My Clinic |
|---|---|---|---|
| 1–2 | 0 — Kick-off & source lock | Walk SMEs through the v0.2 storyboard pack and review register | Close B-items and D1–D14; confirm LMS + SCORM version (D9), brand (D11) |
| 2 | 1 — Action map | Final objectives and evidence map (already drafted) | Approve objectives |
| 3–4 | 2 — Storyboards | Apply Phase 0 decisions; retrofit 03 and complete 07 (status G1–G2); close the 52 register rows | Approve storyboards (**30% payment**) |
| 4–6 | 3 — Narration & media | Two companion voices (D10), audio, captions, images, companion PNGs, EHR test captures | Approve voices and visuals |
| 5–7 | 4 — Build | Build 8 packages per `scorm-structure.md`; `lint_course`; previews | Preview review |
| 7–9 | 5 — QA, LMS, pilot | 81 test cases, SCORM Cloud, LMS test, pilot | Pilot learners, sign-off |
| 9–10 | Delivery | Final packages, sources, admin guide | Launch (**final payment**) |

## 4. What blocks everything (top 6)

These are the items from `../README.md` §3 that stop more than one package. Details and owners are in [`00_program/cross-module-decisions.md`](00_program/cross-module-decisions.md).

1. **Patient identifiers in `IT.mp4`** (module 08). The video must not be used in any package. Module 08 is planned around new screenshots of a test patient.
2. **Code Orange threshold** (modules 01, 02). One rule is needed: recommended *≥ 500 mL or any highly toxic/reactive/explosive substance*.
3. **Emergency code sheet and extensions** (modules 01, 02). One naming set and the real extension numbers (the decks show "5555" as a placeholder).
4. **Regulator name: CCHI vs CHI** (modules 05, 06).
5. **NotebookLM watermark / licence** on the Quality video (module 07). The plan rebuilds the content natively, so the video is optional.
6. **Brand kit** (all). The logo, colours and font are now taken from My Clinic's own decks (`00_program/brand/`); Marketing confirms them (D11).

---

## 5. How to use these plans with Claude + edumints

1. Connect the MCP client to the edumints server (hosted `https://scorm.edumints.com/mcp` or self-hosted Docker).
2. Open the module folder. Close Phase 0 with the SMEs.
3. Ask Claude to run Phase 1–3 for that module, using the plan file as the brief. Claude calls `get_playbook`, `lint_visual_plan`, `lint_narration_script` and `lint_authoring_plan`, and **stops for your approval** at the end of Phase 3.
   - **Phase 2b is a separate run.** Once the screen list is approved, point Claude at
     `00_program/storyboard-template/README.md` and ask for `storyboard/storyboard.md`. One module
     per run. Claude fills every field of every card and leaves nothing in `<angle brackets>`
     except `<hr-…>` asset placeholders.
4. Phase 4: Claude builds with `create_project` / `add_screen` (or `build_from_spec`), using `language: "en"` (the server default is Turkish).
5. Phase 5: run the QA checklist, test in SCORM Cloud and your LMS, and record sign-off.
