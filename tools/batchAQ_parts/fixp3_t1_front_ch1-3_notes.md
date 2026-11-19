# Round 2 (P3) fix notes: t1_front_ch1-3

Script: `fixp3_t1_front_ch1-3.py` (caller's `e()`). It has 10 edits on 7 pages. All 10 were stub-tested against the current `pages/live` (after batch AP), and each `old` occurs exactly once. Sources were re-fetched on 2026-11-18.

| # | Page | What changed | Source (verified) |
|---|---|---|---|
| 1 | 597061 (1.8 Valley Connection) | "near Earlimart" → "in Tulare County", to match the cited note 6 | ABC30, already note 6: crash in Tulare County "near Avenue 24"; it never names Earlimart |
| 2 | 597061 (1.8 Molecule in the Clinic) | "the most widely used medicine" → "one of the most widely used medicines". No citation added. | StatPearls wording "one of the most widely used". NCBI blocked fetch, so I softened the claim instead of citing it. |
| 3 | 597061 (1.8 Nursing) | 70% swab: added the main reason (water speeds protein denaturation), cited | CDC, Chemical Disinfectants: optimum "60%–90% solutions in water"; "proteins are denatured more quickly in the presence of water" |
| 4 | 597057 (1.4 Pauling) | 1954 prize "for his work on protein structure" → official scope (chemical bond and structures of complex substances such as proteins), cited | Royal Swedish Academy of Sciences (kva.se): "for his research into the nature of the chemical bond and its application to the elucidation of the structure of complex substances" |
| 5 | 597059 (1.6 To Your Health) | The two superseded MyPlate sentences were replaced with the 2025–2030 Guidelines' own advice, cited. That advice: saturated fat ≤10% of calories, no added sugars, sodium <2,300 mg for ages 14+, favor oils such as olive oil. | DGA 2025–2030 PDF, realfood.gov/documents/DGA.pdf (text extracted and checked) |
| 6 | 597065 (2.1) | "tens of millions of compounds" → "more than 300 million substances registered by Chemical Abstracts Service", cited | cas.org/content: "chemical substances (300M+)" |
| 7 | 597071 (2.7) | CO poisoning "kills people" → "kills hundreds of people … every year, most often in winter", cited | CDC MMWR 66(8), 2017: 2,244 deaths 2010–2015, 393 in 2015, winter peak |
| 8 | 597072 (2.8 figure caption) | Ozone hole "fill in about mid-November" → "usually close in December", cited | Copernicus Atmosphere Monitoring Service 2025: closed Dec 1, "one of the earliest closures in the past four decades"; 2020 closed Dec 28 |
| 9 | 597072 (2.8 To Your Health) | "Bromine-containing compounds are widely used in fire extinguishers…" → halons once widely used, U.S. production ended 1994, only recycled halon today, cited. I dropped the unsourced "on clothing" detail; the sentence now says bromine compounds "are also used as flame retardants". | EPA Halons Program: "On January 1, 1994, production and import of virgin halons were phased out" |
| 10 | 597072 (2.8 Nursing) | Halothane 1956 / hepatitis cited | OpenAnesthesia (IARS), Halothane: "entered clinical practice in 1956"; "Halothane hepatitis is a major limiting adverse effect" |

## Same-wording check across all pages
None of the changed phrases appears on any other page: "mid-November", "tens of millions of compounds", "most widely used medicine", "for his work on protein structure", "70% rather than 100%" and "Earlimart" are each on one page only. No Practice Problems page or other chapter needs an edit.

## Skipped (nice-to-have; no "says who?" need, or the source is already adequate)
- **597061 note 3 (Albany ATM 100 notes):** it supports both statements. A swap to an NWS page is optional.
- **597061 heat-rule note:** Cornell LII copy of 8 CCR §3395 is accurate. The official dir.ca.gov copy is optional.
- **597082 note 1 (NOAA Monterey Bay):** it supports every statement; it is just not Valley-specific.
- **597081 note 1 (Saltveit):** the link works through the Wayback viewer. The direct `…id_/` PDF URL is optional.
- **597075 Cumulative Problem 2.4 answer (×2), "binds hemoglobin about 200 times more tightly":** the number is consistent with ATSDR ("over 200 times") and UKHSA ("245-fold"). A citation in a practice answer is not needed.
- **597072 chloroform "introduced in 1847":** the date is correct (Simpson, Nov 1847). The Wood Library-Museum page refused the fetch, so I added no citation. The halothane citation covers the sentence's main point.
- **Licensing:** the OpenStax Chemistry 2e figure credit on 597061 says CC BY-NC-SA 4.0. The OpenStax page itself now states CC BY-NC-SA 4.0, so the credit is correct and needs no change.

## For the author to decide (numbers only he can choose)
- **597070 (2.6 Looking Closer: Gas Densities):** methane 0.67 g/L, air 1.29 g/L, propane 1.88 g/L and butanes about 2.5 g/L are taken at different temperatures (air 1.29 is at 0 °C; methane 0.67 is near 20 °C). The comparison still holds. If he wants one condition, the 0 °C, 1 atm values are about 0.72, 1.29, 2.0 and 2.6 g/L. Check them against his Table 2.6.1 before changing anything.
- **597055 (1.2):** "sodium chloride … boils at 1413 °C". Sources differ: PubChem lists 1413 °C and the CRC Handbook gives 1465 °C. Either is defensible; I left it as is.
- **Round-1 note:** the coordinator's live LDL cell ("Under 100 mg/dL; under 70 for adults 40–75 with diabetes and other heart risk factors") matches the source line added in round 1 (ADA Sec. 10 and MedlinePlus). Nothing more is needed there.
