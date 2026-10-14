# Pre-kickoff slide drafting — batch 1 of 4

**14 October 2026 · v0.1 · internal review only.** Started on the owner's instruction
to generate slides from the **current content**, then refine after the kickoff.
These drafting batches are not the programme's formal Phase 0–5 exit gates.
No SME, Marketing, voice, asset, DPO or LMS decision has been closed by this work.

## Drafting sequence

The existing learning/build order stays **03 → 07 → 01 → 02 → 04 → 05 → 06 → 08**.
The machine-readable selection is [`draft-slide-phases.json`](draft-slide-phases.json).

| Draft batch | Packages | Core screens | State / next review |
|---|---|---:|---|
| **1 — Welcome & clinical governance** | **03 HR + 07 Quality** | **36 + 22 = 58** | **First browser-rendered draft and screenshot set generated**; review layout, wording, companions and pending policies |
| 2 — Health & safety | 01 FMS + 02 Safety Lab | 54 + 26 = 80 | **Generated and browser-captured for draft review**; all 80 remain brief-only, emergency numbers/thresholds/answer keys pending |
| 3 — Operations & revenue cycle | 04 Operations + 05 RCM A + 06 RCM B | 13 + 21 + 15 = 49 | **Generated and browser-captured for draft review**; all 49 remain brief-only, role/payer/policy details pending |
| 4 — EHR guided workflow | 08 EHR | 20 | **Owner-reported draft review complete**; 20 PNGs/checks reported, test-account captures/DPO clearance pending; output is not in this checkout for independent re-review |

All batches total **207** core screens. Optional screens are not silently added.
Later batches retain their current skeletal build blocks; rendering a brief is not
finishing its production interaction or obtaining an approved answer key.

## Essential inputs — now enforced, not just referenced in documentation

For each selected package the generator requires:

1. `storyboard/storyboard.md` — canonical IDs, order, type, wording, points, objectives,
   evidence, branches, feedback and current narration. No source card is rewritten.
2. `storyboard/visual-plan.json` — explicit **L1–L6** layout and visual/capture briefs.
3. `storyboard/narration-script.json` — current transcript fallback; final audio is not generated.
4. Every `phase-0-*` through `phase-5-*` plan. **Phase 1** objective/evidence mappings and
   **Phase 2** screen IDs/order/types/points are reconciled with the cards. The **Phase 3**
   table controls which companions appear and where. Source-lock/build/QA plans remain
   inspectable, with their approval gates still open.
5. The package's prefilled `course-templates/*-production-worksheet.md` and the universal
   `course-production-template.md`. Package identity, canonical links, required sections,
   counts, score totals, module colour and eight build/QA checkboxes are read. A mismatch
   is a review issue, not a value the generator silently repairs; a missing essential input
   stops generation.
6. The supplied brand kit, **all eight reference PNGs**, and **`mockups.html`**. Canvas,
   header/rule/footer, content/title/section/scenario and guide geometry is compiled into
   `layout-tokens.css` and recorded in `layout-contract.json`. This is not a claim that
   every inline mockup decoration is automatically compiled or that current content is
   pixel-identical to the sample screens.

`generation-report.json` records exact input paths/SHA256 hashes, alignment, current
worksheet gates, mode counts and unresolved assets. The studio exposes copies of the
required textual planning inputs under **Production worksheet & plan alignment**;
only the generated directory is served, never the source-media repository.

## First-batch result

- **58 IDs, original order, 26 scored drafts, 240 planned points** retained:
  HR **36 / 15 / 145**, Quality **22 / 11 / 95**.
- Coverage classifications: **48 rendered common drafts / 9 structured interaction
  reviews / 1 pending-answer-key brief**. Display diagrams now show the authored SVG and
  repeat the labels in readable HTML, but remain draft visual reviews. Native content
  blocks, worked-example artifacts and the optional-text reflection are now rendered
  rather than incorrectly treated as missing content. Consent-dependent leadership
  portraits/identifying captions stay withheld on screen under the source B6 gate.
