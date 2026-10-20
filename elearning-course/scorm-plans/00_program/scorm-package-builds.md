# SCORM package builds — draft for 03 + 07 (pilot)

> **Update 2026-10-20: own player.** The edumints compiler is retired. Packages are now built with `tools/build_package.py` and played by our own SCORM 1.2 player (`tools/player/`, see its README). The browser check is `tools/check_packages.py`. Where this page names `edumints_build.py`, read `build_package.py`.

> **Superseded (2026-10-15).** The canonical build route is `tools/build_course_spec.py` + `tools/edumints_build.py`: all eight packages, brand skin, companions, the explore-hotspot fix and the `lint_course` gate, with results in [`draft-builds.md`](draft-builds.md). This file and `tools/build_scorm_packages.py` are kept as the record of the first 03/07 pilot only.

**Date:** 2026-10-15  
**Branch:** `arena/1ea38f88-my-clinic`  
**Tool:** `tools/build_scorm_packages.py` (uses `core/project.py` + `core/packager.py` from `edumints-scorm-mcp` `4bbf459`)  
**Status:** **Draft for review and LMS smoke-test — not production release**

> This is the first package-level build on this programme. The eight storyboards have been at
> `v0.2` with clean planning gates since `2026-10-14` (`lint_planning` 0e/0w, `audit_scorm_base` clean
> 207 screens / 95 scored / 26 scenarios). This pilot builds the two modules that are first in the
> learning path and have the fewest open checklist items.

---

## What was built

| Module | Title | SCORM | Screens | Scored | Points | Pass | Objectives | Outline | Assets (incl. dummies) | Zip | Size | Validate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 03 | My Clinic — Welcome On Board: My Clinic & HR Essentials | **2004** 4th ed. | 36 | 15 | 145 | 70% (102) | 6 | 10 | 36 (9 real SVG + 27 dummies/brand) | `03_hr-employee-induction_2004.zip` | 495 KB | `validate_project` OK · `validate_zip` OK |
| 07 | My Clinic — Clinical Governance: Quality, Patient Safety & Risk | **1.2** | 22 | 11 | 95 | 80% (76) | 5 | 7 | 7 (3 real SVG + 4 dummies/brand) | `07_quality-safety-and-risk_1.2.zip` | 421 KB | `validate_project` OK · `validate_zip` OK |

*Source of truth for each row: the storyboard JSON blocks in `<module>/storyboard/storyboard.md` (36 + 22 blocks, same ids/order/types/points as `phase-2-storyboard.md`), plus `phase-4-build.md` for course settings and `storyboard.md` header for objectives/outline. No screen was added, removed or reordered.*

**Zips are not committed to Git** (see `.gitignore` + `build-pipeline.md` §1: *“Built zips and media are not committed; store them in Drive with the version number.”*). They are in `.generated/scorm/` (reproducible; see *Reproduce* below) and are ready to upload to **SCORM Cloud / the target LMS** for smoke-testing:

```
.generated/scorm/
├── 03_hr-employee-induction_2004.zip
├── 03_hr-employee-induction_build-report.json
├── 07_quality-safety-and-risk_1.2.zip
├── 07_quality-safety-and-risk_build-report.json
└── scorm-build-summary.json
```

Also generated (ignored, review-only): `.generated/screens/` — 58-slide branded preview for the same two modules (`generate_screens.py --phase 1`), `generation-report.json` with input hashes and layout contract.

---

## Honest scope — what this draft *is* and *is not*

**Is:**

* A **validateable SCORM package** per the edumints compiler: `index.html` (player + theme + all 58 screens), `imsmanifest.xml` (1 organization / 1 item / 1 SCO, `adlcp:masteryscore` or `imsss:minNormalizedMeasure`), `runtime/scorm-again.min.js`, `assets/*`, and `PROVENANCE` only if media provenance exists. `validate_zip` exits 0 (no blocking errors) on both zips.
* **Content-faithful:** every storyboard block is present with its real `type`, `id`, `title`, `prompt_html`, `options`/`pairs`/`nodes`/`steps`, `points`, `objective_ids`, `evidence_screen_ids`, `feedback`, `outline`/`section`, and scoring. The 9 real 03 SVGs (`hr-img-*`) and 3 real 07 SVGs (`qsr-img-*`) are embedded; brand tiles/logos are embedded from `00_program/brand/assets/`.
* **Gated:** `lint_planning` 8/8 clean, `build_scorm_structure` fresh, `audit_scorm_base` clean (03 12/12, 07 11/12 — only thin-evidence remains), `audit_assets` clean, `validate_project` 0 errors on both builds.

**Is not:**

