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
