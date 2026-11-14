# Final publication QA (2026-11-14)

Scope: *Introductory Organic and Biological Chemistry for FCC*, 199 live LibreTexts pages, PDF export of 2026-11-14 10:50 (1,359 pp.). This was a gate check, not a rewrite. It was done by Claude (AI) in one session; it is **not** an independent peer review.

## What was done, and how

| Check | Method | Result |
|---|---|---|
| Source = live = PDF | Fetched all 199 pages via the deki API in the signed-in browser and SHA-256-compared them with `pages/live/`; matched each section paragraph against the PDF text | 199/199 identical; PDF current (includes batch AG) |
| Answer keys and worked examples | Five independent AI reviewers, three chapters each, re-solved every worked example, exercise, Chapter Guide item, Practice Problem and cumulative problem from the stripped page text **before** reading the answer; scripted Q/A numbering match; codons checked by script | ~2,000 items; **0 wrong keys**; 1 P1 convention issue; 9 P2 wording items |
| Printed answer keys | Counted every "Problem N.M" in each chapter's Practice Problems print range | Every problem prints question + answer once; none missing, none duplicated |
| PDF render scan | All 1,359 pages: raw TeX, "Swipe sideways", replacement characters, "undefined/NaN", "Unknown", blank footers, pages under 40 words; flagged pages rendered and viewed | Clean except cover "Unknown" and the 13.5 footer (p. 1098) |
| Internal links and section refs | Every `/@go/page` link and every "Section N.M" mention, all pages | 0 broken; 347 Ch 12–15 references read for topic fit |
| Interactives and videos | HTTP check of all 36 itsdrdan.github.io endpoints and oEmbed check of all 75 YouTube videos; one Try It (6.7 esterification) played by hand: wrong answer → specific feedback, right answer → accepted | All load; widget logic correct in the one tested |
| External links | 193 non-video links fetched | 161 OK, 29 refuse scripts (403: CDC, OSHA etc.; not broken), 3 redirect (2 loop for scripts) |
| Lab references | Every In the Lab box and lab mention | 27 boxes, science OK; provisional items in `LAB_MANUAL_INTEGRATION_BACKLOG.md` |
| Phone run-through | iPhone 17 simulator, Safari, signed out: 6.7 section (figures, side-scroll box, lab box), 14.7 Practice Problems (Answer toggle), 14.8 Practice Games (embedded Metabolic Marathon: question, hint, correct-answer feedback), Glossary | All work at phone width; Previous/Next arrows go to another Workbench book for signed-out readers (N1); Answer toggles look like plain text (no arrow), cosmetic; Fig 6.7.2 labels small but zoomable |
| Rosa's Story, Valley | Read all 15 Rosa parts; checked the ledger for open Valley figures | Consistent; Valley rechecks already closed 11-13 |
| Front matter claims | About, For Instructors, Course Outline Alignment read for claims | 3 wording fixes drafted (lab manual x2, problem count) |

## Chapter matrix

"Tested" = done in this pass. "Assumed" = relied on an earlier pass's record, not repeated today.

| Ch | Pages inspected | Science / answer keys (items re-solved) | Student path | Interactives / links | Figures / print | Accessibility | Findings | Unresolved |
|---|---|---|---|---|---|---|---|---|
| 1 | all 12 | Tested (~135); clean | Partly tested: route, guide, problems read; 1.5 lab box | Links tested; widgets load (tested); play-through assumed | Text scan tested; pp. 81–89 viewed (tall table rows, readable) | Alt text used to solve items; screen reader not tested | B5, F1 | ~6 Lewis-drawing answers are images only (not verifiable from text) |
| 2 | all 13 | Tested (~125); clean | Partly tested | Same | Text scan | Same | — | — |
| 3 | all 12 | Tested (~120) | Partly tested | Same | Text scan | Same | B4 | — |
| 4 | all 14 | Tested (~135) | Partly tested | Same | Text scan | **B1 alt text gives wrong thymol isomer** | B1 | — |
| 5 | all 9 | Tested (~130); clean | Partly tested | Same | Text scan | Same | — | — |
| 6 | all 14 | Tested (~120); clean | Partly tested; 6.7 Try It played (tested) | Try It tested | Text scan | Same | — | — |
| 7 | all 15 | Tested (~160); clean | Partly tested | Same | Text scan | Same | — | — |
| 8 | all 11 | Tested (~140) | Partly tested | Same | Text scan | Same | B3 | — |
| 9 | all 10 | Tested (~115) | Partly tested | Same | Text scan | Same | B2 | 3 saponification practice panels in Figs 9.2.3–9.2.5 have no printed answer (by design, figure practice) |
| 10 | all 14 | Tested (~130); clean | Partly tested | Same | Text scan | Same | — | ~3 image-only items consistent with alt text |
| 11 | all 11 | Tested (~150) | Partly tested | Same | Text scan | Same | **C1–C8 citrate synthase → transferase (decided)** | 1 graph item consistent with alt text |
| 12 | all 13 | Tested (~145; ~50 codon sequences by script); clean | Partly tested | Same | Text scan | Same | — | 2 image-read sequences consistent with alt text |
| 13 | all 13 | Tested (~150); clean | Partly tested | Same | Text scan; **13.5 footer blank (p. 1098)** | Same | P1 (print) | Recompile |
| 14 | all 9 | Tested (~110); ATP convention consistent | Partly tested | Same | Text scan | Same | (C, 14.3 already says "in this course") | — |
| 15 | all 15 | Tested (~130) | Partly tested; Rosa Part 15 read | Same | Text scan | Same | B6, B7 | — |
| Front/back | 11 | Claims read | — | — | Cover "Unknown" (LibreTexts registry); Glossary prints without its intro paragraph (LibreTexts glossary template) | — | F2, F3, F4 | Cover author |

"Student path, partly tested" means a reviewer worked the readiness questions, examples, guide and problems in order from the text; nobody watched a real student, and timing, motivation and the games were not tried.

## Not tested in this pass

- Screen reader (VoiceOver/NVDA) session; keyboard-only run of the book and games; zoom/reflow; color contrast by hand; captions/transcripts of the 75 videos.
- Playing the Practice Games through; all but one Try It set; ADAPT assignments and settings (counts in the ADAPT boxes were verified on 11-13, not today).
- Real phones; on the simulator only four pages were walked through today (the 11-13/11-14 sweep is relied on for the rest: all 199 pages fit at 375 px).
- Visual inspection of every PDF page: only flagged pages and their neighbors were rendered and viewed; labels under 6 pt were last measured on the 22:12 11-13 compile (clean) and not re-measured today.
- Chemical drawings were checked through their alt text and captions, not by viewing each image.
- PDF/UA conformance; every PDF hyperlink.
