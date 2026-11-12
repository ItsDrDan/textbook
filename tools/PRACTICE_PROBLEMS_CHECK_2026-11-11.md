# CHEM 3B Practice Problems answer check (2026-11-11)

All 15 Practice Problems pages were checked: 1,231 questions (1,123 numbered problems, 84 Cumulative Problems and 24 Case Set questions).
- Every problem was solved independently and compared with the book's answer and explanation, against `tools/CONVENTIONS.md` and the GOB scope.
- Every flag below was then rechecked in the live page source.
- Each page's inline answers and its answer key were also compared mechanically. They agree on every problem.

**No answer key is wrong.** Every answer letter and every computed value is correct. All findings are in explanations, option wording, tables or alt text.

Ruled out as false alarms:
- 5.49 and 8.21: "2ⁿ" is correctly superscripted on the page.
- The case-scenario text looked garbled, but that came from the text extraction; the pages are fine.

## Higher priority: the explanation states something wrong or contradicts a course convention

| # | Problem | Page | Problem in the text | Proposed fix |
|---|---|---|---|---|
| 1 | 10.64 (a), (c) | 597165 | Says Asp/Glu side chains are charged because of "their pI values are about 3", and "below the pI". The convention is to compare pH with the side-chain pKa; pI applies only to the whole free amino acid. | Use the side-chain pKa: about 3.9 (Asp) and 4.1 (Glu). |
| 2 | Cumulative 11.3 (c) | 597174 | "heavy-metal ions … are treated in this course as irreversible inhibitors" implies they are not noncompetitive. | "…they act away from the active site; in this course they count as both noncompetitive and irreversible inhibitors." |
| 3 | Case Set 11.1, option A | 597174 | Calls vitamin C "a cofactor". The convention says a cofactor is an inorganic ion, and 11.61 says the cofactor is Fe²⁺. | "…needed by the enzyme that hydroxylates proline in collagen (it keeps the enzyme's Fe²⁺ cofactor reduced)." |
| 4 | 13.52, 14.53 | 597199, 597206 | Calls thiamine "a required cofactor" and "a cofactor made from thiamine". | "coenzyme" (thiamine pyrophosphate). |
| 5 | Cumulative 15.6 (a) | 597219 | Says glucagon makes the liver "hydrolyze glycogen's α-glycosidic bonds". 13.58 correctly says phosphate is the reagent, not water. | "…break glycogen's α-glycosidic bonds by phosphorolysis (glycogen phosphorylase, using Pi), giving glucose-1-phosphate…" |
| 6 | 13.47 (c) | 597199 | "the product that pyruvate becomes in Stage 3". The book puts pyruvate → acetyl CoA in Stage 2. | "Acetyl CoA, made from pyruvate at the end of Stage 2, is the fuel for Stage 3…" |
| 7 | 2.64; 2.60 | 597075 | 2.64 says "two conformations". 2.60's keyed option B and its reasoning say "chair". Conformers are out of scope. | 2.64: "the same molecule drawn at two moments of free rotation about a single bond". 2.60: "It is puckered (not flat), so every bond angle is close to 109.5°". |
| 8 | 6.65 (e) | 597120 | Calls 2- vs 3-methylbutanoic acid skeletal isomers because "the methyl branch … changes the carbon skeleton". Both share the same 2-methylbutane skeleton. | Call them positional isomers: same skeleton, with the branch at a different place along the acid chain. |
| 9 | 1.57 (d) | 597063 | Says the lone pairs on "both nitrogens" can accept hydrogen bonds. The amide N's lone pair is shared with the C=O, as 1.76 itself says. | The amide N–H donates; the C=O oxygen and the amine nitrogen accept. |
| 10 | 8.59 | 597142 | "no human enzyme hydrolyzes the β(1→4) link". Lactase does, in lactose (8.44, 8.47). | "…the β(1→4) link between glucose units". |
| 11 | 8.33 | 597142 | Answer "D-galactitol". Galactitol is achiral, so it has no D/L form. | "galactitol (dulcitol)", the same way 8.34 writes "ribitol". |
| 12 | Cumulative 14.4 (c) vs 14.52 | 597206 | 14.4 calls cyanide's block "essentially irreversible", but 14.52 says the antidote frees Complex IV. | Call cyanide a tight-binding but reversible inhibitor that antidotes can remove. |
| 13 | Cumulative 15.5 (b) | 597219 | "releases both acetyl carbons as CO₂". The two CO₂ released in that turn are not the incoming acetyl carbons; only the number matches, as 14.16 says. | "…releases two carbons as CO₂, as many as acetyl CoA brought in, so there is no net gain of oxaloacetate." |

## Lower priority: imprecise, ambiguous, or a table or alt-text error

| # | Problem | Page | Problem in the text | Proposed fix |
|---|---|---|---|---|
| 14 | 1.64 (a) | 597063 | Says the double bond "puts a rigid bend" in the chain, but only a cis double bond does. The question never says oleic acid is cis. | Say that oleic acid's C=C is cis and that the cis arrangement makes the bend. |
| 15 | 7.59 (c) | 597133 | Nylon-6,6 "amide links are separated by runs of six carbons". That is six CH₂ on the diamine side but four on the diacid side. | "runs of six and four CH₂ groups". |
| 16 | 13.58 | 597199 | "Coenzyme/nucleotide: none (Pi is the reagent)". Glycogen phosphorylase carries PLP (from vitamin B₆). | "No nucleotide; Pi is the reagent (the enzyme carries PLP, from B₆, as a bound coenzyme)." |
| 17 | 14.49 (b) | 597206 | "X must act at or after CoQ". With succinate as the fuel, a Complex II blocker would also fit. | "…at Complex II or downstream, but not at Complex I". The answer "No" is unchanged. |
| 18 | Cumulative 4.4 | 597101 | An OH "carries about four or five carbons into water". The convention says alcohols ≤4 C. | "about four carbons". |
| 19 | 2.82, 2.78, 3.75 (a) | 597075, 597087 | "four-corner zigzag" for a four-carbon chain. By 1.52's rule (every corner and every end is a carbon), that zigzag has two corners and two ends. | "a four-carbon zigzag … off the second carbon", and so on. |
| 20 | 1.56 (c) | 597063 | Asks about isopropyl alcohol "based on this table alone", but the table lists propan-1-ol, not isopropyl alcohol. | Compare with propan-1-ol, or add isopropyl alcohol (bp 82 °C) to the table. |
| 21 | 4.54 | 597101 | The table caption says "four unknowns", but there are three (P, Q, R). Q is phenol, which is a solid, yet the stem calls all three "liquids". | "three unknowns"; "unknowns" instead of "unknown liquids". |
| 22 | 3.71 | 597087 | The alt text gives "a chain of eight carbons" plus two methyls on one end and one on the other, which reads as 11 C. Geraniol has 10. | "an eight-carbon chain with methyl branches on C3 and C7, C=C at C2–C3 and C6–C7, ending in CH₂OH". |
| 23 | 11.60 (a) | 597174 | "an ester, Chapter 7". Esters are in Chapter 6; acetylcholine appears in 7.11. | "an ester (Chapter 6; see also Section 7.11)". |
| 24 | 5.56 (b) | 597108 | "the alcohol is somewhat more soluble". The measured values are nearly equal (about 4.5 vs 4.3 g/100 mL). | Optional: "about equally soluble, the alcohol slightly more so". |
