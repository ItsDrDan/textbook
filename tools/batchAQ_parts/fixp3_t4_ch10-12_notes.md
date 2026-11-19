# fixp3_t4_ch10-12 notes (round 2, P3 polish, 2026-11-18)

Script: `SCRATCH/fixp3_t4_ch10-12.py`. It was written against `pages/live` after batch AP went live, so the round-1 fixes are already in the pages.

At module level the script only defines helpers (and only if the builder has not already supplied `e()`), then calls `e()`. Asserts and file output run only under `__main__`. It passed two tests: exec'd with a stub `e()`, and run directly with `--dry`. Result: 24 edits on 10 pages. Every source was re-checked for the exact sentence it supports.

| # | Page | What changed | Source (re-verified) |
|---|---|---|---|
| 1 | 597162 10.9 nitrate box | Source 2 replaced in place: the *Scientific American* story becomes the UC Davis report itself. | Harter, Lund et al., *Addressing Nitrate in California's Drinking Water*, 2012 (California Assembly copy). The text reads "roughly 254,000 people" in the Tulare Lake Basin and Salinas Valley. |
| 2 | 597163 10.10 Valley Connection | The 10-minute rest is now tied to "At 95 °F or above". "New workers in high heat" becomes "Workers newly assigned to a high-heat area". | 8 CCR §3395(e)(6) and (g)(2), already cited as source 3. |
| 3–5 | 597169 11.4 chlorpyrifos box | Feedstuffs removed. CalEPA moves from 5 to 1 (trailing slash added). The ban sentence's ^5 becomes ^1. Sources 2–4 keep their numbers. | The CalEPA release lists the six crops and both dates. |
| 6 | 597169 To Your Health: Penicillin | Fleming 1928 and 1940s mass production now cited. | Gaynes, *Emerging Infectious Diseases* 2017 (PMC5403050): "In 1928, a chance event in Alexander Fleming's London laboratory…" |
| 7 | 597169 Molecule in the Clinic | "the most common antibiotic for dental infections" becomes "a first-choice antibiotic for a dental infection that needs one", cited. | ADA chairside guide (CDC-hosted PDF), which recommends amoxicillin 500 mg 3×/day or penicillin VK. |
| 8 | 597169 Lecture Connection | Imported candies, spices, pottery, greta and azarcón now cited. | CDPH *Lead Poisoning Overview* (candy, spices, leaded-glaze pottery, imported remedies) and CDPH *Lead in Traditional Remedies* brochure (greta, azarcón). |
| 9–12 | 597170 11.5 almond box | "about 80%" becomes "nearly 80%". The UC Davis "breeding projects" page is dropped. The Almanac becomes source 1 for both the world share and the counties; almonds.org becomes 2; NIH ODS/UKY becomes 3. The in-text ^4 on the blood-thinner sentence becomes ^3. | 2022 Almond Almanac: "CALIFORNIA GROWS NEARLY 80% OF THE WORLD'S ALMONDS"; production by county on p. 35. |
| 13 | 597182 12.9 Valley fever | ^5 becomes ^2,5 on "roughly 5 to 10% … chronic". | CDC clinical overview: about 5 to 10% develop chronic pulmonary disease. |
| 14 | 597182 source 4 | genome.gov PCR glossary slug updated (the old one was a redirect). | — |
| 15 | 597182 Human genome | HGP dates cited. | NHGRI timeline: "On Oct. 1, 1990, the project officially begins"; completion April 14, 2003. NHGRI Completion FAQ: T2T filled the remaining gaps on March 31, 2022. |
| 16 | 597182 CRISPR | Casgevy 2023 cited. | FDA press release, Dec 8, 2023. |
| 17 | 597181 12.8 | AZT 1987 cited. | FDA history exhibit: "In March of 1987, FDA approved zidovudine (AZT)…" |
| 18 | 597181 | U=U cited. | CDC *HIV Treatment as Prevention*: "will not transmit HIV to their sex partners". |
| 19 | 597181 Dental Hygiene | "survives for days on surfaces" becomes "stays infectious on surfaces for at least 7 days", cited. | CDC *Clinical Overview of Hepatitis B*. |
| 20 | 597183 12.5 Example 3 | "has not changed since the 1980s" becomes "has been made from the same viral surface protein since the 1980s", cited. | CDC Pink Book, Hepatitis B: recombinant HBsAg vaccine first licensed in 1986; Heplisav-B (2017) is "a third recombinant vaccine". |
| 21 | 597172 11.7 | Lactase decline: added "about two-thirds of all people", cited. | MedlinePlus Genetics: "Approximately 65 percent of the human population…" |
| 22 | 597167 11.2 | Fischer 1894 and Koshland 1958 cited once. The audit listed this sentence under 597166, but it is on 597167. | Koshland, *Angew Chem Int Ed Engl* 1995;33:2375 (doi:10.1002/anie.199423751). The abstract was read through search because Wiley blocks the fetcher. |
| 23–24 | 597178 12.4 | Two genome.gov figure-credit links (title and href) updated to their new slugs (Ribonucleic-Acid-RNA, Transfer-RNA-tRNA). | — |

