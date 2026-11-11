# CHEM 3B textbook review and revision brief for Claude

Prepared for Dr. Daniel Kwasniewski, Fresno City College. November 8, 2026.

## Purpose and evidence boundary

Make *Introductory Organic and Biological Chemistry for FCC* a dependable, approachable resource for allied-health students. Preserve its local identity, instructor voice, worked examples, course alignment, and free access while correcting scientific explanations and improving the student workflow.

The reviewed artifact is `Full.pdf`, 1,274 PDF pages, compiled November 9, 2026 UTC. It contains roughly 440,000 extracted words. The review covered the front matter and chapter structure, text searches across the export, selected examples and answer keys across the course, and visual inspection of 23 distinct pages. It is a detailed revision brief based on a first-pass review, not a certification that every paragraph, figure, answer, clinical claim, or live interaction is correct. No repository code, ADAPT settings, screen-reader session, or live widget behavior was independently tested for this review.

All locations below use the PDF viewer's one-based page number. Some include the printed footer, which differs from the viewer number. Search the quoted phrase or section title if later exports shift pagination. Exact page references identify observed issues. Chapter audit instructions identify work still needed. Suggested technical causes are hypotheses until confirmed in the source.

## Overall assessment

The course has a strong instructional foundation. Its most valuable additions are the Lecture Connections, Problem/Solution/Check examples, continuing Rosa case, Valley Connections, and specific links between textbook topics and practice tools. These features make the resource distinctive and relevant to FCC students. Preserve them.

The principal weaknesses are a recurring rendering defect in molecular figures, several overly broad statements in explanations, and an organization that sometimes requires students to reconcile inherited source material with later course-specific corrections. The size of the export also makes a clearly marked required reading path essential. A reference library can be extensive while the assigned route through it stays manageable.

Prioritize dependable representations and explanations before adding more content. The export contains 1,108 distinct numbered problems in the chapter practice sections, based on headings matching `Problem chapter.number`. This count excludes worked examples and other exercises and does not establish the number or quality of ADAPT items. The advertised chapter homework draws total 625 questions if all 15 listed assignments are used once. Actual workload depends on instructor assignment choices and item complexity.

## Instructions for the next Claude session

1. Obtain the current source files and identify the exact revision used to generate the reviewed export. Read repository instructions before editing. Trace how HTML, SVG, practice content, and LibreTexts pages are generated and published.
2. Create an issue ledger using the IDs below. For each issue record the source file or LibreTexts page, evidence, proposed correction, related occurrences, validation performed, and remaining uncertainty.
3. Correct shared figure and typography generation first. Produce a small representative export to verify the repair before regenerating the entire book.
4. Correct the confirmed scientific explanation issues. Search the source, chapter guides, glossary, practice keys, and any shared question bank for the same wording or rule.
5. Review the assigned reading route and reconcile source/course conventions where students first encounter them.
6. Complete the chapter audit matrix. Every reviewed problem needs an independent solution and a recorded outcome. A search that finds no suspicious phrases does not constitute review.
7. Test website behavior and the PDF separately. Record which environments and interactions actually passed.
8. Deliver a change log, an updated issue ledger, a fresh export, and a short instructor review list. Preserve attribution and the evidence behind each substantive correction.

Start with issues R01–R03 and C01–C06. Batch repeated corrections through their shared source where possible. Finish and verify one coherent batch before spending remaining context on the next batch.

## Confirmed rendering and publication issues

### R01 — Skeletal-structure atom labels become unreadable in the PDF

**Severity — release blocker for affected exercises.**

**Observed locations.** Acetaminophen at PDF pp. 71 and 110; lidocaine at p. 124; eugenol at p. 125; chlorinated alkane at p. 195; benzocaine at p. 262; multifunctional carbonyl compounds at p. 403; amine/amide reaction drawings at p. 555. The defect is visible in rendered pages, not merely in extracted text.

**Evidence and consequence.** Dark skeletal bonds survive, while several heteroatom labels appear white or nearly invisible against the pale background. On p. 110, students must identify acetaminophen's functional groups, but the NH, OH, and carbonyl oxygen cannot be read normally. A missing Cl label can make a haloalkane look like an alkane. Missing O/N labels change the apparent chemical identity and make answer keys seem arbitrary.

**Source investigation.** Locate the Bond Voyage structure/reaction rendering path and inspect the actual SVG or image supplied to LibreTexts. Check explicit text fill, stroke, stroke width, paint order, masking, CSS inheritance, theme variables, and font embedding. White outlines intended to create a background halo may be covering the letter interiors. This is a plausible cause, not an established diagnosis. Compare one failing skeletal figure with the readable expanded structures on pp. 110, 744, and 813.

**Required result.** Every required atom label, hydrogen label, charge, bond, wedge, and dash must remain distinguishable on the page background in the website, PDF, and grayscale print. Use explicit export-safe styling in generated chemistry assets. If live SVG cannot be exported reliably, provide a verified print asset generated from the same molecular representation.

**Acceptance checks.** Render at normal reading size and enlarged size. Verify acetaminophen, lidocaine, benzocaine, a halogenated alkane, a charged amino acid, a reaction with ionic products, and a stereochemical example. Independently reconstruct each molecule from the visible figure and confirm it matches the question and solution. A readable caption does not compensate for an unreadable structural formula. Run the same check for all assets generated through the repaired path.

