# fix_t2_ch4-6 notes (Chapters 4–6)

Script: `SCRATCH/fix_t2_ch4-6.py`. Running it tests all edits in memory against the current live mirror and writes `SCRATCH/fix_t2_ch4-6.json`. 14 edits, all OK (each `old` matches exactly once, in sequence). No repo file was written. Every source was re-checked while writing it in.

| # | P | Page | What changed | Source (verified) |
|---|---|---|---|---|
| 1 | P1 | 597103 (5.2 Valley Connection) | Smoke sentence: "acrolein and formaldehyde, along with benzene" → "acrolein, formaldehyde, benzene and hydrogen cyanide"; footnote 5 → 6 | O'Dell et al., ES&T 54(19), 2020, doi 10.1021/acs.est.0c04497 (abstract via PubMed 32857515 / search; ACS page returns 403): "acrolein, formaldehyde, benzene, and hydrogen cyanide are the dominant contributors…" |
| 2 | P1+P2 | 597103 Sources list | Old fn 5 (Navarro 2021, which doesn't support the claim) replaced by new 5 = National Cancer Institute, *Formaldehyde and Cancer Risk*, and new 6 = O'Dell et al. 2020. Footnotes stay in reading order. | NCI fact sheet (fetched): IARC "classifies formaldehyde as a human carcinogen"; NTP 2011 "known human carcinogen" |
| 3 | P1 | 597093 (4.4 To Your Health) | "10 mL… about 30 mL (1 oz) can be fatal" → "4 to 10 mL… lethal dose is estimated at 300 to 1,000 mg per kg of body weight (very roughly 30 to 90 mL for an adult)"; the existing UKHSA link is kept | UKHSA Methanol: toxicological overview (updated 11 Oct 2024, fetched) |
| 4 | P1 | 597094 (4.5 Clinical Connection: Nursing) | Cross-reference "as little as 10 mL" → "as little as 4 to 10 mL", to match edit 3 | Same UKHSA source |
| 5 | P2 | 597103 (5.2 VC) | `<sup>5</sup>` added after the IARC/NTP formaldehyde carcinogen sentence | NCI, as in edit 2 |
| 6 | P2 | 597103 (To Your Health: Acetone, Ball text) | Inline "(Source: ATSDR, Toxicological Profile for Acetone, 2022)" after "less than 1 mg/100 mL of blood" | ATSDR tp21.pdf (June 2022, read directly): healthy whole blood 0.84–1.90 mg/L (0.08–0.19 mg/100 mL); ketoacidotic plasma 290–424 mg/L |
| 7 | P2 | 597103 attribution line | "The text is reproduced unchanged;" → "…reproduced unchanged except for one added source citation;" | Keeps the adaptation statement accurate after edit 6 |
| 8 | P2 | 597093 (4.4 Lecture Connection example) | Inline CDC citation after "at least 60% alcohol when soap and water are not available" | CDC, Hand Sanitizer Guidelines and Recommendations (fetched): "use a hand sanitizer with at least 60% alcohol" |
| 9 | P2 | 597043 (Rosa's Story Part 5) | Inline source after "about 194 mg/dL" | Nathan et al. (ADAG), Diabetes Care 2008, PMC2742903 (fetched): "AG mg/dl = 28.7 × A1C − 46.7" → 194.4. Cited instead of the ADA chart because the chart has no 8.4% row (8% → 183, 8.5% → 197). |
| 10 | P2 | 597044 (Rosa's Story Part 6) | Inline Dawes 2003 citation after "about 5.5, the point at which enamel starts to dissolve" | C. Dawes, JCDA 69(11):722–4, 2003 (PDF read): critical pH "may be 5.5" with high salivary Ca/P; about 6.5 with low; plaque fluid as low as 5.1 |
| 11 | P2 | 597112 (6.4 Dental Hygiene box) | Inline Dawes 2003 citation after "Below a mouth pH of about 5.5 it starts to dissolve" | Same. This box has only a "Further reading" line, no Sources list, so the inline style is used. |
| 12 | P3 (free link) | 597094 VC fn 3 | ncbi.nlm.nih.gov/pmc/… → pmc.ncbi.nlm.nih.gov/articles/PMC6527027/ (301 redirect) | Zakhari 2006 (fetched) |
| 13 | P3 (free link) | 597094 VC fn 5 | Dead web-archive PDF → pmc.ncbi.nlm.nih.gov/articles/PMC3860438/ (same Ehlers 2007 article) | PMC3860438 (fetched): "approximately 40 percent of people of Far East Asian descent" |
| 14 | P3 (free link) | 597113 VC fn 5 | DOAJ record (403) → https://doi.org/10.3390/horticulturae9030382 | Wang et al., Horticulturae 9(3):382, 2023 |

## Skipped or not edited, and why
- **Critical pH "about 5.5" on recap and practice pages:** 597119 (Clinical Update recap, Case Question 6.3 and its answer key, Chapter Guide dental line), 597120 (problem and answers), 597101 (Problem 4.56-type answer, xylitol). The number is not wrong, and each point is cited where it is taught (597112) and where the Ch 6 story starts (597044). Per "one citation per claim", I did not add more.
- **Methanol 10 mL / 30 mL:** grepped the whole page set. It appears only in 597093 and 597094 (both fixed). No other chapter repeats it.
- **A1c 194 mg/dL:** appears only on 597043.
- **All P3 items from the audit except the three free link fixes:**
  - GV Wire → Fresno County Crop Report (597098 fn 3, 597113 fn 4; the 2025 report is now out with garlic 10th and peaches 8th).
  - Garlic 86% (2007) is dated.
  - CDFA $309 M / 99% still needs a manual check.
  - AirNow guide wording still needs a manual check.
  - NIAAA "sleep medicines … overdose" wording (597094 fn 6).
  - Ethyl butyrate melting point −101 → −97 °C (597114).
  - Ethylene glycol −49 °C.
  - Footnote order 1, 3, 2 on 597098.
  - ChemistryViews links.
  - Optional sources (Lister, triclosan, naproxen, lactate).

## For the author to decide
- **Edit 7 (attribution line on 597103):** adding a citation inside the Ball text makes "reproduced unchanged" inaccurate, so the line now says "except for one added source citation". If you prefer, drop edits 6 and 7 together and leave the acetone sentence unsourced. The number itself is correct.
- **Edit 3:** a range (30–90 mL) replaces the single "30 mL (1 oz)" figure, because UKHSA gives only a mg/kg range. If you would rather not convert, cut the parenthetical "(very roughly 30 to 90 mL for an adult)".
