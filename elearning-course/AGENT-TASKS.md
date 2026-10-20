# Agent tasks — read this whole file before you change anything

You are working on the **My Clinic induction e-learning** project: 8 SCORM packages for a Saudi outpatient clinic group (Jeddah and Riyadh). The packages are built from storyboards and played by **our own SCORM 1.2 player** (`scorm-plans/tools/player/`, made for Oracle Learning). The edumints compiler is no longer used. Your job is one task from the list in §4.

Follow these instructions **exactly**. If a step fails or something is unclear, **stop and report it**. Do not guess, and do not work around a rule.

---

## 1. The 12 rules (breaking any of them makes your work unusable)

1. **Never change anything scored.** Do not change any screen's `points`, `objective_ids`, `id`, `type`, `node_id` or order in `storyboard/storyboard.md`, `phase-2-storyboard.md` or `build/screens.json`. These numbers are in the client's contract. The build stops if you change them.
2. **New interactivity goes only in `<module>/production/personalisation.json`.** Never put it in the storyboard. Everything you add there must be unscored (`points: 0`).
3. **Never invent facts.** Policy numbers, phone extensions, leave days, codes, limits and names come from only two places:
   - the source decks, as written in the storyboard;
   - `scorm-plans/00_program/kickoff-assumed-answers.md` (researched working answers).

   When you use a working answer, keep or add the marker `⚠ Draft — pending <decision id>` on screen (never in narration).
4. **No real people's data.** Use no real patient, staff or claim data, and no names, photos, phone numbers or ID numbers of real people. Use fictional data only.
5. **Never regenerate Noor or Dr. Omar.** Use only the files in `scorm-plans/00_program/characters/assets/`. Do not create new characters with names.
6. **Never run `tools/assemble_storyboard_docs.py`.** It overwrites the narration and all rewrite work is lost.
7. **Never edit generated files by hand.** These are generated:
   - `decision-sheet.*`
   - `media-jobs.json` and `media-jobs-summary.md`
   - `course-spec.json`, `asset-map.json`, `build-report.json`, `preview.html`
   - `scorm-structure.md`
   - `draft-builds.md`
   - `kickoff-assumed-answers.md`
   - `kickoff-pack.docx`

   Change the source file, then run the generator (§3).
8. **Pictures carry no text.** No letters, numbers or logos in generated images. Labels go in HTML.
9. **One task, one module, one branch, one pull request.** Do not mix tasks.
10. **Run all the gates (§3) before every commit.** Do not commit if one fails.
11. **Never merge your own pull request.** Never push to `main`. The owner merges.
12. **Write like a person.** Plain, short English sentences. No filler such as "Keep the next action clear" or "Use the principle in context".

---

## 2. Set-up (do this at the start of every session)

```bash
cd <repo root>                                   # the folder that contains elearning-course/
git fetch origin main && git checkout -b <your-branch> origin/main
python3 -m venv /tmp/edu-venv
/tmp/edu-venv/bin/pip install -q python-docx pillow pytest
T=elearning-course/scorm-plans/tools
# the browser check (check_packages.py) needs Node + Playwright + Chromium; cloud sessions have them in /opt
```

Name your branch for the task, for example `agent/t1-narration-04` or `agent/t3-images-02`. If your environment gives you a required branch name, use that one.

If Node or Chromium is missing, run every other gate, skip `check_packages.py`, and say so in your report.

---

## 3. The gates (run all of them before every commit)

```bash
python3 $T/build_media_jobs.py                       # refresh job lists
python3 $T/build_course_spec.py <module>             # storyboard + layer + maps → course-spec.json
python3 $T/build_package.py <module>                # package → zip, build/package/, preview.html, build-report.json
python3 $T/check_packages.py <NN>                    # plays the course in a browser on a mock LMS (right, wrong, resume)
python3 $T/draft_builds_report.py
python3 $T/lint_planning.py
python3 $T/audit_assets.py                           # must end with hard_failures=0
python3 $T/audit_scorm_base.py                       # must end with "audit clean"
/tmp/edu-venv/bin/python -m pytest -q $T/tests       # every test must pass
```

`build_package.py` must end with `validate ok`. `check_packages.py` must end with `failures=0`: the all-correct run ends **passed**, the all-wrong run ends **failed**, and the resume run reopens on the same screen.

**Never edit `tools/player/player.js` or `player.css` as part of a content task.** The player is shared by all nine packages; a change there is its own task, and it must pass `check_packages.py` for every module.

The total points for each module must stay the same:

| Module | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 |
|---|---|---|---|---|---|---|---|---|
| Total points | 220 | 145 | 145 | 50 | 100 | 80 | 95 | 90 |

