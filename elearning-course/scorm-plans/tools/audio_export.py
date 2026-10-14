#!/usr/bin/env python3
"""Canonical narration → audio-production export for the My Clinic programme.

One implementation of the rules that every pack must obey, so a regenerated pack can never
silently regress them:

* **Speaker labels are routing, not speech.** ``OMAR:`` / ``NOOR:`` select the voice and stay in
  ``narration`` and ``narration_text`` (captions), but ``tts_text`` / ``ssml`` never contain them
  (the bug this module fixes: the TTS voice read the label aloud).
* **One recording segment per spoken line.** A two-voice screen is split into segments with
  ``part`` = ``omar-1`` / ``noor-1`` (companions.md §5); single-voice screens use ``part`` =
  ``omar`` / ``noor``. The audio file per screen is joined afterwards.
* **One voice block.** Every ``narration-script.json`` carries the same companion persona text
  (provider and voice ids stay ``null`` until programme decision D10 closes).
* **One export schema.** ``audio-script-export.json`` always has
  ``module_id, language, wpm, voices, generated_by, total_est_sec, segments, voice_talent_md``
  and every segment has ``screen_id, part, speaker, filename, narration_text, tts_text, ssml,
  est_sec, cues, timing_source``.

The lexicon, pause/cue handling and SSML generation mirror the edumints server's
``core.playbook.export_audio_script`` (revision 4bbf4591) so the output is what the server would
produce for the same input; the speaker handling is the programme improvement on top of it.
"""
from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path
from typing import Any

WPM = 140
MAX_SEGMENT_SEC = 60.0
MAX_SENTENCE_WORDS = 25
PAUSE_JOIN_SEC = 0.3
TOOL_REVISION = "4bbf4591cf8a3ffcb63909fcb69f0547e1654db0"

MARK_RE = re.compile(r"\[\[[^\]]*\]\]")
CUE_RE = re.compile(r"\[\[cue:([A-Za-z0-9_.-]+)\]\]")
PAUSE_RE = re.compile(r"\[\[pause:(\d+(?:\.\d+)?)\]\]")
WORD_RE = re.compile(r"[\w'’-]+", re.UNICODE)
SPEAKER_RE = re.compile(r"^(NOOR|OMAR):\s*", re.M)

VOICE_BRIEFS = {
    "noor": "Female, early-to-mid 30s, warm, calm and clear; international English with a light "
            "Gulf Arabic accent welcome; smiling but not bubbly; ~140 wpm",
    "omar": "Male, late 30s, friendly, confident and relaxed; international English with a light "
            "Gulf Arabic accent welcome; medium-low pitch; ~140 wpm",
}
VOICE_PERSONA = (
    "Two fixed companion voices (companions.md §5): Dr. Omar, lead host — male, late 30s, "
    "friendly, confident, medium-low pitch; Noor, co-host — female, early-to-mid 30s, warm, calm, "
    "clear. Neither voice may be cloned from or resemble a real employee. Provider and voice ids "
    "pending program D10."
)


def words(text: str) -> list[str]:
    return WORD_RE.findall(text or "")


def spoken(text: str) -> str:
    """Caption text: markers removed, whitespace collapsed, speaker labels kept."""
    return re.sub(r"\s+", " ", MARK_RE.sub(" ", text)).strip()


def estimate_sec(text: str, wpm: int = WPM) -> float:
    pauses = sum(float(p) for p in PAUSE_RE.findall(text))
    return round(len(words(spoken(text))) / wpm * 60.0 + pauses, 1)


def speakers_of(text: str) -> list[str]:
    return [m.group(1).lower() for m in SPEAKER_RE.finditer(text)]


def tts_text(text: str, lexicon: dict[str, str]) -> str:
    """Speech input: speaker labels removed, lexicon readings applied."""
    body = SPEAKER_RE.sub("", spoken(text))
    return apply_lexicon(body, lexicon)


def apply_lexicon(text: str, lexicon: dict[str, str]) -> str:
    if not lexicon:
        return text
    pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in sorted(lexicon, key=len, reverse=True)) + r")\b")
    return pattern.sub(lambda m: lexicon[m.group(1)], text)


