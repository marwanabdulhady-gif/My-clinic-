# Motion and animation spec — eight My Clinic packages

**For authors, build agents and reviewers · 14 October 2026**

Every screen in all eight `visual-plan.json` files now carries a structured `motion` object
next to the legacy `animation` token. The token said *what kind* of movement a screen had
(`fade`, `fade-up`, `none`); the object says *how*: entrance preset, duration, delay, easing,
the layer order, what each layer is bound to, emphasis, answer-feedback movement, exit, the
total entrance budget in milliseconds and the reduced-motion fallback.

- **Vocabulary and rules:** [`../tools/motion_spec.py`](../tools/motion_spec.py)
- **Generator (writes the spec):** [`../tools/build_motion_spec.py`](../tools/build_motion_spec.py)
- **Lint (re-checks it every run):** [`../tools/lint_planning.py`](../tools/lint_planning.py) → `motion_spec` in each `lint-report.json`
- **Implementation:** [`../tools/screen_generator/style.css`](../tools/screen_generator/style.css) (`@keyframes`) and [`../tools/screen_generator/player.js`](../tools/screen_generator/player.js) (`applyMotion`)
- **Tests:** [`../tools/tests/test_motion_spec.py`](../tools/tests/test_motion_spec.py)
- **Programme summary:** [`motion-spec-summary.json`](motion-spec-summary.json)

The spec is **derived, never hand-edited**. After any storyboard or visual-plan change run:

```bash
python3 elearning-course/scorm-plans/tools/build_motion_spec.py
python3 elearning-course/scorm-plans/tools/lint_planning.py
```

The test suite fails if a committed spec drifts from what the generator produces, which is
the guard against hand edits.

## Why this exists

Two build agents reading `"animation": "fade-up"` produce two different courses: one fades in
over 200 ms, the other over a second, and neither reveals the labelled parts of a diagram in
the order the narration names them. Module 03 alone has **72 `[[cue:…]]` marks** in its
narration script matched to 72 `cue_targets`; those marks now drive 70 layer reveals instead
of being decorative text. Motion is also where accessibility is won or lost, so the fallback
is part of the spec rather than an afterthought.

## Preset vocabulary

| Group | Presets | Notes |
|---|---|---|
| `entry` | `none`, `fade`, `fade-up`, `fade-down`, `slide-left`, `pop-in`, `grow-x`, `rise-stagger`, `draw-line` | one per screen |
| `layers[]` | `fade`, `fade-up`, `fade-down`, `pop-in`, `wipe-right`, `grow-x`, `draw-line`, `count-up` | ≤ 8 per screen |
| `emphasis` | `none`, `pulse-once`, `underline-draw`, `highlight-sweep` | at most one target |
| `feedback` | `none`, `settle-once`, `nudge-once`, `pulse-once` | safe choice / choice to review |
| `exit` | `none`, `fade`, `fade-down`, `slide-left` | ≤ 400 ms |
| `easing` | `standard`, `decelerate`, `accelerate`, `spring` | cubic-bézier tokens in `style.css` |

Timing envelope: entry 120–900 ms, layers 80–900 ms, emphasis ≤ 1,200 ms, feedback ≤ 900 ms,
exit ≤ 400 ms, stagger ≤ 160 ms, total entrance budget ≤ 1,500 ms. Motion eats seat time, and
the eight packs are budgeted at roughly four hours (`scorm-structure.md` §1), so long
entrances are lint errors rather than taste.

## Intent by screen type

The generator assigns one intent per screen and derives everything else from it.

| Intent | Screens | Entrance | Layers |
|---|---|---|---|
| `orient` | `title_slide`, layout L1 | `fade-up` 520 ms | logo, title, subtitle, companions, tagline |
| `section` | layout L2 openers | `fade-up` 520 ms | staged |
| `teach` | `content_slide`, `video`, `data_chart` | legacy token, defaulting to `fade-up` | headline, body, the named asset |
| `explore` | `tabs`, `accordion`, `flashcards`, `timeline`, `worked_example` | legacy token | the authored parts, or the declared cues |
| `reflect` | `poll` (unscored) | legacy token | staged |
| `assess` | `mcq`, `true_false`, `fill_blank`, `matching`, `drag_drop`, `sorting`, `hotspot`, `labeled_diagram`, `image_compare`, `decision_scenario`, `simulation`, `adaptive_practice`, `game`, `escape_room` | **`none`** | **none** |
| `close` | `results_breakdown`, `summary` | `fade-up` | score ring, objectives, advice, job aids |

## Rules the lint enforces

1. **Assessment screens do not move.** On any screen where an answer is given, `entry.preset`
   must be `none` and there must be no layers. Motion must not cue an answer, and
   `gamification-plan.md` also forbids revealing an answer through a visible reaction before
   the interaction. Feedback movement (`settle-once` / `nudge-once`) happens *after* the
   choice and is cosmetic — the text carries the result, so colour is never the only cue.
2. **Cue layers must be declared.** A layer with `trigger: "cue"` must name an id in that
   screen's `cue_targets`, or the lint reports `motion_unknown_cue`.
3. **Nothing loops.** `motion.loop` must be `false` everywhere: a loop competes with
   narration, and the reduced-motion contract cannot express "loops stopped".
4. **No excluded mechanic reaches the motion layer.** `timer`, `countdown`, `leaderboard`,
   `badge` and `streak` in a spec are errors — `gamification-plan.md` excludes them.
5. **Budget is recomputed, not asserted.** `budget_ms` must equal the slowest of
   entrance / layer / emphasis, and stay under 1,500 ms.
6. **Reduced motion is `static`.** Every spec says so, `style.css` implements it with
   `@media (prefers-reduced-motion: reduce)`, and `.mo-static` also unhides cue layers so a
   learner who disables animation never loses content that was waiting for a cue.

## Motion inside SVG assets

Own-SVG assets carry a small amount of self-contained motion (a stroke drawing in, segments
growing, one settle), always inside `@media (prefers-reduced-motion: no-preference)` so the
asset is static by default for anyone who asks for it. See the module 03 drafts in
[`../03_hr-employee-induction/storyboard/assets/`](../03_hr-employee-induction/storyboard/assets/).
Rules for asset motion:

- Animate **one** idea per asset: a draw-in, a grow, a settle. No ambient looping.
- Never animate anything that carries a fact into or out of view in a way that could hide it
  (a number, a label, a hazard in a spot-the-hazard scene).
- Keep it under ~1 s and never delay the moment the asset is legible.
- Never use motion as the only signal of state; pair it with text or shape.

## Video remains out of scope

This spec changes transitions and reveals inside the SCORM screens. It does **not** add
standalone video: `visual-and-motion-agent-brief.md` keeps new videos at zero for the Rev01
baseline, with the single optional `qsr-060` motion clip still gated on D7/D8.

## Reviewing motion in the draft studio

`tools/generate_screens.py` passes each screen's spec to the review player as `_motion`. The
player applies the presets, and every screen's **Motion spec & reduced-motion behaviour**
panel lists the entrance, the layer order with delays, emphasis, feedback movement, exit and
budget, with a **Replay entrance & cue layers** button that fires cue-bound layers in the
order the narration will. That panel is a review aid on the internal draft — it is not part
of a learner build, and nothing in it records learner state.
