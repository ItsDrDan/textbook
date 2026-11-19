# fixr3_t5_ch13-15 notes (Round 3, author decisions, 2026-11-18)

Script: `SCRATCH/fixr3_t5_ch13-15.py`, 21 `e()` edits. The dry run on the current `pages/live/` (batch AQ live) matched all 21 exactly once. Edits JSON: `SCRATCH/fixr3_t5_ch13-15.json`. No repo file was written.

Post-checks in the script:
- 597193 and 597202 no longer contain "wikipedia" or "by-sa" anywhere.
- 597213 no longer says "20 mg of ketone".

## 1. Wikipedia credits removed after rewriting (597193, 597202)

What was actually borrowed:
- **597193:** the Malik CC0 text credited a step list to it.wikipedia "Glicolisi". Every step figure on the page is already DK's own SVG.
- **597202:** the Malik text credited "equations" to ru.wikipedia "Цикл трикарбоновых кислот". On ru.wikipedia those equations are images (Krebs_Cycle_Reaction_N_ru.png). All of them were replaced earlier by DK's own step SVGs (`figures/pathways/cac/step1–8.svg`), so no ru.wikipedia material is left on the page.

For each step I compared the live sentence with the current Wikipedia text, translated in short. Any sentence that kept the source's order or structure was rewritten. Steps 1, 3 and 6 of glycolysis and steps 1–3 of the cycle were already DK's own explanatory writing, with no match in the source, so they are unchanged. The existing "Adapted from … (Malik), CC0" credit lines stay.

### 597193 (13.5) glycolysis, it.wikipedia "Glicolisi" (translated) vs final

| Step | it.wikipedia (translated, short) | Live before | Final |
|---|---|---|---|
| credit | – | "(Step list adapted from the Italian Wikipedia article Glicolisi, CC BY-SA 4.0.)" | removed; the sentence is now just "The ten reactions of glycolysis are the following." |
| 1 | "Intracellular glucose is phosphorylated by the enzyme hexokinase… one of the three key steps" | DK's own sentence (hexokinase moves a phosphate from ATP to the C6 –OH) | unchanged: already independent |
| 2 | "The next step consists of the isomerization of glucose-6-phosphate to fructose-6-phosphate" | "G6P, which is an aldohexose, isomerizes to F6P, which is a ketohexose." | "Phosphoglucose isomerase rearranges glucose 6-phosphate into fructose 6-phosphate. The C=O moves from C1 to C2, so an aldose becomes a ketose with the same formula." |
| 3 | "Following the isomerization, F6P undergoes another phosphorylation… not reversible" | DK's own sentence (PFK, second ATP, C1 –OH) | unchanged |
| 4 | "F1,6BP… is the true activated version of glucose… [the step] consists of the cleavage of F1,6BP" | "The open-chain form of F1,6BP, in equilibrium with the cyclic form, splits into two compounds, G3P and DHAP." | "Aldolase cuts fructose 1,6-bisphosphate between C3 and C4. It works on the open-chain form of the sugar, which is in equilibrium with the ring. Each three-carbon piece keeps one phosphate: one is DHAP, the other G3P." |
| 5 | "Aldolase split the hexose into two different trioses… TPI converts DHAP into G3P" | "This reaction is an isomerization reaction between G3P and its isomer DHAP." | "Triose phosphate isomerase converts DHAP and G3P back and forth. Only G3P goes on to step 6, so as G3P is used up, DHAP keeps turning into more of it." |
| 6 | "G3P is converted to 1,3-BPG by G3P dehydrogenase… the sum of two processes" | DK's own text (enzyme–cysteine thioester, oxidation, phosphate replaces –SH) | unchanged |
| 6 note | – | "The ketone group in DHAP does not oxidize directly but converts to G3P due to the equilibrium in reaction 5. So, reaction 6 and the reactions after it happen twice…" | "DHAP is never oxidized itself; step 5 turns it into G3P first. Each glucose therefore gives two G3P, and steps 6 to 10 run twice per glucose." |
| 7 | "1,3-BPG gives up a phosphate group to an ADP" | "A phosphate group is transferred from 1,3-BPG to ADP producing an ATP and a 3-phosphoglycerate." | "Phosphoglycerate kinase moves the high-energy phosphate on C1 of 1,3-bisphosphoglycerate onto ADP. The products are ATP and 3-phosphoglycerate." |
| 7 note | ("up to now two ATP have been spent") | "Since this step happens twice…, it compensates for the two ATP consumed, one in step 1 and the other in step 3." | "Because step 7 runs twice per glucose, its 2 ATP pay back the 2 ATP spent in steps 1 and 3." |
| 8 | "The position of the phosphate group is changed from carbon 3 to carbon 2" | "3-PG is isomerized to 2-PG. … mutase moves the phosphate group from carbon 3 to carbon 2." | "Phosphoglycerate mutase shifts the phosphate of 3-phosphoglycerate from C3 to C2, giving 2-phosphoglycerate. No atoms are gained or lost, so this is an isomerization." |
| 9 | "The penultimate reaction is essentially a dehydration of 2-PG" | "2-PG is dehydrated, i.e., H2O is eliminated from it, producing PEP." | "Enolase removes a water molecule from 2-phosphoglycerate (a dehydration). The new C=C sits next to the phosphate, and the product is phosphoenolpyruvate (PEP)." |
| 10 | "In the last step PEP, through pyruvate kinase… the phosphate group is given to an ADP to form ATP" | "PEP transfers its phosphate group to ADP producing pyruvate and ATP." | "Pyruvate kinase moves the phosphate from PEP onto ADP, giving ATP and pyruvate." |
| 10 note | – | "Since the reaction happens two times for each glucose, two ATP are produced in this step." | "Step 10 also runs twice per glucose, so it makes 2 ATP." |