def ssml_for(text: str, language: str, lexicon: dict[str, str]) -> str:
    chunks: list[str] = []
    # The speaker label routes the line to a voice; it must never reach the synthesiser.
    for token in re.split(r"(\[\[[^\]]*\]\])", SPEAKER_RE.sub("", text)):
        cue, pause = CUE_RE.fullmatch(token), PAUSE_RE.fullmatch(token)
        if cue:
            chunks.append(f'<mark name="{escape(cue.group(1), quote=True)}"/>')
        elif pause:
            chunks.append(f'<break time="{pause.group(1)}s"/>')
        elif lexicon:
            pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in sorted(lexicon, key=len, reverse=True)) + r")\b")
            pos = 0
            for match in pattern.finditer(token):
                chunks.append(escape(token[pos:match.start()], quote=True))
                chunks.append(f'<sub alias="{escape(lexicon[match.group(1)], quote=True)}">{escape(match.group(1), quote=True)}</sub>')
                pos = match.end()
            chunks.append(escape(token[pos:], quote=True))
        else:
            chunks.append(escape(token, quote=True))
    body = re.sub(r"\s+", " ", "".join(chunks)).strip()
    return f'<speak xml:lang="{escape(language, quote=True)}">{body}</speak>'


def cue_times(text: str, wpm: int = WPM) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    clock = 0.0
    sec_per_word = 60.0 / wpm
    for token in re.split(r"(\[\[[^\]]*\]\])", text):
        cue, pause = CUE_RE.fullmatch(token), PAUSE_RE.fullmatch(token)
        if cue:
            out.append({"cue": cue.group(1), "at_sec": round(clock, 1)})
        elif pause:
            clock += float(pause.group(1))
        else:
            clock += len(words(token)) * sec_per_word
    return out


def split_segment(segment: dict[str, Any]) -> list[dict[str, Any]]:
    """Split a segment that mixes speakers into one segment per spoken line.

    Already-split segments (a single label) are returned unchanged but gain their ``part`` and
    ``speaker`` fields. Parts are numbered per screen in order of first appearance.
    """
    text = segment["narration"]
    labels = speakers_of(text)
    if len(set(labels)) <= 1:
        speaker = labels[0] if labels else None
        part = segment.get("part") or speaker
        out = dict(segment)
        out["speaker"] = speaker
        out["part"] = part
        return [out]

    blocks: list[tuple[str, list[str]]] = []
    for line in text.splitlines():
        match = SPEAKER_RE.match(line.strip())
        if not match:
            if blocks:
                blocks[-1][1].append(line)
            continue
        speaker = match.group(1).lower()
        if blocks and blocks[-1][0] == speaker:
            blocks[-1][1].append(line)
        else:
            blocks.append((speaker, [line]))

    parts: list[dict[str, Any]] = []
    seen: dict[str, int] = {}
    total_words = max(1, sum(len(words(spoken(b_text))) for _, lines in blocks for b_text in lines))
    target = segment.get("target_sec")
    for speaker, lines in blocks:
        seen[speaker] = seen.get(speaker, 0) + 1
        line_text = "\n".join(lines).strip()
        part = speaker if len(blocks) == 1 else f"{speaker}-{seen[speaker]}"
        share = len(words(spoken(line_text))) / total_words
        part_segment = dict(segment)
        part_segment["narration"] = line_text
        part_segment["speaker"] = speaker
        part_segment["part"] = part
        if target:
            part_segment["target_sec"] = max(5.0, round(float(target) * share))
        parts.append(part_segment)
    return parts


def voices_block(lead: str | None = None) -> dict[str, Any]:
    voices = {
        name: {
            "label": "OMAR:" if name == "omar" else "NOOR:",
            "brief": VOICE_BRIEFS[name],
            "provider": "external",
            "voice_id": None,
            "status": "pending program D10",
        }
        for name in ("omar", "noor")
    }
    return voices


def voice_record() -> dict[str, Any]:
    return {"provider": "external", "voice_id": None, "persona": VOICE_PERSONA, "gender": None}


def build_export(script: dict[str, Any], lead: str | None = None) -> dict[str, Any]:
    """Build the canonical audio-script export from a narration-script dict."""
    wpm = script.get("wpm") or WPM
    lexicon = script.get("lexicon") or {}
    language = script.get("language", "en")
    segments: list[dict[str, Any]] = []
    for segment in script["segments"]:
        narration = segment["narration"]
        speaker = segment.get("speaker") or (speakers_of(narration) or [None])[0]
        part = segment.get("part") or speaker
        part_suffix = f"_{part}" if part and part != speaker else ""
        segments.append({
            "screen_id": segment["screen_id"],
            "part": part,
            "speaker": speaker,
            "filename": f"{script['module_id']}_{segment['screen_id']}{part_suffix}.mp3",
            "narration_text": spoken(narration),
            "tts_text": tts_text(narration, lexicon),
            "ssml": ssml_for(narration, language, lexicon),
            "est_sec": estimate_sec(narration, wpm),
            "cues": cue_times(narration, wpm),
            "timing_source": "estimated_word_count",
        })
    return {
        "module_id": script["module_id"],
        "language": language,
        "wpm": wpm,
        "voices": voices_block(lead),
        "generated_by": "tools/audio_export.py (edumints core.playbook export rules, rev "
                        f"{TOOL_REVISION[:8]})",
        "total_est_sec": round(sum(item["est_sec"] for item in segments), 1),
        "segments": segments,
        "voice_talent_md": voice_talent_md(script, segments, lead),
    }


