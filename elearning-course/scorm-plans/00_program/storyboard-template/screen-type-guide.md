# Screen-type guide for storyboard cards

What each screen card must contain, by edumints screen type. Field names come from the edumints models (`core/project.py`) and `docs/SCREEN_TYPES.md`; check `list_screen_types` at build time in case the schema has moved on.

**Fields every screen has:** `type`, `id`, `title`, `section`, `node_id`, optional `narration_asset_id` + `narration_text` (added in Phase 3/4), `notes`.
**Every scored screen also has:** `points`, `objective_ids`, `feedback` (`correct_html`, `incorrect_html`, `show_correct_answer`).

Only the types used in the eight module plans are listed. Use no other type without changing Phase 2 first.

---

## Content and explore screens (unscored)

### `title_slide`
| Must contain | Build fields |
|---|---|
| Title (≤ 8 words), subtitle (≤ 12 words), optional background image | `title`, `subtitle`, `background_asset_id`, `body_html` |

### `content_slide`
| Must contain | Build fields |
|---|---|
| Keywords (≤ 45 words), layout, one image or diagram if useful. For several stacked parts use `blocks` (each block is text **or** an image) | `body_html` or `blocks: [{html} / {asset_id, caption}]`, `media_asset_id`, `layout`: `text` / `text_media` / `media_text` / `full_media` |

Note: all `blocks` reveal as **one** unit with narration. If parts must appear one by one, use separate top-level paragraphs in `body_html`.

### `accordion`
| Must contain | Build fields |
|---|---|
| 3–9 panels; each a short title + ≤ 40 words; optional image per panel | `items: [{title, body_html, image_asset_id, image_alt}]` |

### `tabs`
| Must contain | Build fields |
|---|---|
| 2–5 tabs; label ≤ 3 words; body ≤ 40 words | `tabs: [{label, body_html, image_asset_id, image_alt}]` |

### `flashcards`
| Must contain | Build fields |
|---|---|
| Front (term, ≤ 6 words) and back (meaning, ≤ 30 words) for every card; optional image per side with alt text | `cards: [{front_html, back_html, front_asset_id, back_asset_id, front_alt, back_alt}]` |

### `timeline`
| Must contain | Build fields |
|---|---|
| Events in order: date or step label, title, ≤ 25 words each | `events: [{date, title, body_html, image_asset_id, image_alt}]` |

### `labeled_diagram` (`mode: "display"`)
| Must contain | Build fields |
|---|---|
| Diagram brief, every label with position (x, y on a 0–1000 scale) and short text | `image_asset_id`, `prompt_html`, `mode: "display"`, `labels: [{id, text, x, y}]` |

### `hotspot` (`mode: "explore"`)
| Must contain | Build fields |
|---|---|
| Image brief, image alt text, every region with name, shape, rough position and the text it reveals. Say whether all regions must be opened | `image_asset_id`, `image_alt`, `prompt_html`, `mode: "explore"`, `require_all: true`, `regions: [{id, shape: "rect"/"circle", coords, label_html, feedback_html}]` |

Coordinates are in the image's natural pixels. Write `TBD after final image` in the card and give the rough position in words (e.g. "top-right, above the door"). **`poly` is not allowed.**

### `image_compare`
| Must contain | Build fields |
|---|---|
| Two images of the same size; labels; caption | `before_asset_id`, `after_asset_id`, `before_label`, `after_label`, `prompt_html`, `caption` |

### `worked_example`
| Must contain | Build fields |
|---|---|
| Problem statement; each step = action + reason (why); optional self-explanation question (unscored) | `intro_html`, `steps: [{action_html, rationale_html, artifact_asset_id, artifact_caption}]`, `fading`: `full` / `partial` / `problem_only`, `self_explanation_prompt_html` |

### `poll`
| Must contain | Build fields |
|---|---|
| Question; options (or open text); reflection shown after answering. Unscored | `prompt_html`, `options: [{id, text_html}]`, `multi`, `allow_text`, `reflection_html` |

### `video`
| Must contain | Build fields |
|---|---|
| Clip brief and length (≤ 60 s if rendered on the server), poster, transcript, WebVTT captions | `video_asset_id`, `poster_asset_id`, `captions_asset_id`, `caption`, `require_complete: false`, `narration_text` (transcript) |

---

## Scored question screens

### `mcq`
| Must contain | Build fields |
|---|---|
| Stem (a situation, not a definition recall where possible); 3–4 options; one correct (or `multi_select`); **feedback per option** explaining why | `prompt_html`, `options: [{id, text_html, correct, feedback_html}]`, `multi_select`, `feedback`, `points` |

Distractors must be plausible mistakes people really make (take them from the Phase 1 "why it goes wrong" column).

