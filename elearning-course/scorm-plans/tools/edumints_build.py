#!/usr/bin/env python3
"""Compile a module's ``build/course-spec.json`` with the real edumints server code, in-process.

Runs the same functions the MCP tools expose — ``brand_to_theme``, ``build_from_spec``,
``lint_course``, ``validate_package``, ``preview`` — against a local checkout of
edumints-scorm-mcp, with auth disabled and a throwaway data directory. Nothing is mocked: the
zip, the lint findings and the validation result are the compiler's own output.

Writes into ``<module>/build/``:
  * ``<package name>.zip``      — the SCORM package (DRAFT until Phase 0 and media are closed)
  * ``preview.html``            — single-file preview for reviewers
  * ``build-report.json``       — build warnings, lint_course issues, validate_package result

Run with the edumints virtualenv (see ``00_program/build-pipeline.md`` §6):

    EDUMINTS_DIR=/path/to/edumints-scorm-mcp \\
      /path/to/venv/bin/python elearning-course/scorm-plans/tools/edumints_build.py 03_hr-employee-induction
"""
from __future__ import annotations

import asyncio
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
EDU = Path(os.environ.get("EDUMINTS_DIR", "/home/user/marwanabdulhady-gif/edumints-scorm-mcp"))
DATA = Path(tempfile.mkdtemp(prefix="edumints-"))
for k, v in {"SCORM_AUTH_ENABLED": "0", "DATA_DIR": str(DATA), "DB_PATH": str(DATA / "scorm.db"),
             "PUBLIC_BASE_URL": "http://localhost/scorm", "BUILD_SYNC_TIMEOUT_SEC": "300",
             "SCORM_NO_TTL_CLEANER": "1", "RATE_LIMIT_PER_MIN": "100000",
             "SCORM_SCHEMA_DIR": str(DATA / "no_schemas")}.items():
    os.environ.setdefault(k, v)
sys.path.insert(0, str(EDU))

import server  # noqa: E402

SHORT = {"00": "Sample", "01": "FMS", "02": "SafetyLab", "03": "WelcomeOnBoard", "04": "OpsMyCare",
         "05": "RCM-A", "06": "RCM-B", "07": "ClinicalGov", "08": "EHR"}


# Post-build player patches for edumints 4bbf459 (remove once fixed upstream; see programme
# status G18). The player writes percentages Turkish-style ("%75"); English needs "75%".
PLAYER_PATCHES = [
    ('sc.textContent="%"+scoreValue();', 'sc.textContent=scoreValue()+"%";'),
    ('pctEl.textContent="%"+pct;', 'pctEl.textContent=pct+"%";'),
]


def patch_player(html: str) -> tuple[str, int]:
    n = 0
    for old, new in PLAYER_PATCHES:
        n += html.count(old)
        html = html.replace(old, new)
    return html, n


def patch_zip(path: Path) -> int:
    import zipfile
    tmp = path.with_suffix(".tmp")
    total = 0
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "index.html":
                text, total = patch_player(data.decode("utf-8"))
                data = text.encode("utf-8")
            zout.writestr(item, data)
    tmp.replace(path)
    return total


def fn(tool):
    return getattr(tool, "fn", tool)


def dump(o):
    return o.model_dump(mode="json") if hasattr(o, "model_dump") else o


