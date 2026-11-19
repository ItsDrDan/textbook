# fixp3_t5_ch13-15 notes (Round 2, P3 polish, 2026-11-18)

Script: `SCRATCH/fixp3_t5_ch13-15.py`, 23 `e()` edits. The dry run on the current `pages/live/` (after batch AP, with round-1 edits already live) matched all 23 exactly once. Edits JSON: `SCRATCH/fixp3_t5_ch13-15.json`. No repo file was written.

| # | Page | Change | Source (re-verified) |
|---|---|---|---|
| 1 | 597213 Valley box | "in DKA the blood pH is 7.30 or lower.<sup>2</sup>" → "falls below 7.3.<sup>4</sup>" | Umpierrez GE et al., Diabetes Care 2024 consensus: pH <7.3 and/or HCO3 <18. Confirmed through the ACP Diabetes Guide and CCJM 2025 summaries; the publisher pages return 403. |
| 2 | 597213 Valley box | Fluids: "isotonic saline (0.9% NaCl) or a balanced salt solution such as lactated Ringer's" | 2024 consensus: saline or balanced crystalloids, with balanced preferred when available (CCJM 2025 summary) |
| 3 | 597213 | Potassium sentence now cites <sup>1,2,4</sup> | Chiasson (insulin only after K+ is above 3.3); 2024 consensus (insulin only after K+ is above 3.5) |
| 4 | 597213 | Chiasson 2003 link changed to the open PMC151994 copy (the CMAJ PDF returns 403) | PMC151994 loads and supports pH ≤7.30, breath acetone, the named ketone bodies, saline, low-dose insulin and the potassium rule |
| 5 | 597213 | Added Source 4: Umpierrez 2024 consensus, doi 10.2337/dci24-0032 (number 4 was freed in round 1) | as above |
| 6 | 597213 anion-gap box | MSD Source 2 updated to the new URL with title "Acute Complications of Diabetes Mellitus" | New URL loads; H1 confirmed; still says "Anion gap > 10 to 12" |
| 7 | 597213 main text | "as low as 6.9" → "below 7.3, and in severe cases below 7.0", with inline citation | 2024 consensus |
| 8 | 597203 CO box | Source 6: SB 183 floor analysis replaced by H&S Code §17926 (official leginfo URL) | Statute text read via FindLaw: fossil fuel appliance, fireplace or attached garage; single-family by Jul 1 2011; other units by Jan 1 2013. The page text needs no change. |
| 9 | 597203 lecture table | DNP "led to its ban" now cited | Grundlingh 2011 J Med Toxicol (PMC3550200): "not fit for human consumption" in 1938 |
| 10 | 597203 | "almost 90% of the body's oxygen use" → "uses most of the oxygen the body takes in" | No source found for 90%; rewritten as a qualitative statement |
| 11 | 597201 | "about 30% … almost 90%" → "only a modest share … most of the oxygen the body takes in" | Same; neither number could be verified (the Zurlo 1990 abstract gives no %) |
| 12 | 597201 | Krebs 1937 / 1953 Nobel Prize cited | NobelPrize.org facts page. Confirmed via search; the site returns 403 to automated fetch. |
| 13 | 597201 | Mitchell 1978 Nobel Prize in Chemistry cited | NobelPrize.org (same caveat) |
| 14 | 597206 | DNP diet-pill history (practice problem) cited | Grundlingh 2011 |
| 15 | 597211 | TAG share 98% → 95%, cited | Wang TY et al., Eur J Clin Invest 2013 (PMC3996833): "~95% of dietary lipids are triacylglycerols" |
| 16 | 597218 | Chapter Guide 98% → 95% (summary text, so no second citation) | same |
| 17 | 597209 | BMI: "25.0 to 29.9 is overweight, and 30 kg/m² or higher is obese" | NIDDK (already cited in the same paragraph) |
| 18 | 597192 | "automobiles are only about 20%–25% efficient" → "only about 12%–30% of the energy in gasoline is used to move a car down the road", cited | fueleconomy.gov (DOE/EPA): "Only about 12%–30% of the energy…" |
| 19 | 597191 | Lactase decline: "(about 65% of people)", cited | MedlinePlus Genetics: "Approximately 65 percent of the human population…" |
| 20 | 597194 | Galactosemia on every state's newborn screening panel, cited | Pyhtila 2014 JIMD Rep (PMC4413015): "By 2004, essentially all infants born in the USA were screened for galactosemia" |
| 21 | 597216 | OTC deficiency as the most common urea cycle disorder, cited | Batshaw 2014 Mol Genet Metab (PMC4178008): "The most common disorder is ornithine transcarbamylase deficiency" |
| 22 | 597193 | Credit: "adapted from a public-domain resource at Wikipedia" → "adapted from the Italian Wikipedia article Glicolisi, CC BY-SA 4.0" | The adapted item is article text (the step list), not a Commons image; the step figures are DK's own SVGs. The it.wikipedia footer says CC BY-SA. |
| 23 | 597202 | Credit: "a public-domain source on the Russian-language Wikipedia" → "the Russian-language Wikipedia article on the citric acid cycle (CC BY-SA 4.0)" | The adapted items are the reaction equations and text; the figures are DK's own SVGs. The ru.wikipedia footer says CC BY-SA. |

## Skipped and why
- **597195 Source 6 (StatPearls author list):** I could not confirm the current byline. NCBI shows a CAPTCHA, and statpearls.com returns 403. An older version lists Mathew TK, Tadi P, and Zubair M appears as editor. Someone needs to check it in a browser; I did not guess.
- **597193 ChemistryViews "Further reading" (3 links):** the site returns 403. Search shows Part 2 at chemistryviews.org/?p=39767 and Part 3 at ?p=39764, but I could not find Part 1's new URL. A browser check is needed before swapping any of them.
- **597203 Sources 1 and 2 (CDC, "2024"):** no change. 2024 is the original publication date; the pages were updated in 2026. Either year is defensible.
- **Optional citations not added** (textbook-level, or a reader is unlikely to ask "says who?"):
  - fever raising metabolic rate about 10% per °C (597195, 597203)
  - propofol 1.1 kcal/mL and lipid emulsion 2 kcal/mL (597212)
  - metformin lactic-acidosis risk factors (Rosa Part 14; 597197)
  - ADA sick-day plan (Rosa Part 15)
  - "126 on two occasions" (597195; the CDC cutoffs are already cited in the Valley box)

## Needs the author
1. **597213, ketone body levels:** "kidneys excrete about 20 mg of ketone bodies each day… about 1 mg… per 100 mL". This is inherited from the Ball text and I found no modern source. MedlinePlus gives no number. Keep it, delete it, or replace it with a lab reference value of his choice.
2. **597213, anion-gap example:** "DKA is diagnosed with a gap above about 10 to 12". MSD still says this, but the 2024 consensus no longer uses the anion gap as a first-line criterion; it relies on ketones plus pH or bicarbonate. He could add "(older criterion; current guidelines use ketones and pH)" or leave the example as is.
3. **Licensing, 597193 and 597202:** both pages are CC0-based, and the step list and equations are credited to Wikipedia text under CC BY-SA 4.0, which carries ShareAlike terms. He should decide whether the current, heavily rewritten wording is still an adaptation. If it is, BY-SA applies to that part. If not, the credit can be dropped.
4. **597201 and 597203, muscle oxygen:** I removed the numbers (30% at rest, about 90% working) because I could not verify them. If he wants numbers back, they need a physiology source.
