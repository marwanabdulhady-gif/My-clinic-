# Local review fonts

Unmodified Google Fonts binaries, retrieved **2026-10-14** from the public
[`google/fonts`](https://github.com/google/fonts) repository at commit
`6159c1997ff813fb7d14a4cebeb2ebfedd7b6dc9`.

- **Montserrat-Variable.ttf** — upright variable font; the review renderer uses weights 400–700.
- **Tajawal-Regular.ttf / Tajawal-Medium.ttf / Tajawal-Bold.ttf** — Arabic 400 / 500 / 700.
- **Montserrat-OFL.txt / Tajawal-OFL.txt** — the corresponding SIL Open Font License 1.1 texts.
- **provenance.json** — upstream paths, Git blob hashes, byte sizes and SHA256 checksums.

`tools/generate_screens.py` verifies the checksums, then copies fonts, licences and
provenance into the standalone preview. CSS uses relative `@font-face` URLs: no Google
Fonts/CDN request, installed system font or connection is required to review it.
Tajawal is the `:lang(ar)` family and the Arabic-glyph fallback in the HTML font stack.
The browser gate explicitly loads both families. Existing SVG assets remain supplied
images; their text is also repeated in readable HTML on display-diagram screens.

This does **not** close Marketing D11 or approve an Arabic translation/RTL release.
The current slides are English. Do not change the binaries without updating provenance
and retaining their licence texts.
