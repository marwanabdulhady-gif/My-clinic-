# Brand kit and theme (all modules)

![My Clinic logo](brand/logo-preview.png)

Playbook topic: `get_playbook('brand')` · Gate: `brand_to_theme(brand)` → `set_theme(project_id, theme_tokens)`

**The full brand guide for designers and AI agents is [`brand/brand-identity.md`](brand/brand-identity.md).** This page is the short summary and the decisions that sit around it.

## 1. Where the brand comes from

The My Clinic logo, colours, font and graphic elements were taken from My Clinic's own official decks in the course folder:

- `HR.pptx` — Employee Induction deck in the company template (logo lock-up, navy title backgrounds, petal watermark, Montserrat, values colours).
- `Operations & My Care Structure.pptx` — logo block with the four value tiles and the tagline "Where your health matters".

Colours were sampled from the original image files. They are ready to use. **Marketing still confirms them against the official brand guide (decision D11)**; if anything changes, edit only `brand/brand-identity.md` and `brand/brand-kit.json`.

Do **not** use the Health & Safety 2 template colours (PDF metadata says *"First Clinic"*, another organisation — decision D12) or the L2S/e-leap proposal colours.

## 2. Brand at a glance

| Item | Value |
|---|---|
| Logo | Five-petal mark + عيادتي + My Clinic. Files in [`brand/assets/`](brand/assets/): `logo-horizontal-navy.png` (on light), `logo-horizontal-white.png` (on navy), `mark-navy.png` / `mark-white.png` |
| Tagline | Where your health matters |
| Primary | Navy **#003867** |
| Value colours | Caring purple **#652D8C** · Ambitious teal **#008C99** (small text: **#006E78**) · Responsible magenta **#9D3293** · Collaborative burgundy **#7C0041** |
| Neutrals | Ink #1F2A37 · Muted #5B6B7B · Mist #C0CED9 · Off-white #F4F7FA · White |
| Accent (warnings, key numbers) | Magenta #9D3293 |
| Font | Montserrat (Bold titles, SemiBold subheads, Regular/Medium body); Arabic: Tajawal (proposed) |
| Motifs | Large petal watermark, 2 px navy header rule, square value tiles with white line icons, rounded cards, pill buttons |
| Imagery | Flat vector, navy outlines, white space, one module colour highlight, no text in images |
| Brand kit for edumints | [`brand/brand-kit.json`](brand/brand-kit.json) |
| Screen mockups | [`brand/screen-mockups/`](brand/screen-mockups/) (L1 Title … L6 Results) |

## 3. Theme decision

| Option | Use when |
|---|---|
| `brand_to_theme(brand/brand-kit.json)` + style preset `style-minimal` | **Default** for all eight packages |
| `high-contrast` | Accessibility variant on request |

Per project, set the **module colour** (table in `brand-identity.md` §2) as the `secondary` role. Embed Montserrat (SIL OFL) as a custom font.

Contrast gate: `brand_to_theme` will flag teal #008C99 for small text (4.0 : 1). That is expected: small teal text uses #006E78; white text on teal must be large/bold.

## 4. Colour roles per screen (60-30-10)

| Screen kind (layout) | Background | Text | Highlight |
|---|---|---|---|
| L1 Title | Navy gradient | White, subtitle Mist | Module chip |
| L2 Section opener | White + petal watermark | Navy | Module-colour tile |
| L3 Content | White | Ink / Navy headings | Module colour bullets; magenta callout (max one) |
| L4 Question | Off-white | Ink / Navy stem | Selected option navy; feedback green/red with icon + words |
| L5 Scenario | White | Ink | Companion avatar ring (Noor purple / Omar teal) |
| L6 Results / close | Off-white | Navy | Weak objectives flagged with icon + text |

Emergency-code colours are content, shown as small chips next to the printed name, never as backgrounds.

## 5. Arabic / bilingual plan

- **Release 1: English (`language: "en"`).** All sources are in English. The logo already carries the Arabic name.
- **Release 2: Arabic (`language: "ar"`)** after release 1 is signed off. RTL works automatically, but edumints player strings are not yet localised into Arabic (controls fall back to English).
- Bilingual emergency-code cards in release 1 use Tajawal for Arabic.
