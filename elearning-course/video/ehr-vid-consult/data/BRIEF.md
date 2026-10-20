# BRIEF — ehr-vid-consult

| Field | Value |
|---|---|
| clip id | `ehr-vid-consult` |
| module | 08 |
| placement | new unscored video screen after ehr-001 |
| route | narrated-explainer with one voice interaction |
| destination | lms (SCORM 1.2, Oracle Learning), unscored screen |
| aspect / fps | 1920x1080 master, 30 fps → 1280x720 SCORM encode |
| target length | 45 s of narration (the interaction pause is extra) |
| voice | Dr. Omar only (male), see video/PRODUCTION-PLAN.md §2 |
| captions | WebVTT with `<v Dr. Omar>` tags |
| music / sfx | off unless the owner says on |
| brand | video/_shared/brand/README.md, module colour `#006E78` |

## Message
Complete, specific, linked, on the day.

## Audience
Physicians in module 08.

## Action
Follow the consultation order in the EHR.

## Proof
none

## Stated vs inferred
- **Stated:** see data/facts.md (every line has a source).
- **Inferred (needs OK):** nothing

## Owner OK (Gate A)
- [ ] approved by ______ on ____-__-__
