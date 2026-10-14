#!/usr/bin/env python3
"""Prepare the next G10 approval request; never produce assets or approve policy."""
from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path

from assemble_storyboard_docs import PLANS, parse_assets
from planned_visual_assets import screen_ids

OUTPUT = PLANS / '00_program' / 'asset-approval-handoff'
FIELDS = ['asset_id', 'module', 'screens', 'placement', 'brief', 'draft_alt', 'production_gate',
          'review_owner_role', 'status', 'reviewer_name', 'review_date', 'signed_decision',
          'approved_file_or_record', 'comments']


def request_rows():
    rows = []
    for folder in ['01_health-and-safety-1', '02_health-and-safety-2', '08_it-ehr-consultation']:
        for asset in parse_assets(PLANS / folder):
            aid = asset['id']
            included = (aid in {'hs1-img-eyewash', 'hs1-img-treatment-room', 'hs1-img-pump-label',
                                'hs2-img-extinguisher', 'hs2-img-kit-chem', 'hs2-img-kit-bio',
                                'hs2-img-spill-photo'} or aid.startswith(('hs2-img-drill-', 'ehr-shot-')))
            if not included:
                continue
            owner = ('EHR lead + DPO; Pharmacy/Medical Director for examples as applicable'
                     if aid.startswith('ehr-shot-') else
                     'Biomedical Engineering + Facilities' if aid == 'hs1-img-pump-label' else
                     'Facilities + Safety/EHS' if aid.startswith('hs1-') else 'Safety Manager + EHS')
            rows.append(dict(zip(FIELDS, [aid, folder, ', '.join(screen_ids(asset['screens'])),
                asset['placement'], asset['brief'], asset['alt'], asset['gate'], owner,
                'Pending — not submitted', '', '', '', '', ''])))
    ids = [r['asset_id'] for r in rows]
    if len(ids) != 44 or len(set(ids)) != 44:
        raise ValueError('Expected 44 unique G10 approval rows (13 safety visuals + 31 EHR shots). Reconcile manifests before changing scope.')
    return rows


