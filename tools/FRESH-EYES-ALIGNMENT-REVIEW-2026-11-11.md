# Fresh-eyes alignment review: CHEM 3B textbook + ADAPT (2026-11-11)

Six independent reviewers each read the live page bodies in `textbook-git/pages/live/`, the bank (`bank/*.json`) and the ADAPT export (`adapt/`). They checked them against `tools/COR_outline.md` (the Spring 2027 COR), `tools/CONVENTIONS.md` and the instructor rules. Nothing was edited.

"✔ confirmed" means I re-checked the item myself in the live HTML or the actual image. Everything else is as reported by a reviewer, with an exact quote, and has not been re-checked yet.

## Bottom line
- **COR coverage is complete.** Every topic in COR units 1–17 has a home in the book. The answer keys are clean: the reviewers spot-solved about 60 bank items and the worked examples in Ch 11–12, and checked every β-oxidation ATP tally, and found no wrong keys. The ATP convention is consistent everywhere.
- **The original "Lecture Connection" layers are accurate and at GOB level.** The Central Valley boxes were rated accurate, sourced and respectful in every chapter. Examples: tule fog, Tulare dairy, almonds/aflatoxin, nitrate, Cal/OSHA heat rules, chlorpyrifos, raisins, wine, wildfire smoke.
- **Nearly every real problem is in the inherited Ball/Malik source text left above the Lecture Connections.** That text:
  - has factual errors;
  - carries 2000s-era clinical content;
  - re-teaches the same pathway two or three times;
  - in a few places contradicts the book's own conventions.
- **ADAPT/bank:** the reviewers found no correctness problems, but the balance is off.
  - Chirality wedge/dash items, Ch 1 review and fatty-acid ATP arithmetic are over-weighted.
  - About 15 COR subtopics have 0–2 items.
  - Central Valley context is almost absent from the questions.

---