### R02 — Charge and special-character corruption

**Severity — high.**

PDF p. 555 visibly shows replacement-like glyphs in reaction labels involving H+, Cl−, and NH4+. Text extraction found the unusual glyph `⯑` on 48 pages before the back matter. That is a search lead, not proof that all 48 pages have the same visible defect.

Use supported chemical notation consistently. Inspect source encoding, fonts, SVG text nodes, and superscript generation. Where appropriate use real superscript elements or supported Unicode characters with a verified font. Do not globally delete the unfamiliar glyph because it may stand in for a meaningful sign.

Acceptance checks must include H+, OH−, NH4+, Cl−, Ca2+, carboxylate, protonated amine, NAD+, NADH, FADH2, β-oxidation, α/β carbohydrate labels, arrows, and equilibrium arrows. Verify both visual meaning and extracted text. Inspect the corresponding screen-reader output in the web version.

### R03 — Cover author metadata

**Severity — medium.**

The outer cover on PDF p. 1 credits `Unknown`, while p. 2 credits Dr. Dan correctly. Correct the generating book metadata so the cover, title page, PDF metadata, and attribution display agree with the intended authorship. Preserve source-author credits within adapted sections. Regenerate the cover to confirm the metadata change actually reaches the export.

### R04 — Printed answers immediately follow questions

**Severity — medium; usability issue.**

In sampled practice pages, answer disclosures expand into printed answers immediately below the question. That makes self-testing difficult and means the instruction to open an answer toggle does not describe the PDF experience.

Provide a deliberate print workflow. Options include a student practice export with a separate answer section, or a questions-only companion generated from the same content. Keep answers available in an accessible form. Shared IDs must keep questions, figures, solutions, and answer references synchronized. Test pagination so a question does not lose its figure or options at a page break. The instructor should be able to print a small chapter assignment without assembling screenshots.

## Confirmed scientific and explanatory corrections

### C01 — Tollens' reagent explanation overgeneralizes

**Priority — high. Location — Section 5.7, PDF p. 406, printed p. 387, Problem 5.2.**

The key states `Only aldehydes are oxidized by Tollens’ reagent.` Section 8.5 on PDF p. 611 explains that ketoses such as fructose can give positive Tollens' and Benedict's tests under basic conditions. The multiple-choice answer can remain correct for its listed compounds while the explanation is too broad.

Suggested replacement meaning: Among these choices, the aldehyde gives a positive Tollens' test because it is oxidized to a carboxylate while silver ions are reduced to silver metal. Ordinary simple ketones do not give this test. Certain reducing sugars also test positive under the basic conditions, as discussed in Chapter 8.

Audit all statements about aldehydes, simple ketones, α-hydroxy ketones, reducing sugars, and oxidation tests together. Verify that every test question specifies the substrate and reagent conditions needed for its intended result. Do not replace the overgeneralization with an equally broad claim about all ketones or all carbonyl compounds.

Acceptance cases include a simple aliphatic aldehyde, a simple ketone, glucose, fructose, sucrose, and a stated α-hydroxy ketone. Check that the explanations in Chapters 5 and 8 agree.

### C02 — pI is used beyond what it establishes

**Priority — high. Locations — pp. 743–744, 808–809, and 813.**

Three related repairs are needed.

**Threonine drawing, pp. 743–744.** The problem requests structures well below and above the pI. The answer says everything that can accept or donate H+ does so. Comparing pH with pI indicates the sign of the average net charge, but the relevant pKa values determine which individual groups are predominantly protonated. Replace vague pH endpoints with explicit values chosen relative to the ionizable groups, and provide the required pKa information or a reference table. For an introductory exercise, strongly acidic and clearly basic conditions can illustrate the intended +1 and −1 forms, provided the limits and predominant-species convention are stated.

**Electrophoresis, Problem 10.59, pp. 808–809.** The question asks direction and net-charge sign. The answer adds that aspartate moves fastest because pH is far above its pI and that histidine moves only slightly because its pI is relatively close. Remove these unsupported speed rankings. Under the exercise's simplified conditions, pH versus pI supports the direction of migration. Relative speed also depends on charge magnitude, size, shape, and the separation conditions. Additional data would be needed for a speed comparison.

**Peptide solution, p. 813.** The lysine-side-chain explanation invokes a pI of about 9.7 as if it were the side-chain ionization constant. Use the relevant side-chain pKa to justify protonation. A free amino acid's pI is not the pKa of its side-chain amine, and a peptide has its own acid–base behavior.

Acceptance checks should distinguish average net charge from a single dominant drawn species. Test a neutral-side-chain amino acid, an acidic amino acid, a basic amino acid, and a peptide with ionizable side chains. Verify the logic at pH below, near, and above each relevant pKa. Require chemically correct terminal groups and explicitly state the pH of products when hydrolysis and subsequent neutralization are involved.

### C03 — Six enzyme classes presented as exhaustive

**Priority — high. Locations — pp. 823–825; related wording on pp. 1023 and 1045.**

