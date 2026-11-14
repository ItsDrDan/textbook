# Batch AH review (draft, not published)

Built 2026-11-14 by `tools/batchAH_build.py` from `pages/live/` (which matched all 199 live pages by SHA-256 on 2026-11-14). Approve all, or name rows to drop or reword. The matching bank change (fb-3B-2030) is in `bank/metabolism.json`; the live ADAPT question still needs updating.

## Part A. Lab-manual promises (neutral wording; experiment numbers untouched)

**F1. 1.5 In the Lab: "The lab manual appendix has a VSEPR chart ... and an electronegativity chart"** (1.5, page 597058)

Why: The new lab manual is not published, so students cannot find that appendix. Both charts already exist in the book: the VSEPR table earlier on this page and the Pauling electronegativity figure in 1.4. When the manual is out, the appendix pointer can be added back (LAB_MANUAL_INTEGRATION_BACKLOG.md, row 2).

- Before: The lab manual appendix has a VSEPR chart for organic geometries and an electronegativity chart you can use with this chapter.
- After: For a VSEPR chart of organic geometries, use the table “Electron groups, molecular shapes and bond angles” above; electronegativity values are in Figure 1.4.3.

**F2. For Instructors: "experiment numbers and links will be added when the manual is published"** (For Instructors, page 597396)

Why: Thirteen In the Lab boxes already print experiment numbers (1, 2, 3, 4, 6, 7, 8a, 8b, 9, 11, 12, 13, 14), so the sentence contradicted the book. The numbers themselves are not changed; whether they are final is unknown until the manual is done.

- Before: experiment numbers and links will be added when the manual is published.
- After: where a box already gives an experiment number, that number is provisional; numbers and links will be checked and added when the manual is published.

**F4. For Instructors: "60-80 original problems per chapter"** (For Instructors, page 597396)

Why: Counted on 2026-11-14: Chapter 14 has 67, Chapters 8 and 10 have 81, Chapter 2 has 83 (plus 6 cumulative problems in Chapters 2-15).

- Before: pages hold 60–80 original problems per chapter
- After: pages hold 67–83 original problems per chapter

**F3. About This Book, zero-textbook-cost sentence: "the free lab manual"** (About This Book, page 597270)

Why: "The free lab manual" reads as if a specific free manual is already available; the one written for this book is in preparation (For Instructors). "A free lab manual" keeps the ZTC condition true either way. Restore "the" when the manual is published.

- Before: together with the free lab manual and the free study tools, qualify
- After: together with a free lab manual and the free study tools, qualify

## Part B. Verified science and wording fixes (P2)

**B1. 4.2 Figure alt text, thymol: methyl "two carbons further around the ring"** (4.2, page 597091)

Why: Read the usual way (OH on C1, isopropyl on C2, two carbons further = C4) this describes 2-isopropyl-4-methylphenol, not thymol. In thymol the CH3 (C5) is para to the isopropyl (C2). Screen-reader users get the wrong structure; the visible figure is correct.

- Before: and a CH3 group two carbons further around the ring."
- After: and a CH3 group on the ring carbon directly across from the isopropyl group (2-isopropyl-5-methylphenol)."

**B2. 9.2 Lecture Connection: olestra "all eight OH groups esterified"** (9.2, page 597145)

Why: Commercial olestra is a mixture of sucrose hexa-, hepta- and octaesters (FDA food-additive listing, 21 CFR 172.867).

- Before: is sucrose with all eight OH groups esterified to fatty acids
- After: is sucrose with six to eight of its eight OH groups esterified to fatty acids

**B3. 8.7 Dental Hygiene box: amylase gives "maltose and glucose"** (8.7, page 597140)

Why: Alpha-amylase gives mainly maltose, maltotriose and short dextrins, very little free glucose (glucose comes from brush-border enzymes, as 13.3 says).

- Before: hydrolyzes starch that sticks to teeth into maltose and glucose that plaque bacteria can ferment
- After: hydrolyzes starch that sticks to teeth into maltose and other small sugars that plaque bacteria can ferment

**B4. 3.9 Chapter Guide summary: "Nothing in this chapter dissolves in water"** (3.9 Chapter Guide, page 597086)

Why: Section 3.8 includes phenol, aniline and benzoic acid; phenol dissolves to about 8 g per 100 mL. The paragraph is about hydrocarbons, and now says so.

- Before: Nothing in this chapter dissolves in water.
- After: None of this chapter’s hydrocarbons dissolves in water.

