#!/usr/bin/env python3
"""Refresh the results table in 00_program/draft-builds.md from each module's build output.

Reads ``<module>/build/build-report.json``, ``asset-map.json`` and ``course-spec.json``
(written by ``build_course_spec.py`` + ``edumints_build.py``) and replaces the table between
the ``<!-- builds:start -->`` / ``<!-- builds:end -->`` markers. Everything else in the file
is hand-written and left alone.

    python3 elearning-course/scorm-plans/tools/draft_builds_report.py
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
DOC = PLANS / "00_program" / "draft-builds.md"


def table() -> str:
    rows = ["| Module | SCORM | Screens | Scored | lint errors | lint warnings | validate | Package | KB | Pending media | Companions placed | Explore-hotspot rules |",
            "|---|---|---:|---:|---:|---|---|---|---:|---:|---:|---:|"]
    for d in sorted(PLANS.glob("0[1-8]_*")):
        b = d / "build"
        if not (b / "build-report.json").exists():
            rows.append(f"| {d.name[:2]} | — | — | — | — | not built | — | — | — | — | — | — |")
            continue
        r = json.loads((b / "build-report.json").read_text())
        a = json.loads((b / "asset-map.json").read_text())
        s = json.loads((b / "course-spec.json").read_text())
        lint = r.get("lint_course") or {}
        codes = collections.Counter(i["code"] for i in lint.get("issues", []))
        warns = ", ".join(f"`{k}`×{v}" if v > 1 else f"`{k}`" for k, v in codes.items()) or "—"
        pend = sum(1 for k, v in a["assets"].items() if v.get("status") == "PENDING" and k != "_audio")
        ok = (r.get("validate_package") or {}).get("ok")
        pkg = r.get("package") or {}
        rel = f"../{d.name}/build/"
        rows.append(
            f"| [{d.name[:2]}]({rel}) | {s['scorm_version']} | {len(s['screens'])} | "
            f"{sum(1 for x in s['screens'] if x.get('points'))} | {lint.get('error_count', '?')} | {warns} | "
            f"{'ok*' if ok else 'FAIL'} | [`{pkg.get('file', '')}`]({rel}{pkg.get('file', '')}) | "
            f"{round(pkg.get('bytes', 0) / 1024)} | {pend} | {a.get('companions_placed', 0)} | "
            f"{r.get('explore_hotspot_rules', 0)} |")
    return "\n".join(rows)


def main() -> None:
    text = DOC.read_text()
    block = f"<!-- builds:start -->\n{table()}\n<!-- builds:end -->"
    if "<!-- builds:start -->" in text:
        text = re.sub(r"<!-- builds:start -->.*?<!-- builds:end -->", block, text, flags=re.S)
    else:  # first run: replace the first markdown table that starts with "| Module | SCORM"
        text = re.sub(r"\| Module \| SCORM.*?\n(?=\n)", block + "\n", text, count=1, flags=re.S)
    DOC.write_text(text)
    print(table())


if __name__ == "__main__":
    main()