The text says every enzyme belongs to one of six classes. Current IUBMB nomenclature also includes EC 7, translocases. Keep the six traditional classes as the core course selection if that matches the outline and exams. Add one sentence acknowledging the seventh class and explain that the chapter concentrates on the six most frequently used in the assigned reaction exercises.

Suggested meaning: This course emphasizes the six traditional enzyme classes below. The current EC classification also includes translocases, which catalyze movement of ions or molecules across membranes or their separation within membranes.

Check headings, tables, glossary entries, counting questions, games, and metabolism prompts for claims of exhaustiveness. Do not automatically reclassify every transport-related enzyme or add an unplanned assessment requirement. Validate individual classifications against IUBMB when editing examples.

### C04 — Bond breaking described as the source of released energy

**Priority — high. Locations — p. 977 and related phrasing on p. 1108.**

The ATP video description on p. 977 says breaking a phosphate bond releases energy. The citric-acid-cycle discussion on p. 1108 says a step is driven by breaking the thioester bond of acetyl CoA. Both encourage students to attribute favorable reaction energy to the isolated bond-breaking step.

For ATP, describe the overall hydrolysis reaction as having a negative Gibbs free-energy change under cellular conditions. Bond breaking requires energy; the overall balance includes formation and stabilization of products. For citrate formation, describe coupling to the favorable hydrolysis of the acetyl-CoA thioester in the overall citrate synthase reaction. Keep the explanation appropriate to CHEM 3B and avoid unsupported claims that one single factor universally accounts for the entire free-energy change.

Search diagrams, captions, tips, glossary definitions, quizzes, and video descriptions for analogous wording. Test whether students can explain why bond breaking itself requires energy while ATP hydrolysis overall can drive a coupled process. Include the participating water and chemically meaningful products in reaction figures.

### C05 — ATP accounting conventions appear in conflicting reading order

**Priority — high for instructional consistency. Locations — pp. 1008, 1128–1129, 1133.**

The draft already explains the older 3 ATP/NADH and 2 ATP/FADH2 convention and states the course's 2.5 and 1.5 values. It also correctly discusses 30 versus 32 ATP depending on the handling of cytosolic reducing equivalents. The issue is placement and question consistency. Students can encounter the old source table before the corrective Lecture Connection.

Place the current course convention before the first affected source table. Clearly mark historical accounting if retained. Whenever a question expects 32 ATP, state the malate–aspartate-shuttle assumption or explicitly invoke a nearby course accounting convention. When the question asks generally about complete aerobic oxidation, allow the explained approximate range. Use internally consistent gross/net, per-glucose/per-acetyl-CoA, and ATP-equivalent labels.

Acceptance calculations include net glycolytic ATP of 2, NADH and FADH2 yields per turn of the cycle, approximately 10 ATP equivalents per acetyl CoA, and 30/32 per glucose under the stated shuttle assumptions. For saturated even-chain fatty acids, verify cycle count, acetyl-CoA count, activation cost, and the chosen P/O ratios. The reviewed laurate calculation on p. 1216 gives 78 and its palmitate comparison gives 106 using the stated assumptions. Preserve these worked checks while testing other cases independently.

### C06 — Glycogenesis step numbers change meaning

**Priority — medium. Location — p. 1042, printed p. 1023, Section 13.8.**

The five-step table identifies UDP-glucose activation as step 3. The prose then introduces a three-step lecture scheme where activation is step 2. The following energy paragraph says step 3 consumes UTP. Its chemistry matches the table but its reference is ambiguous after the renumbering.

Replace the numeric reference with the reaction name. State that phosphorylation of free glucose consumes one ATP, and UDP-glucose activation consumes UTP, counted as another ATP equivalent when UTP is regenerated from UDP. Tie the two-equivalent cost to the stated starting substrate. If both numbering schemes are retained, label each explicitly and use reaction names in cross-references.

Acceptance checks include matching all table rows to the diagram, tracing the nucleotide products, and confirming that the problem specifies whether the starting molecule is free glucose or an already phosphorylated intermediate.

### C07 — A metabolism learning objective implies every listed carrier derives from a B vitamin

**Priority — medium. Location — p. 1057, printed p. 1038, Section 13.10.**

The objective lists NAD+/NADH, FAD/FADH2, CoA, ATP/ADP, and NADPH, followed by an instruction to name the B vitamin each is built from. Narrow this to the vitamin-derived coenzymes. ATP and ADP should not be assigned a B-vitamin precursor by this wording.

Use explicit mappings for the examples taught: niacin/B3 for NAD-related cofactors, riboflavin/B2 for FAD-related cofactors, and pantothenate/B5 as a component of CoA. Explain that these are components or precursors, rather than implying the entire coenzyme is simply the vitamin. Verify the vitamin table and corresponding assessment items together.

### C08 — A correct worked example ends with an unsafe general rule

**Priority — medium. Location — p. 1060, printed p. 1041, Section 13.10.**

The gluconeogenesis example correctly explains that fructose-1,6-bisphosphatase hydrolyzes a phosphate without recovering ATP. Its Check then begins, `If you need ATP one way, you don’t need it the other way.` That sentence can be memorized as a general rule about reversing reactions even though the example involves a different enzyme and reaction.

