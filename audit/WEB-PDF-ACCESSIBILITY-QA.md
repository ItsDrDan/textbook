# Web, PDF and accessibility QA (master refinement pass, 2026-11-13)

Web and PDF are reported separately and never merged. "Tested" means the check named was run in this pass; anything else says so.

Environment: page snapshot `pages/live/` (all 199 pages, matched live by SHA-256 after batch P; page bodies have not changed since); live pages opened in the app's browser pane (Chromium), signed in as the author; PDF = `Full.pdf` compiled 2026-11-13 16:37, 1,340 physical pages, Prince 16.2; PDF read with PyMuPDF.

## 1. Preflight items from the brief

| Item | Finding | Web | PDF | Status |
|---|---|---|---|---|
| Version mismatch | About This Book says "Version 1.2" at the top and in the history, but the Reviews paragraph still says "This is version 1.1." (PDF p. 15). | confirmed in 597270 | confirmed p. 15 | drafted in batch Q |
| Cover author "Unknown" | PDF p. 1 prints "Unknown" under the title; the PDF metadata Author field is empty. The inside title page (p. 2) names the author. This comes from the LibreTexts book record, not from any page body. | n/a | confirmed | **author action:** set at LibreTexts (bookshelf submission), as already planned |
| Blank "curated by ." | 78 page footers end "authored, remixed, and/or curated by ." (the author's own pages). Adapted pages print "Staff via source content…", "LibreTexts" or "Muhammad Arif Malik". The name comes from each page's author tag, which the own pages lack. | n/a | 78 pages | **proposed, needs OK:** add the author tag to the 78 own pages through the tags API (same method as the Index tag moves); one test page first, then compile it to confirm the footer |
| Near-empty pages (e.g. p. 197) | 15 physical pages hold only the license footer (9, 123, 197, 237, 249, 319, 333, 364, 418, 557, 720, 898, 935, 1144, 1310): the footer block did not fit under the last line of the page before it. A few more hold only the last line or two of a page plus the footer. No page is blank because of a hidden answer widget. | n/a | measured | export-level; not fixable from page content without padding text. Left. |
| Accessibility claims | See section 3. The book's own content passes; two gaps are outside the claim as written. | tested (sample) | tested (structure) | see below |
| Links after the renumbering | 1,089 internal `/@go/page` links: every link whose text shows a section number points at the page with that number. 0 mismatches, 0 unknown targets. Every "Section N.M" mention names a section that exists. | tested, all pages | TOC has 1,713 entries; 194 page-level entries map to the 194 printed pages | pass |
| Print fallback for Try It and games | A Try It box prints its title, a one-sentence description and a link "Open this practice in a new tab"; Practice Games pages print each game's description, suggested order and link. Nothing promises interaction in print. A paper reader has no visible address, only a hyperlink. | n/a | viewed p. 142, 329 | pass; optional P3: print the Study Hub address once per Practice Games page |
| Glossary translations | 329 entries audited (`audit/reviews/glossary_audit.md`). | read in full | n/a | 29 edits drafted |
| Clinical nuance | See `audit/ROSA-AND-VALLEY-CONTINUITY.md`. | | | |

## 2. Web checks (all 199 pages unless noted)

| Check | Method | Result |
|---|---|---|
| Internal link numbers | script (`audit` run of 2026-11-13) | 1,089 links, 0 wrong |
| Images without alt text | script | 0. (34 images have empty alt on purpose: they are the 2nd and later strips of a sliced figure whose first strip carries the description.) |
| Iframes without a title | script | 0 of 256 (78 videos, 178 widgets and games) |
| Tables without header cells | script | 0 of 193 |
| Heading order | script | 1 skip: 3.2 jumps from h2 to h4 at Example 1 (P3) |
| Vague link text ("here", bare URLs) | script | 0 |
| Answer-key parity | script | 108 keyed pages, entries equal hidden answers on every page |
| Widget and game addresses | curl, 243 distinct URLs | 241 answer 200; the other 2 are the same URLs with unencoded spaces (browsers encode them; they load). No X-Frame-Options or CSP header blocks embedding. All HTTPS with HSTS. |
| Widget parameters | script against `bank/` | every topic, id and reaction key exists; every filtered pool is at least as large as `n` |
| Try It widget, bank mode | live, by hand | loads; hint gives a concept cue; a wrong choice gives feedback specific to that choice and "Try again" (recoverable); score in an `aria-live="polite"` region; all buttons at least 44 px high; `lang="en"`; a `prefers-reduced-motion` rule exists; progress is in localStorage only |
| Try It widget, axe-core 4.x, WCAG 2.0/2.1/2.2 A and AA rule tags | local copy with the patched `fbx.js`, before and after answering | 0 violations; 18–20 colour-contrast nodes "needs review" (axe could not decide; not hand-measured) |
| Live section page 4.5, axe-core 4.10 on `#pageText` | live | **1 rule fails, 208 nodes: `aria-allowed-attr`** on `<div class="glossarizer_replaced" aria-expanded="false">`. This markup is added to every glossary word by LibreTexts' glossary script after the page loads; it is not in the page source. No other violation in the page text. |

**Not tested in this pass:** a real screen reader (VoiceOver/NVDA) session; 200% and 400% zoom reflow; phone and Chromebook hardware; video caption accuracy (the pages only say captions exist); the reaction-lab mode and the 16 full games beyond loading (see `GAMES-AND-TRYIT-VALIDATION.md`); keyboard-only traversal of a LibreTexts page end to end.

## 3. Accessibility: claims against evidence

The About page says every page passed an automated WCAG 2.1 A/AA scan and that the Try It widgets and games are operable. Findings:

| # | Sev | Where | Finding | Action |
|---|---|---|---|---|
| A1 | P1 | Try It widget (`js/fbx.js`), all bank-mode embeds | **In 114 of the 171 questions whose answer choices are drawings, two or more choices had the same accessible name** (for example two choices both read "skeletal structure, 5 carbons, O, 1 double bond" for an aldehyde and a ketone). A screen-reader user could not tell the choices apart. Stem drawings were all named just "skeletal structure". | **Fixed locally** (commit 3d548f2): the description now says where each atom, multiple bond, wedge and dotted line sits, and adds a condensed-formula walk only when two choices would still read the same. Tested on all 1,065 drawings in the bank: 0 duplicate labels, 0 errors; verified in the browser. Goes live when the branch is merged to `main` (GitHub Pages). The games that load `fbx.js` from this repo get it at the same time. |
| A2 | P1 (platform) | every page with glossary words | LibreTexts' glossary pop-ups are `div`s with `aria-expanded` but no role and no tab stop: an axe "critical" failure, and the pop-up definitions cannot be opened from the keyboard. The Glossary page itself is a normal table and is accessible. | Not fixable in page content. **Author action:** report to LibreTexts; consider one sentence in the accessibility statement that pop-up definitions need a mouse or touch and the Glossary page has the same text. |
| A3 | P2 | accessibility statement wording | "Every page was checked with an automated scan" is true of the page content as authored; it does not cover what the platform adds at run time (A2) or the widget labels (A1). | After A1 ships, the statement is accurate for the book's own content; add the A2 sentence if wanted. |
| A4 | P3 | 3.2 | One heading-level skip (h2 → h4). | Left for the next page edit on 3.2. |
| A5 | P3 | widget | Colour contrast flagged "needs review" by axe on 18–20 nodes; not measured by hand. | Next session: measure the pill badges and hint text against 4.5:1. |

## 4. PDF checks (2026-11-13 16:37 export)

| Check | Result |
|---|---|
| Tagged PDF | Yes: `MarkInfo /Marked true`, a structure tree, `Lang (en)`, `DisplayDocTitle true`. |
| Structure tags | 14,453 P; headings H1 194, H2 983, H3 514, H4 22; 192 tables with 790 TH and 4,760 TD cells; 998 lists; 1,785 Formula; 651 Caption. |
| Figure alt text | 1,124 Figure tags, 1,095 with `/Alt`, none empty. The 29 without are the continuation strips of sliced figures (first strip carries the description). |
| Title / author metadata | Title set; Author empty (see preflight). |
| Page labels | None: a PDF viewer shows physical page numbers (1–1,340), which differ from the printed ones (roman numerals to xxi, then 1–1,318). The ledger records both. Export-level. |
| Bookmarks | 1,713 outline entries. |
| Hyperlinks | 5,350 link annotations. Not each one followed. |
| Blank or near-blank pages | 15 footer-only pages, listed above. None caused by hidden content. |
| Answers in print | Print keys present on 108 pages; after batch Q every exercise has one. Keys sit at the end of the page, not beside the questions. |
| Text under 6 pt, missing glyphs, raw MathJax | Not re-measured in this pass; the 16:20/16:37 check in `ISSUE_LEDGER.md` stands (31 pages with words under 6 pt; worst: 14.5.2 at 4.8 pt, 15.9.1 at 5.1 pt). |
| Reading order | Tag tree exists and follows source order (Prince); not audited page by page with a screen reader. |

**Not tested:** PAC/veraPDF conformance (PDF/UA), screen-reader reading order on complex pathway pages, every hyperlink target.
