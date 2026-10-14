#!/usr/bin/env python3
"""Package a captured offline DRAFT review, never a SCORM/learner release. Stdlib only."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import zipfile

REPO = Path(__file__).resolve().parents[4]
CORE = ['index.html', 'player.js', 'scenario.js', 'style.css', 'layout-tokens.css',
        'layout-contract.json', 'generation-report.json', 'review.html']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pack(output):
    output = output.resolve()
    if not output.is_relative_to(REPO / '.generated'):
        raise ValueError('Review package output must be under .generated/')
    report = json.loads((output / 'generation-report.json').read_text())
    captures = json.loads((output / 'review/capture-report.json').read_text())
    if report['production_ready'] or captures['production_ready']:
        raise ValueError('This tool only packages draft review artefacts')
    if captures['generation_report_sha256'] != digest(output / 'generation-report.json'):
        raise ValueError('Screenshot revision is stale; regenerate and recapture first')
    files = {output / name for name in CORE}
    files.add(output / 'review/capture-report.json')
    files.add(output / 'review/phase-overview.png')
    for capture in captures['captures']:
        path = output / capture['image']
        if digest(path) != capture['sha256']:
            raise ValueError(f'Capture checksum mismatch: {capture["screen_id"]}')
        files.add(path)
    # Include this revision's declared files only, not stale media from an older asset map.
    html = (output / 'index.html').read_text()
    data = json.loads(html.split('<script id="course-data" type="application/json">')[1].split('</script>')[0])
    withheld = {item['asset_id'] for module in data['modules'] for screen in module['screens']
                for item in screen.get('_withheld', [])}
    for aid, filename in (data['preview_assets'] | data['assets']).items():
        if aid not in withheld and Path(filename).suffix.lower() != '.mp4':
            files.add(output / filename)
    files.update(output / 'fonts' / font['filename'] for font in report['font_provenance']['files'])
    files.add(output / 'fonts/provenance.json')
    files.add(output / 'reference/mockups/mockups.source.txt')
    files.update(output / ref['image'] for ref in report['layout_contract']['references'])
    files.update(output / 'reference/inputs' / record['path']
                 for module in report['modules'] for record in module['contract']['inputs'])
    for path in files:
        if not path.is_file() or not path.resolve().is_relative_to(output):
            raise ValueError(f'Missing/unsafe review file: {path}')
    phase = report['phase']['id'] if report.get('phase') else 'custom'
    filename = output / f'MyClinic_Phase{phase}_DRAFT_review_v0.1.zip'
    instructions = f'''MY CLINIC — INTERNAL DRAFT REVIEW v0.1

Phase/batch: {phase}
{report['screen_count']} current-content slides; {captures['capture_count']} real browser captures.

Unzip the entire folder, then open review.html for the screenshot gallery or
index.html for the interactive draft. Keep assets/fonts/reference/review next
to those files. No server, CDN or installed Montserrat font is required.

This is NOT a SCORM package, approved policy, final audio, pass/completion
record or learner delivery. Incomplete interactions, source-lock decisions,
full-size art (G6), voices (D10), Marketing (D11) and LMS (D9) remain pending.
Dense slides are full-height review captures; production 16:9 pagination
requires a later reviewed pass. Only selected states are in PNGs; use the
interactive draft to explore details and branches.

Planning copies are read-only traceability references, not a complete
repository export. Edit authoritative storyboards/plans/worksheets in the
repository after owner decisions; regenerate, recapture and repackage.
Some links inside source Markdown point to repository files outside this pack.
Do not share internal content/source specifications outside authorised channels.
'''
    with zipfile.ZipFile(filename, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        archive.writestr('READ-ME-FIRST.txt', instructions)
        for path in sorted(files):
            archive.write(path, str(path.relative_to(output)))
    with zipfile.ZipFile(filename) as archive:
        if archive.testzip() is not None:
            raise ValueError('Review archive verification failed')
        if any(name.endswith('.mp4') or name == 'imsmanifest.xml' for name in archive.namelist()):
            raise ValueError('Draft archive must not contain source videos or a SCORM manifest')
    return filename


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=REPO / '.generated/screens')
    args = parser.parse_args()
    try:
        filename = pack(args.out)
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f'Review packaging failed: {exc}\n')
    print(f'DRAFT review archive: {filename}\nBytes: {filename.stat().st_size}')


if __name__ == '__main__':
    main()
