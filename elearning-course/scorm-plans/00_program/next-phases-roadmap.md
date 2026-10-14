# Next phases — implementation roadmap in PR-sized chunks

![My Clinic logo](brand/logo-preview.png)

> Prepared **2026-10-14** from [`programme-status.md`](programme-status.md), the eight phase plans,
> the [SME/build-detail register](storyboard-review-register.md) and the
> [asset & template audit](asset-template-audit.md). Everything up to and including the v0.2
> storyboards is done; this file cuts **the remaining work** into chunks small enough to review as
> one pull request each.

**How to use it.** One chunk = one issue = one PR. A PR for a chunk must end with the chunk's exit
gate green (the commands are named in each chunk). Chunks that need a My Clinic decision say so up
front and stay blocked until the decision is written into the module's Phase 0 file or
[`cross-module-decisions.md`](cross-module-decisions.md). Nothing here authorises turning an open
source value into course content.

Standard exit-gate command chain after any content change:

```bash
python3 elearning-course/scorm-plans/tools/assemble_storyboard_docs.py <module…>   # generated packs
python3 elearning-course/scorm-plans/tools/normalise_narration.py                  # hand-authored packs (03, 07)
python3 elearning-course/scorm-plans/tools/lint_planning.py                        # must exit 0
python3 elearning-course/scorm-plans/tools/build_scorm_structure.py                # structure + summary
python3 elearning-course/scorm-plans/tools/export_storyboard_docx.py               # client Word pack
python3 elearning-course/scorm-plans/tools/build_decision_sheet.py                 # decision sheet (after any Phase 0 write-back)
python3 elearning-course/scorm-plans/tools/export_kickoff_docx.py                  # kick-off pack Word document
python3 elearning-course/scorm-plans/tools/audit_assets.py                         # must exit 0
```

`build_decision_sheet.py` reads the Phase 0 files and `cross-module-decisions.md` and lists only
**open** rows, so every decision written back removes itself from the sheet — the row count in the
kick-off pack is the programme's live blocker count.

---

## Chunk map

| # | Chunk | Unblocks | Depends on | Owner | Est. | Status |
|---|---|---|---|---|---|---|
| C0 | Tooling, audio schema, branded Word pack, audit | repeatable gates | — | agent | done | **PR #32** |
| C1 | Phase 0 decision sheet + kick-off pack | everything | — | L2S + My Clinic | done | **PR #33** · sheet ready, kick-off not yet booked |
| C2 | SME build-detail closure, modules 01–02 | 01–02 Phase 4 fields | C1 | Safety SME + L&D | 3 d | open |
| C3 | SME build-detail closure, modules 03–04 | 03–04 Phase 4 fields | C1 | HR/Ops SME + L&D | 2 d | open |
| C4 | SME build-detail closure, modules 05–06 | 05–06 Phase 4 fields | C1 | RCM SME + L&D | 3 d | open |
| C5 | SME build-detail closure, modules 07–08 (+07 poll/band/quote checks) | 07–08 Phase 4 fields | C1 | Quality/EHR SME + DPO | 3 d | open |
| C6 | Voice decision D10: samples, approval, voice ids | Phase 3 audio | C1 | course owner | 1 d | open |
| C7 | Companion full-size art (G6) + avatar replacement | Phase 3 visuals | — | Marwan (Canva) | 1 d | open |
| C8 | Brand confirmation D11 + theme/RTL addendum | Phase 4 theme | C1 | Marketing + L2S | 2 d | open |
| C9 | 08 test-environment captures + DPO review | 08 Phase 3/4 | C1 | IT + DPO | 2 d | open |
| C10 | Phase 3 media production, modules 03 + 07 (build order 1–2) | 03/07 build | C2–C9 as relevant | L2S | 4 d | open |
| C11 | Phase 3 media production, modules 01 + 02 | 01/02 build | C2, C6, C7 | L2S | 4 d | open |
| C12 | Phase 3 media production, modules 04–06 | 04–06 build | C3, C4, C6, C7 | L2S | 4 d | open |
| C13 | Phase 3 media production, module 08 | 08 build | C9 | L2S | 3 d | open |
| C14 | Phase 4 build + preview, modules 03 + 07 | 03/07 QA | C10 | L2S | 4 d | open |
| C15 | Phase 4 build + preview, modules 01 + 02 | 01/02 QA | C11 | L2S | 5 d | open |
| C16 | Phase 4 build + preview, modules 04–06 | 04–06 QA | C12 | L2S | 5 d | open |
| C17 | Phase 4 build + preview, module 08 | 08 QA | C13 | L2S | 3 d | open |
| C18 | Phase 5 QA, LMS test, pilot (81 cases) | launch | C14–C17, D9 | L2S + My Clinic | 6 d | open |
| C19 | Delivery pack: sources, admin guide, maintenance | final payment | C18 | L2S | 2 d | open |