async def brand_theme(module_colour: str | None) -> dict:
    kit = json.loads((PLANS / "00_program" / "brand" / "brand-kit.edumints.json").read_text())
    from core.project import BrandKit
    res = dump(await fn(server.brand_to_theme)(BrandKit(**kit)))
    theme = res.get("theme_tokens") or res.get("theme") or res
    theme["logo_asset_id"] = "brand-logo-horizontal-navy"
    theme["logo_alt"] = "My Clinic"
    theme["custom_fonts"] = [{"family": "Montserrat", "asset_id": f"font-montserrat-{w}", "weight": w}
                             for w in (400, 600, 700)]
    import base64
    css = (PLANS / "00_program" / "brand" / "edumints-skin.css").read_text()
    for token, f in (("__MARK_NAVY__", "mark-navy.png"), ("__MARK_WHITE__", "mark-white.png")):
        b64 = base64.b64encode((PLANS / "00_program" / "brand" / "assets" / f).read_bytes()).decode()
        css = css.replace(token, "data:image/png;base64," + b64)
    if "__MARK_NAVY_FAINT__" in css:
        from io import BytesIO
        from PIL import Image
        im = Image.open(PLANS / "00_program" / "brand" / "assets" / "mark-navy.png").convert("RGBA")
        im.putalpha(im.getchannel("A").point(lambda a: int(a * 0.06)))
        buf = BytesIO(); im.save(buf, "PNG", optimize=True)
        css = css.replace("__MARK_NAVY_FAINT__", "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode())
    if module_colour:
        css = f":root{{--mc-module:{module_colour}}}\n" + css
    theme["custom_css"] = css
    if module_colour:
        theme.setdefault("color", {})["secondary"] = module_colour
    return theme


async def run(module: str) -> dict:
    mdir = PLANS / module
    out = mdir / "build"
    spec = json.loads((out / "course-spec.json").read_text())
    extra_css = spec.pop("__extra_css", "")
    report: dict = {"module": module, "edumints_revision": os.popen(f"git -C {EDU} rev-parse --short HEAD").read().strip()}
    if spec.get("theme") == "__BRAND__":
        import re
        m = re.search(r"module colour \*\*[^#*]*(#[0-9A-Fa-f]{6})", (mdir / "README.md").read_text())
        spec["theme"] = await brand_theme(m.group(1) if m else None)
        if extra_css:
            spec["theme"]["custom_css"] += "\n/* generated: explore hotspot positions */\n" + extra_css
            report["explore_hotspot_rules"] = extra_css.count("{") - 1
        report["theme_keys"] = sorted(spec["theme"].keys())
        report["module_colour"] = m.group(1) if m else None
    b = dump(await fn(server.build_from_spec)(spec))
    report["build"] = b
    pid = b.get("project_id")
    if not pid:
        return report
    report["lint_course"] = dump(await fn(server.lint_course)(pid))
    report["validate_package"] = dump(await fn(server.validate_package)(pid))
    pkgs = sorted((DATA / "packages").glob("*.zip"), key=lambda p: p.stat().st_mtime)
    if pkgs:
        num = module[:2]
        name = (f"MC_Sample_OracleLearning_{spec['scorm_version']}.zip" if num == "00"
                else f"MC_{num}_{SHORT[num]}_v0.1-draft_{spec['scorm_version']}.zip")
        shutil.copy(pkgs[-1], out / name)
        report["player_patches"] = patch_zip(out / name)
        report["package"] = {"file": name, "bytes": (out / name).stat().st_size}
    try:
        pv = dump(await fn(server.preview)(pid))
        if pv.get("inline_html"):
            (out / "preview.html").write_text(patch_player(pv["inline_html"])[0])
            report["preview"] = "preview.html"
    except Exception as e:  # preview is a convenience; never hide the build result
        report["preview_error"] = str(e)[:300]
    return report


def main() -> None:
    for module in sys.argv[1:]:
        try:
            rep = asyncio.run(run(module))
        except Exception as e:  # report the compiler's own refusal verbatim
            rep = {"module": module, "error": f"{type(e).__name__}: {e}"}
        (PLANS / module / "build" / "build-report.json").write_text(json.dumps(rep, ensure_ascii=False, indent=2, default=str))
        lint = rep.get("lint_course") or {}
        issues = lint.get("issues", lint if isinstance(lint, list) else [])
        errs = [i for i in issues if isinstance(i, dict) and i.get("severity") == "error"]
        print(json.dumps({"module": module, "status": rep.get("build", {}).get("status"),
                          "error": rep.get("error"), "lint_errors": len(errs), "lint_issues": len(issues),
                          "validate_ok": (rep.get("validate_package") or {}).get("ok"),
                          "package": rep.get("package")}, ensure_ascii=False))
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    main()
