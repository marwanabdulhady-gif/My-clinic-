"""Phase 3 visual planning helpers. No asset production, approval or inferred interaction key."""
from __future__ import annotations

import re

DRILL_SCENES = [
    ('Rescue', 'Smoke in a consultation room with an unnamed patient.',
     'Consultation room with smoke and an unnamed patient; no real person or identifier.'),
    ('Alarm', 'Call point and phone; call-script wording is editable HTML after approval.',
     'Fire alarm call point beside a telephone; labels and call script are separate editable text.'),
    ('Contain', 'Oxygen cylinder and alcohol rub; containment cues follow the signed node list.',
     'Consultation-room scene with an oxygen cylinder, alcohol rub and a door.'),
    ('Extinguish or evacuate', 'Small bin fire versus spreading fire; depict both states in separate editable layers.',
     'Bin-fire scene with a separate spreading-fire state for the authored decision.'),
    ('Evacuate', 'Stairwell with evacuation chair and an unnamed wheelchair user; no real floor plan.',
     'Generic stairwell with an evacuation chair and an unnamed wheelchair user.'),
    ('Assembly point', 'Generic assembly point; local names and all-clear wording remain editable.',
     'Generic outdoor assembly point with unnamed colleagues waiting.'),
]
# State descriptions follow the numbered actions in module 08 Phase 2, not a fabricated EHR UI.
CAPTURE_STEPS = {
    'dx': ['Add Diagnosis dialog', 'Diagnosis search with draft E11 input', 'Diagnosis results',
           'Primary diagnosis details, onset and chronicity', 'Diagnosis favourites star'],
    'order': ['Order search', 'Drug-name search using the approved B6 example',
              'Medication route, dose, frequency and duration fields', 'Assessed-diagnosis selection',
              'Patient-instructions fields', 'Order submission control'],
    'wizard': ['Package search using the approved B6 example', 'Form Wizard item review',
               'Form Wizard item removal', 'Form Wizard finalisation'],
    'summary': ['Consultation Summary entry', 'Lab orders, special tests and referrals in summary',
                'Download and Print control'],
    'sms': ['Send SMS educational-material entry', 'SMS department selection',
            'SMS diagnosis-code search', 'SMS leaflet selection', 'SMS Send control'],
    'ref': ['Referral entry', 'Referral specialty selection', 'Referral-reason field',
            'Referral type and timing fields', 'Follow-up toggle and interval', 'Referral Save control'],
}


def expand_ids(raw: str) -> list[str]:
    """Expand 1..N and slash-separated IDs without losing wildcard or optional notation."""
    result = []
    for part in raw.replace('`', '').split(' / '):
        part = re.sub(r'\s*\*?\(optional\)\*?', '', part).strip()
        match = re.fullmatch(r'(.+-)(\d+)\.\.(\d+)', part)
        if match:
            first, last = int(match[2]), int(match[3])
            if first < 1 or last < first or last - first > 100:
                raise ValueError(f'Invalid asset range: {raw}')
            result.extend(f'{match[1]}{i}' for i in range(first, last + 1))
        else:
            result.append(part)
    return result


def screen_ids(text: str) -> list[str]:
    # Phase 3 also uses compact lists: `ehr-010, 011` and `hs2-060, 062, 063, 064`.
    result, prefix = [], None
    for match in re.finditer(r'(?<![a-z0-9-])(?:([a-z0-9]+)-)?(\d{3})(?!\d)', text):
        prefix = match[1] or prefix
        if prefix:
            result.append(f'{prefix}-{match[2]}')
    return result


def assets_for_screen(assets: list[dict], sid: str) -> list[dict]:
    # Exact matches only: ehr-010 is not ehr-0100. Shared assets may have multiple placements.
    return [asset for asset in assets if sid in screen_ids(asset['screens'])]


