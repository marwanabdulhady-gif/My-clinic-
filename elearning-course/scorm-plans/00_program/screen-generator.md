# Local branded slide generator

**Status: current-content draft review, not Phase 4/SCORM delivery.** It renders the
existing cards without inventing missing content or treating them as approved policy.
It does not use the edumints server, package SCORM, record LMS data, award a final
course score/pass/completion, implement cue timing or certify accessibility.

The owner requested phased drafting before kickoff. See
[`draft-slide-production.md`](draft-slide-production.md) for the first **58-slide / 61-PNG**
batch, its eight mockup comparisons, verification and post-kickoff write-back procedure.

## Generate and review

Python 3.10+; standard library only. From the repository root:

```bash
# First drafting batch: 03 HR (36) + 07 Quality (22), in learning-path order.
python3 elearning-course/scorm-plans/tools/generate_screens.py --phase 1

# Later batches: --phase 2 (01/02), --phase 3 (04/05/06), --phase 4 (08).
# Use a separate output folder for each review revision/batch.
python3 elearning-course/scorm-plans/tools/generate_screens.py \
  --phase 2 --out .generated/slides/phase-2

# All eight, for regression or a combined review; no --phase means all.
python3 elearning-course/scorm-plans/tools/generate_screens.py \
  --out .generated/all-screens

# Or select exact module folder names (--phase and module names are mutually exclusive).
python3 elearning-course/scorm-plans/tools/generate_screens.py \
  03_hr-employee-induction 07_quality-safety-and-risk

# Serve ONLY generated output, never the source/media repository.
python3 -m http.server 8000 --bind 0.0.0.0 --directory .generated/screens
```

The output includes `index.html`, `player.js`, `scenario.js`, `style.css`,
`layout-tokens.css`, `layout-contract.json`, `generation-report.json`, local fonts,
review assets and copies of the required textual plans/worksheets. Embedded inert
JSON and relative URLs also support opening `index.html` offline; no CDN or build
step is needed. Only share this internal content through authorised review channels.

`.generated/` is ignored by Git. In-repo output is restricted to that directory to
protect authoring sources. Regeneration replaces generated files, but does not prune
obsolete assets; use a **fresh directory** when changing the asset map or distributing
a new review copy. A screenshot gallery whose generation-report hash no longer
matches is invalidated until the browser capture tool is rerun.

## Input and rendering contract

**Required inputs** are each selected package's storyboard JSON blocks, visual and
narration plans, **all six Phase 0–5 plans**, its **course production worksheet** and
the **universal production template**. Missing essential inputs stop generation.
The generator reconciles worksheet counts/scored screens/points, colour and canonical
input links; Phase 1 objective/evidence mappings; and Phase 2 IDs/order/types/points.
Phase 3 tables drive companion poses/placements. Mismatches are reported for review,
never silently repaired or turned into approval. Worksheet build/QA checkboxes are
preserved and shown in the studio.

The supplied `brand-kit.json`, **`brand/screen-mockups/mockups.html` and all eight PNGs**
are actual inputs. Explicit visual-plan L1–L6 entries select the layout. Geometry is
compiled from the HTML into CSS tokens, including title, header/rule/footer, section,
content, scenario and guide positions. The renderer still implements flowing content
and responsive adaptations; it does not blindly transplant mockup sample text,
answers or results. Every reference/input has a SHA256 entry in the report.

- **Rendered draft:** common authored content/interactions: titles, content/summary (including native HTML/image blocks),
  tabs, accordion, flashcards, timeline, worked examples; MCQ, true/false, poll,
  fill-blank, matching and categorisation checks. Matching/drag-drop use accessible
  selects, not pointer-only dragging. Results show **NOT SCORED / NOT RUN**, neutral
  bars and planned settings, not a fake percentage or pass. Decision scenarios play
  one decision at a time, follow the exact authored target/feedback/score delta, lock
  choices while reviewing feedback and support reset. No course result is awarded.
- **Interaction review:** authored steps/nodes/labels/regions for adaptive practice,
  games, escape rooms, simulations, hotspots, labelled diagrams, comparisons and
  sorting. Display diagrams show the existing own SVG and repeat labels in HTML.
  Production algorithms, spatial alignment and scoring remain unimplemented.
- **Build detail pending:** missing build fields, skeletal cards and incomplete keys
  produce a labelled visual brief. No answer, policy, branch, target or calculation
  is derived from prose. In particular, pending `qsr-032` cannot be graded.

Current full-source coverage stays **207 screens / 95 scored screens**:
**48 rendered / 9 interaction review / 150 brief-only**. The first batch contains
**58 / 26**: **48 rendered / 9 review / 1 brief-only**, **240 planned points**.
Six later packages still have review-hand-off skeletons rather than full build
schemas. Every screen has at least one unresolved review/build issue, including
missing final audio. Coverage counts are not approval/readiness.

IDs, input order, points, objectives and evidence remain inspectable. Module selection,
search, Previous/Next and hash links support review:

```text
#03_hr-employee-induction/hr-001
#07_quality-safety-and-risk/qsr-032
```

In-memory choices persist while navigating; reload clears them. Nothing is stored or
sent to an LMS/remote service. Audio, if explicitly mapped, is manual, with no autoplay.
Dense slides grow vertically rather than cropping or shrinking readable body text;
production 16:9 pagination/density is a later reviewed pass.

## Branding, fonts and safe review assets

