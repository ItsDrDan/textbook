# fixp3_t2_ch4-6 notes (ROUND 2, P3 polish, Chapters 4–6)

Script: `SCRATCH/fixp3_t2_ch4-6.py`. It tests all edits in memory against the current live mirror and writes `SCRATCH/fixp3_t2_ch4-6.json`.
- 8 edits, all OK: each `old` string matches exactly once, applied in sequence.
- No repo file was written.
- Round 1 (fix_t2_ch4-6.py) is already live as drafted. I checked 597103 (NCI fn 5, O'Dell fn 6, HCN), 597093 and 597094 ("4 to 10 mL"). Its stub now reports FAIL because those `old` strings are gone, which is expected.
- Every source below was re-checked while writing it in.

| # | Page | What changed | Source (verified) |
|---|---|---|---|
| 1 | 597094 (4.5 VC, In the clinic) | "with anxiety or sleep medicines it raises overdose risk" → "with anxiety medicines it raises overdose risk, with sleep medicines it can slow breathing" | NIAAA, Harmful Interactions (rev. 2014; existing fn 6). Anxiety row: "increased risk for overdose". Sleep row: "slowed or difficult breathing". |
| 2–3 | 597098 (4.9 VC) | Footnote markers 3, 2 → 2, 3, and Sources entries 2 and 3 swapped, so the list is in reading order. No source changed. | Re-verified the CDFA claims in other ways: NASS Vegetables 2022 Summary gives California garlic value of $309 million in 2022; CDFA 2022–2023 Agricultural Exports (table p. 7) gives California's share of U.S. garlic exports as 100.0% in 2021 and 2022. |
| 4 | 597096 (4.7 Lecture Connection) | Inline source after "Lister's surgical antiseptic in the 1860s". Cited in the author's own sentence because the Ball text above it is "reproduced unchanged". | Pitt and Aubin, Can J Surg 2012, PMC3468637: "carbolic acid compounds as an antiseptic"; Lancet papers "the first in March 1867". |
| 5 | 597097 (4.8 figure caption) | Inline source after "introduced diethyl ether into surgical practice in 1846" | Makris et al., Annals of Surgery Open 2022, PMC10431324: Oct 16, 1846 "Ether Day", Morton's "successful public demonstration of surgical anesthesia" at MGH |
| 6 | 597105 (5.4, lactate and fatigue) | Inline source after "no longer thought to be the main cause of that fatigue" | Allen, Lamb and Westerblad, Physiol Rev 88:287–332, 2008, doi 10.1152/physrev.00015.2007. Abstract (PubMed 18195089 via QxMD): lactate/H⁺ explanation "probably of limited importance in mammals". |
| 7 | 597106 (5.5 Lecture Connection) | Inline source after the naproxen single-enantiomer sentence | Papp et al., Molecules 27(9):2986, 2022, PMC9101765: "used as a single enantiomer, in the form of S-naproxen"; "R-naproxen is hepatotoxic". |
| 8 | 597114 (6.6 Table 1) | Ethyl butyrate melting point &minus;101 → &minus;97 °C, with an inline source in the cell | PubChem CID 7762: −97 °C (CRC Handbook, 95th ed.); other listings −93 °C. No source gives −101. This is the only occurrence in the whole page set. |

## Audit P3 items resolved with no edit
- **597103 fn 2 (AirNow 2019 guide):** now VERIFIED. pymupdf extracts the text: "Disposable N95 or P100 respirators remove only particles, not gases or vapors"; organic vapor cartridge "can reduce exposure to irritating gases in smoke, such as aldehydes"; "acetaldehyde, acrolein, formaldehyde and benzene" named among HAPs; sensitive groups listed.
- **597103 fn 1 (Creek Fire release):** fully verified. "causing smoke impacts to all counties of the Valley air basin… warns residents to stay indoors".
- **597098 fn 3, now fn 2 (CDFA review):** both numbers confirmed through NASS and the CDFA exports report (see #2–3). The review itself (>10 MB) still can't be fetched. The citation stays.
- **597098 garlic "86%, by a 2007 UC Davis estimate":** kept. The sentence already dates the figure, and no current national share exists (NASS estimates garlic for California only).
- **597113 fn 5 DOI, 597094 fn 3/fn 5 URLs:** done in round 1 and live.

## Skipped (author or manual check needed)
- **GV Wire → Fresno County Crop & Livestock Report** (597098 fn 2 after renumbering; 597113 fn 4). The county PDFs (2024: 19 MB, 2025: 25 MB) are too large to fetch, and no county summary page lists the top ten. I would not cite a document I couldn't read.
  - The 2025 report is out ($9.64 B). KMPH news (Nov 3, 2026) puts peaches 8th and garlic 10th in 2025.
  - Someone needs to open the PDF, confirm the top-ten page, and then swap the citation. The author could also update "in 2024" to "in 2025".
- **ChemistryViews "The Chemistry of Dental Care" Part 1 and Part 2** (597096, 597112, further reading). Cloudflare returns 403 to every automated fetch, including curl. Part 2 is indexed at chemistryviews.org/?p=39767; no Part 1 page was found. Needs a browser check, then either a URL update or removal of the Part 1 link.
- **597095: "60% ethylene glycol… freezes at −49 °C (−56 °F)".** Tables give about −48 °C (−55 °F) for 60 wt%; vendor charts differ, and weight % vs volume % matters. Within rounding, so left unchanged. The author can choose "about −48 °C (−55 °F)", which needs a source he accepts, such as an MEGlobal/Dow freeze-point chart (industry).
- **597096: triclosan "has since been removed from most U.S. toothpastes".** Accurate (Colgate Total, the only U.S. toothpaste with it, dropped it in January 2019), but the only sources are news reports, and FDA has no current page saying so. Left uncited.
- **597094 fn 5: "East Asian" vs the source's "Far East Asian".** Wording choice for the author; not changed.

## Optional "says who?" citations skipped (low value)
- 597042 Rosa's mouthwash "about 20% ethanol" (fictional product).
- 597109 formic acid "first obtained by the distillation of ants" (Ball text, standard etymology).
- 597109 vinegar "4%–10% acetic acid".
- 597093 "1 pt of pure ethanol would kill most people" (Ball text; no clean source; the author may want to soften it).
- 597106 menthol enantiomer "musty, barely cools".
- 597112 37% phosphoric acid etch; 597103 propanal and diethyl ether solubility values (they match the ICSC/NIOSH values).

## Licensing
No licensing-only issues in this group. The 597097 Morton painting (Ernest Board, died 1934) is correctly credited as public domain via Wikimedia Commons (PD-old).
