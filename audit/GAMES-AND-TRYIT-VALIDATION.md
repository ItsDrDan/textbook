# Games and Try It validation (master refinement pass, 2026-11-13)

What is embedded, what was tested, and what was found. Live tests were run in the app's browser pane against the deployed GitHub Pages sites on 2026-11-13.

## 1. Inventory (from `audit/inventory.json`; every iframe on all 199 pages)

| Kind | Embeds | Where |
|---|---|---|
| Try It, question-bank mode (`practice.html?t=…`) | 103 | section pages, Chapter Guides, Practice Problems (cumulative mixes), Practice Games |
| Try It, reaction-lab mode (`practice.html?rxn=…`) | 17 | reaction sections of Chapters 2–7 and their guides |
| Full game embeds | 58 | 15 Practice Games pages: Final Boss 14, Organic Origins 7, Sticky Molecules 7, Bond Voyage! 6, hub page 5, Mirror Match 4, Proton Patrol 3, Metabolic Marathon 3, Functional Group Flashcards 2, Peptide Party 2, Lewis Structure Studio 1, Sweet Structures 1, Lipid Lab 1, Enzyme Engine 1, Helix Hustle 1 |
| Videos (YouTube) | 78 | section pages and guides |
| **Total** | **256 iframes on 99 pages**, every one with a `title` | |

70 of the 125 content sections have no embed at all. That is by design in most cases (the Chapter Guide carries the practice), but the Chapter 11–15 route pages tell students to "answer the Try It questions in each section"; batch Q rewords that line on five pages.

The section → objective → widget map is the `Components`, `Objectives` and `Page id` columns of `TEXTBOOK-COVERAGE-LEDGER.md` together with `audit/reviews/widget_alignment.md` (one row per bank-mode widget).

## 2. Test matrix

| Check | Scope | Result |
|---|---|---|
| Address answers | 243 distinct widget/game/figure URLs (curl) | 241 return 200. The other two are URLs with literal spaces in the page source (1.8 and 3.1 widgets); browsers encode them and they load. P3: encode them next time those pages are edited (batch Q replaces the 3.1 one). |
| Framing allowed | response headers of the widget, Final Boss, Sticky Molecules | No `X-Frame-Options`, no CSP; HTTPS with HSTS. They embed. |
| Parameters valid | all 120 `practice.html` embeds, against `bank/` and the reaction-key list | every topic file, question id and reaction key exists; no filtered pool is smaller than its `n` |
| Loads inside the book | 4.5 live page | three iframes present with titles; the Try It iframe is `loading="lazy"`; the box has a "Not loading? Open this practice in a new tab" link |
| Bank-mode interaction | 4.8 widget, by hand | question renders; **Hint** gives a concept cue without the answer; a wrong choice gets feedback written for that choice and "Try again"; **Check**, **New Question**, topic menu work; score announced through `aria-live`; no console errors |
| Automated accessibility | bank-mode widget, axe-core, WCAG 2.0–2.2 A/AA tags, before and after answering | 0 violations (patched local copy); colour contrast "needs review" on 18–20 nodes |
| All 16 game pages and the reaction lab load | each opened in a 420 px wide frame | all load with no script error; each has a title, an h1, `lang="en"`, a viewport tag, a `prefers-reduced-motion` rule, no horizontal scroll at 420 px, no unlabeled visible button, no image without `alt`; none claims to report grades |
| Privacy / gradebook wording | widget footer and Practice Games pages | "Progress is saved in this browser only." No sign-in. Nothing implies a grade is submitted. ADAPT is described separately on the landing pages. |
| Print fallback | PDF pp. 142 and 329 | description, suggested order and a link print; no dead iframe box |

**Not tested in this pass:** playing each game through; keyboard-only play of each game; correctness of randomly generated reaction-lab and game questions (Bond Voyage!, Final Boss and the bank were audited on 2026-11-11 to 11-13; see `ISSUE_LEDGER.md`); touch behaviour on a real phone; saved-progress persistence across visits; the ADAPT assignments (settings were not opened; the "50 of 101" statement for Chapter 1 was not re-verified).

## 3. Findings

| # | Sev | Finding | Evidence | Action |
|---|---|---|---|---|
| G1 | **P1** | **74 of the 103 bank-mode Try It boxes serve questions that are off-topic for their section or on material not yet taught.** The `q=` filter matches words anywhere in a question's choices and explanation, so a loose pattern pulls in the wrong items. Worst: 1.3 "Lewis structures" 2 on-topic of 39; 3.1 "Naming alkenes and alkynes" 2 of 57 (the rest are addition reactions taught in 3.4); 4.8 "Ethers" 2 of 18 (alcohol oxidation, and thiols from 4.9); 5.1 6 of 48; 13.1 11 of 92; 13.4 "Glycolysis and pyruvate" 26 of 136, with 94 on Chapters 13.5–15. | `audit/reviews/widget_alignment.md` (all 1,110 bank items classified by stem and correct answer; distractors and images not read); confirmed live: the first "Ethers" question served was an alcohol oxidation. | **Drafted in batch Q:** 73 widgets get an explicit `ids=` list (or, for 8 chapter-end widgets, a pattern that drops the 1–3 forward items); 144 edits including the matching "open in a new tab" links. Every new URL was re-simulated independently against the bank (ids exist, pool equals the listed pool, `n` ≤ pool) and one was loaded live. Changed widgets start with fresh saved progress. |
| G2 | P1 | Bank gaps exposed by G1: only **2** Lewis-structure items exist (the 1.3 widget is left unchanged for now and flagged), **1** true alkene-naming item, **5** ketone-body items. Thin (6–9 items): 2.3, 2.5, 4.2, 4.9, 6.1, 6.5, 8.5, 8.7, 10.1, 13.3, 15.3, 15.9. | same file, "bank gaps" | Next session: write 6–8 items for each gap (they also serve Final Boss and ADAPT), or point 1.3 at Lewis Structure Studio instead. |
| G3 | P2 | Cumulative-review mixes (`fresh=1`) leak ahead because topic files span chapters: the 2.11 mix can draw 98 of 246 items from later chapters; 13.11 can draw 110 (one `metabolism.json` covers Chapters 13–15). | same file, item 7 | Needs a per-item chapter tag or split topic files; not drafted. |
| G4 | P1 (accessibility) | Duplicate screen-reader labels on structure choices (114 of 171 items). | `WEB-PDF-ACCESSIBILITY-QA.md` A1 | Fixed locally in `js/fbx.js`; live on merge. |
| G5 | P3 | Final Boss opened with `?course=3B` still shows "CHEM 3A" in its browser-tab title at load. | game load test | Separate repo (`finalexam`); note only. |
| G6 | P3 | Widgets titled for more than the section teaches: 6.1 "Naming acids and esters" (esters are 6.5), 12.2 "DNA structure and replication" (replication is 12.3). Pools are narrowed in batch Q; titles kept. | alignment file | Retitle when convenient. |

## 4. New interactive development

None built. The assessment does not show a gap that a new widget would close better than fixing selection (G1) and writing questions (G2). The one candidate worth a prototype later is a Fischer ↔ Haworth conversion drill for 8.4, the hardest skill in Chapter 8, which today has only multiple-choice items.