def production_gate(aid: str) -> str:
    if aid == 'hs1-img-treatment-room':
        return 'PENDING 01 B6; Facilities confirms equipment, sockets and visual targets before illustration/hotspots.'
    if aid == 'hs1-img-pump-label':
        return 'PENDING Biomedical/Facilities confirmation of the inspection-label rule; fictional dates in an editable HTML overlay.'
    if aid == 'hs1-img-eyewash':
        return 'PENDING My Clinic photo permission and Facilities/EHS approval of the pictured unit.'
    if aid.startswith('hs2-img-drill-'):
        return 'PENDING D1/D2 and 02 B2/B8 as applicable; Safety Manager signs all six nodes/scenes, code wording and assembly-point treatment.'
    if aid == 'hs2-img-spill-photo':
        return 'PENDING D1 / 02 B1 threshold; EHS signs volume cue and puzzle context before illustration.'
    if aid in {'hs2-img-extinguisher', 'hs2-img-kit-chem', 'hs2-img-kit-bio'}:
        return 'PENDING client photo permission and EHS/Safety equipment review; kit procedure also awaits 02 B4.'
    if aid.startswith('ehr-shot-'):
        common = 'PENDING 08 B2/D6: approved test environment, fictional patient, per-file DPO review; B3 version and B5 labels confirmed.'
        extra = (' B4 mandatory fields.' if aid == 'ehr-shot-form' else
                 ' B6 Pharmacy-approved examples.' if '-order-' in aid or '-wizard-' in aid else
                 ' B8 SMS feature/leaflets; fictional phone only.' if '-sms-' in aid else
                 ' B9 referral timing and approved reason.' if '-ref-' in aid else '')
        return common + extra
    return 'PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.'


def expand_asset(row: dict) -> list[dict]:
    result = []
    for aid in expand_ids(row['id']):
        asset = {**row, 'id': aid, 'manifest_id': row['id'],
                 'optional': '(optional)' in row['id'], 'gate': production_gate(aid),
                 'placement': 'Screen visual; production placement reviewed by the SME.'}
        drill = re.fullmatch(r'hs2-img-drill-(\d)', aid)
        capture = re.fullmatch(r'ehr-shot-([a-z]+)-(\d+)', aid)
        if drill:
            index = int(drill[1]) - 1
            label, brief, alt = DRILL_SCENES[index]
            asset.update(brief=brief, alt=alt, placement=f'Node {index + 1} · {label}')
        elif capture:
            group, index = capture[1], int(capture[2]) - 1
            label = CAPTURE_STEPS[group][index]
            asset.update(brief=f'{label}; capture in approved test environment, 1920×1080 at 125% zoom.',
                         alt=f'Test-patient EHR screen showing {label.lower()}; no real identifiers.',
                         placement=f'Step {index + 1} · {label}')
        elif aid == 'ehr-shot-list':
            asset['placement'] = 'ehr-010 step 1 · consultation list'
        elif aid == 'ehr-shot-form':
            asset['placement'] = 'ehr-010 step 2; reused on ehr-011 for mandatory-field exploration'
        elif aid == 'hs2-img-kit-chem':
            asset.update(alt='Chemical spill kit supplied by My Clinic; equipment and colour await EHS review.', placement='Left comparison image')
        elif aid == 'hs2-img-kit-bio':
            asset.update(alt='Biological spill kit supplied by My Clinic; equipment and colour await EHS review.', placement='Right comparison image')
        elif aid == 'hs1-img-pump-label':
            asset['brief'] += '; label dates and overdue status in editable HTML, not AI-rendered lettering.'
        result.append(asset)
    return result


def is_visual(asset: dict) -> bool:
    kind = asset['kind'].lower()
    return not any(word in kind for word in ['audio', 'character', 'pdf', 'mp4', 'vtt']) and not asset['id'].endswith('*')


def imagery_entry(asset: dict) -> dict:
    kind = asset['kind'].lower()
    kind = ('screenshot' if 'screenshot' in kind else 'photo' if 'photo' in kind else
            'diagram' if any(word in kind for word in ['svg', 'diagram', 'html']) else 'illustration')
    route = ('client' if kind in {'screenshot', 'photo'} else 'svg' if 'own' in asset['source'].lower()
             else 'generate' if 'ai' in asset['source'].lower() else 'client')
    return {'kind': kind, 'description': f"{asset['id']}: {asset['brief']} Placement: {asset['placement']} {asset['gate']}",
            'source': route, 'alt_text': asset['alt'] if asset['alt'].lower() != 'n/a' else 'Editable on-screen diagram; equivalent text provided in HTML.',
            'decorative': False}
