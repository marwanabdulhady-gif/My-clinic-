# Storyboard template: brief for the storyboarding agent

![My Clinic logo](../brand/logo-preview.png)

This folder is everything an AI agent (or a human designer) needs to write the **full, screen-by-screen storyboard** for each module. It turns the one-line rows in each module's `phase-2-storyboard.md` into complete screen cards that a developer can build in edumints without asking questions.

| File | What it is |
|---|---|
| [`module-storyboard-template.md`](module-storyboard-template.md) | The template to copy: a module header plus one **screen card** to repeat for every screen |
| [`screen-type-guide.md`](screen-type-guide.md) | What each screen type must contain (fields, limits, edumints build fields) |
| [`example-screens.md`](example-screens.md) | Three finished screen cards from module 01, to copy the level of detail |
| [`review-checklist.md`](review-checklist.md) | Checks to run on every screen before handing in the module |

---

## 1. Task for the agent

Write one storyboard file per module, with one completed screen card for **every** screen listed in that module's `phase-2-storyboard.md`.

- **Do one module per run.** Do not mix modules in one file.
- **Output path:** `elearning-course/scorm-plans/<module folder>/storyboard/storyboard.md`
  - Example: `elearning-course/scorm-plans/01_health-and-safety-1/storyboard/storyboard.md`
- **Keep screen ids exactly as in Phase 2** (`hs1-402`, `hr-044`, …). Do not add, remove, merge or reorder screens. If you think a change is needed, write it under *Proposed changes* in the module header and keep the original screen.

## 2. Inputs to read first (in this order)

1. `../../README.md` (scorm-plans overview) and `../cross-module-decisions.md`.
2. The module's `README.md`, `phase-0-source-lock.md`, `phase-1-action-map.md`, `phase-2-storyboard.md`, `phase-3-narration-and-assets.md`, `phase-4-build.md`.
3. The module's source file in `elearning-course/md/` (the Phase 2 *Src* column gives the page, slide or time). Facts come **only** from this source or from closed Phase 0 decisions.
4. **`../characters/companions.md` — the two companion characters (mandatory)**: who they are, poses and asset ids, placement, voices and script rules. Then **`../brand/brand-identity.md` — the My Clinic brand identity (mandatory).** Logo files and placement, colour palette and the module colour, Montserrat type scale, icons, illustration style, the **AI image prompt template**, and the six screen layouts L1–L6 with mockups in `../brand/screen-mockups/`. Then `../brand-and-theme.md`, `../narration-and-lexicon.md` (voice, writing rules, lexicon) and `../build-pipeline.md` (settings, limits).
5. `screen-type-guide.md` and `example-screens.md` in this folder.

## 3. Rules (do not break)

1. **No invented facts.** Every number, rule, name or code must trace to the source or a closed decision. If it depends on an open Phase 0 item, write the value from the source, mark it `⚠ PENDING <item id>` (e.g. `⚠ PENDING B1 / D1`) and list it under *Open questions*.
2. **No real people or patients.** Use fictional names, MRNs, phone numbers and dates in scenarios. No staff names unless the Phase 0 decision allows it.
3. **On-screen text:** keywords only, aim for ≤ 25 words, hard limit 45 (title not counted). State the word count.
4. **Narration:** follows `narration-and-lexicon.md` (≈140 wpm, sentences ≤ 25 words, "you", no interface talk, never reads the screen, never gives away a question's answer). Each segment ≤ 60 s.
5. **Every scored screen** has: correct answer(s), feedback for correct and incorrect (and per choice for scenarios), `objective_ids`, `points` matching Phase 4.
6. **Every meaningful image** has alt text; decorative images are marked decorative. Colour is never the only way to tell things apart.
7. **Only supported edumints screen types** (see `screen-type-guide.md`). Hotspot regions are `rect` or `circle` only.
8. **Companions (Noor and Dr. Omar)** follow `../characters/companions.md`: the lead host narrates; each character appears and speaks only where the module's Phase 3 "Companions in this module" table says; every spoken line is prefixed `NOOR:` / `OMAR:`.
9. Write in **plain, warm, professional English** (British spelling, as in the source decks).
10. **Brand identity is mandatory.** Every card names its layout (L1–L6), the logo file and position, the module colour and the colour roles from `../brand/brand-identity.md`. Use only palette colours.
11. **Never ask an image tool to draw the logo or the words "My Clinic".** The logo is always the supplied PNG in `../brand/assets/`. Images must contain no text.
12. For every AI-generated image, write the **filled prompt** from the brand prompt template in the card. Diagrams are briefed as own SVG with real text, not AI images.

## 4. Workflow for each module

1. Copy `module-storyboard-template.md` to the output path.
2. Fill the **module header** from the module's README, Phase 1 and Phase 4.
3. For each row in `phase-2-storyboard.md`, copy the **screen card** and fill every field. Delete guidance text in `<angle brackets>`; never leave a field empty — write `n/a` with a reason.
4. Write the full narration for the screen, using the intent in `phase-3-narration-and-assets.md`.
5. Fill the **build fields** block with the edumints JSON for that screen (use the field names in `screen-type-guide.md`).
6. Run `review-checklist.md` on every card. Fix what fails.
7. Fill the module **summary tables** at the end of the template (assets, open questions, word and time totals).
8. Set each card's status to `Draft — ready for SME review`.

## 5. Definition of done

- One card per Phase 2 screen, same ids and order.
- All checklist items pass, or the failure is explained under *Open questions*.
- Totals match Phase 4: number of scored screens and total points.
- Estimated narration time is within ±15% of the Phase 3 estimate.
- No `<angle bracket>` guidance text left in the file.

## 6. What happens next

The storyboard goes to the module's SME for review (Phase 2 exit gate). Approved cards are then turned into `visual-plan.json` and `narration-script.json` for `lint_visual_plan` and `lint_narration_script`, and finally into the course spec (Phase 4).

## 7. Prompt to give the agent (copy and paste, change the module)

```text
You are writing the screen-by-screen storyboard for one My Clinic e-learning module.

Repository: marwanabdulhady-gif/My-clinic-
Module folder: elearning-course/scorm-plans/<01_health-and-safety-1>/

1. Read elearning-course/scorm-plans/00_program/storyboard-template/README.md and follow it exactly.
2. Read the inputs it lists, in order, for this module only.
3. Copy module-storyboard-template.md to <module folder>/storyboard/storyboard.md.
4. Write one complete screen card for every screen in the module's phase-2-storyboard.md,
   in the same order and with the same ids. Match the detail in example-screens.md.
5. Never invent facts. Mark anything that depends on an open Phase 0 item as ⚠ PENDING <id>.
   Follow elearning-course/scorm-plans/00_program/brand/brand-identity.md for every screen:
   layout L1–L6, logo file and position, module colour, palette, Montserrat sizes, and the
   AI image prompt template. Never generate the logo; never put text in images.
   Use the companions Noor and Dr. Omar exactly as in 00_program/characters/companions.md and
   the module's Phase 3 companion table; prefix every spoken line NOOR: or OMAR:.
6. Run review-checklist.md on every card and fill the module summary tables.
7. Commit the file on a new branch and open a pull request titled
   "Storyboard: <module title> v0.1".
```

Run one module per agent session. Suggested order (matches the learning path and the plans' readiness): 03, 07, 01, 02, 04, 05, 06, 08.