## Tier 1 — Wrong chemistry or clinical facts a student would learn (fix first)
| Page | Section | Problem | Fix |
|---|---|---|---|
| 597164 | 10.11 Guide | ✔ "Nine are essential (must come from food)" | ten (arginine convention) |
| 597144 | 9.1 table | ✔ arachidonic acid `CH3(CH2)4(CH2CH=CH)4(CH2)2COOH` puts the first C=C at ω-7 | `CH3(CH2)4(CH=CHCH2)4(CH2)2COOH` |
| 597139 | 8.6 | ✔ galactosemia milk restriction "not permanent" | lifelong; delete |
| 597192 | 13.4 | ✔ "58% of released energy that is not conserved" (the same page says 35% is conserved) | 65% |
| 597203 | 14.4 | ✔ electrons go "from … higher reduction potential to … lower" (stated twice) | lower → higher, or drop the reduction-potential language |
| 597069 | 2.5 Ex 2b | ✔ the answer image shows **4-isopropyl**-2-methylheptane for "4-ethyl-2-methylheptane"; its alt text says a third name (4-ethyl-3-methylheptane) | redraw (file 27436) and fix the alt text |
| 597069 / 597072 / 597121 | 2.5 Ex 1, 2.8 Ex 2, 7.1 Ex 2 & 5 | ✔ the images are correct but the **alt text names the wrong molecule** (2-methylbutane, 2,4-dimethylpentane, 2-bromobutane, 3-bromo-2-methylpentane, ethyldimethylamine, 3-methyl-2-butanamine) | fix the alt text only |
| 597085 | 3.8 Table 2 | ibuprofen alt text/structure is sec-butyl; ibuprofen is isobutyl | use the Bond Voyage drawing |
| 597093, 597105 | 4.4, 5.4 | methanol toxicity blamed on formaldehyde (it is formate); 5.4 gives ethanol as the antidote | formate; fomepizole first-line |
| 597106 (+597108 P5.9) | 5.5 | cis/trans called diastereomers right after "we call them cis–trans"; Fig 1 lists "conformational isomers" as stereoisomers; broken figure references | delete the paragraph, replace the figure, fix the references and P5.9 |
| 597163 | 10.10 | alcohol "sterilizes" (the text above says it doesn't); Alzheimer's, Huntington's and Parkinson's listed alongside prion diseases | "disinfects"; separate prions from other misfolding diseases |
| 597146 | 9.3 | infant respiratory distress passage: lecithin defined as PE/PI/PS; surfactant described as "lecithin + sphingomyelin"; risk "before 28 weeks" | rewrite around DPPC; risk extends to about 34 weeks |
| 597169 | 11.4 | penicillin box: Gram-positive defined wrongly; "fatal coma"; pneumonia "kills only the very old" | short modern box: β-lactam, real allergy rates, MRSA, stewardship |
| 597183, 597185 | 12.9, P12.53/12.62 | mRNA-vaccine argument rests on "no reverse transcriptase in human cells" (false: telomerase, LINE-1) | argue from cytoplasm and rapid degradation instead |
| 597192 | 13.4 | diabetes box: glyburide "increases receptor sensitivity"; target 70–120; "juvenile/adult-onset"; no metformin, GLP-1 or SGLT2 | replace; point to 13.7 |
| 597193 | 13.5 | "lactate makes muscles tire and sore" (contradicts 13.4) | match 13.4 |
| 597072 / 597040 | 2.8 / Ch 2 opener | ethyl chloride as an "emergency general anesthetic"; sevoflurane/desflurane called "hydrocarbons" | delete; "halogenated ethers" |
| 597059 | 1.6 | "Trans fats are used in many prepared and fried foods"; MyPyramid image captioned as MyPlate | rewrite to the current FDA status |
| 597154 | 10.1 | "Basic: contains an N … lone pair" (this would make Trp, Asn and Gln basic); Arg "almost as strong a base as NaOH" | fix both |
| 597102 | 5.1 | β-hydroxybutyrate called a ketone | match P5.62 |
| 597127 | 7.7 | "Liver disease slows amide hydrolysis" (acetaminophen: glucuronidation/sulfation; lidocaine: CYP) | "liver metabolism" |

## Tier 2 — The book contradicts its own conventions (students are graded on these)
- **Citrate synthase.** 597166 11.1 and 597173 11.8 say "'Synthase' (no ATP) is a lyase." That contradicts 14.3, the Glossary and CONVENTIONS (citrate synthase is a ligase). State the exception.
- **Feedback inhibition** is filed as a noncompetitive example in 11.4, 11.6 and 11.8. CONVENTIONS says it is allosteric regulation.
- **"Point mutation" titles.** The 12.6 figure caption and table title still group insertions and deletions as point mutations.
- **Heavy metals** are called "irreversible" on 597169 and in P11.59, but "both" in Cumulative 11.3. Use "both" throughout.
- **pKa-style reasoning without the word.** 10.2 has the carboxyl switch "at about pH 2" and the amino switch "at pH 9–10", with pI "halfway between". 10.4 sets a side-chain charge from the free amino acid's pI.
- **Curved arrows.** 10.6 draws peptide resonance with curved arrows. The 15.3 figure and its alt text describe a mechanism ("acylate attacks the alpha phosphate").
- **E/Z and optical rotation.** The 6.5 Valley box says "(Z)-3-hexenyl acetate"; 5.5 says "(–)-menthol".
- **10.5 calls "hydrophobic interaction" "often misused".** CONVENTIONS requires that exact term.
- **Ester boiling-point rule.** 6.6, 6.11 and P6.56 say "ester ≈ aldehyde/ketone", but the page's own chart shows the ester lower. P6.65(e) contradicts P6.66.
- **Lipase products.** Ch 9 (597145, 597150 Ex 5, 597151 P9.65a) gives glycerol + 3 fatty acids; Ch 15 stops at a monoacylglycerol.
- **Numbers that disagree between pages:**
  - Glycogen depletion: 12–24 h, ~24 h and 12–18 h.
  - Energy efficiency: 35% vs 34%.
  - Replication error rate: 1 in 10⁹ vs 1 in 10¹⁰.
  - Glycogen branch spacing: three different values.
  - Lactose intolerance: two sets of figures on 8.6.
  - Brown fat in adults: 14.4 vs 15.6.

## Tier 3 — Dated clinical content in inherited source text (clinical currency)
- **12.7 HIV** is frozen at about 2007. Update to integrase single-tablet regimens, PrEP, U=U, and person-first language.
- **12.8 genetic engineering:**
  - Flu vaccine listed as recombinant.
  - Bt crops called "hold promise".
  - Fingerprinting mixes restriction-enzyme and STR methods.
  - No CRISPR/Casgevy.
  - The 12.6 "Looking Closer" box is a 1980s essay; delete it.
- **9.2 / 9.6 (Ball):**
  - Advice to keep fat <30% of calories; "most peanut butter partially hydrogenated".
  - 2006 CDC data, "600 mg cholesterol", the LDL:HDL ratio.
  - "Sex-change operations" (use "gender-affirming hormone therapy").
- **Lipid panel "needs a fasting blood draw"** in 3 places (597149, 597150, P9.55d). Non-fasting has been standard since 2018.
- **4.8** lists halothane, enflurane and isoflurane plus the miscarriage claim. Use sevoflurane/desflurane.
- **7.3/7.8** nicotine lethal dose "about 50 mg"; current estimate is 0.5–1 g. Add pediatric e-liquid poisoning.
- **15.5** cholesterol box: "saturated … fatty acids serve as catalysts"; unnamed "study"; dead source.
- **Other dated items:**
  - 12.6 PKU screening window (now 24–48 h); stigmatizing IQ statistics.
  - CF: no mention of modulators (Trikafta, F508del).
  - 11.4 methanol antidote: name fomepizole.
  - 5.2 formaldehyde is a "known" (not "likely") carcinogen.
  - 4.4 CO deaths: about 2,200 per year.
  - Bovine insulin, Clinitest, glucose-oxidase meters.
- **Missing high-yield items:**
  - prediabetes (fasting 100–125 mg/dL, A1c 5.7–6.4%), never named in Ch 8;
  - GLP-1 agonists and SGLT2 inhibitors, plus euglycemic DKA in 15.7;
  - osmosis and IV-fluid tonicity in 9.5;
  - pulse oximetry reading falsely normal in CO poisoning (2.7).

## Tier 4 — Structure, order and redundancy (learner experience)
- **Ch 15 order** jumps between lipids and proteins:
  - Protein digestion (15.9) comes after amino acid degradation.
  - The urea cycle is separated from transamination.
  - Mobilization comes after β-oxidation.
  - Proposed order:
    - Lipids: digestion/lipoproteins → storage/mobilization/glycerol → activation/carnitine → β-oxidation → ketone bodies → lipogenesis.
    - Proteins: digestion/N balance → transamination/deamination → urea cycle → carbon skeletons/overlap → amino acid synthesis.
  - Lipid digestion (COR 16.1) is hidden inside 15.1 "Fatty Acid Activation".
- **Ch 13–14 duplication:**
  - Glycolysis taught 3× (13.4, 13.5, 14.1).
  - Pyruvate → acetyl CoA taught 3×.
  - Citric acid cycle and ETC taught 2× (14.2, then 14.3/14.4).
  - β-oxidation taught 3×.
  - The pentose phosphate pathway is hidden under the title "Entry of Other Sugars" (13.6).
  - 13.7 (hormonal control) comes before the glycogen and gluconeogenesis sections it depends on.
- **Ch 12:**
  - RNA types and transcription are taught in 12.3, 12.4 and 12.9.
  - 12.9 repeats 12.5 almost word for word.
  - 12.9 sits after Genetic Engineering.
- **Pages that copy or repeat other pages:**
  - 7.8's body is a word-for-word copy of 7.3.
  - 10.3's body is a copy of 10.2.
  - Membrane lipids are taught 3× (9.3–9.5) with conflicting terms (cephalin).
  - 10.4 and 10.6 duplicate peptide naming.
  - 6.10 re-teaches amine salts before Ch 7.
- **Majors-level text to trim:**
  - 14.4 Q-cycle, Fe–S, Cu/Mg/Zn atoms, rotor subunits.
  - 15.8/15.11 enzymology (AMPK, ACC, SAM/THF).
  - 5.4 Jones reagent and hydrates.
  - 6.2 acid → aldehyde reduction (also P6.63–64).
  - 1.7 hybridization/σ–π, with a garbled aromatic definition.
  - 12.6 table of 16 genetic diseases.
  - 11.4 Ball poisons table.
- **Exercises with no answers:** 12.2 (even items), 12.3 Ex 1–2, 12.5 Ex 4, 2.5, 2.8, 3.1 Ex 2, 3.8 Ex 1–2.
- **Alt text gives away exercise answers** to screen-reader users: 4.2, 5.1, 6.5, 7.1 and 7.4 Exercise 1.
- **Orphan figure references:** 15.8 and 15.11 (15.11 also prints its Summary twice), 8.3 "Figure 1", 5.5.
- **Mislabeled answer headings** in 597191, 597200, 597208 and 597210.
- **Broken or off-book links:** 597059, 597067, 597070 (×2) and 597080 go to Workbench; 597057 links to the Windward course and 597071 to Purdue.

## Tier 5 — Front matter and the alignment page
- **ADAPT is invisible to students.**
  - About This Book (597270) never mentions ADAPT.
  - For Instructors (597396) says ADAPT is "being built … contact the author".
  - Every Practice Problems page says the sets are live.
  - Proposed fix: add the route read → Try It → Practice Problems → ADAPT (graded, via Canvas) → Games.
- **Course Outline Alignment (597272) corrections:**
  - Add a row for COR 17.5 (→ 15.4). Two reviewers flagged this independently.
  - 2.6 → add 2.7.
  - 3.3 → add 3.3.
  - 1.3 → drop 2.1.
  - 4.1 → 4.2 / 5.5.
  - 7.5 → not 6.9.
  - 9.3 → 8.5.
  - 10.1 → 9.1.
  - 11.3 → 10.4 / 10.6.
- **About This Book** says every chapter opens with outline-worded objectives. That is not true: the openers have none, and the section learning objectives use source wording. The 5.5 learning objectives omit COR 6.2–6.4; the 8.4 objectives omit Fischer ↔ Haworth.
- **For Instructors** is missing the no-E/Z, no-conformer and no-Newman/chair rules, and thiol in the acid ranking.
- **Lab experiment numbers** are cited in 1.5, 2.1, 2.4 and 3.7, but For Instructors says they "will be added".
- **Possible addition:** a short "how to use this book if you work / are learning English" note, pointing to the Spanish glossary.
- **COR 8.6** names "nucleophilic acyl substitution", but the term never appears. Name it once in 7.6, with no mechanism.
- **"Reactions at a Glance" gaps:**
  - 3.9: benzene halogenation, nitration and sulfonation; polymerization.
  - 4.11: alcohol combustion, thiol → disulfide.
  - 5.6: acetal hydrolysis.

## Tier 6 — ADAPT and question-bank balance
- **Data note.** The correct answer is always `c[0]` (`k` is a calculator flag). ADAPT zips hold 962 unique items. The CSV covers only the 405 main-set items.
- **Orphans.** 43 text items are in no export because no widget regex catches them. Several are the only coverage for their COR topic:
  - 2.1 carbon classification: 0014
  - 2.7 halogenation: 0020, 0351
  - 2.9 polymers: 0025
  - 17.1 protein digestion: 0305, 0307, 0340
- **COR subtopics with 0 items:**
  - 3.3 aromatic property ranking
  - 4.4 Le Chatelier/dehydration reversibility
  - 9.5 aldaric/alduronic acids
  - 10.2 leukotrienes/thromboxanes
  - 10.3 fat oxidation/rancidity
  - 11.1 one-/three-letter codes and D/L
  - 12.3 covalent modification/zymogens
  - 13.6 recombinant DNA
  - 16.3 unsaturated fatty-acid oxidation
  - 17.2 protein turnover
  - 8.8 neurotransmitter definition and function
  - NaHCO3/NaOH acid tests, biuret, ninhydrin
- **Over-weighted topics:**
  - Chirality wedge/dash: 73 bank items / 57 ADAPT items. About 30 are near-clones (0777–0823), including 2-center and ring cases 0785, 0788, 0822 and 0823.
  - Ch 1 review: 101 items.
  - Molar mass ×13 and strong acid/base ×9 (CHEM 3A material).
  - Fatty-acid ATP arithmetic: 26 items.
- **Off-COR items:**
  - dehydrohalogenation, dehalogenation and dehydrogenation (0237–0239, 0914–0917);
  - acid reduction (0246, 0926).
- **Item fixes:**
  - 0199: CK-MB → troponin.
  - 0641: hydroquinone skin-lightening framing.
  - 0161: garbled sentence.
  - 0445: the hint gives the answer away.
- **Duplicates.** 14 Ch 3 items appear in both `Ch03_extra` and `Ch03_more`. Check whether both copies are live in ADAPT.
- **Licensing mismatch.** 36 image credit lines in the zips say CC BY-NC-SA, but the bank is CC BY 4.0.
- **Central Valley context is in about 4 of 1,045 questions.** Candidates for 15–20 new items:
  - valley fever antifungals;
  - farmworker organophosphate exposure (cholinesterase);
  - heat illness and enzyme denaturation;
  - diabetes, A1c and glycation;
  - dairy and lactose;
  - aflatoxin in nuts.

## Suggested order of work
1. Tier 1 and Tier 2 as live surgical edits (about 35 pages), plus the matching repo PR, using the existing edit-list JSON method.
2. Tier 5 front matter and alignment-page corrections (3 pages).
3. Tier 3 clinical-currency rewrites (box-sized replacements).
4. Tier 6 ADAPT rebalance: export the orphans, write the gap items, trim the clones.
5. Tier 4 restructure (Ch 15 reorder, Ch 13–14 and 12 de-duplication). This is the largest job; it moves LibreTexts pages and renumbers sections, which affects ADAPT, Canvas and game links. Do it last, ideally between terms.