Build order stays **03 → 07 → 01 → 02 → 04 → 05 → 06 → 08** (learning path and proposal staggering).

---

## C1 — Phase 0 decision sheet and kick-off pack — **shipped in PR #33** (2026-10-14)

**Goal:** one page that lists every open decision with a named owner and a due date, so the
kick-off meeting closes items instead of discovering them.

**What is in the repo now**

| Artefact | Contents | Regenerate with |
|---|---|---|
| [`decision-sheet.md`](decision-sheet.md) | **102 open rows** parsed from the eight `phase-0-source-lock.md` files, `cross-module-decisions.md` (D1–D14) and `scorm-structure-summary.json` (G4 thin objectives). Columns: ID, module(s), decision needed, recommended answer (draft), owner role, due date, write-back target, status. | `tools/build_decision_sheet.py` |
| [`decision-sheet.csv`](decision-sheet.csv) | The same rows, for the owner to fill in and return | same |
| [`kickoff-pack.md`](kickoff-pack.md) / [`kickoff-pack.docx`](kickoff-pack.docx) | **MC-KO-01 v0.1** — 90-minute run sheet, attendee-role→decision map, pre-reads, the same-day write-back procedure, what the room does *not* decide, then the decision sheet as an attachment | `tools/export_kickoff_docx.py` |

**Due dates the sheet proposes** (kick-off K = Monday **2026-10-19**):

- **2026-10-22 (K+3 wd)** — the **28 tier-1 rows**: Code Orange threshold, code names and extension
  numbers, radiation dose bands, laser classes, waste-bin colours, spill procedure, licence/ethics
  rules, incident-reporting wording, and the PHI/DPO items. Phase 3 media for those screens cannot
  start before these close.
- **2026-10-26 (K+5 wd)** — the **3 release-gating enablers**: D9 LMS/SCORM version, D10 voices,
  D11 brand. These gate C6, C8 and every Phase 4 build chunk.
- **2026-10-30 (end of week 2)** — the remaining **71 tier-2 module facts**: labels, codes, band
  names, policy numbers and screen wording.

**Still to do — owner actions, not agent work**

1. Book the kick-off for 2026-10-19 and send `kickoff-pack.docx` with the invite, plus the nine
   client-review Word files, `decision-sheet.csv` and proposal Rev01 (the pre-read list is §4 of the
   pack).
2. Run the meeting to the run sheet; each named owner confirms or replaces the recommended answer.
3. The same day, write every decision into the file named in its **Write back to** column and set
   the row to `Closed (date)`; rerun `build_decision_sheet.py` + `export_kickoff_docx.py` and the
   closed rows drop out of the sheet.

**Exit gate:** every row has owner + due date ✅ · `audit_assets.py` clean ✅ · pack sent ⬜ (owner,
step 1 above).
**Blocked by:** nothing — this is the chunk that unblocks the rest.