* **Not audio-complete** — narration `narration_asset_id` placeholders (`<hr-aud-*>`, `<qsr-aud-*>`) are stripped for this draft. D10 (voice provider / `voice_id`) is still `Open`; no TTS or human audio is bundled. The player shows no audio control beyond the transcript (`narration_text` remains in the storyboard, not in the package).
* **Not visually complete** — 27 of the 36 assets in 03 and ~4 in 07 are **dummy SVGs** that say *“Draft visual — Pending SME / DPO review — placeholder”*. The 03 combined 7C SVG is reused for six individual 7C icons; leader photos, Oracle screenshots, wristband photos and other sensitive visuals are placeholders per **B6 / D5 / D6**. See the `asset_map` in the build report for the real-vs-dummy list.
* **Not policy-approved** — 102 Phase 0 decisions (`decision-sheet.md`: 28 tier-1, 3 tier-3, 71 tier-2) and 52 `storyboard-review-register` rows are still `Open`. The packages carry `⚠ PENDING` in visible text where the source decision is not closed (e.g. `qsr-001` quote, `hr-020` branch names D3, `qsr-032` risk band B6). No threshold, code, branch name, band, or policy number was invented to make the package validate.
* **Not a conformance claim** — `validate_zip` checks package structure and manifest XSD, not LMS runtime. SCORM Cloud / LMS import, `lint_course` at `production`/`delivery`, cmi.* runtime probe and the 81-case QA plan (`phase-5-qa-and-delivery.md`) are still required (C18).
* **Not the other six packages** — 01/02/04/05/06/08 remain at storyboard level. Their builds are queued in `next-phases-roadmap.md` as C15–C17 and are blocked on the same open decisions.

---

## Reproduce

From the repository root, after cloning the edumints core once:

```bash
# 1. Clone the compiler core (if not at /tmp/edumints)
git clone --depth 1 https://github.com/marwanabdulhady-gif/edumints-scorm-mcp.git /tmp/edumints
pip install --break-system-packages pydantic python-ulid lxml jinja2 nh3 aiosqlite httpx  # + fastmcp if needed

# 2. Regenerate the planning gates (must be clean before any build)
python3 elearning-course/scorm-plans/tools/build_motion_spec.py
python3 elearning-course/scorm-plans/tools/lint_planning.py
python3 elearning-course/scorm-plans/tools/build_scorm_structure.py
python3 elearning-course/scorm-plans/tools/audit_scorm_base.py
python3 elearning-course/scorm-plans/tools/audit_assets.py

# 3. Build the draft SCORMs for the pilot (03+07)
python3 elearning-course/scorm-plans/tools/build_scorm_packages.py \
  03_hr-employee-induction 07_quality-safety-and-risk \
  --out .generated/scorm

# 4. (Optional) Build the branded review preview for the same phase
python3 elearning-course/scorm-plans/tools/generate_screens.py --phase 1 --out .generated/screens
python3 -m http.server 8000 --bind 0.0.0.0 --directory .generated/screens
# Preview at http://localhost:8000 (or https://{port}-{sandboxId}.e2b.app in Arena)

# 5. Verify (examples)
unzip -l .generated/scorm/03_hr-employee-induction_2004.zip
python3 -c "import zipfile; print(zipfile.ZipFile('.generated/scorm/07_quality-safety-and-risk_1.2.zip').read('imsmanifest.xml').decode()[:800])"
```

The build is **deterministic** for a given storyboard checkout: same screens, same assets, same `imsmanifest.xml`. The `data_dir` temp directory and `package token` change per run, but the zip payload (HTML + manifest + assets) is stable.

---

## Files changed in this PR

* **New:** `elearning-course/scorm-plans/tools/build_scorm_packages.py` — deterministic draft builder (stdlib + edumints core). Documented as draft; never invents policy text.
* **New:** `elearning-course/scorm-plans/00_program/scorm-package-builds.md` (this file) + `scorm-package-builds.json` — the committed build summary (points to the ignored zips).
* No storyboard, visual plan, narration, or phase file was hand-edited; `scorm-structure.md` and `scorm-base-audit.*` were regenerated via the existing tools and remain fresh.

---

## Next steps (in roadmap order)

1. **LMS smoke-test this pilot** — import the two zips to SCORM Cloud and the target LMS (D9) and run the C18 QA checklist (viewed_all_and_passed, cmi.* reporting, resume, per-objective scores). Record results in `phase-5-qa-and-delivery.md`.
2. **Close the 03/07 tier-1/2 decisions** that affect these packages (e.g. 03 B5/D3 branch names, B6/D5 personal data, GOSI rates B12; 07 B3–B9 IPSG/identifiers/bands, B1 transcript listen) and write them to the `Write back to` files, then regenerate `decision-sheet` + this build.
3. **Produce final media** for the placeholders (oracle captures from a test account per B8/D6, leader photos with consent per D5, wristband matrix art per B6) and replace the dummies.
4. **Close D10 voices** and bundle real audio (one `narration_asset_id` per narrated screen, normalized per `audio_export.py`).
5. Repeat the build for the remaining six packages in roadmap order: **C15** (01+02) → **C16** (04+05+06) → **C17** (08, after DPO test captures), then **C18** full QA.

No merged PR is a client approval or a launch sign-off; every `⚠ PENDING` remains a blocker until the named SME writes the decision to its source file.