### 597202 (14.3) citric acid cycle, ru.wikipedia (translated) vs final

| Step | ru.wikipedia (translated, short) | Live before | Final |
|---|---|---|---|
| credit | – | "The following equations of the reactions are adapted from the Russian-language Wikipedia article… (CC BY-SA 4.0), Wikipedia." | "The eight reactions of the cycle are the following." |
| 1–3 | condensation by citrate synthase; aconitase isomerization via cis-aconitate; oxidative decarboxylation of isocitrate | DK's own explanations (3° vs 2° alcohol, thioester hydrolysis, Mg2+) | unchanged: already independent; citrate synthase is not classed here (house rule: transferase, stated in the table) |
| 4 | "α-KG is converted to succinyl-CoA and CO2… nearly identical to the pyruvate dehydrogenase reaction" | "The fourth reaction resembles the previous link reaction's oxidative decarboxylation of pyruvate… NAD+ is reduced… acyl-group is transferred to HS-CoA…" (same order as the source: comparison, then the outcome) | "α-Ketoglutarate dehydrogenase does the same chemistry as pyruvate dehydrogenase (Section 14.1). A carboxylate leaves as CO2, the remaining four-carbon piece is oxidized while NAD+ is reduced to NADH, and the piece is attached to HS–CoA as a thioester. The product is succinyl CoA, as shown below." |
| 5 | "succinyl-CoA synthetase uses the thioester energy to phosphorylate GDP… GTP can pass its phosphate to ADP (equivalent)" | Malik two-step description plus DK's hydrolysis note | Rewritten in plain steps: phosphate replaces –S–CoA; DK's hydrolysis note kept; phosphate to GDP gives GTP (substrate-level, like glycolysis steps 7 and 10); GTP → ATP, "one GTP counts as one ATP" |
| 6 | "succinate is oxidized to fumarate by a flavoprotein" | "one FAD is reduced into FADH2 at the expense of oxidation of succinate to fumarate" | "Succinate dehydrogenase takes two hydrogens from the –CH2–CH2– of succinate, making the C=C of fumarate. FAD accepts them and becomes FADH2, as shown below." |
| 7 | "reversible hydration of fumarate to form L-malate" | "H2O hydrates the C=C of fumarate producing malate" | "Fumarase adds water across the C=C of fumarate (a hydration): –OH goes on one carbon and H on the other. The product is malate, as shown below." |
| 7 note | "fumarase hydrates the trans isomer but not the cis… stereospecific" | "Recall that the enzymes are stereospecific. … only fumarate (not its cis-isomer)… only L-malate" | "Fumarase is stereospecific. It accepts fumarate, the trans isomer, but not its cis isomer, and it makes only one enantiomer of malate, L-malate." |
| 8 | "L-malate dehydrogenase catalyzes the oxidation of L-malate to oxaloacetate" | "one more NAD+ is reduced into NADH at the expense of oxidation of malate into oxaloacetate" | "Malate dehydrogenase oxidizes the 2° –OH of malate to a ketone, giving oxaloacetate, and NAD+ is reduced to NADH, as shown below." |
| 8 note | (oxaloacetate consumed by citrate synthase) | "The oxaloacetate is the reactant of step 1 and begins the cycle again…" | "Oxaloacetate is where the cycle started, so it can now pick up another acetyl CoA and begin a new turn. One turn, for one acetyl CoA, adds up to this overall reaction." |
| two turns | – | "Recall that the catabolism of one glucose molecule produces two pyruvates… So, the citric acid cycle runs twice… One GTP ultimately converts into one ATP." | "One glucose gives two pyruvate, and each pyruvate gives one acetyl CoA in the link reaction, so the cycle turns twice per glucose. Each GTP counts as one ATP." |

