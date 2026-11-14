# Release blockers and fixes: final publication gate (2026-11-14)

Reference export: `~/Downloads/Full-3.pdf`, 1,359 pages, Prince 16.2, written 2026-11-14 10:50. Source: live LibreTexts. On 2026-11-14 all 199 live pages were fetched through the deki API and hashed, and every one matched `pages/live/` (no drift). Every section paragraph of 12+ words in `pages/live/` was found in the PDF text (the 3 misses were tokenizer artifacts), so the PDF is current with the live book, including batch AG.

**Release blockers (P0) found: none.**

Update 2026-11-14: the author chose to switch citrate synthase to transferase (row C1–C8).

Nothing below has been published. Fixes are drafted in batch AH (`tools/batchAH_build.py`, review sheet `audit/BATCH_AH_REVIEW.md`, branch `audit/2026-11-final-gate`, local only).

## P1

| ID | Location | Issue (before) | Proposed fix (after) | Evidence | Status | Remaining risk |
|---|---|---|---|---|---|---|
| C1–C8 | 11.1 (597166) table and "Two traps"; 11.8 (597173) Key Idea 2 and Common Mistakes; 14.3 (597202) step table; 14.6 (597205) Key Idea; Glossary (488232) "ligase" and "transferase" | The book said citrate synthase "is classified as a ligase". IUBMB class is **transferase** (EC 2.3.3.1; a lyase, EC 4.1.3.7, before 2002), never a ligase, and the book's own rule is that a ligase spends ATP. | **Author decided 2026-11-14: switch to transferase everywhere.** Eight edits in batch AH Part C; bank item fb-3B-2030 rewritten (key transferase, distractors ligase/hydrolase/oxidoreductase, new per-choice feedback); ADAPT question list CSV row updated. Metabolic Marathon and the Study Hub question bank already keyed transferase; Final Boss has no such item. | Lecture slides (Ch 14, "Citrate synthase is a Ligase"); `bank/metabolism.json`; game sources | Drafted locally, not published | Live ADAPT question fb-3B-2030 still keys ligase until updated; the ADAPT QTI zips still hold the old item; the instructor's Ch 14 slides need the same change. Publish the bank change and batch AH together so the Try It and the page agree. |
| F2 | For Instructors (597396) | "experiment numbers and links will be added when the manual is published", while 13 In the Lab boxes already print experiment numbers. Internal contradiction in an instructor-facing claim. | "where a box already gives an experiment number, that number is provisional; numbers and links will be checked and added when the manual is published." | grep of all 199 pages (list in `LAB_MANUAL_INTEGRATION_BACKLOG.md`) | Drafted | None; numbers unchanged. |
| F1 | 1.5 (597058) In the Lab | "The lab manual appendix has a VSEPR chart ... and an electronegativity chart" promises a resource students cannot open. | Points to the VSEPR table on the same page and Figure 1.4.3 (both verified to exist; the table precedes the box). | `pages/live/597058.html`, `597057.html` | Drafted | None. |

## P2 (low-risk, unambiguous)

