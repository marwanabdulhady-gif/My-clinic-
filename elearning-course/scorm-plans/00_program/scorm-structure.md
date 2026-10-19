# SCORM structure — the whole programme

![My Clinic logo](brand/logo-preview.png)

This is the structure of the eight SCORM packages: how they sit in the LMS, what is inside each zip, how the manifest is built, how a course is organised from outline to screen, and what the LMS receives. It is taken from how the edumints compiler actually packages a course (`core/packager.py`, `core/manifest.py`, revision `4bbf459`), not from a generic SCORM template.

Each module has its own generated file, `<module>/scorm-structure.md`, with its outline, every screen, the objectives and the tracking. Regenerate them after any approved storyboard change:

```bash
python3 elearning-course/scorm-plans/tools/build_scorm_structure.py
```

---

## 1. Level 1 — the programme in the LMS

Six commercial courses (the proposal) = **eight SCORM packages**. Each package is a separate LMS activity, so each has its own completion, score and objectives record.

| LMS course (proposal) | Package | File (v1.0) | SCORM | Screens | Scored | Points | Pass | Seat time | Completion |
|---|---|---|---|---:|---:|---:|---|---|---|
| 1 HSE | 01 Facility Management & Safety | `MC_01_FMS_v1.0_1.2.zip` | 1.2 | 54 | 24 | 220 | 80% (176) | ~55 min | viewed all + passed |
| 1 HSE | 02 Safety in Practice Lab | `MC_02_SafetyLab_v1.0_1.2.zip` | 1.2 | 26 | 13 | 145 | 80% (116) | ~33 min | viewed all + passed |
| 2 HR | 03 Welcome On Board | `MC_03_WelcomeOnBoard_v1.0_1.2.zip` | 1.2 | 36 | 15 | 145 | 70% (102) | ~45 min | viewed all + passed |
| 3 Operations | 04 Who Does What | `MC_04_OpsMyCare_v1.0_1.2.zip` | 1.2 | 13 | 4 | 50 | 70% (35) | ~15 min | viewed all + passed |
| 4 RCM | 05 RCM Part A | `MC_05_RCM-A_v1.0_1.2.zip` | 1.2 | 21 | 10 | 100 | 80% (80) | ~25 min | viewed all + passed |
| 4 RCM | 06 RCM Part B | `MC_06_RCM-B_v1.0_1.2.zip` | 1.2 | 15 | 7 | 80 | 80% (64) | ~20 min | viewed all + passed |
| 5 Quality | 07 Clinical Governance | `MC_07_ClinicalGov_v1.0_1.2.zip` | 1.2 | 22 | 11 | 95 | 80% (76) | ~25 min | viewed all + passed |
| 6 IT | 08 EHR Consultation | `MC_08_EHR_v1.0_1.2.zip` | 1.2 | 20 | 11 | 90 | 80% (72) | ~25 min | viewed all + passed |
| | **Total** | | | **207** | **95** | | | **~4 h** | |

Optional screens are not counted: `qsr-060` (in-house speak-up video) and `ehr-060` (re-recorded walkthrough). Adding either adds one unscored screen and one video asset.

### Learning path and LMS set-up

```text
Induction curriculum (LMS learning path)
├── 1. 03 Welcome On Board            all new employees · day 1
├── 2. 07 Clinical Governance         clinical staff (recommended for all)
├── 3. 01 Facility Management & Safety  all new staff
├── 4. 02 Safety in Practice Lab        all new staff · prerequisite 01
├── 5. 04 Who Does What               front-line, PX, clinical
├── 6. 05 RCM Part A                  physicians, dentists
├── 7. 06 RCM Part B                  physicians, RCM staff · recommended after 05
└── 8. 08 EHR Consultation            physicians, clinical · recommended after 05
```

- **Prerequisites are set in the LMS**, not in the packages: each package is a single SCO and cannot see another package's result.
- **Audience rules** (who is assigned what) are LMS enrolment rules. Suggested groups: *All staff* (03, 01, 02, 04), *Clinical* (+07, 08), *Physicians/dentists* (+05, 06), *RCM staff* (06).
- **Attempts and retakes** are LMS settings (the compiler has no attempt limit). Suggested: unlimited attempts, keep the highest score.
- **Attestation (D14):** if My Clinic needs a signed acknowledgement, add it as an LMS step after 01 and 03.

