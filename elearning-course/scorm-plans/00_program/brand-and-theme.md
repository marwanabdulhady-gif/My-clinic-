# Brand kit and theme (all modules)

Playbook topic: `get_playbook('brand')` · Gate: `brand_to_theme(brand)` → `set_theme(project_id, theme_tokens)`

## 1. Where the brand comes from

In this order (playbook rule: **never invent brand colours**):

1. My Clinic brand guidelines PDF (exact hex values, fonts, logo rules). **Owner: Marketing / Communications.** Not in the source pack yet; request it in Phase 0.
2. Approved materials already in the pack: the HR deck template (`google_drive/HR.pptx`) and the intranet home page (slide 53). Sample the colours only if the guide is not available, and mark them *"sampled, awaiting confirmation"*.
3. Logo file (from Marketing).

Do **not** use the Health & Safety 2 template colours. Its PDF metadata says *"First Clinic"* with a different author, so it may be another organisation's template (README item 15).

## 2. Brand kit to fill (draft)

```json
{
  "name": "My Clinic",
  "colors": {
    "primary": "<from brand guide>",
    "secondary": "<from brand guide>",
    "accent": "<from brand guide — use for warnings and key numbers only>",
    "dark": "<near-black or dark navy body text>",
    "light": "<off-white page background>",
    "surface": "#FFFFFF"
  },
  "fonts": {
    "heading": "<brand heading font> (Latin) + Tajawal or IBM Plex Sans Arabic (Arabic)",
    "body": "<brand body font> (Latin) + Tajawal or IBM Plex Sans Arabic (Arabic)"
  },
  "imagery_style": "Clean flat illustration and real My Clinic photos (with consent). White space first, one idea per screen, line icons. No stock clichés, no clip art, no watermarks.",
  "voice": {
    "tone": "warm, calm, precise",
    "persona": "an experienced colleague coaching a new team member on their first week",
    "formality": "conversational-professional"
  },
  "do": [
    "One idea per screen; keywords on screen, explanation in narration",
    "Use the brand accent only for warnings, codes and key numbers",
    "Real HTML text, never text baked into images",
    "Arabic and English names of emergency codes where the facility poster is bilingual"
  ],
  "dont": [
    "No decorative elements that do not help learning",
    "No NotebookLM or other third-party watermarks in any asset",
    "No real patient data, ever",
    "No staff photos or names without written consent"
  ]
}
```

## 3. Theme decision

| Option | Use when |
|---|---|
| `brand_to_theme(brand)` result + style preset `style-minimal` | **Default.** Brand guide received. Matches the minimalist look the course owner prefers. |
| `themes/corporate/brand-clinical.json` (teal `#0f726a`) | Fallback for internal drafts **only** while the brand guide is pending. Label previews "Draft theme". |
| `high-contrast` | Accessibility variant on request. |

Contrast gate: `brand_to_theme` must report no `error` pairs (text below 4.5:1). If it darkens `primary`, tell Marketing; it is a visible brand change.

## 4. Colour roles per screen (60-30-10)

| Screen kind | Background | Text | Accent use |
|---|---|---|---|
| Title / section opener | `primary` | `on_primary` | none |
| Content, accordion, tabs | `light` / `surface` | `dark` | key number or warning only |
| Question / activity | `surface` | `dark` | feedback states use `success` / `error` |
| Emergency code cards | `surface` with a **colour chip** for the code | `dark` | code colour is never the only cue: always print the code name |

Rule: the accent appears as a background on no more than 10% of screens (lint code `accent_overuse`).

## 5. Visual system (minimalist)

- **Icons:** one line-icon family across all eight packages (e.g. a CC0 or own set). Record provenance for each.
- **Illustrations:** flat, two or three brand colours, white background. Used for scenarios (clinic corridor, store room, consultation room).
- **Diagrams:** authored SVG via `svg_to_asset` (fire triangle, NFPA diamond, AREC cycle, risk matrix, iceberg, org charts, process steps). Real text, not images of text.
- **Photos:** only My Clinic's own photos with consent (branches, equipment, eyewash station, spill kits, extinguisher label). Source-deck photos may be reused only after Phase 0 confirms the rights.
- **Characters:** one fictional mentor used across modules (see `narration-and-lexicon.md` §5). Optional; scenarios work without them.

## 6. Arabic / bilingual plan

- **Release 1: English (`language: "en"`).** All sources are in English.
- **Release 2: Arabic (`language: "ar"`)**, after release 1 is signed off. The player switches to right-to-left automatically, but the edumints roadmap notes that Arabic player strings are **not localised yet** (controls fall back to English). Raise this with the edumints maintainer or accept English controls for release 2.
- Keep emergency code names bilingual on the code cards in release 1 (the facility poster in H&S 2 page 5 is bilingual).
- Arabic fonts: Tajawal, Cairo or IBM Plex Sans Arabic. A Latin-only brand font breaks Arabic text.
