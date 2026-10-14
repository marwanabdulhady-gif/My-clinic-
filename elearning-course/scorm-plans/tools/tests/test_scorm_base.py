"""Regression tests for the base SCORM structure across all eight packages.

Run with the repository's own runner:

    python3 -m pytest elearning-course/scorm-plans/tools/tests -q

These exercise the real generator (``build_scorm_structure.build``) and the real audit
(``audit_scorm_base``) against the storyboard build blocks on disk — no fixtures, no
re-implementation. They fail if a package loses objectives, interaction mapping, a pass
mark, a Phase 3 gamification rule, its motion spec, or if the generated structure document
goes stale against the storyboard.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import audit_scorm_base  # noqa: E402
from audit_scorm_base import (EXPECTED_SCENARIO_TOTAL, EXPECTED_SCENARIOS,  # noqa: E402
                              EXPECTED_SCORED_TOTAL, EXPECTED_SCREEN_TOTAL, is_hard,
                              label_key)
from build_scorm_structure import (INTERACTION_TYPE, activity_rules, build,  # noqa: E402
                                   has_feedback, rule_for, scenario_shape, suspend_estimate)

PLANS = TOOLS.parent
MODULES = sorted(p for p in PLANS.glob("0[1-8]_*") if p.is_dir())


@pytest.fixture(scope="module")
def audited():
    return {folder.name[:2]: audit_scorm_base.audit_module(folder) for folder in MODULES}


def test_all_eight_packages_are_covered(audited):
    assert sorted(audited) == ["01", "02", "03", "04", "05", "06", "07", "08"]


def test_programme_totals_reconcile_with_the_planned_baseline(audited):
    assert sum(m["screens"] for m in audited.values()) == EXPECTED_SCREEN_TOTAL
    assert sum(m["scored"] for m in audited.values()) == EXPECTED_SCORED_TOTAL
    assert sum(m["scenario_count"] for m in audited.values()) == EXPECTED_SCENARIO_TOTAL


@pytest.mark.parametrize("num,expected", sorted(EXPECTED_SCENARIOS.items()))
def test_scenario_counts_match_the_scenario_design_plan(audited, num, expected):
    """scenario-design-plan.md: 5 + 3 + 4 + 1 + 2 + 2 + 2 + 7 = 26 Rev01 experiences."""
    assert audited[num]["scenario_count"] == expected, audited[num]["scenario_screens"]


def test_every_objective_has_scored_evidence(audited):
    for num, m in audited.items():
        assert m["objectives"] > 0, num
        row = next(c for c in m["checklist"] if c["requirement"].startswith(
            "Every objective has at least one scored screen"))
        assert row["ok"], (num, row["evidence"])


def test_every_scored_screen_maps_to_an_interaction_type(audited):
    for num, m in audited.items():
        assert sum(m["interaction_types"].values()) == m["scored"], num
        assert set(m["interaction_types"]) <= set(INTERACTION_TYPE.values()), num


def test_every_scored_screen_names_its_objective(audited):
    for num, m in audited.items():
        row = next(c for c in m["checklist"] if c["requirement"].startswith(
            "Every scored screen names its objective"))
        assert row["ok"], (num, row["evidence"])


def test_pass_mark_and_completion_rule_are_set(audited):
    for num, m in audited.items():
        assert m["pass_mark"] in (70, 80), num
        assert m["pass_points"] == -(-m["points"] * m["pass_mark"] // 100), num
        assert any(c["ok"] and c["requirement"].startswith("Completion rule set")
                   for c in m["checklist"]), num


def test_resume_state_fits_the_scorm_version_limit(audited):
    for num, m in audited.items():
        assert m["suspend_limit"] == (64000 if m["scorm"] == "2004" else 4096), num
        assert m["suspend_chars"] < m["suspend_limit"], (num, m["suspend_chars"])
        assert m["suspend_headroom"] == m["suspend_limit"] - m["suspend_chars"]


def test_every_scenario_screen_has_a_phase_3_gamification_rule(audited):
    for num, m in audited.items():
        row = next(c for c in m["checklist"] if c["requirement"].startswith(
            "Gamification rules recorded for every scenario screen"))
        assert row["ok"], (num, row["evidence"])
        for scen in m["scenario_screens"]:
            assert scen["points"] >= 0
            assert scen["objectives"], scen


def test_no_excluded_gamification_mechanic_is_introduced(audited):
    """gamification-plan.md excludes leaderboards, ranking, time pressure, streaks, badges."""
    for num, m in audited.items():
        assert m["banned_mechanic_hits"] == [], (num, m["banned_mechanic_hits"])


def test_physical_badges_and_reporting_deadlines_are_not_flagged():
    """The scan must not read a staff ID badge or a reporting deadline as a game mechanic."""
    from build_scorm_structure import banned_mechanic_hits
    benign = [
        "NOOR: Wear your badge. Apply the point to a familiar task.",
        "| Body | People: ID always · contractor permits · visitor badges · score the risk |",
        "The exact reporting channel and time limit require confirmation.",
        "Keyboard: three node choices use focusable buttons; no time limit or countdown.",
    ]
    assert banned_mechanic_hits("\n".join(benign)) == []
    hostile = [
        "Earn a badge for each 10 points scored.",
        "Show a leaderboard of scores by department.",
        "A 30-second countdown timer runs on each question.",
        "Reward streaks unlock the next question.",
    ]
    hits = {word for word, _ in banned_mechanic_hits("\n".join(hostile))}
    assert {"badge", "leaderboard", "countdown", "streak"} <= hits, hits
    deadline = banned_mechanic_hits("A time limit of 45 seconds applies to each quiz question.")
    assert "time limit" in {word for word, _ in deadline}, deadline


def test_motion_spec_present_for_every_screen(audited):
    for num, m in audited.items():
        row = next(c for c in m["checklist"] if c["requirement"].startswith(
            "Motion spec present for every screen"))
        assert row["ok"], (num, row["evidence"])


def test_generated_structure_documents_are_not_stale(audited):
    stale = [m["module"] for m in audited.values() if not m["structure_document_fresh"]]
    assert not stale, "rerun tools/build_scorm_structure.py for: " + ", ".join(stale)


def test_structure_documents_contain_the_new_base_sections():
    for folder in MODULES:
        text = (folder / "scorm-structure.md").read_text(encoding="utf-8")
        for heading in ("## 6. Tracking", "### Interaction records", "## 7. Gamification",
                        "## 8. Scenarios and branching", "## 9. Base SCORM structure checklist"):
            assert heading in text, (folder.name, heading)


def test_audit_cli_exits_clean_and_writes_reports():
    result = subprocess.run([sys.executable, str(TOOLS / "audit_scorm_base.py")],
                            capture_output=True, text=True, cwd=str(PLANS.parent.parent))
    assert result.returncode == 0, result.stdout + result.stderr
    assert "audit clean" in result.stdout
    payload = json.loads((PLANS / "00_program" / "scorm-base-audit.json").read_text())
    assert payload["clean"] is True
    assert payload["hard_failures"] == []
    assert payload["totals"]["scenarios"] == EXPECTED_SCENARIO_TOTAL
    report = (PLANS / "00_program" / "scorm-base-audit.md").read_text(encoding="utf-8")
    assert "## Base requirements per package" in report
    assert "## Hard failures" in report


def test_label_key_normalises_interpolated_values():
    assert label_key("Pass mark written to the manifest (80%)") == \
           label_key("Pass mark written to the manifest (70%)")
    assert label_key("Completion rule set (`viewed_all_and_passed`)") == \
        "Completion rule set"
    assert is_hard("Completion rule set (`viewed_all_and_passed`)")
    assert not is_hard("Thin-evidence objectives flagged for SME sign-off")


def test_activity_rule_lookup_matches_screen_and_number_lists():
    text = ("| Activity | Objective | Rules | Success | Failure / retry | Accessibility |\n"
            "|---|---|---|---|---|---|\n"
            "| hs2-030 Code Red drill | hs2-o2 | 6 nodes; 2 lives | ≥ 5 of 6 | restart | Buttons |\n"
            "| Simulations (010, 020, 031) | o1–o4 | click or type | all steps | retry | text |\n")
    rules = activity_rules(text)
    assert len(rules) == 2
    assert rule_for(rules, "hs2-030")["rules"].startswith("6 nodes")
    assert rule_for(rules, "ehr-020")["success"] == "all steps"
    assert rule_for(rules, "zzz-999") == {}


def test_scenario_shape_falls_back_to_the_phase_3_row():
    screen = {"type": "decision_scenario", "id": "x-001"}
    assert "no branch JSON in the storyboard block yet" in scenario_shape(screen)
    row = {"rules": "3 nodes, +1 per correct route"}
    shape = scenario_shape(screen, row)
    assert "not in the storyboard block yet" in shape
    assert "3 nodes, +1 per correct route" in shape
    authored = {"type": "decision_scenario", "id": "x-002",
                "nodes": [{"choices": [{"goto_node_id": "n2"}, {"goto_node_id": None}]}]}
    assert scenario_shape(authored) == "1 decision nodes · 2 authored choices · 1 explicit branches"


def test_has_feedback_reads_the_authored_blocks():
    assert has_feedback({"feedback": {"correct_html": "ok"}})
    assert has_feedback({"options": [{"feedback_html": "why"}]})
    assert has_feedback({"nodes": [{"choices": [{"feedback_html": "why"}]}]})
    assert has_feedback({"items": [{"explain_html": "why"}]})
    assert not has_feedback({"prompt_html": "question"})


def test_suspend_estimate_is_conservative_and_documented():
    assert suspend_estimate([], []) == 0
    assert suspend_estimate([{}] * 26, [{}] * 13) == 26 * 24 + 13 * 48