- **61 real browser PNGs**: one initial capture per slide plus the Care-pillar feedback,
  Caring-tab and supplier-scenario feedback states. `review.html` includes an eight-screen
  overview, the eight reference→draft comparisons, all captures in original order and
  links back to the interactive studio.
- Captures use a **960px-wide canvas**, with a 540px minimum. Dense screens expand and
  are captured at full height instead of being cropped or shrinking body text. This is
  deliberately review-friendly; a post-kickoff density/pagination pass is still needed
  for production 16:9 delivery. Expandable details and alternate branches/states remain
  available in the interactive preview, not all simultaneously in a single PNG.
- Existing companion preview JPGs and interim avatar PNGs are placed from Phase 3.
  **They do not resolve the missing full-size production IDs or close G6.** Planned
  scene/capture images remain explicit placeholders; no new art is generated or approved.
- Licensed **Montserrat and Tajawal are bundled locally**, with upstream commit,
  checksums and both OFL texts in [`brand/fonts/`](brand/fonts/). This is an English draft,
  not an approved Arabic/RTL variant.

## Subsequent-batch results

- **Batch 2 — Health & Safety:** generated 80 slides in canonical order (module 01: 54; module 02: 26), retaining 37 planned scored screens. All **80/80 are brief-only**: 63 have missing build fields and 29 have unresolved asset references (these groups overlap). The engine did not supply emergency numbers, spill thresholds or missing answer keys. Browser capture produced **80 PNGs and 80 mobile checks**, with local fonts and no browser errors, missing requests or external requests. The offline review ZIP passed archive-integrity verification.
- **Batch 3 — Operations & Revenue Cycle:** generated 49 slides (module 04: 13; module 05: 21; module 06: 15), retaining 21 planned scored screens. All **49/49 are brief-only**: 41 have missing build fields and 18 have unresolved asset references. The engine did not infer reporting lines, payer limits, policy or rejection data. Browser capture produced **49 PNGs and 49 mobile checks**, with local fonts and no browser errors, missing requests or external requests. The offline review ZIP passed archive-integrity verification.
- Both batches used the current brand kit, all eight supplied mockup references, the HTML mockup geometry, package storyboards, Phase 0–5 plans and required worksheets. Capture was rerun under Node 22.17. Output remains in ignored `.generated/slides/phase-2/` and `phase-3/`; galleries, captures and ZIPs are review artefacts, not committed sources or SCORM packages.
- **Batch 4 — EHR:** the owner reports 20 brief-only screens, 20 real browser captures/mobile checks and a verified offline ZIP. Those files were not present in this sandbox checkout, so that batch is recorded as owner-reported rather than independently reopened here. Test-account screenshots and DPO clearance remain pending as stated by the owner.

### Title-background correction discovered in the screenshots

The supplied `background-title-navy.png` contains a **centred logo**, not a blank
background as its earlier planning brief implied. Placing a title and another logo on
it created overlap and duplicate branding. Titles now use the **navy gradient defined
in `mockups.html`**, the unchanged white logo at the prescribed top-left position, and
the supplied petal mark. The original PNG is still copied as a reference asset; it is
not edited or redrawn. The deviation is recorded in `layout-contract.json`; Marketing
can confirm or replace it under **D11** after kickoff.

### Boundaries that remain unchanged

- `⚠ PENDING` wording/decision IDs stay visible. The pending `qsr-032` risk-band answer
  cannot be graded; no band, clinical rule, branch, reporting line or threshold is invented.
- The results layout shows **“NOT SCORED / NOT RUN”**, empty neutral bars and the current
  **planned** settings, not the mockup's sample 86% result, a pass or a completion record.
- No final narration/audio, SCORM zip, edumints project, LMS upload or production QA
  is produced. Native interaction equivalence, cue timing, final captions, privacy
  approval and full accessibility testing remain later work.
