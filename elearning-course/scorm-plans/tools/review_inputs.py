"""Required planning/template inputs and geometry compiled from the supplied mockups.

Only presentation metadata is derived here. Never derive assessments, policy values,
branch logic, completion, approval or narration from a worksheet or visual brief.
"""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct

PLANS = Path(__file__).resolve().parents[1]
PROGRAM = PLANS / '00_program'
REPO = PLANS.parents[1]
MOCKUP_FILES = {
    's1': '01-title.png', 's2': '02-section-opener.png',
    's3': '03-content.png', 's4': '04-question.png',
    's5': '05-scenario.png', 's6': '06-results.png',
    's7': '07-meet-your-guides.png', 's8': '08-companion-tip.png',
}


def fingerprint(path):
    data = path.read_bytes()  # Missing essential input is a generation failure.
    return {'path': str(path.relative_to(REPO)), 'sha256': hashlib.sha256(data).hexdigest(),
            'bytes': len(data)}


def plain(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    return text.replace('`', '').replace('**', '').strip()


def table_rows(text):
    """Yield dicts from Markdown tables, keeping the header of each individual table."""
    header = None
    for line in text.splitlines():
        if not line.startswith('|'):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if all(re.fullmatch(r'[- :]+', c) for c in cells):
            continue
        if header is None:
            header = [plain(c) for c in cells]
        elif len(cells) == len(header):
            yield dict(zip(header, cells))


def phase_files(module):
    files = {}
    for phase in range(6):
        matches = sorted(module.glob(f'phase-{phase}-*.md'))
        if len(matches) != 1:
            raise ValueError(f'{module.name}: exactly one Phase {phase} plan is required')
        files[str(phase)] = matches[0]
    return files


def module_contract(module, cards, visuals, narration):
    """Read the actual production worksheet and all six phase plans; reconcile baselines."""
    worksheet = PROGRAM / 'course-templates' / (module.name.replace('_', '-') + '-production-worksheet.md')
    base_template = PROGRAM / 'course-templates' / 'course-production-template.md'
    worksheet_text, base_text = worksheet.read_text(), base_template.read_text()
    required_sections = [s for s in re.findall(r'^## (.+)$', base_text, re.M)]
    absent = [s for s in required_sections if f'## {s}' not in worksheet_text]
    if absent:
        raise ValueError(f'{worksheet.name}: missing template sections: {", ".join(absent)}')
    fields = {key.strip(): value.strip() for key, value in
              re.findall(r'^- ([^:\n]+): (.+)$', worksheet_text, re.M)}
    for key in ['Package id / prefix', 'Screen list and counts', 'Package colour/layout',
                'Storyboard', 'Visual plan', 'Script', 'Learning outcomes and on-the-job actions']:
        if key not in fields:
            raise ValueError(f'{worksheet.name}: required worksheet field missing: {key}')
    if module.name not in fields['Package id / prefix']:
        raise ValueError(f'{worksheet.name}: worksheet belongs to a different package')
    for key, path in [('Storyboard', module / 'storyboard/storyboard.md'),
                      ('Visual plan', module / 'storyboard/visual-plan.json'),
                      ('Script', module / 'storyboard/narration-script.json')]:
        links = re.findall(r'\]\(([^)]+)\)', fields[key])
        if not links or (worksheet.parent / links[0]).resolve() != path.resolve():
            raise ValueError(f'{worksheet.name}: {key} must link to this module\'s canonical input')
    counts = re.search(r'(\d+) planned screens, (\d+) scored screens, (\d+) points', fields['Screen list and counts'])
    if not counts:
        raise ValueError(f'{worksheet.name}: missing numeric screen/score/point baseline')
    expected = dict(zip(['screens', 'scored', 'points'], map(int, counts.groups())))
    actual = {'screens': len(cards), 'scored': sum(bool(s.get('points')) for s in cards),
              'points': sum(s.get('points', 0) for s in cards)}
    plans = phase_files(module)
    screen_rows = []
    layout_variants = {}
    deferred = []
    for row in table_rows(plans['2'].read_text()):
        if 'Id' not in row or 'Type' not in row:
            continue
        sid = plain(row['Id']).replace('★', '').strip()
        if not re.fullmatch(r'[a-z0-9]+-\d+', sid):
            continue
        item = {'id': sid, 'type': re.search(r'[a-z_]+', plain(row['Type'])).group(),
                'points': int(row.get('Pts', '').strip() or '0')}
        variant = re.search(r'\((text_media|full_media|text)\)', plain(row['Type']))
        if variant:
            layout_variants[sid] = variant.group(1)
        if 'optional' in ' '.join(row.values()).lower():
            deferred.append(item)
        else:
            screen_rows.append(item)
    issues = []
    if expected != actual:
        issues.append(f'Worksheet baseline {expected} differs from storyboard {actual}')
    build_rows = [{'id': s['id'], 'type': s['type'], 'points': s.get('points', 0)} for s in cards]
    if build_rows != screen_rows:
        issues.append('Phase 2 IDs/order/types/points differ from storyboard; retain cards and review the mismatch')
    visual_ids = [s['screen_id'] for s in visuals['screens']]
    objectives = {}
    for row in table_rows(plans['1'].read_text()):
        oid = plain(row.get('Id', ''))
        if not re.fullmatch(r'[a-z0-9]+-o\d+', oid):
            continue
        objectives[oid] = {'text': plain(next((value for key, value in row.items() if key.startswith('Objective')), '')),
                           'assessed_by': re.findall(r'[a-z0-9]+-\d+', next((value for key, value in row.items() if key.startswith('Assessed by')), ''))}
    if not objectives:
        raise ValueError(f'{module.name}: Phase 1 objective map is required')
    for card in cards:
        variant = layout_variants.get(card['id'])
        if variant and card.get('layout') and variant != card['layout']:
            issues.append(f'{card["id"]}: Phase 2 layout {variant} differs from storyboard {card["layout"]}; retain current card/Phase 3 layout for draft, reconcile before production')
        unknown = set(card.get('objective_ids', [])) - objectives.keys()
        if unknown:
            issues.append(f'{card["id"]}: objective IDs not in Phase 1: {sorted(unknown)}')
        if card.get('points') and not card.get('objective_ids'):
            issues.append(f'{card["id"]}: scored screen needs a Phase 1 objective')
        if card.get('points') and any(card['id'] not in objectives[oid]['assessed_by'] for oid in card.get('objective_ids', []) if oid in objectives):
            issues.append(f'{card["id"]}: objective evidence differs from Phase 1')
    if visual_ids != [s['id'] for s in cards]:
        issues.append('Visual plan IDs/order differ from storyboard')
    narration_ids = {s['screen_id'] for s in narration['segments']}
    if narration_ids != {s['id'] for s in cards}:
        issues.append('Narration coverage differs from storyboard')
    gates = [{'checked': state.lower() == 'x', 'text': text}
             for state, text in re.findall(r'^- \[([ xX])\] (.+)$', worksheet_text, re.M)]
    inputs = [worksheet, base_template, *plans.values(),
              module / 'storyboard/storyboard.md', module / 'storyboard/visual-plan.json',
              module / 'storyboard/narration-script.json']
    companions = {}
    for row in table_rows(plans['3'].read_text()):
        if 'Screen' not in row or 'Pose / asset' not in row:
            continue
        sid = plain(row['Screen'])
        companions[sid] = {'visible': plain(row['Visible']),
                           'assets': re.findall(r'char-(?:noor|omar|duo)-[a-z0-9-]+', row['Pose / asset']),
                           'placement': plain(row.get('Placement (brand layout)', row.get('Placement', ''))),
                           'brief': plain(row.get('What they do', ''))}
    color = re.search(r'#[a-fA-F0-9]{6}', fields['Package colour/layout'])
    if not color:
        raise ValueError(f'{worksheet.name}: package colour is required')
    return {'worksheet': str(worksheet.relative_to(PLANS)),
            'identity': {key: plain(fields.get(key, '')) for key in
                         ['Commercial course group', 'Audience', 'Seat-time estimate',
                          'Proposal revision', 'SCORM/completion/pass mark', 'Lead character / co-host']},
            'color': color.group().upper(), 'expected': expected, 'actual': actual,
            'alignment': 'matched' if not issues else 'review-required', 'issues': issues,
            'deferred': deferred, 'objectives': objectives, 'gates': gates, 'inputs': [fingerprint(p) for p in inputs],
            'companions': companions}


class MockupTree(HTMLParser):
    """Minimal tree to extract the supplied mockup styles, not a remote HTML renderer."""
    void = {'img', 'meta', 'link', 'br', 'hr', 'input'}

    def __init__(self):
        super().__init__()
        self.root = {'tag': 'root', 'attrs': {}, 'children': []}
        self.stack = [self.root]
        self.ids = {}

    def handle_starttag(self, tag, attrs):
        node = {'tag': tag, 'attrs': dict(attrs), 'children': []}
        self.stack[-1]['children'].append(node)
        if node['attrs'].get('id'):
            self.ids[node['attrs']['id']] = node
        if tag not in self.void:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i]['tag'] == tag:
                del self.stack[i:]
                break