**B5. 1.10 Problem 1.71(c) answer: open chain "would need an O-H"** (1.10 Practice Problems, page 597063)

Why: An open four-carbon chain with O on one end needs two more H (CH3CH2CH2CH2OH, C4H10O), not one. The conclusion (draw the ring) is unchanged. The text appears twice (inline answer and print answer key); both change.

- Before: which would need an O–H to be a real molecule.
- After: which would need an O–H and an extra H on the end carbon to be a real molecule (that would be C4H10O, not C4H8O).

**B6. 15.8 Lecture Connection: after transamination the amino acid "contains only C, H, and O"** (15.8, page 597208)

Why: False for amino acids with N or S in the side chain (Lys, Arg, His, Trp, Asn, Gln, Cys, Met). What transamination removes is the alpha-amino group.

- Before: After transamination the original amino acid contains only C, H, and O.
- After: After transamination the original amino acid has lost its α-amino group and is now an α-keto acid.

**B7. 15.11 table, tyrosine row: phenylalanine hydroxylase "uses O2 and NADPH"** (15.11, page 597217)

Why: The enzyme's reducing cofactor is tetrahydrobiopterin (BH4); NAD(P)H only regenerates BH4 afterward. Dropping "and NADPH" matches the section text above the table ("using O2 to add an -OH group").

- Before: phenylalanine hydroxylase that uses O2 and NADPH to add an OH to the ring
- After: phenylalanine hydroxylase that uses O2 to add an OH to the ring

## Part C. Citrate synthase is a transferase (author decided 2026-11-14 to switch from ligase)

**C1. 11.1 six-class table, lyase row: "citrate synthase is the course exception, a ligase"** (11.1, page 597166)

Why: IUBMB classifies citrate synthase as a transferase (EC 2.3.3.1; before 2002 a lyase, EC 4.1.3.7), never a ligase, and the book's own rule says a ligase spends ATP; citrate synthase spends none. The author chose to switch the course to transferase (2026-11-14), which also matches Metabolic Marathon ("Dr. Dan: citrate synthase = transferase") and the Study Hub question bank, which already key Transferase.

- Before: also aldolase and most synthases (no ATP; citrate synthase is the course exception, a ligase)
- After: also aldolase and most synthases (no ATP; citrate synthase is the exception, a transferase)

**C2. 11.1 "Two traps": citrate synthase "is classified as a ligase"** (11.1, page 597166)

Why: IUBMB classifies citrate synthase as a transferase (EC 2.3.3.1; before 2002 a lyase, EC 4.1.3.7), never a ligase, and the book's own rule says a ligase spends ATP; citrate synthase spends none. The author chose to switch the course to transferase (2026-11-14), which also matches Metabolic Marathon ("Dr. Dan: citrate synthase = transferase") and the Study Hub question bank, which already key Transferase.

- Before: The one exception in this course is citrate synthase (Chapter 14): it is classified as a ligase.
- After: The one exception you will meet is citrate synthase (Chapter 14): it is a transferase. It moves the acetyl group from acetyl CoA onto oxaloacetate (CoA–SH leaves), and it spends no ATP, so it is not a ligase.

**C3. 11.8 Key Idea 2: ligase list "plus citrate synthase, the course exception"** (11.8 Chapter Guide, page 597173)

Why: IUBMB classifies citrate synthase as a transferase (EC 2.3.3.1; before 2002 a lyase, EC 4.1.3.7), never a ligase, and the book's own rule says a ligase spends ATP; citrate synthase spends none. The author chose to switch the course to transferase (2026-11-14), which also matches Metabolic Marathon ("Dr. Dan: citrate synthase = transferase") and the Study Hub question bank, which already key Transferase.

- Before: ligase (ATP is spent and two molecules become one; synthetase, carboxylase; plus citrate synthase, the course exception).
- After: ligase (ATP is spent and two molecules become one; synthetase, carboxylase). Citrate synthase is the one synthase that is not a lyase: it is a transferase that moves an acetyl group onto oxaloacetate.

**C4. 11.8 Common Mistakes: citrate synthase "is classified as a ligase"** (11.8 Chapter Guide, page 597173)

Why: IUBMB classifies citrate synthase as a transferase (EC 2.3.3.1; before 2002 a lyase, EC 4.1.3.7), never a ligase, and the book's own rule says a ligase spends ATP; citrate synthase spends none. The author chose to switch the course to transferase (2026-11-14), which also matches Metabolic Marathon ("Dr. Dan: citrate synthase = transferase") and the Study Hub question bank, which already key Transferase.