| ID | Location | Before | After | Evidence | Status |
|---|---|---|---|---|---|
| B1 | 4.2 (597091) Figure alt text | Thymol's CH3 "two carbons further around the ring" (reads as C4, i.e. the wrong isomer for a screen-reader user) | "on the ring carbon directly across from the isopropyl group (2-isopropyl-5-methylphenol)" | Thymol = 2-isopropyl-5-methylphenol; the figure label is correct | Drafted |
| B2 | 9.2 (597145) | Olestra "all eight OH groups esterified" | "six to eight of its eight" | 21 CFR 172.867 (hexa- to octaesters) | Drafted |
| B3 | 8.7 (597140) Dental box | Amylase gives "maltose and glucose" | "maltose and other small sugars" | α-amylase products: maltose, maltotriose, dextrins | Drafted |
| B4 | 3.9 (597086) summary | "Nothing in this chapter dissolves in water." | "None of this chapter's hydrocarbons dissolves in water." | 3.8 includes phenol (~8 g/100 mL) | Drafted |
| B5 | 1.10 (597063) Problem 1.71(c), inline and print key | Open chain "would need an O–H to be a real molecule" | "...an O–H and an extra H on the end carbon (C4H10O, not C4H8O)" | H count | Drafted |
| B6 | 15.8 (597208) | After transamination the amino acid "contains only C, H, and O" | "has lost its α-amino group and is now an α-keto acid" | False for Lys, Arg, His, Trp, Asn, Gln, Cys, Met | Drafted |
| B7 | 15.11 (597217) table | Phenylalanine hydroxylase "uses O2 and NADPH" | "uses O2" (matches the section text) | Cofactor is tetrahydrobiopterin | Drafted |
| F3 | About This Book (597270) | "together with the free lab manual" (ZTC sentence) | "a free lab manual" | Manual in preparation | Drafted |
| F4 | For Instructors (597396) | "60–80 original problems per chapter" | "67–83" | Counted per chapter on 2026-11-14 | Drafted |
| N1 | Every page, top and bottom page-navigation bar, **signed-out readers** (seen on iPhone 17 simulator, Safari, 2026-11-14) | "◀ Previous" shows no title and "Next ▶" reads "CHEM V101 Textbook Ventura College" and opens that other Workbench book; checked on 6.7 and 14.7, same on both. Signed in on desktop the same page correctly shows 6.6 ◀ / ▶ 6.8. | No content fix possible: LibreTexts builds these arrows. Likely because the book is still in Workbench (unpublished); recheck after Bookshelf publication, and report to LibreTexts if it persists. Students reach pages from Canvas module links (190, checked 11-13) and the table of contents, which work. | Simulator screenshots; desktop DOM links | Platform; not fixed | A student paging through the book with the arrows lands in another college's book. Desktop signed-out view not tested (signing out of the shared browser was avoided). |
| P1 | 13.5 (597194) PDF p. 1098 footer | Prints "curated by ." | No content change. Tags are correct (`author@Daniel Kwasniewski`, same as the 77 pages that print correctly). The 22:12 compile printed this footer correctly; the earlier `Full.pdf` had the same fault on 14.3. Treat as a compile-time flake: recompile, or compile 13.5 alone and check. | LibreTexts API tags, PDF text scan | Not fixable in content; recheck next compile |
| P2 | Cover, PDF p. 1 | Author "Unknown" | No content change possible. The root page (488223) already carries `author@Daniel Kwasniewski` and `authorname:dkwasniewski`; the cover generator looks the `authorname` up in LibreTexts' author registry, which has no record for `dkwasniewski`. Pages 2, 9 and the About page credit the author correctly. **Action: ask LibreTexts to create the author record (or set it at bookshelf publication).** | API tags read 2026-11-14 | Author/LibreTexts action |

## Checked and found correct (no change)

- All 27 In the Lab boxes: chemistry and safety (details in `LAB_MANUAL_INTEGRATION_BACKLOG.md`).
- ATP convention: consistent on every Chapter 13–15 page; each 36/38, 3 ATP/NADH or 129-for-palmitate mention is labeled as the older convention.
- Every Practice Problems page: each problem's question and answer print exactly once in the PDF (1,123 problems plus 84 cumulative).
- 0 internal links to non-book pages; 0 links whose "Section N.M" text points to another section; 0 "Section N.M" references to sections that do not exist; 347 references into Chapters 12–15 read for topic fit after the 12/13/15 reorder: all fit (15.1's statin pointer to 15.10 is thin but not wrong).
- Rosa's Story parts 1–15: timeline, medications (metformin, atorvastatin, insulin glargine, doxycycline), lab values and answers consistent and correct.
- Valley figures flagged 11-13 (11.4 thresholds, 9.2 20%, 4.5 40%) were already rechecked and closed (ISSUE_LEDGER line ~698).

## Deliberately not changed

- Experiment numbers in In the Lab boxes (provisional; see the backlog).
- "last updated November 13, 2026" on About This Book: batch AG went live 11-14. Change it, with a version-history line, in the same step that publishes batch AH, so the date is the publication date.
- P3 items: inherited "This table finds the mass of atoms." captions (1.5), "109.5o" with a letter o (1.7, inherited), long 1.7 alkane table with tall rows (PDF pp. 81–89), two inherited external links that redirect or loop for scripts (calepa.ca.gov chlorpyrifos release, ozonewatch.gsfc.nasa.gov).
