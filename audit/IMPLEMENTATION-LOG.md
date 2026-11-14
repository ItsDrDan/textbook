# Implementation log (master refinement pass, 2026-11-13)

Branch: `audit/2026-11-master-refinement` (pushed; no PR; not merged, so nothing is deployed to GitHub Pages).

**Batch Q was published on LibreTexts on 2026-11-13 on the instructor's "Publish batch Q".** Dry run first: all 117 live pages matched their expected `before` hash and every edit matched its count. Pilot save on 597270, then the other 116. **All 117 pages read back identical to the planned text.** Then the Index page (488231): 13 pointers changed to follow the Glossary (read back identical), and the 13 matching page tags moved on 18 pages (`tools/index_tag_moves_batchQ_2026-11-13.json`; each tag list read back as planned). `pages/live` is synced (hash-checked).

Single-page compiles after publishing: **4.5 (597094)** prints the oxidation definition, the completed Summary, the outline bridge and Exercise 4.5.1 in the key; **4.2 (597091)** prints both exercise parts inside the box and the new "Answers to Exercises" key. In both, the new answers also print beside their exercise, as every existing inline answer in the book does (2.5 on p. 165 and the 4.5 Valley answer on p. 325 of the 16:37 export do the same).

## Files changed

| File | Change | Live? |
|---|---|---|
| `js/fbx.js` | `molDesc` rewritten; new `molWalk`, `optLabels`; `optLabel` uses per-question labels; stem drawings carry a real description instead of "skeletal structure" / "Lewis structure". +91 / −9 lines. | No. Live when this branch is merged to `main` (GitHub Pages). Carry the same code to `finalexam` (the README's "edit there first" rule). |
| `tools/check_struct_labels.js` | New regression check for the above. | n/a |
| `tools/audit_inventory.py` → `audit/inventory.json` | Inventory of all 199 pages: components, embeds, headings, objectives, PDF page ranges. | n/a |
| `tools/question_ledger.py` → `audit/QUESTION-LEDGER.csv` | 1,812 examples and exercises, one row each. | n/a |
| `tools/coverage_ledger.py` → `audit/TEXTBOOK-COVERAGE-LEDGER.md` | One row per page. | n/a |
| `tools/batchQ_build.py` → `tools/batchQ_2026-11-13.json`, `tools/batchQ_sha_2026-11-13.json` | **Draft** page edits: 310 edits on 117 pages, 0 uploads. | **Yes, published 2026-11-13.** |
| `audit/edits/*.json` | The reviewers' edit lists that feed batch Q (pedagogy ×3, glossary, Rosa/Valley with 7 held, widgets). | n/a |
| `audit/reviews/*.md` | The reviewers' full reports. | n/a |
| `audit/*.md` | The nine deliverables of the brief, plus `BATCH_Q_REVIEW.md` (readable list of every draft edit). | n/a |
| `.gitignore` | `audit/preview/` (the edited-page previews the build writes). | n/a |
| `Study Games/.claude/launch.json` (outside the repo) | Added a `textbook-widget` preview entry serving a scratch copy of the widget. | n/a |

## Batch Q contents

| Part | Edits | Pages | What |
|---|---|---|---|
| A | 1 | 1 | "This is version 1.1" → 1.2 |
| B | 38 | 12 | Answers for 24 inherited exercises (inline and print key); two stray list items on 4.2 moved back into their boxes |
| C | 2 | 1 | Exemplar 4.5: oxidation defined at first use; Summary completed (the other two 4.5 edits are counted in B and D) |
| D | 67 | 63 | Pedagogy edits (7 P1, 47 P2, 13 P3) |
| E | 29 | 1 | Glossary: 11 Spanish equivalents, 5 definitions, 13 section pointers |
| F (Rosa/Valley) | 29 | 25 | Fictional-patient line on Parts 2–15; HDL cut-off; garlic county claim; two dead links; 7.11 source links; small fixes |
| F (Try It) | 144 | 60 | 73 widgets: new question selection (iframe `src` and its "open in a new tab" link) |
| **Total** | **310** | **117** | |

Held out of the batch: 7 Rosa story edits (see `ROSA-AND-VALLEY-CONTINUITY.md`). The two Part 15 edits (P0) were approved by the instructor on 2026-11-13 ("Use proposed ER check") and are in the batch.

## Tests run

| Test | Command or method | Result |
|---|---|---|
| Batch Q strings | `python3 tools/batchQ_build.py` (asserts every `old` occurs the stated number of times) | pass; 0 skipped |
| Batch Q markup | open/close tag counts for 15 tags, before vs after, all 117 pages | no change in balance on any page |
| Widget URLs in batch Q | each new URL re-simulated against `bank/` with the widget's filter rule | 73 of 73: ids exist, pool equals the listed pool, `n` ≤ pool; 4.8 loaded live |
| Structure labels | `node tools/check_struct_labels.js` | 1,065 drawings; 171 structure-choice questions; 0 duplicates; 0 bad labels (before the change: 114 duplicates) |
| Widget in a browser (patched) | local preview, questions fb-3B-0507 / 0596 / 0797 / 0919 | labels match the drawings; no console errors |
| axe-core on the widget | WCAG 2.0–2.2 A/AA tags, before and after answering | 0 violations |
| axe-core on live 4.5 | `#pageText` | 1 platform-injected rule failure (glossary pop-ups), 0 from page content |
| Internal links | all pages | 1,089 links, 0 wrong numbers |
| Page structure | all pages | 0 images without alt (34 intentional empty alts), 0 untitled iframes, 0 tables without headers, 1 heading skip |
| Answer-key parity | all pages | 108 keyed pages consistent; 24 unanswered exercises found |
| External widget/game URLs | curl ×243 | 241 OK; 2 false alarms (unencoded spaces) |
| 16 games + reaction lab load | 420 px frames | all load, no script errors |
| PDF text and tags | PyMuPDF on the 16:37 export | see `WEB-PDF-ACCESSIBILITY-QA.md` |
| Earlier corrections still present | PDF text search | transcription direction, tyrosine, ATP numbers, ten essential amino acids, first-aid advice: all present |
| Scope scan | keyword scan of all pages | no pKa, R/S, E/Z, meso, Newman, chair-flip, Km or hybridization content outside the disclaimers |

Not run: the next full-book PDF (needs a new compile), a screen-reader session, phone hardware.
