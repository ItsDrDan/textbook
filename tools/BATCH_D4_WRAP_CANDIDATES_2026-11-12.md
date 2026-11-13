# Batch D4: figure-wrap candidates (review 2026-11-12)

No image in the book floats in the PDF. A narrow figure therefore sits alone on its row with blank space beside it.
The tested fix (already used on 1.8, Figure 1.8.9) is an inline float: the PDF honours inline styles, and a
page-style rule un-floats it on phones. Wrapping does not change a figure's size; it lets text run beside it.

Source: full-book PDF of 2026-11-12 00:50, every raster image narrower than 3.3 in that prints alone on its row
(152 images). Uncaptioned structure images inside worked examples (about 110) are left out: they illustrate a step,
and text beside them would split the example. Numbers below are current (after the C1 renumbering).

## Group A: already float on screen, not in print (26 images, 7 pages)

These carry LibreTexts' `internal left` / `internal right` classes, which the PDF ignores, so in print the next
paragraph starts at the image's bottom edge and leaves a blank block beside it (review: pp.716–812).

Recommended: make them float in print too (inline `float` + `max-width:45%` + margin):
- 1.4: the polar H–Cl bond figure (Figure 1.4.2)
- 9.3: phospholipid space-filling model; snake venom photo; lysophospholipid; phosphatidic acid
- 10.6: sickle-cell illustration
- 10.7: α-helix model; β-sheet ribbon; antiparallel and parallel β-sheet drawings
- 13.1: digestive system; animal cell; mitochondrion cutaway
- 14.4: coenzyme Q; heme of cytochrome c
- 15.4: the four animal photos (polar bears, orca, camel, geese)

Not recommended (large diagrams that print better full width; remove the float class instead, so the
screen matches print):
- 13.1: overview of metabolism; stages of food catabolism
- 14.4: Complex I, Complex II, Complex IV, ATP synthase, summary of glucose catabolism

## Group B: captioned figures that print alone and narrow (19 recommended)

Photos and simple drawings that read well at their current size:

| Section | Figure | Printed size (in) |
|---|---|---|
| 1.4 | Linus Pauling photo | 1.95 × 3.0 |
| 1.7 | Figure 1.7.2 (n-hexane models) | 1.18 × 1.13 |
| 1.8 | Figure 1.8.3 (sodium chloride) | 2.6 × 2.47 |
| 1.8 | Figure 1.8.10 (DNA double strand) | 1.94 × 3.0 |
| 2.6 | Figure 2.6.1 (oil spill photo) | 2.2 × 3.0 |
| 2.9 | Figure 2.9.1 (cyclopropane model) | 2.25 × 1.91 |
| 4.3 | Figure 4.3.2 (ethanol–water hydrogen bonding) | 2.63 × 3.0 |
| 5.4 | Figure 5.4.2 (Tollens' test photo) | 2.11 × 1.72 |
| 7.10 | Figure 7.10.3 (nylon spatula photo) | 1.5 × 2.0 |
| 8.3 | Figure 8.3.1 (food sources of hexoses) | 1.77 × 2.69 |
| 8.3 | Figure 8.3.2 (Fischer projection of D-glucose) | 1.56 × 2.69 |
| 9.3 | Figure 9.3.3 (lipid bilayer cross-section) | 2.42 × 2.37 |
| 9.5 | Figure 9.5.2 (monolayer, micelle, bilayer) | 1.8 × 3.0 |
| 10.5 | Figure 10.5.2 (α-helix ball-and-stick) | 2.38 × 3.0 |
| 10.6 | Figure 10.6.2 (disulfide linkages) | 2.74 × 3.0 |
| 10.10 | Figure 10.10.2 (amyloid plaque formation) | 2.82 × 3.0 |
| 12.2 | Figure 12.2.2 (DNA double helix) | 2.66 × 3.0 |
| 12.8 | Figure 12.8.1 (viruses) | 2.99 × 3.0 |
| 4.7 | Figure 4.7.1 (phenol structure and photo) | 2.0 × 2.3 |

Not recommended: their text is already small in print, and wrapping invites further shrinking:
- 2.8 ozone map (its legend is already unreadable)
- 9.3.1 phospholipid structure; 9.4.2 sphingomyelin; 10.5.5 and 10.5.6 (tertiary and quaternary structure)
- 10.7.1 (three thin panels)
- 12.1.2 nucleotides; 12.2.1 DNA segment; 12.2.4 base-pair widths; 12.4.5 codon table; 12.6.3 genetic code; 12.7.1 mutations
- 13.3.1 and 13.3.2; 15.4.1 β-oxidation; 15.7.1 protein digestion

Already done: 1.8, Figure 1.8.9 (methanol).

Pick any subset; the edits are mechanical (one inline style per figure plus the phone rule in the page style block).
