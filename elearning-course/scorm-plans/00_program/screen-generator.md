# Local branded screen generator

**Status: draft review renderer, not Phase 4/SCORM delivery.** It converts existing
storyboard JSON into browser screens without inventing missing content or claiming
SME approval. It does not use the edumints server, package SCORM, record LMS data,
calculate a final course score, implement cue timing, or certify accessibility.

## Generate and review

From the repository root, with Python 3.10+ (no extra Python dependencies):

```bash
# All eight modules
python3 elearning-course/scorm-plans/tools/generate_screens.py

# Or select modules, using their exact folder names
python3 elearning-course/scorm-plans/tools/generate_screens.py \
  03_hr-employee-induction 07_quality-safety-and-risk

# Serve only the generated output, never the source/media repository
python3 -m http.server 8000 --bind 0.0.0.0 --directory .generated/screens
```

The output is `.generated/screens/index.html`, `player.js`, `scenario.js`, `style.css`, copied review
assets and `generation-report.json`. It also opens directly as a local file: course data
is embedded as inert JSON, so no fetch, CDN, external font service or build step is needed.
The preview contains internal course content; only share through authorised review channels.

The output directory is ignored by Git. Rebuild after approved storyboard changes.
Regeneration replaces generated files but does not prune obsolete assets; use a fresh
`--out` directory when changing the asset map or producing a client review copy. In-repo
output is restricted to `.generated/` to prevent overwriting authoring sources.

Every screen retains its permanent ID and input order. Module selection, searchable outline,
Previous/Next and hash links support review. For example:

```text
#03_hr-employee-induction/hr-001
#07_quality-safety-and-risk/qsr-032
```

Transcript, evidence links, planned points, objective IDs, visual concept, notes and source
JSON remain inspectable. Choices are held **in memory only** while navigating screens;
reload clears them. No learner data is stored or transmitted. Audio is optional and manual;
there is no narration autoplay or assumed cue timing.

## Rendering contract

Inputs: each selected module's `storyboard/storyboard.md` (JSON build blocks),
`visual-plan.json` (review briefs and module title), `narration-script.json` (transcript
fallback), plus `00_program/brand/brand-kit.json` and supplied brand PNGs.

- **Rendered draft:** authored content and common interactions rendered as real HTML.
  Content/summary, title, tabs, accordion, flashcards, timeline and worked-example displays;
  MCQ, true/false, poll, fill-blank, matching and categorisation answer checks. Matching and
  drag/drop use keyboard-accessible selects, not pointer-only dragging. Results displays
  show authored objective advice, **not a computed score**. Decision scenarios now play
  one decision at a time, lock the choice while feedback is reviewed, follow the exact
  authored target, and show a draft-only sum of authored score deltas. Reset starts a new
  in-memory run. No course points, pass or completion is awarded. Missing targets, feedback,
  scores, cyclic graphs or unreachable nodes remain build issues, not inferred wiring.
- **Interaction review:** structured authored steps/nodes/options for
  adaptive practice, games, escape rooms, simulations, hotspots, labelled diagrams,
  image comparisons and sorting. Their production algorithms, geometry and scoring are
  deliberately not implemented. Source JSON is always available; this is not an upstream
  screen-model or interaction-equivalence claim.
- **Build detail pending:** skeleton JSON, missing required fields or incomplete answer
  keys produce a labelled visual brief. The generator never derives an answer key, target,
  policy, branch or assessment from prose. In particular, the unapproved risk band on
  `qsr-032` cannot be checked as a correct answer.

On the **2026-10-14 checkout**, generation confirms **207 screens / 95 scored screens**:
**44 rendered drafts, 9 interaction reviews, 154 brief-only screens**. Six modules have
review-hand-off skeletons rather than full build content. All 207 have at least one unresolved
review/build issue (including missing audio). These counts describe renderer coverage,
not approval or readiness. All existing Phase 0, SME, voice, DPO and asset gates still apply.

## Branding and assets

