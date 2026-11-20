# Final verification before review (2026-11-19/20)

Scope: the live CHEM 3B book (199 pages), Full (33).pdf, external links, phone display, color, and screen-reader structure.
Standard: WCAG 2.1 AA (plus the 2.2 AA rules axe checks), the book's own accessibility statement (About This Book, 597270).

## What was tested

| Test | Scope | Result |
|---|---|---|
| Local copies match live | all 199 pages, SHA-256 | 195 matched; 4 (488232, 597107, 597108, 597132) were the Nov 15 batch AK publish that the local copy had missed. Replaying AK reproduced the live hashes exactly. Synced (e16d160). |
| Automated WCAG scan, live pages as LibreTexts renders them | all 199 pages, 320 px wide (WCAG reflow width), hidden answers opened, axe-core 4.10.2 (WCAG 2.0/2.1/2.2 A+AA + best practice) | 0 errors. Findings: (1) LibreTexts glossary pop-ups `aria-allowed-attr` on 149 pages (platform; already disclosed in the statement); (2) **scrollable-region-focusable**: 169 side-scrolling tables and figure boxes the keyboard could not reach (ours); (3) one invalid list (12.3); (4) one heading skip (15.4). 696 color-contrast "needs review" nodes (text over images/gradients axe cannot measure); no contrast failures. |
| Reflow at 320 px | all 199 pages | Only wide display equations on 5 pages (allowed: 2-D layout), the genetic-code table on 12.6 3 px wide, and the 5.2 figure caption 11 px wide (fixed). |
| Static structure | all 199 pages | 1,264 images: all have alt (34 empty alt on purpose: continuation strips of split figures). 262 iframes: all titled. 194 tables: all have header cells; 1 had no caption (fixed). 1 duplicate id (fixed). 9 new-tab links without rel=noopener (fixed). |
| Color | the book's 116 SVG figures, simulated deuteranopia/protanopia; all "shown in red/green" text | 12 figures use a dark red and dark green that look alike to red-green color-blind readers; in 11 the parts are also labeled in text, and in the collagen helix the chains are told apart by weave, not color. Every "in red / in green" sentence also names the part in words. No change needed. |
| Screen-reader math | all math | 1 page (11.6, 597171) used `\ ` spacing that MathJax speech reads as "empty" (9 places). Fixed (`\;`). |
| Hint/Answer controls | 131 pages, 1,640 Answer controls | Work with keyboard and screen readers, but show as a plain 47×18 px word: below the WCAG 2.2 24 px target size and not visibly a button. Fixed with the same screen-only 44 px button style as the CHEM 3A book (tested live: 109×44 px, arrow hidden from screen readers). |
| External links | 1,114 distinct URLs | 75/75 videos exist; 671 web links answer 200; 46 bot-blocked (CDC, DOI publishers, BLS, NIH, ATSDR, Fresno County, ChemistryViews, Textile Exchange) all opened correctly in a real browser. NASA Ozone Watch (2.8 image credit) timed out, including its home page: NASA server, recheck later. **3 dead: the GLmol 3-D viewer scripts on 11.1** (figure missing; fixed). |
| PDF (Full (33).pdf, 1,374 pp.) | whole file | Tagged, Lang en, title shown; 194 H1 / 1,009 H2 / 514 H3; 193 tables with header cells; 1,222 of 1,251 figures with alt (the 29 are continuation strips). Batch AS change present (p. 1201). |
| iPhone Safari (iOS simulator, signed out) | 9.2 | Loads for a signed-out reader; text, figures, videos, attribution and the Try It box render and reflow well. LibreTexts' floating side buttons cover the last letters of some lines (platform). The "next page" arrow shows "CHEM V101 Textbook…" for signed-out readers (known LibreTexts bug, in post-publish checks). The simulator was too slow on this machine for tap-through of the Try It box; the widget passed real-tap tests earlier. |

## Fixed in batch AT (see audit/BATCH_AT_REVIEW.md)

11.1 missing figure; 180 tables + 109 figure boxes keyboard-focusable; 1,640 Hint/Answer controls as 44 px buttons; 12.3 list; 15.4 heading; 12.2 duplicate id; 5.2 figure reflow; Course Outline table caption; math speech on 597171; rel=noopener on 9 links.

## Not covered (honest limits)

- A real VoiceOver/NVDA listening pass by a person (the 3A book has a script for this: github/CHEM3Atextbook/audit/VOICEOVER_TEST_SCRIPT.md; the same script works for 3B).
- Text inside figure images (contrast measured only for the SVG colors, not every PNG).
- Caption accuracy of the YouTube videos.
- LibreTexts' own interface (glossary pop-ups, Previous/Next arrows, floating buttons).

## After publishing batch AT (rescan of all 163 changed pages, 2026-11-20)

- All 1,640 Hint/Answer controls measure at least 44 px; LibreTexts kept tabindex/role/aria-label and the new style (it wraps the style in its usual CDATA markers).
- The 11.1 figure displays with caption, credit and 3-D link.
- New findings, fixed in batch AT2: (1) pages with several wide figures had regions all named "Wide figure: scroll sideways" (axe landmark-unique, 21 pages); (2) 32 side-scrolling figure boxes are `<span class="fig-scroll">`, missed by AT (6 pages), plus the 3.7 bromination reaction row.
- No other violations apart from the LibreTexts glossary pop-ups.
- After batch AT2 (published 2026-11-20): rescan of all 70 changed pages, plus a fresh rescan of the 10 pages that had findings, at 320 px: **0 violations** other than the LibreTexts glossary pop-ups.
