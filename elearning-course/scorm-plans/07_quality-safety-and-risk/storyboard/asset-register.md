# Visual and audio asset register — Module 07

Production hand-off for review. `Generated` means the file exists (in this repository or in My Clinic's Canva account); `to make` / `planned` means it must still be produced and approved. Every asset still needs its `add_asset` provenance record in Phase 4.

## Generated in this review pack

| Asset id | File | Kind | Provenance | Status | Alt text |
|---|---|---|---|---|---|
| `qsr-img-spo` | [`assets/qsr-img-spo.svg`](assets/qsr-img-spo.svg) | diagram | own (native SVG, palette colours only, no logo) | Draft generated native SVG; improvement-cycle step names pending B11. | Structure leads to processes, which lead to outcomes. |
| `qsr-img-matrix` | [`assets/qsr-img-matrix.svg`](assets/qsr-img-matrix.svg) | diagram | own (native SVG, palette colours only, no logo) | Draft generated native SVG; scores final, band names/colours pending B6 (every cell has a band slot). | Risk matrix: impact by likelihood, scores 1 to 25. |
| `qsr-img-iceberg` | [`assets/qsr-img-iceberg.svg`](assets/qsr-img-iceberg.svg) | diagram | own (native SVG, palette colours only, no logo) | Draft generated native SVG; terms pending B8. | Iceberg: critical incidents at the tip, adverse events below, near misses at the base. |

## Programme companions used in this module (shared, not module art)

Source: [`companions.md`](../../00_program/characters/companions.md) §3. The full-size production files (PNG with a transparent background) are in [`../../00_program/characters/assets/`](../../00_program/characters/assets/) — imported 2026-10-15; the untouched originals are in `assets/originals/` and the Canva media ids below stay for traceability (`https://www.canva.com/M/<media id>`). There is **no module-specific character art or prompt** for module 07.

| Asset id | Canva media id / route | Screens | Status | Alt text | Preview |
|---|---|---|---|---|---|
| `char-noor-welcome` | MAHX-pFaNMU | qsr-000 | Generated (Canva AI); in `00_program/characters/assets/` | Noor, the safety liaison, smiling and waving in welcome. | [preview](../../00_program/characters/previews/char-noor-welcome.jpg) |
| `char-noor-listening` | MAHX-v3i0kY | qsr-002 | Generated (Canva AI); in `00_program/characters/assets/` | Noor, the safety liaison, holding a tablet and listening. | [preview](../../00_program/characters/previews/char-noor-listening.jpg) |
| `char-noor-avatar-neutral` | MAHX-n4HuyU | qsr-051 | Generated (Canva AI); in `00_program/characters/assets/` | Noor, the safety liaison. | [preview](../../00_program/characters/previews/char-noor-avatar-neutral.jpg) |
| `char-noor-avatar-concern` | crop from char-noor-concern (MAHX-hFE0aQ) | qsr-021, qsr-051 | Ready (full-size crop in `00_program/characters/assets/`, 2026-10-15) | Noor, the safety liaison, looking concerned. | [preview](../../00_program/characters/previews/char-noor-concern.jpg) |
| `char-noor-avatar-happy` | crop from char-noor-success (MAHX-jiR90M) | qsr-021, qsr-051 | Ready (full-size crop in `00_program/characters/assets/`, 2026-10-15) | Noor, the safety liaison, smiling. | [preview](../../00_program/characters/previews/char-noor-success.jpg) |
| `char-noor-success` | MAHX-jiR90M | qsr-092 | Generated (Canva AI); in `00_program/characters/assets/` | Noor, the safety liaison, smiling and giving a thumbs up. | [preview](../../00_program/characters/previews/char-noor-success.jpg) |
| `char-omar-thinking` | MAHX-jgu1Vk | qsr-031 | Generated (Canva AI); in `00_program/characters/assets/` | Dr. Omar, the family physician, with his hand at his chin, thinking through the risk score. | [preview](../../00_program/characters/previews/char-omar-thinking.jpg) |
| `char-omar-avatar-neutral` | MAHX-nPHDkA | qsr-040 | Generated (Canva AI); in `00_program/characters/assets/` | Dr. Omar, the family physician. | [preview](../../00_program/characters/previews/char-omar-avatar-neutral.jpg) |
| `char-omar-avatar-happy` | crop from char-omar-success (MAHX-llCU5M) | qsr-092 | Ready (full-size crop in `00_program/characters/assets/`, 2026-10-15) | Dr. Omar, the family physician, smiling. | [preview](../../00_program/characters/previews/char-omar-success.jpg) |

## Planned assets from Phase 3

| Planned id | Kind | Screens | Brief | Source route | Alt text / accessibility note |
|---|---|---|---|---|---|
| `qsr-img-quote` | SVG/typography | qsr-001 | Quote on brand background, no imagery | own | n/a (text in HTML) |
| `qsr-img-spo` | SVG | qsr-010 | Three linked blocks — draft SVG generated (see above) | own | "Structure leads to processes, which lead to outcomes." |
| `qsr-img-pillars` | illustration | qsr-020 | Six pillars with numbered icons (ID band, speech bubble, red-label vial, surgical checklist, hands, yellow band) — no NotebookLM frames reused | ai-generated / own | "Six patient safety goals as six pillars." |
| `qsr-img-wristbands` | illustration | qsr-021 | Two wristbands with the same name, different MRN and DOB (fictional data) | ai-generated | "Two patient wristbands with the same name and different record numbers." |
| `qsr-img-matrix` | SVG | qsr-031, 032 | 5×5 matrix, band colours and band names in every cell (B6) — draft SVG generated (see above) | own | "Risk matrix: impact by likelihood, scores 1 to 25." |
| `qsr-img-iceberg` | SVG | qsr-040 | Iceberg with three labelled layers — draft SVG generated (see above) | own | "Iceberg: critical incidents at the tip, adverse events below, near misses at the base." |
| `qsr-vid-speakup (optional)` | video + VTT | qsr-060 | ≤ 60 s, recorded in-house, consent on file, captions | own | transcript |
| `char-noor- / char-omar-` | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Noor, the safety liaison, explaining." |

## Audio

One file per narrated screen, `MC07-clinical-governance_<screen>.mp3` (22 files). `qsr-092` is recorded as two lines (`noor-1`, `omar-1`), joined with 0.3 s silence and normalised. Voices and provider pending **D10**; see [`voice_talent.md`](voice_talent.md).

## Non-negotiable production rules

- Use the supplied My Clinic logo PNGs; never generate, redraw or bake the logo into an AI image or diagram.
- AI images contain no text, letters, numbers, brand names or real patient/staff likenesses; wristband identifiers stay HTML text.
- Companion images come only from the approved programme set; never re-prompt Noor or Dr. Omar per module.
- Keep diagrams as SVG/HTML so pending B6/B8/B11 wording can be replaced after SME review; never show a risk band by colour alone.
- The source video's frames and narration are not reused (D7).
