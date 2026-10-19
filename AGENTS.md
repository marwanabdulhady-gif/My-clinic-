# Instructions for every agent in this repository (same as CLAUDE.md)

Before you change anything, read **[`elearning-course/AGENT-TASKS.md`](elearning-course/AGENT-TASKS.md)** from top to bottom. It has the 12 rules, the set-up commands, the checks you must run before every commit, and the task list in priority order.

The short version:

1. Take the first task in AGENT-TASKS.md §4 that is not done and not blocked. Do one task, for one module, on one branch.
2. Never change anything scored. That means screen ids, types, order, points or objectives. New interactivity goes only in `<module>/production/personalisation.json`.
3. Never invent policy facts. Use the storyboard or `scorm-plans/00_program/kickoff-assumed-answers.md`, and keep the `⚠ Draft — pending` marker.
4. Never run `tools/assemble_storyboard_docs.py`. Never edit generated files by hand.
5. Run every check in AGENT-TASKS.md §3, look at your screens in `preview.html`, then open a pull request. Never merge it yourself.
6. End with the report described in AGENT-TASKS.md §5.

If something is unclear or a step fails, stop and report it. Do not guess.