def declarations(text):
    return dict((key.strip(), value.strip()) for key, value in
                re.findall(r'([a-zA-Z0-9_-]+)\s*:\s*([^;]+)', text))


def mockup_contract(folder=None):
    folder = folder or PROGRAM / 'brand/screen-mockups'
    source = folder / 'mockups.html'
    text = source.read_text()
    tree = MockupTree()
    tree.feed(text)
    css = re.search(r'<style>(.*?)</style>', text, re.S).group(1)

    def rule(selector):
        match = re.search(r'(?:^|\})\s*' + re.escape(selector) + r'\s*\{([^}]+)\}', css)
        if not match:
            raise ValueError(f'Mockup CSS rule missing: {selector}')
        return declarations(match.group(1))

    def inline(sid, predicate):
        for child in tree.ids[sid]['children']:
            if predicate(child):
                return declarations(child['attrs'].get('style', ''))
        raise ValueError(f'Mockup geometry missing: {sid}')

    def px(value):
        if not re.fullmatch(r'\d+(?:\.\d+)?px', value):
            raise ValueError(f'Expected mockup pixel geometry, got {value!r}')
        return float(value[:-2])

    stage, header, line, footer = rule('.stage'), rule('.hdr'), rule('.rule'), rule('.ftr')
    title_logo = inline('s1', lambda n: n['tag'] == 'img')
    title_text = inline('s1', lambda n: n['tag'] == 'div' and any(c['attrs'].get('class') == 'chip' for c in n['children']))
    content_text = inline('s3', lambda n: any(c['tag'] == 'h1' for c in n['children']))
    scene = inline('s5', lambda n: n['attrs'].get('class') == 'ph')
    scenario_text = inline('s5', lambda n: n['tag'] == 'div' and not n['attrs'].get('class'))
    section_tile = inline('s2', lambda n: any(c['tag'] == 'svg' for c in n['children']))
    section_text = inline('s2', lambda n: n['tag'] == 'div' and any(c['tag'] == 'div' for c in n['children']))
    guides_text = inline('s7', lambda n: any(c['attrs'].get('class') == 'chip' for c in n['children']))
    portrait = inline('s7', lambda n: n['tag'] == 'div' and any(c['tag'] == 'img' for c in n['children']))
    metrics = {
        'canvas-width': stage['width'], 'canvas-height': stage['height'],
        'header-height': header['height'], 'screen-margin': line['left'],
        'rule-height': line['height'], 'footer-bottom': footer['bottom'],
        'content-top': content_text['top'], 'content-text-width': content_text['width'],
        'title-left': title_logo['left'], 'title-logo-top': title_logo['top'],
        'title-logo-height': title_logo['height'], 'title-text-top': title_text['top'],
        'scenario-media-width': scene['width'], 'scenario-media-height': scene['height'],
        'scenario-gap': f'{px(scenario_text["left"]) - px(scene["left"]) - px(scene["width"]):g}px',
        'section-tile-size': section_tile['width'], 'section-tile-left': section_tile['left'],
        'section-text-left': section_text['left'], 'section-text-top': section_text['top'],
        'section-text-width': section_text['width'], 'section-tile-top': section_tile['top'],
        'guides-text-top': guides_text['top'], 'guides-text-width': guides_text['width'],
        'portrait-card-width': portrait['width'], 'portrait-top': portrait['top'],
    }
    for value in metrics.values():
        px(value)
    background = declarations(tree.ids['s1']['attrs']['style'])['background']
    if not re.fullmatch(r'linear-gradient\([0-9a-zA-Z%. #,()-]+\)', background):
        raise ValueError('Unsafe/unsupported mockup title background')
    metrics['title-background'] = background
    refs = []
    for sid, filename in MOCKUP_FILES.items():
        if sid not in tree.ids:
            raise ValueError(f'Missing mockup stage: {sid}')
        path = folder / filename
        raw = path.read_bytes()
        if raw[:8] != b'\x89PNG\r\n\x1a\n':
            raise ValueError(f'Invalid reference PNG: {path}')
        width, height = struct.unpack('>II', raw[16:24])
        if width * 9 != height * 16:
            raise ValueError(f'Reference must be 16:9: {path}')
        refs.append({'id': sid, 'image': 'reference/mockups/' + filename,
                     'width': width, 'height': height, 'input': fingerprint(path)})
    return {'source': fingerprint(source), 'metrics': metrics, 'references': refs,
            'title_background_note': 'The supplied background-title-navy.png contains a central wordmark. It is retained as a reference asset, not placed behind title text. The mockup-defined navy gradient, unchanged white logo and mark avoid duplication; D11 confirmation is still pending.',
            'policy': 'Mockup geometry is compiled from HTML; content flows and may expand vertically. No reference answers or sample results are copied.'}


