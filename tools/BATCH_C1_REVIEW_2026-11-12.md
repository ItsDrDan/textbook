# Batch C1: figure numbering (review 2026-11-12)

Lecture Connection and Chapter Guide figures were hard-numbered from 1 again after the source figures (which LibreTexts numbers X.Y.1, X.Y.2 … via `\PageIndex`), so two figures shared a number. The hard-numbered figures now continue after the last source figure; Chapter Guide two-part numbers become three-part. Edit list: `tools/batchC1_fignum_2026-11-12.json` (built by `tools/batchC1_build.py`, replay-checked against `pages/live`).

Special cases: **1.6** the uncaptioned ethyne image becomes Figure 1.6.3 (fills the gap); **5.4** source figures 2–4 become 1–3 (captions and in-text references); **9.1** source figure 2 becomes 9.1.1 (references 2a/2b → 1a/1b). Cross-references updated: 8.3 (two, → 8.3.3) and the 12.1 Professor Tip (→ 12.1.6). Pages 1.7, 9.4, 14.2 and 14.4 were flagged by the scan but only because a paragraph begins "Figure \(\PageIndex{n}\) shows…"; no change there beyond what is listed.

| Section | Page | Renumbered |
|---|---|---|
| 1.6: Introduction to Organic Chemistry | 597059 | 1.6.1 → 1.6.6 |
| 1.7: Representing organic compounds | 597060 | 1.7.1 → 1.7.4, 1.7.2 → 1.7.5 |
| 1.9: Chapter Guide - Bonding Review - Lewis Structures and Intermolecular Forces | 597062 | 1.1 → 1.9.1, 1.2 → 1.9.2, 1.3 → 1.9.3 |
| 2.3: Branched-Chain Alkanes | 597067 | 2.3.1 → 2.3.2, 2.3.2 → 2.3.3, 2.3.3 → 2.3.4 |
| 2.8: Halogenated Hydrocarbons | 597072 | 2.8.1 → 2.8.2 |
| 2.9: Cycloalkanes | 597073 | 2.9.1 → 2.9.2, 2.9.2 → 2.9.3 |
| 2.10: Chapter Guide - Alkanes and Cycloalkanes | 597074 | 2.1 → 2.10.1 |
| 3.2: Cis-Trans Isomers (Geometric Isomers) | 597079 | 3.2.1 → 3.2.5, 3.2.2 → 3.2.6 |
| 3.8: Structure and Nomenclature of Aromatic Compounds | 597085 | 3.8.1 → 3.8.3, 3.8.2 → 3.8.4, 3.8.3 → 3.8.5 |
| 3.9: Chapter Guide - Alkenes, Alkynes, and Aromatic Compounds | 597086 | 3.1 → 3.9.1 |
| 4.2: Alcohols - Nomenclature and Classification | 597091 | 4.2.1 → 4.2.2, 4.2.2 → 4.2.3, 4.2.3 → 4.2.4 |
| 4.5: Reactions of Alcohols | 597094 | 4.5.1 → 4.5.2, 4.5.2 → 4.5.3 |
| 4.7: Phenols | 597096 | 4.7.1 → 4.7.2 |
| 4.11: Chapter Guide - Alcohols, Phenols, Ethers, and Thiols | 597100 | 4.1 → 4.11.1 |
| 5.3: Adding Alcohols to Aldehydes and Ketones- Hemiacetals and Acetals | 597104 | 5.3.1 → 5.3.3, 5.3.2 → 5.3.4, 5.3.3 → 5.3.5, 5.3.4 → 5.3.6 |
| 5.4: Reduction and oxidation (redox) reactions | 597105 | 5.4.1 → 5.4.4, 5.4.2 → 5.4.5, 5.4.3 → 5.4.6 |
| 5.6: Chapter Guide - Aldehydes and Ketones | 597107 | 5.1 → 5.6.1, 5.2 → 5.6.2, 5.3 → 5.6.3 |
| 6.1: Carboxylic Acids - Structures and Names | 597109 | 6.1.1 → 6.1.3, 6.1.2 → 6.1.4 |
| 6.11: Chapter Guide - Carboxylic Acids and Esters | 597119 | 6.1 → 6.11.1 |
| 7.1: Amines - Structures and Names | 597121 | 7.1.1 → 7.1.2, 7.1.2 → 7.1.3, 7.1.3 → 7.1.4 |
| 7.12: Chapter Guide - Amines and Amides | 597132 | 7.1 → 7.12.1, 7.2 → 7.12.2 |
| 8.2: Classes of Monosaccharides | 597135 | 8.2.1 → 8.2.3 |
| 8.3: Important Hexoses | 597136 | 8.3.1 → 8.3.3 |
| 8.4: Cyclic Structures of Monosaccharides | 597137 | 8.4.1 → 8.4.3, 8.4.2 → 8.4.4 |
| 8.5: Properties of Monosaccharides | 597138 | 8.5.1 → 8.5.2, 8.5.2 → 8.5.3 |
| 8.6: Disaccharides | 597139 | 8.6.1 → 8.6.2, 8.6.2 → 8.6.3, 8.6.3 → 8.6.4 |
| 8.7: Polysaccharides | 597140 | 8.7.1 → 8.7.4, 8.7.2 → 8.7.5 |
| 9.1: Fatty Acids | 597144 | 9.1.1 → 9.1.2, 9.1.2 → 9.1.3, 9.1.3 → 9.1.4, 9.1.4 → 9.1.5 |
| 9.6: Steroids | 597149 | 9.6.1 → 9.6.4, 9.6.2 → 9.6.5 |
| 10.4: Peptides | 597157 | 10.4.1 → 10.4.2, 10.4.2 → 10.4.3, 10.4.3 → 10.4.4 |
| 10.5: Proteins | 597158 | 10.5.1 → 10.5.9 |
| 11.1: Enzymes | 597166 | 11.1.1 → 11.1.2, 11.1.2 → 11.1.3 |
| 11.2: Enzyme Action | 597167 | 11.2.1 → 11.2.4, 11.2.2 → 11.2.5 |
| 11.3: Enzyme Activity | 597168 | 11.3.1 → 11.3.3, 11.3.2 → 11.3.4 |
| 11.6: Enzyme Regulation- Allosteric Control and Feedback Inhibition | 597171 | 11.6.1 → 11.6.3 |
| 12.1: Nucleotides | 597175 | 12.1.1 → 12.1.4, 12.1.2 → 12.1.5, 12.1.3 → 12.1.6 |
| 15.8: Removing the Nitrogen - Transamination and Oxidative Deamination | 597208 | 15.8.1 → 15.8.2 |
| 15.4: Oxidation of fatty acids | 597209 | 15.4.1 → 15.4.3, 15.4.2 → 15.4.4 |

Other edits: 597059: 1.6 caption ethyne as Figure 3; 597105: 5.4 source figure 2 -> 1; 597105: 5.4 source figure 2 -> 1; 597105: 5.4 source figure 3 -> 2; 597105: 5.4 source figure 3 -> 2; 597105: 5.4 source figure 4 -> 3; 597105: 5.4 source figure 4 -> 3; 597136: cross-reference follows renumbered figure; 597136: cross-reference follows renumbered figure; 597144: 9.1 source figure 2a -> 1a; 597144: 9.1 source figure 2b -> 1b; 597144: 9.1 source figure 2 -> 1; 597175: cross-reference follows renumbered figure