### `true_false`
| Must contain | Build fields |
|---|---|
| One clear statement; the correct value; feedback that explains | `prompt_html`, `correct: true/false`, `feedback`, `points` |

### `fill_blank`
| Must contain | Build fields |
|---|---|
| Prompt; each blank with an id/label and **all** accepted answers (units, spellings, number formats) | `prompt_html`, `blanks: [{id, accepted: [...]}]`, `case_sensitive: false`, `feedback`, `points` |

### `matching`
| Must contain | Build fields |
|---|---|
| 4–8 pairs; left and right each ≤ 12 words; no two right-hand items that could both fit one left item | `prompt_html`, `pairs: [{id, left_html, right_html}]`, `feedback`, `points` |

### `sorting`
| Must contain | Build fields |
|---|---|
| Items **in the correct order** (the player shuffles them); 3–9 items; why the order matters in feedback | `prompt_html`, `items: [{id, text_html}]`, `feedback`, `points` |

### `drag_drop`
| Must contain | Build fields |
|---|---|
| 2–5 targets; 4–10 items, each with its correct target; feedback | `prompt_html`, `items: [{id, text_html, correct_target_id}]`, `targets: [{id, label_html}]`, `feedback`, `points` |

### `labeled_diagram` (`mode: "quiz"`)
| Must contain | Build fields |
|---|---|
| Diagram brief **without** the labels; each label's correct position (0–1000 scale) | `image_asset_id`, `prompt_html`, `mode: "quiz"`, `labels: [{id, text, x, y}]`, `points` |

### `hotspot` (`mode: "quiz"`)
| Must contain | Build fields |
|---|---|
| Question; image; the correct region(s) and distractor regions, each with feedback | `regions: [{id, shape, coords, correct, label_html, feedback_html}]`, `points` |

---

## Scenario, game and simulation screens (scored)

### `decision_scenario`
| Must contain | Build fields |
|---|---|
| Intro (who, where, what's at stake); 1–4 nodes; each node a situation + 2–4 choices; every choice has `score_delta`, next node and **why** feedback (never empty); pass score | `intro_html`, `nodes: [{id, prompt_html, image_asset_id, image_alt, choices: [{id, text_html, feedback_html, score_delta, goto_node_id}]}]`, `start_node_id`, `pass_score`, `points`, `feedback` |

Use the node table in the screen card. Last node's choices have `goto_node_id: null`.

### `game` (`template: "case_sim"`)
| Must contain | Build fields |
|---|---|
| Intro; mechanics (score, lives, hints with text); every node with situation + choices; per choice: next node, feedback, effects; debrief; pass score. **No timer** unless Phase 3 says so | `template`, `intro_html`, `start_node_id`, `pass_score`, `points`, `mechanics: {score: {id, start}, lives: {id, start}, hints: {id, hints: [{text, cost}]}}`, `nodes: [{id, content_html, choices: [{id, text_html, to, feedback_html, on_choose: [{do: "score.correct", points} / {do: "lives.lose", n} / {do: "score.wrong"}]}]}]`, `feedback` |

See `examples/games/lab-safety-game.en.json` in the edumints repo for a full working game.

### `escape_room`
| Must contain | Build fields |
|---|---|
| Premise; puzzles in order; each puzzle's clue visible on screen (as text); accepted answers incl. variants; one text hint each; lives; debrief | `intro_html`, `puzzles: [{id, prompt_html, accepted: [...], hint_html, case_sensitive: false}]`, `lives`, `points` |

### `simulation`
| Must contain | Build fields |
|---|---|
| Task statement; one card row per step: screenshot (test data only), alt text, instruction, click target (region) **or** typed input with accepted answers, hint | `prompt_html`, `steps: [{image_asset_id, image_alt, instruction_html, regions: [...] or input_accepted: [...], input_label, hint_html}]`, `points`, `feedback` |

### `adaptive_practice`
| Must contain | Build fields |
|---|---|
| Item bank (≥ 3, usually 12–15): stem, options with the correct one, difficulty 0–1, explanation after answering, hint shown on a wrong answer; stop and pass settings | `prompt_html`, `adaptive: {strategy: "elo"}`, `items: [{id, prompt_html, options: [{id, text_html, correct}], difficulty, explain_html, scaffold_html}]`, `max_items`, `target_success`, `pass_ratio`, `points` |

---

## Closing screens

### `results_breakdown`
| Must contain | Build fields |
|---|---|
| One section per objective with the scored screen ids it covers and advice shown if weak | `body_html`, `sections: [{title, screen_ids: [...], advice_html}]`, `weak_threshold`, `show_total` |

### `summary`
| Must contain | Build fields |
|---|---|
| What the learner can now do (3–6 points), next step, links to job aids | `body_html`, `show_score`, `show_completion` |
