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
- **Phone figures (batch W, PR #63, published 2026-11-13):** Figure 12.6.4 has a stacked copy (`figures/phone/`, built by `tools/phone_figs.py`) shown only below 600 px by a screen-only media query in a page `<style>` block; LibreTexts kept the markup. Checked three ways: desktop pane shows the wide figure only; iPhone 17 simulator shows the stacked figure only; single-page PDF of 12.6 prints the wide figure once (labels 6.0 pt and up). Pattern: add class `fig-wide` to the existing `<img>`, follow it with `<img class="fig-phone">`, same alt text on both. Also seen on the phone: the genetic code table collapses to one column (platform behaviour).
- **Phone figures, batch X (PR #65, published 2026-11-13):** eight more wide figures have stacked phone copies: 1.3 Lewis errors (597056), 6.3 acid dimer (597111), 8.7 polysaccharides (597140), 9.4 myelin (597147), 9.5 RBC tonicity (597148), 10.7 collagen (597160), 11.4 inhibitor rates (597169), 14.4 Fo rotor steps (597203). Each page was loaded at 1100 px and 375 px after publishing: wide figure only on desktop, stacked figure only on the phone width, same alt text on both. `tools/phone_figs.py` SPECS holds the crop rectangles; preview them in a real browser (PyMuPDF does not clip text). `python3 tools/phone_inventory.py` lists the figures whose labels are still small on a phone: mostly flow diagrams, reactions and pathway strips that cannot be stacked without a redraw. Open decision: side-scroll on phones, or redraw.
- **Phone side-scroll test (batch Y, published 2026-11-13):** 14.5 Figure 1 (yield flow, page 597204) is wrapped in `<div class="fig-scroll">` with a phone-only hint line. Below 600 px the image stays 860 px wide and the box scrolls sideways. Checked: desktop width unchanged and no hint; iPhone 17 simulator shows the hint, readable labels, and the figure scrolls; single-page PDF prints the full-width figure with no hint. Two lessons: LibreTexts lays `<figure>` out as a flex box, so the scroll box needs `width:100%; max-width:100%; min-width:0`; and the hidden hint needs `!important` because a platform rule for `<p>` outranks a plain class. Not yet rolled out to the other wide flow diagrams.
- **Phone side-scroll rollout (batch Z, published 2026-11-13):** 137 scroll boxes (158 images) on 66 pages, built by `tools/phone_scroll_build.py` from `tools/phone_scroll_metrics.json` (label size per figure). A figure gets a box when its usual label would be under 8 px on a 354 px screen; the phone width is chosen so that label is about 10 px, in 60 px steps. Adjacent slices of one figure share one box. One hint line per page. Three linked figures were left alone (inside `<a>`): ester_bp (6.6), fa_synthesis (15.6), nonessential_aa (15.11). First rule let an inner wrapper inside `<figure>` stretch to the image width on four pages; the corrected rule (`figure > * { min-width:0; max-width:100% }` plus a viewport cap on the box) was swapped into every page. Every page was loaded at 1100 px and 375 px after publishing. Known, not from this change: the long net equation on 13.5 is wider than a phone screen; the genetic code table on 12.6 collapses to one column.
- **Batch Z result:** all 66 pages read back identical to the corrected build; at 1100 px every page shows no hint and no changed figure width; at 375 px every page shows one hint, every box scrolls, no box is wider than the text column and no page gained sideways overflow. (The checker flags 597188 at desktop width because an inline wrapper around a block image measures as zero wide; the image itself is unchanged.) Not verified: PDFs of batch Z pages (the single-page compile queue was stalled on 2026-11-13; the same markup pattern printed correctly on 14.5), and the real simulator beyond 14.5. Check both on the next full compile: no "Swipe sideways" text in print, figures at full width.
- **Batch Z2 (published 2026-11-13, PR #69):** the 21:06 full compile printed the phone hint "Swipe sideways to see the whole figure." on 34 of the 66 batch Z pages (figures printed at full width; stacked phone figures did not print twice). Fix on all 66 pages: the hint carries inline `style="display:none"`, and the batch Z style block sits just before the first scroll box (or before its paragraph: LibreTexts closes a `<p>` that contains a `<style>`, which it did on 13.1 until republished). All 66 read back identical to `tools/batchZ2_build.py` output and were rechecked at 1100 and 375 px with no change from before. Next compile: "Swipe sideways" should appear 0 times.
- **Last small labels (PR #71, batch AA, published 2026-11-13):** circled phosphate P enlarged (font x1.19, circle x1.14; `tools/enlarge_circled_p.py`, same ratios now in `tools/glycolysis.js`) in glycolysis step 4, citric acid cycle step 5, urea cycle step 1 and the ATP synthase figure; CoQ 13 to 14 px in `etc_inner.svg`. Cache-busted on 13.5, 14.3, 14.4, 15.9; all four read back identical and the new figures are served. Next compile should show no label under 6 pt. Known and older than today: 14.4 and 13.1 scroll sideways slightly on phones (wide equations), 13.5 net equation too.
- **21:39 full compile (2026-11-13):** "Swipe sideways" prints 0 times; every stacked phone figure prints once; side-scroll figures print at full width; 107 footers all with an author. Only labels under 6 pt: the circled phosphate "P" on three pathway pages (about 5.4 pt) and "CoQ" in the 14.4 electron transport figure (5.85 pt). Cover author still "Unknown" until LibreTexts publishes the book.
- **22:12 full compile (2026-11-13):** no label under 6 pt anywhere (the circled P and CoQ fixes printed), "Swipe sideways" 0, every phone figure once, 107 footers with an author. Only "Unknown" on the cover remains (LibreTexts publication).
- **ADAPT on phones (2026-11-13):** works in Student View on the iPhone simulator; the 78 new questions now have a Show Hint button (see `adapt/README.md`).
- **AI statement (batch AB, PR #74, published 2026-11-13):** About This Book (597270) has a "Use of AI tools" section after "Sources and adaptation statement", wording approved by the author (names Claude; review sentence: "approved each set of AI-drafted changes before it was published, read a sample of each set closely, and corrected what was wrong"). LibreTexts renumbers `section_N` ids on save; nothing links to them. `pages/live/597270.html` matches live by hash. Keep the list in that section current if AI is used for new kinds of work.
- **Final phone walkthrough (2026-11-13, batch AC, published):** on the iPhone 17 simulator a Try It box (4.5) and a study game (Bond Voyage on 4.13) load, scroll inside their frames, take answers and show hints/feedback. Fixed and published: (1) the three linked figures (6.6 ester boiling points, 15.6 fatty acid synthesis, 15.11 nonessential amino acids; labels were about 5-6 px on phones) now side-scroll, links kept; (2) 13.1, 13.5 and 14.4 no longer slide sideways on phones: paragraphs holding MathJax scroll inside themselves below 600 px (`p:has(> mjx-container)`); (3) 12.6 genetic code table drops LibreTexts' `mt-responsive-table` (which collapsed it to one column and hid the base labels on phones) and keeps `width:100%`, so desktop is unchanged and phones show the full grid. All seven pages read back identical and were checked at 1100 and 375 px. Not scanned: other pages for wide equations (the equation rule is only on 13.1, 13.5, 14.4); other `mt-responsive-table` tables in the book.
- **Tables on phones (batch AD, published 2026-11-13, PR #77):** LibreTexts' `mt-responsive-table` hides every `<th>` below 600 px and stacks cells into one column; its `data-th` label strip renders empty, so every table lost its headers on phones. 108 pages (all with such tables except the Glossary, 488232) now carry one phone-only style block, placed just before the first table, that keeps each table as a grid with its header row and lets wide tables scroll sideways inside themselves. Desktop and print unchanged (pilot pages 6.1 and 2.2 measured identical at 1100 px before and after). Any new page with a table should get the same block (copy it from `tools/batchAD_build.py`).
- **Batch AD result:** all 108 pages read back identical; at 375 px no table on any page hides its header row; at 1100 px every page is unchanged. Pre-existing overflow found during the check, not caused by tables: wide equations on 12.1, 14.3 and 15.4 make those pages slide sideways on phones (same fix as batch AC would work); a benzene reaction diagram on 3.7 is wider than a phone; three long condensed formulas in a 1.7 table run slightly past the edge even at desktop width.
- **Batch AE (published 2026-11-13):** the last pages that slid sideways are fixed: 12.1, 14.3, 15.4 (wide equations, batch AC rule), 3.7 (benzene substitution diagram; phone rule `figure > * { min-width: 0; max-width: 100% }`), 1.7 (long condensed formulas widened a table even on desktop; the table now scrolls inside a `.tbl-scroll` box on screen, print untouched). All five read back identical; at 375 and 1100 px the page is exactly the screen width. Only scanned pages that have tables or were flagged; a book-wide overflow scan of every page was not run.
- **Book-wide phone sweep (2026-11-14):** all 199 live pages loaded at 375 px in the signed-in browser and checked for any element wider than the screen that is not inside a scroll box. Only 10.8 (597161, disulfide-formation equation) still slid sideways; fixed in batch AF and rechecked at 375 and 1100 px. After this, no page in the book is wider than a phone screen. Method: load each page in a 375 px iframe, wait 2.5 s, compare `documentElement.scrollWidth` with the viewport and list unclipped elements past the right edge (script in this session; images that load lazily after 2.5 s are not measured).
- **Batch AG (approved and published 2026-11-14, PR #80):** the last repeated text (14.2, 15.5, 15.6, about 300 words cut, with disagreements fixed: Kussmaul breathing in 15.5; one acetyl-CoA export route and the ACC-phosphorylation tip in 15.6; Stage III numbering in 14.2) and the two remaining low-confidence wording items (14.3 NADH rule, 10.5 tannic acid). All five pages read back identical and fit the screen at 375 and 1100 px. The "Duplicate telling" and "Low-confidence wording" items under "Work not done" are closed.

## Final publication gate (2026-11-14, branch `audit/2026-11-final-gate`, local, uncommitted)

- Verdict: lecture textbook READY WITH NAMED NONBLOCKING ITEMS. Reports: `FINAL_PUBLICATION_QA.md`, `RELEASE_BLOCKERS_AND_FIXES.md`, `LAB_MANUAL_INTEGRATION_BACKLOG.md`, `FINAL_RELEASE_CHECKLIST.md`.
- Live = `pages/live` (199/199 by hash) = Full-3.pdf text. ~2,000 items re-solved by five independent reviewers: 0 wrong keys.
- Batch AH drafted (13 edits, 12 pages, NOT published): lab-manual wording (1.5, For Instructors, About), problem-count claim, 7 small science/alt-text fixes, and Part C: citrate synthase switched to transferase everywhere (author decision 2026-11-14; bank fb-3B-2030 and ADAPT CSV updated locally; live ADAPT item, QTI zip and his Ch 14 slides still say ligase).
- Open: cover "Unknown" needs a LibreTexts author record for `dkwasniewski` (root page already has author@ tag); 13.5 footer printed blank in Full-3 (tags fine; recompile). The "Recheck three Valley figures" item above was closed on 11-13.

## Published 2026-11-14 (batch AH)

Batch AH (21 edits, 15 pages) is live; every page read back identical to `tools/batchAH_sha_2026-11-14.json` and `pages/live` is synced. Bank fb-3B-2030 now keys transferase (goes live with the PR merge).

## Check after publishing (do these when reviewing the published book)

1. **Previous/Next arrows (real problem, item N1 in `RELEASE_BLOCKERS_AND_FIXES.md`).** On 2026-11-14, signed-out Safari on the iPhone 17 simulator showed "◀ Previous" with no title and "Next ▶ CHEM V101 Textbook Ventura College" on every page tried (6.7, 14.7); tapping Next opened Ventura College's Workbench book. Signed in on desktop, the same page correctly links 6.6 / 6.8. Analyze: (a) open several pages signed out on desktop and on a phone (private window), note where the arrows go; (b) recheck after the book moves from Workbench to the Bookshelf; (c) if still wrong, report to LibreTexts with page ids and screenshots. No page edit can fix it (LibreTexts builds the arrows).
2. Full PDF compile: cover author (needs LibreTexts author record for `dkwasniewski`), 13.5 footer (p. ~1098 printed "curated by ."), batch AH text present, "Swipe sideways" = 0, labels ≥ 6 pt.
3. Done 2026-11-14: the Try It shows fb-3B-2030 with transferase as the key, and live ADAPT question 355222 keys transferase (read back).
4. Instructor's Ch 14 slides and any exam key: citrate synthase = transferase.

- 2026-11-14 12:20 compile: all batch AH text printed; cover still "Unknown"; footers of 6.10 and 9.3 printed blank (13.5 fixed). The tag `author@Muhammad Arif Malik` was then added to the 19 Malik pages that lacked it (`tools/author_tags_malik_2026-11-14.json`). Next compile: check that no footer prints "curated by .".
- 2026-11-14: `author@Daniel Kwasniewski` added to all 115 adapted pages (`tools/author_tags_adapted_2026-11-14.json`); footers now credit him (Ball pages had printed "curated by via source content" with no name). Share of own writing per page: `audit/AUTHORSHIP_SHARE_2026-11-14.md`. Open: whether majority-own pages get a visible "written by" line.