---

## 2. Level 2 — inside one package (the zip)

Every package has the same shape. The compiler writes exactly these files:

```text
MC_<NN>_<short>_v<major>.<minor>_<scorm>.zip
├── imsmanifest.xml          # manifest: metadata, 1 organization, 1 item, 1 SCO resource
├── index.html               # the whole course: player, theme, every screen (one page app)
├── runtime/
│   └── scorm-again.min.js   # SCORM API wrapper for 1.2 and 2004
├── runtime/…                # extra runtime files only if a screen needs them (e.g. Lottie)
└── assets/
    ├── <prefix>-img-*.svg|png   # diagrams, illustrations, test-patient screenshots
    ├── char-noor-*.png          # companion poses (shared programme set)
    ├── char-omar-*.png
    ├── brand logo PNGs, title background, petal watermark
    ├── <prefix>-aud-<screen>.mp3  # one narration file per narrated screen, normalised
    ├── <prefix>-vid-*.mp4 + .vtt  # only where a video screen is used
    ├── <prefix>-pdf-*.pdf         # job aids linked from the summary screen
    └── PROVENANCE.json          # media provenance records (written when present)
```

Rules:

- **One SCO per package.** The whole course is one launchable item; sections are an in-player menu, not separate SCOs. This keeps resume, scoring and objectives in one record.
- `assets/` names come from `add_asset` (`assets/<file name>`; a short random prefix is added only if a name collides). Keep the planned ids from the asset registers as file names so the asset map stays readable.
- The **companion art** is the same eight-pose set in every package (`characters/companions.md` §3). Only the poses a module uses are uploaded to that module.
- Built zips and media are **not** committed to Git; they are stored in Drive with the version number (`build-pipeline.md` §1).

---

## 3. Level 3 — the manifest