## C2–C5 — SME build-detail closure (52 register rows)

**Goal:** close the screen-level authoring questions in
[`storyboard-review-register.md`](storyboard-review-register.md) so Phase 4 has concrete options,
pairs, variants, feedback and pass/replay rules.

**Per chunk (module pair):** work the register rows for those modules with the named SME; write the
answers into Phase 2/Phase 4 and the cards; remove resolved `⚠ PENDING` markers only where the
owner's written decision exists; rerun the exit-gate chain; mark rows closed in the CSV.
Module 07 additionally closes the three checks from the v0.2 review: companion beside the unscored
poll (`qsr-002`), risk-matrix band names (B6) and the closing quote (B1).

**Two lists, one owner.** The [decision sheet](decision-sheet.md) rows for the pair (`01/*` + `02/*`
for C2, and so on) carry the *facts* the SME must confirm; the register rows carry the *build
detail* behind them. Run them in the same session, write both answers into the Phase 0/Phase 4
files, then rerun `build_decision_sheet.py` + `export_kickoff_docx.py` so the closed rows drop out
of the pack the client holds. The module 07 poll check is sheet row `07/P01`; its band names are
`07/B6` and its closing quote is `07/B1`.

**Exit gate:** register shows 0 open rows for the pair; `lint_planning.py` and `audit_assets.py`
exit 0; `scorm-structure.md` regenerated.

## C6 — Voices (D10)

**Goal:** two fixed, commercially licensed voices (Noor, Dr. Omar) with client-approved 30-second
samples; then real `voice_id`s in every pack.

**Steps:** shortlist providers; generate/record the "meet your guide" samples; client approval;
record provider + ids in [`narration-and-lexicon.md`](narration-and-lexicon.md) §1 and in each
`narration-script.json` → `voice` (via `tools/audio_export.py`, one change, eight packs).

**Exit gate:** ids present in all eight scripts; samples approved in writing; exports regenerated.

## C7 — Companion full-size art (G6)

**Goal:** the 18 full-size transparent PNGs in `characters/assets/`, replacing the interim crops.
The Canva media ids are tabulated in [`asset-template-audit.md`](asset-template-audit.md) §2.

**Exit gate:** `audit_assets.py` reports 18/18 full-size files and no interim placeholder in use;
visual boards show the full-size poses.

## C8 — Brand confirmation (D11) and theme/RTL

**Goal:** Marketing confirms logo usage, palette and Montserrat; decide whether release 1 ships an
Arabic/RTL variant. If yes, add a per-module RTL addendum (mirrored layouts L1–L6, Tajawal type
scale, caption direction) to each Phase 4 file.

**Exit gate:** D11 written in `cross-module-decisions.md`; `brand-kit.json` untouched or formally
versioned; RTL addenda present if approved.

## C9 — Module 08 test environment and captures

**Goal:** DPO-approved screenshots of a fictional test patient at 1920×1080 for the seven
simulations; the source video stays out of every package.

**Exit gate:** capture sheet (`ehr-capture-sheet`) satisfied per frame; DPO sign-off recorded;
assets in `08_…/storyboard/assets/` with PROVENANCE entries.

## C10–C13 — Phase 3 media production (per module group)

**Goal:** shipping narration audio (joined two-voice parts with 0.3 s silence, normalised), final
images from the recorded AI prompts or supplied/consented photos, captions/WebVTT, and
`PROVENANCE.json` per package.

**Exit gate:** `lint_narration_script` clean on the server; audio loudness-normalised; every asset
has provenance; `asset-template-audit.md` shows no planned-not-built asset left for the module.

## C14–C17 — Phase 4 build (per module group)

**C14 preparatory implementation started:** [local branded review tooling and scenario playback](c14-implementation.md).
This is a draft-preview slice, not a completed Phase 4 build; C10 and the production exit gate remain blocked.

