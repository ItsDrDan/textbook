# fix_t5_ch13-15 notes (2026-11-18)

Script: `SCRATCH/fix_t5_ch13-15.py`. It defines 12 `e()` edits. A dry run applies them in memory to the current `pages/live/*.html`, and all 12 matched exactly once. Edits JSON: `SCRATCH/fix_t5_ch13-15.json`. No repo file was written.

Every source below was re-checked on 2026-11-18 against the exact sentence it supports.

| # | P | Page | Change | Source |
|---|---|---|---|---|
| 1 | P2 | 597192 (13.4 To Your Health) | Cites the complications list (amputations, blindness, kidney failure) | CDC, About Diabetes ("the No. 1 cause of kidney failure, lower-limb amputations, and adult blindness") |
| 2 | P1 | 597192 | "increases the risk… by two to four times" → "doubles the risk of heart disease and also raises the risk of stroke" | CDC, Diabetes and Your Heart ("twice the risk for heart disease"; no stroke multiplier given, so the stroke wording is qualitative) |
| 3 | P1+P2 | 597192 | "about 38 million" → "40.1 million Americans, 12.0% of the population, had diabetes in 2023"; the 90–95% type 2 share now says "of diagnosed diabetes" and is cited | CDC National Diabetes Statistics Report (updated Sept 16 2026: 40.1 million, 12.0%, 2023 data); CDC About Diabetes ("about 90% to 95% of all diagnosed cases") |
| 4 | P2 | 597195 (13.9) | Links the ADA "15-15 rule" | ADA, Hypoglycemia (Low Blood Glucose) ("15/15 rule of 15g fast-acting carbs/15 minutes"; below 70 mg/dL) |
| 5 | P2 | 597195 dental box | "periodontal treatment measurably improves glucose control" → "lowers HbA1c by about 0.4 percentage points on average", cited | Simpson TC et al., Cochrane 2022, CD004714.pub4 (HbA1c 0.43% lower at 3–4 months, moderate certainty) |
| 6 | P2 | 597053 (Rosa Part 15) | "Studies suggest that treating gum disease can modestly improve…" → "Treating gum disease can modestly improve… (Source: Cochrane review…)" | Same Cochrane review |
| 7 | P2 | 597209 (15.4) | Deleted "In earlier times… about 20%…" (no source). The sentence is now "Today about 36% of the food calories eaten in the United States come from fat." | USDA ARS, What We Eat in America, NHANES 2017–2018, Table 5 (total fat 36% of energy, ages 2+ and adults 20+) |
| 8 | P2 | 597209 | Links "According to NIH, nearly 3 out of 4 adults…" | NIDDK, Overweight & Obesity Statistics (30.7% + 42.4% = 73.1%, adults 20+) |
| 9 | P2 | 597213 (15.5 Valley box) | Deleted the "2020 community health assessment… 12%… 9.8%" sentence | Could not be verified: the PDF's TLS certificate was rejected and no search result confirms the numbers. The PLACES 2023 sentence already makes the point. |
| 10 | P2 | 597213 | Removed Sources item 4 (2020 CHNA); it was the last item, so nothing is renumbered | — |
| 11 | P2 | 597208 (15.8 Career Focus) | "must be referred" → "Many patients are referred by a physician"; dropped the retired "registered clinical exercise physiologist" title; degree sentence rewritten and cited | BLS Occupational Outlook Handbook, Exercise Physiologists ("Most need at least a bachelor's degree…"; physicians "may… refer them") |
| 12 | P3 (free) | 597211 (15.1 Fig. 1 credit) | IntechOpen link changed to https://www.intechopen.com/chapters/39567 | Old URL 301-redirects there; same chapter (doi 10.5772/50622) |

## Checked, nothing else to change
I searched all live pages for the corrected numbers: "38 million", "two to four times", "3 out of 4 adults", "20% of food calories" and "registered clinical exercise physiologist". Each one appears only on the page edited above. None appear on Practice Problems pages or on other chapters' pages.

## Skipped (P3, not approved)
- 597213 Source 2 (Chiasson, CMAJ 2003): outdated, with the 2024 consensus as replacement. The link returns 403 rather than being dead, so it was left as is.
- 597203 SB 183 floor analysis (contradicts itself): text is correct, source swap is P3.
- 597193 ChemistryViews links (403, possibly moved): needs a browser check.
- 597195 Source 6 StatPearls author list: needs a browser check.
- C4 (pH "as low as 6.9"), C5 (TAG 98%), C6 (BMI "over 30"), plus the optional history, physiology and label sources.

## For the author to decide
- Edit 2: CDC gives no number for stroke, so the stroke clause says only "raises the risk". To keep a number, you would need a different source (for example AHA).
- Edit 7: the historical "earlier times… 20%" comparison is gone. Restoring it needs a historical diet source.
- Edit 9: if you can open the 2020 CHNA PDF and confirm 12% and 9.8%, the sentence and Source 4 can stay instead.
