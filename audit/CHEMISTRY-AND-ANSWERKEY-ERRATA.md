# Chemistry and answer-key errata (master refinement pass, 2026-11-13)

Scope of this file: errors and gaps found **in this pass**. Everything found before it is in `tools/ISSUE_LEDGER.md` and
`tools/REVIEW_2026-11-13.md` and is not repeated. Status words: *drafted* = in `tools/batchQ_2026-11-13.json`, not live;
*fixed locally* = changed in this repo branch, not deployed.

## What was and was not re-checked

- **Not re-solved in this pass:** the 1,231 Practice Problems and the Chapter Guide exercises. They were re-solved in full on 2026-11-11 and again on 2026-11-13 (no wrong key either time). Re-solving them a third time the same day would not be independent evidence.
- **Checked by script in this pass:** answer presence and print-key parity for all 1,812 examples and exercises (`audit/QUESTION-LEDGER.csv`); every ATP tally met by the Chapter 13–15 reviewer (recomputed against 2.5 / 1.5 / 10 / 30–32 / 106, all agree).
- **Solved by hand in this pass:** the 24 inherited exercises below, which had no answer.
- **Changelog items the prompt asked about**, confirmed in the 2026-11-13 16:37 PDF text: transcription directions (12.4), tyrosine from phenylalanine as an oxidation (15.11), ATP yields, ten essential amino acids. No pKa, R/S, E/Z, meso, Henderson–Hasselbalch or Newman content (keyword scan of all 199 pages).

## P0 (stop-ship)

None found.

## P1