**Goal:** one edumints project per package built exactly per its `scorm-structure.md`
(outline, objectives, points, tracking), `language: "en"`, `lint_course` clean, preview reviewed.

**Exit gate:** `lint_course` 0 errors; preview screenshots reviewed against
`screen-visuals.html`; SCORM settings match Phase 4 (version, completion rule, pass mark).

## C18 — Phase 5 QA, LMS and pilot

**Goal:** the 81 test cases per module Phase 5, SCORM Cloud run, real-LMS upload (needs D9), pilot
with 5–8 new starters, sign-off recorded in [`qa-checklist.md`](qa-checklist.md).

**Exit gate:** all cases pass; completion/pass/objective data verified in the LMS; pilot feedback
triaged; sign-off rows filled.

## C19 — Delivery pack

**Goal:** final zips in Drive (never Git), source export, admin guide (upload, versioning,
maintenance triggers), and the Rev01 → as-built reconciliation table.

**Exit gate:** delivery checklist in each Phase 5 file complete; final payment milestone met.

---

## Issue index (opened 2026-10-14)

C0 shipped as [PR #32](https://github.com/marwanabdulhady-gif/My-clinic-/pull/32) (merged);
C1 shipped as [PR #33](https://github.com/marwanabdulhady-gif/My-clinic-/pull/33).

| Chunk | Issue |
|---|---|
| C1 | [#13](https://github.com/marwanabdulhady-gif/My-clinic-/issues/13) |
| C2 | [#20](https://github.com/marwanabdulhady-gif/My-clinic-/issues/20) |
| C3 | [#21](https://github.com/marwanabdulhady-gif/My-clinic-/issues/21) |
| C4 | [#22](https://github.com/marwanabdulhady-gif/My-clinic-/issues/22) |
| C5 | [#23](https://github.com/marwanabdulhady-gif/My-clinic-/issues/23) |
| C6 | [#14](https://github.com/marwanabdulhady-gif/My-clinic-/issues/14) |
| C7 | [#15](https://github.com/marwanabdulhady-gif/My-clinic-/issues/15) |
| C8 | [#16](https://github.com/marwanabdulhady-gif/My-clinic-/issues/16) |
| C9 | [#17](https://github.com/marwanabdulhady-gif/My-clinic-/issues/17) |
| C10 | [#24](https://github.com/marwanabdulhady-gif/My-clinic-/issues/24) |
| C11 | [#25](https://github.com/marwanabdulhady-gif/My-clinic-/issues/25) |
| C12 | [#26](https://github.com/marwanabdulhady-gif/My-clinic-/issues/26) |
| C13 | [#27](https://github.com/marwanabdulhady-gif/My-clinic-/issues/27) |
| C14 | [#28](https://github.com/marwanabdulhady-gif/My-clinic-/issues/28) |
| C15 | [#29](https://github.com/marwanabdulhady-gif/My-clinic-/issues/29) |
| C16 | [#30](https://github.com/marwanabdulhady-gif/My-clinic-/issues/30) |
| C17 | [#31](https://github.com/marwanabdulhady-gif/My-clinic-/issues/31) |
| C18 | [#18](https://github.com/marwanabdulhady-gif/My-clinic-/issues/18) |
| C19 | [#19](https://github.com/marwanabdulhady-gif/My-clinic-/issues/19) |

## Issue and PR convention

- Issue title: `C<n> — <chunk name>`; body: the chunk section above plus the module list.
  (Issues #13–#31 are open. The `roadmap-chunk` label exists in the repository but the current
  integration token cannot attach labels, so the issue titles carry the chunk id instead.)
- PR title matches the issue; PR body links the issue and pastes the exit-gate output.
- A PR never mixes chunks: reviewable size is the point. If a chunk grows past ~400 changed lines
  of documentation, split it by module.
- Generated files (packs, reports, docx) are committed **with** the tool change that produced them,
  so every artefact in Git is reproducible from the repository.
