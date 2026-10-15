#!/usr/bin/env python3
"""Generate offline branded review screens, not a SCORM package. Stdlib only."""
from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
import math
from pathlib import Path
import re
import shutil
import sys

from review_inputs import fingerprint, layout_for, mockup_contract, module_contract, phase_plan

PLANS = Path(__file__).resolve().parents[1]
TEMPLATES = Path(__file__).resolve().parent / 'screen_generator'
BRAND = PLANS / '00_program' / 'brand'
# These are deliberately not presented as production implementations.
REVIEW_ONLY = {'adaptive_practice', 'simulation', 'escape_room',
               'game', 'hotspot', 'labeled_diagram', 'image_compare', 'sorting'}
INTERACTIVE = {'mcq', 'true_false', 'poll', 'matching', 'drag_drop', 'fill_blank', 'decision_scenario'}
KNOWN = REVIEW_ONLY | INTERACTIVE | {'title_slide', 'content_slide', 'summary',
        'tabs', 'accordion', 'flashcards', 'timeline', 'worked_example', 'results_breakdown'}


class SafeHTML(HTMLParser):
    """Keep semantic course text; drop scripts, URLs and executable attributes."""
    allowed = {'p', 'strong', 'em', 'b', 'i', 'ul', 'ol', 'li', 'br', 'span', 'div',
               'h2', 'h3', 'h4', 'blockquote', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'sup', 'sub'}
    void = {'br'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.blocked = 0

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style', 'iframe', 'object'}:
            self.blocked += 1
        if not self.blocked and tag in self.allowed:
            self.out.append(f'<{tag}>')

    def handle_endtag(self, tag):
        if tag in {'script', 'style', 'iframe', 'object'}:
            self.blocked = max(0, self.blocked - 1)
        elif not self.blocked and tag in self.allowed and tag not in self.void:
            self.out.append(f'</{tag}>')

    def handle_data(self, data):
        if not self.blocked:
            self.out.append(html.escape(data))


def sanitize(value):
    if isinstance(value, dict):
        out = {}
        for key, v in value.items():
            if (key.endswith('_html') or key == 'html') and isinstance(v, str):
                parser = SafeHTML()
                parser.feed(v)
                parser.close()
                out[key] = ''.join(parser.out)
            else:
                out[key] = sanitize(v)
        return out
    if isinstance(value, list):
        return [sanitize(v) for v in value]
    return value


def load_cards(path):
    cards = []
    for index, match in enumerate(re.finditer(r'```json\s*\n(.*?)```', path.read_text(), re.S), 1):
        try:
            block = json.loads(match.group(1))
        except json.JSONDecodeError as exc:
            raise ValueError(f'{path}: invalid JSON block {index}: {exc}') from exc
        if isinstance(block, dict) and 'id' in block and 'type' in block:
            cards.append(block)
    if not cards:
        raise ValueError(f'{path}: no screen build blocks')
    seen = set()
    for card in cards:
        sid = card['id']
        if not isinstance(sid, str) or not re.fullmatch(r'[a-z0-9]+-[a-zA-Z0-9_-]+', sid):
            raise ValueError(f'{path}: invalid screen ID {sid!r}')
        if sid in seen:
            raise ValueError(f'{path}: duplicate screen ID {sid}')
        seen.add(sid)
        if not isinstance(card['type'], str) or card['type'] not in KNOWN:
            raise ValueError(f'{sid}: unsupported screen type {card["type"]!r}')
        for key in ['title', 'section', 'subtitle', 'notes', 'narration_text']:
            if key in card and not isinstance(card[key], str):
                raise ValueError(f'{sid}: {key} must be text')
        for key in ['options', 'tabs', 'items', 'cards', 'events', 'steps', 'pairs',
                    'targets', 'blanks', 'sections', 'nodes', 'regions', 'blocks']:
            if key in card and (not isinstance(card[key], list) or
                                any(not isinstance(item, dict) for item in card[key])):
                raise ValueError(f'{sid}: {key} must be an array of objects')
        for key in ['objective_ids', 'evidence_screen_ids']:
            if key in card and (not isinstance(card[key], list) or
                                any(not isinstance(item, str) for item in card[key])):
                raise ValueError(f'{sid}: {key} must be an array of strings')
    return cards


def scenario_issues(card):
    """Reject incomplete graphs instead of inventing targets or retry mechanics."""
    nodes = card.get('nodes', [])
    if not isinstance(nodes, list) or not nodes:
        return ['scenario nodes']
    by_id = {}
    for node in nodes:
        if not isinstance(node, dict) or not isinstance(node.get('id'), str) or not node['id'] or node['id'] in by_id:
            return ['unique scenario node IDs']
        by_id[node['id']] = node
    if not isinstance(card.get('start_node_id'), str) or card['start_node_id'] not in by_id:
        return ['valid scenario start node']
    for node in nodes:
        choices = node.get('choices')
        if not node.get('prompt_html') or not isinstance(choices, list) or not choices:
            return ['scenario prompts and choices']
        seen = set()
        for choice in choices:
            if not isinstance(choice, dict) or not isinstance(choice.get('id'), str) or not choice['id'] or choice['id'] in seen:
                return ['unique scenario choice IDs']
            seen.add(choice['id'])
            if not choice.get('text_html') or not choice.get('feedback_html'):
                return ['authored scenario choice text and feedback']
            delta = choice.get('score_delta')
            if isinstance(delta, bool) or not isinstance(delta, (int, float)) or not math.isfinite(delta):
                return ['authored finite scenario score deltas']
            if 'goto_node_id' not in choice or (choice['goto_node_id'] is not None and
                (not isinstance(choice['goto_node_id'], str) or choice['goto_node_id'] not in by_id)):
                return ['valid scenario branch targets']
    visiting, visited = set(), set()

    def visit(nid):
        if nid in visiting:
            return False
        if nid in visited:
            return True
        visiting.add(nid)
        for choice in by_id[nid]['choices']:
            target = choice['goto_node_id']
            if target is not None and not visit(target):
                return False
        visiting.remove(nid)
        visited.add(nid)
        return True

    if not visit(card['start_node_id']):
        return ['acyclic scenario (production retry logic required)']
    if len(visited) != len(by_id):
        return ['reachable scenario nodes']
    return []


def missing_fields(card):
    t = card['type']
    requirements = {
        'summary': ['body_html'],
        'mcq': ['prompt_html', 'options'], 'true_false': ['prompt_html', 'correct'],
        'poll': ['prompt_html'], 'tabs': ['tabs'], 'accordion': ['items'],
        'flashcards': ['cards'], 'timeline': ['events'], 'worked_example': ['steps'],
        'matching': ['pairs'], 'drag_drop': ['items', 'targets'],
        'fill_blank': ['prompt_html', 'blanks'], 'results_breakdown': ['sections'],
        'decision_scenario': ['nodes', 'start_node_id'], 'simulation': ['steps'],
        'adaptive_practice': ['items'], 'hotspot': ['regions'],
    }
    missing = [k for k in requirements.get(t, []) if k not in card or card[k] in (None, '', [])]
    if t == 'content_slide' and not card.get('body_html') and not (card.get('blocks') and
        all(isinstance(b, dict) and (b.get('html') or b.get('asset_id')) for b in card['blocks'])):
        missing.append('body_html or blocks')
    if t == 'poll' and not card.get('options') and not card.get('allow_text'):
        missing.append('options or optional text reflection')
    if t == 'mcq' and not any(o.get('correct') for o in card.get('options', [])):
        missing.append('correct option')
    if t == 'fill_blank' and any(not b.get('accepted') for b in card.get('blanks', [])):
        missing.append('accepted answers')
    if t == 'decision_scenario':
        missing.extend(scenario_issues(card))
    return missing


def asset_ids(value):
    found = set()
    if isinstance(value, dict):
        for key, v in value.items():
            if (key.endswith('_asset_id') or key == 'asset_id') and isinstance(v, str):
                found.add(v.strip('<>'))
            else:
                found |= asset_ids(v)
    elif isinstance(value, list):
        for v in value:
            found |= asset_ids(v)
    return found


def module_data(module):
    source = module / 'storyboard' / 'storyboard.md'
    cards = load_cards(source)
    visual_path = module / 'storyboard' / 'visual-plan.json'
    visuals = json.loads(visual_path.read_text())
    visual_by_id = {v['screen_id']: v for v in visuals.get('screens', [])}
    narration_path = module / 'storyboard' / 'narration-script.json'
    narration = json.loads(narration_path.read_text())
    contract = module_contract(module, cards, visuals, narration)
    source_text = source.read_text()
    lines = {}
    for segment in narration.get('segments', []):
        text = re.sub(r'\[\[.*?\]\]', '', segment.get('narration', ''))
        lines.setdefault(segment['screen_id'], []).append(text.strip())
    for card in cards:
        visual = visual_by_id.get(card['id'], {})
        card['_brief'] = visual.get('on_screen_text') or ''
        companion = dict(contract['companions'].get(card['id'], {}))
        if 'char-duo-welcome' in companion.get('assets', []):
            companion['assets'] = ['char-omar-welcome', 'char-noor-welcome']
        card['_companion'] = companion
        card['_layout'] = layout_for(visual, companion)
        annotation = re.search(r'^### `'+re.escape(card['id'])+r'`.*?(?=^### `|\Z)', source_text, re.M | re.S)
        pending_groups = re.findall(
            r'PENDING\s+(?:CONSENT\s+)?((?:[BDGP]\d+|NEW-\d+)(?:\s*/\s*(?:[BDGP]\d+|NEW-\d+))*)',
            (annotation.group() if annotation else '') + json.dumps(card), re.I)
        card['_pending'] = sorted({value.upper() for group in pending_groups
                                   for value in re.findall(r'[BDGP]\d+|NEW-\d+', group, re.I)})
        card['_withheld'] = [{'asset_id': block['asset_id'].strip('<>'),
                              'reason': 'Consent-dependent portrait/identifying caption in the source remains pending'}
                             for block in card.get('blocks', []) if block.get('asset_id') and
                             re.search(r'pending consent', block.get('caption', ''), re.I)]
        card['_visual'] = visual.get('visual_concept', '')
        # Structured motion spec written by tools/build_motion_spec.py (vocabulary in
        # tools/motion_spec.py). The review player applies it; it is not a production build.
        card['_motion'] = visual.get('motion')
        card['_planned_visuals'] = []
        for image in visual.get('imagery', []):
            match = re.match(r'([a-z0-9-]+):\s*(.*)', image.get('description', ''), re.S)
            if match:
                card['_planned_visuals'].append({'asset_id': match[1], 'brief': match[2],
                                                'alt': image.get('alt_text', '')})
        card['_missing'] = missing_fields(card)
        card['_mode'] = ('brief' if card['_missing'] or card.get('asset_status') else
                         'review' if card['type'] in REVIEW_ONLY else 'rendered')
        if not card.get('narration_text'):
            card['narration_text'] = ' '.join(lines.get(card['id'], []))
    return {'id': module.name, 'title': visuals.get('module_title', module.name),
            'source': str(source.relative_to(PLANS)),
            'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'contract': {k: v for k, v in contract.items() if k != 'companions'}, 'screens': cards}


def generate(modules, output, asset_map=None, phase_id=None):
    output = output.resolve()
    # Never overwrite authoring sources, the tool, or a parent of the checkout.
    repo = PLANS.parents[1]
    if output == repo or output in repo.parents or output == PLANS or output in PLANS.parents:
        raise ValueError('Output must be a dedicated generated-preview directory')
    if output.is_relative_to(repo) and not output.is_relative_to(repo / '.generated'):
        raise ValueError('In-repository output must live under .generated/')
    if not modules:
        raise ValueError('At least one module is required')
    phases = phase_plan()
    selected_phase = next((p for p in phases['phases'] if p['id'] == phase_id), None)
    if phase_id and (not selected_phase or selected_phase['modules'] != [m.name for m in modules]):
        raise ValueError('Phase selection must match the configured package order')
    layouts = mockup_contract()
    data = [module_data(module) for module in modules]
    brand = json.loads((BRAND / 'brand-kit.json').read_text())
    output.mkdir(parents=True, exist_ok=True)
    (output / 'assets').mkdir(exist_ok=True)
    assets = {}
    preview_assets = {}
    asset_provenance = {}
    # Preview-resolution companion art is separate from resolved production assets.
    character_root = PLANS / '00_program/characters'
    for path in sorted((character_root / 'previews').glob('char-*.jpg')):
        dest = 'assets/review-' + path.name
        shutil.copyfile(path, output / dest)
        preview_assets[path.stem] = dest
        asset_provenance[path.stem] = {'status': 'preview-resolution review art; full-size PNG in characters/assets/',
                                     'production_approved': False, **fingerprint(path)}
    for path in sorted((character_root / 'assets').glob('char-*-avatar-*.png')):
        dest = 'assets/review-' + path.name
        shutil.copyfile(path, output / dest)
        preview_assets[path.stem] = dest
        asset_provenance[path.stem] = {'status': 'full-size avatar PNG from characters/assets/; pending visual approval',
                                     'production_approved': False, **fingerprint(path)}
    # Fonts are licensed, local and checksum-verified. English only; no Arabic translation is inferred.
    font_root = BRAND / 'fonts'
    font_provenance = json.loads((font_root / 'provenance.json').read_text())
    (output / 'fonts').mkdir(exist_ok=True)
    for font in font_provenance['files']:
        path = font_root / font['filename']
        if path.name != font['filename'] or fingerprint(path)['sha256'] != font['sha256']:
            raise ValueError('Bundled font filename/checksum mismatch')
        shutil.copyfile(path, output / 'fonts' / path.name)
    shutil.copyfile(font_root / 'provenance.json', output / 'fonts/provenance.json')
    # The eight reference PNGs and their HTML source are real generation inputs.
    reference_root = output / 'reference/mockups'
    reference_root.mkdir(parents=True, exist_ok=True)
    for ref in layouts['references']:
        shutil.copyfile(BRAND / 'screen-mockups' / Path(ref['image']).name, output / ref['image'])
    shutil.copyfile(BRAND / 'screen-mockups/mockups.html', reference_root / 'mockups.source.txt')
    (output / 'layout-tokens.css').write_text(':root {\n' + ''.join(
        f'  --{key}: {value};\n' for key, value in layouts['metrics'].items()) + '}\n')
    (output / 'layout-contract.json').write_text(json.dumps(layouts, indent=2) + '\n')
    for path in sorted((BRAND / 'assets').glob('*.png')):
        name = 'brand-' + path.stem
        dest = 'assets/' + name + path.suffix
        shutil.copyfile(path, output / dest)
        assets[name] = dest
        asset_provenance[name] = {'status': 'supplied brand asset; D11 pending',
                                  'production_approved': False, **fingerprint(path)}
    # Own authored diagrams only; no automatic use of video frames or patient captures.
    for module in modules:
        for path in sorted((module / 'storyboard' / 'assets').glob('*.svg')):
            dest = f'assets/{module.name}-{path.name}'
            shutil.copyfile(path, output / dest)
            assets[path.stem] = dest
            asset_provenance[path.stem] = {'status': 'authored draft SVG; SME approval pending',
                                          'production_approved': False, **fingerprint(path)}
    # Explicit maps are review-local inputs, not an approval/provenance record.
    if asset_map:
        mapping = json.loads(asset_map.read_text())
        if not isinstance(mapping, dict):
            raise ValueError('Asset map must be an object: asset ID -> local filename')
        for aid, filename in mapping.items():
            if not re.fullmatch(r'[a-zA-Z0-9_-]+', aid) or not isinstance(filename, str):
                raise ValueError(f'Invalid asset mapping: {aid}')
            path = (asset_map.parent / filename).resolve()
            if not path.is_file() or path.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.mp3', '.wav', '.ogg', '.mp4', '.pdf'}:
                raise ValueError(f'{aid}: missing or unsupported local asset {filename}')
            dest = f'assets/{aid}{path.suffix.lower()}'
            shutil.copyfile(path, output / dest)
            assets[aid] = dest
            asset_provenance[aid] = {'status': 'explicit local review map; not an approval',
                                     'production_approved': False}
    issues = []
    for module in data:
        module['color'] = brand['module_colors'][module['id']]
        if module['contract']['color'] != module['color'].upper():
            raise ValueError(f'{module["id"]}: worksheet colour differs from brand kit')
        for card in module['screens']:
            planned_ids = {image['asset_id'] for image in card.get('_planned_visuals', [])}
            planned_ids.update(card['_companion'].get('assets', []))
            unresolved = sorted((asset_ids(card) | planned_ids) - assets.keys())
            card['_unresolved'] = unresolved
            if card['_mode'] != 'rendered' or unresolved:
                issues.append({'module': module['id'], 'screen_id': card['id'],
                               'mode': card['_mode'], 'missing_fields': card['_missing'],
                               'unresolved_assets': unresolved, 'withheld_review_items': card['_withheld']})
    report = {'kind': 'local-draft-review', 'production_ready': False,
              'phase': selected_phase, 'phase_plan': phases,
              'layout_contract': layouts, 'font_provenance': font_provenance,
              'asset_provenance': asset_provenance,
              'shared_inputs': [fingerprint(PLANS / '00_program/draft-slide-phases.json'),
                                fingerprint(BRAND / 'brand-kit.json'),
                                fingerprint(BRAND / 'brand-identity.md'),
                                fingerprint(PLANS / '00_program/visual-production-plan.md'),
                                fingerprint(BRAND / 'fonts/provenance.json'),
                                fingerprint(Path(__file__)),
                                fingerprint(Path(__file__).with_name('review_inputs.py')),
                                *[fingerprint(TEMPLATES / name) for name in ['index.html','player.js','scenario.js','style.css']]],
              'screen_count': sum(len(m['screens']) for m in data),
              'render_modes': {mode: sum(s['_mode'] == mode for m in data for s in m['screens'])
                               for mode in ['rendered', 'review', 'brief']},
              'scored_screen_count': sum(bool(s.get('points')) for m in data for s in m['screens']),
              'modules': [{'id': m['id'], 'screen_count': len(m['screens']),
                           'source': m['source'], 'source_sha256': m['source_sha256'],
                           'contract': m['contract'],
                           'layouts': {lid: sum(s['_layout']['id'] == lid for s in m['screens']) for lid in ['L1','L2','L3','L4','L5','L6']}} for m in data],
              'issues': issues}
    payload = sanitize({'brand': brand, 'modules': data, 'assets': assets, 'preview_assets': preview_assets,
                        'asset_provenance': asset_provenance, 'report': report})
    # Escaping < makes even a literal </script> in source safe inside the JSON element.
    serialized = json.dumps(payload, ensure_ascii=False).replace('<', '\\u003c').replace('&', '\\u0026')
    template = (TEMPLATES / 'index.html').read_text()
    (output / 'index.html').write_text(template.replace('__COURSE_DATA__', serialized))
    for filename in ['player.js', 'scenario.js', 'style.css']:
        shutil.copyfile(TEMPLATES / filename, output / filename)
    for module in data:
        for record in module['contract']['inputs']:
            dest = output / 'reference/inputs' / record['path']
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(repo / record['path'], dest)
    (output / 'generation-report.json').write_text(json.dumps(report, indent=2) + '\n')
    # Never leave an apparently current screenshot gallery after inputs/style change.
    capture_report = output / 'review/capture-report.json'
    try:
        capture_hash = json.loads(capture_report.read_text()).get('generation_report_sha256')
    except (OSError, ValueError):
        capture_hash = None
    current_hash = hashlib.sha256((output / 'generation-report.json').read_bytes()).hexdigest()
    if capture_hash != current_hash:
        (output / 'review.html').write_text(
            '<!doctype html><html lang="en"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>My Clinic — captures pending</title><link rel="stylesheet" href="style.css">'
            '<main><h1>Screenshots need to be refreshed</h1>'
            '<p>The current slide inputs or styling have changed, or no captures exist yet. '
            'Previous images are not proof of this revision.</p>'
            '<p>Rerun tools/browser/capture_slides.cjs against this generated preview.</p>'
            '<a href="index.html">Open current draft slides →</a></main></html>')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('modules', nargs='*', help='Module folder names; default: all eight')
    parser.add_argument('--out', type=Path, default=PLANS.parents[1] / '.generated' / 'screens')
    parser.add_argument('--phase', choices=[p['id'] for p in phase_plan()['phases']],
                        help='Generate one pre-kickoff draft batch, in the programme build order')
    parser.add_argument('--asset-map', type=Path, help='JSON asset ID -> filename relative to map')
    args = parser.parse_args()
    available = {p.name: p for p in sorted(PLANS.glob('0[1-8]_*')) if p.is_dir()}
    try:
        if len(set(args.modules)) != len(args.modules):
            raise ValueError('Duplicate module selection')
        unknown = set(args.modules) - available.keys()
        if unknown:
            raise ValueError(f'Unknown modules: {", ".join(sorted(unknown))}')
        if args.phase and args.modules:
            raise ValueError('Use --phase or explicit module names, not both')
        selected = next((p['modules'] for p in phase_plan()['phases'] if p['id'] == args.phase), None)
        report = generate([available[n] for n in (selected or args.modules or available)], args.out, args.asset_map, args.phase)
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f'Generation failed: {exc}\n')
    print(f'{report["screen_count"]} draft screens; {len(report["issues"])} screens have review/build issues.')
    print(f'Preview: {args.out / "index.html"}\nReport: {args.out / "generation-report.json"}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
