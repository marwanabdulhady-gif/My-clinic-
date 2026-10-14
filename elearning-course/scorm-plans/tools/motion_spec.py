"""Shared motion vocabulary and builder for the My Clinic storyboard packs.

The programme's visual plans carried a single free-text ``animation`` token per screen
(``fade``, ``fade-up`` or ``none``). That is enough to tell an author the *intent*, but it
carries no timing, no easing, no layer order, no cue binding and no reduced-motion
fallback, so two build agents produce two different courses. This module is the single
source of truth for the motion vocabulary:

* the preset/easing names that the review player and (later) the edumints theme implement,
* :func:`motion_for_screen`, which derives a structured spec from the screen's type,
  layout, ``cue_targets`` and legacy ``animation`` token, and
* :func:`lint_motion`, the deterministic rules reused by ``lint_planning.py`` and the tests.

Rules the builder enforces because the approved plans require them
(``gamification-plan.md``, ``scenario-design-plan.md``):

* assessment screens keep ``entry.preset == "none"`` — nothing moves while a learner is
  answering, and no motion hints at the answer;
* no timers, countdowns, streaks, badges or leaderboards are expressed as motion;
* ``loop`` is never true on a scored screen;
* every spec carries ``reduced_motion: "static"``, matching the
  ``prefers-reduced-motion`` block in ``screen_generator/style.css``.

Nothing here renders or exports media; it only writes JSON that the review player reads.
"""
from __future__ import annotations

import re

SPEC_VERSION = "1.0"

# Presets implemented in screen_generator/style.css (@keyframes) and player.js.
ENTRY_PRESETS = ("none", "fade", "fade-up", "fade-down", "slide-left", "pop-in",
                 "grow-x", "rise-stagger", "draw-line")
LAYER_PRESETS = ("fade", "fade-up", "fade-down", "pop-in", "wipe-right", "grow-x",
                 "draw-line", "count-up")
EMPHASIS_PRESETS = ("none", "pulse-once", "underline-draw", "highlight-sweep")
FEEDBACK_PRESETS = ("none", "settle-once", "nudge-once", "pulse-once")
EXIT_PRESETS = ("none", "fade", "fade-down", "slide-left")
EASINGS = ("standard", "decelerate", "accelerate", "spring")
REDUCED_MOTION = ("static",)
TRIGGERS = ("enter", "cue", "interaction")

# Timing envelope. Kept deliberately short: the packs are seat-time budgeted
# (scorm-structure.md §1) and long entrances eat narration time.
ENTRY_MS = (120, 900)
LAYER_MS = (80, 900)
EMPHASIS_MS = (0, 1200)
FEEDBACK_MS = (0, 900)
EXIT_MS = (0, 400)
MAX_STAGGER_MS = 160
MAX_LAYERS = 8
MAX_BUDGET_MS = 1500

# Words that would turn motion into a mechanic the approved plans exclude.
BANNED_WORDS = ("timer", "countdown", "leaderboard", "badge", "streak", "race clock")

# Screen groups. Mirrors SCORED_TYPES/PASSIVE_TYPES in lint_planning.py.
ASSESSMENT_TYPES = {"mcq", "true_false", "fill_blank", "poll"}
INTERACTION_TYPES = {"matching", "drag_drop", "sorting", "hotspot", "labeled_diagram",
                     "image_compare", "term_match_race"}
SCENARIO_TYPES = {"decision_scenario", "simulation", "adaptive_practice", "game",
                  "escape_room"}
# Screens where an entrance could cue the answer, so the interaction area must stay still.
# Unscored `poll` reflections are deliberately excluded: they carry no answer to give away.
STILL_ENTRY_TYPES = ({"mcq", "true_false", "fill_blank"} | INTERACTION_TYPES | SCENARIO_TYPES)
CLOSE_TYPES = {"results_breakdown", "summary"}
EXPLORE_TYPES = {"tabs", "accordion", "flashcards", "timeline", "worked_example"}

LAYER_TARGETS_BY_TYPE = {
    "title_slide": ("logo", "title", "subtitle", "companions", "tagline"),
    "content_slide": ("headline", "body", "media"),
    "video": ("frame", "caption"),
    "data_chart": ("axes", "series-1", "annotation"),
    "tabs": ("tab-bar", "panel-1", "panel-2", "panel-3"),
    "accordion": ("item-1", "item-2", "item-3", "item-4"),
    "flashcards": ("card-front", "card-back", "deck-progress"),
    "worked_example": ("problem", "step-1", "step-2", "step-3", "rule"),
    "timeline": ("axis", "event-1", "event-2", "event-3"),
    "results_breakdown": ("score-ring", "objective-1", "objective-2", "advice"),
    "summary": ("headline", "action-list", "job-aids", "sign-off"),
}