Replace it with a check specific to the bypass. State that the gluconeogenic bypass uses hydrolysis instead of reversing the phosphofructokinase reaction, so ATP is not regenerated at that step. Retain the useful overall comparison between the energy cost of gluconeogenesis and the ATP yield of glycolysis. Search other Check sections for a similar pattern where a valid example ends in an excessively broad shortcut.

## Student experience and course organization

### D01 — Put the assigned route at the start of each chapter

The About page directs students to read the source sections and the Lecture Connections, with the Chapter Guide appearing afterward. For a 1,274-page export, students need a visible distinction between required preparation, optional reference depth, and practice selected for the week.

Add a compact chapter opening with prerequisite skills, the required section list, a short readiness task, and a suggested practice route. Let the instructor assign the depth. Use measured student completion times before publishing estimates. Avoid turning all 70 or more chapter questions into an implied minimum requirement.

Provide two entry paths. A student preparing for class needs a short sequence of reading and initial practice. A student reviewing for an exam needs a diagnostic that sends them to the specific explanation and a new problem. Both paths should link to the same authoritative content so corrections remain synchronized.

### D02 — Make Lecture Connections the first source of course conventions

Retain attribution while moving crucial course framing above inherited sections. A brief statement of what students should learn can precede the detailed source reading, while extended instructor examples can remain after it. Where source conventions differ, the convention notice belongs before the conflicting material. Students should be able to answer what convention applies without scrolling through the whole section.

Prioritize ATP accounting, enzyme classes, chemical naming conventions, pH/charge assumptions, and structure representations. Correct a scientific error directly in adapted content when permitted, documenting the adaptation. Preserve historical material only when its historical role is pedagogically useful.

### D03 — Build explicit reasoning into clinical cases

Keep Rosa and the Valley Connections. For each case, make the intended chemistry observable. Ask students to identify the relevant feature, use it to predict a property or pathway, then explain the prediction in one or two sentences. Include sufficient information to solve the problem without requiring unintroduced clinical knowledge.

Review each case for the difference between a biochemical explanation and a clinical conclusion. A laboratory value rarely establishes a diagnosis by itself. Verify medication, diagnostic-threshold, toxicology, and treatment-related claims against current authoritative clinical sources during the dedicated clinical review. This brief does not certify those claims. Keep patient care decisions within the intended educational boundaries of the course.

### D04 — Preserve confidence without replacing reasoning with slogans

The Professor Tips and Check boxes are central to the voice of the book. Give each shortcut its conditions. Ask whether a learner could apply it to a neighboring case and obtain an incorrect answer. Check words such as always, never, only, all, must, and exactly in their full chemical context. A search is a way to locate candidates, not an instruction to remove every absolute statement.

### D05 — Use cumulative retrieval

Include a small set of prior-topic problems in each chapter. For example, a carbohydrate section can retrieve carbonyl chemistry and stereochemistry; a protein section can retrieve amides and acid–base behavior; a metabolism section can retrieve oxidation, enzyme class, and coenzyme roles. Identify which earlier section supports each item. Keep cumulative work short enough that students can complete it routinely.

## Assessment and answer-key audit

Create an inventory with stable question IDs, chapter, learning objective, prerequisite, skill type, format, difficulty rationale, answer, explanation, figure ID, source status, and review status. Use an existing data model if available. Add fields only where they support actual maintenance or review.

For every assessed item, independently solve the problem before comparing with the existing answer. Check that the prompt provides enough information, all displayed structures are valid, the intended response is uniquely correct under the assumptions, and the explanation supports the actual answer. Multiple-choice distractors must be plausible and unequivocally wrong under the stated conditions. Equivalent naming conventions or chemical representations must not accidentally make two choices correct.

For numerical items, recompute from the supplied values and check units, significant figures, tolerances, and rounding instructions. For acid–base items, distinguish dominant species from average net charge. For stoichiometry and metabolism, check the stated basis and gross versus net totals. For structure questions, validate carbon count, hydrogen count, charge, valence, stereochemistry, and atom connectivity independently of the caption.

Design feedback for the error a student made. A wrong ATP answer may come from forgetting activation cost, counting one turn per glucose, or using an older P/O ratio. Each needs a different explanation. A naming error may reflect wrong parent selection, numbering, suffix priority, or a malformed structure. Feedback should identify the first conceptual correction and allow another attempt.

For free-response inputs, test legitimate alternatives actually taught in the course. Evaluate accepted name variants, spacing, capitalization, Unicode minus, charge notation, and chemical formula formatting. Avoid normalizing different chemical structures into the same answer. State when a task requires a specific representation or naming convention.

For ADAPT, verify the advertised bank size, selection count, attempts, hints, scoring, and Canvas grade passback in the real course configuration. Those settings are described in the PDF but were not independently accessed. Use stratified selection by learning objective and skill when random assignment is intended to represent chapter mastery. Check that different student draws have comparable workload and topic coverage. Randomness alone does not establish fairness.

For students who struggle, identify a short essential set, a second set that rebuilds prerequisite skills, and an optional challenge set. This is a proposed instructional organization, not a finding that existing questions lack variety. Keep access to all practice while making the next step clear.

## Chapter-by-chapter remaining audit

