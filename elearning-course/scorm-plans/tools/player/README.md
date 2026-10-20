# My Clinic course player (SCORM 1.2, Oracle Learning)

Our own player for the nine packages (eight courses and the Oracle sample). It replaced the edumints compiler on 2026-10-20 because the owner wanted a design we fully control: minimal, interactive and animated, and built only for Oracle Learning.

```bash
python3 tools/build_course_spec.py <module>   # storyboard → build/course-spec.json (unchanged)
python3 tools/build_package.py <module>       # course-spec.json → build/package/ + build/MC_…_1.2.zip
python3 tools/check_packages.py [NN …]        # plays it in Chromium on a mock LMS: right, wrong, resume
```

Open `<module>/build/preview.html` to try a course. With no LMS it saves progress in the browser and shows a **Preview** tag; **☰ → Restart preview** clears it.

## Files

| File | What it is |
|---|---|
| `player.js` | The engine. It handles navigation, variables, XP/rank/meter, the SCORM 1.2 calls and the renderers for all 27 screen types. It has no dependencies and works in ES5-era browsers. |
| `player.css` | The design system: brand tokens, layouts, every animation, and the reduced-motion fallback. |
| `test/play.js`, `test/lms.html` | The browser bot and the mock LMS used by `check_packages.py`. |

## Design rules (from `00_program/brand/brand-identity.md`)

- **Minimal.** The page is off-white, content sits on white cards, navy is the structure colour and the module colour is the only highlight. Magenta is used only for warnings and lives.
- **No outlines around text** (owner feedback, 2026-10-20). Cards are separated from the page by soft shadows or light tints. A coloured ring appears only to show a state:
  - navy: selected;
  - green: correct;
  - red: wrong;
  - module colour: drop target.
- **Montserrat**, packaged with the course (it is never loaded from the web). Small teal text uses the dark teal `#006E78`.
- **Motion has a purpose.**
  - Screens slide in the direction you travel.
  - Blocks rise in, one after another.
  - Choices lift when you hover over them.
  - A correct answer draws a tick; a wrong one gives a short shake.
  - Feedback slides up.
  - You get XP toasts and a rank-up toast, and the meter dots pulse.
  - The results ring counts up and the bars fill.
  - A pass gets a confetti burst.
  - Hotspot badges ping until they are opened.
  - Accordions open smoothly, flashcards flip in 3D, and the tab underline glides.
  - **`prefers-reduced-motion`** turns all of this into instant changes and stops every loop.
- **Accessible.** Every control is a real button. Drag-and-drop, matching and sorting also work by tap or keyboard (tap an item, then tap the box; or use the ↑ ↓ buttons). Focus moves to each new screen's title. Feedback is announced (`role=status`). The colour of a state always comes with a word or an icon.

## Scoring (the same rules as the storyboards; nothing scored is changed)

- Each scored activity gets **one attempt**. Its points are all-or-nothing. Next stays locked until the learner answers. Unscored quick checks offer **Try again**.
- **Score** = points earned ÷ total points × 100. **Passed / failed** is set when the learner reaches the last screen. Before that the status is `incomplete`.
- If the learner is below the pass mark, the results screen offers **Try the activities you missed**. This clears only the missed activities and takes the learner back to the first one.
- Rules for each type:
  - **Decision scenario:** passes on `pass_score` good decisions.
  - **Game:** passes on `pass_score` points, and fails if all lives are lost.
  - **Escape room:** passes when every lock opens before the lives run out.
  - **Adaptive practice:** passes when right ÷ answered is at least `pass_ratio`. It stops early after 3 in a row once the success target is met.
  - **Simulation:** full points when every step is completed. Extra clicks are reported but not penalised, as in the old player.
- XP, rank and the course meter are only for the learner. They are kept in the resume data and never affect the score.

## What Oracle receives (SCORM 1.2)

| Data model element | When |
|---|---|
| `cmi.core.lesson_status` | `incomplete` at first launch; `passed`/`failed` on reaching the last screen |
| `cmi.core.score.raw/min/max` | after every scored answer (0–100) |
| `cmi.objectives.n` (id, score.raw, status) | after every scored answer, one per objective with scored evidence |
| `cmi.interactions.n` (id, type, student_response, result, weighting, latency, time, objectives.0.id) | once per scored activity, at a fixed index so a retry overwrites instead of adding a row |
| `cmi.core.lesson_location`, `cmi.suspend_data` | every screen change (JSON, kept under 4,000 characters; the largest course uses about 1,600) |
| `cmi.core.session_time`, `cmi.core.exit` | on leaving: `suspend` unless passed/failed |

The API is found in the parent frames and in `window.opener`, so it works both in Oracle's frame and in a new window. The manifest is one SCO with `adlcp:masteryscore` set to the pass mark, and `imsmanifest.xml` sits at the zip root.

## When you change the player

1. Change `player.js` / `player.css` only, never the built `package/` folders.
2. Rebuild every package (`for m in 00_* 0[1-8]_*; do python3 tools/build_package.py $m; done`).
3. `python3 tools/check_packages.py` must end with `failures=0`, and `pytest -q tools/tests` must pass.
4. Look at the screens you changed at 1280 × 800 **and** at 390 × 844 (phone).