# Legacy free-text token -> structured entry preset. Unknown tokens fall back to fade.
LEGACY_ENTRY = {"fade": "fade", "fade-up": "fade-up", "fade-down": "fade-down",
                "slide-left": "slide-left", "pop-in": "pop-in", "none": "none",
                "": "none"}


def intent_for(screen_type: str, layout: str = "") -> str:
    """Which job the motion does on this screen. Used by the review player's motion notes."""
    layout_id = (layout or "").split(" ")[0].upper()
    if screen_type == "title_slide" or layout_id == "L1":
        return "orient"
    if layout_id == "L2":
        return "section"
    if screen_type in CLOSE_TYPES:
        return "close"
    if screen_type in SCENARIO_TYPES or screen_type in INTERACTION_TYPES:
        return "assess"
    if screen_type in ASSESSMENT_TYPES:
        return "reflect" if screen_type == "poll" else "assess"
    if screen_type in EXPLORE_TYPES:
        return "explore"
    return "teach"


def _intent_entry(intent: str, legacy: str) -> str:
    """Entry preset for an intent, honouring the legacy token where it is compatible."""
    mapped = LEGACY_ENTRY.get((legacy or "").strip().lower(), "fade")
    if intent == "assess":
        # Never animate the interaction area while a learner is answering.
        return "none"
    if intent in {"orient", "section"}:
        return "fade-up" if mapped in {"fade", "fade-up", "none", ""} else mapped
    if intent == "close":
        return "fade-up"
    return mapped or "fade-up"


def _layer_preset(screen_type: str, trigger: str) -> str:
    if trigger == "cue":
        if screen_type in {"timeline", "worked_example"}:
            return "wipe-right"
        if screen_type in {"labeled_diagram", "hotspot"}:
            return "draw-line"
        return "fade-up"
    if screen_type == "title_slide":
        return "fade-up"
    if screen_type == "results_breakdown":
        return "count-up"
    return "fade-up"


def layers_for(screen: dict) -> list[dict]:
    """Cue-bound layers where the plan declares ``cue_targets``, else a staged entry set."""
    stype = screen.get("screen_type") or ""
    cues = [c for c in (screen.get("cue_targets") or []) if isinstance(c, str) and c.strip()]
    if cues:
        out = []
        for index, cue in enumerate(cues[:MAX_LAYERS]):
            out.append({
                "id": cue,
                "trigger": "cue",
                "preset": _layer_preset(stype, "cue"),
                "delay_ms": index * 60,
                "duration_ms": 320,
                "easing": "standard",
                "stagger_ms": 60,
            })
        return out
    ids = LAYER_TARGETS_BY_TYPE.get(stype, ("headline", "body", "media"))
    # Bind the media layer to the real asset id when the plan names one, so the player can
    # target the actual element instead of a generic slot.
    imagery = [i for i in (screen.get("imagery") or []) if isinstance(i, dict)]
    asset_id = ""
    for image in imagery:
        if image.get("decorative"):
            continue
        match = re.match(r"([A-Za-z0-9-]+):", image.get("description") or "")
        if match:
            asset_id = match.group(1)
            break
    ids = tuple(asset_id if layer_id == "media" and asset_id else layer_id for layer_id in ids)
    return [{
        "id": layer_id,
        "trigger": "enter",
        "preset": _layer_preset(stype, "enter"),
        "delay_ms": index * 90,
        "duration_ms": 360,
        "easing": "standard",
        "stagger_ms": 90,
    } for index, layer_id in enumerate(ids)]


def emphasis_for(screen: dict, intent: str) -> dict:
    stype = screen.get("screen_type") or ""
    if intent == "assess":
        return {"preset": "none", "target": None, "duration_ms": 0, "easing": "standard"}
    if stype in {"worked_example", "labeled_diagram"}:
        return {"preset": "underline-draw", "target": "key-term", "duration_ms": 620,
                "easing": "decelerate"}
    if stype == "timeline":
        return {"preset": "highlight-sweep", "target": "current-event", "duration_ms": 560,
                "easing": "standard"}
    if stype == "title_slide":
        return {"preset": "pulse-once", "target": "module-chip", "duration_ms": 520,
                "easing": "spring"}
    return {"preset": "none", "target": None, "duration_ms": 0, "easing": "standard"}