def voice_talent_md(script: dict[str, Any], segments: list[dict[str, Any]], lead: str | None = None) -> str:
    wpm = script.get("wpm") or WPM
    lexicon = script.get("lexicon") or {}
    counts: dict[str, int] = {}
    for item in segments:
        counts[item["speaker"] or "unknown"] = counts.get(item["speaker"] or "unknown", 0) + 1
    order = sorted(counts, key=lambda name: (name != (lead or "omar"), name))
    lines = [
        f"# Voice-over script — {script['module_id']}",
        "",
        f"Language: {script.get('language', 'en')} · Pace: ~{wpm} wpm · Two voices: **Dr. Omar** "
        "(lead host) and **Noor** (co-host) — [`companions.md`](../../00_program/characters/companions.md) §5.",
        "",
        "## Voices",
        "",
        "| Voice | Brief | Lines in this module | Provider / voice id |",
        "|---|---|---|---|",
    ]
    for name in order:
        label = "**Dr. Omar** (`OMAR:`)" if name == "omar" else "**Noor** (`NOOR:`)"
        lines.append(f"| {label} | {VOICE_BRIEFS.get(name, '—')} | {counts[name]} | Pending program **D10** |")
    lines += [
        "",
        "Neither voice may be cloned from, or resemble, a real My Clinic employee. Record a "
        "30-second sample of each voice reading a “meet your guide” line for approval before "
        "producing this module. Once D10 closes, record the provider and voice ids in "
        "`00_program/narration-and-lexicon.md` §1 and in `narration-script.json` → `voice`.",
        "",
        "The speaker label (`OMAR:` / `NOOR:`) selects the voice and is **not** spoken; "
        "`tts_text` in [`audio-script-export.json`](audio-script-export.json) already has it "
        "removed and the lexicon applied. Two-voice screens are recorded as one file per `part` "
        f"and joined with {PAUSE_JOIN_SEC} s of silence (companions.md §5).",
        "",
        "## Pronunciation guide",
        "",
    ]
    lines += [f"- **{term}** → {sound}" for term, sound in lexicon.items() if term not in {"NOOR", "OMAR"}]
    lines += ["", "## Recording table", "", "| # | Screen / part | Speaker | Tone | Script | Est. sec | File |",
              "|---|---|---|---|---|---|---|"]
    for i, (item, source) in enumerate(zip(segments, script["segments"]), 1):
        label = item["screen_id"] + (f"/{item['part']}" if item["part"] and item["part"] != item["speaker"] else "")
        script_cell = re.sub(r"\[\[pause:(\d+(?:\.\d+)?)\]\]", r"*(pause \1s)*", CUE_RE.sub("", source["narration"]))
        script_cell = re.sub(r"\s+", " ", script_cell).strip().replace("|", "\\|")
        tone = (source.get("tone") or "").replace("|", "\\|")
        lines.append(f"| {i} | `{label}` | {item['speaker']} | {tone} | {script_cell} | {item['est_sec']} | `{item['filename']}` |")
    return "\n".join(lines) + "\n"


def write_outputs(module_dir: Path, script: dict[str, Any], lead: str | None = None) -> dict[str, Any]:
    """Normalise a module's narration script in place and write the export + voice table."""
    story = module_dir / "storyboard"
    normalised: list[dict[str, Any]] = []
    for segment in script["segments"]:
        normalised.extend(split_segment(segment))
    script["segments"] = normalised
    script.setdefault("language", "en")
    script.setdefault("wpm", WPM)
    script["voice"] = voice_record()
    export = build_export(script, lead)
    (story / "narration-script.json").write_text(json.dumps(script, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (story / "audio-script-export.json").write_text(json.dumps(export, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (story / "voice_talent.md").write_text(export["voice_talent_md"], encoding="utf-8")
    return export


def load_script(module_dir: Path) -> dict[str, Any]:
    return json.loads((module_dir / "storyboard" / "narration-script.json").read_text(encoding="utf-8"))
