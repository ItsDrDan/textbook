# fix_t3_ch7-9 notes (DRAFT, not published)

Script: `SCRATCH/fix_t3_ch7-9.py`. A dry run on the current live pages passed: 20 edits on 10 pages, each `old` found exactly once. The patched copies are in `SCRATCH/fix_t3_ch7-9_out/`. No repo files were touched.
Citation style: 597145's Valley box already has a numbered list, so it uses `<sup>`/list edits. Everything else uses an inline `(Source: Publisher, <a>Title</a>)`.

| # | P | Page | What changed | Source (re-verified 2026-11-18) |
|---|---|---|---|---|
| 1 | P2 | 597123 (7.3) | Nicotine lethal dose sourced; old figure "50 mg" → "50–60 mg" | Mayer B., Arch Toxicol 2014;88:5–7, PMC3880486 ("lower limit causing fatal outcomes is 0.5–1 g") |
| 2 | P2 | 597134 (8.1 text) | "about 60%–65% by mass of the average diet" → "about half of the calories in the average U.S. diet" + source | USDA ARS, What We Eat in America NHANES 2017–2018, Table 7 (adults ≈47% of energy from carbohydrate) |
| 3 | P2 | 597134 (8.1 Lecture) | "about 65% of the diet" → "about half of our calories (47% for U.S. adults)" | Same as #2 (cited once on the page) |
| 4 | P2 | 597141 (8.8 Key Idea 1) | "about 65% of the diet" → "about half of dietary calories" (no citation; the guide points to 8.1) | Same as #2 |
| 5 | P1 | 597136 (8.3 text) | Normal urine glucose "trace to 20 mg/dL" → "little or no glucose, 0–15 mg/dL" + source | MedlinePlus, Glucose urine test (0–15 mg/dL) |
| 6 | P2 | 597136 (8.3 Lecture, glucose box) | Source added for 70–99 / <70 / 100–125 / ≥126 | ADA Standards of Care 2026 §2 (Tables 2.1, 2.2; doi:10.2337/dc26-S002) and §6 (Table 6.4, Level 1 <70 mg/dL; doi:10.2337/dc26-S006) |
| 7 | P2 | 597136 (Artificial Sweeteners box) | "All of the extensive clinical studies … are safe" rewritten: IARC 2023 Group 2B, JECFA keeps ADI 40 mg/kg; closing safety sentence kept without "all studies" | WHO news release, 14 July 2023 |
| 8 | P2 | 597137 (8.4 Nursing) | HbA1c cutoffs sourced (inside the existing parentheses, after a semicolon) | ADA 2026 §2 |
| 9 | P1 | 597139 (8.6 To Your Health) | Galactosemia "1 in every 65,000" → "Classic galactosemia occurs in about 1 in 30,000 to 60,000 newborns" + source | MedlinePlus Genetics, Galactosemia |
| 10 | P3 (free link fix) | 597139 (8.6 Valley, source 2) | Link changed from the California index page to the Tulare County profile PDF | USDA NASS 2022 Census profile cp06107 (milk $2,814,167 thousand, rank 1 of 1,770) |
| 11 | P1 | 597144 (9.1 text) | "about 4–6 g of the essential fatty acids" → "about 12–17 g of linoleic acid and 1.1–1.6 g of α-linolenic acid each day" + source | Penn State Extension, Omega Fatty Acids (IOM Adequate Intakes); NIH ODS gives the same ALA values |
| 12 | P2 | 597145 (9.2 text) | PHO phase-out: "In 2015 the FDA ruled … phased out of U.S. foods by 2018–2021" + source | FDA, Final Determination Regarding Partially Hydrogenated Oils |
| 13 | P2 | 597145 (9.2 text) | Source added to "saturated fat at or below 10% of daily calories" | Dietary Guidelines for Americans 2025–2030 PDF (cdn.realfood.gov/DGA.pdf; "should not exceed 10% of total daily" calories) |
| 14 | P2 | 597145 (Valley) | "Tulare County's milk was worth about $2.3 billion" → "Tulare County sold about $2.8 billion of milk in 2022, more than any other U.S. county" | USDA NASS 2022 Census, Tulare profile |
| 15 | P2 | 597145 (Valley, source 2) | GV Wire (news) → Fresno County 2024 Annual Crop & Livestock Report; USDA NASS Tulare profile (one numbered entry, so no renumbering) | See the flag below on the Fresno PDF |
| 16 | P1 | 597145 (Valley, source 5) | Broken uidaho.edu link → https://doi.org/10.3168/jds.2014-7919 | Loften et al., J Dairy Sci 97:4661–4674 (2014) |
| 17 | P2 | 597146 (9.3 IRDS) | "highest before about 28 weeks … up to about 34 weeks" → "The earlier a baby is born, the higher the risk; the problem is uncommon in babies born at 39 weeks or later" + source | MedlinePlus, Neonatal respiratory distress syndrome |
| 18 | P2 | 597149 (9.6 Lecture) | Source added to the lipid-panel targets | MedlinePlus, Cholesterol Levels: What You Need to Know (all numbers match) |
| 19 | P2 | 597149 (9.6 text) | DELETED the sentence: NIH "five times greater" (men 30–49, >260 vs ≤200) | No source with this figure could be found |
| 20 | P2 | 597149 (9.6 text) | Outdated averages (170; 250 at age 55; "females tend to have lower") → NCHS 2021–2023: 11% of adults have high total cholesterol, men 40–59 highest (18%), no overall sex difference | CDC NCHS Data Brief 515 (Nov 2024) |

## For the author to decide or check
- **#15, Fresno 2024 report:** the PDF is too large for my fetch tool. The $1.45 B almond value and its No. 1 rank were confirmed only through Agri-Pulse and The Business Journal reports of that county report. Open the PDF once to confirm.
- **#14, Tulare milk:** I switched to the 2022 Census figure because the official Tulare 2024 report site refused my fetch (403). Valley Voice reports $2.27 B for 2024. If you prefer the 2024 number, cite the Tulare County 2024 Crop & Livestock Report after opening it.
- **#17, IRDS:** the 28- and 34-week cutoffs were dropped because no reachable source gave them (StatPearls was blocked by a CAPTCHA). Put them back if you have a source you trust (for example, StatPearls NBK560779: about 98% at 24 weeks, 5% at 34 weeks).
- **#7, sweeteners:** the last sentence ("considered safe for healthy people in moderate amounts") is your original claim without the "all studies" part. It stands on the WHO/JECFA source for aspartame only; FDA's own statement page URL now returns 404.
- **#16, Loften:** the paper confirms palmitic acid is the most abundant fatty acid in milk fat. "Oleic second" was seen only in a truncated abstract snippet.

## Skipped
- All P3 items in the audit except the free link fix #10. Not done: ChemistryViews Part 3 check, Almanac host and Fresno 20% share, Textile Exchange 6%, LBNL, caffeine, cartridge pH, cocaine 15 s, sweetener dates, tomato-juice methanol, Stephan curve, lactose 40%, nylon 1935, Friedewald, 597131 sup anchors, and the open-chain-fraction consistency.
- 597141 Chapter Guide glucose and HbA1c numbers, and 597142 practice problems: no citation added. The numbers are correct and are sourced in 8.3 and 8.4.
- 597145 Lecture Connection repeats the PHO phase-out: left uncited, since the same page now cites it in the section text.

## Other chapters' pages
The whole live page set was grepped for the corrected numbers ("65% of the diet", "65,000", "20 mg glucose", "4–6 g of the essential", the nicotine lethal dose, "five times greater", "average about 170"). No occurrences were found outside the pages edited here.