- No patient-bearing video, source-video frame, consent-restricted staff portrait or
  identifiable billing log is automatically imported.

## Reproduce and continue

From the repository root:

```bash
# Current first batch; Python 3.10+, standard library only.
python3 elearning-course/scorm-plans/tools/generate_screens.py --phase 1

# Serve only the generated preview (0.0.0.0 supports Arena's live preview).
python3 -m http.server 8000 --bind 0.0.0.0 --directory .generated/screens
```

Optional screenshot runtime (Node 22.17+, pinned npm packages; no browser CDN needed):

```bash
mkdir -p .generated/tooling
cp elearning-course/scorm-plans/tools/browser/package*.json .generated/tooling/
npm ci --prefix .generated/tooling --ignore-scripts
node elearning-course/scorm-plans/tools/browser/capture_slides.cjs \
  --url http://127.0.0.1:8000 --out .generated/screens

# Optional offline review archive (not SCORM):
python3 elearning-course/scorm-plans/tools/browser/pack_review.py --out .generated/screens
```

The URL above is **tool-side only**. All browser-facing links/fonts/assets use relative
URLs, including in Arena's proxied preview. A local Chromium can instead be supplied
with `CHROMIUM_EXECUTABLE`; Playwright can be supplied with `PLAYWRIGHT_MODULE`.
The runtime extracts NSS/NSPR from the npm binary's own bundled archive on minimal
Linux systems; no OS packages or system-file changes are needed.

For the next batch use `--phase 2 --out .generated/slides/phase-2`, then serve/capture
that output; repeat for `--phase 3` and `--phase 4`. Never mix `--phase` with explicit
module names. For a regression-only all-module preview, omit `--phase` and use a
separate ignored output folder.

Regeneration invalidates an old screenshot gallery if its report hash no longer
matches; rerun the capture tool before presenting that revision. Outputs/screenshots
and browser binaries stay in ignored `.generated/`, not Git or a release folder.

## Verification performed for this draft

- **27 repository Python tests** pass, including required templates/plans, real HTML
  geometry extraction, font checksum/licence handling, pending assets/keys, preservation
  of original IDs/scoring/evidence, deterministic generation and stale-capture invalidation.
- Node scenario gate: **189 authored paths across four scenarios**, exact feedback,
  transitions, score deltas, reset and invalid-graph/state guards.
- Browser regression: **207 screens**, draft checks, scenario keyboard flow, search,
  state across navigation, pending keys and 390px horizontal-overflow checks.
- First-batch capture gate: **58 slides / 61 PNGs / 58 mobile checks**, local font loading,
  canonical width, no missing requests, external requests or browser errors.
- All eight planning lints: **0 errors / 0 warnings** (local port, not upstream delivery lint).
- Asset/template audit: **0 hard failures**. Existing production blockers remain open.

These are smoke/planning checks, **not** client visual approval, full accessibility,
SCORM/LMS validation, the 81-case delivery suite or a pilot. Formal C14/C18 gates stay open.

## Post-kickoff write-back

Record owner decisions in the existing Phase 0/cross-module files; update approved
storyboard/plan/worksheet details together; run the normal planning gates; regenerate
this batch and recapture it. Keep screen IDs/scoring stable unless the approved plan
explicitly changes them. Review missing artwork and content density before moving from
this draft renderer to the production edumints build.

## Source reconciliation / conditional placements

- HR `hr-001`: Phase 2 screen-list worksheet says `full_media`; current build card,
  visual plan and Phase 3 say `text_media` / L3. Follow current card/Phase 3 for this
  draft, report **review-required**, and reconcile the source list before production.
- HR `hr-061`: the feedback avatar/tip belongs after the simulation. This is a
  structured review, not functional step tracking; the conditional tip remains
  withheld until proper final-step logic is implemented, never shown prematurely.
