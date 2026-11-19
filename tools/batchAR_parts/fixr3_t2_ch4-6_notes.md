# fixr3_t2_ch4-6 notes (ROUND 3: local primary sources, Chapters 4–6)

**Script and test**
- Script: `SCRATCH/fixr3_t2_ch4-6.py`. It tests the edits in memory against the current `pages/live` (batch AQ live) and writes `SCRATCH/fixr3_t2_ch4-6.json`.
- 5 edits, all OK. The test also confirms no GV Wire link is left on 597098 or 597113.
- No repo file was written.
- I grepped every page for garlic/peach numbers or Fresno top-ten claims. Only 597098 and 597113 carry them. No Practice Problems or other chapters repeat them.

**Primary sources read** (downloaded to `SCRATCH/dl/` with curl, read with PyMuPDF)
- **CDFA, *California Agricultural Statistics Review 2023–2024*** (PDF dated 2025-09; the newest edition listed on cdfa.ca.gov/statistics). Printed page numbers:
  - **p. 9:** California supplies "99 percent or more of the nation's exported … garlic".
  - **p. 12** (table "Commodity Rank, Acreage, Production, and Value, 2023"): garlic, CA rank 1, CA share of U.S. receipts 100.0%, value $311,708,000.
  - **p. 23** (Leading Commodities by County, 2023): Fresno #8 Peaches $352,946,000, #9 Garlic $309,396,000.
  - **p. 27** (Leading Counties by commodity, 2023): Garlic: Fresno 62.7%, Kern 25.6%. Peaches: Fresno 47.0%, Tulare 19.5%.
- **CDFA *Review 2022–2023*** (the old fn 3 on 597098) is now verified too:
  - p. 100: "In 2022, the total value of garlic was $309 million".
  - p. 10: 99% of exports.
  - p. 24: Fresno 2022 top ten has #8 Garlic and #9 Peaches.
  - It is superseded by the 2023–2024 edition.
- **USDA AMS 2024 raisin hearing, Exhibit 7** (M. Schutz, RAC), now read in full:
  - p. 1: the five counties, "biggest production in Fresno & Madera Counties", "about 1,500 producers".
  - p. 2: "approximately 86% of raisins sold in the US are California Raisins".

| # | Page | What changed | Source |
|---|---|---|---|
| 1 | 597098 (4.9 Valley Connection) | Garlic paragraph rewritten (see list below) | CDFA Review 2023–2024 pp. 9, 12, 23, 27 |
| 2 | 597098 Sources | UC Davis 2007, GV Wire and CDFA 2022–2023 replaced by two CDFA 2023–2024 entries: 1 = pp. 9, 12; 2 = pp. 23, 27, county commissioners' data, 2023 | as above |
| 3 | 597113 (6.5 Valley Connection) | "Peaches are also among Fresno County's top ten crops" + ", and the county grows nearly half of California's peaches by value" | CDFA Review 2023–2024 pp. 23 (Fresno #8 peaches) and 27 (Fresno 47.0%) |
| 4 | 597113 Sources fn 4 | GV Wire replaced by CDFA Review 2023–2024, pp. 23 and 27 | as above |
| 5 | 597113 Sources fn 2 | ", pp. 1–2" added to the raisin hearing exhibit | Exhibit 7, read in full |

Edit 1 in detail (597098):
- "California grows most… (86%, by a 2007 UC Davis estimate)" became "California grows nearly all of the nation's garlic", followed by:
  - 2023 crop value about $312 million;
  - share of U.S. garlic sales listed as 100%;
  - 99%+ of U.S. garlic exports.
- "Garlic was one of Fresno County's ten highest-value crops in 2024" became "Fresno County alone grew about 63% of the state's garlic by value, and garlic was one of the county's ten highest-value crops." Both now refer to 2023.

## "In 2024" vs "in 2025": not decided from the county report (blocked)
- **What I tried:**
  - Direct curl of both Fresno County reports (2024: ag-crop-and-livestock-report_2024.pdf; 2025: ag-crop-and-livestock-report-2025.pdf) returns **403 Access Denied** from the county's Akamai edge.
  - A copy via the Internet Archive was refused by the session's permission classifier, so I did not pursue it further.
  - I did not try to get around the block.
- **What I did instead:** the text now uses **2023**, the newest year in a primary source I could read: CDFA's county-commissioner tables, which are compiled from the county crop reports.
- **News reports of the 2025 Fresno report** (KMPH, Nov 3, 2026): total $9.64 B, peaches 8th, garlic 10th. Both crops are still top ten.
- **If the author wants 2025:** someone downloads the report in a browser and confirms the top-ten page and garlic/peach values. Then:
  - On 597098, change "garlic was one of the county's ten highest-value crops" to say "in 2025".
  - Add a source: "Fresno County Department of Agriculture, 2025 Crop &amp; Livestock Report, 2026, p. N".
  - Same on 597113.
  - I can draft that edit once the page number is known.

## Other Valley numbers checked
- **597094 District 13 crush:** already a primary source (USDA NASS/CDFA Final Grape Crush Report 2025: 802,609 of 2,761,914 t). CDFA Review 2023–2024 p. 82 has only 2023 crush data, so no change.
- **597113 raisin counties, 1,500 growers, 86%:** the industry's own figures (RAC testimony), now verified with pages. CDFA reviews report raisin grapes statewide only, with no county split. No Kern, Tulare, Kings, Madera or Merced county report states these numbers in a form I could find, so no extra local source was added.
- **Kern/Tulare/Kings/Madera/Merced county reports:** not needed for any Chapter 4–6 sentence. The only county-level claims in these chapters are Fresno's, and CDFA p. 27 covers the other counties' shares (Kern 25.6% of garlic, Tulare 19.5% of peaches) if the author wants to mention them.

## Outside this group (not edited)
- 597156 also cites the CDFA *Review 2022–2023*. A newer 2023–2024 edition exists. That page belongs to another group.

## For the author
- **"Most" → "nearly all", and the 2007 "86%" is gone.** CDFA's 100% is California's share of U.S. garlic cash receipts (USDA ERS data, as tabled by CDFA). If you prefer the softer wording, "most of the nation's garlic" with the same source also works.
- **Fresno top-ten year:** see above. The text says 2023 now; a 2025 update needs the county PDF opened by hand.