| # | Section (page id) | PDF p. | Problem | Correct chemistry / fix | Status |
|---|---|---|---|---|---|
| E1 | 4.2, 4.4, 4.5, 4.8, 5.1, 6.1, 6.4, 6.5, 6.8, 7.1, 7.3, 7.7 (12 pages) | see ledger | **24 inherited exercises have no answer anywhere**, on screen or in print. Earlier checks counted only the house-style boxes; these use the source book's `<section class="box-exercise">` markup. | Answers written and worked by hand (list below), added inline and to the print key. | drafted |
| E2 | 9.6 (597149) | 738–746 | "Excess cholesterol … transported by the blood to the gallbladder." | The liver secretes cholesterol into bile, which reaches the gallbladder through the bile ducts (the page's own Bile Salts section says so). | drafted |
| E3 | 5.4 (597105) Summary | 408–418 | "ketones give no reaction" with Tollens'/Benedict's; the same page's table and 5.6 mark α-hydroxy ketones (fructose) positive. | "simple ketones give no reaction (an α-hydroxy ketone such as fructose is the exception)". | drafted |
| E4 | 13.4 (597192) Nursing box | 1057–1064 | "Thiamine is the cofactor of pyruvate dehydrogenase" (missed by the batch M cofactor fix). | Convention 11.5: TPP is a coenzyme. | drafted |
| E5 | 10.2 (597155) | 788–792 | The rule "pH above pI → net −1 for a neutral R group" applied to alanine (pI 6.0) at pH 7.4 contradicts "zwitterion, net 0 at pH 7.4" on the same page. | One sentence: use the charged forms when the pH is far from the pI; at 7.4 a neutral-R amino acid is still drawn as the zwitterion. | drafted |
| E6 | 2.5 (597069) Example 1(c) | 162–169 | Solution credits the numbering to "rule 3"; the page's rule 2 is numbering and rule 3 is alphabetical order, which is never used to explain ethyl-before-methyl. | Rule numbers corrected and the alphabetical step stated. | drafted |
| E7 | 4.11 (597100) Common Mistakes | 354–364 | Reads as "do not count neighbor hydrogens" although 4.5 teaches Zaitsev by exactly that count. | Reworded so both tests agree. | drafted |
| E8 | 1.8 (597061) Example 4(b) | 96–114 | Solution says it is "difficult to know for certain" whether ethanol is a solid. | Reasoned answer: liquid, with the boiling point as the check. | drafted |

## P1 (low) and P2 factual wording

| # | Section (page id) | Problem | Fix | Status |
|---|---|---|---|---|
| E9 | 10.6 (597159) | 20ⁿ described as the number of "constitutional isomers" of a peptide. | It counts sequences; most differ in formula. | drafted |
| E10 | 6.8 (597116) | "catalyzed by either an acid or a base"; the same page says the base is a reactant. | Acid is a catalyst, base is used up. | drafted |
| E11 | 15.7 (597215) Example 1 Check | "more urea, more negative" nitrogen balance: wrong in general. | Negative only when N out exceeds N in. | drafted |
| E12 | 15.10 (597210) | Glucogenic defined as "pyruvate or oxaloacetate" only. | "or a citric acid cycle intermediate", as the page's own table has it. | drafted |
| E13 | 14.3 (597202) | "ten energetic molecules" beside the convention's "10 ATP per acetyl CoA". | States 6 NADH, 2 FADH₂, 2 ATP, worth 20 ATP per glucose. | drafted |
| E14 | 13.9 (597195) | "every counter-regulatory hormone is catabolic", yet they switch on gluconeogenesis (anabolic, 13.1). | Reworded. | drafted |
| E15 | 4.9 (597098) Valley box | "the garlic smell [is] the –SH group at work": garlic and onion odors are mostly sulfides and disulfides. | Sentence replaced by the boiling-point argument. | drafted |
| E16 | About This Book (597270), PDF p. 15 | "This is version 1.1." | 1.2 | drafted |

**Not drafted (low confidence, need a source or a decision):** 14.3 oxidation rule omits glycolysis step 6, and step 5 is "phosphate substitutes" in the text but "hydrolysis" in the table; 14.4 "1.14 volts = −218 kJ/mol" (computes to about −220); 7.4 Example 1 Check says N-ethyl-N-methylbenzamide "is a liquid" (unverified); 9.5 "about 7 nm thick" against the 9.3 figure; 10.5 "alkaloid reagents, such as tannic acid".

## E1 detail: answers written for the 24 exercises

Each was solved from the page text and the figure description (alt text); images were not viewed, so a figure whose alt text is wrong would carry the error through. A chemistry colleague should read these 24 before or after publishing.

| Exercise | Answer |
|---|---|
| 4.2.1 | (a) 1,2-propanediol; (b) 1-methylcyclopentanol |
| 4.2.2 | (a) CH₃CH₂CH(OH)CH₂CH₂CH₂CH₃; (b) CH₃CH(CH₃)CH(OH)CH₂CH₂CH₃ |
| 4.4.1 | cyclopentene + H₂O → cyclopentanol (H₃PO₄ over the arrow) |
| 4.5.1 | (a) 3-methyl-3-hexanol, 3°: no reaction; (b) 2-methyl-1-propanol → 2-methylpropanal → 2-methylpropanoic acid; (c) 3-methyl-2-hexanol → 3-methyl-2-hexanone |
| 4.8.1 | (a) dibutyl ether; (b) cyclobutyl ethyl ether |
| 5.1.1 | (a) ketone, ethyl propyl ketone; (b) aldehyde; (c) ketone, cyclobutyl methyl ketone |
| 5.1.2 | (a) 3,3-dimethylbutanal; (b) 2-methyl-3-hexanone; (c) cyclobutanone |
| 5.1.3 | (a) CH₃CH₂CHBrCH₂CHICH₂CHO; (b) CH₃COCH₂CH(CH₂CH₃)CHBrCH₂CH₃ |
| 6.1.1 | (a) 5-chloropentanoic acid; (b) 2-bromo-4-methylpentanoic acid |
| 6.1.2 | CH₃CH(CH₃)CHBrCH₂CH₂COOH |
| 6.4.1 | (a) HCOOH + H₂O ⇌ HCOO⁻ + H₃O⁺; (b) ClC₆H₄COOH + H₂O ⇌ ClC₆H₄COO⁻ + H₃O⁺ |
| 6.4.2 | (a) C₆H₅COOH + NaOH → C₆H₅COO⁻Na⁺ + H₂O; (b) with NaHCO₃ → C₆H₅COO⁻Na⁺ + H₂O + CO₂ |
| 6.5.1 | (a) ethyl pentanoate / ethyl valerate; (b) propyl propanoate / propyl propionate |
| 6.5.2 | CH₃CH₂CH₂CH₂COO–C₆H₅ |
| 6.8.1 | CH₃CH₂CH₂COOCH₃ + H₂O ⇌ butanoic acid + methanol (H⁺) |
| 6.8.2 | CH₃CH₂COOCH₂CH₃ + NaOH → sodium propanoate + ethanol |
| 7.1.1 | (a) isopropylmethylamine, 2°; (b) diethylmethylamine, 3°; (c) butylamine, 1°; (d) dipropylamine, 2° |
| 7.1.2 | (a) CH₃CH₂NHCH(CH₃)₂, 2°; (b) (CH₃CH₂)₂NCH₂CH₂CH₃, 3° |
| 7.1.3 | o-chloroaniline (2-chloroaniline) |
| 7.1.4 | benzene ring with NH₂ and, para to it, CH(CH₃)₂; 1° |
| 7.1.5 | ClCH₂CH(NH₂)CH(CH₂CH₃)CH₂CH₂CH₂CH₃ |
| 7.1.6 | ethylammonium, triethylammonium, dipropylammonium, tetrabutylammonium ions |
| 7.3.1 | acid HI; base tripropylamine, (CH₃CH₂CH₂)₃N |
| 7.7.1 | (a) propanamide + H₂O → propanoic acid + NH₃; (b) hexanamide + H₂O → hexanoic acid + NH₃ (NH₄⁺ in acid; carboxylate in base) |

Also on 4.2: part (b) of both exercises sat outside the exercise box as a stray bullet; the draft moves each back inside.

## Answer-key structure (all pages)

- 1,812 items: 288 worked examples and 1,524 exercises/problems (1,231 on Practice Problems pages, 228 in Chapter Guides, 353 on section pages).
- Print keys: 108 pages have a print-only key; on every one the number of key entries equals the number of hidden inline answers (1,591 = 1,591; six guides also have one "drawn example" disclosure, which does print).
- After batch Q, no exercise in the book is without an answer. Chapter 1 and 7.4 exercises show their answers in the open (inherited "Answer a:" lines), which is a spoiler-placement issue (P3), not a missing key.
- 211 answers are three words or fewer ("B.", a name, a number). Most are naming or matching items where a bare answer is the answer; they are flagged `bare_answer` in the CSV for a later pass.

**Update 2026-11-14 (batch AG):** the "not drafted" list above is closed. 14.3 step 5 wording, 14.4 (−220 kJ/mol), 9.5 (4 to 5 nm) and 7.4 (no "is a liquid" claim) were already fixed live; the 14.3 NADH rule now includes the aldehyde oxidation of glycolysis step 6, and 10.5 replaces "alkaloid reagents" with "tannic acid and similar polyphenols".