The tasks in this matrix are required review targets. Unless an issue ID is cited, they are not claims of a confirmed error.

| Chapter | Practice pages | Review tasks and expected evidence |
|---|---|---|
| 1 Bonding review | 115–129 | Repair R01. Check valence, formal charge, resonance, electron groups versus molecular shape, and distinction between bond and molecular polarity. For drug structures, validate every functional-group assignment and hydrogen-bond donor/acceptor claim. Use comparable molecules for boiling-point rankings and qualify solubility predictions. |
| 2 Alkanes | 183–198 | Verify longest-chain selection, tie-breaks, substituent numbering, ring versus chain parent selection, and condensed-formula parsing. For combustion balance C, H, and O. State conditions for halogenation and avoid implying a single product where substitution mixtures are possible. Check all halogen labels visually. |
| 3 Unsaturated and aromatic compounds | 253–269 | Verify cis/trans applicability, any E/Z assignments, aromatic versus alkene reactivity, addition products, and hydrogenation stoichiometry. Check when regiochemistry is assumed or taught. Review the benzocaine and geraniol structures. Distinguish a named major product from an exclusive product when needed. |
| 4 Alcohols and related groups | 332–345 | Check classification of the carbon bearing OH, oxidation of primary and secondary alcohols, phenol/alcohol acidity, ethers as acceptors, thiol/disulfide transformations, and conditions in reaction schemes. Verify that clinical examples identify the correct molecule and process. |
| 5 Carbonyls and chirality | 406–421 | Correct C01. Review Tollens/Benedict boundaries, carbonyl oxidation and reduction, hemiacetal/acetal connectivity, D/L reference conventions, and enantiomer/diastereomer/meso distinctions if included. Check 2^n counts for symmetry exceptions. Repair R01 in multifunctional nomenclature drawings. |
| 6 Acids and esters | 485–499 | Check ester naming direction, acid versus base hydrolysis products, carboxylate charge, conditions for esterification, and the effect of ionization on solubility. Ensure buffer and pH predictions specify the necessary pKa or assumptions. |
| 7 Amines and amides | 564–579 | Repair R02 and the affected reaction figures. Check amine classification by groups attached to N, amide resonance/basicity distinctions, ammonium salt charges, and hydrolysis products under stated conditions. Review simplifications in direct acid-plus-amine amidation and make activation or heating assumptions clear. |
| 8 Carbohydrates | 638–655 | Cross-check C01. Validate Fischer/Haworth conversions, anomeric carbon, α/β relative configuration, epimer versus enantiomer distinctions, reducing-end status, glycosidic linkage positions, and oxidation products. Verify that D/L is not equated with optical rotation. |
| 9 Lipids | 716–731 | Check fatty-acid notation, cis/trans effects, chain-length comparisons, ester count, saponification products, and structural distinction among phospholipids, sphingolipids, and steroids. Qualify membrane-fluidity comparisons by temperature and composition where relevant. |
| 10 Amino acids and proteins | 800–817 | Correct C02. Verify all peptide sequences in both directions, termini, side-chain charge, hydrolysis products, peptide-bond counts, and amino-acid abbreviations. Distinguish denaturation, reduction of disulfides, and peptide hydrolysis. Audit pH conditions in every drawn structure. |
| 11 Enzymes and vitamins | 868–884 | Correct C03. Check activation-energy versus equilibrium claims, saturation, temperature/pH interpretations, cofactors/coenzymes, and vitamin mappings. If kinetic parameters are used, distinguish competitive, uncompetitive, mixed, and pure noncompetitive inhibition under the stated model. Match graphs, labels, and keys. |
| 12 Nucleic acids | 959–974 | Check 5′/3′ direction, template versus coding strand, antiparallel pairing, RNA versus DNA bases, reading frame, start/stop handling, and mutation consequences. Verify all sequence translations against the specified code and strand. Review distinctions among replication, transcription, and translation. |
| 13 Carbohydrate metabolism | 1064–1079 | Correct C04–C08 as applicable. Check pathway locations, carbon balance, ATP investment/payoff, NAD+/NADH recycling, glycogen synthesis/breakdown, gluconeogenesis bypasses, and tissue-specific hormonal effects. Check that fermentation is distinguished from glycolysis itself. |
| 14 Energy production | 1139–1153 | Correct C04/C05. Check carbon accounting through pyruvate oxidation and the cycle, reducing-equivalent yields, oxygen's role, proton-pumping complexes, ATP synthase, and inhibitor versus uncoupler predictions. Match the diagram to the numerical convention. |
| 15 Lipid/protein metabolism | 1221–1236 | Check β-oxidation activation costs, cycle counts, odd-chain and unsaturated exceptions where included, ketogenesis, glucogenic/ketogenic fates, transamination, oxidative deamination, and urea nitrogen sources. Distinguish three ATP molecules from four high-energy phosphate equivalents in urea synthesis when teaching that accounting. Verify clinical claims separately. |

## Accessibility and visual quality verification

The front matter claims WCAG 2.1 AA preparation, rewritten descriptions for 875 inherited figures, and automated scans of every page. These are statements in the book. This review did not verify the underlying scan results or establish conformance. Keep claims proportional to recorded evidence.

