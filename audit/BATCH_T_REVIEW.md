# Batch T review sheet (draft, not published)

65 page edits on 28 pages and 20 figure-file uploads, built by `tools/batchT_build.py`. Exact strings: `tools/batchT_2026-11-13.json`.

## A. Duplicated prose trimmed (14.2, 14.4, 15.4, 15.5) and conflicts fixed (15.6)

Only text that is told again elsewhere on the same page was cut. Figures, tables, examples, exercises, objectives, summaries, boxes and credits were not touched.

### 14.2: Stage III of Catabolism (597201): 2858 → 2719 words

- **cut: What one turn of the citric acid cycle yields** (kept: "Per turn (per acetyl CoA): 2 CO2, 3 NADH, 1 FADH2, 1 GTP")
  - was: Over the next seven steps, two carbons leave as CO 2 , three NAD + and one FAD are reduced, one GTP (worth one ATP) is made, and oxaloacetate is regenerated so the cycle can turn again.
  - now: (removed)
- **cut: Definition of oxidation and reduction** (kept: "Loss of Electrons is Oxidation, Gain of Electrons is Reduction")
  - was: Recall that a compound is reduced when it gains electrons or hydrogen atoms and is oxidized when it loses electrons or hydrogen atoms.
  - now: (removed)
- **cut: Chain components are reduced and then reoxidized as electrons pass along** (kept: "The metal ions can be reduced and then oxidized repeatedly as electrons are passed")
  - was: Each intermediate compound in the electron transport chain is reduced by the addition of one or two electrons in one reaction and then subsequently restored to its original form by delivering the electron(s) to the next compound along the chain. The successive
  - now: The successive
- **cut: ATP per NADH (2.5) and per FADH2 (1.5); older 3 and 2** (kept: "This course uses 2.5 ATP per NADH and 1.5 per FADH2")
  - was: Experiment has shown that about 2.5 ATP molecules are formed for every molecule of NADH oxidized in the electron transport chain, and about 1.5 ATP molecules for every molecule of FADH 2 oxidized (older books use 3 and 2). Table
  - now: Table

### 14.4: Oxidative Phosphorylation (597203): 5460 → 5218 words

- **merge: Electrons pass to carriers that hold them more tightly; energy released per step** (kept: "At each step, electrons pass to a carrier that holds them more tightly")
  - was: In each step, the electrons are passed to a carrier that holds them more tightly, that is, one with a higher (more positive) reduction potential. Energy is released in each step, and the bigger the difference between the two carriers, the more energy is released. The energy is converted
  - now: Energy is released at each step. The energy is converted
- **cut: The two mobile carriers (coenzyme Q, cytochrome c) and their routes** (kept: "moves freely inside the lipid bilayer of the inner membrane, carrying electrons from Compl")
  - was: Coenzyme-Q ( Q ) is a hydrophobic electron carrier molecule that moves in a hydrophobic environment inside the lipid bilayer of the inner membrane from complexes I and II to complex III. Cytochrome c ( Cyt \; c ) is a hydrophilic electron carrier molecule that moves along the surface of the inner membrane facing the intermembrane space from complex III to complex IV.
  - now: (removed)
- **cut: Coenzyme Q carries electrons to Complex III** (kept: "carrying electrons from Complex I and Complex II to Complex III")
  - was: QH2 then carries the electrons through the membrane to Complex III.
  - now: (removed)
- **cut: Coenzyme Q carries electrons to Complex III** (kept: "carrying electrons from Complex I and Complex II to Complex III")
  - was: Coenzyme-Q passes on the electrons from complex II to complex III as from complex I to complex III.
  - now: (removed)
- **cut: Cytochrome c carries electrons from Complex III to Complex IV** (kept: "carrying electrons one at a time from Complex III to Complex IV")
  - was: Cyt~ c carries the electron to complex IV.
  - now: (removed)
- **fix-conflict: Definition of oxidative phosphorylation (ATP synthesis alone vs electron transport coupled to ATP synthesis)** (kept: "oxidation of NADH and FADH2 coupled to phosphorylation of ADP, is oxidative phosphorylatio")
  - was: in a process called oxidative phosphorylation . It takes
  - now: ; this is the phosphorylation half of oxidative phosphorylation. It takes
