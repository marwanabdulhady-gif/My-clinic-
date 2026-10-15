#!/usr/bin/env python3
"""Rebuild the offline SCORM schema directory used for manifest XSD validation.

``validate_package`` fetches the IMS/W3C schemas from ``imsglobal.org`` / ``w3.org`` on first use
(only the ADL files are vendored inside edumints), which sandboxes without network access cannot
reach.  Setting ``SCORM_SCHEMA_DIR`` switches validation to the fully offline path, which expects
one flat directory per SCORM generation::

    <SCORM_SCHEMA_DIR>/12/     driver_12.xsd + every adl/*.xsd + the IMS/W3C schemas for SCORM 1.2
    <SCORM_SCHEMA_DIR>/2004/   driver_2004.xsd + every adl/*.xsd + the IMS/W3C schemas for 2004

The schema *files* are not committed (IMS/W3C licensing — the same reason the compiler fetches them
at runtime).  What is committed is ``00_program/xsd-schema-provenance.json``: every file with its
byte count, its sha256 and the sha256 the compiler expects.  This tool rebuilds the directory from
that record — ADL files and both drivers from the edumints checkout, everything else from the
recorded public mirrors — and verifies every byte against the recorded hash.

    python3 elearning-course/scorm-plans/tools/fetch_scorm_schemas.py --out /path/to/scorm-schemas
    SCORM_SCHEMA_DIR=/path/to/scorm-schemas EDUMINTS_DIR=/path/to/edumints-scorm-mcp \\
      .venv/bin/python elearning-course/scorm-plans/tools/edumints_build.py 01_health-and-safety-1
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
PROVENANCE = PLANS / "00_program" / "xsd-schema-provenance.json"
EDU = Path(os.environ.get("EDUMINTS_DIR", "/home/user/edumints-scorm-mcp"))
VERSION_DIRS = {"12": "12", "2004": "2004"}
DRIVERS = {"12": "driver_12.xsd", "2004": "driver_2004.xsd"}
W3_XML_RE = re.compile(r"http://www\.w3\.org/2001(?:/03)?/xml\.xsd")


def gh_contents(source: str) -> bytes:
    """Fetch one file from a ``owner/repo/path/to/file`` provenance string."""
    owner, repo, path = source.split("/", 2)
    result = subprocess.run(["gh", "api", f"repos/{owner}/{repo}/contents/{path}"],
                            capture_output=True, text=True)
    if result.returncode:
        raise SystemExit(f"gh api failed for {source}: {result.stderr.strip()[:200]}")
    payload = json.loads(result.stdout)
    if "content" not in payload:
        raise SystemExit(f"{repo}/{path} is not a file")
    return base64.b64decode(payload["content"])


def write_verified(target: Path, data: bytes, expected: str, problems: list[str]) -> None:
    """Write ``data`` to ``target`` after checking it against ``expected``.

    The expected hash always covers the bytes as recorded — for the two schemas that import
    ``xml.xsd`` by absolute URL the local-relative rewrite happens before this call, and the record
    pins the rewritten bytes it actually validated with.
    """
    digest = hashlib.sha256(data).hexdigest()
    if digest != expected:
        problems.append(f"{target.name}: sha256 {digest[:12]}… != recorded {expected[:12]}…")
    target.write_bytes(data)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", required=True, help="Target directory (created if missing).")
    args = parser.parse_args()
    out = Path(args.out)
    record_data = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    problems: list[str] = []
    written = 0

    vendored = record_data["vendored_from_compiler_checkout"]
    for version, dirname in VERSION_DIRS.items():
        target_dir = out / dirname
        target_dir.mkdir(parents=True, exist_ok=True)
        # Flat copy of the vendored ADL schemas plus this generation's driver, exactly as the
        # compiler's fetch path stages them.
        for source in sorted((EDU / "runtime" / "schemas" / "adl").glob("*.xsd")):
            expected = vendored[f"adl/{source.name}"]
            write_verified(target_dir / source.name, source.read_bytes(), expected, problems)
            written += 1
        driver = DRIVERS[version]
        write_verified(target_dir / driver, (EDU / "runtime" / "schemas" / driver).read_bytes(),
                       vendored[driver], problems)
        written += 1

    for version, files in record_data["mirrored"].items():
        target_dir = out / VERSION_DIRS[version]
        target_dir.mkdir(parents=True, exist_ok=True)
        for name, info in files.items():
            raw = gh_contents(info["source"])
            # The record pins the mirror bytes (the same the compiler hashes from the URL).  The
            # xml.xsd import is rewritten to the local-relative form afterwards, because that is
            # what validation loads from disk.
            if hashlib.sha256(raw).hexdigest() != info["sha256"]:
                problems.append(f"{target_dir.name}/{name}: mirror bytes differ from the record")
            if info.get("xml_xsd_import_rewritten"):
                raw = W3_XML_RE.sub("xml.xsd", raw.decode("utf-8")).encode("utf-8")
            target_dir.joinpath(name).write_bytes(raw)
            written += 1

    print(f"wrote {written} schema files into {out}")
    for row in record_data.get("substitutions", []):
        print(f"note: {row['version']}/{row['file']} is the documented substitute — {row['why'][:120]}…")
    if problems:
        print("\n".join("FAIL " + p for p in problems), file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