Inspect representative pages using keyboard-only navigation and a screen reader. Include a structure exercise, a dense pathway figure, a table, an answer disclosure, an embedded game, and video navigation. Verify heading order, meaningful link names, focus visibility, focus order, disclosure state, iframe title, and a way to leave an embedded activity. Automated checking can supplement this work.

For molecular diagrams, distinguish a descriptive alternative from an answer reveal. When a figure is the question, its accessible representation should supply equivalent structural information without announcing the functional groups or classification the learner must infer. Use an appropriate text or structured representation and test it with actual users. For pathways, describe inputs, outputs, compartments, arrows, and relevant stoichiometry in a readable order.

Verify that color reinforces meaning already conveyed by labels, symbols, or layout. Check the PDF in grayscale and at typical laptop viewing size. Large pathway graphics need an accessible larger view and readable text equivalents. Verify contrast of formula labels separately from paragraph text.

Test the export's tagged reading order, table associations, formulas, bookmarks, and links. A tagged PDF flag alone does not establish accessibility. The reviewed PDF contains many bookmarks and working-looking link annotations, but this does not establish that every destination or reading sequence is correct. Confirm that bookmarks navigate to the desired content rather than merely the matching table-of-contents entry.

## Live tool and technical checks

Use the actual generated links and current application source to test the student journey. For each chapter, open its practice page, launch every assigned game, and verify that the intended CHEM 3B course/topic is selected. Some export links include course, topic, or search parameters. Confirm that the target application recognizes them and actually produces the intended question set.

Test empty or invalid topic selections, exhausted question filters, incorrect and correct responses, hints, revealed answers, retries, keyboard operation, refresh, saved-progress behavior, and a fresh browser profile. Confirm whether progress is local to a browser and whether students can understand the limits. Do not claim cross-device progress unless it exists and has been tested.

Check responsive layouts at phone, tablet, and laptop sizes, including Canvas embedding if used. Verify that controls remain reachable at increased text size and that diagrams retain a readable enlargement option. Evaluate touch targets and horizontal overflow in chemical formulas and tables.

For generated figures, create a small regression set using the existing renderer and export path. It should include all critical representations from R01/R02. A text-only assertion that an SVG contains `O` cannot establish that the oxygen is visible. Combine semantic checks with rendered inspection.

For randomized questions, enumerate finite banks when practical and independently verify representative generated boundary cases. Check repeated or chemically equivalent choices, contradictory hints, impossible inputs, and answer-dependent feedback. A correct answer string alone does not establish chemical correctness of the problem.

## Attribution and publication review

Retain the section-level source table and explicit adaptation log. They are valuable maintenance records. The book combines original contributions, adapted CC BY-NC-SA material, and other sources with distinct terms. Preserve that distinction when reorganizing or generating alternate exports. Verify third-party figure permissions and credit against the actual source record. The current draft's licensing claims should be checked by the designated institutional OER reviewer before release; this brief is not a legal determination.

The front matter states that practice problems and examples are original and that commercial textbook/test-bank content was not used. Keep a provenance record that supports those assertions. Editing should record the source of newly introduced material. Reviewers should be able to trace a figure, example, or clinical claim to its source or authorship record without relying on AI recollection.

Verify the asserted course-outline mapping against the actual approved CHEM 3B outline. The PDF includes a detailed alignment table, which is a useful starting point, but presence of a topic in a table does not prove adequate teaching or assessment coverage. Link each required skill to instruction, guided practice, independent practice, and the intended assessment.

## Implementation sequence and completion criteria

### Batch 1 — Restore readable chemistry

Repair R01/R02 through the shared generation path. Correct R03. Export representative chapters and inspect all affected figure types. Save a record of the exact test cases and export environment. Finish when students can recover the intended chemical information from each tested diagram and all discovered occurrences have been tracked.

### Batch 2 — Correct reusable scientific rules

Implement C01–C08. Review related glossary entries, tables, guides, practice keys, and shared question data. Independently solve the affected questions. Finish when explanations agree across chapters and the corrected rules work on the stated acceptance cases.

### Batch 3 — Clarify the student route

Implement required-reading guidance, earlier convention notices, selected essential practice, cumulative retrieval, and print self-testing. Pilot one early organic chapter and one metabolism chapter before applying the format across the book. Keep the instructor's voice and the Rosa/Valley connections.

### Batch 4 — Complete content and interaction review

Work through the chapter matrix and assessment inventory. Test live links, ADAPT settings, embedded tools, accessibility, and the export. Record actual results and unresolved cases. Separate an item that passed from one that was only searched or sampled.

### Batch 5 — Instructor and student acceptance

Have another chemistry instructor inspect the highest-risk material and a small group of students try representative reading-and-practice tasks. Observe whether they find the next step, interpret the structures, explain their reasoning, and recover from an error. Record confusing wording and unnecessary navigation. Use the observations to refine the resource before expanding features.

## Suggested issue-ledger fields

