# Draft SCORM builds (v0.1-draft)

![My Clinic logo](brand/logo-preview.png)

> Built **2026-10-15**, rebuilt the same day with the full-size companion art, with the real edumints compiler (`4bbf459`) in-process — see [`build-pipeline.md`](build-pipeline.md) §6. These are **drafts for review and LMS smoke tests, not release builds**: every value tied to an open Phase 0 decision is shown as `⚠ Draft — pending <ID>`, media that is not produced yet is a branded PENDING card, and there is no narration audio until D10 (captions only).

<!-- builds:start -->
| Module | SCORM | Screens | Scored | lint errors | lint warnings | validate | Package | KB | Pending media | Companions placed | Explore-hotspot rules |
|---|---|---:|---:|---:|---|---|---|---:|---:|---:|---:|
| [01](../01_health-and-safety-1/build/) | 1.2 | 54 | 24 | 0 | `free_hints`, `too_many_list_items`, `text_only_run`×5, `visual_poverty`, `scored_over_objectives` | ok* | [`MC_01_FMS_v0.1-draft_1.2.zip`](../01_health-and-safety-1/build/MC_01_FMS_v0.1-draft_1.2.zip) | 2331 | 4 | 7 | 22 |
| [02](../02_health-and-safety-2/build/) | 1.2 | 26 | 13 | 0 | `free_hints`, `text_only_run`, `visual_poverty`, `unbound_scored_question`, `scored_over_objectives` | ok* | [`MC_02_SafetyLab_v0.1-draft_1.2.zip`](../02_health-and-safety-2/build/MC_02_SafetyLab_v0.1-draft_1.2.zip) | 3264 | 9 | 4 | 11 |
| [03](../03_hr-employee-induction/build/) | 1.2 | 36 | 15 | 0 | `scored_over_objectives` | ok* | [`MC_03_WelcomeOnBoard_v0.1-draft_1.2.zip`](../03_hr-employee-induction/build/MC_03_WelcomeOnBoard_v0.1-draft_1.2.zip) | 1205 | 23 | 3 | 7 |
| [04](../04_operations-and-my-care/build/) | 1.2 | 13 | 4 | 0 | — | ok* | [`MC_04_OpsMyCare_v0.1-draft_1.2.zip`](../04_operations-and-my-care/build/MC_04_OpsMyCare_v0.1-draft_1.2.zip) | 2474 | 4 | 3 | 6 |
| [05](../05_rcm-documentation-and-coding/build/) | 1.2 | 21 | 10 | 0 | `free_hints`, `too_many_list_items`, `text_only_run`, `visual_poverty`, `scored_over_objectives` | ok* | [`MC_05_RCM-A_v0.1-draft_1.2.zip`](../05_rcm-documentation-and-coding/build/MC_05_RCM-A_v0.1-draft_1.2.zip) | 518 | 0 | 3 | 0 |
| [06](../06_rcm-ebp-benefits-and-rejections/build/) | 1.2 | 15 | 7 | 0 | `scored_over_objectives` | ok* | [`MC_06_RCM-B_v0.1-draft_1.2.zip`](../06_rcm-ebp-benefits-and-rejections/build/MC_06_RCM-B_v0.1-draft_1.2.zip) | 704 | 0 | 3 | 0 |
| [07](../07_quality-safety-and-risk/build/) | 1.2 | 22 | 11 | 0 | `text_only_run`, `scored_over_objectives` | ok* | [`MC_07_ClinicalGov_v0.1-draft_1.2.zip`](../07_quality-safety-and-risk/build/MC_07_ClinicalGov_v0.1-draft_1.2.zip) | 806 | 2 | 3 | 6 |
| [08](../08_it-ehr-consultation/build/) | 1.2 | 20 | 11 | 0 | `too_many_list_items`, `scored_over_objectives` | ok* | [`MC_08_EHR_v0.1-draft_1.2.zip`](../08_it-ehr-consultation/build/MC_08_EHR_v0.1-draft_1.2.zip) | 702 | 31 | 3 | 6 |
<!-- builds:end -->

\* These build reports were produced offline, so they carry the `schema_unavailable` warning: structural checks only. The XSD check has since been run separately with an offline schema directory (`SCORM_SCHEMA_DIR`) — **all eight manifests validate with 0 errors and 0 warnings** ([`xsd-validation.md`](xsd-validation.md)). Rerun `validate_package` with the authentic SCORM 1.2 root schema before a release build.