Module folder names (`scorm-plans/`):
- `01_health-and-safety-1`
- `02_health-and-safety-2`
- `03_hr-employee-induction`
- `04_operations-and-my-care`
- `05_rcm-documentation-and-coding`
- `06_rcm-ebp-benefits-and-rejections`
- `07_quality-safety-and-risk`
- `08_it-ehr-consultation`

**Look at your work.** Open `<module>/build/preview.html` in a browser (Playwright screenshot is fine) and look at every screen you touched, before and after you answer it. Text must be readable, nothing cut off, and no raw markup or `{{…}}` visible. The preview saves progress in your browser: use **☰ → Restart preview** to start again.

---

## 4. The tasks, in priority order

Take the **first task that is not done and not blocked**. Do one module at a time.

### T1 — Rewrite the filler narration ★ highest priority, not blocked

**Why:** 156 narration segments in six modules (01, 02, 04, 05, 06, 08) contain generic filler. They cannot be voiced until rewritten. Modules 03 and 07 are already clean: use them as your style example (`03_hr-employee-induction/storyboard/narration-script.json`).

**Do one module per pull request, in this order: 04, 05, 06, 08, 02, 01** (smallest first).

1. Run `python3 $T/narration_rewrite.py export <module>`. It writes `<module>/production/narration-rewrite.csv`.
2. For each row, read `screen_title`, `on_screen_text`, `screen_type`, `scored` and `without_filler`. Also read that screen's card in `<module>/storyboard/storyboard.md`; search for the screen id.
3. Write the new narration in the `new_text` column:
   - Start with the same speaker label as now: `NOOR:` or `OMAR:`.
   - Length: between 60 % and 115 % of `target_words`.
   - Say something real about **this** screen: the situation, why it matters, or a short true-to-life moment. Base it on `without_filler` and the card.
   - Speak to the learner ("you"). Short sentences. No lists.
   - **On a scored screen (`scored = yes`), never give or hint at the answer.** Set up the situation and stop.
   - Do not read the on-screen text word for word.
   - No `⚠`, no "PENDING", no numbers or names that are not already on the screen.
4. Run `python3 $T/narration_rewrite.py apply <module>`.
   - If it prints `REFUSED`, fix those rows and run it again. It writes nothing until every row passes.
5. Run `python3 $T/narration_rewrite.py check <module>`. It must say **0** segments still contain filler.
6. Delete `<module>/production/narration-rewrite.csv`; do not commit it. Run the gates (§3). Commit, push, open a pull request titled `T1: narration rewrite <module>`.

**Done when:** `check` reports 0 for the module, the gates pass, and the PR is open.

### T2 — Draw the missing diagrams and icons (own SVG), not blocked

**Why:** 35 pictures must be drawn as SVG, not generated: GHS pictograms, icon sets, charts, NFPA diamonds and similar.

1. Open `<module>/production/media-jobs.json`. Pick jobs with `"route": "own-svg"` and `"status": "todo"`.
2. Draw each one as a clean SVG at the job's `target_file`:
   - Brand: navy `#003867` lines, white and `#F4F7FA` fills, one module colour (the `module_colour` at the top of the job file), Montserrat for any label, `viewBox` set, no external links.
   - Follow the job's `brief` exactly.
   - GHS pictograms: red diamond border, black symbol, white background (UN standard). Draw them yourself; do not copy a vendor's file.
3. Run the gates. In `preview.html`, check the PENDING card is replaced by your drawing.

**Done when** the job shows `"status": "done"` after `build_media_jobs.py`, and the gates pass.

### T3 — Generate the scene images (AI image tool), not blocked for drafts

**Only do this if you have an image-generation tool.** If you don't, skip to the next task.

1. Pick jobs with `"route": "ai-image"` and `"status": "todo"`. Do module 02 first (the Code Red drill scenes), then 01, 03, 04, 07.
2. Use the job's `prompt` **exactly as written**. Size 1920 × 1080, PNG, saved at `target_file`.
3. Check the picture against every line of the job's `acceptance`. Regenerate if any line fails:
   - no text or letters in the image;
   - every item the brief lists is clearly visible;
   - nothing extra;
   - no real-looking faces of identifiable people.
4. If the job has a `hotspots` block, do T4 for this picture before you commit.
5. Add an entry to the job in `media-jobs.json`: `"made_by"`, `"tool"`, `"model"`, `"date"`, `"prompt_used"`. These fields are kept when the file is regenerated. Then run the gates.

### T4 — Map the hotspots on every new picture (goes with T3)

1. Run `python3 $T/map_hotspots.py init <module> <asset-id>`.
2. Open `<module>/production/hotspots/<asset-id>.json`.
   - For each region, write the pixel box `[x, y, width, height]` on the picture's own size (`image_size`).
   - Set `"mapped_by"` to your name and the date.