| Part | SCORM 1.2 packages (all eight, Oracle Learning target) | SCORM 2004 4th ed. (optional; not in Oracle's documented editions) |
|---|---|---|
| Identifier | `MANIFEST-<project_id>` | `MANIFEST-<project_id>` |
| Metadata | LOM: title, language `en`; description, keywords and learning time from `metadata` | same |
| Organization | `ORG-1` with one `ITEM-1` → `RES-1` | same |
| Pass mark | `<adlcp:masteryscore>` = passing score (70 or 80) | `<imsss:primaryObjective satisfiedByMeasure="true">` with `minNormalizedMeasure` 0.70 / 0.80 |
| Objectives | not in manifest (runtime only) | one `<imsss:objective objectiveID="…">` per objective that has at least one scored screen |
| Sequencing | none | none beyond objectives (single SCO) |
| Resource | `type="webcontent" adlcp:scormtype="sco" href="index.html"` + every file | `adlcp:scormType="sco"` + every file |

The manifest only writes a pass mark when the course has at least one scored screen. All eight packages do.

**SCORM version choice (2026-10-19).** All eight are SCORM 1.2 for Oracle Learning, which documents 1.2 and 2004 Editions 2–3 (the compiler writes 4th Edition). The 1.2 `suspend_data` limit is not a risk: worst case 749 bytes for 01 against 4,096. See [`oracle-learning-compatibility.md`](oracle-learning-compatibility.md).

---

## 4. Level 4 — inside the course (outline → section → screen)

```text
Course (project)
├── settings: title, language "en", layout "stage" 960×540, theme, tracking
├── objectives: <prefix>-o1 … <prefix>-oN        → reported to the LMS
├── outline (section menu, unlock_rule "free")
│   ├── <prefix>-sA  Section title   (objective)
│   │   ├── screen <prefix>-000  title_slide        (layout L1)
│   │   ├── screen <prefix>-001  content_slide      (L3)  narration · companion
│   │   └── screen <prefix>-0nn  mcq ★ points · objective_ids · feedback
│   ├── <prefix>-sB …
│   └── close: results_breakdown → summary (L6)
└── assets: images, audio, video, PDFs + provenance
```

| Element | Rule |
|---|---|
| Screen id | `<prefix>-<section><nn>`, permanent once built (`hs1-402`, `ehr-031`) |
| Section | each screen's `node_id` = its outline section; section ids `<prefix>-s<letter or number>` |
| Scored screen | `points` + `objective_ids`; feedback for right and wrong; replay cannot inflate the score |
| Results | every package ends with `results_breakdown` (by objective) then `summary` with `show_score` (04 ends on `summary` only) |
| Narration | one audio file per narrated screen; `narration_text` = captions/transcript with speaker names |
| Companions | Noor / Dr. Omar on ≤ 1 screen in 3, never over a question (`characters/companions.md`) |
| Layouts | L1 title · L2 section opener · L3 content · L4 question · L5 scenario · L6 results/close (`brand/brand-identity.md` §7) |

Prefixes: `hs1` 01 · `hs2` 02 · `hr` 03 · `ops` 04 · `rcma` 05 · `rcmb` 06 · `qsr` 07 · `ehr` 08.

---

## 5. Level 5 — what the LMS receives

| Report | SCORM 1.2 | SCORM 2004 |
|---|---|---|
| Completed | `cmi.core.lesson_status` = `completed` / `passed` / `failed` | `cmi.completion_status` |
| Passed | `lesson_status` = `passed` when score ≥ mastery score | `cmi.success_status` against `cmi.scaled_passing_score` |
| Score | `cmi.core.score.raw / max / min` | `cmi.score.raw / max / scaled` |
| Per objective | `cmi.objectives.n.id / score / status` | `cmi.objectives.n.id / score / success_status` |
| Per question | `cmi.interactions.n.*` (type, response, result, objective) | `cmi.interactions.n.*` |
| Resume | `cmi.suspend_data` (4,096 chars) + `lesson_location` | `cmi.suspend_data` (64,000 chars) + `location` |
| Time | `cmi.core.session_time` | `cmi.session_time` |

Completion rule for all eight is `viewed_all_and_passed`: the LMS shows *passed* only when every screen was viewed **and** the pass mark was reached. xAPI is off for release 1.

---

## 6. Versioning

- **Minor** (`v1.1`): text, media or feedback fixes. Replace the package in the same LMS activity; learner records are kept.
- **Major** (`v2.0`): any change to scored screens, points or objectives. Import as a new LMS activity, because old attempts no longer match.
- Screen and objective ids are never reused for different content.

---

## 7. Personalisation layer (on top of the storyboard structure)

The structure above is the client-reviewed storyboard: it stays fixed. Each package also has an **unscored** layer, `<module>/production/personalisation.json`, applied at build time by `tools/personalise.py` ([plan](personalisation-and-interactivity-plan.md)):

```text
Course
├── variables: role (text, default "all"), role_label (text, default "team member")
├── <prefix>-00x  branching  "Make it yours"  → set_vars role, role_label   (after the opening)
├── …storyboard screens…
│   ├── <tip>-<role>  accordion  visible_if role == <role>   (one per role group)
│   ├── <tip>-all     tabs       visible_if role == "all"
│   ├── <id>c         true_false / mcq, points 0               (quick checks)
│   └── <id>p         exploration (choice / prediction / slider), replayed on the close
└── close: summary with "As a {{role_label}}: …" (never hidden → "viewed all" still completes)
```

| Rule | Why |
|---|---|
| Only unscored screens are added or converted; the build stops otherwise | total points, objectives and pass marks stay as reviewed (`cmi.core.score` unchanged) |
| One role question per package | each package is its own SCO; SCORM 1.2 carries no role from the LMS |
| Role-specific content is unscored | the score total is fixed at build time and counts hidden screens |
| `suspend_data` grows by ~100 bytes (two short variables + choice ids) | still far under the 4,096-character SCORM 1.2 limit (G24) |

LMS learning paths by role (which packages each person is assigned) are Oracle Learning enrolment rules, listed in [`roles.json`](roles.json). They replace the four audience groups in §1 once D15 closes.
