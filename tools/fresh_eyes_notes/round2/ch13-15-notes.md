# ch13-15 round 2 (Tier 3 + Tier 4) — notes

- **Edit list:** edits2/ch13-15.json (41 edits, 16 pages). It was drafted against the current pages/live, which already contain the round-1 edits.
- **Builder:** scratchpad/ch1315r2/build.py.
- **Validator:** scratchpad/ch1315r2/validate.py. It checks:
  - every `old` count at the moment it is applied, in sequence;
  - that the net open-minus-close count of p, td, li, div, section, ul, ol, figure and table is the same in `new` as in `old`;
  - that strong, em, sub, sup and a are balanced inside `new`.

  Result: ALL OK.

## Tier 3 (clinical currency)
- **597211 15.5:** rewrote the "Good vs. Bad Cholesterol" box as three short paragraphs.
  - The same molecule is carried by different particles: LDL delivers cholesterol to tissues and plaque; HDL returns it to the liver.
  - Total cholesterol under 200 mg/dL is desirable, and LDL goals are now set from each patient's overall risk.
  - Saturated and trans fats raise LDL, trans fats also lower HDL, unsaturated fats lower LDL, and omega-3s mainly lower triglycerides.
  - Removed the "catalysts" wording, the unnamed "study", and the dead UMMC footnote (with its hr and footnotes div).
- **597195 13.7 (Nursing box):** added that many people with type 2 diabetes take metformin, a GLP-1 receptor agonist or an SGLT2 inhibitor (pointer to 13.4). Also added that SGLT2 inhibitors cause glucose in the urine, so a positive urine glucose is expected in these patients.
- **597213 15.7 (Nursing box):** added SGLT2-associated euglycemic DKA. DKA can occur with near-normal glucose, so check ketones and pH.
- **597192 13.4 complication bullets:** changed to "a leading cause of blindness in working-age adults" and "leading cause of lower-limb amputations not caused by injury".
- **597203 14.4 newborn brown fat:** now says it sits around the neck, between the shoulder blades, and around the kidneys and spine.
- **597209 15.3:** "hibernating animals like polar bears…" became "bears build up fat… live on it for months in their winter dens". The camel claim was cut to "draw on it when food is scarce".
- **597189 13.2 CK box (optional item):** added "extreme exertion, heat stroke (a risk for farmworkers and others who work outdoors in Valley summers)" to the rhabdomyolysis list. No statistics were added.

## Tier 4 (in-page redundancy and scope)
- **597200 14.1**
  - Deleted the re-taught Glycolysis section (both phases) and the β-Oxidation section (Entry, Activation, Oxidation, Hydration, Oxidation, Cleavage). This removes two figures, two NDSU/YouTube video embeds and the β-oxidation SVG images. All of this is taught in 13.5 and 15.3, and 14.1's own Professor Tip already said to skip it.
    - The two embeds that go with it are the "Glycolysis: An Overview" NDSU animation and the "Beta oxidation" Biotech Review link. Both belonged to the deleted duplicate source text, not to the Lecture Connection. If the instructor wants to keep the videos, restore just those embed blocks.
  - Added a one-paragraph pointer to 13.5 and 15.3.
  - Deleted the References list (Garrett & Grisham and Raven, both with a wrong "Twayne" publisher). It only supported the deleted text.
  - Rewrote the Professor Tip so it no longer refers to "the glycolysis steps in this section".
  - The pyruvate → acetyl CoA detail on this page is in the Lecture Connection, so it was kept.
- **597201 14.2**
  - Replaced the eight-step citric acid cycle walkthrough and the Ball cycle figure (Figure 1) with a short overview plus a pointer to 14.3.
  - Replaced the half-reaction-by-half-reaction ETC text (FMN, Fe·S, CoQ, cytochrome a/a3) and the porphyrin figure (Figure 4) with two short paragraphs (complexes, carriers, O2, iron Fe3+/Fe2+) plus a pointer to 14.4.
  - Kept: mitochondrion structure, chemiosmosis, the muscle 30%/90% O2 fact that 14.4 cites, the 10 ATP per acetyl CoA table, Key Takeaways and both NDSU video embeds.
  - Updated the Professor Tip.
  - Figures 2 and 3 now have no Figure 1 or Figure 4 alongside them. \PageIndex numbers are literal, so the main session may want to renumber the captions to 1 and 2 and update the in-text references to match.
- **597192 13.4**
  - Replaced the Ball step-by-step glycolysis prose, its two phase figures and the bis/di box with a two-phase overview. The overview names substrate-level phosphorylation, points to 13.5, and adds a note that the full ATP table's non-glycolysis rows are explained in Chapter 14.
  - Deleted the "In phase II…" emphasis box, which repeated the overview.
  - Kept the "ATP numbers in this course" box, Table 1, the diabetes box, the fates-of-pyruvate material and the Lecture Connection.
  - The remaining fates figure is still labelled Figure \PageIndex{3}; consider renumbering it to 1.
