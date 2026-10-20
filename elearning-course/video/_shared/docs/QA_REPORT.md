# QA report — <clip-id>

> Numbers only from the commands, pasted, never typed from memory.

| Check | Command | Result | Pass? |
|---|---|---|---|
| cues resolved | `resolve_cues.py` | n cues | |
| delivery checks (format, size, loudness, true peak, flashes, VTT) | `delivery_check.py renders/<clip-id>.mp4 --vtt data/<clip-id>.vtt --json data/qa_delivery.json` | paste all lines | |
| sync / black / freeze / caption agreement | `qa_check.py renders/<clip-id>.mp4` (kit) | | |
| motion (advisory) | `motion_check.py … --profile explainer` | | — |
| looked at contact.jpg, phone.jpg, strips | `review_sheets.py` | | |
| captions = narration word for word | diff of VTT text vs `script.md` | | |
| facts on screen ⊆ `facts.md` | by eye, every scene | | |

## Not checked (say what and why)
- 