def layout_for(visual, companion):
    layout = re.match(r'L[1-6]\b', visual.get('layout', ''))
    if not layout:
        raise ValueError(f'{visual.get("screen_id")}: explicit visual-plan layout L1–L6 is required')
    lid = layout.group()
    ref = 's' + lid[-1]
    if lid == 'L1' and len(companion.get('assets', [])) > 1:
        ref = 's7'
    if 'tip card' in companion.get('placement', '').lower():
        ref = 's8'
    return {'id': lid, 'description': visual['layout'], 'reference_id': ref,
            'reference_image': 'reference/mockups/' + MOCKUP_FILES[ref]}


def phase_plan():
    path = PROGRAM / 'draft-slide-phases.json'
    data = json.loads(path.read_text())
    phases = data.get('phases', [])
    ids, modules = set(), []
    for phase in phases:
        if phase['id'] in ids or not phase['modules']:
            raise ValueError('Invalid draft phase plan')
        ids.add(phase['id'])
        for name in phase['modules']:
            if not re.fullmatch(r'0[1-8]_[a-z0-9-]+', name) or not (PLANS / name).is_dir():
                raise ValueError(f'Unknown module in phase plan: {name}')
        modules.extend(phase['modules'])
    if len(set(modules)) != len(modules) or set(modules) != {p.name for p in PLANS.glob('0[1-8]_*') if p.is_dir()}:
        raise ValueError('Draft phases must cover all eight packages exactly once')
    return data