- Supplied navy/light logos are unchanged; module colours come from the kit and must
  match the worksheet. Questions/body text are never watermarked. Small teal labels
  use the kit's darker teal for contrast; feedback includes words/icons, not colour alone.
- **Title correction:** the supplied navy PNG has a baked-in central logo. It is still
  copied as a reference, but titles use the **mockup-defined navy gradient**, unchanged
  white logo and mark so text is not overlapped by a duplicate logo. This deviation is
  in the layout contract; D11 remains pending.
- **Fonts:** licensed, checksum-verified Montserrat and Tajawal are bundled from
  [`brand/fonts/`](brand/fonts/), including OFL texts and upstream provenance. Arabic
  font support does not approve an Arabic translation/RTL release; this draft is English.
- **Companions:** existing review JPGs/interim avatar PNGs are separate `preview_assets`.
  The Phase 3 placements now render. The full-size companion PNGs landed in
  `characters/assets/` (G6 closed 2026-10-15); this generator still embeds the review art
  until it is repointed at the next rebuild. No new character art is generated.
- Only own `storyboard/assets/*.svg` diagrams are automatically copied. Missing scenes,
  consent-restricted portraits, software captures, audio and downloads stay pending.
  No patient-bearing videos/frames or identifiable billing data are imported.

An explicit map can supply **trusted, authorised local review media**:

```json
{
  "char-omar-explaining": "approved-art/char-omar-explaining.png",
  "hr-aud-001": "approved-audio/hr-aud-001.mp3"
}
```

```bash
python3 elearning-course/scorm-plans/tools/generate_screens.py \
  --phase 1 --asset-map /path/to/review-assets.json
```

Paths resolve relative to the map. PNG/JPEG/WebP/SVG and MP3/WAV/OGG display/play in
supported slots. MP4/PDF can be copied for later wiring; this renderer does not
implement video/download interactions. A map is **not** consent, DPO clearance,
licensing or approval. Never map identifiable patient captures or untrusted SVGs.

## Real screenshots and comparison gallery

Optional Node 22.17+ runtime; pinned dependencies and the bundled Chromium come
from npm. No browser CDN/OS installation is required:

```bash
mkdir -p .generated/tooling
cp elearning-course/scorm-plans/tools/browser/package*.json .generated/tooling/
npm ci --prefix .generated/tooling --ignore-scripts

# Against the running generated-only server above:
node elearning-course/scorm-plans/tools/browser/capture_slides.cjs \
  --url http://127.0.0.1:8000 --out .generated/screens
```

`--out` must correspond exactly to the served directory and be under `.generated/`.
The script verifies that the served HTML matches the local file; waits for fonts and
image decoding; takes every initial slide plus authored HR feedback/tab states;
checks canonical width, all slides at 390px, pending-key guards and missing/external
requests; then writes:

- `review.html` — overview, eight reference→draft comparisons, all slide PNGs and links
  back to the studio (the studio header has a **Screenshot gallery** link).
- `review/phase-overview.png` — one compact browser-captured review sheet.
- `review/screens/*.png` — actual full-height slide/state captures, not AI mock pictures.
- `review/capture-report.json` — IDs, states, dimensions, image hashes, source/working-tree
  provenance, generation-report hash, browser/font/mobile check results and QA scope.

A local browser can be supplied with `CHROMIUM_EXECUTABLE`; an installed Playwright
with `PLAYWRIGHT_MODULE`; another npm Chromium module with `CHROMIUM_MODULE`.
`tools/browser/runtime.cjs` handles local bundled NSS/NSPR on minimal Linux systems.
The localhost URL is tool-side only: browser-facing URLs stay relative for Arena's proxy.

To download the captured review as one **offline, non-SCORM** archive:

```bash
python3 elearning-course/scorm-plans/tools/browser/pack_review.py --out .generated/screens
```

The packer checks the capture revision and image hashes, excludes source videos and
regression folders, and includes a read-me with the remaining gates. The output is
`MyClinic_Phase1_DRAFT_review_v0.1.zip` for the first batch; it is ignored with the rest
of `.generated/`. Authoritative edits still belong in the repository inputs.

## Validation and remaining production work

```bash
python3 -m unittest discover -s elearning-course/scorm-plans/tools/tests -v
node --check elearning-course/scorm-plans/tools/screen_generator/player.js
node --check elearning-course/scorm-plans/tools/screen_generator/scenario.js
# Requires a generated preview containing 03 + 07:
node elearning-course/scorm-plans/tools/tests/test_scenario.cjs
python3 elearning-course/scorm-plans/tools/lint_planning.py

# Existing regression smoke requires an ALL-module generated preview, not only batch 1:
PREVIEW_URL=http://127.0.0.1:8000 \
node elearning-course/scorm-plans/tools/tests/screen_preview_smoke.cjs
```

**27 Python tests**, **189 authored scenario paths**, the **207-screen browser regression**
and **58-slide/61-PNG capture gate** pass on this checkout. Planning lint is clean in all
eight packs (local port). These are smoke/planning checks, not upstream lint, visual
approval, a full accessibility audit, SCORM/LMS validation, the 81-case delivery QA or a pilot.

After kickoff, write decisions to the named Phase 0/cross-module files, update the
approved cards/plans/worksheets together, regenerate and **recapture**. Production
still needs source-lock/SME decisions, the remaining provenance captures and approvals,
D10-approved voices,
final audio/captions/cues, validated upstream schemas/interactions and D9 settings;
then edumints lints/build, SCORM validation, actual-LMS resume/scoring tests and pilot.
Nothing here changes commercial scope or authorises generated video.