The chemistry and house conventions are unchanged:
- FAD makes the C=C from –CH2–CH2–.
- GTP counts as 1 ATP.
- The page's "worth 20 ATP" line (2.5 per NADH, 1.5 per FADH2) is untouched.
- Enzyme classes are not restated in the step text; the page's own table still carries them, with citrate synthase as transferase.

The overall MathJax equations and all figures are untouched.

## 2. 597213 ketone figures

- **Before:** "the kidneys excrete about 20 mg of ketone bodies each day, and the blood levels are maintained at about 1 mg of ketone bodies per 100 mL of blood."
- **After:** "blood ketone bodies stay low, about 0.1 to 0.25 mmol/L (roughly 1 to 3 mg per 100 mL of blood), and only a very small amount is lost in the urine (Source: Puchalska P, Crawford PA, Multi-dimensional roles of ketone bodies…, Cell Metabolism, 2017)."
- **Blood level source:** Puchalska & Crawford 2017 (PMC5313038): healthy adults' total ketone bodies "normally exhibit circadian oscillations between approximately 100–250 µM", rising to about 1 mM after 24 h of fasting. Converting at about 103 g/mol (acetoacetate 102, BHB 104), 0.1–0.25 mmol/L is about 1–3 mg/100 mL. The old "about 1 mg/100 mL" was the low end of that range, so it now shows as a range with the SI unit.
- **Urinary 20 mg/day:** I found no legitimate source for this number.
  - Tried: NCBI Bookshelf (Clinical Methods, StatPearls Ketogenesis), which blocks automated access; a download attempt was refused by the session's permission check, so I did not retry.
  - MedlinePlus gives no numbers.
  - A 1958 study of healthy men (Johnson, Sargent & Passmore), seen only as a secondary copy, reports about 0.9–2.8 µmol/min. That would be roughly 130–400 mg/day, far above 20 mg.
  - Puchalska & Crawford support only "a very small fraction" in urine.
  - So the number was removed and the qualitative statement cited. If the author has Tietz or another clinical chemistry text with a daily figure, he can put a number back with that page cited.
- **Anion-gap example:** kept as is, per the author.

## Needs the author
- If he wants a daily urinary ketone figure, it needs a print source (e.g., Tietz) that he can cite with a page number. I did not guess one.