- **597203 14.4 (Malik ETC trimmed)**
  - FMN, [2Fe-2S]/[4Fe-4S] and the semiquinone are gone; the "two mobile carriers" paragraph is kept, with the cytochrome c heme image.
  - The FMN structure image (fileid 446228) is dropped, and the ubiquinone alt text is simplified.
  - Complex I no longer covers FMN, Fe-S chains, P-side/N-side or the pumping mechanism.
  - The Complex II cofactor inventory is gone.
  - The Complex III Q-cycle text and its Q-cycle image (fileid 436642) are replaced by a plain cytochrome paragraph.
  - The Complex IV "three copper, one magnesium, one zinc" detail now reads "iron (in heme) and copper".
  - The Fo c-ring and F1 α/β/γ paragraphs are replaced by a turbine paragraph and a stalk/shape-change paragraph.
  - Professor Tip updated.
  - Kept: equations per complex, chemiosmosis, the ATP synthase figure group (its alt text still mentions the subunits, which describes the drawing), heating the body, the CO Valley box and all Lecture/clinical content.
- **597214 15.8**
  - Fixed the orphan "(Figure 1)" and "upper right in the figure at left" references (now pointing to the Lecture Connection figure). Also fixed "both acetyl-CoA molecules", since one of them is malonyl-CoA.
  - Removed the D-configuration sentence.
  - "(palmitoyl-CoA)" now reads "released as palmitate".
  - Simplified ACC regulation: insulin on; glucagon and epinephrine off by phosphorylation; citrate activates; palmitoyl-CoA inhibits by feedback inhibition. AMP kinase and polymerization are gone.
  - The fatty acid synthase enzyme list (and its orphan Figure 2 reference) is cut to one sentence.
  - The elongase paragraph (and another orphan figure reference) is cut to one sentence.
  - The desaturation paragraph is kept, because the essential fatty acids depend on it.
- **597217 15.11**
  - Condensed the enzyme-by-enzyme source text (glutamine synthetase, pyrroline-5-carboxylate, the SAM/cystathionine route, THF) into three plain paragraphs. This also fixes "D-pyrroline" and the orphan "(Figure 12 and 13)".
  - The tyrosine/PKU paragraph and the essential-amino-acid sentence are kept unchanged.
  - Removed the duplicated Summary box.
- **597194 13.6**
  - The mannose paragraph is reduced to a "beyond this course" sentence. It still names hexokinase and phosphomannose isomerase and the step-3 entry, so Exercises 1(b) and 7(c) remain answerable.
  - The transketolase/transaldolase paragraph is trimmed but keeps both names (Exercises 5 and 7(d) use them).
  - The polyol-pathway sentence is removed from the Nursing box.
  - The GALT steps are kept: galactosemia (classic = missing GALT) depends on them.
- **597204 14.5:** added a "Energy in food" paragraph (4-4-9 kcal/g; 1 food Calorie = 1 kcal) with one worked example: 30 g carbohydrate + 8 g protein + 12 g fat = 260 kcal. This supports the 14.6 learning objective, so the objective was kept.
- **597243/597244/597245 Practice Games:** "Every short practice set from this…" is now "Selected short practice sets from this…".

## Not done / left for the main session
- 13.5 (597193) still repeats the fates of pyruvate (aerobic, anaerobic, fermentation) that 13.4 also teaches. It was left alone per the "keep fates-of-pyruvate material" instruction. If 13.4 and 13.5 are merged later, keep one copy.
- 14.4 (597203) still contains the "Insulin - the blood glucose-regulating hormone" paragraph and the second full 32-ATP table, which repeat 14.5. These are candidates for a later cut; I left them because they were not in this assignment.
- Figure-number gaps from the deletions:
  - 14.2: figures 2 and 3 remain.
  - 13.4: figure 3 remains.
  - 14.4: Figures 1 and 2 are unaffected; the deleted images had no numbered captions.
- The 597209 activation image (fileid 446289) still needs the curved-arrow redraw requested in round 1.
- 14.1's adapted-from note still says "Some source figures were replaced with original figures by Daniel Kwasniewski". After the cut, the only figures left are Ball's 1 and 2, so that clause no longer applies. Consider trimming it.

## Page-move / retitle proposal (NOT in the JSON)
Retitles, with no move:
- 13.6 "Entry of Other Sugars into Glycolysis" → "Other Sugars and the Pentose Phosphate Pathway".
- 14.1 "Overview of Stage II of Catabolism" → "Acetyl CoA: From Pyruvate to the Citric Acid Cycle" (now accurate after the cut).
- 14.2 "Stage III of Catabolism" → "Stage III of Catabolism: An Overview".