Navy/light logo variants are copied unchanged; module colour comes from the brand kit.
Title screens use the supplied navy background and petal motif; body/question screens do
not watermark text. CSS uses Montserrat with local Arial fallback. It does not bundle an
unapproved font, substitute generated logos, generate character art, or copy patient-bearing
video frames. Companion art/placements recorded only in prose stay explicitly pending.
Existing own SVGs under `storyboard/assets/` may be copied for review; only actual matching
asset IDs are resolved. Placeholder assets are visible, including their IDs and alt text.

Supply **trusted, authorised review files** with an explicit JSON asset map:

```json
{
  "char-omar-explaining": "approved-art/char-omar-explaining.png",
  "hr-aud-001": "approved-audio/hr-aud-001.mp3"
}
```

```bash
python3 elearning-course/scorm-plans/tools/generate_screens.py \
  03_hr-employee-induction --asset-map /path/to/review-assets.json
```

Filenames resolve relative to the map. Assets are copied, not linked to arbitrary remote URLs.
Mapped PNG/JPEG/WebP/SVG images and MP3/WAV/OGG narration can display/play in supported slots.
Other accepted local media (MP4/PDF) are copied for later wiring; this renderer does not supply
video or download interactions. A map **does not confer consent, DPO clearance, licensing or
provenance**. Do not use untrusted SVGs or identifiable patient captures.

## Validation and reports

```bash
python3 -m unittest discover -s elearning-course/scorm-plans/tools/tests -v
node --check elearning-course/scorm-plans/tools/screen_generator/player.js
node --check elearning-course/scorm-plans/tools/screen_generator/scenario.js
# Requires the all-module generated preview above:
node elearning-course/scorm-plans/tools/tests/test_scenario.cjs
python3 elearning-course/scorm-plans/tools/lint_planning.py
```

Eight Python unit tests cover the current 207/95 totals, preserved IDs/order/scoring/evidence,
deterministic output, invalid JSON/duplicate IDs/unknown types, inert HTML, pending answer
keys, asset maps, source-directory protection and scenario graph validation. The Node state
gate traverses **189 authored paths** across `hr-031`, `hr-044`, `qsr-021` and `qsr-051`,
checking exact feedback, target transitions, score-delta totals and reset. It also tests
invalid graphs, double-choice/advance guards, early exits and snapshot isolation. Invalid inputs exit nonzero; unresolved
build detail is reported, not treated as a generation failure or production approval.

`generation-report.json` records `production_ready: false`, render-mode counts, module
source hashes, missing fields and unresolved assets per screen. This is a local generator
report, not an edumints lint result. Upstream production lint and preview are still required.

Optional browser smoke gate (install Playwright separately and provide a working Chromium):

```bash
PLAYWRIGHT_MODULE=/absolute/path/to/node_modules/playwright \
CHROMIUM_EXECUTABLE=/absolute/path/to/chromium \
PREVIEW_URL=http://127.0.0.1:8000 \
node elearning-course/scorm-plans/tools/tests/screen_preview_smoke.cjs
```

The loop visits all 207 screens, checks title/ID navigation, tests MCQ, matching and fill-blank
feedback, tabs, in-memory state, keyboard scenario choices/feedback/continue/reset, pending
policy markers and answer keys, simulation disclaimers, screen search and
390px horizontal overflow, and fails on browser errors or missing HTTP assets. It passed
locally with headless Chromium. This is a smoke check, **not** the 81-case delivery QA suite,
a visual-approval pass, an LMS test, a pilot or a full accessibility audit.

## Remaining production work

Close relevant SME/Phase 0 decisions; replace skeleton blocks with validated upstream screen
schemas; provide authorised full-size companion art and audio; wire production interactions,
media, cue timing and companion placement; rerun upstream lints; obtain human approval; then
build with edumints, validate SCORM, test resume/scoring in the actual LMS and run the pilot.
Nothing in this generator changes commercial scope or adds generated video.
