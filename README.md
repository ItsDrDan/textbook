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


> **Important (Nov 5, 2026): the live LibreTexts book is now ahead of `pages/`.** A polish pass was made directly on LibreTexts: outbound links fixed, Ball transclusions forked, leftover Ball Exercises/Summary pages deleted, 13.3+13.4 merged (Chapter 13 renumbered 13.3–13.12), Chapter 15 overlaps trimmed and retitled, Rosa openers and Career Spotlights added to every chapter page, Key Ideas turned into Chapter Summaries. `tools/sync-libretexts.js` now **skips** any page edited on LibreTexts after the cutoff in the script, so running it cannot undo that work. Before rebuilding with `build_pages.py`, pull the live HTML back into `drafts/`/`sections/` first, or treat LibreTexts as the source of truth for those pages.

> **Diagrams with text labels are images now (Nov 5, 2026, overnight pass).** LibreTexts' glossary script wraps glossary words in an HTML `<div>` even inside an inline SVG `<text>`, and browsers then drop the word ("D-Glucose" showed as "D-"). Every inline SVG that has text labels (about 290 figures on 83 pages) was uploaded as a file attached to its own page (`fig-p<pageid>-<n>.svg`) and replaced by an `<img>` with the SVG's aria-label as alt text. Rule for new figures: never paste an SVG with `<text>` into a page; upload it (or host it under `figures/`) and use `<img>`. The step and reaction close-ups in `figures/pathways/` come from `tools/glycolysis.js` and are linked from GitHub Pages.

## License
See `LICENSE.md`: content CC BY-NC-SA 4.0; source sections keep their own licenses (`pages/back_sources.html`).

## First-time setup
1. Create the GitHub repo **ItsDrDan/textbook** and push this folder to `main`.
2. Settings → Pages → Deploy from branch `main` / root. Wait for `https://itsdrdan.github.io/textbook/practice.html?t=alcohols` to load.
3. Sign in to chem.libretexts.org, open the book, open the browser console, paste `tools/sync-libretexts.js`, press Enter.

## Widget URL cheat sheet
```
practice.html?t=alcohols&n=10                      ten exam questions on alcohols
practice.html?t=metabolism&q=glycoly|pyruvate       regex filter on the question text
practice.html?ids=fb-3B-0019,fb-3B-0020             hand-picked questions
practice.html?t=structure,properties,hydrocarbons&n=12&fresh=1   cumulative mix: new random set each visit, spread evenly across topics
practice.html?rxn=hydration,hydrohalogenation&mode=product   reaction lab (modes: identify, product, reactant, name, mix)
&title=...&game=orgrxn|origins|carbs|peptides|finalboss|lewis|flash   header and "Play the full game" link
```
Reaction keys: combustion substitution hydrogenation halogenAdd hydrohalogenation hydration dehydration ox1Ald ox1Acid oxAldAcid ox2 reduction esterification esterHydrolysis saponification amidation amideHydrolysis amideBase hemiacetal acetal neutralAcid neutralAmine

## Updating the book (after the November 2026 COR enhancement)
- Source of truth for the Chapter Guides and Practice Problems: `drafts/` (copied from the authoring folder). Edit there, then `python3 tools/build_pages.py` to regenerate `pages/`.
- `sections/` holds the full section pages that replaced empty placeholders (4.10, 7.11, 11.7, 12.9, 13.7–13.10, 14.5, 15.6) and the front-matter "About This Book" page; `build_pages.py` copies them into `pages/` and numbers their figures.
- `sections/add_<pageId>.html` are the Lecture Connection blocks appended to the 125 sections taken from the source books. `sections/src_<pageId>.html` (111 files) hold the source text of every one of those sections that contains figures, copied in from the source book with the figure alt text rewritten for accessibility (November 2026; every one of the 875 inherited figures was re-described) and ending in an "Adapted from" note; `build_pages.py` uses `src_` when it exists and the transclusion widget from `tools/transclusions.json` otherwise. The alt-text work is recorded in `tools/alt_scan.json` (what was there), `tools/alt_new.json` and `tools/alt_map.json` (what replaced it) and `tools/source_issues.txt` (errors noticed in the source figures).
- Cumulative Review problems (Chapters 2–15) live in `tools/cumulative.py` (six written problems per chapter plus a `fresh=1` Try It mix of every topic covered so far); `build_pages.py` appends them to each Practice Problems page.
- Practice Games pages for Chapters 9, 11 and 13–15 embed the three CHEM 3B games built in November 2026: Lipid Lab (ItsDrDan/lipids), Enzyme Engine (ItsDrDan/enzymes) and Metabolic Marathon (ItsDrDan/metabolism). Their Exam Practice mode loads `js/fbx.js`, `css/widget-base.css` and `bank/<topic>.json` from this repo.
- Figure tools: `tools/draw.js` (structures, reaction schemes), `tools/pathway.js` (pathway/flow diagrams from a JSON spec), `tools/molsvg.py` (fused rings), `tools/preview.py` (render a page to PNG), `tools/check_fragment.py` (sanity checks).
- Push to LibreTexts: upload the new `pages/` folder to this repo, then paste `tools/sync-libretexts.js` into the browser console on chem.libretexts.org (it updates every page listed in `pages/manifest.json`, creating "Practice Games" and "About This Book" if missing).
- Authoring standards: `tools/AUTHOR_BRIEF.md`, `tools/REVIEW_BRIEF.md`, `tools/COR_outline.md`.
