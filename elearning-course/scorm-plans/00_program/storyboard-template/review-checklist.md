# Screen review checklist

Run this on **every** screen card before handing in a module storyboard. These checks mirror the edumints gates (`lint_visual_plan`, `lint_narration_script`, `lint_course`) so problems are caught before build. Mark failures in the card's *Notes* section.

## A. Accuracy and source

- [ ] Every fact, number, code and rule traces to the *Source* cell (page/slide/time) or a closed Phase 0 decision.
- [ ] Anything that depends on an open Phase 0 item is marked `⚠ PENDING <id>` and listed in the module's open questions.
- [ ] No real patient, staff, claim or phone data. Scenario names, MRNs and dates are fictional.
- [ ] Terminology matches the program decisions (code names, regulator name, branch names, "critical incident" vs "sentinel event").

## B. On-screen text

- [ ] Title ≤ 8 words.
- [ ] Body ≤ 45 words (aim ≤ 25); word count stated.
- [ ] Keywords, not full sentences read by the narrator.
- [ ] British spelling; consistent capitalisation of codes (Code Red, Code Orange).

## C. Visual

- [ ] Visual concept ≥ 6 words and specific enough for a designer.
- [ ] Colour roles set; text/background pair is a dark-on-light or `on_primary`-on-`primary` pair.
- [ ] Accent used only for warnings, codes or key numbers.
- [ ] Every non-decorative image has alt text; decorative images are marked.
- [ ] Asset ids reuse Phase 3 ids where they exist; new assets have a brief and a provenance source (`own`, `ai-generated`, `cc0`, `public-domain`, `local`).
- [ ] Hotspot regions are `rect` or `circle`.
- [ ] Mentor character used only where Phase 3 lists it.

## D. Interaction and scoring

- [ ] Screen type matches Phase 2 (or a change is proposed in the module header).
- [ ] Scored screen: `points` and `objective_ids` match Phase 4.
- [ ] Correct answer is unambiguous; distractors are realistic mistakes.
- [ ] Feedback explains **why**, for both correct and incorrect (and every scenario choice).
- [ ] Typed answers list all reasonable variants (units, spelling, number formats).
- [ ] Scenarios/games: every path ends; pass score is reachable; replay can't inflate the score.
- [ ] Escape rooms: every clue is visible on screen as text.

## E. Narration

- [ ] Sentences ≤ 25 words; "you"; present tense; active voice.
- [ ] Does not read the on-screen text word for word.
- [ ] No interface talk ("click", "as you can see", "on this slide").
- [ ] Question screens: set-up only — the answer is not given away.
- [ ] ≤ 60 seconds; estimated time within ±15% of target.
- [ ] Every `[[cue:id]]` matches a listed cue target.
- [ ] Every acronym is in the master lexicon or listed under *New lexicon terms*.

## F. Accessibility

- [ ] Can be completed by keyboard alone.
- [ ] Meaning never depends on colour alone.
- [ ] Narrated screen has `narration_text`; video has captions.
- [ ] No unadjustable timer.

## G. Build fields

- [ ] JSON block is valid (quotes, commas, brackets) and uses field names from `screen-type-guide.md`.
- [ ] `id`, `node_id`, `section` match the module header outline.
- [ ] Planned asset ids are written as `<asset-id>` placeholders, not invented server ids.

## H. Brand identity (`../brand/brand-identity.md`)

- [ ] Layout L1–L6 named and matches the screen type table in §7.
- [ ] Logo: supplied PNG only, right colourway (navy on light, white on navy), right size and position; one logo per screen.
- [ ] No logo, "My Clinic" text or any other text requested from an image model.
- [ ] Colours only from the palette; navy for structure, the **module colour** as the single highlight, magenta only for warnings/key numbers.
- [ ] Contrast: no small white text on teal; small teal text uses #006E78.
- [ ] Montserrat sizes from §3; nothing below 14 px except the footer.
- [ ] Petal watermark only on L1, L2 or closing screens.
- [ ] Icons are single-weight line icons from one family, with provenance.
- [ ] AI images have a filled prompt from §6 and pass the review (only the briefed elements, no text, palette colours).
- [ ] Mentor character matches the character description (navy scrubs, navy hijab, purple lanyard, no logo on badge).
