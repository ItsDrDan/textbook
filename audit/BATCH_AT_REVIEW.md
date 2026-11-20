# Batch AT review: final accessibility and reviewer-readiness fixes, 2026-11-20

Published 2026-11-20 (338 edits on 163 pages; uploaded image = file 512954; live hashes checked, local copies synced; LibreTexts adds its CDATA wrapper to the new style and reordered one img attribute on 5.2).  Found by the checks in audit/FINAL_VERIFICATION_2026-11-20.md.

| # | Where | Change | Why |
|---|---|---|---|
| 1 | 11.1 Enzymes, Figure 1 | The GLmol 3-D viewer (its three scripts at libretexts.org/awesomefiles/GLmol now return 404) is replaced by the RCSB PDB image of alcohol dehydrogenase, entry 1CDO (CC0), with alt text, a new caption and a link "Rotate the 3-D model at the RCSB Protein Data Bank". Citation: Ramaswamy et al., Protein Science 5, 663–671 (1996). | The page showed a caption with no figure, on the web and in print. |
| 2 | 95 pages, 180 tables | `tabindex="0"` on side-scrolling tables (`mt-responsive-table`) | On phones and at 400% zoom these tables scroll sideways; a keyboard user could not scroll them (WCAG 2.1.1; axe scrollable-region-focusable). Tables keep their captions as names. |
| 3 | 69 pages, 109 figure boxes | `tabindex="0" role="region" aria-label="Wide figure: scroll sideways"` on `div.fig-scroll` | Same problem for the side-scrolling figures from the phone-figure batches. |
| 4 | 131 pages, 1,640 controls | Screen-only style: Hint/Answer `<summary>` becomes a 44 px outlined button with ▸/▾ (arrow hidden from screen readers), focus ring, shaded when open. Print unchanged. Same rule as the CHEM 3A book (approved there 2026-11-19). Checked: no glossary word occurs in the style text. | LibreTexts shows "Answer" as a plain 47×18 px word: under the WCAG 2.2 24 px target size and not visibly tappable. |
| 5 | 12.3 DNA Replication | List closed before the replication-fork figure | The figure sat inside a `<ul>` (invalid list; screen readers counted it as a list item). |
| 6 | 15.4 Oxidation of Fatty Acids | "Fat and obesity" box title h4 → h3 | Heading skipped a level. |
| 7 | 12.2 Nucleic Acid Structure | Empty duplicate `<ul id="gob-ch19_s02_s02_l04">` removed | Duplicate id. |
| 8 | 5.2 Properties of Aldehydes and Ketones, Figure 1 | Image gets max-width 100% | Caption ran 11 px past a 320 px screen. |
| 9 | Course Outline Alignment | Caption on the lab-manual table | Only table in the book without a caption. |
| 10 | 11.6 Enzyme Regulation | `\ ` → `\;` in the A → B → C → D pathway (9 places) | MathJax speech reads `\ ` as "empty". |
| 11 | 1.9, 2.10, 8.8 (videos); 12.6, 14.1, 14.2 (VCell) | rel="noopener" on 9 new-tab links; leftover Google search attributes removed from the VCell links | Security best practice; consistency. |

Publishing note: post one table page first and confirm LibreTexts keeps `tabindex`/`role`; stop if it strips them.

## Batch AT2 (follow-up, published 2026-11-20)

142 edits on 70 pages (`tools/batchAT2_build.py`): every side-scrolling figure region gets its own name ("Scroll sideways: " + the start of its figure's alt text; repeats numbered), the 32 `<span class="fig-scroll">` boxes on 13.4, 13.5, 14.2, 14.3, 15.4 and 15.8 become focusable named regions, and so does the 3.7 bromination reaction row. On save LibreTexts writes …, α, β and – inside attributes as named entities; local copies include that and match live hashes.
