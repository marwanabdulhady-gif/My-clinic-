# Phase 3 — Narration & assets (06 RCM Part B)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## Companions in this module (Noor and Dr. Omar)

Character bible: [`../00_program/characters/companions.md`](../00_program/characters/companions.md). **Lead host: Omar** (narrates every narrated screen unless listed below). **Co-host: Noor**.

| Screen | Visible | Pose / asset | Placement (brand layout) | Speaks | What they do |
|---|---|---|---|---|---|
| rcmb-000 | Omar | `char-omar-welcome` | L1 half-body bottom-right | Omar | Welcome |
| rcmb-030 | Noor | `char-noor-avatar-neutral + tip card` | L3 tip card | Noor | Tip: document the diagnosis and the impact on daily life — that is what gets mental-health care approved |
| rcmb-050 | Omar | `char-omar-explaining` | L3 right column | Omar | Rejection-log story (companions.md §1) |
| rcmb-052 | Omar | `char-omar-avatar-neutral → -happy / -concern` | L5 avatar | Omar | Rework scenario host |
| rcmb-091 | Omar + Noor | `char-omar-success + char-noor-avatar-happy` | L6 | Omar + Noor | Two-voice close |

- Visible on 5 screens (about one in three or fewer). Not visible on question screens except as a feedback avatar.
- Spoken lines in scripts are prefixed `OMAR:` / `NOOR:`; two-voice screens are split into one segment per line (`part` = `omar-1`, `noor-1`, …) and joined into one audio file per screen (companions.md §5).
- Character images are the shared program assets `char-noor-*` / `char-omar-*` (companions.md §3); no module-specific character art.

## 1. Narration outline

| Screen | Speaker | Sec | Narration intent |
|---|---|---|---|
| rcmb-000 | Omar | 12 | Twenty minutes on what's new and why claims still bounce. |
| rcmb-001 | Omar | 30 | Benefits change; documentation decides whether a covered service is actually paid. |
| rcmb-010 | Omar | 10 | Set up the sort. |
| rcmb-020 | Omar | 40 | Prevention is now covered: think of the patient in front of you who is due a screen. |
| rcmb-021 | Omar | 8 | Set up. |
| rcmb-030 | Noor | 35 | Mental-health cover is wider, but it has a limit and needs pre-authorisation for some services. |
| rcmb-031 | Omar | 8 | Set up. |
| rcmb-040 | Omar | 45 | Five benefits that change what you can offer at discharge, by phone, for diabetes and for women's health. |
| rcmb-041 | Omar | 8 | Set up. |
| rcmb-050 | Omar | 30 | How to read a rejection comment; each one tells you what to fix. Omar's story: "The first time I read our log I recognised two of my own claims." |
| rcmb-051 / 052 | Omar | 8 / 15 | Set up. |
| rcmb-060 | Omar | 10 | Set up adaptive practice. |
| rcmb-090 | Omar | 10 | Read your results. |
| rcmb-091 | Omar + Noor | 20 | Four habits; keep the one-page summary handy. |

Estimated audio: ~5 minutes.

## 2. Lexicon used

EBP, CHI/CCHI (after D4), MOH, FIT, DEXA, FBS ("F-B-S"), HbA1c, Tdap, PCV13, PPSV23, PTSD, IUD ("I-U-D"), OPD ("O-P-D"), SAR, PCOS.

## 3. Asset manifest

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| rcmb-img-benefit-icons | SVG ×12 | rcmb-010, 020, 040 | Line icons per benefit | own | decorative |
| rcmb-tbl-log | HTML table | rcmb-050, 051 | Rebuilt rejection rows (B8); invented ids `CLM-0001`…; no names, dates or providers | own | n/a |
| rcmb-pdf-ebp | PDF | rcmb-091 | One-page EBP summary from the official document (B3), approved by payer relations | own | n/a |
| char-noor-* / char-omar-* | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." |
| rcmb-aud-* | audio | narrated screens | TTS | ai-generated | transcript |

**Not used:** the slide-6 screenshot, the CHI logo (third-party mark), the slide-8 infographic image. Text is rebuilt in HTML.

## 4. Activity plans

| Activity | Objective | Rules | Success | Accessibility |
|---|---|---|---|---|
| rcmb-051 classify | rcmb-o3 | 8 items, 5 targets | all correct for full points | keyboard |
| rcmb-052 rework | rcmb-o3 | 3 nodes | all best | buttons |
| rcmb-060 adaptive | rcmb-o2 | Elo, 15-item bank, max 8 | pass ratio 0.6 | radio buttons |

## 5. Approval request

Payer relations approves every benefit statement and the 15 adaptive items. DPO approves the rebuilt log. RCM lead approves the rest.