def feedback_for(screen: dict, intent: str) -> dict:
    """Feedback motion. Unscored reflections and passive screens get none."""
    if intent == "assess" and screen.get("screen_type") != "poll":
        return {"correct": "settle-once", "incorrect": "nudge-once", "duration_ms": 420,
                "easing": "spring"}
    if screen.get("screen_type") == "poll":
        # Unscored reflection: acknowledge the reflection quietly, never mark it wrong.
        return {"correct": "settle-once", "incorrect": "none", "duration_ms": 260,
                "easing": "standard"}
    return {"correct": "none", "incorrect": "none", "duration_ms": 0, "easing": "standard"}


def budget_for(entry: dict, layers: list[dict], emphasis: dict) -> int:
    """Longest single path from screen start to rest: entry, or the slowest layer/emphasis."""
    entry_end = int(entry.get("delay_ms", 0)) + int(entry.get("duration_ms", 0))
    layer_end = max((int(l.get("delay_ms", 0)) + int(l.get("duration_ms", 0)) for l in layers),
                    default=0)
    emphasis_end = int(emphasis.get("duration_ms", 0))
    return max(entry_end, layer_end, emphasis_end)


def motion_for_screen(screen: dict) -> dict:
    """Build the structured motion spec for one visual-plan screen (pure, idempotent)."""
    stype = screen.get("screen_type") or ""
    layout = screen.get("layout") or ""
    legacy = (screen.get("animation") or "").strip().lower()
    intent = intent_for(stype, layout)
    entry_preset = _intent_entry(intent, legacy)
    entry_duration = 0 if entry_preset == "none" else (520 if intent in {"orient", "section"} else 420)
    entry = {"preset": entry_preset, "duration_ms": entry_duration, "delay_ms": 0,
             "easing": "decelerate" if entry_preset != "none" else "standard"}
    layers = [] if intent == "assess" else layers_for(screen)
    emphasis = emphasis_for(screen, intent)
    spec = {
        "spec_version": SPEC_VERSION,
        "intent": intent,
        "entry": entry,
        "layers": layers,
        "emphasis": emphasis,
        "feedback": feedback_for(screen, intent),
        "exit": {"preset": "none" if intent == "assess" else "fade",
                 "duration_ms": 0 if intent == "assess" else 180,
                 "easing": "accelerate"},
        "loop": False,
        "reduced_motion": "static",
    }
    spec["budget_ms"] = budget_for(entry, layers, emphasis)
    spec["notes"] = (
        "Assessment screen: the interaction area stays still so motion cannot cue an answer."
        if intent == "assess" else
        "Layer reveals are bound to the narration cue marks in narration-script.json."
        if any(l["trigger"] == "cue" for l in layers) else
        "Staged entrance; nothing loops and no timing pressure is applied."
    )
    return spec


