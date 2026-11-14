# Next-session checkpoint (written 2026-11-13, end of the master refinement pass)

## State

- Repo `textbook-git`: the pass was merged to `main` as PR #50 (79005d9) on 2026-11-13; the `js/fbx.js` label fix is live on GitHub Pages. Item 4 below is done. Final Boss has the same code as v41 (commit a8033ea in `github/finalexam`).
- Live LibreTexts book: **batch Q published 2026-11-13** (310 edits, 117 pages, all read back identical), plus the Index page pointers and 13 page tags. `pages/live` matches it. Items 2 and 3 below are done.
- Latest PDF checked: `~/Downloads/Full.pdf`, 2026-11-13 16:37, 1,340 pp.
- Coverage: every page has a ledger row, a pedagogy score and script checks. Correctness of problems rests on the 11-11 and 11-13 re-solves, not on this pass.

## Update, end of 2026-11-13

Batch R (`audit/BATCH_R_REVIEW.md`, branch `content/2026-11-batchR`) drafts most of the "Work not done" list below: Rosa story edits, bank gaps, section exercises, Check steps, Valley questions, cumulative-mix caps, the low-confidence errata and the P3 page fixes. See the 2026-11-13 batch R entry in `tools/ISSUE_LEDGER.md` for what is and is not in it. **Merged (PR #53) and published on 2026-11-13; all 54 pages read back identical.** Still to do from it: confirm in the next PDF compile; add the 18 new questions (fb-3B-2238 to 2255) to Final Boss and ADAPT; thin-topic questions; the duplicated inherited prose (author decision).

## Update, batch T (2026-11-13, merged as PR #57 and published)

Small-print figures (41 files), 60 thin-topic questions, ADAPT export, prose trims and Try It selections are live; see the batch T entries in `tools/ISSUE_LEDGER.md`. Open after it: confirm label sizes in the next full PDF; create the 78 new questions in live ADAPT (files ready in `adapt/`); push or merge the Final Boss branch `textbook-new-3B-2026-11-13`; update the figure generators to the new label sizes; cover author at LibreTexts.

## Waiting on the instructor (in order)

1. **Rosa story edits.** The Part 15 emergency-department check (P0) was approved on 2026-11-13 and is in batch Q. Seven smaller story edits are still held (Part 12 timeline "six months later" and insulin wording, Part 9 LDL follow-up, Part 10 repeat test, Part 13 meals, 14.5 burrito example ×2). Once decided, clear `skip` on those rows in `audit/edits/rosa_valley.json` (or edit the `new` text) and rerun `python3 tools/batchQ_build.py`.
2. **Publish batch Q** (310 edits, 117 pages). Read `audit/BATCH_Q_REVIEW.md` first; the 24 new exercise answers and the 29 Glossary edits deserve a look. Method as for batches M–P: push the branch, have the signed-in LibreTexts tab fetch `tools/batchQ_2026-11-13.json` from raw.githubusercontent.com at that commit, dry-run against live (compare the `before` hashes in `tools/batchQ_sha_2026-11-13.json`), save, read back, sync `pages/live`.
3. **With the Glossary pointer edits (13 terms):** change the same pointers on the Index page (488231) and move the page tags (GET then PUT `/@api/deki/pages/{id}/tags`), or the printed Index will disagree. Terms: alkane, hydrocarbon, digestion, Cori cycle, molecular formula, condensed structural formula, substitution reaction, mitochondrial matrix, anticodon, DNA, ATP synthase, coenzyme Q, cytochrome.
4. **Merge the branch to `main`** so the widget label fix goes live on GitHub Pages; copy the new `molDesc` / `molWalk` / `optLabels` code into `finalexam`.
5. **(Done 2026-11-13: `author@Daniel Kwasniewski` added to all 78; see `tools/author_tags_2026-11-13.json`.)** ~~Author tag on the 78 own pages~~ so footers print "curated by Daniel Kwasniewski" instead of "curated by ." Test on one page and compile it before doing the rest.
6. **Cover author "Unknown":** LibreTexts book record.
7. **Report the glossary pop-up ARIA failure to LibreTexts** (details in `WEB-PDF-ACCESSIBILITY-QA.md`, A2), and decide on one sentence in the accessibility statement.

## First checks after publishing

- Done: 597094 (4.5) and 597091 (4.2) compiled alone; the new text and keys print.
- Open three changed Try It boxes in the book (4.8, 13.4, 3.1) and answer a question in each.
- Next full PDF: version line on p. 15; 24 answers in print; rerun `tools/audit_inventory.py` with the new PDF.

## Work not done, by priority

**P1**
- Write questions for the bank gaps: Lewis structures (2 exist; the 1.3 widget is unchanged for that reason), alkene naming (1), ketone bodies (5); then the thin topics listed in `GAMES-AND-TRYIT-VALIDATION.md`.
- A chemistry colleague reads the 24 new answers (figures were not viewed; answers rest on alt text).
- Recheck three Valley figures: 11.4 cholinesterase thresholds (3 CCR 6728 amended 2025), 9.2 "Fresno 20% of the crop", 4.5 "40%".

**P2**
- One exercise for each section that has none: 6.6, 8.3, 9.4, 10.7, 10.9, 11.1, 11.3, 11.5, 11.6, 12.1, 12.4, 12.7, 13.2, 15.6, 15.11.
- A Check step for Chapter Guide examples 1.9 (2–4), 2.10 (1–4), 3.9 (1, 3–5).
- "Think about it" questions for the ten Valley boxes without one.
- Cumulative-review mixes draw from later chapters (needs per-item chapter tags in `bank/`).
- Duplicate telling in 14.2, 14.4, 15.4, 15.5, 15.6: needs the author's decision on cutting inherited prose.
- Low-confidence wording items in the errata file ("not drafted" list).

**P3**
- 3.2 heading skip; unencoded spaces in the 1.8 widget URL; Final Boss tab title with `?course=3B`; widget titles at 6.1 and 12.2; Chapter 1 and 7.4 inherited answers shown in the open; print the Study Hub address on Practice Games pages; widget colour contrast by hand; fifteen footer-only PDF pages (export-level).

## Not tested at all in this pass

Screen reader session; zoom reflow; phone and Chromebook hardware; caption accuracy; playing games through; ADAPT settings; PDF/UA conformance; every PDF hyperlink.

## How to rerun the tooling

```
python3 tools/audit_inventory.py <pdf_slim.json> > audit/inventory.json   # pdf_slim.json = {toc, pages:[{p,label,words}]} from PyMuPDF
python3 tools/question_ledger.py
python3 tools/batchQ_build.py
python3 tools/coverage_ledger.py
node tools/check_struct_labels.js
```

## Known risks

- The pedagogy scores and several findings come from delegated readers; a sample of their edits was checked against the page text and the chemistry, not every one.
- The widget alignment classified questions from stems and correct answers; distractors and images were not read.
- Changed Try It boxes start students' saved progress over.
- Batch Q assumes the live pages still equal `pages/live`; the publish dry-run must confirm that.

## Update 2026-11-13 (batch U and ADAPT)

- ADAPT: the 78 new questions (fb-3B-2238 to 2315) are live in course 4605 and read back identical to the bank. See `adapt/README.md`.
- Figure generators hold the enlarged label sizes (`concept_maps.py`, `oer_figs.js` sphingolipids, `glycolysis.js`). Run `python3 tools/check_figure_labels.py` after regenerating any figure; it fails if a label drops below its recorded print size (`tools/figure_label_floors.json`). `oer_figs.js` has drifted from nine of its live figures, so regenerate only the figure you mean to change.
- Batch U (`tools/batchU_build.py`): 14.4 cyanide told once, 15.4 stage numbering and the inherited "Unsaturated fatty acids" box, cache-busts for regenerated figures. `fig-p597204-yield-flow.svg` must be re-uploaded to LibreTexts file 512775 (owner page 597204).
- **Published 2026-11-13:** batch U is live (18 pages, each read back identical; PR #59 merged), `pages/live` synced, and the yield-flow figure is re-uploaded (file 512775, revision 3). Next: the full PDF compile, then confirm label sizes in print.
- **Published 2026-11-13 (batch V, PR #61):** the 19:32 compile showed every word label at 6 pt or more; the short labels still under 6 pt were raised in the 12.5 tRNA figure (file 512603, revision 3), the 12.6 elongation figure (file 512767, revision 4) and the 14.4 rotor figure (cache-bust on 597203, read back identical). Page 597202 (14.3) gained the tag `author@Muhammad Arif Malik` after its footer printed with no author. Next compile: confirm these four.
- **Phone side-scroll test (batch Y, published 2026-11-13):** 14.5 Figure 1 (yield flow, page 597204) is wrapped in `<div class="fig-scroll">` with a phone-only hint line. Below 600 px the image stays 860 px wide and the box scrolls sideways. Checked: desktop width unchanged and no hint; iPhone 17 simulator shows the hint, readable labels, and the figure scrolls; single-page PDF prints the full-width figure with no hint. Two lessons: LibreTexts lays `<figure>` out as a flex box, so the scroll box needs `width:100%; max-width:100%; min-width:0`; and the hidden hint needs `!important` because a platform rule for `<p>` outranks a plain class. Not yet rolled out to the other wide flow diagrams.