3. Run `python3 $T/map_hotspots.py preview <module>` and screenshot `production/hotspots/preview.html`. **Every box must sit on its object.** Fix and repeat until they do.
4. You may add extra hotspots for other useful things in the picture under `"add_regions"`:
   - each needs `id`, `shape: "rect"`, `coords`, `label_html` and `feedback_html`;
   - end the feedback with `<em>(Proposed — SME to confirm.)</em>`;
   - on a **scored** screen they wait for the SME; leave `"sme_approved": false`.

   The worked example is `01_health-and-safety-1/production/hotspots/hs1-img-corridor.json`.
5. Run the gates and look at the hotspot screen in `preview.html`.

### T5 — Interactivity backlog, not blocked

**Why:** some screens are still read-only. The list is §5 of `scorm-plans/00_program/personalisation-and-interactivity-plan.md`; the details are in `00_program/interactivity-upgrades.json`.

1. Work only in `<module>/production/personalisation.json`. Copy the pattern of existing entries:
   - `"convert"` turns an unscored screen into flashcards, tabs, a timeline or an explore hotspot, keeping all of its content;
   - `"insert_after"` adds an unscored quick check or exploration;
   - `"append_html"` adds a line to the closing screen.
2. You may convert only screens with `points` 0. A converted screen must still teach everything the old one said.
3. Explore hotspots on an existing diagram need region boxes. Get them from the SVG's own coordinates (open the SVG file), then check the preview.
4. Run the gates. Look at every changed screen in `preview.html`.

### T6 — Job aids (5 PDFs), draft only, not blocked

The jobs with `"route": "own-pdf"` in modules 03, 05, 06 and 08, plus emergency-code cards for 01/02.
- Build each PDF as one or two A4 pages in the brand (navy header band, My Clinic logo from `00_program/brand/assets/`, Montserrat).
- Use only facts already on the module's screens.
- Put **"DRAFT — pending client confirmation"** in the footer.
- Save to the job's `target_file` path, with the `.pdf` extension.

### T7 — Motion-graphics videos (voiced by Dr. Omar) ✅ open (owner, 2026-10-20)

The owner asked for the videos now, with one male voice (Dr. Omar), one voice interaction per clip, and a visual and motion plan for every scene. The plan is ready. Your job is to produce it, not redesign it.

1. Read [`video/PRODUCTION-PLAN.md`](video/PRODUCTION-PLAN.md) from top to bottom, then [`video/README.md`](video/README.md).
2. Work on **one clip per branch**, in this order:
   - `prog-vid-welcome`;
   - then `qsr-vid-speakup`;
   - then the rest in module order.
3. Each clip's drafts are already in `video/<clip-id>/data/`: `BRIEF.md`, `facts.md`, `script.md`, `cues.json`, `visual_plan.json`, `interactions.json`. Follow tasks V1–V6 in the plan's §5 and stop at every gate.
4. **To change wording, a scene or a motion beat:**
   - edit `video/_shared/plan/clips.json`;
   - run `python3 video/_shared/scripts/scaffold_clips.py --force <clip-id>`;
   - make sure it ends with `problems=0`.
   Never edit `PRODUCTION-PLAN.md` by hand.
5. **Never speak a pending fact.** If a line needs one, stop and report.
6. **V0 (interactive video in the player) is a player task.** Do not do it inside a clip task. Until it exists, deliver the clip as plain video.
7. If a script you need is not in `video/_shared/scripts/` yet (`transcribe.py`, `build_timeline.py`, `qa_check.py`…), stop and report it. Do not write a replacement yourself.

### T8 — Voice recording (TTS) ⛔ blocked

Blocked until decision **D10** (voices) closes **and** T1 is done for the module.

### Blocked — do not start

These wait on My Clinic:
- the EHR screenshots (31) and the Oracle screenshots (5);
- client photos (4) and leader portraits;
- anything whose job `gate` names an open decision for a release build.

---

## 5. When you finish (every session)

1. Commit with a clear message. Push your branch. Open a pull request with:
   - the task number (T1–T6);
   - the module;
   - what you changed;
   - the gate results (paste the last line of each);
   - screenshots of the screens you changed.
2. Do **not** merge.
3. End with a short report to the owner:
   - **Done:** what you finished (task, module, number of items).
   - **Checked:** gates passed yes/no, screens looked at.
   - **Not done / problems:** anything you skipped, refused rows, missing tools.
   - **Next:** the next task and module from §4.

If something in this file does not match what you see in the repository, stop and report it. Do not change this file unless the owner asks.
