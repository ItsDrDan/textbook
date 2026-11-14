# Licensing and attribution QA (master refinement pass, 2026-11-13)

No licence was changed in this pass, and no third-party figure, question or text was imported.

## Model in force (college OER coordinator, recorded 2026-11-11)

- Book front page: CC BY 4.0 unless otherwise indicated.
- Pages adapted from Ball, Hill and Scott or from *Fundamentals of GOB* (LibreTexts): CC BY-NC-SA 4.0 at page level. Blocks marked as the author's own keep CC BY 4.0.
- Third-party figures keep their own licence in the caption.
- Question bank and its ADAPT copies: CC BY 4.0. Games and game code: © ItsDrDan, all rights reserved; linked and embedded, not part of the licensed text.

## Checks run in this pass

| Check | Method | Result |
|---|---|---|
| Page licence vs source note | For each page, the licence in the PDF footer ("This page titled … is shared under …") was compared with the page's own "Adapted from …" note. | 186 of 199 footers parsed (95 CC BY 4.0, 91 CC BY-NC-SA 4.0). **0 mismatches:** every page whose adapted note names an NC-SA source prints NC-SA, and no own page prints NC-SA. The 13 not parsed are five container pages with no footer and eight whose title did not match the script's pattern (1.2, 1.3, 4.1, 4.2, 5.1, 5.2, and the Chapter 4, 14 and 15 guide/problem pages); not checked by hand. |
| Counts stated in Detailed Licensing | The brief quotes 104 CC BY 4.0 / 95 CC BY-NC-SA 4.0 of 199. | Not re-derived: the 13 unparsed pages keep this pass from confirming either number. |
| Licence strings in captions and credits | keyword count over all pages | CC BY 4.0 ×883, CC BY-NC-SA 3.0 ×329 (source figure credits), CC BY-NC-SA 4.0 ×101, public domain ×96, CC0 ×73, CC BY 2.0 ×11, CC BY 3.0 ×4, "all rights reserved" ×4 (the games). **No CC BY-SA and no ND material** remains (batch E removed the last BY-SA images). |
| Captions without a credit | `<figure>` elements whose caption has no credit wording | 67 of 506. Consistent with the earlier finding that most are inner panels of credited composites or the author's own drawings; the one known unknown is the 13.4 sulfonylurea image (LibreTexts file 128222, source not identified). Unchanged. |
| Blank author in page footers | PDF text | 78 own pages print "curated by ." (see the web/PDF file). This is attribution metadata, not a licence problem, but the author's name should print on his own pages. |

## Effect of this pass on licence boundaries

- **Batch Q edits inside NC-SA pages.** The answers added to inherited exercises, the reworded inherited sentences and the corrected worked examples sit inside pages that are CC BY-NC-SA 4.0. They are adaptations of NC-SA text and take that licence; the existing page note ("The text was edited for CHEM 3B by Daniel Kwasniewski …") already covers edits of this kind. No own-work CC BY label is added to them.
- **Try It selections** are URL parameters; no licensed content moves.
- **`js/fbx.js`** (game code, all rights reserved) was edited in this repo; the README says to edit the Final Boss source first and copy here. The new description code must be carried back to `finalexam` so the two stay the same.
- **Valley Connection sources:** two replacement citations (a California Watch news story; a PLoS ONE paper, CC BY) are cited and linked, not copied.
- **Glossary:** Spanish equivalents are single terms, the author's own.

## Open items (unchanged from earlier passes)

- 13.4 sulfonylurea image: source unknown.
- Cover author "Unknown" and the blank footer names: LibreTexts metadata.
- Independent confirmation of the 104 / 95 split after the next compile.