## Not needed
- **A28 (597170, "in data from 2011–2020"):** the audit was wrong. The CDC page does say "Data from 2011–2020 have shown…". No change.

## Skipped: optional citations left out ("says who?" test)
- **A1 CDFA 2022 milk figures (597156):** accurate as dated. A 2023–2024 review exists (milk $8.1 B in 2023); updating would be the author's choice.
- **A2–A5 ChemistryViews "Further reading" (597158, 597166):** the series exists; the site blocks automated fetches. Further reading, not citations.
- **A18 StatPearls organophosphate (597169 ^2):** NCBI serves a CAPTCHA, so I could not re-read the pralidoxime "aging" sentence. The source is kept.
- **A19 San Diego County summary of 3 CCR §6728 (597169 ^3):** accurate. Upgrading to the regulation text is optional.
- **A25 almonds.org for 7.3 mg vitamin E (597170, now ^2):** industry source kept. The NIH ODS fact sheets refuse automated fetches, so a replacement could not be verified.
- **Already done in round 1:** A6 (pdb.org), A22 (Jakubowski link), A24/A27 (moved PDFs).
- **Other genome.gov glossary links on 597178/597182** (Codon, Genetic-Code, Transcription, DNA-Fingerprinting, Recombinant-DNA): already resolve with no slug change.
- **Licensing:** none of this group's pages credits Wikipedia, so there was nothing to fix.

## Needs the author (not guessed)
1. **597154, "asparagine in 1806. It was obtained from protein found in asparagus juice":**
   - The date is right (Vauquelin and Robiquet, 1806), but I found no source to cite except Wikipedia and blogs.
   - "From protein found in" is probably wrong: it was crystallized from evaporated asparagus juice, not from a protein.
   - Suggested: "…obtained from asparagus juice (hence the name)." Citing the original paper (Ann. Chim. 57:88, 1806) would need a check.
2. **597159, "Bovine (cow) insulin … It is no longer sold in the United States":**
   - The claim is correct; beef insulin for humans was discontinued in the U.S. in 1998.
   - FDA's Q&A page on importing beef/pork insulin now returns 404, so there is no live official source. Leave it uncited or remove the sentence.
3. **597159, "Swallowed insulin is just protein … so it must be injected":** inhaled insulin (Afrezza) exists. A possible fix is "must be injected (one form is inhaled)". I found no verified FDA source in this pass.
4. **597163 table, "Cooking does not lower the nutritional value of a protein":** this overstates the case slightly, since browning reactions can reduce available lysine. Soften or keep.
5. **597165 and 597162 Think-about-it answer:** CO "about 200 times" was left as is. Section 10.9 now says "more than 200 times" (ATSDR). Align these if you want.
