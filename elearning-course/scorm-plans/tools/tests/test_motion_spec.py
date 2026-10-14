"""Regression tests for the structured motion spec (tools/motion_spec.py).

Run with the repository's own runner:

    python3 -m pytest elearning-course/scorm-plans/tools/tests -q

These tests fail if a visual plan loses its motion spec, if a spec drifts from the
derived one (i.e. someone hand-edited it), if an assessment screen gains an entrance that
could cue the answer, or if a preset is named in a plan but not implemented in the review
player's stylesheet.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from motion_spec import (  # noqa: E402
    EMPHASIS_PRESETS, ENTRY_PRESETS, EXIT_PRESETS, FEEDBACK_PRESETS, LAYER_PRESETS,
    MAX_BUDGET_MS, SPEC_VERSION, STILL_ENTRY_TYPES, budget_for, lint_motion,
    lint_plan_motion, motion_for_screen,
)

PLANS = TOOLS.parent
MODULES = sorted(p.name for p in PLANS.glob("0[1-8]_*"))
GENERATOR = TOOLS / "screen_generator"


def plan_for(folder: str) -> dict:
    return json.loads((PLANS / folder / "storyboard" / "visual-plan.json")
                      .read_text(encoding="utf-8"))


def all_screens():
    for folder in MODULES:
        for screen in plan_for(folder).get("screens", []):
            yield folder, screen


def test_every_pack_has_the_motion_spec():
    for folder in MODULES:
        plan = plan_for(folder)
        assert plan.get("motion_spec_version") == SPEC_VERSION, folder
        assert plan.get("motion_generated", {}).get("tool", "").startswith(
            "tools/build_motion_spec.py"), folder
        assert all(isinstance(s.get("motion"), dict) for s in plan["screens"]), folder


def test_committed_specs_match_the_derived_spec():
    """A hand-edited motion object is a defect: the spec is generated, not authored."""
    drifted = []
    for folder, screen in all_screens():
        if screen["motion"] != motion_for_screen(screen):
            drifted.append(f"{folder}/{screen['screen_id']}")
    assert not drifted, "motion spec drifted from tools/build_motion_spec.py: " + ", ".join(drifted)


def test_every_committed_spec_is_lint_clean():
    problems = []
    for folder, screen in all_screens():
        for issue in lint_motion(screen["motion"], screen):
            problems.append(f"{folder}/{screen['screen_id']}: {issue['code']} {issue['message']}")
    assert not problems, "\n".join(problems)


def test_plan_level_motion_lint_is_clean():
    for folder in MODULES:
        report = lint_plan_motion(plan_for(folder))
        assert report["error_count"] == 0, (folder, report["issues"])
        assert report["screen_count"] == len(plan_for(folder)["screens"])


def test_assessment_screens_keep_the_interaction_area_still():
    """gamification-plan.md: no motion may hint at the answer while a learner is answering."""
    offenders = [(folder, s["screen_id"]) for folder, s in all_screens()
                 if s["screen_type"] in STILL_ENTRY_TYPES
                 and s["motion"]["entry"]["preset"] != "none"]
    assert not offenders, offenders
    for folder, screen in all_screens():
        if screen["screen_type"] in STILL_ENTRY_TYPES:
            assert screen["motion"]["layers"] == [], (folder, screen["screen_id"])
            assert screen["motion"]["loop"] is False
            assert screen["motion"]["feedback"]["correct"] in FEEDBACK_PRESETS


def test_unscored_polls_may_still_move():
    polls = [s for _, s in all_screens() if s["screen_type"] == "poll"]
    assert polls, "expected poll screens in the packs"
    assert any(p["motion"]["entry"]["preset"] != "none" for p in polls)
    assert all(p["motion"]["intent"] == "reflect" for p in polls)


def test_cue_layers_only_reference_declared_cue_targets():
    cue_bound = 0
    for folder, screen in all_screens():
        declared = set(screen.get("cue_targets") or [])
        for layer in screen["motion"]["layers"]:
            if layer["trigger"] == "cue":
                cue_bound += 1
                assert layer["id"] in declared, (folder, screen["screen_id"], layer["id"])
    # Module 03 is the only pack whose narration script carries [[cue:…]] marks today.
    assert cue_bound == 70, f"expected 70 cue-bound layers, found {cue_bound}"


def test_entrance_budget_is_recomputed_and_bounded():
    for folder, screen in all_screens():
        spec = screen["motion"]
        expected = budget_for(spec["entry"], spec["layers"], spec["emphasis"])
        assert spec["budget_ms"] == expected, (folder, screen["screen_id"])
        assert spec["budget_ms"] <= MAX_BUDGET_MS, (folder, screen["screen_id"], spec["budget_ms"])
        assert spec["reduced_motion"] == "static"


def test_no_banned_mechanic_leaks_into_motion():
    banned = ("timer", "countdown", "leaderboard", "badge", "streak")
    for folder, screen in all_screens():
        text = json.dumps(screen["motion"]).lower()
        for word in banned:
            assert word not in text, (folder, screen["screen_id"], word)


@pytest.mark.parametrize("mutation,code", [
    ({"entry": {"preset": "spin", "duration_ms": 400, "delay_ms": 0, "easing": "standard"}},
     "motion_entry_preset"),
    ({"entry": {"preset": "fade", "duration_ms": 5000, "delay_ms": 0, "easing": "standard"}},
     "motion_entry_duration"),
    ({"emphasis": {"preset": "none", "target": None, "duration_ms": 0, "easing": "wobble"}},
     "motion_emphasis_easing"),
    ({"reduced_motion": "slow"}, "motion_reduced_motion"),
    ({"loop": True}, "motion_loop_unsupported"),
    ({"budget_ms": 9999}, "motion_budget"),
    ({"notes": "add a countdown ring"}, "motion_banned_mechanic"),
])
def test_lint_rejects_broken_specs(mutation, code):
    screen = {"screen_id": "x-001", "screen_type": "content_slide", "layout": "L3 Content",
              "animation": "fade-up", "cue_targets": [], "imagery": []}
    spec = motion_for_screen(screen)
    spec.update(json.loads(json.dumps(mutation)))
    codes = {issue["code"] for issue in lint_motion(spec, screen)}
    assert code in codes, codes


def test_lint_rejects_unknown_cue_layer_and_scored_entrance():
    screen = {"screen_id": "x-002", "screen_type": "mcq", "cue_targets": ["a"], "imagery": []}
    spec = motion_for_screen(screen)
    spec["layers"] = [{"id": "zzz", "trigger": "cue", "preset": "fade-up", "delay_ms": 0,
                       "duration_ms": 300, "easing": "standard", "stagger_ms": 0}]
    spec["entry"] = {"preset": "pop-in", "duration_ms": 300, "delay_ms": 0, "easing": "standard"}
    codes = {issue["code"] for issue in lint_motion(spec, screen)}
    assert {"motion_unknown_cue", "motion_assessment_entry"} <= codes, codes


def test_missing_motion_is_an_error_not_a_silent_pass():
    screen = {"screen_id": "x-003", "screen_type": "content_slide"}
    codes = {issue["code"] for issue in lint_motion(None, screen)}
    assert codes == {"motion_missing"}


def test_every_preset_is_implemented_in_the_review_player():
    css = (GENERATOR / "style.css").read_text(encoding="utf-8")
    player = (GENERATOR / "player.js").read_text(encoding="utf-8")
    for preset in ENTRY_PRESETS:
        assert f".mo-entry-{preset}" in css, preset
    for preset in LAYER_PRESETS:
        assert f".mo-layer-{preset}" in css, preset
    for preset in EMPHASIS_PRESETS:
        if preset != "none":
            assert f".mo-emphasis-{preset}" in css, preset
    for preset in FEEDBACK_PRESETS:
        if preset != "none":
            assert f".mo-feedback-{preset}" in css, preset
    for preset in EXIT_PRESETS:
        # Exit presets reuse the entrance keyframes; only 'none' needs no rule.
        if preset != "none":
            assert f"@keyframes mo-{preset}" in css, preset
    assert "applyMotion(root, s)" in player
    assert "prefers-reduced-motion: reduce" in player
    assert "mo-static" in player and ".mo-static" in css


def test_reduced_motion_never_leaves_a_cue_layer_hidden():
    css = (GENERATOR / "style.css").read_text(encoding="utf-8")
    reduced_block = css[css.index("@media (prefers-reduced-motion: reduce)"):]
    assert '.mo-layer[data-mo-trigger="cue"]' in reduced_block
    assert ".mo-static" in css
