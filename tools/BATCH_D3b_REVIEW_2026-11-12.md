# Batch D3b: tall diagrams print readably (review 2026-11-12)

LibreTexts' PDF caps each image at about 3 in high and at the text width (~6.65 in). Square or tall diagrams
therefore print with 3–5 pt text. Fix: cut each one along clean rows (no text line, no node box crossed; thin
arrows and panel backgrounds may be crossed) into strips at least ~2.3× wider than tall. On screen the strips
stack pixel-identically (checked by rendering); in print each strip prints at full text width.

| Section | Figure (file) | Strips | Print text now → after | Extra print length |
|---|---|---|---|---|
| 5.4 | hydrogenation.svg | 4 | 3.6 → 9.4 pt | +4.9 in |
| 12.4 | trna_loading.svg | 2 | 5.1 → 8.5 pt | +2.0 in |
| 13.1 | fig-p597188-1.svg | 2 | 5.6 → 7.8 pt | +1.2 in |
| 13.6 | fig-p597194-1.svg | 2 | 5.2 → 6.9 pt | +1.0 in |
| 13.6 | fig-p597194-2.svg | 2 | 5.5 → 7.2 pt | +0.9 in |
| 13.7 | fig-p597196-1.svg | 2 | 4.5 → 5.9 pt | +0.9 in |
| 13.7 | fig-p597196-2.svg | 3 | 5.4 → 8.5 pt | +1.7 in |
| 13.8 | fig-p597197-4.svg | 3 | 4.0 → 7.4 pt | +2.5 in |
| 14.3 | fig-p597202-1.svg | 2 | 3.2 → 5.6 pt | +2.3 in |
| 14.4 | respiration.svg | 3 | 4.2 → 7.2 pt | +2.2 in |
| 15.6 | fa_synthesis.svg | 2 | 4.1 → 6.7 pt | +1.9 in |
| 15.10 | fig-p597210-1.svg | 2 | 5.1 → 7.5 pt | +1.4 in |
| 15.11 | nonessential_aa.svg | 2 | 5.1 → 8.6 pt | +2.0 in |

Not done here (no clean cut row; need a redraw): 13.5 glycolysis flow chart (fig-p597193-1, 4.1 pt),
14.4 ATP synthase (atp_synthase.svg, 4.4 pt), 14.4 electron transport chain (etc.svg, 5.1 pt),
14.5 fig-p597204-1 (very wide, 4.9 pt), 14.3 wheel (author: leave). Skipped as marginal: 9.4 sphingolipids
(cut would split the structure), 7.12 reaction roadmap. Chapter concept maps print at 5.2 pt (wide; need larger type).

Cut-line previews: tools/batchD3b_review/cuts_*.png (red lines).
Strips are hosted on GitHub Pages (figures/print/), so they go live only after this branch is merged.
