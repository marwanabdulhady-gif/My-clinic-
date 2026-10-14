# Phase 3 — Narration & assets (06 RCM Part B)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## 1. Narration outline

| Screen | Sec | Narration intent |
|---|---|---|
| rcmb-000 | 12 | Twenty minutes on what's new and why claims still bounce. |
| rcmb-001 | 30 | Benefits change; documentation decides whether a covered service is actually paid. |
| rcmb-010 | 10 | Set up the sort. |
| rcmb-020 | 40 | Prevention is now covered: think of the patient in front of you who is due a screen. |
| rcmb-021 | 8 | Set up. |
| rcmb-030 | 35 | Mental-health cover is wider, but it has a limit and needs pre-authorisation for some services. |
| rcmb-031 | 8 | Set up. |
| rcmb-040 | 45 | Five benefits that change what you can offer at discharge, by phone, for diabetes and for women's health. |
| rcmb-041 | 8 | Set up. |
| rcmb-050 | 30 | How to read a rejection comment; each one tells you what to fix. Mentor: "The first time I read our log I recognised two of my own claims." |
| rcmb-051 / 052 | 8 / 15 | Set up. |
| rcmb-060 | 10 | Set up adaptive practice. |
| rcmb-090 | 10 | Read your results. |
| rcmb-091 | 20 | Four habits; keep the one-page summary handy. |

Estimated audio: ~5 minutes.

## 2. Lexicon used

EBP, CHI/CCHI (after D4), MOH, FIT, DEXA, FBS ("F-B-S"), HbA1c, Tdap, PCV13, PPSV23, PTSD, IUD ("I-U-D"), OPD ("O-P-D"), SAR, PCOS.

## 3. Asset manifest

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| rcmb-img-benefit-icons | SVG ×12 | rcmb-010, 020, 040 | Line icons per benefit | own | decorative |
| rcmb-tbl-log | HTML table | rcmb-050, 051 | Rebuilt rejection rows (B8); invented ids `CLM-0001`…; no names, dates or providers | own | n/a |
| rcmb-pdf-ebp | PDF | rcmb-091 | One-page EBP summary from the official document (B3), approved by payer relations | own | n/a |
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
