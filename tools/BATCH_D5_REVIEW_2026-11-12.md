# Batch D5: print layout leftovers (review 2026-11-12)

Edit list: tools/batchD5_fixes_2026-11-12.json (13 edits on 12 pages, replay-checked against pages/live).

1. **Garbled exercise headings ("1.1.2Exerc"):** six boxes use a `<header><h5 class="editable">` form instead of the standard `<h5 class="box-legend editable">`. Converted to the standard form: 1.1 Exercise 2, 1.3 Exercise 2, 1.5 Exercise 1, 1.8 Exercises 1 and 3, 6.9 Exercise 1. Content unchanged.
2. **1.7 "Four ways to draw the same molecule" table:** cut off at the right margin. The structure images go from 218/218/141 px to 160/160/104 px (the width attribute is the print maximum), so all four columns fit.
3. **Table 11.1.2:** the 976 px reaction image had no width and pushed the table past the margin; it gets width 440.
4. **Stranded drawn-example labels** (2.10, 3.9, 4.11, 5.6, 6.11, 7.12; 30 labels): `page-break-after:avoid` on each bold label, so it stays with its drawing.

Checks after publishing: SHA-256 per page, and one-page compiles of 1.1, 1.7 and 11.1.
