# Lab manual integration backlog

Written 2026-11-14 during the final publication gate. **This is not a list of textbook defects.** The companion CHEM 3B lab manual is still being written; everything below waits for it. Source: every "In the Lab" box and every lab mention in `pages/live/` (live LibreTexts, matched by hash on 2026-11-14).

## How the book refers to the lab today

- 27 "In the Lab" boxes on 27 section pages, in every chapter except 14 (About This Book says Chapter 14 has no lab in the course outline; that is consistent).
- Some boxes cite an experiment number, others name the experiment by topic ("the alcohols and phenols experiment"). The numbers used are 1, 2, 3, 4, 6, 7, 8a, 8b, 9, 11, 12, 13, 14 and "Experiments 1–7". No 5 or 10 is cited by number.
- Whether these numbers are **provisional, agreed or wrong cannot be decided from the book or the repo**: no lab manual draft is in the repo or in `Study Games/`, and the 11-12/11-13 ledgers record "lab experiment numbers wait for the final lab manual". They were not renumbered in this pass.
- For Instructors (597396) said numbers "will be added when the manual is published" while 13 numbers are already printed. Draft fix in batch AH (see `RELEASE_BLOCKERS_AND_FIXES.md`, item F2): the sentence now says the printed numbers are provisional.

## Science and safety check of the boxes (class A/C)

All 27 boxes were read for chemistry and safety on 2026-11-14. No chemically false or unsafe statement was found. Checked in particular: Br2 and KMnO4 tests (3.7), dichromate oxidation colors (4.5), FeCl3 and NaOH tests (4.7, 4.10), Tollens' and iodoform (5.4), ester odors (6.6), aspirin synthesis and FeCl3 purity test (6.7), Benedict's, Seliwanoff's and yeast fermentation (8.5), iodine test (8.7), bromine number and saponification (9.2), ninhydrin, biuret and casein pI 4.6 (10.3), denaturing agents (10.10), amylase activity (11.3), vitamin C iodometric titration (11.5), DNA extraction (12.3), digestion tests (13.3), urine glucose threshold about 180 mg/dL (13.9), nitroprusside ketone pad not detecting β-hydroxybutyrate (15.5), urine protein (15.7).

One note for the manual, not the book: 5.2 says students "meet" formaldehyde, acetone and benzaldehyde "by smell". The manual should state the wafting technique and ventilation for formaldehyde (a carcinogen). The textbook sentence does not instruct a procedure, so it was left alone.

## Class B: provisional cross-references (check when the manual is final)