- Before: the one exception in this course is citrate synthase (Chapter 14), which is classified as a ligase.
- After: the one exception is citrate synthase (Chapter 14), a transferase: it moves the acetyl group of acetyl CoA onto oxaloacetate and spends no ATP.

**C5. 14.3 step table, step 1 enzyme class: "ligase in this course"** (14.3, page 597202)

Why: IUBMB classifies citrate synthase as a transferase (EC 2.3.3.1; before 2002 a lyase, EC 4.1.3.7), never a ligase, and the book's own rule says a ligase spends ATP; citrate synthase spends none. The author chose to switch the course to transferase (2026-11-14), which also matches Metabolic Marathon ("Dr. Dan: citrate synthase = transferase") and the Study Hub question bank, which already key Transferase.

- Before: citrate synthase (ligase in this course: it joins two molecules)
- After: citrate synthase (transferase: it moves the acetyl group from CoA onto oxaloacetate; no ATP is spent, so it is not a ligase)

**C6. 14.6 Chapter Guide, Key Idea: "Citrate synthase is treated as a ligase"** (14.6 Chapter Guide, page 597205)

Why: IUBMB classifies citrate synthase as a transferase (EC 2.3.3.1; before 2002 a lyase, EC 4.1.3.7), never a ligase, and the book's own rule says a ligase spends ATP; citrate synthase spends none. The author chose to switch the course to transferase (2026-11-14), which also matches Metabolic Marathon ("Dr. Dan: citrate synthase = transferase") and the Study Hub question bank, which already key Transferase.

- Before: Citrate synthase is treated as a ligase, aconitase and fumarase are lyases,
- After: Citrate synthase is a transferase (no ATP, so not a ligase), aconitase and fumarase are lyases,

**C7. Glossary "ligase": "this course also treats citrate synthase ... as a ligase"** (Glossary, page 488232)

Why: IUBMB classifies citrate synthase as a transferase (EC 2.3.3.1; before 2002 a lyase, EC 4.1.3.7), never a ligase, and the book's own rule says a ligase spends ATP; citrate synthase spends none. The author chose to switch the course to transferase (2026-11-14), which also matches Metabolic Marathon ("Dr. Dan: citrate synthase = transferase") and the Study Hub question bank, which already key Transferase.

- Before: such as DNA ligase (this course also treats citrate synthase, which joins acetyl CoA and oxaloacetate, as a ligase).
- After: such as DNA ligase.

**C8. Glossary "transferase": add citrate synthase as an example** (Glossary, page 488232)

Why: IUBMB classifies citrate synthase as a transferase (EC 2.3.3.1; before 2002 a lyase, EC 4.1.3.7), never a ligase, and the book's own rule says a ligase spends ATP; citrate synthase spends none. The author chose to switch the course to transferase (2026-11-14), which also matches Metabolic Marathon ("Dr. Dan: citrate synthase = transferase") and the Study Hub question bank, which already key Transferase.

- Before: such as kinases, aminotransferases and thiolase.
- After: such as kinases, aminotransferases, thiolase and citrate synthase (which moves an acetyl group onto oxaloacetate).

## Part D. Version note

**D1. About This Book: last-updated date** (About This Book, page 597270)

Why: Batches AG and AH were published on 2026-11-14.

- Before: (last updated November 13, 2026)
- After: (last updated November 14, 2026)

**D2. About This Book: version history line for 2026-11-14** (About This Book, page 597270)

Why: Records what changed in this update.

- Before: 1.2 (November 13, 2026).
- After: Update (November 14, 2026). Final pre-release check: citrate synthase is now classified as a transferase (Sections 11.1, 11.8, 14.3, 14.6 and the Glossary); references to the lab manual, which is still in preparation, were reworded; small corrections in 1.10, 3.9, 4.2, 8.7, 9.2, 15.8 and 15.11. 1.2 (November 13, 2026).

## Publish method (after approval)

Same as batches M-AG: push the branch, have the signed-in LibreTexts tab fetch `tools/batchAH_2026-11-14.json` at that commit, dry-run against live using the `before` hashes in `tools/batchAH_sha_2026-11-14.json`, save, read back, sync `pages/live`. Update the About This Book "last updated" date and add a version-history line in the same step.
