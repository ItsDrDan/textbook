# fix_t4_ch10-12 notes (2026-11-18)

Script: `SCRATCH/fix_t4_ch10-12.py`. It reads the live pages only. Run it with `--dry` to test the asserts; a normal run writes `SCRATCH/fix_t4_ch10-12.json` and `SCRATCH/fix_t4_preview/<id>.html`. It was test-run against the current live HTML: 21 edits on 12 pages, all asserts pass. There are no P1 items in this group, so these are all the P2 items from `srcaudit_t4_ch10-12.md`, plus four moved-link swaps (P3, URL only). Each source was re-checked for the exact sentence while writing it in.

| # | Pri | Page | What changed | Source (re-verified) |
|---|---|---|---|---|
| 1 | P2 | 597048 Ch 10 opener, Rosa Part 10 | Added a citation for "uACR 45 mg/g, where under 30 is normal; repeated to confirm". | National Kidney Foundation, *Urine albumin-creatinine ratio (uACR)*: under 30 mg/g is "normal" or "at goal"; the test "often needs to be repeated". |
| 2 | P2 | 597154 10.1 Lecture Connection | Protein 0.8 g/kg/day: the sentence was reshaped slightly so the citation fits. | Wolfe et al., Adv Nutr 2017 (PMC5347101): "the EAR and the RDA for protein are 0.66 and 0.80 g/kg/d". The National Academies DRI chapter was unreadable by the fetcher. |
| 3 | P2 | 597159 10.6 | Aspartame "about 180 times" changed to "about 200 times sweeter than sucrose", cited. | MedlinePlus, *Sweeteners – sugar substitutes*: "200 times sweeter than sucrose". FDA's aspartame page now returns Page Not Found, so it is not cited. |
| 4 | P2 | 597159 10.6 Clinical Connection: Nursing | Albumin normal range 3.5–5.0 changed to 3.4–5.4 g/dL, cited. | MedlinePlus, *Albumin blood test*: "3.4 to 5.4 g/dL". |
| 5 | P2 | 597165 Problem 10.63 | Same albumin range, 3.4–5.4 g/dL. Not re-cited. The answer is unchanged, since 2.1 is still low. | (as #4) |
| 6 | P2 | 597160 10.7 Triple helix | "most abundant protein of vertebrates making up 30% to 35%" changed to "most abundant protein in mammals, making up about 30% of their protein by mass", cited. | Ricard-Blum 2011, Cold Spring Harb Perspect Biol (PMC3003457): "the most abundant proteins in mammals (∼30% of total protein mass)". |
| 7 | P2 | 597162 10.9 Lecture Connection | CO binds Fe²⁺ "about 200 times" changed to "more than 200 times more tightly", cited. The Think-about-it answer and the 10.12 answer still say "about 200 times"; that is not wrong, so they were left alone. | ATSDR, *Toxicological Profile for Carbon Monoxide*, ch. 2: "over 200 times greater". StatPearls was blocked by a CAPTCHA, and its articles disagree (200, 220, 200–250). |
| 8 | P2 | 597162 Valley Connection: Nitrate | "about one in three domestic wells…" changed to "When UC Davis tested 200 domestic wells in Stanislaus, Merced, Tulare and Kings counties, 42–46% had nitrate above the drinking-water limit,^1". | Lockhart, King and Harter, UC Davis Task Report 3, 2013: 46% (Tulare/Kings) and 42% (Stanislaus/Merced) exceeded the MCL; 200 wells sampled. |
| 9 | P2 | 597162 same | Fertilizer/manure sentence ^3 changed to ^1 (the same UC Davis report, now in slot 1). | (as #8) |
| 10 | P2 | 597162 same | Methemoglobin "cannot carry oxygen" ^4 changed to ^3 (ATSDR). | ATSDR CSEM *Nitrate/Nitrite Toxicity, Who Is at Most Risk*: nitrites oxidize Hb to MetHb, which cannot carry oxygen effectively. |
| 11 | P2 | 597162 same | ^4,5 changed to ^3,4; added ^4 to "The federal limit of 10 mg/L … set to protect infants"; boiling ^6 changed to ^5. | ATSDR CSEM: HbF "more readily oxidized"; the reductase "has only about half the activity it has in adults". UW PEHSU: "The 10 mg/L standard was set to protect infants". Iowa HHS: boiling concentrates nitrate. |
| 12 | P2 | 597162 same, Sources list | Removed the Truthout 2010 reprint. The UC Davis report moves to 1. The "CDC" stacks PDF (actually AAP *Pediatric Environmental Health* ch. 33, ©2012 AAP) is replaced by the ATSDR CSEM page (archive.cdc.gov). | Renumbering was unavoidable to keep one entry per source; the list is now 1 to 5. |
| 13 | P2 | 597162 same | Iowa HHS renumbered from 6 to 5. | — |
| 14 | P2 | 597169 11.4 To Your Health: Penicillin | "most people whose charts say penicillin allergy turn out not to be allergic" changed to "about 10% of U.S. patients report a penicillin allergy, and fewer than 1% of them are truly allergic when evaluated", cited. | CDC, *Clinical Features of Penicillin Allergy*. |
| 15 | P2 | 597180 12.7 | "PKU affects about 1 in 12,000 newborns in North America" changed to "In the United States, PKU affects about 1 in 25,000 newborns", cited. | MedlinePlus Genetics, *Phenylketonuria*: "In the United States, PKU occurs in 1 in 25,000 newborns." |
| 16 | P2 | 597181 12.8 Clinical Connection: Dental Hygiene | HPV-16 "now causes most oropharyngeal cancers" changed to "HPV is now linked to about 60% to 70% of oropharyngeal cancers", cited. | CDC, *Basic Information about HPV and Cancer*: "about 60% to 70% of cancers of the oropharynx may be linked to HPV". CDC does not tie the share to type 16 alone. |
| 17 | P2 | 597184 12.10 Chapter Guide, Health Career Connection | Same HPV claim reworded to match #16. Not re-cited. | (as #16) |
| 18 | P3 link | 597158 10.5 | Hemoglobin Bart's image source href changed from http://www.pdb.org (now redirects to wwpdb.org) to https://www.rcsb.org/structure/1I3D. | — |
| 19 | P3 link | 597169 11.4 | "noncompetitive inhibitor" link (title and href) changed from the Jakubowski page now in LibreTexts "Purgatory" to Jakubowski and Flatt, *Fundamentals of Biochemistry*, Ch. 6 Enzyme Activity. | URL returns 200. |
| 20 | P3 link | 597170 11.5 | UKY vitamin E PDF URL changed to publications.mgcafe.uky.edu (the old URL 301-redirects there). | — |
| 21 | P3 link | 597170 11.5 | Almond Almanac URL changed from almonds.it to it.almonds.org (the old URL 301-redirects there). | — |

## Same wrong number on other chapters' pages (not edited; another group's)
- **597136 (8.3 Important Hexoses, Ch 8):** "aspartame … about 180 times sweeter than sucrose". It should read "about 200 times" (MedlinePlus).

## Skipped
- **All other P3 items from the audit:**
  - Almond 80% footnote.
  - Industry source for vitamin E.
  - Feedstuffs source in 597169.
  - CDFA newer data.
  - Title 8 wording in 597163.
  - HBV vaccine wording in 597183.
  - Valley fever 5–10% citation in 597182.
  - History citations (Fleming, AZT, HGP, Casgevy, Fischer/Koshland, asparagine).
  - Lactase 65%, CDPH lead, amoxicillin wording.
  - genome.gov slug redirects.
  - CalEPA trailing slash.
- **ChemistryViews "Further reading" links:** left as is. They block automated fetches but exist.
- **597163 and 597170:** both changed since the audit. On 597170 only two href strings were touched, and both are confirmed present in the current file. 597163 has no P2 item.

## For the author
- **597162 nitrate box:** the new first sentence reports a 200-well study sample, not a valley-wide rate. If you want a valley-wide figure, there isn't a good public one. The GAMA 2006 survey (44% of 136 Tulare County valley-floor wells) is the alternative.
- **597159 and 597165 albumin range:** changed to the MedlinePlus 3.4–5.4 g/dL. If your lecture uses 3.5–5.0, you could keep that number with a "ranges vary by lab" note instead.
