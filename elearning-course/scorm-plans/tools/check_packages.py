#!/usr/bin/env python3
"""Play every packaged course in a real browser on a mock SCORM 1.2 LMS and check what it reports.

    python3 tools/check_packages.py                 # all modules + the Oracle sample
    python3 tools/check_packages.py 04 07           # only these

For each package it runs tools/player/test/play.js three times:
  * right   — answers every activity correctly → must end "passed", score 100 (or the known gap below)
  * wrong   — answers every activity wrongly   → must end "failed"
  * resume  — closes the course after 6 screens and relaunches → must reopen on the same screen
and fails on any JavaScript error or a screen where Next stays locked.

Needs Node with Playwright (preinstalled in the cloud sessions at /opt/node-tools) and Chromium.
"""
from __future__ import annotations

import concurrent.futures as cf
import functools
import http.server
import json
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
TEST = Path(__file__).resolve().parent / "player" / "test"
# activities that cannot be answered correctly until a decision closes (score below 100 is expected)
KNOWN = {"07": "qsr-032 has no accepted risk band until B6 closes"}


def run(base: str, folder: str, *args: str) -> dict:
    p = subprocess.run(["node", str(TEST / "play.js"), base, folder, *args], capture_output=True, text=True, timeout=900)
    line = next((l for l in p.stdout.splitlines() if l.startswith("{")), None)
    return json.loads(line) if line else {"errs": [p.stderr.strip()[-400:] or "no output"]}


def main() -> int:
    want = set(sys.argv[1:])
    mods = [d for d in sorted(PLANS.glob("0*_*")) if (d / "build" / "package" / "index.html").exists()
            and (not want or d.name[:2] in want)]
    www = Path(tempfile.mkdtemp(prefix="mc-lms-"))
    (www / "lms.html").write_text((TEST / "lms.html").read_text())
    for d in mods:
        (www / d.name[:2]).symlink_to(d / "build" / "package")
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(www)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    jobs = {}
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for d in mods:
            k = d.name[:2]
            jobs[(k, "right")] = ex.submit(run, base, k, "right")
            jobs[(k, "wrong")] = ex.submit(run, base, k, "wrong")
            jobs[(k, "resume")] = ex.submit(run, base, k, "right", "", "6")
    srv.shutdown()
    fails = 0
    for d in mods:
        k = d.name[:2]
        r, w, z = (jobs[(k, m)].result() for m in ("right", "wrong", "resume"))
        problems = r.get("errs", []) + w.get("errs", []) + z.get("errs", [])
        if r.get("status") != "passed":
            problems.append(f"all-correct run ended {r.get('status')}")
        if r.get("score") != "100" and k not in KNOWN:
            problems.append(f"all-correct score {r.get('score')}")
        if w.get("status") != "failed":
            problems.append(f"all-wrong run ended {w.get('status')}")
        note = f" (expected: {KNOWN[k]})" if k in KNOWN and r.get("score") != "100" else ""
        print(f"{k}: right {r.get('status')} {r.get('score')}{note} · wrong {w.get('status')} {w.get('score')} · "
              f"{r.get('screens')} screens · {r.get('interactions')} interactions · resume "
              f"{'ok' if not z.get('errs') else 'FAIL'}" + ("" if not problems else " · PROBLEMS: " + "; ".join(problems)))
        fails += bool(problems)
    print(f"packages={len(mods)} failures={fails}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