- **merge: Mushroom shape of ATP synthase: F_O in the membrane, F_1 in the matrix** (kept: "is the hydrophobic part embedded in the inner membrane (see Figure")
  - was: It is in the shape of a mushroom with two major parts: a stem-like part which is a hydrophobic portion embedded in the inner membrane, is called F O, and a mushroom head-like part that protrudes into the matrix, is called F 1, as illustrated in Figure \PageIndex{2 a.
  - now: Its two major parts, F O and F 1 , are illustrated in Figure \PageIndex{2 a.
- **cut: Uncoupled electron transport releases all its energy as heat** (kept: "So, all energy released during the electron transport process becomes heat energy")
  - was: When the electron transport chain operates without ATP synthesis, all of the electron transport energy is used as heat.
  - now: (removed)
- **cut: Cyanide antidote hydroxocobalamin** (kept: "its cobalt binds cyanide to form cyanocobalamin, which the kidneys excrete")
  - was: The antidote hydroxocobalamin binds cyanide to form cyanocobalamin (vitamin B 12 ), which the kidneys excrete. 4
  - now: 4
- **cut: Why NADH is worth 2.5 ATP and FADH2 1.5 (three pumps vs two)** (kept: "Electrons from NADH pass through three proton pumps (I, III, IV); electrons from FADH2")
  - was: In short, each NADH gives about 2.5 ATP and each FADH 2 about 1.5 ATP, because electrons from NADH pass three proton pumps (Complexes I, III and IV) and electrons from FADH 2 pass only two (III and IV). Each GTP counts as one ATP.
  - now: Each GTP counts as one ATP.

### 15.4: Oxidation of fatty acids (597209): 4098 → 4007 words

- **cut: The four reactions repeat until only acetyl CoA is left** (kept: "goes through the process of four reactions again and again until the last")
  - was: The process repeats on the fragment acyl- CoA again and again until the last acyl- CoA fragment left is acetyl- CoA .
  - now: (removed)
- **cut: Acyl CoA is transported from cytosol into mitochondria (and the pointer 'as described next' leads nowhere: the next heading is Reaction 1)** (kept: "is transported from the cytosol into mitochondria for the second stage of")
  - was: As described next, acyl-CoA product is transported from the cytosol into mitochondria for the \beta -oxidation process.
  - now: (removed)
- **cut: Thiolysis leaves an acyl CoA two carbons shorter** (kept: "the rest of the chain, now two carbons shorter, stays attached to the new CoA")
  - was: The second product of the above reaction is an acyl- CoA with two C's fewer than the initial acyl- CoA .
  - now: (removed)
- **fix-conflict: 'cycles' vs 'repetitions' for rounds of beta-oxidation** (kept: "it is a linear set of four reactions that repeats, and each repetition gives")
  - was: the number of cycles for a fatty acid containing
  - now: the number of cycles (the Lecture Connection calls them repetitions) for a fatty acid containing
- **merge: Derivation of the ATP formula: +10 for the last acetyl CoA, -2 for activation (stated twice in a row)** (kept: "there are an additional 10 ATP's from the last acetyl-CoA. The activation step converts")
  - was: So, after adding ten from the last acetyl- CoA to the formula ( (0.5\times{n -1)\times{14 )~ ATP's and subtracting 2 for the 2ATP's consumed in the activation step, the formula
  - now: So, the formula
- **cut: Glucose is quick energy; fat is the denser long-term store** (kept: "Although glucose is a quick energy source that animals need, fatty acids have higher energ")
  - was: Glucose is a quick energy source, but animals use fats as relatively longer-term energy storage molecules due to their higher energy density.
  - now: (removed)
- **fix-conflict: 'cycles' vs 'repetitions' for rounds of beta-oxidation** (kept: "it is a linear set of four reactions that repeats, and each repetition gives")
  - was: 8 − 1 = 7 cycles, so
  - now: 8 − 1 = 7 repetitions, so
- **fix-conflict: 'cycles' vs 'repetitions' for rounds of beta-oxidation** (kept: "it is a linear set of four reactions that repeats, and each repetition gives")
  - was: (from step 1 of each cycle)
  - now: (from step 1 of each repetition)
- **fix-conflict: 'cycles' vs 'repetitions' for rounds of beta-oxidation** (kept: "it is a linear set of four reactions that repeats, and each repetition gives")
  - was: (from step 3 of each cycle)
  - now: (from step 3 of each repetition)
- **fix-conflict: 'cycles' vs 'repetitions' for rounds of beta-oxidation** (kept: "it is a linear set of four reactions that repeats, and each repetition gives")
  - was: one more cycle (1.5
  - now: one more repetition (1.5
- **fix-conflict: 'cycles' vs 'repetitions' for rounds of beta-oxidation** (kept: "it is a linear set of four reactions that repeats, and each repetition gives")
  - was: n /2 − 1 cycles.
  - now: n /2 − 1 repetitions.

### 15.5: Ketone Bodies and Ketoacidosis (597213): 2494 → 2398 words

- **cut: Acetone is exhaled; fruity breath** (kept: "The odor comes from acetone, the small, volatile ketone that is breathed out")
  - was: When the acetone in the blood reaches the lungs, its volatility causes it to be expelled in the breath. The sweet smell of acetone, a characteristic of ketosis, is frequently noticed on the breath of severely diabetic patients.
  - now: (removed)
- **fix-conflict: Blood pH in ketoacidosis (6.9 in source text vs 7.30 or lower in the Valley Connection)** (kept: "in DKA the blood pH is 7.30 or lower")
  - was: (to 6.9 from a normal value of 7.4)
  - now: (to as low as 6.9 from a normal value of 7.4)
- **cut: Untreated ketoacidosis leads to coma; it is an emergency** (kept: "that can lead to dehydration, and ultimately coma and death")
  - was: Untreated patients may go into a coma. At that point, prompt treatment is necessary if the person’s life is to be saved.
  - now: (removed)
- **cut: How DKA arises (no insulin -> fat breakdown -> ketone bodies)** (kept: "DKA starts when the body does not have enough insulin to move glucose")
  - was: In DKA insulin does not function, glucose cannot be used for energy, fats are broken down to acetyl CoA, and ketogenesis runs unchecked; the ketone bodies are soluble in blood and urine, and acetone is detectable in the breath.
  - now: (removed)

### 15.6: Biosynthesis of Fatty Acids (597214): 2104 → 2108 words

- **fix-conflict: Is lipogenesis beta-oxidation reversed? Where does it happen? (course convention: cytosol; elongation in the ER is stated under Elongation)** (kept: "These mirror the steps of beta-oxidation, but the compartment, carrier, coenzyme and hormo")
  - was: occurs in the cytosol and endoplasmic reticulum of the cell and is chemically similar to the beta-oxidation process, but with a couple of key differences.
  - now: occurs in the cytosol of the cell. Its reaction types mirror those of beta-oxidation, but it is a separate pathway with several key differences.
- **fix-conflict: Acetyl CoA carboxylase: 'only' vs 'main' regulated enzyme** (kept: "which makes malonyl-CoA, is the main regulated enzyme of fatty acid synthesis")
  - was: , the only regulatory enzyme of fatty acid synthesis
  - now: (removed)
- **fix-conflict: Is lipogenesis beta-oxidation reversed?** (kept: "Steps 2, 3, and 4 are the reverse of steps 3, 2, and 1")
  - was: From this point forward, the chemical reactions resemble those of beta oxidation reversed.
  - now: From this point forward, the reaction types mirror those of beta-oxidation in reverse order, although the pathway is not beta-oxidation run backward (see the Lecture Connection).

## B. Figures whose labels printed under 6 pt

Label font sizes raised so they print at about 6.1 to 6.4 pt; multi-line labels re-spaced; a few labels moved so they do not touch a box or an arrow (`tools/small_print_nudges.json`). Each result was rendered and looked at.

| Figure file | Shown on | PDF p. (18:41) | Printed before → after (pt) | Hosted |
|---|---|---|---|---|
| ch02.svg | 2.10 | 192 | 5.77 → 6.18 | GitHub |
| ch03.svg | 3.9 | 271 | 5.77 → 6.18 | GitHub |
| ch07.svg | 7.12 | 594 | 5.77 → 6.18 | GitHub |
| fig-p597137-fischer-to-haworth.svg | 8.4 | 649 | 5.75 → 6.19 | LibreTexts (upload) |
| fig-p597144-7.svg | 9.1 | 715 | 5.31 → 6.28 | LibreTexts (upload) |
| fig-p597146-phosphatidylcholine.svg | 9.3 | 731 | 5.4 → 6.3 | LibreTexts (upload) |
| sphingolipids.svg | 9.4 | 738 | 5.61 → 6.23 | GitHub |
| fig-p597157-1.svg | 10.4 | 808 | 5.51 → 6.15 | LibreTexts (upload) |
| ch10.svg | 10.11 | 848 | 5.77 → 6.18 | GitHub |
| fig-p597172-2.svg | 11.7 | 917 | 5.79 → 6.27 | LibreTexts (upload) |
| ch11.svg | 11.8 | 925 | 5.77 → 6.18 | GitHub |
| fig-p597183-2.svg | 12.5 | 989 | 5.75 → 6.23 | LibreTexts (upload) |
| fig-p597183-3.svg | 12.5 | 989 | 5.75 → 6.13 | LibreTexts (upload) |
| fig-p597179-elongation.svg | 12.6 | 1000 | 5.72 → 6.18 | LibreTexts (upload) |
| ch12.svg | 12.10 | 1023 | 5.77 → 6.18 | GitHub |
| fig-p597192-1.svg | 13.4 | 1081 | 5.67 → 6.11 | LibreTexts (upload) |
| fig-p597193-glycolysis-flow.svg | 13.5 | 1094 | 5.35 → 6.21 | LibreTexts (upload) |
| fig-p597196-1-1.svg | 13.7 | 1108 | 5.49 → 6.18 | GitHub |
| fig-p597196-1-2.svg | 13.7 | 1108 | 5.49 → 6.18 | GitHub |
| fig-p597197-5.svg | 13.8 | 1119 | 5.67 → 6.14 | LibreTexts (upload) |
| ch13.svg | 13.10 | 1135 | 5.77 → 6.18 | GitHub |
| fig-p597202-cac-flow.svg | 14.3 | 1174 | 5.57 → 6.21 | LibreTexts (upload) |
| fig-p597202-1-v2-1.svg | 14.3 | 1174, 1181 | 5.37 → 6.19 | GitHub |
| fig-p597202-1-v2-2.svg | 14.3 | 1174, 1181 | 5.37 → 6.19 | GitHub |
| fig-p597202-1-v2-3.svg | 14.3 | 1174, 1181 | 5.37 → 6.19 | GitHub |
| fig-p597204-yield-flow.svg | 14.5 | 1200 | 4.77 → 6.29 | LibreTexts (upload) |
| fig-p597204-2.svg | 14.5 | 1200 | 5.31 → 6.28 | LibreTexts (upload) |
| fig-p597207-1.svg | 15.1 | 1237 | 5.66 → 6.13 | LibreTexts (upload) |
| fig-p597212-1.svg | 15.2 | 1240 | 5.89 → 6.3 | LibreTexts (upload) |
| fig-p597212-2.svg | 15.2 | 1240 | 5.89 → 6.1 | LibreTexts (upload) |
| glycerol-glycerol-3-phosphate.svg | 15.4 | 1259 | 5.3 → 6.12 | GitHub |
| fig-p597209-1.svg | 15.4 | 1259 | 5.3 → 6.18 | LibreTexts (upload) |
| fig-p597209-2.svg | 15.4 | 1259 | 5.3 → 6.18 | LibreTexts (upload) |
| fa_synthesis-v2-1.svg | 15.6 | 1268 | 5.74 → 6.26 | GitHub |
| fa_synthesis-v2-2.svg | 15.6 | 1268 | 5.74 → 6.26 | GitHub |
| step1.svg | 15.9 | 1283 | 5.74 → 6.2 | GitHub |
| step2.svg | 15.9 | 1283, 1284 | 5.74 → 6.2 | GitHub |
| step3.svg | 15.9 | 1283, 1284, 1285 | 5.74 → 6.2 | GitHub |
| step4.svg | 15.9 | 1284 | 5.74 → 6.2 | GitHub |
| fig-p597216-2.svg | 15.9 | 1285 | 5.11 → 6.17 | LibreTexts (upload) |
| ch15.svg | 15.12 | 1298 | 5.77 → 6.18 | GitHub |

## C. Try It boxes on the twelve thin sections

- 2.3 Try It: five new questions added to the selection (12 in the pool, 10 per round)
- 2.5 Try It: five new questions added to the selection (11 in the pool, 10 per round)
- 4.2 Try It: five new questions added to the selection (14 in the pool, 10 per round)
- 4.9 Try It: five new questions added to the selection (13 in the pool, 10 per round)
- 6.1 Try It: five new questions added to the selection (11 in the pool, 10 per round)
- 6.5 Try It: five new questions added to the selection (13 in the pool, 10 per round)
- 8.5 Try It: five new questions added to the selection (11 in the pool, 10 per round)
- 8.7 Try It: five new questions added to the selection (13 in the pool, 10 per round)
- 10.1 Try It: five new questions added to the selection (14 in the pool, 10 per round)
- 13.3 Try It: five new questions added to the selection (14 in the pool, 10 per round)
- 15.3 Try It: five new questions added to the selection (13 in the pool, 10 per round)
- 15.9 Try It: five new questions added to the selection (13 in the pool, 10 per round)

## New bank questions (60; in `bank/`, live when this branch is merged)

**Section 2.3**

- Three of these condensed formulas are the same compound written in different ways. Which one is a different compound, a constitutional isomer of the other three? **Answer:** CH 3 CH 2 CH(CH 3 )CH 2 CH 3
- Pentane, C 5 H 12 , has three constitutional isomers. How many of them have a longest continuous chain of exactly four carbons? **Answer:** 1
- Which compound is a constitutional isomer of pentane, CH 3 CH 2 CH 2 CH 2 CH 3 ? **Answer:** C(CH 3 ) 4
- A student writes CH 2 (CH 3 )CH 2 CH 2 CH 3 and calls it a branched isomer of pentane. What is this compound really? **Answer:** pentane itself, because a CH 3 on an end carbon only makes the chain longer
- Which is the smallest alkane that has a constitutional isomer? **Answer:** butane, C 4 H 10
**Section 2.5**

- What is the IUPAC name of CH 3 CH 2 C(CH 3 ) 2 CH 2 CH 2 CH 3 ? **Answer:** 3,3-dimethylhexane
- Which condensed formula is 2,3-dimethylpentane? **Answer:** CH 3 CH(CH 3 )CH(CH 3 )CH 2 CH 3
- What is the IUPAC name of CH 3 CH(CH 3 )CH(CH 3 )CH(CH 2 CH 3 )CH 2 CH 2 CH 3 ? **Answer:** 4-ethyl-2,3-dimethylheptane
- What is the IUPAC name of CH 3 CH(CH 2 CH 3 )CH 2 CH 2 CH 3 ? **Answer:** 3-methylhexane
- What is the molecular formula of 3-ethyl-2-methylpentane? **Answer:** C 8 H 18
**Section 4.2**

- What is the IUPAC name of CH 3 CH 2 CH(OH)CH 2 CH 2 CH 3 ? **Answer:** 3-hexanol
- Which of these is a tertiary (3°) alcohol? **Answer:** 2-methyl-2-butanol, CH 3 C(CH 3 )(OH)CH 2 CH 3
- Cyclohexanol is a six-carbon ring with one OH group on a ring carbon. How is this alcohol classified? **Answer:** secondary (2°)
- Which condensed formula is 3-methyl-1-butanol (3-methylbutan-1-ol)? **Answer:** (CH 3 ) 2 CHCH 2 CH 2 OH
- Rubbing alcohol is isopropyl alcohol, (CH 3 ) 2 CHOH. Which choice gives its IUPAC name and its classification? **Answer:** 2-propanol; secondary (2°)
**Section 4.9**

- What is the IUPAC name of CH 3 CH(SH)CH 2 CH 2 CH 3 ? **Answer:** 2-pentanethiol
- Two molecules of ethanethiol, CH 3 CH 2 SH, undergo mild oxidation [O]. What is the organic product? **Answer:** CH 3 CH 2 –S–S–CH 2 CH 3
- The disulfide CH 3 CH 2 CH 2 –S–S–CH 2 CH 2 CH 3 is treated with a reducing agent [H]. What forms? **Answer:** two molecules of 1-propanethiol, CH 3 CH 2 CH 2 SH
- Ethanethiol, CH 3 CH 2 SH (62 g/mol), boils at 35 °C. Ethanol, CH 3 CH 2 OH (46 g/mol), boils at 78 °C. What is the best explanation? **Answer:** The S–H bond is barely polar, so thiol molecules cannot hydrogen bond with each other.
- Which compound is a disulfide ? **Answer:** CH 3 –S–S–CH 3
**Section 6.1**

- What is the IUPAC name of CH 3 CH 2 CH(CH 3 )COOH? **Answer:** 2-methylbutanoic acid
- The ketone body 3-hydroxybutanoic acid (β-hydroxybutyric acid) builds up in the blood in uncontrolled diabetes. Which condensed formula is this compound? **Answer:** CH 3 CH(OH)CH 2 COOH
- Formic acid and acetic acid are the common names of the two smallest carboxylic acids. What are their condensed formulas, in that order? **Answer:** HCOOH and CH 3 COOH
- The name 3-methylpentanoic acid gives a number for the methyl group but none for the carboxyl group. Why is no number needed? **Answer:** The carboxyl carbon is always at the end of the parent chain and is always carbon 1.
- Which compound is a carboxylic acid? **Answer:** CH 3 CH 2 COOH
**Section 6.5**

- Which condensed formula is methyl propanoate? **Answer:** CH 3 CH 2 COOCH 3
- Pentyl ethanoate (pentyl acetate), CH 3 COOCH 2 CH 2 CH 2 CH 2 CH 3 , has a pear-like odor. Which acid and which alcohol do the two parts of this ester come from? **Answer:** ethanoic acid and 1-pentanol
- What is the IUPAC name of HCOOCH 2 CH 3 ? **Answer:** ethyl methanoate
- Which compound is an ester? **Answer:** CH 3 CH 2 COOCH 2 CH 3
- In propyl ethanoate, CH 3 COOCH 2 CH 2 CH 3 , how many carbon atoms belong to the acid part and how many to the alcohol part? **Answer:** 2 in the acid part, 3 in the alcohol part
**Section 8.5**

- Fructose is a ketose, with no aldehyde group, yet it gives a positive Benedict's test. Why? **Answer:** In the basic test solution fructose rearranges into an aldose, and the aldose is oxidized
- A glucose solution is heated with blue Benedict's reagent and a brick-red solid forms. Which statement describes the redox change? **Answer:** Glucose is oxidized and Cu 2+ is reduced to Cu 2 O
- A student heats four solutions with Benedict's reagent: glucose, fructose, maltose and xylitol (the sweetener in sugar-free gum). Which solution stays blue? **Answer:** xylitol
- Mannitol is made from the aldohexose mannose by reaction with H 2 and a metal catalyst. What change takes place? **Answer:** The –CHO group at C1 is reduced to –CH 2 OH, giving a sugar alcohol
- Glucose is warmed with Tollens' reagent, which contains Ag + . What is seen, and what does the glucose become? **Answer:** A silver mirror forms; glucose becomes gluconic acid
**Section 8.7**

- A drop of iodine solution turns deep blue-violet on a slice of potato. Which polysaccharide causes this color, and why? **Answer:** Amylose, because its coiled chain traps iodine inside the helix
- Glycogen has α(1→6) branch points about every 8–12 glucose units, more often than amylopectin. How does the extra branching help an animal? **Answer:** A branched molecule has many chain ends, so enzymes can release glucose from many places at once
- Cotton is about 95% cellulose. It is strong and does not dissolve in water, even though every glucose unit has several –OH groups. What explains this? **Answer:** The straight β(1→4) chains lie side by side and hydrogen bond to each other, forming tightly packed fibers
- Which statement about plant starch is correct? **Answer:** It is a mixture of amylose (unbranched) and amylopectin (branched), with more amylopectin
- A cow gets glucose from the cellulose in grass, but a person cannot. What is the reason? **Answer:** Microorganisms in the cow's digestive tract make cellulase, which hydrolyzes β(1→4) links
**Section 10.1**

- Glycine is the only one of the 20 common amino acids that is not chiral. What is the reason? **Answer:** Its side chain is an H atom, so the α-carbon is bonded to two identical H atoms
- The side chain of glutamine is –CH 2 CH 2 –CONH 2 . How is glutamine classified at pH 7.4? **Answer:** polar neutral
- Which pair of amino acids has side chains that carry a negative charge at pH 7.4? **Answer:** aspartate and glutamate
- Ten of the 20 amino acids are called essential . What does this term mean? **Answer:** The body cannot make them, so they must come from food
- Methionine has the side chain –CH 2 CH 2 –S–CH 3 and cysteine has –CH 2 –SH. How are the two side chains classified? **Answer:** Methionine is nonpolar; cysteine is polar neutral
**Section 13.3**

- Starch digestion starts in the mouth but pauses while food is in the stomach. Why? **Answer:** Stomach acid denatures salivary amylase, so the enzyme stops working
- Stage I of catabolism (digestion) breaks each food into its building blocks. Which pairing is correct? **Answer:** proteins → amino acids
- A bite of bread is swallowed and digested. In what order does its starch meet the carbohydrate-digesting enzymes? **Answer:** salivary amylase (mouth) → pancreatic amylase (small intestine) → maltase (brush border)
- How much ATP does the body capture when starch is hydrolyzed to glucose during digestion (Stage I)? **Answer:** None; the small amount of energy released by hydrolysis is lost as heat
- After sucrase, lactase and maltase finish their work, what happens to the glucose, fructose and galactose? **Answer:** They are absorbed through the wall of the small intestine into the blood and go to the liver first
**Section 15.3**

- Activating one palmitic acid (16 carbons) to palmitoyl CoA costs the equivalent of 2 ATP. What does it cost to activate one stearic acid (18 carbons)? **Answer:** 2 ATP, because activation is done once per fatty acid whatever its length
- In fatty acid activation, R–COO − reacts with CoA–SH to give fatty acyl CoA, R–CO–S–CoA. Which functional group joins the fatty acid to coenzyme A? **Answer:** a thioester
- Why does a long-chain fatty acyl CoA need the carnitine shuttle? **Answer:** Fatty acyl CoA cannot cross the inner mitochondrial membrane to reach the matrix
- Where in the cell do fatty acid activation and β-oxidation take place? **Answer:** Activation at the outer mitochondrial membrane; β-oxidation in the mitochondrial matrix
- Carnitine acyltransferase moves a fatty acyl group from coenzyme A onto carnitine. To which enzyme class does it belong? **Answer:** transferase
**Section 15.9**

- Why does the body convert the nitrogen from amino acids into urea instead of letting ammonia build up? **Answer:** Ammonia is a toxic base, while urea is neutral, relatively nontoxic and very soluble in water
- In a liver cell, where do the reactions of the urea cycle take place? **Answer:** The entry step and step 1 in the mitochondrial matrix; steps 2–4 in the cytosol
- Urea, H 2 N–CO–NH 2 , has one carbon atom. Where does that carbon come from? **Answer:** CO 2 , as bicarbonate (HCO 3 − )
- Making one urea costs the equivalent of 3 ATP. Where is that ATP spent? **Answer:** 2 ATP to make carbamoyl phosphate (entry step) and 1 ATP when citrulline joins aspartate (step 2)
- Patient A has a high blood urea nitrogen (BUN) and normal blood ammonia. Patient B has a normal BUN and high blood ammonia. What do these results mean chemically? **Answer:** A: urea is being made but not excreted. B: NH 4 + is not being converted to urea
