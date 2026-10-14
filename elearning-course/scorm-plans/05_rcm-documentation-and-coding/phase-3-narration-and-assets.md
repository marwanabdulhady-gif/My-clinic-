# Phase 3 — Narration & assets (05 RCM Part A)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## 1. Tone

Peer-to-peer: a senior physician talking to colleagues, not a billing department. Short, respectful, a little candid ("Most of us were never taught this in training. I wasn't either.").

## Companions in this module (Noor and Dr. Omar)

Character bible: [`../00_program/characters/companions.md`](../00_program/characters/companions.md). **Lead host: Omar** (narrates every narrated screen unless listed below). **Co-host: Noor**.

| Screen | Visible | Pose / asset | Placement (brand layout) | Speaks | What they do |
|---|---|---|---|---|---|
| rcma-000 | Omar | `char-omar-welcome` | L1 half-body bottom-right | Omar | Welcome, peer-to-peer |
| rcma-001 | Omar | `char-omar-explaining` | L3 right column | Omar | Claims story (companions.md §1) |
| rcma-011 | Noor | `char-noor-avatar-neutral + tip card` | L3 tip card | Noor | Tip: nurses' notes count too — vital signs justify the order |
| rcma-031 | Omar | `char-omar-avatar-thinking → -happy / -concern` | L5 avatar | Omar | Joint-pain case host |
| rcma-050 | Omar + Noor | `char-omar-avatar (host); char-noor-tip (hints)` | L5 | Omar + Noor | "Fix the note" game: Omar hosts, Noor gives the hints |
| rcma-091 | Omar | `char-omar-success` | L6 right | Omar | Close with the desk checklist |

- Visible on 6 screens (about one in three or fewer). Not visible on question screens except as a feedback avatar.
- Spoken lines in scripts are prefixed `OMAR:` / `NOOR:`; two-voice screens are split into one segment per line (`part` = `omar-1`, `noor-1`, …) and joined into one audio file per screen (companions.md §5).
- Character images are the shared program assets `char-noor-*` / `char-omar-*` (companions.md §3); no module-specific character art.

## 2. Narration outline

| Screen | Speaker | Sec | Narration intent |
|---|---|---|---|
| rcma-000 | Omar | 12 | 25 minutes to fewer rejected claims and fewer calls from RCM. |
| rcma-001 | Omar | 30 | The reviewer only has your note; good documentation protects the patient, you and the clinic. |
| rcma-002 | Omar | 8 | Invite a guess. |
| rcma-010 | Omar | 35 | What always goes in, what never should. |
| rcma-011 | Noor | 25 | Same patient, same fluids; one note gets paid. |
| rcma-012 / 013 | Omar | 8 each | Set up. |
| rcma-020 | Omar | 35 | Coding is clinical translation; specific codes get accepted. |
| rcma-021 | Omar | 8 | Set up. |
| rcma-022 | Omar | 40 | Talk through the provisional diagnosis: honest about uncertainty, still specific. |
| rcma-023 | Omar | 10 | Set up; mention the BMI nuance only in feedback. |
| rcma-030 | Omar | 35 | Defensive medicine feels safe but gets rejected; follow work-up protocols, document deviations. |
| rcma-031 | Omar | 15 | Set up the joint-pain patient. |
| rcma-032 / 033 | Omar | 8 each | Set up. |
| rcma-040 | Omar | 10 | Set up; "let's check your earlier guess". |
| rcma-041 | Omar | 30 | Coverage changes often; Part B covers what's new. |
| rcma-042 | Omar | 8 | Set up. |
| rcma-050 | Omar + Noor | 15 | Three notes, your pen. |
| rcma-090 | Omar | 10 | Read your results. |
| rcma-091 | Omar | 25 | The six-point checklist to keep at your desk. |

Estimated audio: ~8 minutes.

## 3. Lexicon used

RCM, CDI, HPI, ICD-10, CCHI/CHI (after D4), BMI, HbA1c, PCOS, HRT ("H-R-T"), CRP ("C-R-P"), ESR ("E-S-R"), anti-Ro ("anti-row"), anti-La ("anti-lah"), URTI ("U-R-T-I"), MRI, CBC; ICD-10 codes letter-by-letter (J03 → "J zero three").

## 4. Asset manifest

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| rcma-img-note-weak / -strong | SVG note cards | rcma-011 | Two identical-size EHR-style note cards (generic, no vendor UI), weak vs strong text | own | "Weak note: patient given IV fluids." / "Strong note: dehydration signs, IV fluids for stabilisation." |
| rcma-img-reviewer | SVG | rcma-001 | Minimal illustration: note on one side, reviewer with only the paper on the other | own | "A reviewer sees only the written note." |
| rcma-img-notes-1..3 | HTML | rcma-050 | Invented notes in HTML (real text) | own | n/a |
| rcma-pdf-checklist | PDF | rcma-091 | One-page "Clear, strong, defensible" desk checklist | own | n/a |
| char-noor-* / char-omar-* | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." |
| rcma-aud-* | audio | narrated screens | TTS (peer tone) | ai-generated | transcript |

No source-deck images are used (claim data and branding questions sit with module 06).

## 5. Activity plans

| Activity | Objective | Rules | Success | Accessibility |
|---|---|---|---|---|
| rcma-031 joint pain | rcma-o3 | 2 nodes | both best | buttons |
| rcma-050 fix the note | rcma-o5 | `case_sim`, 3 nodes, +1 best rewrite, 1 hint each, no lives, no timer | `pass_score` 2 | buttons; rewrites are text |

## 6. Approval request

Medical Director: all clinical vignettes. Coding lead: every code on every screen and in feedback. RCM lead: rules, intervals, tone. Payer relations: coverage statements.