| Field | What to record |
|---|---|
| ID | Stable identifier such as C02 or a newly assigned chapter issue |
| Evidence | Exact section, question, figure, PDF page, and short description |
| Status | Confirmed, under investigation, corrected, verified, or unresolved |
| Source | Current file/page and revision used for the change |
| Correction | What changed and the chemical or instructional reason |
| Propagation | Related occurrences in guides, glossary, games, and banks |
| Verification | Independent calculation, source check, rendered page, or interaction performed |
| Remaining work | Specific untested cases, missing access, or instructor decision |

## Sources supporting technical corrections

These were consulted during the initial review. Recheck current authoritative records when changing material whose classification or guidance may have evolved.

- IUBMB enzyme classification, including EC 7 translocases. https://iubmb.qmul.ac.uk/enzyme/ and https://iubmb.qmul.ac.uk/enzyme/EC7/
- IUBMB EC 2.7.7.9, UDP-glucose activation reaction. https://iubmb.qmul.ac.uk/enzyme/EC2/7/7/9.html
- Research on amino-acid electrophoretic mobility and its dependence on charge and hydrodynamic behavior. https://pubmed.ncbi.nlm.nih.gov/17941132/ and https://pubmed.ncbi.nlm.nih.gov/40202216/
- Chemistry education research on ATP hydrolysis explanations and the bond-breaking misconception. https://pubmed.ncbi.nlm.nih.gov/37906689/ and https://pubmed.ncbi.nlm.nih.gov/40485986/
- IUPAC carbohydrate α/β terminology. https://goldbook.iupac.org/terms/view/A00003
- Creative Commons source materials for institutional review of adaptation and collection terms. https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode.en and https://creativecommons.org/compatible-licenses/

## Additional requirements for independent learning and long-term reliability

Added after reviewing the complete revision brief. These are proposed improvements and verification tasks, not additional confirmed defects in the textbook. Implement them in the existing chapter structure where possible. Prioritize changes to essential instruction before increasing chapter length or adding software features.

### L01 — Audit the bridge from explanation to independent work

For every core assessed skill, identify four existing items or supply what is missing: a fully worked example, a partially completed example, an independent problem with a closely related structure, and a transfer problem that changes the context or representation. Students should have a chance to finish some of the reasoning themselves before being asked to produce the entire solution.

For an ester-naming sequence, the full example can identify the alcohol-derived group and acid-derived portion. A partially worked example can identify one portion and leave the other to the student. The independent problem can use a new ester, followed by a transfer item that asks for its hydrolysis products under stated conditions. For metabolism, move from a fully labeled accounting table to a partially completed table and then a calculation with explicitly stated assumptions.

Acceptance criterion: an instructor can trace each essential skill from explanation through guided work to independent performance. A set consisting only of recognition questions is insufficient evidence that students can draw, calculate, or explain that skill.

### L02 — Teach translation among representations explicitly

Audit transitions among names, molecular formulas, condensed formulas, skeletal structures, expanded structures, Fischer projections, Haworth projections, reaction equations, and pathway diagrams. Introduce only the representations required for the current topic and explicitly teach what is preserved or hidden in each.

For structure translation, require students to track connectivity, atom count, charge, and stereochemistry when applicable. Include an exercise asking whether two drawings represent the same molecule. Avoid relying on the renderer's chosen orientation as the chemical identity. Pair unfamiliar visual conventions with a small legend or example at first use.

Acceptance criterion: students can translate in both directions for the representations the course assesses. Naming a displayed molecule and drawing a molecule from a name should each have appropriate instruction and practice.

### L03 — Make prerequisite repair specific and brief

At each major chapter transition, identify two to four prerequisite skills and link directly to a short refresher and one check problem for each. Example transitions include carbonyl chemistry into carbohydrates, amides and acid–base behavior into peptides, and oxidation/reduction into metabolism.

If a student misses the prerequisite check, the next step should identify the exact concept to revisit. A link to an entire 80-page chapter makes it difficult to recover efficiently. Reuse existing explanations and examples wherever possible. Completion of a game should be supplemented by a fresh independent check when the objective requires unaided work.

Acceptance criterion: a student who misses a prerequisite can reach a relevant explanation and retry with a new problem without needing the instructor to locate the material.

### L04 — Distinguish supported practice from independent success

When a game or widget reports progress, verify what its counters actually mean. A correct response after revealing the answer, a correct response after a hint, and an independently correct response should have understandable labels if the tool records those distinctions. A streak or total score should not be presented as proof of chapter mastery without an appropriate independent task.

For essential objectives, provide a short readiness check with fresh questions and explicit conditions about references and hints. Map missed items to a next step. Treat suggested thresholds as instructor decisions to evaluate with students. Avoid inventing a numerical mastery threshold and presenting it as validated.

Acceptance criterion: a student can tell what they completed with help and what they can do independently. Progress displays should encourage retries and make recovery from an error straightforward.

### L05 — Check transfer and diagnose reasoning errors

Add or select a few prompts that ask students to explain why an attractive wrong answer fails, compare two methods, or correct a short flawed solution. Label flawed examples clearly and provide an accurate explanation after the attempt. Use these sparingly around persistent misconceptions already relevant to the chapter.

For example, show a peptide-charge explanation that incorrectly substitutes pI for a side-chain pKa and ask which information is needed to decide the side-chain protonation state. After students have learned the corrected rule, change the peptide and pH for an independent follow-up. Other targets include confusing polar bonds with a polar molecule, swapping the two portions of an ester name, and counting gross ATP as net ATP.

