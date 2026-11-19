# Source and science-verification audit — CHEM 3B textbook and lab manual (2026-11-18)

Seven independent checkers read every textbook page (199) and every lab-manual source file (15 experiments,
2 workshops, appendices, front matter, and the 3 draft labs). For each cited source they opened it, confirmed the
publisher is legitimate and that it states the exact claim; for unsourced real-world claims (statistics, clinical
values, history, regional facts, hazards, data tables) they found and verified a source. **Nothing has been edited.**
Detail (with quotes, URLs, proposed wording) is in the seven `srcaudit_*.md` files in this folder.

## Totals

| Group | Sources checked | OK | Problem | Unverified (site blocked) | Need a new source | Errors / outdated |
|---|---|---|---|---|---|---|
| Front matter + Ch 1–3 | 26 | 22 | 4 | 0 | 14 | 9 |
| Ch 4–6 | 23 | 14 | 5 | 4 | 10 | 6 |
| Ch 7–9 | 35 | 27 | 5 | 3 | 17 | 9 |
| Ch 10–12 | 44 | 28 | 7 | 9 (exist; confirmed by search) | 22 | 7 |
| Ch 13–15 | 30 | 21 | 5 | 4 | 19 | 7 |
| Manual Exp 1–8, workshops, drafts | 0 cited (45 chemicals' hazards checked) | — | — | 3 | 17 | 12 |
| Manual Exp 9–15, appendices | 4 + 4 data tables | 8 | 0 | 1 | 9 | 6 + 4 hazard |
| **Total** | **166** | **120** | **26** | **24** | **108** | **56** (+4 hazards) |

Good news: no invented sources anywhere; every Valley Connection statistic checked (crop values, census, air
district, CDC county diabetes, heat rule, Valley fever, fentanyl deaths, Narcan date) matches its source; the
manual's data tables (electronegativities, atomic weights, fatty-acid data, physical constants) are correct;
Rosa's Story clinical numbers are plausible and current; the Glossary had no wrong definitions.

## P1 — fix first (wrong number/claim, or a citation that does not support its sentence)

| # | Where | Problem | Fix (source) |
|---|---|---|---|
| 1 | 1.8 (597061) gecko box | "In 2000, Kellar Autumn…" — the SiO2/GaAs result is 2002 | Autumn et al., PNAS 2002, 99:12252 |
| 2 | 2.8 (597072) ozone figure credit | NASA link 404 | ozonewatch.gsfc.nasa.gov/Scripts/big_image.php?date=2006-09-24&hem=S |
| 3 | 4.4 (597093) methanol | "about 30 mL (1 oz) can be fatal" is not in the cited UKHSA page (it gives 4–10 mL can cause permanent damage; lethal 300–1,000 mg/kg) | reword to the source |
| 4 | 5.2 (597103) wildfire smoke, fn 5 | Navarro 2021 does not rank the main gas-phase risks | O'Dell et al., ES&T 2020, doi 10.1021/acs.est.0c04497 (adds HCN) |
| 5 | 8.3 (597136) | normal urine glucose "trace to 20 mg/dL" | 0–15 mg/dL (MedlinePlus) |
| 6 | 8.6 (597139) | galactosemia "1 in 65,000" | 1 in 30,000–60,000 (MedlinePlus Genetics) |
| 7 | 9.1 (597144) | essential fatty acids "4–6 g/day" | AI 12–17 g linoleic + 1.1–1.6 g α-linolenic (IOM DRI; NIH ODS) |
| 8 | 9.2 (597145) fn 5 | Loften et al. link 404 | doi 10.3168/jds.2014-7919 |
| 9 | 13.4 (597192) | "about 38 million Americans with diabetes" (outdated, uncited) | current CDC National Diabetes Statistics Report figure, with link |
| 10 | 13.4 (597192) | heart attack/stroke risk "two to four times" (uncited) | "about twice" (CDC) |
| 11 | Manual Exp 10 intro | "active compound in willow bark is salicylic acid" | salicin (converted to salicylic acid in the body); Desborough & Keeling, Br J Haematol 2017 |
| 12 | Manual Exp 14 intro A | water-soluble vitamins "not stored" | add: except B12, stored in the liver for years (NIH ODS / MedlinePlus) |
| 13 | Draft Digestion hazards | phenolphthalein "suspected carcinogen" | GHS H350 "may cause cancer" + H341 (ECHA/PubChem); FDA removed it from OTC laxatives 1999 |

Note on the pear/banana decision: one checker preferred "banana" because PubChem describes pentyl acetate as
banana-like. n-Amyl (pentyl) acetate is sold as both "banana oil" and "pear oil", so the author's "pear" can stay;
a source line can say so.

## P2 highlights (missing source on a statistic/clinical claim, or a weak/outdated source)
- **Clinical reference values without a source** (cite MedlinePlus / ADA Standards of Care 2026 / NKF / NAS DRI):
  glucose and A1c cutoffs (8.x pages), albumin 3.5–5.0 → 3.4–5.4 g/dL (10.6, 10.12), UACR < 30 mg/g, protein
  0.8 g/kg, lipid targets (9.6), Rosa's chart ranges incl. LDL target (likely < 70 now, ADA 2026), A1c 8.4% ≈ 194 mg/dL.
- **Numbers to correct:** PKU 1 in 12,000 → about 1 in 10,000–25,000 (US ~1 in 25,000); aspartame 180× → ~200× (FDA);
  "about 65% of the diet is carbohydrate" → ~47% of calories (USDA WWEIA); IRDS risk by gestational age; Exp 14 vitamin C
  RDA 75 mg is women only (men 90 mg); urinalysis draft fasting glucose 70–99 mg/dL; Exp 10 USP limit (3.0% for
  coated/buffered tablets, students test a buffered one).
- **Weak sources to upgrade:** GV Wire news articles (use county crop reports), Truthout/California Watch nitrate
  "one in three wells" (use Lockhart et al. 2013, already cited), "CDC" PDF that is really an AAP chapter, outdated
  2003 DKA guideline (2024 consensus), SB 183 floor analysis (cite the statute), "NIH long-term study" five-times
  statistic in 9.6 that could not be found (rewrite or delete).
- **Unsourced claims to cite:** formaldehyde carcinogen (NCI), CDC 60% sanitizer, enamel critical pH 5.5 (Dawes 2003),
  nicotine lethal dose (Mayer 2014), trans-fat phase-out (FDA 2015), gum-disease treatment and glucose (Cochrane 2022),
  benzene and leukemia (ATSDR), benzo[a]pyrene (IARC/EPA), HPV ~70% of oropharyngeal cancers (CDC), penicillin
  allergy (CDC), CO affinity (StatPearls), aspartame IARC 2023 note.
- **Lab manual hazards understated vs GHS:** 10% NaOH and 10% HNO3 are corrosive; benzoic/salicylic acid serious eye
  damage; methyl salicylate "harmful" not "toxic"; bromine fatal if inhaled; acetic anhydride, AgNO3, FeCl3;
  methylene chloride: add instructor note on the 2024 EPA TSCA rule (lab use only under a Workplace Chemical Protection Program).
- **Manual internal inconsistency:** Exp 5 Tollens' leftover reagent → aqueous (instructor notes) vs non-halogenated
  organic (Waste Instructions).

## P3 (polish)
Moved links (PMC, pdb→rcsb, Jakubowski, UKY vitamin E, IntechOpen, DOAJ→DOI), ethyl butyrate mp −97 °C, TAG "98%"
of dietary lipid → 90–95%, BMI "over 30" → "30 or more", DKA pH "as low as 6.9", hep B vaccine wording, halon use,
CAS > 200 million compounds, Pauling Nobel citation, Wikipedia credited as "public domain" on 13.5/14.3 (text is
CC BY-SA), Valley box on 7.11 with sources but no footnote numbers, optional citations for history items.

## Recommended for the manual
One "Sources for Data" section in the front matter (hazards = GHS via PubChem/supplier SDS; physical constants =
CRC/PubChem/NIST; atomic weights = CIAAW; clinical ranges = MedlinePlus), plus a one-line Sources list in the
three draft labs. Drafted text is in section 6 of the two `srcaudit_m*.md` files.

## Suggested next steps
1. Textbook batch AP: all P1 + P2 items on LibreTexts (each with its verified source in the page's footnote style).
2. Lab manual: P1/P2 text and hazard fixes + Sources for Data section, rebuild, then his Word export.
3. P3 polish as a later batch. Items marked UNVERIFIED (site blocked automated fetches) get a manual check in the browser while fixing.