**Chapter 13:** move 13.7 (Regulation and Stress, 597195) after gluconeogenesis.

| Page | Current | New |
|---|---|---|
| 597196 Glycogen | 13.8 | 13.7 |
| 597197 Gluconeogenesis | 13.9 | 13.8 |
| 597195 Regulation | 13.7 | 13.9 |

**Chapter 15:** lipid block first, then protein block. Lipid digestion becomes its own section by merging the digestion part of the old 15.1 Lecture Connection into old 15.5 (lipoproteins). Activation and the carnitine shuttle stay in old 15.1.

| Page | Current | New |
|---|---|---|
| 597211 (+ digestion text moved from 597207) | 15.5 | 15.1 Digestion of Fats and Lipid Transport |
| 597212 Storage/Mobilization | 15.6 | 15.2 |
| 597207 Activation/Transport | 15.1 | 15.3 |
| 597209 β-Oxidation (+ glycerol) | 15.3 | 15.4 |
| 597213 Ketone bodies | 15.7 | 15.5 |
| 597214 Fatty acid synthesis | 15.8 | 15.6 |
| 597215 Digestion of proteins / N balance | 15.9 | 15.7 |
| 597208 Transamination/deamination | 15.2 | 15.8 |
| 597216 Urea cycle | 15.10 | 15.9 |
| 597210 Carbon skeletons + pathway overlap | 15.4 | 15.10 |
| 597217 Amino acid synthesis | 15.11 | 15.11 (unchanged) |

Cross-references that would need updating. Counts come from a regex over every pages/live/*.html for "Section(s) N.N" text references, including lists such as "Sections 15.2 and 15.4", plus /@go/page/<id> links. Page 488232 (Glossary) and 597272 (Course Outline Alignment) carry many of them. The raw output is in scratchpad/ch1315r2/xrefs.txt.

| Section | Text refs | Pages with text refs | @go links | Pages with @go links |
|---|---|---|---|---|
| 13.7 (→13.9) | 10 | 488232×3, 597191, 597192×2, 597193, 597198×2, 597213 | 10 | 597270, 488232×3, 597199×2, 597198×3, 597272 |
| 13.8 (→13.7) | 12 | 488232×2, 597194×2, 597195×4, 597197×2, 597198×2 | 8 | 488232×2, 597199×2, 597198×2, 597272×2 |
| 13.9 (→13.8) | 12 | 488232, 597192×2, 597193, 597195, 597196×2, 597198, 597200, 597209, 597210, 597213 | 6 | 488232, 597051, 597198×2, 597272×2 |
| 15.1 (→15.3; digestion refs →15.1) | 11 | 488232×4, 597191×4, 597209, 597211, 597214 | 10 | 597191, 488232×4, 597272×2, 597053, 597218×2 |
| 15.2 (→15.8) | 11 | 488232×3, 597210×3, 597215×2, 597217×2, 597218 | 6 | — |
| 15.3 (→15.4) | 12 | 488232, 597200, 597202, 597207×4, 597211, 597218×2, 597219×2 | 12 | — |
| 15.4 (→15.10) | 7 | 488232×2, 597208×3, 597211, 597215 | 7 | — |
| 15.5 (→15.1) | 3 | 597207, 597212, 597214 | 2 | — |
| 15.6 (→15.2) | 6 | 488232×2, 597203, 597207, 597209, 597211 | 4 | — |
| 15.7 (→15.5) | 11 | 488232×3, 597207×2, 597209×3, 597212, 597218×2 | 13 | — |
| 15.8 (→15.6) | 4 | 488232, 597207, 597211, 597212 | 3 | — |
| 15.9 (→15.7) | 5 | 488232×2, 597191×3 | 5 | — |
| 15.10 (→15.9) | 12 | 488232×2, 597208×3, 597210×4, 597217, 597218×2 | 6 | — |
| 15.11 | unchanged | — | — | — |

Also needed:
- Figure captions numbered by section ("Figure 13.7.1", "Figure 15.3.1", and so on) on 597195, 597196, 597197, 597207, 597208, 597209, 597210, 597212, 597213 and 597216 must be renumbered.
- The Chapter 13 and 15 openers ("Read every numbered section 15.1 to 15.11"), the chapter guides' Key Idea pointers, CONVENTIONS.md ("Taught" and "Depends on" columns cite 13.x/15.x numbers, e.g. 15.10, 15.11), and the bank/game copy that cites section numbers all need updating as well.
- Because of the double counting (text plus links), a regex-driven renumber with a mapping table, run in one pass, is safer than hand edits.