def lint_motion(spec, screen=None) -> list[dict]:
    """Deterministic motion rules. Returns issue dicts like lint_planning.issue()."""
    def issue(sev, code, message, path=None):
        return {"severity": sev, "code": code, "message": message, "path": path}

    problems = []
    screen = screen or {}
    sid = screen.get("screen_id")
    stype = screen.get("screen_type")
    if not isinstance(spec, dict):
        return [issue("error", "motion_missing", "screen has no motion spec object")]
    if spec.get("spec_version") != SPEC_VERSION:
        problems.append(issue("error", "motion_spec_version",
                              f"motion.spec_version must be '{SPEC_VERSION}'", "motion"))
    if spec.get("intent") not in {"orient", "section", "teach", "explore", "assess",
                                  "reflect", "close"}:
        problems.append(issue("error", "motion_intent",
                              f"unknown motion intent '{spec.get('intent')}'", "motion.intent"))
    if spec.get("reduced_motion") not in REDUCED_MOTION:
        problems.append(issue("error", "motion_reduced_motion",
                              "motion.reduced_motion must be 'static' "
                              "(prefers-reduced-motion must disable every preset)",
                              "motion.reduced_motion"))

    def check_block(name, block, presets, bounds, allow_zero=True):
        if not isinstance(block, dict):
            problems.append(issue("error", f"motion_{name}", f"motion.{name} must be an object",
                                  f"motion.{name}"))
            return
        preset = block.get("preset", block.get("correct"))
        if name == "feedback":
            for key in ("correct", "incorrect"):
                if block.get(key) not in FEEDBACK_PRESETS:
                    problems.append(issue("error", "motion_feedback_preset",
                                          f"motion.feedback.{key} '{block.get(key)}' is not a "
                                          f"known preset {list(FEEDBACK_PRESETS)}",
                                          f"motion.feedback.{key}"))
        elif preset not in presets:
            problems.append(issue("error", f"motion_{name}_preset",
                                  f"motion.{name}.preset '{preset}' is not a known preset "
                                  f"{list(presets)}", f"motion.{name}.preset"))
        if block.get("easing") not in EASINGS:
            problems.append(issue("error", f"motion_{name}_easing",
                                  f"motion.{name}.easing '{block.get('easing')}' is not one of "
                                  f"{list(EASINGS)}", f"motion.{name}.easing"))
        duration = block.get("duration_ms")
        delay = block.get("delay_ms", 0)
        if not isinstance(duration, int) or isinstance(duration, bool):
            problems.append(issue("error", f"motion_{name}_duration",
                                  f"motion.{name}.duration_ms must be an integer",
                                  f"motion.{name}.duration_ms"))
            return
        if duration == 0 and not allow_zero:
            problems.append(issue("error", f"motion_{name}_duration",
                                  f"motion.{name}.duration_ms must be > 0",
                                  f"motion.{name}.duration_ms"))
        if duration and not bounds[0] <= duration <= bounds[1]:
            problems.append(issue("error", f"motion_{name}_duration",
                                  f"motion.{name}.duration_ms {duration} is outside "
                                  f"{bounds[0]}–{bounds[1]} ms", f"motion.{name}.duration_ms"))
        if not isinstance(delay, int) or isinstance(delay, bool) or delay < 0:
            problems.append(issue("error", f"motion_{name}_delay",
                                  f"motion.{name}.delay_ms must be an integer >= 0",
                                  f"motion.{name}.delay_ms"))

    check_block("entry", spec.get("entry", {}), ENTRY_PRESETS, ENTRY_MS)
    check_block("emphasis", spec.get("emphasis", {}), EMPHASIS_PRESETS, EMPHASIS_MS)
    check_block("exit", spec.get("exit", {}), EXIT_PRESETS, EXIT_MS)
    check_block("feedback", spec.get("feedback", {}), FEEDBACK_PRESETS, FEEDBACK_MS)

    layers = spec.get("layers")
    if not isinstance(layers, list):
        problems.append(issue("error", "motion_layers", "motion.layers must be a list",
                              "motion.layers"))
        layers = []
    if len(layers) > MAX_LAYERS:
        problems.append(issue("warn", "motion_layer_count",
                              f"{len(layers)} layers (> {MAX_LAYERS}) — the entrance will not read",
                              "motion.layers"))
    cues = set(screen.get("cue_targets") or [])
    seen = set()
    for index, layer in enumerate(layers):
        path = f"motion.layers[{index}]"
        if not isinstance(layer, dict):
            problems.append(issue("error", "motion_layer", "layer must be an object", path))
            continue
        lid = layer.get("id")
        if not isinstance(lid, str) or not lid.strip():
            problems.append(issue("error", "motion_layer_id", "layer needs a non-empty id", path))
        elif lid in seen:
            problems.append(issue("error", "motion_layer_id", f"layer id '{lid}' is used twice",
                                  path))
        seen.add(lid)
        if layer.get("preset") not in LAYER_PRESETS:
            problems.append(issue("error", "motion_layer_preset",
                                  f"layer preset '{layer.get('preset')}' is not a known preset "
                                  f"{list(LAYER_PRESETS)}", f"{path}.preset"))
        if layer.get("trigger") not in TRIGGERS:
            problems.append(issue("error", "motion_layer_trigger",
                                  f"layer trigger '{layer.get('trigger')}' is not one of "
                                  f"{list(TRIGGERS)}", f"{path}.trigger"))
        if layer.get("trigger") == "cue" and lid not in cues:
            problems.append(issue("error", "motion_unknown_cue",
                                  f"cue layer '{lid}' is not in the screen's cue_targets "
                                  f"{sorted(cues)}", f"{path}.id"))
        if layer.get("easing") not in EASINGS:
            problems.append(issue("error", "motion_layer_easing",
                                  f"layer easing '{layer.get('easing')}' is not one of "
                                  f"{list(EASINGS)}", f"{path}.easing"))
        for key, bounds in (("duration_ms", LAYER_MS), ("delay_ms", (0, 4000))):
            value = layer.get(key)
            if not isinstance(value, int) or isinstance(value, bool):
                problems.append(issue("error", "motion_layer_timing",
                                      f"layer {key} must be an integer", f"{path}.{key}"))
                continue
            if key == "duration_ms" and not bounds[0] <= value <= bounds[1]:
                problems.append(issue("error", "motion_layer_timing",
                                      f"layer {key} {value} is outside {bounds[0]}–{bounds[1]} ms",
                                      f"{path}.{key}"))
            if key == "delay_ms" and value < bounds[0]:
                problems.append(issue("error", "motion_layer_timing",
                                      f"layer {key} must be >= 0", f"{path}.{key}"))
        stagger = layer.get("stagger_ms", 0)
        if not isinstance(stagger, int) or isinstance(stagger, bool) or stagger > MAX_STAGGER_MS:
            problems.append(issue("warn", "motion_layer_stagger",
                                  f"stagger_ms {stagger} exceeds {MAX_STAGGER_MS} ms — layers will "
                                  "arrive one at a time instead of as a group",
                                  f"{path}.stagger_ms"))
    if spec.get("loop") is not False:
        # No screen in the eight packs loops: a loop competes with narration and the
        # reduced-motion contract ("static") cannot express "loops stopped".
        problems.append(issue("error", "motion_loop_unsupported",
                              f"motion.loop must be false — looping motion is not used in this "
                              f"programme (screen '{sid}')", "motion.loop"))
    if screen.get("screen_type") in STILL_ENTRY_TYPES:
        entry = spec.get("entry") or {}
        if entry.get("preset") != "none":
            problems.append(issue("error", "motion_assessment_entry",
                                  f"assessment screen '{sid}' must keep entry.preset 'none' so "
                                  "motion cannot cue the answer", "motion.entry.preset"))
        if spec.get("loop"):
            problems.append(issue("error", "motion_loop_scored",
                                  f"scored screen '{sid}' must not loop motion", "motion.loop"))
    if not isinstance(spec.get("loop"), bool):
        problems.append(issue("error", "motion_loop", "motion.loop must be a boolean",
                              "motion.loop"))
    budget = spec.get("budget_ms")
    if not isinstance(budget, int) or isinstance(budget, bool):
        problems.append(issue("error", "motion_budget", "motion.budget_ms must be an integer",
                              "motion.budget_ms"))
    else:
        expected = budget_for(spec.get("entry") or {}, layers, spec.get("emphasis") or {})
        if budget != expected:
            problems.append(issue("error", "motion_budget",
                                  f"motion.budget_ms {budget} does not match the recomputed "
                                  f"{expected} ms", "motion.budget_ms"))
        elif budget > MAX_BUDGET_MS:
            problems.append(issue("warn", "motion_budget",
                                  f"entrance takes {budget} ms (> {MAX_BUDGET_MS}) — it will eat "
                                  "narration time", "motion.budget_ms"))
    for field in ("notes", "intent"):
        text = str(spec.get(field) or "").lower()
        for word in BANNED_WORDS:
            if word in text:
                problems.append(issue("error", "motion_banned_mechanic",
                                      f"'{word}' is not an approved mechanic "
                                      "(gamification-plan.md)", f"motion.{field}"))
    return problems


def lint_plan_motion(plan) -> dict:
    """Plan-level motion lint: per-screen rules plus motion monotony across the run."""
    issues = []
    screens = plan.get("screens", []) if isinstance(plan, dict) else []
    for index, screen in enumerate(screens):
        sid = screen.get("screen_id")
        issues.extend(lint_motion(screen.get("motion"), screen))
    run_preset, run_len = None, 0
    for screen in screens:
        preset = ((screen.get("motion") or {}).get("entry") or {}).get("preset")
        if preset == run_preset:
            run_len += 1
        else:
            run_preset, run_len = preset, 1
        if run_len == 5 and preset not in {"none"}:
            issues.append({"severity": "warn", "code": "motion_monotony",
                           "message": f"5 screens in a row use the '{preset}' entrance — vary the "
                                      "motion so the run does not read as one long transition",
                           "path": f"screens[{screens.index(screen)}]({sid})"})
    return {
        "error_count": sum(1 for i in issues if i["severity"] == "error"),
        "warn_count": sum(1 for i in issues if i["severity"] == "warn"),
        "clean": not issues,
        "spec_version": SPEC_VERSION,
        "screen_count": len(screens),
        "issues": issues,
    }