def write_handoff(out):
    rows = request_rows()
    out.mkdir(parents=True, exist_ok=True)
    tracker = out / 'response-template.csv'
    if tracker.exists():
        with tracker.open(newline='') as handle:
            for row in csv.DictReader(handle):
                if (row.get('status') != 'Pending — not submitted' or
                    any(row.get(key) for key in ['reviewer_name', 'review_date', 'signed_decision',
                                                'approved_file_or_record', 'comments'])):
                    raise ValueError('Response template contains human updates. Archive them in a signed approval record before regeneration; no responses were overwritten.')
    buf = io.StringIO(newline='')
    writer = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)
    tracker.write_text(buf.getvalue())
    request = {'kind': 'approval-request-template', 'status': 'Prepared locally — not submitted or approved',
               'production_authorised': False, 'asset_count': 44, 'safety_visual_count': 13,
               'drill_scene_count': 6, 'ehr_screenshot_count': 31, 'required_video_count': 0,
               'rows': rows}
    (out / 'request.json').write_text(json.dumps(request, ensure_ascii=False, indent=2) + '\n')
    table = '\n'.join(f"| `{r['asset_id']}` | {r['screens']} | {r['placement']} | {r['review_owner_role']} |" for r in rows)
    text = '''# G10 asset approval handoff — full six-scene drill

**Prepared for review, not sent. Nothing here grants production approval.**

This packet is the next step after [G10 reference restoration](../g10-visual-restoration.md).
It covers **44 asset records: 13 safety visuals (including all six Code Red scenes) and 31
unique EHR screenshots**. It is not a new 44-image commission: the safety set includes four
client photos; EHR files are test-environment captures. The overall brief still calls for
21/22 new still illustrations across the programme, five Oracle captures and zero required videos.

## Send / review sequence

1. Course owner names the accountable Safety Manager, Facilities/Biomedical reviewer, EHR
   lead and DPO using the [decision sheet](../decision-sheet.md). Do not infer names or email
   addresses. Use the [kick-off pack](../kickoff-pack.md) to close the facts below.
2. Send Safety the six scene briefs in
   [drill-scene-manifest.json](../../02_health-and-safety-2/storyboard/drill-scene-manifest.json),
   the [module 02 cards](../../02_health-and-safety-2/storyboard/storyboard.md) and its Word
   review document. Ask for a written decision per node before scene production.
3. Send Facilities/Biomedical the [module 01 cards](../../01_health-and-safety-1/storyboard/storyboard.md)
   for treatment-room targets and the editable pump-label example. Request permissioned
   client photos of the eyewash, extinguisher and both spill kits.
4. Send IT/DPO the [31-shot capture manifest](../../08_it-ehr-consultation/storyboard/capture-manifest.json)
   and [module 08 cards](../../08_it-ehr-consultation/storyboard/storyboard.md). Request the
   approved test environment and a completely fictional patient; do not request credentials
   in this CSV, in chat or in Git. IT supplies access through its normal secure process.
5. Reviewers return a copy of `response-template.csv`, with name, date, a signed decision or
   a link to its signed record, and corrections. Store actual responses separately from
   generated templates, and write approved facts back to Phase 0 before building assets.

## Approval questions that must close

### Safety / Facilities / Biomedical

- D1 / module 02 B1: confirm the spill threshold. The spill-volume cue must match the approved
  rule; a draft bottle illustration must not decide the threshold.
- D2 / module 02 B2: confirm code wording and branch extensions. Call scripts stay editable
  HTML; image generation must not bake in text, phone numbers or code labels.
- Sign all six authored drill nodes (rescue, alarm, contain, extinguish/evacuate, stairs/chair,
  assembly/all-clear), including safe actions, scene targets and the trained-only distinction.
- Module 02 B8: confirm generic versus branch-specific assembly-point treatment.
- Module 01 B6: confirm emergency sockets, utilities and target items in the treatment room.
- Biomedical: confirm the overdue-label example and escalation rule. Use fictional label dates
  in an editable overlay; never let an image model invent an inspection date or label.
- For client photos, record ownership/permission and verify equipment against the current site.
  Kit procedure remains blocked by module 02 B4; photography does not approve the procedure.

### IT / EHR / DPO

- B2 / D6: approve the test environment and fictional demographics before capture. Source
  `IT.mp4` and patient-bearing frames are never substitutes.
- B3/B5: record EHR version and confirm labels. Capture at 1920×1080 and 125% browser zoom.
- B4/B6/B8/B9: confirm mandatory fields, approved examples, SMS feature/leaflets, and referral
  wording/timing. Medication or lab examples show system use, not prescribing guidance.
- Use a test-only SMS destination; do not send to a real patient. Confirm safe test execution
  for Order, Send and Save actions with IT before running them.
- DPO reviews **every captured file**, including crops, for names, IDs, record numbers, phones,
  notifications and browser chrome. Review current pixels, not just the fictional patient setup.
- Reuse the consultation-form shot on ehr-011. Up to four legibility crops may be needed, but
  they are not extra workflow steps and still require per-file review.

## Evidence and release rules

`status`, names, dates and signed decisions are intentionally blank/unapproved in the prepared
packet. There are no captured images, generated scenes or signed client approvals attached.
Do not use a row's existence, a tool result or a merge as approval.

Before any asset ships: close its decisions in Phase 0; obtain reviewer sign-off; record source,
license/permission, author, date and approved file reference in provenance; then upload through
Phase 4. Coordinates, hit regions, simulation input aliases and game logic need separate review
against the final visual. Asset approval does not complete the SCORM/LMS/pilot gate.

**Cast:** Noor and Dr. Omar only as named guides; any scene extras are unnamed and non-speaking.
No new character design, voice or video generation is authorised by this packet.

## Response tracker index

Briefs, alt text and gates are in `response-template.csv` and `request.json`. All rows begin
`Pending — not submitted`. This generator refuses to overwrite human responses in the template.

| Asset | Core screens | Planned placement | Reviewer role |
|---|---|---|---|
''' + table + '''

## Regenerate

```bash
python3 elearning-course/scorm-plans/tools/prepare_asset_approval_handoff.py
```

The packet is deterministic from Phase 3 manifests. If returned responses were entered in the
template, archive them separately before regeneration. Never erase reviewer evidence to make
the tool pass. No email is sent by the tool.
'''
    (out / 'README.md').write_text(text)
    return request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=OUTPUT, help='Dedicated handoff output directory')
    args = parser.parse_args()
    try:
        request = write_handoff(args.out)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Handoff failed: {exc}\n')
    print(f'Prepared {request["asset_count"]} pending approval rows; no approvals or submissions recorded.')
    print(args.out / 'README.md')


if __name__ == '__main__':
    main()
