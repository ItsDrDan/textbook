# CHEM 3B textbook — issue ledger

Started 2026-11-10 from the ChatGPT revision brief (`CHEM_3B_Claude_Revision_Brief.md`, IDs R01–R04, C01–C08, D01–D05, L01–L08, M01–M03)
and a check of the 2026-11-09 PDF export (`Full.pdf`, 1,274 pp., PrinceXML 16.2).
Status values: confirmed · under investigation · corrected (source) · corrected (live) · verified · unresolved.

| ID | Evidence | Status | Source | Correction | Propagation | Verification | Remaining work |
|---|---|---|---|---|---|---|---|
| R01 | Atom labels missing in PDF: acetaminophen p.110, amine/amide schemes p.555, others. White boxes where O/N/Cl/NH₂ should be. | corrected (source); live repair ready | `js/engine.js` atomLabel, `tools/molsvg.py`, `tools/scheme.js`, `tools/draw.js`; live: `fig-p<page>-<n>.svg` files attached to LibreTexts pages | Cause: labels use `stroke="#fff"` + `paint-order="stroke"`; Prince ignores paint-order and paints the white outline over the letter. Halo is now a separate white `<text>` (aria-hidden) under the coloured letter. `tools/printfix.js` applies the same change to existing SVGs. | Live scan (anonymous, 2026-11-10): 57 SVG files on 30 pages need it (249 hidden labels), from 156 of 198 pages; 54 pages could not be read anonymously (download redirects). `js/fbx.js` (games' Exam Practice renderer) still uses paint-order — browser only, not in the PDF; left as is. `js/engine.js` is copied from ItsDrDan/organicreactions — copy the change back there. | Rendered with paint-order removed (= Prince behaviour) in Chrome: acetaminophen, lidocaine, ethylammonium, neutralization scheme (sandbox), and live files fig-p597116-3 (saponification, Na⁺), fig-p597121-4 (tetramethylammonium), fig-p597175-1 (5 nucleobases): all labels missing before, all present after. Fix is idempotent. | Run `tools/repair-print.js` signed in (dry run, then pilot of 1, then all). Re-export PDF and check pp. 71, 110, 124, 125, 195, 262, 403, 555 and the nucleobase figure. Grayscale check. |
| R02 | ⯑ on 48 pages; 142 occurrences, all superscript charges (H⁺, NAD⁺, Na⁺, Cl⁻, NH₄⁺, OH⁻, HCO₃⁻…). | corrected (source); live repair ready | Text written with U+207A ⁺ / U+207B ⁻ (raw or `&#8314;`/`&#8315;`); Atkinson Hyperlegible / Liberation Sans lack the glyphs → PrinceFallback box. | HTML text → `<sup>+</sup>` / `<sup>&minus;</sup>`; SVG text → raised `<tspan>`. Attributes (alt, aria-label) unchanged. | Snapshot: 4 pages / 12 charges in page text (597119, 597132, 597193, 597202); 38 more inside figure files (partial scan). | Sandbox render of neutralization scheme and live saponification figure: charges correct. | Same run as R01 (page text needs signed-in access). Check extracted PDF text for leftover ⯑ = 0. |
| R03 | Cover p.1 author "Unknown"; p.2 correct. | unresolved | Book metadata on LibreTexts (author tag). | LibreTexts creates the author tag and adds it when publishing; ask them, or set the book's author property before the next export. | — | — | Instructor/LibreTexts action. |
| R04 | Answers print directly under questions. | open | — | — | — | — | Later batch. |
| C01–C08 | See section below. | corrected (live) | LibreTexts pages | — | — | — | — |

## Live repair log

**2026-11-10 (signed in as the book's author, built-in browser).** Full scan of all 198 pages and their SVG figure files.
- Fixed and written: **100 figure files** (457 hidden labels, 62 charges) and **page text on 4 pages** (597119, 597132, 597193, 597202). All 104 writes returned 200. Files keep their file ids (pages need no edit); LibreTexts keeps the old version as the previous revision, so any file can be rolled back from its file history. Pilot file fig-p597060-4.svg was read back after upload and displayed correctly; the page-text test (597119) read back byte-identical to the intended fix. Each page was re-checked unchanged just before writing.
- **Not yet checked: 86 figure files.** LibreTexts redirects downloads of recently viewed files to a cache the script cannot read (the same file reads fine after it has been cold for a while; a file we had just read was redirected minutes later). Their content is unknown; some will need the fix. Repo copies in `sections/` do not match the live files (the overnight upload redrew them), so they must not be uploaded instead.
  Next step: re-run `tools/repair-print.js` (dry run, then `window.REPAIR_APPLY = true`) in a day or so. It skips fixed files (`data-printfix="1"`) and reports any file it still cannot read.
  Blocked list: fig-p597059-1.svg fig-p597060-1.svg fig-p597063-1.svg fig-p597067-2.svg fig-p597068-1.svg fig-p597072-1.svg fig-p597073-1.svg fig-p597074-4.svg fig-p597079-1.svg fig-p597084-1.svg fig-p597085-4.svg fig-p597085-2.svg fig-p597085-1.svg fig-p597086-7.svg fig-p597086-6.svg fig-p597086-3.svg fig-p597086-1.svg fig-p597091-1.svg fig-p597094-1.svg fig-p597096-1.svg fig-p597099-2.svg fig-p597100-8.svg fig-p597100-7.svg fig-p597100-6.svg fig-p597104-2.svg fig-p597105-2.svg fig-p597106-4.svg fig-p597106-3.svg fig-p597107-9.svg fig-p597107-8.svg fig-p597107-7.svg fig-p597107-6.svg fig-p597107-3.svg fig-p597107-2.svg fig-p597107-1.svg fig-p597108-2.svg fig-p597109-7.svg fig-p597109-4.svg fig-p597109-3.svg fig-p597115-1.svg fig-p597116-1.svg fig-p597117-1.svg glycine_vs_acetic_acid_pKa.svg fig-p597119-7.svg fig-p597119-2.svg fig-p597119-1.svg fig-p597121-2.svg fig-p597121-1.svg fig-p597128-4.svg fig-p597128-3.svg fig-p597131-14.svg fig-p597131-12.svg fig-p597131-6.svg fig-p597131-5.svg fig-p597131-4.svg fig-p597131-1.svg fig-p597132-7.svg fig-p597132-4.svg fig-p597135-1.svg fig-p597136-1.svg fig-p597142-3.svg fig-p597144-7.svg fig-p597144-6.svg fig-p597144-5.svg fig-p597146-1.svg fig-p597154-1.svg fig-p597157-2.svg fig-p597165-1.svg fig-p597166-1.svg fig-p597167-1.svg fig-p597171-1.svg fig-p597172-1.svg fig-p597176-2.svg fig-p597176-1.svg fig-p597177-1.svg fig-p597183-3.svg fig-p597183-2.svg fig-p597193-1.svg fig-p597194-1.svg fig-p597197-5.svg fig-p597197-2.svg fig-p597197-1.svg fig-p597204-2.svg fig-p597207-1.svg fig-p597208-1.svg fig-p597212-2.svg

## Science corrections, 2026-11-10 (live on LibreTexts, 14 pages; each page re-read unchanged before saving and read back identical after)

| ID | Page | Change |
|---|---|---|
| C01 | 5.7 Practice Problems (597108), Problem 5.2 | Key now explains butanal is the only aldehyde among the choices; simple ketones and 2-propanol do not react; points to Ch 8 for ketose sugars. |
| C02 | 10.1 (597154) threonine example | Question uses explicit pH 1 and pH 11; answer uses α-COOH pKa ≈ 2.1 and α-NH3+ pKa ≈ 9.1, says pI gives the sign of net charge and pKa the form. |
| C02 | 10.12 Practice (597165) Problem 10.59 | Removed speed rankings (aspartate "fastest", histidine "only slightly", arginine "farther"); added that pH vs pI gives direction only. |
| C02 | 10.12 Practice (597165) Problem 10.74 (SGK peptide) | Lysine side chain justified by side-chain pKa ≈ 10.5, not the pI of free lysine. |
| new | 10.2 (597155), 10.3 (597156) pI tables | Threonine pI 6.5 → 5.6 (matches the 10.1 worked example; accepted value ≈ 5.6). |
| C03 | 11.1 Enzymes (597166) | "Every enzyme belongs to one of six classes" → course uses six traditional classes; EC 7 translocases acknowledged, not assessed. Examples in Ch 13 ("one of the six classes from Chapter 11") left as is: scoped to the course list. |
| C04 | 13 chapter page (597051) video description; 14.3 (597202) step 1 | ATP hydrolysis described as releasing energy overall (bond breaking takes energy); citrate synthase step coupled to thioester hydrolysis. Also `tools/videos.py` and the Final Boss bank item on succinyl CoA → GTP (`bank/metabolism.json`; mirror in the Final Boss repo). |
| C04 (new) | 14.3 (597202) adapted note | "Oxidation generally releases energy… reduction consumes energy" → catabolic oxidations are downhill overall because electrons go to O2. The rest of that adapted note (C=O vs C=C bond energies predicting NADH vs FADH2) is a shaky heuristic: instructor to decide whether to keep it. |
| C05 | 13.4 (597192), 14.2 (597201), 15.1 (597207) | "ATP numbers in this course" box added right after Learning Objectives, before the older 3/2 tables. Not yet audited: every question expecting 32 ATP states the shuttle assumption. |
| C06 | 13.8 Glycogen (597196) | Energy-cost paragraph uses reaction names instead of step numbers; states 2 ATP-equivalents from free glucose (1 from glucose 6-phosphate). |
| C07 | 13.10 Chapter Guide (597198) objective | B-vitamin instruction limited to NAD/NADP (niacin B3), FAD (riboflavin B2), CoA (pantothenic acid B5); ATP/ADP noted as not vitamin-derived. |
| C08 | 13.9 (597197), 13.10 (597198) ×2 | Slogan "if you need ATP one way…" removed in all three places; replaced with: kinase steps are too far downhill to reverse, so bypass enzymes are used; the phosphatase bypass hydrolyzes the phosphate, so no ATP is regenerated. |

Drafts synced so a rebuild does not undo these: `drafts/Ch05_Practice_Problems…`, `drafts/Ch13_Chapter_Guide…`. `pages/` is build output and still has the old text until the next `build_pages.py` run.
Not changed (instructor's call): 11.x "Every enzyme is a protein" (ribozymes).

## PDF check, export compiled 2026-11-11 (1,275 pp.)

- All C01–C08 text changes present. ⯑ glyphs: 146 → 82 (37 pages: 290, 317, 322, 326, 339, 342, 371, 373, 399, 401, 434, 439, 440, 454, 477, 478, 480, 487, 491, 493, 495, 498, 519, 520, 554, 556, 557, 558, 562, 563, 564, 568, 573, 1052, 1117, 1122, 1128).
- Figures now printing: acetaminophen p.110, eugenol p.125, chloroalkane p.195, benzocaine p.262, amide reactions p.555.
- Hidden-label scan (`tools/pdf_hidden_scan.py`, pdfplumber: glyph with coloured fill + white outline and no clean copy on top): **47 pages**, list in `tools/pdf_hidden_labels_2026-11-11.json`. p.203 is a false positive (table text); p.319 is real (pKa chart labels).
- New cause found: some labels carry a white outline **without** paint-order (p.555 ethylammonium N: fill blue, stroke white). printfix v2 (2026-11-11) also splits those; v2 leaves v1-fixed files unchanged.
- Blocked: after a PDF compile every figure file is cached and cannot be read by script, so the next repair run must happen **before** recompiling, after the cache clears (unknown TTL; >1 h observed).
Next run: paste `tools/repair-print.js` signed in (dry run → `window.REPAIR_APPLY = true`), then recompile and re-run `python3 tools/pdf_hidden_scan.py` on the new Full.pdf. Target: 0 pages (except p.203) and 0 ⯑.

## Repair from page history, 2026-11-11 (no waiting on the cache)

- Figure files can be rebuilt from page history: each page's revision just before the Nov 5 "SVG → file" pass still holds the inline SVGs. Matched by alt text = aria-label (order as tie-break), serialized with the browser's HTML parser + XMLSerializer (keeps nested SVGs and viewBox case), checked against the live image's natural width/height (210/210 matched exactly) and parsed as XML.
- Root cause of the remaining hidden labels (incl. p.555 NH3+): **self-closing `<text …/>`** (empty reaction-condition labels) made the old text regex swallow the next label. printfix v3 matches self-closing text separately. 31 figures were affected.
- Uploaded 153 files (57 never fixed + 96 re-fixed with v3); all 153 audit to 0 hidden labels and 0 superscript characters before upload.

## PDF check, export compiled 2026-11-11 (late), and follow-up fixes

- Hidden-label scan: 3 pages (p.203 false positive; pp.246/248 = 3.9 Chapter Guide figures, which the 153-file pass had skipped). ⯑: 56 on 29 pages.
- Second history-rebuild pass over all pages for figures not updated in the first: 144 rebuilt, 85 uploaded (incl. 597086-2/3/4/6/7/8); 0 size mismatches, 0 XML errors, 0 hidden labels after fix. Identical re-uploads create no new revision (expected).
- ⇌ (U+21CC, `&#8652;`) is not in the PDF fonts: 29 occurrences on 12 live pages replaced by MathJax `\(\rightleftharpoons\)` (verified render on 4.10); drafts synced.
- GitHub-hosted figures with superscript charges fixed in repo: `figures/pathways/oer/atp_synthase.svg`, `atp_rotation.svg`, `respiration.svg`, `sections/reactions/roadmap.svg`; `tools/oer_figs.js` now writes through printfix. printfix v4: a space right after a raised charge is written as a no-break space (renderers dropped it: "H⁺flow").

## PDF check, export compiled 2026-11-11 00:3x — R01/R02 resolved
- Hidden-label scan: only p.203 (known false positive: table text with white outline). 0 hidden figure labels.
- ⯑: 1 left (p.371, ⇌ in the glucose_ring.svg title, GitHub-hosted). Title reworded to "… in equilibrium" in the SVG and in tools/oer_figs.js; the figure already draws equilibrium arrows. Expected next export: 0.
- Status: R01 verified, R02 verified pending this last figure.

## 2026-11-11: C05 follow-up and R04
- **C05 audit** (every "32 ATP" on all 198 pages): four places used 32 with no shuttle stated and were fixed live: 14.7 Problem 14.13 (question now says liver / malate–aspartate; answer adds the 30 for glycerol-3-phosphate), 15.3 per-carbon check and 3-glucose solution, 15.12 hexanoate example, 14.4 respiratory note (now 30–32). Others already state the shuttle, give 30–32, or give 32 as a premise. Fatty-acid checks re-verified: laurate 78, palmitate 106, stearate 120 (2.5/1.5, −2 activation).
- **R04 done (live, 74 pages, 1,502 answers).** LibreTexts print CSS: `.hideprint` hidden in print, `.showprint` hidden on screen. Inline `<details>` answers get `hideprint`; each page ends with a print-only "Answers" list labelled by box title (fallback: first words of the question). Verified with a single-page Prince print of 5.7 (batch.libretexts.org/print/url=…): questions without answers on pp. 1–9, all 78 answers at the end. Generator: `tools/answerkey.js` (idempotent; regenerates the key from the inline answers). `build_pages.py` now runs it on every built page; `pages/*.html` updated.
- Note: LibreTexts strips HTML comments on save; the key is found as the last `<div class="showprint answer-key">` on the page.

## D01 (2026-11-11, live on all 15 chapter landing pages)
- Instructor choices: every numbered section is required reading; no time estimates until measured.
- "Your Route Through Chapter N" box at the top of each chapter page: prerequisites (one line), a 3-question readiness check with click-to-reveal answers (print: in the page's answer key), "Preparing for class" (read N.1 to the last numbered section, Try It questions as you go) and "Reviewing for an exam" (Chapter Guide → Practice Problems with reread-and-retry → Practice Games), plus "Your instructor decides which problems and how much homework are assigned each week."
- Content source: `tools/chapter_openers.json`. Section links are /@go/page/ ids taken from each chapter's subpages.

## PDF check, export compiled 2026-11-11 morning (1,424 pp.)
- ⯑: **0**. Hidden-label scan (chunked, `scan2` in pdf_hidden_scan style): only p.222 table false positive. R01/R02 verified.
- Chapter openers present (15).
- R04 problem: the **full-book compile does not apply LibreTexts' `.hideprint` rule** (single-page print does), so inline answers printed AND the key printed (+149 pp.). Fix: every keyed page now starts with its own `<style>` (`@media print { .hideprint, details.hideprint { display:none !important } }`, plus a screen rule hiding the key); LibreTexts keeps `<style>` in page bodies (CDATA-wrapped). Applied live to 89 pages (74 keyed + 15 chapter pages); `tools/answerkey.js` now emits it and stays idempotent after LibreTexts' CDATA wrapping. Needs a recompile to confirm; if the compile ignores page `<style>` too, fall back to removing the keys (tools/answerkey.js can strip).

## PDF check, export compiled 2026-11-11 ~10:50 (1,336 pp.)
- Page style worked for answers inside problem boxes (practice pages, chapter guides). 43 inline answers still printed: all "Think about it" / "Your turn" / "Practice" answers sitting loose in section text (pages that also carry LibreTexts' own exercise "Answers" list). The full compile appears to rewrite those <details> and the class is lost.
- Fix: every keyed answer is now also wrapped in `<div class="hideprint answer-inline">` (answerkey.js; unwrap-then-wrap so it is idempotent and never consumes a box's closing </div>). Applied live to 89 pages / 1,547 answers; all saves balanced. Online view unchanged. Needs one more compile to confirm 0 inline "Answer" lines.
- Export compiled 11/11 ~11:20 (1,336 pp.): ⯑ 0; hidden labels 0 (p.212 table false positive); still 43 inline answers on the same section pages, with page text identical to the previous export. Single-page print of 1.8 from batch.libretexts.org (live page) hides them correctly → the full compile reused cached renders for those pages. Recompile later to confirm.

## PDF check, export uploaded 2026-11-11 12:30 (1,336 pp.)
- ⯑ 0; inline answers still 43 on the same ~30 section pages (identical text to the 11:20 export) → LibreTexts reused cached renders. Ask LibreTexts to purge the compile cache for those pages (same message as R03). The 21 "Answer a: available at the end of this section" lines are the Ball print convention, not a defect.

## 2026-11-11 afternoon: version 1.1 — adapted text made our own (live, ~110 pages)
Instructor decision: edit source text in place wherever licenses allow (Ball/Fundamentals BY-NC-SA: edits allowed, pages stay NC-SA, changes noted; Malik CC0). Every edited page's footer now reads "The text was edited for CHEM 3B by Dr. Dan … (corrections, course conventions and scope, and wording)". 16 unedited adapted pages still say "reproduced unchanged" (accurate). About This Book adaptation log and Source Attributions intro rewritten accordingly.
- **All 87 "In this course" boxes removed** (0 left). Pattern: fix the source sentence, then delete the box or turn the remaining exam guidance into a Professor Tip with no "the source says" wording. All "the source text" mentions outside licensing removed.
- Source corrections in place: 1.5 water angle ~105°; 1.8 ionic/network not IMFs; 4.8 ether bp; 6.9 "high-energy bonds"; 8.3 glucose range; 10.10 70% alcohol disinfects (not sterilizes), **induce-vomiting advice removed → Poison Control**; 11.5 cofactor/coenzyme; 12.2 5′-GTAC-3′; **12.4 transcription directions**; 12.6 point mutation; 13.2 G6P not G1P, 7.3 kcal; **13.5 step 6 thiol is the enzyme's cysteine, not CoA**; 14.3 FADH→FADH2 (3); **15.11 Phe→Tyr is an oxidation**; 15.7 ketoacidosis.
- Old ATP convention replaced in tables/text: 13.4 (table → 30–32, efficiency 35%), 14.2 (table → 10 per acetyl CoA), 14.4 (efficiency 35%, 30–32), 14.1 (ATP per carbon 5.3 vs 6.6). C05 "ATP numbers" boxes no longer say "including the adapted text on this page".
- Out-of-scope source removed: 3.2 E/Z note; 4.5 ether-forming dehydration; 5.3 base/acid mechanisms + cyanohydrins + hydrates; 5.4 oxidation numbers, H2 mechanism, NaBH4/LiAlH4 mechanism, acid-derivative reductions; 5.5 conformers + mislabeled glyceraldehyde images and their apology tip; 6.10 Ka/Kb/pKb, factors (resonance/induction, incl. the 2.83 typo figure), Henderson–Hasselbalch; 10.8 coordinate bonds; 11.4 duplicate feedback-inhibition paragraph+figure; 14.4 Fo/F1 rotation/catalysis mechanisms and ROS; 13.5/14.3 mechanism wording rewritten at course level. Learning objectives rewritten on 5.3, 5.4, 5.5, 6.10, 15.11 (15.11 had placeholder "Objective 1/2").
- Editor artifact (red "Insert paragraph here" marker) removed from 11.4.
- New: Summary box on 31 sections that had none; Concept Map section in all 15 Chapter Guides (figures/conceptmaps/chNN.svg, tools/concept_maps.py); In the Lab boxes 13.3, 13.7, 15.7, 15.9 (no COR lab for Ch 14); Valley Connections 10.9 (nitrate/methemoglobinemia) and 11.5 (almonds/vitamin E); videos added to 1.3, 1.8, 5.4, 6.10, 7.3; print-only static copy of the Index (DynamicIndex is JS, so the PDF had no index); For Instructors page (597396); About This Book: error-reporting list, version history, v1.1 (also TitlePage).
- Readability: 8 long source sentences split (11.1, 11.2 ×2, 11.3, 11.5, 13.2, 13.4, 15.1).
- Not done / instructor's call: splitting 1.7 or 14.4 into two sections (would renumber and break @go/ADAPT links); a print-lite edition (Practice Problems pages ≈ 279 of 1,336 pp.); more videos for Ch 15 (no suitable ItsDrDan/Amoeba Sisters video exists); "lecture" wording in Lecture Connection blocks kept (means the CHEM 3B course; explained on For Instructors).
- Citrate synthase: instructor decided **ligase** (2026-11-11). Live book already consistent (14.3, 14.6, Glossary). Fixed repo copies: bank/metabolism.json fb-3B-2030 (answer was transferase → ligase), tools/new_questions_nov5.py, tools/glossary_terms.py, sections/add_597202.html, sections/back_glossary_488232.html. Final Boss repo (ItsDrDan/finalexam) checked 2026-11-11: it has no citrate synthase item, so nothing to change there. ADAPT updated in place 2026-11-11 (course 4605, "automatically update" for own assignments, reason recorded): fb-3B-2030 (ADAPT 355222, ligase) plus five reworded items that had not reached ADAPT: fb-3B-2019 (355205), 2025 (355197), 2034 (355224), 2052 (355239), 2054 (355238). Verified in the Ch 13/14/15 assignment views. adapt/*_nov5_QTI.zip rebuilt to match.
- Drafts in `drafts/` and `pages/` do NOT have today's section-page edits (section pages are not built from the repo; sync-libretexts.js only pushes Chapter Guides/Games and skips pages edited live after its cutoff). Live LibreTexts is the source of truth.

## Revision brief items D02–M03 (brief saved as tools/REVISION_BRIEF_2026-11-08.md) — status 2026-11-11

| ID | Status | What was done / what remains |
|---|---|---|
| D02 | corrected (live) | Conventions written into the adapted text itself (all 87 "In this course" boxes resolved, see v1.1 entry). Remaining: none beyond L06 maintenance. |
| D03 | partly reviewed | Rosa Clinical Updates already ask apply-the-chemistry questions with answers and "Where this chemistry is taught" links (Ch 13 checked in full; 15 g/15 min hypoglycemia rule correct). Not done: a recorded clinical-accuracy review of all 15 parts and all Valley Connections by a qualified reviewer (brief says this must be evidenced, not claimed). |
| D04 | corrected (live) | Scanned 176 absolute statements in Professor Tips and Check boxes. Qualified 5 that fail on a neighbouring case: 10.2 zwitterion "only at the pI", 10.1 side chains (Cys/Tyr at high pH), 6.5 "acids never have positional isomers", 1.1 "bonds + lone pairs always four" (full octet), 4.9 thiol oxidation (course scope). The rest are true in context. Section text outside tips not yet scanned. |
| D05 | already present | Every Practice Problems page has a Cumulative Review section and a cumulative Try It mix. |
| L01 | not started | Needs a per-skill inventory (worked → partly worked → independent → transfer). Multi-session job; best done together with the chapter audit matrix. |
| L02 | partly present | Representation translation taught in 1.7, 2.4, 8.4 (Fischer↔Haworth). Not done: a "same molecule or not?" exercise per relevant chapter. |
| L03 | corrected (live) | Every chapter readiness answer (44 of 45; Ch 11 Q1 is CHEM 3A) now ends "If you missed it, review Section N.M" with a direct link. Mapping stored in tools/chapter_openers.json ("review"). Not done: a fresh retry problem per prerequisite. |
| L04 | not started | Concerns game/widget progress labels (games repos, practice.html), not the book text. |
| L05 | added (live) | One "Find the Error" problem per chapter (Problems 1.78, 2.83, 3.78, 4.70, 5.73, 6.72, 7.77, 8.81, 9.73, 10.81, 11.77, 12.76, 13.68, 14.67, 15.69) on the misconceptions the brief names (polar bond vs molecule, ester name swap, gross vs net ATP, pI vs side-chain pKa, etc.). Print keys regenerated (each +1). |
| L06 | documented | tools/CONVENTIONS.md: each convention, where it is taught, everything that depends on it. Duplicate-prose consolidation between sections and guides not yet audited. |
| L07 | partly present | Every video has a "Watch it on YouTube" fallback; every Try It iframe has "Open in a new tab"; print/PDF keeps all text, problems and answers. Not done: transcripts for essential videos; offline test of a downloaded chapter. |
| L08 | partly done | Placeholder objectives fixed (15.11); long sentences split in Ch 11/13/15. Not done: abbreviation-at-first-use audit. Spanish (decided 2026-11-11 by Dr. Dan): keep the Spanish equivalents for glossary terms only; no Spanish sentences or passages anywhere in the book (risk of mistranslation). Live scan of all 199 pages, 11-11: Spanish appears only on the Glossary (488232), 330 term equivalents (longest 76 characters, all terms) plus the label in the intro; no passages. No bilingual review planned. |
| M01 | started | Coverage so far: adapted section text reviewed for conventions/scope on all 110 adapted pages (text extraction + targeted reading, not line-by-line); 15 Chapter Guides structure-checked; Practice Problems answers independently re-solved: only those touched in C01–C08 and the 15 new items. The chapter audit matrix (1,108+ problems, independent solutions) remains the main open job. |
| M02 | in place | Stable page ids and @go links kept (no sections split or renumbered); new problems appended with new numbers; version history + errata list in About This Book (v1.1). |
| M03 | defined | Release gate per chapter: (1) figures render in the latest PDF (✓ all chapters, 11-11 export); (2) assessed answer keys independently checked (✗ pending audit matrix); (3) learning route complete: opener → sections → summary → guide → problems (✓); (4) essential content available in print and online (✓ except 43 cached inline answers pending LibreTexts). Chapters are therefore "ready except gate 2". |
| answerkey.js | fixed | Old-key removal now cuts only the key block (LibreTexts adds wrapper closings after it, which the old regex deleted). |

## 2026-11-11 evening: ADAPT course 4605 updated in place
Edited in the ADAPT question editor ("Automatically update the question" for own assignments, reason recorded on each), matching the bank and the adapt/ export files:
- fb-3B-0063 (ADAPT 354321, Ch 5): "the S form of ibuprofen" → "ibuprofen" (no R/S).
- fb-3B-0192 (ADAPT 354486, Ch 10): feedback adds Arg as the conditionally essential tenth.
- fb-3B-0884 (ADAPT 355079, Ch 11): feedback says "allosteric regulation", not "allosteric (noncompetitive) regulation".
- fb-3B-0895 (ADAPT 355090, Ch 11): answer is "Irreversible (noncompetitive) inhibition … permanently changes the enzyme's shape"; distractor "Noncompetitive inhibition" → "Reversible inhibition"; feedback explains heavy metals are also noncompetitive.
Verified in My Questions and in the Ch 5/10/11 assignment views; correct answers unchanged. fb-3B-0396 is not in the ADAPT course.

## 2026-11-11 late: instructor decisions applied
- **Question bank license: CC BY 4.0** (LICENSE.md, README, adapt/README.md; Final Boss LICENSE has a CC BY 4.0 carve-out for the CHEM 3B questions, game still all rights reserved).
- **Per-choice explanations (b2e68a8): approved** by the instructor ("all of them good").
- **Scope:** "major product" and resonance-counting items stay. **Meso compounds removed:** fb-3B-0778, 0779, 0787, 0790, 0804–0809, 0811, 0812 deleted from bank/ (now 1,045), the ADAPT export files and Final Boss (v38). Meso wording taken out of 0402, 0777, 0782, 0810, 0813 (bank, exports, Final Boss, and the ADAPT course). **Still to do in ADAPT (instructor):** remove the 12 from "CHEM 3B Chapter 5" (assignment 223786; ADAPT ids 354867, 354868, 354876, 354878, 354891–354896, 354898, 354899). Removal was blocked for the assistant.
- **9.3 lipids (597146):** the four glycerophospholipid images (from Malik's book) no longer loaded on LibreTexts. Redrawn with RDKit (POPC, POPE, POPS, POPI), uploaded to the page (files 512693–512696), figure now credited "Structures drawn by Daniel Kwasniewski; CC BY 4.0." Repo copies match live (SHA-256).

## 2026-11-11 night: Practice Problems answer check (M01, all chapters)
All 1,231 questions on the 15 Practice Problems pages (1,123 numbered, 84 Cumulative, 24 Case Set) were re-solved independently and compared with the book's answers. **No wrong answer key.** Inline answers and answer keys agree everywhere. 24 explanation, option-wording, table or alt-text issues were found and fixed on LibreTexts (13 pages, 39 replacements, listed in `tools/practice_problem_fixes_2026-11-11.json`; the findings, with reasons, are in `tools/PRACTICE_PROBLEMS_CHECK_2026-11-11.md`). Repo copies match live (SHA-256). Generators (`tools/cumulative.py`, `sections/boardsets/boardsets.json`) and `drafts/` carry the same fixes. Not changed: section 1.5 (597058) also says an OH carries "about four or five carbons" into water.

## 2026-11-11 late night: PDF recheck follow-ups
- Recompiled PDF (Full (2).pdf, 1,350 pp, 18:59) checked: the title page carries the CC BY statement; credit lines read Daniel Kwasniewski (only "Dr. Dan's Chemistry Study Hub" remains, by decision); no nine-essential, tyrosine, Table 4.5.x or meso text; Figure 4.2.1 prints; the hidden-label scan is clean (only the known alkene-table false positive). It predates the Practice Problems fixes.
- 1.5 (597058): the rule of thumb now reads "about four carbons" for an O–H (Chapter 4), and about five for –COOH (Chapter 6), matching CONVENTIONS.md.
- 9.3 (597146): the lipid drawings printed four across and were illegible. They were re-rendered tight with no built-in label (file revision 2) and laid out two per row.
- Open (instructor): the conformations scope. Sections 1.7, 2.3, 2.9, 2.10 and 5.5 use "conformation" or "chair"; Problems 2.60/2.64 had those words removed on 2026-11-11.
## 2026-11-11 late night: GOB-scope pass (instructor: no Newman projections or chair flips; avoid majors-level content)
Whole-book scan: no Newman/staggered/eclipsed, axial/equatorial or ring-flip content. The 2.9/2.10 chair mention is an example ("folds into a chair"), which the instructor allows. "Conformation" is used only as "same molecule, not an isomer" (GOB level), so Problem 2.64's "conformations" is restored. Rewritten on LibreTexts (12 pages, 22 replacements; `tools/gob_scope_fixes_2026-11-11.json`):
- 15.3 (597209): SN2, nucleophile/electrophile/leaving group and resonance language in fatty-acid activation, hydration, thiolysis and glycerol phosphorylation, replaced with plain steps.
- 13.1 (597188): the citrate synthase step-by-step (Asp375/His274/His320, enol, nucleophilic attack) is cut to a one-sentence summary; the malate dehydrogenase example is simplified (no "hydride"); the enzyme-factor list now talks about charge pairing and H⁺ transfer; "good leaving group" for acetyl CoA is replaced.
- 5.3 (597104): the base/acid "mechanisms described next" framing is removed. 5.4 (597105): the incorrect "alkene is an electrophile … H–H not a nucleophile" is replaced.
- 10.1 (597154): Cahn–Ingold–Prelog/R/S sentence → "all chiral amino acids in human proteins are L". 14.3 (597202): (S)/(R)-malate → L-malate.
- 7.6/7.12 (597126/597132): "nucleophilic acyl substitution" dropped. 1.7 (597060): "sp³ hybridized C" → "tetrahedral C". 13.8 (597196): "good leaving group" → activated UDP-glucose wording. 8.5 (597138): "tautomerism" → plain description.
Kept: the name "nucleophilic addition" in 5.3 (it's the section's reaction name), the KMnO₄/NaBH₄ lab and reduction reagents, the pentose phosphate pathway, the Cori cycle, cAMP, and "transition state" in enzyme catalysis.

## 2026-11-11 night: PDF check of the 19:51 compile, and GOB-scope leftovers
- Checked the 19:51 compile (Full (3).pdf, now `CHEM3B-Full.pdf`, 1,349 pp; the 18:59 one is `CHEM3B-Full-2026-11-11-1859.pdf`). All 39 Practice Problems replacements and all 22 GOB-scope replacements print (2.60 no longer says "chair"); 9.3 Figure 9.3.2 prints two per row and is legible; 1.5 reads "about four carbons". Whole-book checks pass: CC BY statement on p2, every "Dr. Dan" is the Study Hub name, no raw MathJax, figure count unchanged (892; 13.1 is one page shorter), hidden-label scan flags only p224 (known).
- The scan found GOB-scope leftovers outside the fixed pages. Fixed on LibreTexts (5 pages, 7 replacements; `tools/gob_leftover_fixes_2026-11-11.json`):
  - 1.8 (597061): Professor Tip said an O–H/N–H carries "roughly four or five carbons"; now about four, and about five for –COOH (CONVENTIONS.md, matches 1.5).
  - 5.4 (597105): "The mechanism with Jones reagent is shown below" and its curved-arrow image (file 443557) removed and replaced by a plain statement (the agent removes the O–H H and the C–H H; C=O forms); "step#4 of the mechanism" (ketones, tertiary alcohols) reworded as "no hydrogen left to remove".
  - 6.10 (597118): the terminal-alkyne/NaNH₂ and NaH (hydride as base) passages removed; the alcohol + OH⁻ equilibrium is kept, with one sentence: alcohols stay as neutral R–OH in water and the body.
  - 8.5 (597138): "(called tautomerization)" removed: "fructose rearranges into an aldose".
  - 15.3 (597209): "Resonance stabilization … lowering the activation energy" sentence in β-oxidation reaction 1 removed.
- Repo copies (`pages/live/`, `pages/sec_*.html`, `sections/`) updated; live SHA-256 matches `pages/live/` for all five. `drafts/` has none of these strings.
- Open (instructor): 3.7 "electrophilic aromatic substitution"/"electrophile" wording, explained plainly and marked "mechanism not needed"; left as is pending a decision.

## 2026-11-11 night: GOB-scope leftovers, round 2
Fixed on LibreTexts (5 pages, 14 replacements; `tools/gob_leftover_fixes_2_2026-11-11.json`):
- 3.7 (597084) and Ch 3 Guide (597086): the "electrophile (electron-lover)" definition and "stronger electrophile" sentences are now "reactive enough". The reaction name "electrophilic aromatic substitution" is kept (instructor decision, same as "nucleophilic addition" in 5.3).
- 13.5 (597193): "reaction#5/step#1/reactions#1 to 5" typos → "reaction 5", etc.; the phosphoglycerate mutase detail (via position 2 then 3) → "moves the phosphate group from carbon 3 to carbon 2".
- 14.3 (597202): "by the same mechanism as in steps #7 and step#10" → "in the same way as in steps 7 and 10"; "#" typos fixed; **wrong cross-reference "glycolysis (Section 13.6)" → 13.5**; **"only one reaction in this book makes FADH2 (CAC reaction 6)" was wrong (β-oxidation step 1, 15.3, also does) and now names both**.
- 14.4 (597203): semiubiquinone "resonance-stabilized radical anion" → "can also carry just one electron at a time".
- Repo copies (`pages/live/`, `pages/sec_*.html`, `pages/ch03_guide.html`, `sections/`, `drafts/Ch03_…Guide`) updated; live SHA-256 matches `pages/live/` for all five.
- Removed untracked `figures/CREDITS 2.md` (identical copy of CREDITS.md) and `PR_DESCRIPTION.md` (old PR #1 text).
- 9.3 (597146) image credits checked against the source, Malik 6.4: Malik gives no credit for three images either. Two are plain structure drawings (lysophospholipid, phosphatidic acid), probably Malik's own (his book is CC0). The labeled POPC space-filling model ("Choline / Phosphate / Glycerol / Palmitic acid / Oleic acid", file 435596) has no known source; it is not Commons "Phospholipid TvanBrussel" or "POPC labeled.svg". Open: credit or redraw.
## 2026-11-11 night: pKa removed (instructor decision: GOB course does not discuss pKa)
Published on LibreTexts (18 pages, 117 replacements; `tools/pka_removal_fixes_2026-11-11.json`, built by `tools/pka_removal_2026-11-11.py`; review sheet `Study Games/PKA-REMOVAL-REVIEW-2026-11-11.html`, approved before publishing). Every page re-read after saving; live SHA-256 matches `pages/live/` for all 18.
- New rule (CONVENTIONS.md): acid strength is a ranking, carboxylic acid > phenol ≈ thiol > alcohol ≈ water, shown by NaHCO3 (carboxylic acids only) and NaOH (also phenols, thiols). At body pH, –COOH → –COO⁻ and amines → –NH3⁺; phenols and alcohols stay neutral; in strong acid, –COOH keeps its H. Side-chain charge goes by category (Asp/Glu −, Lys/Arg +, His mostly neutral). The old "compare pH with side-chain pKa" convention is retired.
- 4.10 (597099): Ka/pKa/−log review, pKa column, "pKa about 12" dividing line, pKa-scale figure (file 512463, old Figure 4.10.2; the NaOH-test figure is now 4.10.2), Professor Tip, examples, clinical box, summary and Exercises 1/3/5/8 rewritten as rankings; Exercise 1 is a new ranking question.
- 6.10 (597118): LO, pKa section and table, pKa labels under all equations, "pH minus pKa" Professor Tip, salicylate/lactate box, summary; also removed the Malik passage on protonating alcohols/carbonyls with HCl/H2SO4 and "intermediates in organic reactions" (majors-level). Try It query no longer filters on "pK".
- 6.12 (597120): Problem 6.55 rewritten (NaHCO3 fizz, ionized at 7.4, salicylic acid's phenol –OH); lactate nursing problem and acetic acid problem no longer use pKa.
- Ch 10: 10.1 (597154) histidine row and threonine worked example; 10.12 (597165) answers by category; **Find-the-Error 10.81 replaced** (now: Ala-Lys-Gly net charge at 7.4 is +1, not 0); Ch 10 opener answers (597048).
- One-line mentions removed: 4.7, 4.9, 4.11, 4.12, 6.4, 6.11 (and concept-map alt), 13.4, 14.7. Glossary row and index entry removed. About This Book and For Instructors scope notes now name pKa as not covered.
- Repo: Ch 6 concept map label "weak acids: pKa ≈ 4–5" → "weak acids: RCOO⁻ in body" (svg edited directly; generator updated; node not available here). Copies synced in `pages/`, `sections/`, `drafts/`.
- Already pKa-free: question bank, Final Boss 3B items. Open: the ADAPT export list (`adapt/CHEM3B_ADAPT_question_list.csv`) still shows fb-3B-0078 with "pKa of about 3.9"; live ADAPT not checked. Also noted: `pages/live/597396 2.html` is a tracked Finder duplicate (left untouched).

## 2026-11-11 night: PDF check of the 21:28 compile, and the last pKa traces
- Checked the 21:28 compile (Full (4).pdf, now `CHEM3B-Full.pdf`, 1,347 pp; the 19:51 one is `CHEM3B-Full-2026-11-11-1951.pdf`). Everything from PRs #6–#8 prints (4.10 ranking table p345, 6.10 table p498, Ch 10 answers p774/p857, FADH2 sentence p1166, scope note p21). Whole-book checks pass: p2 license, no stray "Dr. Dan", no raw MathJax, hidden-label scan only p224 (known), 891 figures (the 4.10 pKa-scale figure was removed on purpose).
- Last pKa traces fixed on LibreTexts:
  - Figure 4.10.1 (file 512462, now revision 3): the drawing's "weak acid, pKa ≈ 10" label → "weak acid". The SVG is now kept in the repo at `figures/pages/fig-p597099-1.svg`.
  - 6.10 (597118): page tag "pKa" removed (it fed the back-of-book Index). It was the only pKa-related tag in all 199 pages; the other four tags are kept.
  - 10.11 (597164) Example 1 check: "(around pH 2) … (around pH 9–10)" → "in fairly acidic solution … only in basic solution" (`tools/pka_traces_fixes_2026-11-11.json`). Live SHA-256 matches `pages/live/`; `pages/ch10_guide.html` and the draft are updated.

## 2026-11-11 — Fresh-eyes alignment review, Tiers 1, 2 and 5 (PR audit/2026-11-fresh-eyes-fixes)
- Six independent reviewers checked the book and bank/ADAPT against the COR; the report is `tools/FRESH-EYES-ALIGNMENT-REVIEW-2026-11-11.md`. The instructor approved fixing Tiers 1 (wrong facts), 2 (convention contradictions) and 5 (front matter/alignment page).
- Published on LibreTexts: 157 surgical edits on 65 pages (`tools/fresh_eyes_fixes_2026-11-11.json`; per-chapter rationale in `tools/fresh_eyes_notes/`). Live SHA-256 for all 65 pages matches `pages/live/`; the same edits are mirrored into `pages/*.html` and `sections/`.
- Highlights: ten essential amino acids (10.11); arachidonic acid formula (9.1); galactosemia diet lifelong (8.6); 65% not conserved (13.4); electron flow toward higher reduction potential (14.4); methanol → formate, fomepizole (4.4, 5.4); 5.5 isomer chart (had meso, R/S, Newman, swapped E/Z) replaced by an HTML list and cis–trans no longer called diastereomers; alcohol disinfects, prions separated from other misfolding diseases (10.10); infant RDS/DPPC (9.3); penicillin box, diabetes box, mRNA-vaccine reasoning modernized; citrate synthase exception, feedback inhibition ≠ noncompetitive, "point mutation" titles, heavy metals both, ester bp rule, lipase products, glycogen timing/branching, 35% efficiency (14.5 now uses 670 kcal); pKa-style pH 2/9–10 reasoning removed from 10.2; alt text fixed where it named the wrong molecule (2.5, 2.8, 7.1, 8.6).
- Front matter: About This Book and For Instructors now describe ADAPT as live and part of the study route; For Instructors lists the E/Z, meso, Newman/chair and conformation rules; Alignment page rows corrected (1.3, 2.6, 3.3, 4.1, 7.5, 9.3, 10.1, 11.3) and a COR 17.5 row added. Reactions-at-a-Glance rows added in 3.9, 4.11, 5.6; LOs added in 5.5 and 8.4; "nucleophilic acyl substitution" named once in 7.6.
- Images: 2.5 Ex 2a/2b redrawn (new files 512698, 512699; old ones showed an isopropyl group); 15.3 activation image without curved arrows (file 512700); 10.6 curved-arrow resonance image removed; 3.8 ibuprofen now uses the correct isobutyl drawing (file 512427).
- Open (not in these tiers): Tier 3 clinical-currency rewrites, Tier 4 restructuring (Ch 15 order, Ch 13–14/12 duplication, 7.8/10.3 copies), Tier 6 ADAPT rebalance; duplicate "Figure 5.5.3" labels in 5.5; penicillin image still shows methicillin; 8.6 Exercise 1 image shows β,β (alt now matches); lab experiment numbers vs For Instructors (instructor decision); Bond Voyage drawings for the new Reactions-at-a-Glance rows.
- Checked the 23:44 compile (Full (6).pdf, now `CHEM3B-Full.pdf`, 1,347 pp; the 22:33 one is `CHEM3B-Full-2026-11-11-2233.pdf`). The fresh-eyes Tier 1/2/5 text prints (118 distinctive new phrases checked; the only ones not in print are alt text and inline answers marked hideprint). None of the old wording remains ("Nine are essential" on p1280 is 15.11's intended nine-plus-arginine sentence). Visually checked: 2.5 Ex 2a/2b redraws (p170), 5.5 isomer list (p415), 15.3 activation figure without arrows (p1230). Whole-book checks pass: CC BY statement on p2, every "Dr. Dan" is the Study Hub name, no raw MathJax, hidden-label scan only p224 (known), images 2,234 vs 2,238 (−4 as expected: 5.5 Figure 1, 10.6 resonance image, 1.6 MyPyramid image, 3.8 ibuprofen JPEG → SVG).

## 2026-11-12 — Fresh-eyes Tiers 3, 4, 6 and leftovers (PR audit/2026-11-fresh-eyes-tiers-3-4-6)
- **Book: 332 edits on 108 live pages.** Edit list: `tools/fresh_eyes_round2_fixes_2026-11-12.json`. Per-chapter notes: `tools/fresh_eyes_notes/round2/`. All 108 pages match `pages/live/` by SHA-256; LibreTexts renumbered section ids on 597180, 597200 and 597232, and the repo copies carry that.
  - **Tier 3, clinical currency:**
    - HIV in 12.7 now covers integrase-based single-pill regimens, PrEP and U=U, with person-first wording.
    - 12.8 covers CRISPR/Casgevy, STR profiling, and corrected flu vaccine, Bt and chymosin facts.
    - PKU and CF are updated (F508del, CFTR modulators).
    - Lipid panels are no longer described as always fasting (9.6, 9.7, 9.8, 15.6).
    - 9.6 Ball text is updated; it now uses "gender-affirming hormone therapy".
    - Prediabetes is named (8.3, 8.4, 8.8). GLP-1 and SGLT2 notes are added in 13.7, and euglycemic DKA in 15.7.
    - Osmosis and IV fluids are added in 9.5.
    - Anesthetics (4.8), nicotine dose and pediatric e-liquid risk (7.3), and formaldehyde "known carcinogen" (5.2) are updated.
    - Breathalyzer (4.5, 5.4), CO pulse-oximetry pitfall (2.7), HCFC/HFC/HFO (2.8), and California lead sources (11.4) are updated.
    - Lactase non-persistence (11.7) and the organophosphate Valley Connection (7.11; please confirm the 3 CCR §6728 citation) are added.
    - Career boxes are modernized.
  - **Tier 4, in-page structure:**
    - Duplicated source text is replaced or trimmed: 7.8, 10.3, 9.5, 10.6, 14.1, 14.2, 13.4, and Ch 12 (12.3, 12.9).
    - Majors-level text is trimmed: 14.4 ETC, 15.8/15.11, 5.4 Jones/hydrates, 6.2 acid reduction (P6.63–6.64 rewritten), 1.7 hybridization, 11.4/11.5 Ball tables, 13.6.
    - Missing exercise answers are added (2.5, 2.8, 3.1, 3.2, 3.8, 8.1, 8.2, 8.6, 10.2, 12.2, 12.3, 12.5).
    - Alt text that gave away answers is fixed.
    - 5.5 figure numbers are unique.
    - Broken and off-book links are repointed.
    - 4-4-9 food energy is added to 14.5.
    - Organic Origins and Flashcards are added to the 1.11 games page.
- **Images:**
  - 12.2 Exercise 2 guanine now has its NH2 (file 512701).
  - 12.5 tRNA charging now shows ATP → AMP + PPi instead of H2O (file 512702).
  - 8.6 Exercise 1: the drawing shows β,β, which is correct; the answer is added and the alt text no longer gives it away.
  - The penicillin caption now explains methicillin.
- **Tier 6, question bank and ADAPT:**
  - Bank now holds 1,110 items:
    - 65 new: fb-3B-2061–2125.
    - 13 rewritten: 0161, 0199, 0237–0239, 0246, 0445, 0641, 0914–0917, 0926.
  - ADAPT course 4605 is updated live; see `adapt/README.md` (2026-11-12): 100 added, 13 updated in place, 2 moved, 32 removed; 1,031 questions now.
  - `tools/adapt_export.py` no longer imports `build_pages`, so it cannot rebuild pages from the stale drafts, and it places orphans explicitly.
  - Final Boss v40 (ItsDrDan/finalexam 117d327) has the same 13 rewrites and 65 new items.
- **Open:**
  - Page moves and retitles: the Ch 15 lipid/protein order, 13.7 after 13.9, 12.9 after 12.2/12.4, and retitles of 13.6 (PPP), 5.3, 14.1, 14.2, 12.3. The plan, with cross-reference counts, is in `tools/fresh_eyes_notes/round2/ch13-15-notes.md`.
  - Lab experiment numbers wait for the final lab manual.
  - The 5.4 image still says "CrO3 + H2SO4".
  - Image files no longer used on their pages could be deleted (listed in the round 2 notes).
  - Video hints for the new ADAPT questions.

## 2026-11-12 — Section moves and video hints (PR audit/2026-11-section-moves-hints)
- **Checked the 00:50 compile.** It is Full (7).pdf, now `CHEM3B-Full.pdf` (1,327 pp); the 23:44 compile is `CHEM3B-Full-2026-11-11-2344.pdf`.
  - All round-2 (Tier 3/4) text prints; the only misses are alt text and hideprint answers.
  - p2 license present; every "Dr. Dan" is the Study Hub name; no raw MathJax.
  - Hidden-label scan flags only p224 (known).
  - Images: 2,179, down from 2,234 because the duplicated Ball figures were removed.
- **Moves on LibreTexts.** Page ids are unchanged, so every /@go/page link still works. Titles and paths were set through the deki move API, and the sibling order through `PUT pages/{id}/order?afterid=`, which drives the prev/next arrows. No redirect stubs appear in the chapter listings.
  - **Ch 12:** RNA structure moved up. 12.9 → 12.5; 12.5–12.8 → 12.6–12.9. 12.3 is retitled "DNA Replication".
  - **Ch 13:** 13.8 → 13.7 and 13.9 → 13.8. Regulation (old 13.7) → 13.9, the capstone. 13.6 is retitled "Other Sugars and the Pentose Phosphate Pathway".
  - **Ch 15, lipid block:**
    - 15.1 Digestion of Lipids and Lipoprotein Transport (old 15.5). The "Digesting fats" lecture block and its figure moved here from old 15.1.
    - 15.2 Storage/Mobilization (old 15.6).
    - 15.3 Activation and Transport (old 15.1).
    - 15.4 β-oxidation (old 15.3).
    - 15.5 Ketone bodies (old 15.7).
    - 15.6 Lipogenesis (old 15.8).
  - **Ch 15, protein block:**
    - 15.7 Protein digestion (old 15.9).
    - 15.8 Transamination/Deamination (old 15.2).
    - 15.9 Urea cycle (old 15.10).
    - 15.10 Carbon skeletons (old 15.4).
    - 15.11 is unchanged.
  - **5.3** is retitled "Adding Alcohols to Aldehydes and Ketones- Hemiacetals and Acetals".
- **Cross-references: 312 edits on 44 pages** (`tools/section_moves_2026-11-12.json`).
  - What changed: "Section N" text, link text and titles, hard-coded figure labels on moved pages, Chapter Guides, Index, Glossary, Course Outline Alignment, Source Attributions, About and chapter landing pages. Pre-existing wrong Index/Glossary pointers were also fixed.
  - What was kept: Practice Problem, Cumulative and Case numbers, Ball/LibreTexts source numbering, and data values. The keep log has 204 entries.
  - The bank, ADAPT and Final Boss contain no section references, so they needed no changes.
  - SHA-256 of all 44 pages matches `pages/live/`. LibreTexts normalized 597207 (section ids) and 597211 (one closing tag); the repo copies reproduce that. The edits are mirrored into `pages/*.html` and `sections/`.
  - CONVENTIONS.md and LIVE_SNAPSHOT.md are updated.
- **ADAPT video hints.** 38 of the 100 new questions now carry Dr. Dan's lesson video with a start time and jump links (`tools/adapt_hints_new_2026_11_12.py`, `adapt/adapt_new_hints_2026-11-12.json`). Matches were reviewed by hand: 5 skipped, 1 corrected. The other 62 have no matching lesson video.
  - A scan of all 1,031 questions found 8 hints with a doubled "Hint" heading, from the 2026-11-12 PATCHes; all 8 are repaired. Lesson learned: send the hint without ADAPT's mt-section wrapper, because ADAPT adds it on save.
- 2026-11-12 (later): **Video hints, pass 2.**
  - For the 62 new ADAPT questions the keyword rules missed, I searched the lesson transcripts (ItsDrDan/games `data/transcripts.json`) and checked each candidate by hand.
  - 23 questions now get a lesson video, starting at the matching chapter marker. Examples:
    - "how to name benzene as a substituent" (ethers video, 9:02) for phenyl naming;
    - the bicarbonate/CO2 part of Properties of Acids and Bases (15:28) for the NaHCO3 tests;
    - "like dissolves like" (Solubility, 5:29) for the vitamin E and phenol solubility questions;
    - combustion (Types of Chemical Reactions, 12:01) for incomplete combustion and CO.
  - Running total: 61 of the 101 new questions have a video hint. The other 40 have no lesson that teaches their topic (eicosanoids, recombinant DNA, PCR, zymogens, the A1C/lactose context items, amino acid codes). They keep their text hint.
  - Tool: `tools/adapt_hints_new_2026_11_12.py` (MANUAL map). Data: `adapt/adapt_new_hints_2026-11-12_pass2.json`. That tool/data commit ("ADAPT hints pass 2") went straight to main by mistake; this PR only adds the ledger entry.
- 2026-11-12 (01:23 compile checked; Full (8).pdf, now `CHEM3B-Full.pdf`, 1,327 pp; the 00:50 one is `CHEM3B-Full-2026-11-12-0050.pdf`). This is the first compile with the section moves.
  - **Print order is correct** in the table of contents, the chapter listings and the bodies:
    - 12.5 RNA is at p960 and 12.9 genetic engineering at p986.
    - 13.7/13.8/13.9 are at p1075/1083/1092.
    - Ch 15 runs 15.1 digestion and lipoproteins (p1203) through 15.6 lipogenesis, then 15.7 protein digestion (p1240) through 15.11.
    - 5.3 prints its new title.
  - **15.1 (pp1204–1205) checked visually:** Figure 15.1.1 is the lipoprotein classes, then "Digesting fats" with Figure 15.1.2, then "Delivery and storage". Its cross-references read 15.4, 15.2 and 15.6.
  - **Hard-coded figure labels follow the new numbers:** 12.5.1, 13.7.1, 13.9.1, 15.2.1, 15.4.1, 15.10.1.
  - **Old titles appear only in "Adapted from" credits** (source-book titles).
  - **Whole-book checks pass:** p2 license; "Dr. Dan" only in the Study Hub name; no raw MathJax; hidden-label scan flags only p224; 2,179 images (unchanged).

## 2026-11-12 — Polish batch (PR audit/2026-11-polish)
- **Live: 85 edits on 46 pages.** Edit list: `tools/polish_fixes_2026-11-12.json`. Notes: `tools/polish_notes/`.
  - All 46 pages match `pages/live/` by SHA-256. LibreTexts normalized 597193 (section ids) and the 10 answer-key pages (it moved the closing tags after the key); the repo copies reproduce that.
  - The same edits are mirrored into `pages/*.html`, `sections/` and the `pages/ch*_games.html` copies.
- **Chapter Guides 12.10, 13.10 and 15.12:** Key Ideas are reordered to follow the moved sections. Ch 15 is now a lipid block, then a protein block, and its Common Mistakes are reordered to match. Numbered exercises and examples keep their order, so the answer keys still match.
- **Rosa story copies:** Parts 2–15 in the Chapter Guides are replaced by a link to the chapter opening page plus a one-line recap of the facts the Case Questions use (same pattern as Part 1). The 14 guide copies were checked first and matched the landing pages.
- **Ch 13–14 duplication:**
  - 13.4 keeps the fates of pyruvate. The 13.5 copy is now a pointer, and its unique items (the link-reaction video, yeast fermentation diagrams, oxygen debt) moved to 13.4.
  - 14.4's insulin box is removed (13.9 covers insulin).
  - 14.4's duplicate 32-ATP table is now a pointer to 14.5.
  - Figure numbering gaps and clashes are fixed in 13.4, 14.1, 14.2, 14.4, 9.5 and 12.3.
  - Remaining overlaps are listed in `tools/polish_notes/metab-notes.md`.
- **New drawn reaction examples:** 3.9 (polymerization, bromination, nitration, sulfonation), 4.11 (hydration, combustion of ethanol, thiol → disulfide) and 5.6 (acetal hydrolysis). RDKit SVGs, files 512703–512710, with alt text and captions.
- **Image fixes:**
  - 5.4 oxidation figure now shows [O] instead of CrO3 + H2SO4 (file 512711).
  - The 2.10 combustion SVGs' aria-label is complete (files 512433/512435, revision 2).
  - The 7.1 Exercise 3 alt text no longer says "(ortho)".
- **R04, answers printing under questions:** the 17 source-text exercise answers (`<dl>` Answer blocks on 1.1, 1.3, 1.5, 1.8, 2.5, 2.8, 3.1, 3.2, 3.8 and 6.9) are now hideprint toggles on the web. In print they appear in a "Answers to Exercises" key at the end of each page. All 1,569 other answer toggles were already hideprint.
- **Practice Games pages 1.11–12.12:** "Every short practice set" → "Selected short practice sets". Each games page links 2 sets; the chapters have 3–8.
- **About This Book:**
  - New paragraph for students who work, care for family or are learning English: short sessions, Key Ideas first, the Glossary's Spanish equivalents, translated captions, browser read-aloud and translate.
  - The Valley Connection list now includes 7.11.
- **Checks:**
  - The 7.11 citation 3 CCR §6728 is confirmed: "Medical Supervision", with baseline and periodic red-cell and plasma cholinesterase testing for organophosphate/carbamate handlers.
  - axe-core 4.10 over all 199 page bodies: 0 WCAG 2.1 A/AA violations. Best-practice rules flag only one h2→h4 jump (597079 Example box) and two bold "Solution" labels (597060); these were left as they are.
- **Cleanup:**
  - Removed the Finder duplicates `pages/live/597396 2.html` and `drafts/README 2.md`.
  - `drafts/` is kept, because README, LICENSE and `tools/answerkey.js` refer to it.
  - Three unused figures on LibreTexts could not be deleted (the deletion was blocked by the assistant's permission settings), so the instructor needs to remove them: fig-p597099-2.svg (512463, pKa scale), glycine_vs_acetic_acid_pKa.svg (512663) and fig-p597203-1.svg (512622).
- **Needs the instructor:** page 597203 (14.4) has 15 unreferenced attachments that look like contract and licensing documents. They are SCFT contract, SCCCD AR3710 and CC compatibility chart scans (files 512635–512649). Check them and remove them if they were uploaded by mistake.
- 2026-11-12, attachment cleanup on LibreTexts (instructor request). Deleted 18 unreferenced files; LibreTexts keeps deleted files in its archive.
  - From 14.4 (597203): 9 SCFT contract and SCCCD AR3710 scans (512635–512639, 512641–512643, 512645) and 6 CC remix / adapter license charts (512640, 512644, 512646–512649). These were uploaded there by mistake.
  - Unused figures: 512622 (14.4), 512463 (4.10 pKa scale) and 512663 (6.10 pKa comparison).
  - Verified after deletion: 597203 and 597118 keep only their page thumbnails, and 597099 keeps its two figures still in use.
- 2026-11-12, print layout: video boxes and figure wrap.
  - **Finding:** the LibreTexts PDF service (downloads.libretexts.org, Prince) ignores a page's own `<style>` block and the legacy `hideprint` / `rightfig` classes; it honours inline styles and shows `.showprint`. Print-only CSS in the page therefore has no effect. Tested on 1.8 (597061) with single-page compiles.
  - **Video boxes:** the wrapper around each YouTube iframe changed from `height:0px;position:relative;padding-bottom:56.25%` to `position:relative;aspect-ratio:16/9` on 46 pages (64 videos; 60 in the compact form, 4 in the spaced form on 597179, 597200, 597201). The printed "YouTube Video" QR box drops from about 298 pt to about 93 pt tall, QR code intact; on screen the players are unchanged (640×360 desktop, 330×186 phone). Verified by compiling 597061, 597105 and 597200.
  - **Figure wrap (trial, 1.8 only):** Figure 1.8.9 is `<figure class="wrap-right" style="float:right;width:36%;margin:0 0 8px 16px">`, with a screen-only `@media (max-width: 640px)` rule in the page style block that removes the float on phones. Prints with text beside it.
  - **Repo:** `pages/live` matches live for all 46 pages (SHA-256); `pages/`, `sections/`, `drafts/` and `tools/videos.py` carry the same wrapper. The ADAPT hint generators were left as they are (hints are not printed).
  - **Not changed:** nine plain `<iframe width="560" height="315">` embeds (597062, 597074, 597141, 597192, 597193, 597202, 597209).
- 2026-11-12, batch A of the 2026-11-12 review: wrong content in text (branch content/2026-11-batchA).
  - **Live: 96 edits on 61 pages.** Edit list: `tools/batchA_content_fixes_2026-11-12.json`, built and count-checked by `tools/batchA_build.py`. Before/after sheet: `tools/BATCH_A_REVIEW_2026-11-12.md`.
  - **Verified:** a dry run against the live book found every old string at the expected count. After publishing, every new string is present and no old string remains. All 61 `pages/live` copies match live by SHA-256.
  - **Fixed:**
    - 1.5 shapes caption (bond counts).
    - 3.8 steroid ring count.
    - 11.5 vitamin K zymogen wording.
    - 13.1: FADH2/FAD single/double bond pair; ATP pool "roughly 50–250 g" (estimates vary); "digestion" of glucose → oxidation; Latin → Greek roots (also 13.10, 13.11).
    - 14.4: FADH2, O2, and "nearly all" of the oxygen.
    - 15.9: urea overall equation now NH4+ + HCO3− + aspartate; urease/arginase wording; the reference to the missing gout photo (Figure 2) and its orphan caption are removed.
    - 15.10: references to the moved Figure 1 now point to Section 15.8 / Figure 15.8.1.
    - 5.2 and 5.4: Tollens and dichromate equations balanced; Disulfiram (Antabuse).
    - 4.2 "two or more carbons".
    - Ch 7 opener: benzocaine claim, which contradicted P7.54(d).
    - 7.3 nail-biting parenthetical removed.
    - 7.9 heroin wording.
    - 9.6 cholesterol about 35 g.
    - 11.1 Enzyme Commission.
    - 13.6 Exercise 4 starting materials.
    - 12.7: Tay-Sachs "by about age four" (NINDS); the cystic fibrosis pointer.
    - 15.5 DKA potassium and ketone-body timing.
    - 1.2, 1.4, 1.6, 1.7, 1.8 chemistry wording.
    - 6.1, 6.5, 6.7, 6.10 wording and equilibrium arrows.
    - 8.5, 8.9, 9.4, 10.2/10.6 HbS charge, 10.12 table title, 11.2 equilibrium, 11.3 lab sentence, 11.5/11.8 "helper in blood clotting", 14.6 stages, 15.13 P15.9, Glossary acid hydrolysis.
    - Number mismatches: 2.6 octane 126, 4.3 methane −162, 4.8, 4.10, 4.11/5.2 ethyl methyl ether 7 °C, 4.12 (−24 °C, butyl methyl ether), 5.7, Ch 5 opener (RBC 120 days), 6.3 (1.1 g), 6.12 (187 °C), 7.2 (mp 81), 8.7 (25–30), 9.8 (69 °C), 10.2 lysine pI 9.7.
    - Missing answers added: 2.9.1, 3.4.1 (inline and in the answer key), 11.2.1.
  - **Repo:** the same edits are mirrored into 122 files in `pages/`, `sections/` and `drafts/`, and into the generators `tools/cumulative.py`, `glossary_terms.py` and `patient_case.py`. `tools/alt_scan.json` and `tools/pka_removal_2026-11-11.py` are historical records and were left unchanged.
  - **Needs the instructor:** the 7.7 video chapter title "…Carboxylic Acid and Amide" is fixed in the book; also fix it on YouTube.
  - **Deferred:**
    - To batch B (the text matches labels baked into images): 9.2 "Glyceryl palmitate" alt text, and the 6.6 163/164 °C chart.
    - New, not yet fixed: 2.6 (597070) Table 2.6.1 also lists methane at −164 °C.
- 2026-11-12, batch B1 of the 2026-11-12 review: wrong structures in figures (branch figures/2026-11-batchB).
  - **Live: 23 files uploaded; 29 HTML edits on 20 pages.**
    - Edit list: `tools/batchB1_figures_2026-11-12.json`, built by `tools/batchB1_build.py`. File ids: `tools/batchB1_ids_2026-11-12.json`.
    - Assets: `figures/pages/batchB/`. Before/after sheets: `tools/batchB_review/`.
  - **New tool:** `tools/rdsvg.py` draws house-style SVGs from SMILES. It uses RDKit for layout only, with the same colours, label halo and bond widths as the draw.js engine, so no node is needed. It also has helpers for polymer brackets, condensed-formula text, one-line equations and grids.
  - **Redrawn (new files):**
    - 4.7 4-hexylresorcinol, with the OH groups 1,3 (512718).
    - 9.6 estradiol without the C10 methyl (512720), and testosterone with C4=C5 (512721).
    - 5.2 Fig 5.2.2 aldehydes; vanillin was drawn as isovanillin (512722).
    - 4.5 isocitrate → oxalosuccinate, which kept a CH3 for a COOH (512724), and Exercise 4.5.1(b) (512725).
    - 7.3 octylamine with (CH2)7 (512726).
    - 7.10 Fig 7.10.2 nylon synthesis with n and 2n H2O (512727).
    - 6.7 PET formation with 2n H2O (512728).
    - 2.5 Exercise 2.5.1 structure 3: the branches now sit on C3, and the chain is heptane per the answer key (512729).
    - 12.8 raltegravir, with the gem-dimethyl and the amide NH (512732).
    - Captions that credited Ball or FGOB for these images now read "Structure redrawn by Daniel Kwasniewski, CC BY 4.0".
  - **Corrected in place (same file id):**
    - 7.10.1 nylon-6,6 and PET repeat units, in brackets with n.
    - 9.1 Fig 9.1.3 thromboxane B2 and leukotriene B4 (conjugated triene plus C14=C15).
    - 3.7 nitrobenzene and 3.8 2-nitrophenol, with nitro charges.
    - 8.6 Disaccharide W and 8.9 Disaccharide Z, with glucose C4 (in W the right ring's C4 link was also galactose-type).
  - **Raster patches (new ids, because the originals belonged to other pages):**
    - 5.4 NAD+/NADH labels swapped back, with the alt text to match (512723).
    - 13.1 Fig 13.1.3 N5–H in FADH2 (512731).
    - 1.8 Fig 1.8.11: thymine CH3 added, and the guanine-strand P–O–O–C link is now P–O–CH2 (512730).
  - **4.3 Fig 4.3.2:** the PDF service resolved the double-encoded name `%253D14.3.jpg` to an unrelated atom image. The same bytes were re-uploaded as `fig-p597092-ethanol-water.jpg` (512719). The other eight images with `%253D` names printed correctly.
  - **Text-side fixes:**
    - 1.7 Fig 1.7.3: the second condensed formula (`mhchem`, which did not print) is now plain HTML.
    - 1.6 Fig 1.6.1: removed `mt-indent-3`, which cropped the image in print.
    - 10.7: the parallel/antiparallel sentence no longer says left/right. The images were correct on screen; the PDF ignores floats.
  - **Verified:** every edit was present and every file is served (HTTP 200, expected sizes). All 21 `pages/live` copies match live by SHA-256. Mirrored into `pages/sec_*` and `sections/{src,add}_*`.
  - **Open:**
    - The instructor's slides need the same kind of fixes: Slide21 (Neo-Synephrine), Slide22 (equilibrium arrows), and Slides 48/49/51/52 (3 H2, 3 Br2, 3 KOH/LiOH).
    - Ball Fig 12.2.3 (19.7a) still reads "1.08 mm", with wrong cytosine and purine bonds.
    - The 1.8.11 caption credits Ball, but the file is an OpenStax image (CNX_Chem); check the source in batch E.
- 2026-11-12, batch B1, part 2: the instructor's own slide PNGs were patched (by request) in `figures/`, using glyphs copied from the same slides so the lettering matches.
  - Slide21: Neo-Synephrine "CHCH3" → "CHCH2".
  - Slide22: the NH3 + H2O and CH3NH2 + H2O reactions now have equilibrium arrows; the HCl reaction stays one-way.
  - Slide52: "+ H2" → "+ 3H2". Slide51: "+ Br2" → "+ 3Br2", and the practice reaction "+ 3H2O / LiOH" → "+ 3LiOH" with heat under the arrow.
  - Slide48: the practice reaction "+ 3H2O / KOH" → "+ 3KOH" with heat under the arrow.
  - Slides 48 and 49: "Glyceryl palmitate" → "Glyceryl tripalmitate" (the name used in 9.7; deferred from batch A).
  - **Not yet live:** GitHub Pages serves `main`, so the new PNGs appear when the PR is merged. After that, publish `tools/batchB1_slides_fixes_2026-11-12.json` (built by `tools/batchB1_slides_build.py`; 15 edits on 597121, 597123 and 597145). It updates the alt text and adds `?v=20261112` to the slide srcs so cached copies refresh.
  - **Live (2026-11-12):** PRs #18 and #19 merged; the Pages build of 274e7c8 serves the six slides byte-identical to the repo. The 15 alt-text and cache-bust edits are published on 597121, 597123 and 597145 and verified, and `pages/live` matches live by SHA-256.
- 2026-11-12, batch B2 of the 2026-11-12 review: label typos baked into images (branch figures/2026-11-batchB2).
  - **Live: 23 files uploaded; HTML edits on 18 pages.**
    - Edit list: `tools/batchB2_figures_2026-11-12.json`, built by `tools/batchB2_build.py`. File ids: `tools/batchB2_ids_2026-11-12.json` (512734–512754, plus 512617 and 512629 re-uploaded with the same id). Assets: `figures/pages/batchB2/`. Before/after sheets: `tools/batchB_review/B2_*`.
    - Each patched raster was uploaded to its own page under a clean `fig-p<page>-<slug>` name, and the img src/fileid were repointed; alt text was kept.
  - **Method:** letters were copied from the same image (Myriad-style figures) or retyped in Arial on the flat-colour panels.
  - **Fixed:**
    - 1.7 step figures: also, This is the, treat.
    - 5.3 hemiacetal; 7.1 m-chloroaniline (italic m in Trebuchet).
    - 8.4.1: representation, plus the C2–OH bond in panel (b).
    - 10.1 representation.
    - 10.6: GHK; Aspartylphenylalanine; Aspartame; Fig 10.6.1 terminus labels in English with N at the left and C at the right (the Ukrainian labels also had them reversed); alt updated.
    - 10.8 side chains; 11.6.2 Threonine ×3; 12.2.3 1.08 nm (both rotated labels); 12.8 triphosphate.
    - 13.1.2 Nicotinamide; 13.3.1 Pyruvate, oxidation; 14.1.1 Phosphorylated ADP.
    - 14.2.3: Fumarate, CoQ, NAD+, Pi, ½O2 + 2H+.
    - 14.4.3: pyruvate 2C3H3O3, "for two pyruvates", the glycolysis panel shown as net (2 ADP + 2 Pi in, 2 ATP out), 2Pi, 2HS-CoA.
    - 15.4.1: Acyl-CoA dehydrogenase, trans-Enoyl-CoA, Palmitoyl-CoA, FADH2.
    - 15.5: HSCoA.
    - House SVGs: 13.8.2 "(six reversible steps)"; 15.10.1 pyruvate → oxaloacetate one-way, with the caption updated.
  - **Verified:** all 23 files are served (HTTP 200). Every edit and image id is present live, and the 19 `pages/live` copies match live by SHA-256. Mirrored into 36 `pages/` and `sections/` files.
  - **Slide26** (instructor's slide; the two stray bold left arrows were removed) is in `figures/`. After merge, publish the `597167` edit in the B2 JSON (cache-bust `?v=20261112`); it is held until Pages serves the new PNG.
  - **Open:**
    - Ball Fig 12.2.3 structures (cytosine NH2, C4=N3, purine C4=C5).
    - Fig 8.4.1(b) shows a curved-arrow mechanism (excluded by the book's scope rules).
    - 14.1.1 phosphate charges; 9.3.1 condensed formula.
  - **Slide26 live (2026-11-12):** PR #21 merged; Pages build aae37a5 serves the new Slide26. The cache-bust edit on 597167 is published, and `pages/live` matches live by SHA-256.
- 2026-11-12, batch C1 of the 2026-11-12 review: figure numbering (branch content/2026-11-batchC1).
  - **Live: 91 edits on 38 pages.**
    - Scanner: `tools/figscan.py`. Edit list: `tools/batchC1_fignum_2026-11-12.json`, built by `tools/batchC1_build.py`. Label map: `tools/batchC1_label_map_2026-11-12.json`. Review sheet: `tools/BATCH_C1_REVIEW_2026-11-12.md`.
  - **Rule:** \PageIndex source captions keep their numbers. Hard-numbered Lecture Connection figures continue after the page's last source figure (29 section pages). Chapter Guide two-part numbers became three-part (1.9, 2.10, 3.9, 4.11, 5.6, 6.11, 7.12).
  - **Special cases:**
    - 1.6: the ethyne image is now captioned Figure 1.6.3.
    - 5.4: source figures 2–4 became 1–3.
    - 9.1: source figure 2 became 1 (references 2a/2b → 1a/1b).
    - Cross-references follow their figures: 8.3 ×2 (→ 8.3.3) and the 12.1 Professor Tip (→ 12.1.6).
  - **Verified:** every new string is live, and all 38 `pages/live` copies match live by SHA-256 (`tools/batchC1_live_sha_2026-11-12.json`). Mirrored into 73 `pages/` and `sections/` files.
  - **Re-scan:** only 1.7, 9.4, 14.2 and 14.4 are still flagged, and those are false positives (a paragraph beginning "Figure \(\PageIndex{n}\) shows…").
- 2026-11-12, batches C2–C4 of the 2026-11-12 review (branch content/2026-11-batchC2-4).
  - **Live: 36 edits on 22 pages.** Edit list: `tools/batchC2_4_fixes_2026-11-12.json`, built by `tools/batchC2_4_build.py`. Review sheet: `tools/BATCH_C2_4_REVIEW_2026-11-12.md`.
  - **C2, old alt text shown as captions (21 figures):**
    - Deleted 6 second captions that repeated the alt text (1.8 Figs 7, 8, 12; 4.5 Fig 1; 5.2 Fig 1; 9.5 Fig 4).
    - 1.4 Fig 3: the empty credit caption was merged into the real caption, and the colon added.
    - 14 captions that were only screen-reader text were replaced with short real captions, credits kept: 1.1 ×7, 1.2 NH3, 1.3 HCN, 2.7 butane, 4.5 ×3, and the 1.8 group-14 boiling-point graph (its old text also gave values that contradicted the graph).
    - Left as they are: the 4.5 exercise naming captions, which are teaching text.
  - **C3:** 12 `&amp;ndash;` in alt attributes → `&ndash;` (1.8, 3.5, 4.7, 6.8, 7.11, 13.8).
  - **C4:** 9 `display:none` spans removed, rejoining "propionic acid" (6.3) and "oxidoreductase" (11.1).
  - **Verified:** new strings live and old strings gone; the 22 `pages/live` copies match live by SHA-256. Mirrored into `pages/` and `sections/`.
- 2026-11-12, batch C5 of the 2026-11-12 review: leftovers (branch content/2026-11-batchC5).
  - **Live: 46 edits on 37 pages.** Edit list: `tools/batchC5_fixes_2026-11-12.json`, built by `tools/batchC5_build.py`. Review sheet: `tools/BATCH_C5_REVIEW_2026-11-12.md`.
  - **Fixed:**
    - "(Copyright; …)" → "(…)" on 35 credits.
    - The internal "Copied into this book (no longer live-linked)…" note → the standard editing line (4.9, 6.6, 11.5, 15.11).
    - Stale objectives on 14.4, 15.3, 15.4 and 15.10.
    - About 20 one-off leftovers: 1.5, 1.7 ×2, 1.8, 4.1, 4.5, 4.11, 5.6 ×2, 6.10, 7.12, 8.3, 8.7 (CDCES), 10.5, 10.6, 11.1, 11.8, 12.9, 13.12, 14.3, 15.9.
  - **Verified:** new strings live, old strings gone; 37 `pages/live` copies match live by SHA-256. Mirrored.
  - **Open:**
    - Fact-check batch for dated statistics (8.6 sugar, 8.7 cotton/rayon, 4.4 methanol, 12.9 measles, 2.8 ozone hole, 3.5 joints, 3.8 benzo[a]pyrene, 1.6 MyPlate).
    - For batch E: the eight bare "(Public domain)" credits with no source.
    - Restructuring: 6.12/7.13 answer keys, the 10.2/10.3 ninhydrin duplicate, the 12.5 translation preview.
- 2026-11-12, batches C6–C7 of the 2026-11-12 review (branch content/2026-11-batchC6-7).
  - **Live: 133 edits on 47 pages.** Review sheet: `tools/BATCH_C6_7_REVIEW_2026-11-12.md`.
  - **C6 (33 edits):** `tools/batchC6_index_2026-11-12.json`, built by `tools/batchC6_build.py`.
    - 18 Index entries that disagreed with the Glossary now use the glossary section.
    - Six glossary links moved to the teaching section (confirmed by term counts): amide 7.4, reduction 5.4, IMF 1.8, glycol 4.6, tRNA 12.5, complementary base pairs 12.2. Their index entries follow (9).
    - `tools/glossary_terms.py` holds no section numbers, so nothing changed there.
  - **C7 (100 edits on 46 pages):** `tools/batchC7_typos_2026-11-12.json`. Drafted in three parts (`tools/c7_parts/`), then merged and replay-checked; no edit changes markup. Every change was reviewed as a word diff.
  - **Skipped:**
    - Six were already fixed.
    - Need the instructor: the About Valley list order, 1.9 video titles vs YouTube, and the 5.4/5.5 page titles in title case (needs the title API).
    - For batch E: the 15.8 "from Wikipedia" caption.
  - **Verified:** new strings live; the 47 `pages/live` copies match live by SHA-256. Mirrored into 89 `pages/` and `sections/` files.
  - **Instructor:** the 9.2 video chapter title "triplemitoleate" is fixed in the book; fix it on YouTube too.
- 2026-11-12, batch D (print layout) of the 2026-11-12 review (branch print/2026-11-batchD).
  - **D2 live: 15 edits on 7 pages.** Edit list: `tools/batchD2_videos_2026-11-12.json`, built by `tools/batchD2_build.py`.
    - The ten plain or widget YouTube embeds (597062, 597074 ×2, 597141 ×2, 597192, 597193, 597202, 597209 ×2) now use the aspect-ratio wrapper with real titles from YouTube oEmbed.
    - The instructor's guide videos have "(Daniel Kwasniewski (ItsDrDan))" on the title line.
    - The BioMan Biology videos on 13.4, 13.5 and 14.3 now carry a credit line ("not covered by this book's license").
    - Verified by SHA-256 and mirrored. A one-page compile showed the widget embeds already printed as compact QR boxes, so the gain is phones and consistency.
  - **D3 print test, a correction to the earlier note:** the PDF service also ignores inline image sizes. Tested on 14.3 with step images styled `width:100%`, `width:6in` and `height:4in` and the wheel styled `width:6.5in`, and separately `max-height:none`: every one printed at the default size. Wide, short figures print about 4.6 in wide and readable; square or tall figures are held to about 3 in high (the 14.3.1 wheel and the stacked 13.5.1 glycolysis SVGs).
    - So the only fix for small print is the figure's shape: redraw tall or square diagrams in a landscape layout (width at least about 2.2 × height).
    - The test edits were reverted; 597202 is byte-identical to its post-D2 state.
  - **D3, glycolysis overview (13.5, Figure 13.5.1) published:** the two tall SVGs are now six horizontal strips each (`figures/pathways/glycolysis/print/full-investment-1..6.svg`, `full-payoff-1..6.svg`), cut along the blank bands between steps and stacked as `display:block` images. The first strip of each half keeps the alt text; the rest have `alt=""`.
    - On screen they look the same as before. In print each strip is sized like a normal figure, so the text is about 3× larger; the 13.5 PDF is 14 pages (about 2½ more than before).
    - Verified by SHA-256 (c3ba2348…) and mirrored into pages/sec_597193.html and sections/src_597193.html. Edit list: tools/batchD3_print_2026-11-12.json.
    - The 14.3 citric acid cycle wheel was left as is (author's decision): it has no blank bands to cut, and the eight step figures below it print readably.
  - **D3b published (13 tall diagrams as print strips, 11 pages):** 5.4 hydrogenation; 12.4 tRNA loading; 13.1, 13.6 (×2), 13.7 (×2), 13.8, 14.3 flow chart, 14.4 respiration, 15.6 fatty acid synthesis, 15.10 hub, 15.11 nonessential amino acids. Strips on GitHub Pages (figures/print/; PR #29). All 11 pages verified by SHA-256 against pages/live and mirrored.
    - Print tests (5.4, 13.8, 14.4): labels now print at 7.7–9.3 pt, up from 3–5 pt.
    - **Print rule, measured:** printed width = min(`width` attribute or CSS px width × 0.75 pt, 522 pt text width, 216 pt × the image's width/height). So every image is capped at 3.0 in high. A strip less than ~2.42× wider than tall prints narrower than its neighbours, and the edges jog (seen on 13.8.2: the bottom strip printed 4% narrower).
    - Correction prepared as D3c (branch print/2026-11-batchD3c): new cuts with a strict aspect limit for 7 figures and the 13.5 glycolysis halves (the first glycolysis strips printed 3–10% narrower), written as `*-v2-*.svg`; 13.8.2 gets width 660 (no clean cut set fits). Not yet published.
    - Not stripped (no clean cut row; need a redraw): 13.5 glycolysis flow chart, 14.4 ATP synthase, 14.4 electron transport chain, 14.5 wide figure. Skipped: 9.4 sphingolipids, 7.12 roadmap. Concept maps print at about 5 pt.
  - **D3c published (PR #30 merged):** v2 strips on 8 pages (12.4, 13.5 both glycolysis halves, 13.6, 13.8, 14.3, 15.6, 15.10, 15.11); 13.8.2 width 760 → 660. All 8 pages verified by SHA-256 against pages/live and mirrored. Print tests on 13.5, 13.8 and 14.3: strips line up at one scale with no edge jogs; 14.3.2 prints full width.
    - The superseded strip files (figures/print/*-<k>.svg for the redone figures, figures/pathways/glycolysis/print/) are no longer used by any page; they are left in place.
  - **D5 published (13 pages):** six exercise boxes with the `<header><h5|h4 class="editable">` form converted to the standard `box-legend` form (1.1, 1.3, 1.5, 1.8 ×2, 6.9; the 6.9 box used `h4`, so it got an addendum, batchD5b). 1.7 "Four ways" table images 218/218/141 → 160/160/104 px; Table 11.1.2 reaction image width 440. 30 drawn-example labels (2.10, 3.9, 4.11, 5.6, 6.11, 7.12) get `page-break-after:avoid`.
    - Verified by SHA-256 and mirrored. One-page compiles: the 1.1 exercise headings print normally, and both tables fit inside the margin. The stranded-label rule needs a full-book compile to confirm.
  - **D4 published (18 pages), the author's picks of the recommended wraps:**
    - Group A: 19 small screen-floated images now float in print too (inline float, `max-width:45%`, class `wrap-left/right`). Seven large 13.1/14.4 diagrams lose the float and show full width on screen and in print.
    - Group B: 15 captioned figures wrap right (inline float, width 22–40%).
    - Every edited page gets the phone rule (un-float below 640 px) in its style block, added where missing.
    - Dropped after test prints: the 1.7 n-hexane three-panel figure, the 8.3 food-sources and 4.7 phenol composites, and the 1.8 NaCl pair (side-by-side images stack in print). 14.4 heme image gets `clear:both` so text is not squeezed between two floats.
    - The server reorders `width`/`height` attributes on some image tags on save; pages/live copies match live by SHA-256 after copying that order.
    - **PRINT FACT:** an image's `max-width` percentage inside a figure is not honoured by the PDF service, so side-by-side composites stack vertically.
- 2026-11-12, batch E (licensing and attribution). Every finding was re-checked before any change was made.
  - **E1 published (18 edits on 13 pages):**
    - Malik figures with bare "(Public domain)" now credit *Introduction to Organic and Biochemistry* (Malik), public domain. Malik's own captions name no creator.
    - Commons photos credited after a visual match and a Commons API lookup.
    - 1.8 Figs 10–11 are credited to OpenStax *Chemistry 2e* §10.1, CC BY-NC-SA 4.0 (Fig 11 was wrongly credited to Ball).
    - 15.1 lipoprotein diagram credited to Jairam, Uchida and Narayanaswami (IntechOpen 2012, CC BY 3.0).
    - 10.7 Fig 1 credit pointer added.
    - Source Attributions videos and figures statements fixed; About Malik count 21 → 20.
    - Checked and unchanged: 11.6 *Biology 2e* is CC BY-NC-SA 4.0 per OpenStax, so the review was wrong; LibreTexts names itself as the author of *Fundamentals of GOB*.
  - **E2 (local):** QTI generators and all 36 QTI zips now say "Questions by Daniel Kwasniewski, CC BY 4.0", and each zip has a LICENSE.txt. cumulative.py docstring fixed. Live ADAPT fields were not checked (browser not signed in to ADAPT).
  - **E3 published (author's decision: replace):**
    - The CC BY-SA images (3.3 tomatoes, 4.7 phenol crystals, 15.8 ergospirometry photo, 10.7 Fig 1 triple-helix panel) and the uncredited Malik photos (15.4 ×4, 9.3 snake) were replaced with public-domain or CC0 Commons photos. The 10.7 panel is cropped from the book's own collagen diagram.
    - Licences come from the Commons API; uploaded as files 512755–512763 (tools/batchE3_ids_2026-11-12.json).
    - 15.4's four photos now sit in one row above the paragraph (E3b), because the floats squeezed the text.
    - The About bullet was rewritten: the ShareAlike statement is now true, and the stray "also:" and run-on clause are gone.
  - All pages verified by SHA-256 and mirrored.
  - The author confirmed the 40 `canvas-quiz` bank items are their own.
- 2026-11-12, batch F (elevation), published on 31 pages; the author picked the top 15 plus the Valley/clinical hooks. All 73 review suggestions were re-checked against the live pages first (1 done, 44 partly, 28 absent; tools/F_ELEVATION_SHORTLIST_2026-11-12.md).
  - **F1 (15 items):**
    - Worked examples on 12.4, 5.4, 10.2, 2.7, 2.5, 12.7, 11.6 and 9.2.
    - 1.8 donor/acceptor table; 13.9 ADA 15-15 rule; 14.2 Table 1 yield cells.
    - Four new house figures (tools/batchF_figs.py; files 512764–512767): 11.4.2 rate vs [S] with inhibitors, 12.3.4 replication fork, 8.4.5 Fischer→Haworth in three steps, 12.6.4 elongation cycle with P/A sites.
  - **F2 (17 hooks, 24 edits):**
    - New Valley boxes on 4.9, 10.3, 15.7, 12.7, 11.5, 3.5 and 2.6.
    - Clinical additions on 7.9, 7.10, 9.3, 11.7, 8.5, 11.3 and 15.5.
    - Short additions on 14.4, 1.8, 6.9 and 10.1.
    - Every statistic, law or protocol is cited; unverifiable claims were dropped. Spot-checked against the source documents: CDPH 7,137 fentanyl deaths (2023); AB 1830 0.7 mg/lb from 1 Jan 2026.
    - 12.7 heel-stick timing aligned with CDPH (12–48 h).
  - Verified by SHA-256 and mirrored. The server escaped `&` in one 2.6 URL and re-nested 4.9's sections after the new box (renders the same); the repo copies follow live.
- 2026-11-12, batch G (leftovers), published on 2 pages, verified by SHA-256 and mirrored.
  - 9.3: the labelled POPC space-filling image (file 435596) had no source in Malik or on Commons, so it was replaced with an original labelled phosphatidylcholine sketch (file 512768; tools/batchF_figs.py phospholipid()).
  - 9.3 Fig 1 and 9.4 Fig 2: "(Copyright: Public domain)" (the colon form C5 missed) now credits Malik.
  - Still open:
    - ADAPT fb-3B-0078: the bank, payloads and question list are clean; the live ADAPT copy is unchecked (needs sign-in).
    - Lab experiment numbers (Experiments 1–14 cited on about 16 pages): need the lab manual.
- 2026-11-12 night, ADAPT live check (course 4605, signed in):
  - All 1,031 questions are CC BY 4.0, author Daniel Kwasniewski.
  - Five questions still used pKa live (fb-3B-0078, 0864, 0865, 0870, 0871); they were updated in place to the pKa-free bank versions, with hints kept. A re-scan finds no pKa anywhere, and every assignment uses the latest revision.
  - Video-hint licence note: left as is (instructor decision).
  - Details in adapt/README.md.
- 2026-11-12 night, full-book PDF (22:14, 1,324 pp; saved as Study Games/CHEM3B-Full-2026-11-12-2215.pdf) compared with the 00:50 PDF:
  - Pages with figure text under 4.6 pt fell from 29 to 18; the rest are known redraws or concept maps.
  - "Copyright" credit leftovers fell from 41 pages to 4. No margin overflow, no garbled "Exerc" headings.
  - Batch H fixes the new findings (78 pages, verified by SHA-256 and mirrored):
    - H1: 1,553 answer-key and exercise labels keep with their answers (page-break-after:avoid). Test print of 2.11: 0 stranded labels.
    - H2: the 12.4 tRNA-loading strips moved below the side-by-side row; labels now print at 7 pt, up from 4.
    - H3: the 13.1 metabolism overview (CC BY-SA 4.0, the last ShareAlike image) is replaced by an original diagram (file 512769).
    - H4: the last six "Copyright:/;" prefixes in body text are cleaned (13.1 ×4, 9.3 Fig 3 ×2).
    - H5: 12.6 elongation figure amino-acid labels enlarged (same file 512767).
- 2026-11-13, batches I (held items) and J (optional), published on 46 pages; verified by SHA-256 and mirrored. PR #38 (assets) merged. Review: tools/BATCH_IJ_REVIEW_2026-11-12.md.
  - **I:**
    - Dated statistics fact-checked: 8.6 sugar (USDA ERS), 8.7 textiles (Textile Exchange 2025), 4.4 methanol (UKHSA), 12.9 Valley fever, 2.8 ozone hole (NASA), 3.5 joint replacements, 3.8 benzo[a]pyrene, 1.6 MyPlate / DGA 2025–2030.
    - 2.6 methane −162 °C. About Valley list order. 12.5 preview labels.
    - Ninhydrin duplicate removed from 10.2; Ball credit on 10.3 (the fingerprint is not the Commons ShareAlike photo).
    - 6.12/7.13 answer keys synced. 6.6 chart 163 °C. "(opens in new window)" residue removed.
    - 1.5/1.8 embed titles match YouTube (oEmbed); the 1.9 list was already right.
    - Figures: 12.2.3 base pairs (cytosine NH2 and C4=N3, purine C4=C5), 14.1.1 O− charges, 9.3.1 condensed formula redrawn, 8.4.1(b) mechanism arrows removed, Slide 47 "Glyceryl tripalmitate". New files 512770–512775.
    - 5.4/5.5 titles in title case (move API, path unchanged); references on 597271/597272 updated.
  - **J:**
    - 13.5.2 glycolysis flow redrawn landscape (prints 6.4 pt, was 4.1).
    - 14.4.2 parts stacked and ATP synthase as two strips (8.2 pt, was 4.4).
    - 14.4.5 ETC inner-membrane version (about 7 pt). 14.5 yield flow cropped.
    - 18 clarity fixes (tools/batchJ_text_drafts_2026-11-12.json).
  - **Checked and unchanged:** 13.2 table −7.5 (the page's Professor Tip explains it; exams use 7.3).

- **2026-11-13 Batch K (optional work: concept maps and Group C figures), live and verified (SHA-256 on all 30 pages):**
  - Concept maps ch01–ch15 rebuilt with larger type (tools/concept_maps.py, Python renderer tools/pathway.py); the 15 Chapter Guides link `?v=20261113`. The new SVGs are served by GitHub Pages once this branch is merged.
  - 15 new figures, files 512776–512790 (tools/batchK_ids_2026-11-13.json, review sheets in tools/batchK_review/):
    - Structures: 6.8 tristearin saponification, 7.6 amide in two steps, 5.5 menthol/carvone chiral carbons, 3.4 propene + HCl, 2.9 ring numbering, 1.6 aspartame groups, 6.10 aspirin COOH vs COO−.
    - Schematics: 6.3 acetic acid dimer, 9.5 RBC tonicity, 8.7 amylose/glycogen/cellulose, 13.7 glycogen branches, 15.4 acyl CoA α/β numbering, 9.1 linoleic C/ω numbering, 1.3 Lewis structure errors, 7.3 lidocaine neutral form (qualitative, no pKa).
  - Captions renumbered so new figures stay in page order: 6.8.2→6.8.3, 3.4.1→3.4.2, 13.7.1–2→13.7.2–3, 15.4.3–4→15.4.4–5, 9.1.4–5→9.1.5–6 (numbers appear only in their own captions).
  - Server normalised "–" to `&ndash;` in five new alt texts; pages/live holds the server form.

- **2026-11-13 Batch L (full-book PDF check of 2026-11-12 23:50), live and verified (SHA-256 on all 7 pages):**
  - The PDF had 1,337 pages, no overflow, no "Copyright" or "Exerc" leftovers, and tiny-text pages down to 7 (from 18). The batch K figures print at 6.8–11 pt.
  - 14.3.1: the citric acid cycle wheel (printed at ~2 pt) is replaced by a landscape loop, file 512791 (tools/batchL_figs.py).
  - 7.12: Reaction Roadmap redrawn with rows packed, type 16/13, aspect 2.57 (tools/batchL_roadmap.py); the page links `?v=20261113` and it goes live on merge (GitHub Pages).
  - 9.3.1: condensed formula moved below the three-across row, so it prints full width; caption now says "(below)".
  - Stranded labels: 1.3 "Check" and the 8.9 "Case Set Question 8.2" title now carry `page-break-after:avoid`. The 4.4/10.2 Example "Solution" h4s carry the same. The server strips attributes on `div.mt-section`, so the first try on the div did not stick.
  - Left as is: the 15.9 urea-cycle enzyme labels and the 14.4.7 rotor panels (~4.4 pt, readable when zoomed).

- **2026-11-13 IMF batch: Sticky Molecules on the Practice Games pages, live and verified (SHA-256 on all 7 pages):**
  - The new section sits before Final Boss on 1.11 (597232), 4.13 (597234), 7.14 (597237), 8.10 (597238), 9.9 (597239), 10.13 (597240) and 12.12 (597242). It embeds `https://itsdrdan.github.io/IMF/?course=3B` with a chapter tip.
  - Four of the pages also link a lab: H-Bond Lab on 1.11, Mixing Beaker on 4.13, Cell Lab on 9.9 and Protein Fold Lab on 10.13. The lab links were checked with CHEM 3B selected.
  - Built by tools/imf_games_build.py into tools/imf_games_2026-11-13.json. The server renumbered the `mt-section` ids, and pages/live holds the server form.
  - pages/chNN_games.html, the build_pages.py output, was not regenerated.
  - **Plan for the rest:** tools/IMF_INTEGRATION_PLAN.md. Still open, waiting for the instructor's OK:
    - Try It bank and ADAPT: 112 candidates in tools/imf_deck_candidates_2026-11-13.json.
    - One Protein Fold Lab figure for 10.10.
    - Try It widgets for 9.5 and 10.8.
  - **Found, not fixed:**
    - Game fatty-acid melting points differ from 9.1 (palmitoleic 0 vs 0.5, oleic 14 vs 13, arachidonic −50 vs −49 °C).
    - The questionbank tags the osmosis and tonicity items `3B-15`; they should be `3B-10`.
    - The 10.8 Figure 1 caption lists metal coordinate bonds, against CONVENTIONS.

- **2026-11-13 Fresh full check and batch M, live and verified (all 64 pages read back identical):**
  - Report: tools/REVIEW_2026-11-13.md. All 199 live pages matched pages/live by SHA-256 before the check. No wrong answer key and no stale renumbering cross-reference was found.
  - **Published: 93 edits on 64 pages** (tools/batchM_2026-11-13.json, built by tools/batchM_build.py). pages/live holds the post-edit pages.
    - Wrong facts: 3.1 1-pentene mp −165; 7.5 formamide bp 210; 10.1 arginine 174; 11.3 boiling water disinfects; 13.9 Exercise 4 brain fuel at day three; 4.9 rotten-egg smell is H2S; 6.1 bee and wasp stings; 7.10 PET not cross-linked; 7.9 pain relievers; 8.5 five OH groups; 1.8 CO2 about five atmospheres.
    - Conventions: thiamine and biotin are coenzymes (13.1, 13.4, 13.10, 14.1 ×3, 14.6, 15.6) and the Glossary cofactor/coenzyme entries; amine angle about 107° (7.2, P7.76); 15.6 Summary; 10.5 Summary and Figure 5 caption use the four graded interaction names; 4.5 methanol 10 mL; 6.5 pear ester; 7.8 adenosine; 1.9 −25 °C; 1.7 alkyne condensed formulas; 3.9 "pi electrons".
    - Figures: numbers put in order on 7.10, 12.2 and 15.10; 3.2 Figure 3 caption; alt text on P2.72, 8.6.3 and 9.6.5; credits on 9.3 Figure 4, 10.7 Figure 4 and 13.5 Figure 1.
    - Print keys added on 2.9, 8.1, 8.2, 10.2, 11.2, 12.3 and 12.6 (their inline answers never printed); 14.2 key label; 12.6 exercise renumbered 1.
    - 18 path-based in-book links repointed to /@go/page ids; lactate pointers to 13.4 (13.8 ×3, Chapter 14 opener); Chapter 1 game pointers; small wording fixes.
  - **Not done:** the repo mirrors (pages/*.html, sections/, drafts/) and generators; nothing is committed.
  - **Open, needs the instructor** (blank "M" rows in the report): 8.4 Slide36 curved arrow; "hydride" wording; 2.9 cyclopropane; 3.4 Example 3(c); 1.8 "covalent compounds do not ionize"; six figures printing under about 5.3 pt; 65 captioned figures with no credit line; nine dead external links; Glossary/Index pointers (allosteric, reactive oxygen species, alcohol dehydrogenase); About This Book Valley list and version history; 11.1 Figure 1 is script-only.
  - **Bank and ADAPT (not changed):** the extra/more/nov5 QTI zips are stale (24 ids, including four pKa items and a Km item); fb-3B-0650 "sp3"; wording slips on 0629, 0974, 0456, 0227/0599; tools/imf_deck_candidates_build.py sets `k` to the answer index, so 82 of 112 candidates would be mis-keyed on import; the questionbank tonicity items carry both 3B-10 and 3B-15 (remove 3B-15).

- **2026-11-13 PDF check of the 01:14 compile (1,339 pp; first compile with batch M) and four follow-up fixes:**
  - Batch M prints: all 53 searchable text edits, the eight new print-key entries (2.9.1, 8.1.1, 8.2.1, 10.2.1, 11.2.1, 12.3.1, 12.3.2, 12.6.1), Figures 7.10.3, 12.2.5, 12.2.6 and 15.10.2, and the 14.2 key label. p2 licence present; no raw MathJax, "Copyright" or "ItsDrDan" credit.
  - Words under 6 pt: 32 pages, unchanged (list in tools/REVIEW_2026-11-13.md).
  - Found and fixed (live):
    - 6.10 (597118): two `&#8652;` arrows printed as missing glyphs; now MathJax. Read back identical; mirrors updated.
    - 1.3 Lewis-errors figure (file 512789, now revision 2): "e⁻" and "N⁺" printed as missing glyphs; now raised tspans. Source: figures/pages/batchK/ and tools/batchK1_figs.py.
    - Figure 14.1.3 (file 512620, now revision 3): the label inside the drawing said "thiamine cofactor"; now "thiamine coenzyme" (label and aria-label). The live file could not be read (post-compile cache redirect), so it was rebuilt from the original inline SVG (commit c992e64, sections/add_597200.html) plus the print fix; it is 29 bytes larger than revision 2 and was checked by eye against the printed figure and on the live page. Revision 2 stays in the file history. Repo copy: figures/pages/batchM/fig-p597200-1.svg.
    - Chapter 6 concept map (GitHub Pages, live on merge): "RCOO⁻" now uses a normal minus sign (svg and tools/concept_maps.py). The 6.11 page still links `?v=20261113`, so browsers may show the old map for a few minutes after the merge.
  - Method notes: the signed-in page cannot fetch from localhost, and neither the shell nor a browser tab can read files.mtstatic.com; file bytes go in through raw.githubusercontent.com at a pushed commit.
  - Not rechecked in print: these four fixes need the next compile.

- **2026-11-13 PDF check of the 09:36 compile (1,339 pp; after PR #43 was merged):** the four follow-up fixes print.
  - 1.3 Lewis-errors figure (p46): "16 e−", "12 e−", "6 e−" and "N+" print as raised charges.
  - 6.10 (p500): both equilibrium arrows print.
  - 6.11 concept map (p506): "RCOO− in body".
  - Figure 14.1.3 (p1146): "(NAD+, CoA, thiamine coenzyme)"; no "thiamine cofactor" anywhere in the book.
  - Missing-glyph boxes in the whole book: 0. Batch M text, the eight print-key entries and the renumbered figures are unchanged from the 01:14 compile. p2 licence present; no raw MathJax or "Copyright" leftovers.
  - Words under 6 pt: 32 pages, unchanged (open; list in tools/REVIEW_2026-11-13.md).

- **2026-11-13 Batch N (the rest of the 2026-11-13 review that needed no redraw), live and verified (all 45 pages read back identical):**
  - **Published: 83 edits on 45 pages** (tools/batchN_2026-11-13.json, built by tools/batchN_build.py; expected hashes in tools/batchN_sha_2026-11-13.json). pages/live holds the post-edit pages; mirrors updated.
  - **Instructor decisions, 2026-11-13:**
    - "Hydride" replaced everywhere with "two electrons and an H+" wording (Glossary, 11.5, 11.8, 11.9, 13.1 alt, 13.6, 13.11 ×2, 14.2, 14.5, 14.7). The NaBH4 "hydride reagent" in 5.4 and "group 14 hydrides" in 1.8 stay.
    - The curved arrow on the 8.4 ring-closure slide (Slide36, Figure 8.4.3) stays as an allowed exception. CONVENTIONS.md records both.
    - Credit lines added where the caption had none: lecture slides 4.2.2, 5.1.1, 5.5.8, 6.4.1; 4.5 Exercise 1(b) redraw; Ball line on 1.4 Figure 5 and 11.4 Figure 1; Malik line on 14.4 Figure 3.
  - Content: 2.9 cyclopropane; 1.8 and P1.65 "most covalent compounds"; 1.4 C–Br; 2.6 branching; 10.11 Key Idea 2; 4.5 Valley answer; P4.53; Cumulative 13.4.
  - Figures and numbering: 1.6 captions and text no longer promise molecular models; 1.6 Exercise 1 alt relettered with no giveaway; 9.2 soap alt; Tables 13.7.1–2 and 13.8.1–2; 1.5 examples and exercises 1–3; 1.8 Example 2.
  - Pointers and wording: Case Set 14.3 and P10.81; Glossary and Index for allosteric (11.6), reactive oxygen species (13.6), alcohol dehydrogenase (4.5); 8.3 sucralose link; 2.3; 3.8 stray bullet; 5.1; 7.10 and 7.6 "nylon-6,6"; 12.3 and 12.4 end labels; 12.10 box moved; 10.6/10.7 "shown here"; 13.5 credit prefix; About This Book Valley list (+7).
  - **Correction to the review:** the "65 captioned figures with no credit" count was too high. Most were inner panels of composite figures whose outer caption carries the credit. Twelve captions truly lacked one; eight are fixed here and the four 9.3 structure labels sit under a credited figure.
  - **Still open:** 3.4 Example 3(c); 11.1 Figure 1 (script-only viewer); About This Book version entry; uncaptioned images with unknown source (3.3 lycopene, 4.7 Traversi painting and Phenol-3D-balls, 4.8 Morton painting, 13.4 sulfonylureas, 12.8 AZT and raltegravir captions); 6.8 and 7.11 captions that repeat the alt text; 1.7 Figure 1–2 alt letters; 9.3 snake photo position; 10.10 source numbering; nine missing Index entries and 12 weaker Glossary pointers; hot-linked images in 10.7 and 11.6; nine dead links; six figures under about 5.3 pt; bank and ADAPT findings.

- **2026-11-13 Batch O (next-pass rows and dead links), live and verified (all 14 pages read back identical):**
  - **Published: 72 edits on 14 pages** (tools/batchO_2026-11-13.json, built by tools/batchO_build.py; hashes in tools/batchO_sha_2026-11-13.json).
  - Captions: 6.8 aspirin and 7.11 epinephrine no longer repeat the alt text; 12.8 dTTP/AZT (Ball, adapted) and raltegravir (house redraw) now have a caption and credit.
  - 1.7 Figures 1–2: panel letters removed from eight alt texts (they were one behind the visible letters).
  - 10.10 Valley box: sources renumbered in citation order.
  - Glossary and Index: 16 pointers moved to the teaching section; nine new Index lines (beta-pleated sheet, C-terminus, N-terminus, fat-soluble vitamins, water-soluble vitamins, fluid-mosaic model, lock-and-key model, omega-3 and omega-6 fatty acid).
  - Dead links replaced: NDSU Virtual Cell → www.vcell.science (12.6, 14.1, 14.2); 9.2 CIHEAM PDF → FAO AGRIS record; 8.6 USDA Tulare profile → the California county profiles page; 4.5 Grape Crush PDF → the USDA crush reports page; 2.6 NASA oil-spill page → Earth Observatory image 44006 (not confirmed to be the same photo).
  - **Still open:** 10.9 "Nitrates unchecked" link (reprint gone); 6.5 ASHS abstract (server error); 9.3 snake photo position; hot-linked images in 10.7 and 11.6; 3.4 Example 3(c); 11.1 Figure 1; About This Book version entry; unknown-source images; six figures under about 5.3 pt; bank and ADAPT findings.

- **2026-11-13 Batch P (instructor decisions, credits, re-hosted images, small-print labels, bank and exports):**
  - **Published: 24 edits on 11 pages** (tools/batchP_2026-11-13.json, built by tools/batchP_build.py). Ten pages read back identical; on 11.6 (597171) the server moved the image's width attribute, and pages/live holds the server form.
  - **Instructor decisions:** 3.4 Example 3 now uses 1-butene → 2-butanol (3-methyl-1-butene rearranges on hydration); the 11.1 Figure 1 viewer stays, with a caption that says it is an online model (PDB 1CDO); About This Book and the title page are version 1.2 (November 13, 2026) with the old-to-new section numbers.
  - **Credits from the Wikimedia Commons API (file names match; images not compared by eye):** 3.3 lycopene (Jeff Dahl, public domain), 4.7 Traversi painting (public domain), 4.8 Morton painting (Ernest Board, public domain).
  - **9.3:** snake photo moved into the Snake venom box; phosphatidylcholine sketch width 205 → 300.
  - **Files uploaded:** fig-p597192-1.svg (13.4.2, labels 11 → 13 px), fig-p597212-1.svg (15.2.1, 12–13 → 14.5 px), fig-p597212-2.svg (15.2.2, → 14 px, viewBox 0 55 832 447); each was changed by replacing the font-size attribute values in the live file and checked in the browser. New files 512792 (10.7 insulin animation, from Commons) and 512793 (11.6 OpenStax figure; copy in figures/pages/batchP/). The 14.3.2 strips have the 11 px label at 13 px (GitHub Pages, live on merge; page links `?v=20261113b`).
  - **Bank and exports (repo only; details in tools/BANK_FIX_2026-11-13.md):** 13 bank items reworded with no key changed; k cleared on fb-3B-0865/0871; all 36 QTI zips, the payloads and the CSV rebuilt from the bank and verified (0 banned terms, 0 mismatches); CSV writer fixed; IMF candidate builder now keys on c[0].
  - **Not done:** live ADAPT (23 questions listed in BANK_FIX); adapt/README.md counts; tools/adapt_thin.py still has the Ch 3 "extra" keying trap; 13.4 sulfonylurea image source; 14.5.2 (file unreadable today), 9.4 and 15.9.1 small print; 10.9 and 6.5 dead links; Final Boss and questionbank repos.

- **2026-11-13 Live ADAPT brought in line with the bank (course 4605):** 22 questions updated in place and read back matching the bank (ids and method in adapt/README.md). fb-3B-0887 no longer asks for Km; fb-3B-0872 and 0887 have new choices; the rest are stem or feedback wording. A re-scan of all 1,031 live questions finds no pKa, Km, hydride, meso, sp3 or ion–dipole wording and no pending revisions. Not updated: fb-3B-0979 (retired from assignments).

- **2026-11-13 PDF check of the 16:20 compile (1,340 pp; first compile with batches N, O and P):**
  - **Prints correctly:** every searchable text edit of batches N (42), O (8) and P (10); no old wording left. Version 1.2 on p2 and p11 and the 1.2 history entry (p15); Tables 13.7.1–2 and 13.8.1–2; Exercise 1.5.2 in the key; 3.4 Example 3 with the 1-butene drawing (p243); 11.1 "Interactive 3-D model" caption (p866); 12.8 raltegravir caption; Commons credits; the re-hosted 10.7 insulin and 11.6 allosteric figures (looked at in print); 15.2.2 (looked at). "Hydride" appears only as the NaBH4 "hydride reagent" (5.4) and "group 14 hydrides" (1.8). No missing-glyph boxes, raw MathJax or "Copyright" leftovers.
  - **Small print:** 31 pages with words under 6 pt (was 32). 13.4.2 now 5.7 pt (was 4.8); 15.2.2 is off the list and 15.2.1 is 5.9 pt (was 4.9); 14.3.2 label 5.7 pt (was 4.8); 9.3 sketch 5.4 pt (was 4.5). Unchanged: 14.5.2 at 4.8 pt, 15.9.1 at 5.1 pt, 9.4, 12.6, 13.5.
  - **Found:**
    - **The printed Index is LibreTexts' own tag-driven index** ("term, page title"), not the list on the Index page; that list does not print in the full compile. So the Index pointer fixes of batches C6, N and O and the nine new lines are not in print. A comparison of page tags with the corrected list (2026-11-13) shows 60 terms tagged on a different section than the list gives (for example allosteric enzyme 11.4 vs 11.6, reactive oxygen species 14.4 vs 13.6, hemoglobin 10.1 vs 10.9, ketone bodies 15.4 vs 15.5, urea cycle 15.8 vs 15.9). Fix: move those tags to the teaching pages. Not done.
    - 7.10 nylon synthesis figure (file 512727) still says "nylon-66" inside the drawing; the text and alt say nylon-6,6.
    - 9.3 Snake venom box: the photo prints large and the floated Figure 9.3.3 runs into the box (floats and max-width are not honoured in print).

- **2026-11-13 Index tags moved (live):** the printed Index is built from page tags, so 60 tags were moved to the page that teaches the term (list in tools/index_tag_moves_2026-11-13.json; 61 pages touched). Method: GET /@api/deki/pages/{id}/tags, then PUT the full tag list back as `<tags><tag value="…"/></tags>` with the one term removed or added; every other tag (licence, author, article type, source) was kept. Each page's tags were read back and match the plan. A re-comparison finds no term whose tag disagrees with the list on the Index page. Page bodies were not changed. Needs the next compile to confirm in print.
  - **Rule for later:** when a Glossary or Index pointer changes, move the page tag too; the list on the Index page does not print in the full-book PDF.


- **2026-11-13 PDF check, 16:37 compile (1,340 pages):** all 60 Index tag moves are in the printed Index, and no printed entry disagrees with the list on the Index page. Text and small-print checks are identical to the 16:20 compile.
  - **Finding:** the printed Index drops every tag that contains a plain hyphen. Nine Index-page terms were missing for that reason although their tags were live (omega-3 and omega-6 fatty acid 9.1; fluid-mosaic model 9.5; C-terminus and N-terminus 10.4; beta-pleated sheet 10.7; lock-and-key model 11.2; fat-soluble and water-soluble vitamins 11.5). Tags with an en dash do print (enzyme–substrate complex, cis–trans isomers, dipole–dipole attraction).
  - **Fix (live):** an en-dash copy of each of the nine tags was added on pages 597144, 597148, 597157, 597160, 597167 and 597170; the hyphen tags and all other tags were kept, and each page's tags were read back. Needs the next compile to confirm in print.

- **2026-11-13 Master refinement pass (branch audit/2026-11-master-refinement; nothing published):** deliverables in `audit/` (coverage ledger for all 199 pages, question ledger of 1,812 items, errata, pedagogy review, Rosa and Valley continuity, games and Try It validation, web/PDF/accessibility QA, licensing QA, implementation log, checkpoint).
  - **Found:** 24 inherited exercises with no answer on 12 pages (source-book markup the earlier counts missed); 74 of 103 bank-mode Try It boxes serving off-topic or not-yet-taught questions; duplicate screen-reader labels on 114 of 171 structure-choice questions; "This is version 1.1" left on About This Book; Rosa Part 15 manages vomiting with ketones at home (the emergency-department check was approved by the instructor the same day and is in batch Q); glossary pop-ups added by LibreTexts fail an ARIA rule and are mouse-only; 78 own pages print a blank author in the footer.
  - **Drafted, not live:** batch Q, 310 edits on 117 pages (`tools/batchQ_build.py`, review sheet `audit/BATCH_Q_REVIEW.md`).
  - **Fixed locally, not deployed:** `js/fbx.js` structure descriptions (`tools/check_struct_labels.js`: 0 duplicates).
  - **Published 2026-11-13 (instructor: "Publish batch Q"):** 310 edits on 117 pages; dry run matched all `before` hashes; every page read back identical. Index page 488231: 13 pointers follow the Glossary; the 13 page tags moved (`tools/index_tag_moves_batchQ_2026-11-13.json`). Single-page compiles of 4.5 and 4.2 show the new text and keys. Still held: seven Rosa story edits. Not merged: the `js/fbx.js` label fix.

- **2026-11-13 Footer author (live):** the 78 own pages printed "authored, remixed, and/or curated by ." because their `authorname:dkwasniewski` tag has no author record at LibreTexts. The tag `author@Daniel Kwasniewski` was added to all 78 on the instructor's OK (one test page first, then 77; list and method in `tools/author_tags_2026-11-13.json`). Each tag list read back as planned; no page body changed. The web footer and a single-page compile of 1.11 print the name. Needs the next full compile to confirm in print, including the four Malik pages (1.7, 9.4, 10.10, 13.5) whose footer was blank in the 16:37 PDF although the web footer names him.
  - Also on 2026-11-13: PR #51 merged (structure-label refinements, live on GitHub Pages) and Final Boss v41 pushed with the same code.

- **2026-11-13 Batch R drafted (branch content/2026-11-batchR; NOT published, NOT merged):** the open items left after batch Q, on the instructor's "fix everything" (author and cover items excluded). Review sheet: `audit/BATCH_R_REVIEW.md`.
  - **Page edits (95 on 54 pages, `tools/batchR_build.py`):** the seven held Rosa story edits; 3.2 heading levels; the 1.8 and 3.1 "open in a new tab" links, which still opened the old question filter; Try It titles on 6.1 and 12.2; one sentence in the accessibility statement about the platform's glossary pop-ups; "Think about it" questions for the ten Valley boxes that had none; one practice exercise for each of the 15 sections that had none (6.6, 8.3, 9.4, 10.7, 10.9, 11.1, 11.3, 11.5, 11.6, 12.1, 12.4, 12.7, 13.2, 15.6, 15.11), each with a print-key entry; Check steps for eleven Chapter Guide examples (1.9, 2.10, 3.9); fact fixes (14.4: −218 → about −220 kJ/mol; 14.3: step 5 wording and the step 4 oxidation; 7.4: "is a liquid" → "melts far below benzamide"; 9.5: bilayer about 4 to 5 nm); Try It boxes 1.3, 3.1 and 15.5 pointed at new questions; `chmax` added to the 13 cumulative mixes.
  - **Repo (live on merge):** 18 new bank questions (fb-3B-2238 to 2255: 8 Lewis, 6 alkene/alkyne naming, 4 ketone bodies), every key re-solved; every bank item now carries `sec` (first section that teaches it; `tools/bank_sec_tags_2026-11-13.json`); widget option `chmax=N`; answer-letter badge colours raised from about 3:1 to at least 4.8:1 contrast.
  - **Checked and left alone:** 11.4 cholinesterase thresholds match 3 CCR 6728 as amended effective 2023; 9.2 "about 20%" (Almanac 2023: 20.2%, from a search extract); 4.5 "about 40%" (Rwere et al. 2024); 10.5 "alkaloid reagents" is standard usage. Final Boss "1A-557 placeholder text" is a validator false alarm (it reads NaN in NaN3, sodium azide); its tab title is correct.
  - **Order to apply:** merge first (the 1.3, 3.1 and 15.5 boxes need the new question ids on GitHub Pages), check the live widget, then publish the pages.
  - **Not done:** the new questions are not in Final Boss or ADAPT; questions for the twelve thin topics; cutting duplicated inherited prose (14.2, 14.4, 15.4, 15.5, 15.6: the author's call); Study Hub address in print; the widget changes were not run in a local browser this time (the preview-server limit was reached), only simulated against the bank.
  - **Batch R published 2026-11-13 (instructor: "Merge and publish"):** PR #53 merged first (main 16375f2); live widget checked (new Lewis questions load with feedback; letter badges measure 4.8 to 5.7:1; 36 questions served from the Chapter 1-2 cumulative mix, none later than Chapter 2). Then the pages: dry run matched all 54 `before` hashes; **95 edits on 54 pages saved, every page read back identical**; `pages/live` synced by hash. Single-page PDF compiles of 8.3 and 4.9 were requested but the LibreTexts compile queue had not started them when this entry was written, so the print check waits for the next compile.

- **2026-11-13 PDF check, 18:19 compile (1,360 pages; first compile with batches Q and R and the footer author tags):**
  - **Prints correctly:** "This is version 1.2" (p. 15); the 24 exercise answers of batch Q with their keys (4.2, 4.4, 4.5, 4.8, 5.1, 6.1, 6.4, 6.5, 6.8, 7.1, 7.3, 7.7); Rosa Part 15 emergency-department check (p. 1233) and "Six months later" in Part 12; the fictional-patient line; all fifteen "Practice N.M" exercises of batch R with keys; the ten Valley "Think about it" questions sampled (2.6, 4.9, 15.7); Check steps (2.10, 3.9); 14.3, 14.4 (about −220 kJ/mol; no "218" left), 7.4 and 9.5 fact fixes; the accessibility sentence (p. 14); Glossary definition and Spanish edits (p. 1343); Try It titles on 6.1 and 12.2.
  - **Footers:** no page prints a blank name. The own pages print "Daniel Kwasniewski"; 1.7, 9.4, 10.10 and 13.5 print "Muhammad Arif Malik".
  - **Index:** the 13 moved terms print with the new sections (alkane 2.2, hydrocarbon 1.6, digestion 13.3, Cori cycle 13.8, molecular formula 1.7, condensed structural formula 2.4, substitution reaction 2.7, mitochondrial matrix 14.2, anticodon 12.5, ATP synthase, coenzyme Q and cytochrome 14.4).
  - **Found (my error in batch Q):** the equilibrium arrow in the new 6.4.1 and 6.8.1 answers was written `&#8652;`, which the PDF fonts lack; it prints as a box in four places (pp. 476, 479, 495, 500). Fix drafted as batch S (`tools/batchS_2026-11-13.json`: six replacements with MathJax `\(\rightleftharpoons\)` on 597112 and 597116). Not published yet.
  - **Unchanged:** cover author "Unknown" (waits for LibreTexts publication); 12 footer-only pages (was 15). No raw MathJax in the text. Small-print sizes were not re-measured in this check.
  - Note: on chapter landing pages the full compile hides the inline readiness answers and prints only the key, so the "If you missed it, review …" pointers there are web-only.
  - **Batch S published 2026-11-13 (instructor: "Publish the fix"):** the six `&#8652;` arrows on 6.4 (597112) and 6.8 (597116) are now MathJax; both pages matched their expected hash before saving and read back identical; `pages/live` synced. A single-page compile of 6.4 shows the arrow in the Exercise 6.4.1 key (page viewed) and no missing-character boxes. No `&#8652;` is left on any page.

- **2026-11-13 PDF check, 18:41 compile (1,360 pages; first compile with batch S):**
  - Text differs from the 18:19 compile on exactly four pages (476, 479, 495, 500): the equilibrium arrows in Exercises 6.4.1 and 6.8.1, inline and in the key. The missing-character boxes are gone and the arrow is drawn (pp. 476 and 500 viewed). No box or replacement glyph anywhere in the PDF.
  - Everything probed in the 18:19 check still prints (53 of 53 probes for batches Q and R; the three "not found" are old wordings that should be gone, and the web-only readiness pointer).
  - Footers: none blank. Version 1.2 on p. 15. Cover author still "Unknown" (waits for LibreTexts publication).
  - Footer-only pages: 12 (9, 179, 238, 278, 335, 366, 421, 563, 729, 951, 1163, 1330).
  - Small print: 30 pages have words under 6 pt (31 in the 16:20 check). Smallest: 14.5.2 malate-aspartate shuttle 4.8 pt (p. 1200), 15.9.1 urea cycle 5.1 pt (p. 1285), 9.1.6 5.3 pt (p. 715), 13.5.2 5.3 pt (p. 1094), 15.4.5 5.3 pt (p. 1259). These are the redraws already on the open list; no figure got smaller.
