#!/usr/bin/env python3
"""Draw training wireframes for the software simulations until the real captures exist.

The Oracle (03) and EHR (08) simulations need screenshots from an approved test environment
(gates B8, B2/D6). Until those exist, each step shows a clean, clearly labelled wireframe: the
element the learner must click sits exactly on the step's click region, so every simulation is
playable now. Wireframes are drawn from the simulation data — nothing about the real systems is
invented — and say "Training wireframe — not the live system" on every screen.

Output: ``<module>/storyboard/assets/wireframes/<asset-id>.svg``. ``build_course_spec.py`` uses a
wireframe only when no real capture exists, and the media job stays ``todo`` (the capture is
still owed).

    python3 elearning-course/scorm-plans/tools/build_wireframes.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
TARGETS = {"08_it-ehr-consultation": ("ehr-shot", 960, 540, "Clinic EHR"),
           "03_hr-employee-induction": ("hr-img-oracle", 1920, 1080, "HR self-service")}
NAVY, TEAL, MIST, BG, INK = "#003867", "#008C99", "#C0CED9", "#F4F7FA", "#1F2A37"
# Other things on the same page, so the learner has to find the right element (b = button,
# r = row/field, t = tile). Generic workflow words only; nothing copied from the live systems.
DECOYS = {
    "hr-img-oracle-1": [("User name", "r"), ("Password", "r"), ("Forgot password?", "b")],
    "hr-img-oracle-2": [("Pay", "t"), ("Personal Information", "t"), ("Learning", "t"), ("Benefits", "t"), ("Directory", "t")],
    "hr-img-oracle-3": [("Existing Absences", "t"), ("Absence Balance", "t"), ("Time Cards", "t")],
    "hr-img-oracle-4": [("Start date", "r"), ("End date", "r"), ("Comments", "r")],
    "hr-img-oracle-5": [("Save and Close", "b"), ("Cancel", "b"), ("Leave type: Annual", "r")],
    "ehr-shot-list": [("Patient row (fictional) — waiting", "r"), ("Patient row (fictional) — seen", "r"), ("Refresh", "b")],
    "ehr-shot-dx-1": [("Vitals", "b"), ("Add Allergy", "b"), ("Orders", "b"), ("Notes", "b")],
    "ehr-shot-dx-3": [("Type 1 diabetes mellitus", "r"), ("Gestational diabetes", "r"), ("Diabetes, unspecified", "r")],
    "ehr-shot-dx-4": [("Secondary", "b"), ("Onset date", "r"), ("Chronicity", "r")],
    "ehr-shot-dx-5": [("Edit", "b"), ("Remove", "b")],
    "ehr-shot-order-1": [("Lab orders", "b"), ("Radiology", "b"), ("Order history", "b")],
    "ehr-shot-order-3": [("Quantity", "r")],
    "ehr-shot-order-4": [("J03 Acute tonsillitis", "r"), ("No diagnosis", "r")],
    "ehr-shot-order-6": [("Save draft", "b"), ("Cancel", "b")],
    "ehr-shot-wizard-1": [("Lab package B", "r"), ("Lab package C", "r")],
    "ehr-shot-wizard-3": [("Package item 1", "r"), ("Package item 2", "r"), ("Package item 3", "r")],
    "ehr-shot-wizard-4": [("Back", "b"), ("Cancel", "b")],
    "ehr-shot-summary-1": [("Send SMS", "b"), ("Referral", "b"), ("Order history", "b")],
    "ehr-shot-summary-3": [("Close", "b"), ("Back", "b")],
    "ehr-shot-sms-1": [("Consultation Summary", "b"), ("Referral", "b")],
    "ehr-shot-sms-2": [("Language", "r")],
    "ehr-shot-sms-4": [("General healthy-living leaflet", "r"), ("Medication leaflet", "r")],
    "ehr-shot-sms-5": [("Cancel", "b"), ("Preview", "b")],
    "ehr-shot-ref-1": [("Send SMS", "b"), ("Orders", "b"), ("Consultation Summary", "b")],
    "ehr-shot-ref-2": [("Cardiology", "r"), ("Dermatology", "r"), ("Ophthalmology", "r")],
    "ehr-shot-ref-4": [("External · next available", "r")],
    "ehr-shot-ref-5": [("Notes to specialist", "r")],
    "ehr-shot-ref-6": [("Cancel", "b"), ("Save draft", "b")],
}


def clean(t: str) -> str:
    t = re.sub(r"<[^>]+>", "", t or "")
    return html.escape(re.sub(r"\s*⚠.*$", "", t).strip())


def overlaps(a, b, m=12):
    return not (a[0] + a[2] + m < b[0] or b[0] + b[2] + m < a[0] or a[1] + a[3] + m < b[1] or b[1] + b[3] + m < a[1])


def draw(aid: str, uses: list[dict], W: int, H: int, app: str) -> str:
    k = W / 960  # scale for type and chrome
    fs = lambda n: round(n * k)
    bar = fs(44)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="Training wireframe of {app}: {clean(uses[0].get("title", ""))}">',
           f'<rect width="{W}" height="{H}" fill="{BG}"/>',
           f'<rect width="{W}" height="{bar}" fill="{NAVY}"/>',
           f'<text x="{fs(16)}" y="{fs(28)}" font-family="Montserrat,Arial" font-size="{fs(15)}" font-weight="700" fill="#fff">{app}</text>',
           f'<text x="{W - fs(16)}" y="{fs(28)}" text-anchor="end" font-family="Montserrat,Arial" font-size="{fs(11)}" fill="{MIST}">'
           f'TEST PATIENT · fictional · training wireframe — not the live system</text>' if "ehr" in aid else
           f'<text x="{W - fs(16)}" y="{fs(28)}" text-anchor="end" font-family="Montserrat,Arial" font-size="{fs(11)}" fill="{MIST}">'
           f'Test account · training wireframe — not the live system</text>']
    boxes = []
    for u in uses:
        for r in u.get("regions", []):
            c = r["coords"]
            if len(c) == 3:
                cx, cy, rad = c
                boxes.append((cx - rad, cy - rad, 2 * rad, 2 * rad))
                pts = " ".join(f"{cx + rad * 0.9 * (1 if i % 2 == 0 else 0.45) * __import__('math').cos(__import__('math').pi / 2 + i * __import__('math').pi / 5):.0f},"
                               f"{cy - rad * 0.9 * (1 if i % 2 == 0 else 0.45) * __import__('math').sin(__import__('math').pi / 2 + i * __import__('math').pi / 5):.0f}" for i in range(10))
                out.append(f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="#fff" stroke="{MIST}" stroke-width="2"/>'
                           f'<polygon points="{pts}" fill="none" stroke="{NAVY}" stroke-width="{fs(2.5)}" stroke-linejoin="round"/>')
                continue
            x, y, w, h = c
            boxes.append((x, y, w, h))
            label = clean(r.get("label_html", r["id"]))
            if u["kind"] == "hotspot":  # form sections
                out.append(f'<rect x="{x + fs(6)}" y="{max(y, bar) + fs(6)}" width="{w - fs(12)}" height="{h - fs(12) - (bar if y < bar else 0)}" rx="{fs(10)}" fill="#fff" stroke="{MIST}" stroke-width="2"/>'
                           f'<text x="{x + fs(20)}" y="{max(y, bar) + fs(32)}" font-family="Montserrat,Arial" font-size="{fs(13)}" font-weight="700" fill="{NAVY}">{label}</text>')
                for i in range(3):
                    yy = max(y, bar) + fs(52) + i * fs(30)
                    if yy + fs(16) < y + h - fs(12):
                        out.append(f'<rect x="{x + fs(20)}" y="{yy}" width="{w - fs(40) - i * fs(30)}" height="{fs(14)}" rx="{fs(7)}" fill="{BG}"/>')
            elif h >= fs(100):  # panel / tile
                out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{fs(12)}" fill="#fff" stroke="{TEAL}" stroke-width="{fs(2)}"/>'
                           f'<text x="{x + fs(16)}" y="{y + fs(28)}" font-family="Montserrat,Arial" font-size="{fs(14)}" font-weight="700" fill="{NAVY}">{label}</text>')
                for i in range(max(0, min(5, int((h - fs(50)) / fs(28))))):
                    out.append(f'<rect x="{x + fs(16)}" y="{y + fs(44) + i * fs(28)}" width="{w - fs(32) - (i % 3) * fs(60)}" height="{fs(12)}" rx="{fs(6)}" fill="{BG}"/>')
            else:  # button or row
                primary = w <= fs(240) and any(t in label.lower() for t in ("order", "send", "save", "submit", "finalise", "sign in", "print", "add diagnosis"))
                fill, col = (TEAL, "#fff") if primary else ("#fff", NAVY)
                out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{fs(8)}" fill="{fill}" stroke="{TEAL if primary else MIST}" stroke-width="2"/>'
                           f'<text x="{x + (w / 2 if primary else fs(14))}" y="{y + h / 2 + fs(5)}" {"text-anchor=\"middle\"" if primary else ""} '
                           f'font-family="Montserrat,Arial" font-size="{fs(13)}" font-weight="600" fill="{col}">{label}</text>')
        if u.get("input_label"):
            x, y, w, h = fs(60), fs(150), fs(620), fs(52)
            boxes.append((x, y, w, h))
            out.append(f'<text x="{x}" y="{y - fs(10)}" font-family="Montserrat,Arial" font-size="{fs(12)}" font-weight="600" fill="{NAVY}">{clean(u["input_label"])}</text>'
                       f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{fs(8)}" fill="#fff" stroke="{TEAL}" stroke-width="{fs(2)}"/>'
                       f'<rect x="{x + fs(16)}" y="{y + fs(14)}" width="{fs(2)}" height="{fs(24)}" fill="{NAVY}"/>')
    # distractors in free space (same styles as the targets, never on a click region)
    size = {"b": (fs(180), fs(44)), "r": (fs(420), fs(44)), "t": (fs(320), fs(200))}
    for label, kind in DECOYS.get(aid, []):
        w, h = size[kind]
        spot = next(((x, y) for y in range(bar + fs(20), H - h - fs(10), fs(22)) for x in range(fs(60), W - w - fs(30), fs(40))
                     if not any(overlaps((x, y, w, h), b, fs(14)) for b in boxes)), None)
        if not spot:
            continue
        x, y = spot
        boxes.append((x, y, w, h))
        if kind == "t":
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{fs(12)}" fill="#fff" stroke="{MIST}" stroke-width="2"/>'
                       f'<text x="{x + fs(16)}" y="{y + fs(28)}" font-family="Montserrat,Arial" font-size="{fs(14)}" font-weight="700" fill="{NAVY}">{html.escape(label)}</text>')
        else:
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{fs(8)}" fill="#fff" stroke="{MIST}" stroke-width="2"/>'
                       f'<text x="{x + fs(14)}" y="{y + h / 2 + fs(5)}" font-family="Montserrat,Arial" font-size="{fs(13)}" font-weight="600" fill="{NAVY}">{html.escape(label)}</text>')
    # quiet filler rows where nothing is clickable, so the screen reads as a real page
    n = 0
    for yy in range(bar + fs(30), H - fs(40), fs(56)):
        for xx in (fs(60), fs(520)):
            cand = (xx, yy, fs(360), fs(14))
            if n < 6 and not any(overlaps(cand, b) for b in boxes):
                out.append(f'<rect x="{xx}" y="{yy}" width="{fs(360)}" height="{fs(14)}" rx="{fs(7)}" fill="#E3EAF0"/>')
                boxes.append(cand); n += 1
    out.append("</svg>")
    return "\n".join(out)


def main() -> None:
    for module, (prefix, W, H, app) in TARGETS.items():
        spec = json.loads((PLANS / module / "build" / "course-spec.json").read_text())
        uses: dict[str, list[dict]] = {}
        for s in spec["screens"]:
            for st in s.get("steps") or []:
                aid = st.get("image_asset_id") or ""
                if aid.startswith(prefix):
                    uses.setdefault(aid, []).append({"kind": "step", "title": s["title"], **st})
            if s["type"] == "hotspot" and (s.get("image_asset_id") or "").startswith(prefix):
                uses.setdefault(s["image_asset_id"], []).insert(0, {"kind": "hotspot", "title": s["title"], "regions": s["regions"]})
        out = PLANS / module / "storyboard" / "assets" / "wireframes"
        out.mkdir(parents=True, exist_ok=True)
        for aid, u in uses.items():
            (out / f"{aid}.svg").write_text(draw(aid, u, W, H, app))
        print(f"{module}: {len(uses)} wireframes")


if __name__ == "__main__":
    main()
