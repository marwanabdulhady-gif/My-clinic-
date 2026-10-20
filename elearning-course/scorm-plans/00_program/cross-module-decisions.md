# Cross-module decisions (decision log)

These decisions affect more than one package. Record the final answer here **once**, then every module's Phase 0 points to this file. Item numbers in brackets refer to `../../README.md` §3.

| # | Decision needed | Modules | Options / recommendation | Owner | Status | Decision |
|---|---|---|---|---|---|---|
| D1 | **Code Orange spill threshold** [1] | 01, 02 | Recommended: *spill ≥ 500 mL, or any highly toxic/reactive/explosive substance → Code Orange; otherwise call the cleaning supervisor.* Removes the "< 1 L minor spill" wording. | Safety & Security Manager | Open | |
| D2 | **Emergency code sheet** — one naming set (e.g. Code Silver "violent situation involving a weapon" vs "active shooter with weapon"; RRT included or not) and the **real extension numbers** (decks show "5555") [2] | 01, 02, 07 | Use the facility's current MOH code poster as the single source. Code Blue 2222 is national. | Safety & Security Manager + Switchboard | Open | |
| D3 | **Branch names and codes**: J3 Al Andalus vs Al Tahlia; J4 Abhor vs Obhur; PR1 vs PRC [6] | 03, 04 | Use the names on the current branch signage / official website. | HR + Operations | Open | |
| D4 | **Regulator name**: CCHI vs CHI (Council of Health Insurance) [7] | 05, 06 | Use the regulator's current official English name and acronym throughout. | RCM lead (Dr Wafaa Elshayeb or successor) | Open | |
| D5 | **Personal data policy for the course**: staff names, photos, emails, claim numbers [17] | 03, 04, 06 | Recommended: roles on screen, names in a linked live directory; leadership photos only with consent; claim log fully anonymised and rebuilt. | HR + Data Protection Officer | Open | |
| D6 | **IT video with patient identifiers** [13, 18] | 08 | Do not use `IT.mp4` in any package. Re-capture all screens on a test patient. Separately decide whether to purge the file from Git history. | IT + Data Protection Officer | Open | |
| D7 | **Quality video licence and watermark** [12, 16] | 07 | Recommended: rebuild natively; do not ship the NotebookLM video. Optional: a new short intro video made in-house. | Quality Director | Open | |
| D8 | **Incident reporting window** — 24 hours (Quality video and HR ethics slide) | 03, 07 | Confirm against the incident-reporting policy; keep the same wording in both modules. | Quality / Risk Manager | Open | |
| D9 | **LMS and SCORM version** | all | My Clinic uses Oracle Applications Cloud (HR source: Oracle self-service), so the LMS is expected to be **Oracle Learning**. Recommended: **SCORM 1.2 for all eight packages** (Oracle documents 1.2 and 2004 Ed. 2–3; compiler emits 2004 4th Ed.). Confirm with the sample package test (`00_sample-oracle-pilot/`). | L&D / IT | Open — recommendation applied to builds, awaiting Oracle sample-test result | |
| D10 | **Voice route and provider** | all | External English TTS for release 1 (see `narration-and-lexicon.md`). | Course owner | Open | |
| D11 | **Brand kit** | all | Brand taken from My Clinic's own decks (`brand/brand-identity.md`): navy #003867, value colours, Montserrat, logo files. Marketing to confirm or send the official guide. | Marketing | Open — draft in use | |
| D12 | **Template origin of H&S 2** ("First Clinic" metadata) [15] | 02 | Do not reuse H&S 2 template art until confirmed. | Safety & Security Manager | Open | |
| D13 | **Clinical Risk and Infection Control sessions** (on the HR agenda but no source) [5] | 03, program | Out of scope for these eight packages. Flag as a gap in the induction curriculum. | L&D | Open | |
| D14 | **Completion record / acknowledgement form** (H&S 1 page 65 asks staff to sign) | 01, 03 | Use an LMS attestation step after the SCORM package, or a final `poll` screen + LMS e-signature. | L&D | Open | |
| D15 | **Who the induction is for** — role catalogue and LMS learning paths | all | Assumed catalogue in `roles.json` / `personalisation-and-interactivity-plan.md` §1 (8 roles + managers, 3–4 groups per package). HR maps Oracle job families to these roles. | HR + L&D | Open — assumption applied to drafts | |
| D16 | **Extra unscored screens** from the personalisation layer (+26 per learner across the programme; Rev01 says ≈207) | all | Accept as a free value-add and log it in the proposal change log; scored content unchanged. | Course owner | Open | |
| D17 | **Optional motion-graphics videos** (9 planned clips, `media-video-plan.json`) | all | Start with the programme welcome and `qsr-060`; decide the rest after the pilot. Each is a value-add or a change request. | Course owner | Open | |
| D18 | **Gamification across all courses** (challenge, missions, XP, ranks) | all | Owner asked for it on 2026-10-20; built as an unscored layer (`gamification-plan.md`). Confirm the rank names and that XP is not reported to the LMS. | Course owner | Open — applied to drafts | |

## How to close a decision

1. The owner writes the decision and the source (policy number, poster, email) in the *Decision* column.
2. Change *Status* to `Closed (YYYY-MM-DD)`.
3. Update the affected modules' Phase 0 tables and any storyboard rows that depend on it.