Acceptance criterion: each essential topic includes evidence of reasoning beyond recognition of a familiar answer. Review the cognitive demand of the core assigned set, rather than increasing difficulty by adding more obscure terminology.

### L06 — Reduce duplication while preserving useful repetition

Compare each source section, Lecture Connection, Chapter Guide, and practice introduction. Mark repeated explanations that serve a clear retrieval or summary function, and consolidate duplicated prose that adds no new instruction. Keep one authoritative location for detailed rules and use focused summaries elsewhere.

Create a small conventions record covering naming variants taught, charge notation, pH assumptions, ATP accounting, abbreviations, and terminology used on exams. Link each convention to its teaching location. A correction should trigger review of every dependent example and key. Use existing source-generation features if available, and introduce shared data only when it reduces demonstrated duplication.

Acceptance criterion: students encounter compatible explanations throughout the course, and a maintainer can locate every place a changed convention affects. Consolidation should preserve examples that teach distinct reasoning steps.

### L07 — Keep the core learning route usable offline and with blocked embeds

For every required learning objective, confirm that the downloadable reading contains an explanation, a usable static representation, practice, and accessible answers. When a live activity adds essential instruction, provide an equivalent static task or explanation. State which features require an internet connection.

Test a downloaded chapter with the network disconnected. Separately test the web chapter when an embedded game or video fails to load. Students should still be able to identify the topic, continue the required work, and find an alternate way to access the activity when connectivity returns. Give essential videos an accurate transcript or equivalent written explanation. Captions need particular review for chemical names, charges, and numbers.

Acceptance criterion: a failed embed does not remove the only explanation or practice for an assessed skill. Verify this objective by objective rather than treating a successful full-book download as sufficient.

### L08 — Review language and glossary support

Identify unexplained abbreviations, terminology introduced before its definition, long sentences with multiple new concepts, and pronouns with unclear chemical referents. Keep necessary disciplinary vocabulary and explain it at first use. Pair formulas with names where that helps readers learn both.

The front matter describes glossary translations. Audit the actual translated entries for consistency with the English definitions and chemical terminology. Have a qualified bilingual reviewer check the intended student-facing translations before treating them as verified. Maintain links from important terms to their definitions and from definitions to a representative example.

Acceptance criterion: students can find and interpret the vocabulary needed for an exercise without relying on unexplained abbreviations or guessing which molecule a sentence refers to. A readability score alone does not establish conceptual clarity.

### M01 — Track review coverage precisely

Extend the issue ledger with a coverage table. For each chapter record the total number of inventoried text sections, figures, worked examples, and practice items, and how many have received the relevant review. Keep text extraction, visual inspection, independent solution, source verification, and live interaction as distinct recorded activities.

Use the verified inventory as the denominator. Do not report that an entire chapter passed because a few examples passed, or count a repeated question as a new independent case. For generated questions, record the tested templates, input ranges, boundary cases, and any exhaustive enumeration performed.

Acceptance criterion: the final report gives concrete coverage counts, remaining work, and unresolved issues. Every claimed fix has reproducible evidence tied to a source revision and output version.

### M02 — Make revisions safe for a course already in progress

Keep stable question and section identifiers when revising wording or relocating material. Provide redirects or a mapping when a URL must change. Identify which version is used for an assignment or printed packet. Corrections to an answer key should be communicated clearly enough for the instructor to decide whether existing student work needs regrading.

Record the source revision, export date, and versions of shared external activities used for a release where practical. Maintain a short student-facing errata list for substantive corrections, with the affected section/problem, correction date, and corrected interpretation. Check transcluded source material for changes that could silently reintroduce an old convention.

Acceptance criterion: existing Canvas links and assigned question references remain usable, and a reader can determine whether a correction applies to their copy. Review a before-and-after diff of chapter structure, formulas, question numbering, and attribution when producing a new release.

### M03 — Use explicit release gates

An assigned chapter is ready for instructor approval when its required figures render correctly, its assessed answer keys have been independently checked, its required learning objectives have a complete learning route, and its essential content remains available through the supported access formats. Any unresolved issue must be identified with the affected material and a concrete student workaround or a decision to defer that material.

Additional polish can follow after these gates pass. Use the actual teaching schedule to prioritize chapters, while repairing shared defects globally. Clinical accuracy, accessibility, and licensing review need the appropriate evidence or reviewer recorded before corresponding claims of verification are made.

## Copy-ready starting instruction for Claude

Please use this brief to revise my CHEM 3B textbook systematically. First read the current project instructions and locate the source that generates the affected chemistry figures and the LibreTexts/PDF output. Create a persistent issue ledger and begin with R01/R02, then C01–C08. For every correction, locate related instances and independently verify the chemistry. Render representative pages to check that the fix actually survives export. Preserve the course's instructor voice, Rosa's Story, Valley Connections, worked examples, and attribution records. Treat the chapter audit matrix as work to perform, not as a list of already-proven defects. At each stopping point, record what was changed, what passed verification, what remains untested, and the exact next task so work can resume efficiently when usage resets. Keep publication and deployment as explicit instructor decisions.