| # | Section (page id) | What the book says now | Verify later |
|---|---|---|---|
| 1 | 1.5 (597058) | "Model kits (Experiments 1–7)"; kit colors black C, white H, red O, blue N, green Cl, orange Br, purple I | Experiment range; kit color scheme matches the kits the department buys |
| 2 | 1.5 (597058) | Was: "The lab manual appendix has a VSEPR chart … and an electronegativity chart". Draft fix (batch AH, F1): points to the VSEPR table on the same page and Figure 1.4.3 | When the manual has the appendix, optionally add the pointer back |
| 3 | 2.1 (597065) | "Experiment 2 – Properties of Alkanes" | Number and title |
| 4 | 2.4 (597068) | "Experiment 1 – Structures of Alkanes" | Number and title |
| 5 | 3.7 (597084) | "Experiment 3 – Reactions of Hydrocarbons" | Number, title; whether benzene itself is used (most teaching labs substitute toluene or omit it) |
| 6 | 4.3, 4.5, 4.7 (597092, 597094, 597096) | "the alcohols and phenols experiment" (no number) | Number; 5% NaOH concentration; chromate reagent name |
| 7 | 4.10 (597099) | "Experiment 4" (the same alcohols and phenols experiment) | Consistent with item 6 |
| 8 | 5.2, 5.4 (597103, 597105) | "the aldehydes and ketones experiment"; Tollens' and iodoform tests; odors of formaldehyde, acetone, benzaldehyde | Number (5?); which tests the manual keeps; smell technique (see note above) |
| 9 | 6.4, 6.6, 6.7, 6.8 (597112, 597114, 597115, 597116) | "the carboxylic acids and esters experiment"; esters pentyl acetate, octyl acetate, isobutyl formate; aspirin synthesis and TLC of analgesics | Number; ester list; whether aspirin/TLC is in the same experiment |
| 10 | 6.11 Chapter Guide (597119) | "You will make this ester [pentyl acetate] in Experiment 6" | Number 6 and that ester |
| 11 | 6.8 (597116) | "in Chapter 9's lipids experiment you saponify a fat" | Matches item 14 |
| 12 | 7.3 (597123) | "Experiment 7 – Amines and Amides" | Number and title (note 1.5 says kits are used in Experiments 1–7) |
| 13 | 7.7 (597127) | Amide hydrolysis with NaOH, ammonia detected by red litmus (no experiment named) | Whether the amide hydrolysis is part of Experiment 7 |
| 14 | 8.5, 8.7 (597138, 597140) | "Experiment 8a – Types of Carbohydrates and 8b – Tests for Carbohydrates" | Numbering scheme with a/b parts |
| 15 | 9.2 (597145) | "Experiment 9 – Lipids" incl. hand lotion (stearic acid, cetyl alcohol, glycerol, triethanolamine) | Number; lotion recipe still in the manual |
| 16 | 10.3 (597156) | "Experiment 11 – Amino Acids" (paper chromatography, ninhydrin, Rf) and "Experiment 12 – Peptides and Proteins (part 1)" (casein, biuret, ninhydrin); Valley box also says "in Experiment 12 you add acid to milk until pH 4.6" | Numbers 11 and 12 (no Experiment 10 is cited anywhere) |
| 17 | 10.10 (597163) | "Experiment 12 – Peptides and Proteins (part 2)": denaturation with heat, acid, base, ethanol, tannic acid, heavy-metal ions | Agent list |
| 18 | 10.5 (597158) | Denaturation table row: tannic acid "is what the lab (Experiment 12) uses" (in batch AG review note only; check the live row text) | Consistent with item 17 |
| 19 | 11.3 (597168) | "In Experiment 13 you will test … enzyme concentration, temperature and pH, plus an inhibitor"; "Experiment 13 – Enzymes" (amylase, iodine, Benedict's) | Number; inhibitor used |
| 20 | 11.5 (597170) and 11.8 Chapter Guide (597173) | "Experiment 14 – Vitamins" (iodine titration of vitamin C); figure caption "Vitamin C reduces iodine (Experiment 14)" | Number; the figure caption also carries the number |
| 21 | 12.3 (597177) | "the DNA extraction lab" (strawberry, cheek or onion; meat tenderizer or pineapple juice) | Whether the manual includes it and which source tissue |
| 22 | 13.3 (597191) | Digestion of foods (salivary amylase or pancreatin; iodine and Benedict's) | Experiment name/number |
| 23 | 13.9, 15.5, 15.7 (597195, 597213, 597215) | "the metabolism experiment" with simulated urine (glucose, ketones, protein) | Experiment number; test-strip brand chemistry (glucose oxidase, nitroprusside) |
| 24 | About This Book (597270) | Was: "together with the free lab manual … qualify as zero-textbook-cost sections". Draft fix (batch AH, F3): "a free lab manual" | Restore "the free lab manual" once it is published free |
| 25 | About This Book (597270), Course Outline Alignment (597272) | "the laboratory itself is covered by the CHEM 3B lab manual"; "The outline's laboratory topics are taught in the CHEM 3B lab manual" | True of the course today (it has a lab manual); add the link when the new manual is published |
| 26 | For Instructors (597396) | Lab manual "in preparation"; numbers provisional (after F2) | Replace with the link and remove "provisional" |

## Crosswalk to do when the manual is final

1. Make a table: manual experiment number and title → book sections whose In the Lab box should point to it.
2. Replace every provisional number above in one batch (the In the Lab boxes, the 6.11 worked example, the 11.5 figure caption, the 11.8 guide pointer, the 10.3 Valley box).
3. Decide whether boxes that name an experiment by topic only (4.3, 4.5, 4.7, 5.2, 6.4–6.8, 13.3, 13.9, 15.5, 15.7) should gain numbers.
4. Add links from each box to the manual's page, if it is on LibreTexts.
5. Update For Instructors, About This Book (ZTC sentence) and Course Outline Alignment (outline item 15.10 Laboratory).
6. Recompile the PDF and check that the In the Lab boxes still print on the same page as their section.
