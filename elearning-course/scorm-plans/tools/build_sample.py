#!/usr/bin/env python3
"""Build the Oracle pilot sample: a short, fully branded showcase package.

Why a sample: My Clinic runs Oracle Applications Cloud (Fusion HCM), so the courses will be
hosted in Oracle Learning. The sample lets their LMS administrator upload one small package,
launch it, and check that completion, score, pass/fail, objectives, interactions and resume
are recorded — before the eight real packages arrive. It is compiled by the **same pipeline**
as the real courses (`edumints_build.py`), so a pass here is evidence for all eight.

Content is deliberately low-risk and standard (WHO patient-identification and hand-hygiene
practice, RACE/PASS fire response). It does not depend on any open My Clinic decision; it is
still marked as a sample, not reviewed by My Clinic SMEs.

    python3 elearning-course/scorm-plans/tools/build_sample.py 1.2     # → build/course-spec.json
    python3 elearning-course/scorm-plans/tools/build_sample.py 2004
then compile with `edumints_build.py 00_sample-oracle-pilot` (see the sample README).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_course_spec import (BRAND, CHARS, PLANS, data_uri, explore_hotspot_css,  # noqa: E402
                               web_companion)

SAMPLE = PLANS / "00_sample-oracle-pilot"
A = lambda aid: f"{{{{asset:{aid}}}}}"  # noqa: E731 — inline asset token for *_html fields


def host(who: str) -> str:
    if who == "noor":
        return f'<div class="mc-host noor">{A("char-noor-avatar-neutral")}<span>Noor · Safety liaison</span></div>'
    return f'<div class="mc-host omar">{A("char-omar-avatar-neutral")}<span>Dr. Omar · Family physician</span></div>'


SCREENS = [
    # A — Welcome
    {"type": "title_slide", "id": "mcs-000", "title": "Welcome to My Clinic e-learning",
     "subtitle": "A short sample course · about 8 minutes", "section": "Welcome", "node_id": "mcs-sA",
     "body_html": '<p>Sample for Oracle Learning · SCORM test</p>'
                  f'<div class="mc-motion">{A("mcs-mg-pulse")}</div>'
                  f'<div class="mc-guides"><div class="mc-guide omar">{A("char-omar-welcome")}<span>Dr. Omar</span></div>'
                  f'<div class="mc-guide noor">{A("char-noor-welcome")}<span>Noor</span></div></div>',
     "animation": "fade", "reveal": "auto",
     "narration_text": "Dr. Omar: Welcome to My Clinic. I'm Dr. Omar, a family physician. Noor: And I'm Noor, a senior nurse. In eight minutes we'll show you how our courses look, feel and track your progress."},
    {"type": "content_slide", "id": "mcs-001", "title": "How this sample works", "section": "Welcome", "node_id": "mcs-sA",
     "layout": "text_media", "media_asset_id": "char-noor-explaining", "media_alt": "Noor, the course guide, explaining.",
     "body_html": "<ul><li><strong>Three short topics</strong> — the right patient, fire response, clean hands</li>"
                  "<li><strong>Try every interaction</strong> — explore, flip, sort, drag and decide</li>"
                  "<li><strong>Four scored checks</strong> — pass mark 80%</li>"
                  "<li><strong>Leave and come back</strong> — the course remembers where you were</li></ul>",
     "animation": "fade-up", "reveal": "auto",
     "narration_text": "Noor: Three short topics, four quick checks. Close it halfway if you like: when you come back, you pick up where you left off."},
    # B — The right patient
    {"type": "content_slide", "id": "mcs-010", "title": "The right patient, every time", "section": "The right patient", "node_id": "mcs-sB",
     "layout": "text_media", "media_asset_id": "mcs-mg-identify",
     "media_alt": "A patient wristband: full name and date of birth or record number are ticked; room or bed number is crossed out.",
     "body_html": "<p>Before any test, medicine or procedure, confirm <strong>two identifiers</strong>:</p>"
                  "<ul><li><strong>Full name</strong></li><li><strong>Date of birth</strong> or <strong>medical record number</strong></li></ul>"
                  "<p>Ask the patient to say them, then match the wristband or record. <strong>Never</strong> use a room or bed number.</p>",
     "animation": "slide-left", "reveal": "auto",
     "narration_text": "Dr. Omar: Two identifiers, every time: the full name and the date of birth or record number. Ask the patient to say them, then check the band. A room number is not an identifier: patients move."},
    {"type": "flashcards", "id": "mcs-011", "title": "Identifier or not?", "section": "The right patient", "node_id": "mcs-sB",
     "prompt_html": "<p>Flip each card. Is it a safe patient identifier?</p>",
     "cards": [
         {"front_html": "<h3>Full name</h3>", "back_html": "<p>✔ <strong>Yes.</strong> Ask the patient to say it, then compare it with the band.</p>"},
         {"front_html": "<h3>Date of birth</h3>", "back_html": "<p>✔ <strong>Yes.</strong> The usual second identifier.</p>"},
         {"front_html": "<h3>Medical record number</h3>", "back_html": "<p>✔ <strong>Yes.</strong> Unique to one patient in the system.</p>"},
         {"front_html": "<h3>Room or bed number</h3>", "back_html": "<p>✘ <strong>No.</strong> Patients move rooms; a location never identifies a person.</p>"}],
     "animation": "zoom", "reveal": "auto",
     "narration_text": "Noor: Flip the cards. Three are safe identifiers, one is a trap I've seen catch good nurses."},
    {"type": "decision_scenario", "id": "mcs-012", "title": "Two patients, one name", "section": "The right patient", "node_id": "mcs-sB",
     "objective_ids": ["mcs-o1"], "points": 20, "evidence_screen_ids": ["mcs-010"], "pass_score": 2, "start_node_id": "n1",
     "intro_html": host("noor") + "<p>Two patients named <strong>Mohammed Al-Harbi</strong> are waiting for blood tests. You call the name and one of them stands up. (Fictional training example.)</p>",
     "nodes": [
         {"id": "n1", "prompt_html": "<p>He walks over and holds out his arm. What do you do?</p>", "choices": [
             {"id": "a", "text_html": "Ask him to say his full name and date of birth, and check both against his wristband and the request.", "score_delta": 1, "goto_node_id": "n2",
              "feedback_html": "<p><strong>Best choice.</strong> Two identifiers, said by the patient and matched to the band, catch exactly this mix-up.</p>"},
             {"id": "b", "text_html": "He answered to the name, so take the sample.", "score_delta": 0, "goto_node_id": "n2",
              "feedback_html": "<p>Risky. Two patients share that name: answering to it proves nothing. Ask for a second identifier.</p>"},
             {"id": "c", "text_html": "Check the waiting-room seat number on your list.", "score_delta": 0, "goto_node_id": "n2",
              "feedback_html": "<p>A seat or room number is a location, not an identifier. Use the name plus date of birth or record number.</p>"}]},
         {"id": "n2", "prompt_html": "<p>His date of birth does not match the request. What next?</p>", "choices": [
             {"id": "a", "text_html": "Stop, explain kindly, and check the request with the other patient of the same name.", "score_delta": 1,
              "feedback_html": "<p><strong>Right.</strong> A mismatch means stop. You just prevented a wrong-patient result.</p>"},
             {"id": "b", "text_html": "Take the sample and fix the label later.", "score_delta": 0,
              "feedback_html": "<p>Never. A mislabelled sample can lead to the wrong treatment for both patients.</p>"},
             {"id": "c", "text_html": "Ask a colleague which one is the right Mohammed.", "score_delta": 0,
              "feedback_html": "<p>A colleague's memory is not an identifier. Check the identifiers against the request.</p>"}]}],
     "feedback": {"correct_html": "<p><strong>Well done.</strong> You asked for two identifiers and stopped at the mismatch: that is how wrong-patient errors are prevented.</p>",
                  "incorrect_html": "<p>Answering to a name, a seat number or a colleague's memory is not identification. Ask for two identifiers and stop if they do not match.</p>"},
     "narration_text": "Noor: I once nearly drew blood from the wrong Mr Al-Harbi. The wristband stopped me. Your turn."},
    # C — Fire response
    {"type": "hotspot", "id": "mcs-020", "title": "Find the fire safety equipment", "section": "Fire response", "node_id": "mcs-sC",
     "prompt_html": "<p>Open every item. Know where these are before you need them.</p>",
     "image_asset_id": "hs1-img-corridor",
     "image_alt": "Clinic corridor showing a smoke detector, heat detector, sprinkler, call point, extinguisher, fire blanket, evacuation chair and assembly-point sign.",
     "mode": "explore", "require_all": True, "regions": "__FROM_HS1_404__",
     "feedback": {"correct_html": "<p><strong>All eight found.</strong> Detection, alarm, first response and escape route: check where each one is in your own clinic this week.</p>",
                  "incorrect_html": "<p>Open every item to see what it does and when you use it.</p>"},
     "animation": "fade-up", "reveal": "auto",
     "narration_text": "Dr. Omar: Walk the corridor. Open each item: in a real fire you won't have time to look for them."},
    {"type": "content_slide", "id": "mcs-021", "title": "If you find a fire: RACE", "section": "Fire response", "node_id": "mcs-sC",
     "layout": "full_media", "media_asset_id": "mcs-mg-race",
     "media_alt": "RACE: Rescue, Alarm, Contain, Extinguish or Evacuate, appearing one step at a time. PASS: pull, aim, squeeze, sweep.",
     "body_html": "<p><strong>R</strong>escue anyone in danger · <strong>A</strong>larm — pull the call point and call your clinic's fire code · <strong>C</strong>ontain — close doors · <strong>E</strong>xtinguish a small fire, or <strong>E</strong>vacuate.</p>",
     "animation": "fade", "reveal": "auto",
     "narration_text": "Dr. Omar: People first, then the alarm, then close the doors. Only fight a small fire, with the right extinguisher: pull, aim, squeeze, sweep."},
    {"type": "sorting", "id": "mcs-022", "title": "Put RACE in order", "section": "Fire response", "node_id": "mcs-sC",
     "objective_ids": ["mcs-o2"], "points": 10, "evidence_screen_ids": ["mcs-021"],
     "prompt_html": "<p>Smoke is coming from a consultation room. Put your actions in the right order.</p>",
     "items": [
         {"id": "r", "text_html": "<strong>Rescue</strong> — move the patient out of the room"},
         {"id": "a", "text_html": "<strong>Alarm</strong> — pull the call point and call the fire code"},
         {"id": "c", "text_html": "<strong>Contain</strong> — close the door behind you"},
         {"id": "e", "text_html": "<strong>Extinguish or evacuate</strong> — small fire: extinguisher; otherwise leave"}],
     "feedback": {"correct_html": "<p><strong>Correct.</strong> People first; the alarm brings help; a closed door holds smoke back for minutes.</p>",
                  "incorrect_html": "<p>Not quite. Rescue comes first, then raise the alarm, then contain the fire before you try to put it out.</p>",
                  "show_correct_answer": True},
     "narration_text": "Dr. Omar: Smoke from a consultation room. Put your four actions in order."},
    {"type": "mcq", "id": "mcs-023", "title": "Using the extinguisher", "section": "Fire response", "node_id": "mcs-sC",
     "objective_ids": ["mcs-o2"], "points": 10, "evidence_screen_ids": ["mcs-021"],
     "prompt_html": "<p>A small bin fire. You have the right extinguisher. After you <strong>pull the pin</strong>, where do you aim?</p>",
     "options": [
         {"id": "a", "text_html": "At the base of the fire, then sweep side to side.", "correct": True,
          "feedback_html": "<p>Correct. The fuel is at the base: aim low, squeeze, sweep.</p>"},
         {"id": "b", "text_html": "At the top of the flames, where they are highest.", "correct": False,
          "feedback_html": "<p>The flames are not the fuel. Aiming high wastes the extinguisher.</p>"},
         {"id": "c", "text_html": "At the smoke, to clear the air.", "correct": False,
          "feedback_html": "<p>Smoke is not burning. Aim at the base of the fire.</p>"}],
     "feedback": {"correct_html": "<p><strong>PASS:</strong> Pull · Aim low · Squeeze · Sweep.</p>",
                  "incorrect_html": "<p>Remember PASS: Pull · Aim at the base · Squeeze · Sweep.</p>", "show_correct_answer": True},
     "narration_text": "Noor: One quick check on the extinguisher."},
    # D — Clean hands
    {"type": "content_slide", "id": "mcs-030", "title": "Five moments for clean hands", "section": "Clean hands", "node_id": "mcs-sD",
     "layout": "full_media", "media_asset_id": "mcs-mg-moments",
     "media_alt": "WHO five moments for hand hygiene appearing one by one around the patient zone.",
     "body_html": "<p>Clean your hands at the five moments around the patient zone (WHO). It protects the patient — and you.</p>",
     "animation": "fade", "reveal": "auto",
     "narration_text": "Noor: Two moments come before you touch, three come after. Watch where each one sits around the patient."},
    {"type": "drag_drop", "id": "mcs-031", "title": "Which moment is it?", "section": "Clean hands", "node_id": "mcs-sD",
     "objective_ids": ["mcs-o3"], "points": 20, "evidence_screen_ids": ["mcs-030"],
     "prompt_html": "<p>Drag each situation to its hand-hygiene moment.</p>",
     "items": [
         {"id": "i1", "text_html": "You are about to take a patient's blood pressure", "correct_target_id": "m1"},
         {"id": "i2", "text_html": "You are about to dress a wound", "correct_target_id": "m2"},
         {"id": "i3", "text_html": "You have just emptied a urine bag", "correct_target_id": "m3"},
         {"id": "i4", "text_html": "You have just helped a patient onto the couch", "correct_target_id": "m4"},
         {"id": "i5", "text_html": "You have just adjusted the patient's bed rail and left", "correct_target_id": "m5"}],
     "targets": [
         {"id": "m1", "label_html": "1 · Before touching a patient"},
         {"id": "m2", "label_html": "2 · Before a clean / aseptic task"},
         {"id": "m3", "label_html": "3 · After body-fluid exposure risk"},
         {"id": "m4", "label_html": "4 · After touching a patient"},
         {"id": "m5", "label_html": "5 · After touching patient surroundings"}],
     "feedback": {"correct_html": "<p><strong>All five right.</strong> Before you touch, before clean tasks; after fluids, after the patient, after their surroundings.</p>",
                  "incorrect_html": "<p>Not quite. Ask: am I about to touch (1, 2) or have I just touched (3, 4, 5)? Then: the patient, a clean task, body fluids, or only their surroundings?</p>",
                  "show_correct_answer": True},
     "narration_text": "Noor: Five everyday situations. Match each one to its moment."},
    # Z — Results
    {"type": "results_breakdown", "id": "mcs-090", "title": "Your results", "section": "Results", "node_id": "mcs-sZ",
     "body_html": "<p>Your results by topic. Pass mark: 80% (48 of 60 points).</p>",
     "sections": [
         {"title": "The right patient", "screen_ids": ["mcs-012"], "advice_html": "<p>Revisit <strong>The right patient</strong> from the menu.</p>"},
         {"title": "Fire response", "screen_ids": ["mcs-022", "mcs-023"], "advice_html": "<p>Revisit <strong>Fire response</strong> from the menu.</p>"},
         {"title": "Clean hands", "screen_ids": ["mcs-031"], "advice_html": "<p>Revisit <strong>Clean hands</strong> from the menu.</p>"}],
     "narration_text": "Dr. Omar: Here's how you did, topic by topic."},
    {"type": "summary", "id": "mcs-091", "title": "That's how our courses work", "section": "Results", "node_id": "mcs-sZ",
     "body_html": f'{host("omar")}<p>Two identifiers · RACE and PASS · five moments.</p>'
                  "<p><strong>For the LMS team:</strong> your Oracle Learning record should now show this course as completed, with a score, passed or failed, and the three topic results.</p>",
     "show_score": True, "show_completion": True,
     "narration_text": "Dr. Omar: That's the sample. Noor: The full courses work the same way, with more practice and real My Clinic scenarios."},
]


def build(version: str) -> dict:
    hs = next(s for s in json.loads((PLANS / "01_health-and-safety-1/build/screens.json").read_text())
              if s["id"] == "hs1-404")
    assets: dict[str, dict] = {}

    def add(aid: str, path: Path) -> None:
        src = web_companion(path) if aid.startswith("char-") else data_uri(path)
        assets[aid] = {"id": aid, "filename": f"{aid}{path.suffix}", "source": src}

    for f in (SAMPLE / "assets").glob("*.svg"):
        add(f.stem, f)
    add("hs1-img-corridor", PLANS / "01_health-and-safety-1/storyboard/assets/hs1-img-corridor.png")
    for c in ("char-omar-welcome", "char-noor-welcome", "char-noor-explaining",
              "char-noor-avatar-neutral", "char-omar-avatar-neutral"):
        add(c, CHARS / "assets" / f"{c}.png")
    add("brand-logo-horizontal-navy", BRAND / "logo-horizontal-navy.png")
    import base64
    for w in (400, 600, 700):
        f = BRAND.parent / "fonts" / f"montserrat-latin-{w}-normal.woff2"
        assets[f"font-montserrat-{w}"] = {"id": f"font-montserrat-{w}", "filename": f.name,
                                          "source": "data:font/woff2;base64," + base64.b64encode(f.read_bytes()).decode()}
    screens = json.loads(json.dumps(SCREENS))
    for s in screens:
        if s.get("regions") == "__FROM_HS1_404__":
            s["regions"] = hs["regions"]
    spec = {
        "schema_version": "1.0",
        "title": "My Clinic — Sample course for Oracle Learning",
        "description": "Short branded sample to test My Clinic e-learning in Oracle Learning: completion, score, pass/fail, objectives, interactions and resume.",
        "scorm_version": version, "language": "en", "theme": "__BRAND__", "theme_mode": "light",
        "tracking": {"completion_rule": "viewed_all_and_passed", "passing_score": 80},
        "layout_mode": "stage",
        "metadata": {"description": "My Clinic e-learning sample for LMS compatibility testing.",
                     "keywords": ["My Clinic", "sample", "Oracle Learning", "SCORM"], "typical_learning_time": "PT8M"},
        "objectives": [
            {"id": "mcs-o1", "description": "Confirm a patient's identity with two identifiers."},
            {"id": "mcs-o2", "description": "Respond to a fire with RACE and use an extinguisher with PASS."},
            {"id": "mcs-o3", "description": "Match everyday tasks to the five moments for hand hygiene."}],
        "outline": [{"id": n, "kind": "section", "title": t, "unlock_rule": "free"} for n, t in
                    [("mcs-sA", "Welcome"), ("mcs-sB", "The right patient"), ("mcs-sC", "Fire response"),
                     ("mcs-sD", "Clean hands"), ("mcs-sZ", "Results")]],
        "screens": screens,
        "assets": list(assets.values()),
    }
    spec["__extra_css"] = explore_hotspot_css(screens, assets)
    out = SAMPLE / "build"
    out.mkdir(exist_ok=True)
    (out / "course-spec.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    (out / "asset-map.json").write_text(json.dumps(
        {"companions_placed": 5, "assets": {k: {"status": "file"} for k in assets}}, indent=2))
    print(f"sample SCORM {version}: {len(screens)} screens, {sum(1 for s in screens if s.get('points'))} scored, "
          f"{len(assets)} assets")
    return spec


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "1.2")