Each module folder `build/` holds `course-spec.json` (what was compiled), `asset-map.json` (every asset and whether it is a file or PENDING), `build-report.json` (compiler output verbatim), `preview.html` (open in a browser) and the zip. Modules 01, 02, 04, 05, 06 and 08 also hold `screens.json`: the production screens written from the storyboard cards (03 and 07 build straight from their storyboard blocks).

## Lint warnings explained

| Code | Meaning | Action |
|---|---|---|
| `scored_over_objectives` | More scored screens than objectives + 1 (all eight) | Structural, from the approved storyboards. Either accept (compliance courses with section checks) with a one-line rationale at SME sign-off, or merge checks. |
| `text_only_run`, `visual_poverty` | Runs of screens with no teaching visual (01, 02, 05, 07) | Planned asset lists add none there. Candidates for icons or simple SVGs in Phase 3. |
| `free_hints` | Game hints cost nothing (01 capstone, 02 drill, 05 capstone) | Cards specify free hints; decide at SME review. |
| `too_many_list_items` | More than 4 bullets (01, 05, 08) | Cards require these checklists; keep or split. |
| `unbound_scored_question` | 02 `hs2-031` asks about evacuation tools not taught before it | Real content gap: add a short teaching screen or move the question. |

## Fixed in this pass

- **NFPA 704 diagrams were wrong** (`hs1-img-nfpa-blank`, `hs1-img-nfpa-301w`, `hs2-img-nfpa-230`): the quadrants were rotated (blue at the top) and the numbers sat on the wrong colours. Redrawn to the standard layout — red flammability top, blue health left, yellow instability/reactivity right, white special bottom — and the blank diagram no longer prints the answers. `hs1-503` markers re-placed.
- **Explore hotspots did not work in the edumints player**: `bindHotspot` returns before positioning regions in explore mode, so every region stacked in a corner. `build_course_spec.py` now writes each region's position as CSS percentages (verified on the 01 corridor). Report the bug upstream and remove the workaround once fixed.

- **Title-slide subline** (e.g. 07 "MODULE 07 · CARING") was dark text on navy; the skin now sets it in mist capitals.
- **One build route.** `tools/build_scorm_packages.py` (03 + 07 only, writes to the ignored `.generated/`, no `lint_course`, no brand skin, no hotspot fix) is **superseded** by `build_course_spec.py` + `edumints_build.py`, which build all eight with the `lint_course` gate. Keep it only as a reference; do not use it for review packages.

Refresh the table above after any rebuild with `python3 elearning-course/scorm-plans/tools/draft_builds_report.py`.

- **SCORM 1.2 for all eight** (2026-10-19): 01 and 03 rebuilt from 2004 4th Ed. to 1.2 for Oracle Learning ([`oracle-learning-compatibility.md`](oracle-learning-compatibility.md)).
- **Percent display** ("%75" → "75%") patched in each package's player at build time (`player_patches: 2` in every report; G18).
- **Brand weave** on every screen: ~6% petal mark in the card corner and a navy + module-colour top band (owner decision 2026-10-19).

## Still open (do before v1.0)

1. **Narration scripts**: in the six generated packs, many question/simulation screens carry generic filler narration ("The next choice asks you to apply the rule…"). Rewrite before any voice work (D10).
2. **Schema limits** recorded in each `screens.json` `notes`: no per-card feedback on drag/sort, no per-choice companion reaction, no media on mcq/matching/escape-room, one hint ladder per game.
3. **Companion art**: ✅ all eight packages now embed the full-size transparent PNGs from `characters/assets/`, downscaled at build time (poses ≤ 520×700, avatars ≤ 256 px) so packages stay small.
4. **Pending media and captures**: see each `asset-map.json`; EHR (31) and Oracle (5) screenshots need the approved test environments.
5. **Phase 0**: every `⚠ Draft — pending` closes with its decision; rebuild with the two tools.
6. **Content gap** `hs2-031` (evacuation tools asked before they are taught).
7. **Upstream engine bug**: report the explore-hotspot positioning bug to edumints-scorm-mcp, then drop the CSS workaround.
8. **XSD validation**: ✅ run 2026-10-15 for all eight with an offline schema directory — 0 errors, 0 warnings ([`xsd-validation.md`](xsd-validation.md)). Still to do: rerun with the authentic SCORM 1.2 root schema, then the SCORM Cloud smoke test and the client LMS (D9).
