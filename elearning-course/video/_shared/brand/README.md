# Brand for videos

Everything here comes from [`scorm-plans/00_program/brand/brand-identity.md`](../../../scorm-plans/00_program/brand/brand-identity.md), which is still a draft under decision D11. If you are not sure, that file wins. Never invent a colour, font or logo treatment.

## Colours: `tokens.css`
- About **60 %** white or off-white, **30 %** navy, and **10 %** for one module colour plus magenta accents.
- **One module colour per clip.** The table is in `tokens.css`. Programme clips (`prog-…`) use navy only.
- **Magenta (`responsible`)** is the accent for key warnings, key numbers and the callout bar, with at most one callout per scene. It is not decoration. In module 04, magenta is also the module colour, so a warning there must come from the layout (callout bar, ⚠ icon and words).
- Green and red are feedback colours, not brand colours. Use them only for "Correct" and "Not quite", always with an icon and words.
- **Never use colour alone** to carry meaning.
- No gradients except the navy title gradient. No neon, no pure black, no heavy shadows.
- White text on teal must be ≥ 38 px bold at 1080p. Small teal text uses `ambitious-dark`.

## Type
- Montserrat only. Copy `montserrat-latin-{400,600,700}-normal.woff2` and `Montserrat-OFL.txt` from `scorm-plans/00_program/brand/fonts/` into the clip's `public/fonts/`. Never load it from a CDN at render time.
- The sizes in `tokens.css` are the course sizes doubled, because videos are mastered at 1920 × 1080. Body text is never below 28 px.
- Use sentence case for titles ("The fire triangle") and digits for numbers.

## Logo (`scorm-plans/00_program/brand/assets/`)
- Use only the supplied PNGs. Never redraw it, retype it or ask a model to generate it.
- `logo-horizontal-white.png` goes on navy (the opening and closing scenes). `logo-horizontal-navy.png` goes on white or light backgrounds. Never put the logo on teal, purple, magenta, burgundy, a photo or a busy illustration.
- Show the logo only on the first and last scenes, top-left (96 px from the left and 80 px from the top at 1080p). Keep clear space of one petal height around it. One logo per frame.
- The petal watermark (`mark-white.png` at 8–10 % on navy, `mark-navy.png` at 6–8 % on light) may sit large and cropped off the right edge, behind the content.

## Graphic elements
Cards are white with a 1 px `line` border and 24 px radius at 1080p. Chips and buttons are pill-shaped. Icons are single-weight line icons, white on colour tiles and navy or module colour on white. These match §4–5 of the brand file, so the clips look like the courses.

## Characters
Copy the PNG poses you need, **unmodified**, from `scorm-plans/00_program/characters/assets/` into the clip's `public/characters/`. Never generate, redraw or recolour Noor or Dr. Omar. Noor's accent colour is `caring` purple.
