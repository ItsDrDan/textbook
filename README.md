# CHEM 3B textbook assets (ItsDrDan/textbook)

Interactive pieces for **Introductory Organic and Biological Chemistry for FCC** on LibreTexts.
Everything here is served from GitHub Pages at `https://itsdrdan.github.io/textbook/` and embedded in the book.

| Folder | What it is |
|---|---|
| `practice.html` | The **Try It** widget that the book embeds (iframe). Two engines: exam-bank questions and a reaction lab. See the comment at the top of `js/widget.js` for the URL options. |
| `js/engine.js` | Structure drawing, compound library, reaction templates and name checking, extracted from Bond Voyage! (`ItsDrDan/organicreactions`). Edit there first, then copy here. |
| `js/fbx.js` | The Exam Practice module shared by the games (Final Boss question renderer). |
| `bank/*.json` | The Final Boss CHEM 3B question bank, split by topic (985 questions). Ids are `fb-3B-NNNN` (index in the Final Boss bank). |
| `figures/` | The 41 structure figures exported from the lecture slides, referenced by the Chapter Guides. |
| `pages/` | Built HTML for the LibreTexts pages (15 Chapter Guides + 15 Practice Games pages) and `manifest.json`. |
| `tools/build_pages.py` | Rebuilds `pages/` from the Chapter Guide drafts (edit the `PLAN` dict to move or change widgets). |
| `tools/scheme.js` | Draws the inline-SVG reaction schemes used in the guides (`node tools/scheme.js`). |
| `tools/sync-libretexts.js` | Paste into the browser console on chem.libretexts.org to push `pages/` into the book. |

## First-time setup
1. Create the GitHub repo **ItsDrDan/textbook** and push this folder to `main`.
2. Settings → Pages → Deploy from branch `main` / root. Wait for `https://itsdrdan.github.io/textbook/practice.html?t=alcohols` to load.
3. Sign in to chem.libretexts.org, open the book, open the browser console, paste `tools/sync-libretexts.js`, press Enter.

## Widget URL cheat sheet
```
practice.html?t=alcohols&n=10                      ten exam questions on alcohols
practice.html?t=metabolism&q=glycoly|pyruvate       regex filter on the question text
practice.html?ids=fb-3B-0019,fb-3B-0020             hand-picked questions
practice.html?rxn=hydration,hydrohalogenation&mode=product   reaction lab (modes: identify, product, reactant, name, mix)
&title=...&game=orgrxn|origins|carbs|peptides|finalboss|lewis|flash   header and "Play the full game" link
```
Reaction keys: combustion substitution hydrogenation halogenAdd hydrohalogenation hydration dehydration ox1Ald ox1Acid oxAldAcid ox2 reduction esterification esterHydrolysis saponification amidation amideHydrolysis amideBase hemiacetal acetal neutralAcid neutralAmine

## Updating the book (after the November 2026 COR enhancement)
- Source of truth for the Chapter Guides and Practice Problems: `drafts/` (copied from the authoring folder). Edit there, then `python3 tools/build_pages.py` to regenerate `pages/`.
- `sections/` holds the full section pages that replaced empty placeholders (4.10, 7.11, 11.7, 12.9, 13.7–13.10, 14.5, 15.6) and the front-matter "About This Book" page; `build_pages.py` copies them into `pages/` and numbers their figures.
- Figure tools: `tools/draw.js` (structures, reaction schemes), `tools/pathway.js` (pathway/flow diagrams from a JSON spec), `tools/molsvg.py` (fused rings), `tools/preview.py` (render a page to PNG), `tools/check_fragment.py` (sanity checks).
- Push to LibreTexts: upload the new `pages/` folder to this repo, then paste `tools/sync-libretexts.js` into the browser console on chem.libretexts.org (it updates every page listed in `pages/manifest.json`, creating "Practice Games" and "About This Book" if missing).
- Authoring standards: `tools/AUTHOR_BRIEF.md`, `tools/REVIEW_BRIEF.md`, `tools/COR_outline.md`.
