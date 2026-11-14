# Glossary audit — page 488232 (Introductory Organic and Biological Chemistry for FCC)

Date: 2026-11-13. Read-only audit; no repo file was changed.

**Reviewer note.** I am a language-competent reviewer, not a native-speaker chemistry instructor. High-confidence items can be applied as they stand. **Medium- and low-confidence items should be confirmed by a native Spanish-speaking chemistry instructor before they go live.**

## 1. Scope and totals

- **Entries: 329** (329 table rows; every row has exactly one `Español:` span and one section link).
- All 329 link labels match the section number of the page they link to (checked against each page id's title after the 2026-11-12 renumbering). No stale section numbers.
- The Index page (488231) agrees with the Glossary on the section of every shared term, so **any pointer change below also has to be made in the Index list and in the page tags** (CONVENTIONS.md, Index note).
- No Spanish sentences anywhere: Spanish appears only as term equivalents. Rule met.
- Accents: all 329 Spanish strings checked (ácido, éster, éter, hidrólisis, glucólisis, aminoácido, cetona, enlace, etc.). **No accent errors found.**
- Root consistency: gluc- is used throughout (glucólisis, glucógeno, glucogénesis, glucogenólisis, gluconeogénesis, glucolípido, enlace glucosídico); glicol and glicerofosfolípido correctly keep glic-. sustrato/sustitución are consistent (no "substrato"). "enlace de hidrógeno, puente de hidrógeno" are given together in one entry and nowhere else, which is fine.
- The calques named in the brief are all correct as published: azúcar reductor, puente salino, modelo de llave y cerradura, modelo de ajuste inducido, inhibición por retroalimentación, ácido graso, cuerpos cetónicos, lo semejante disuelve a lo semejante, ácido graso saturado, grasa trans.
- Convention words: no "pKa", no "hydride" on the page. cofactor/coenzyme, ligase (citrate synthase), lyase, transferase, point mutation, NAD⁺ ("two electrons and an H⁺") all agree with CONVENTIONS.md.
- tools/glossary_es.py holds the same Spanish strings as the live page for the items sampled (ribosómico, tetraédrico, rancidez, amonio cuaternario, disulfuro), so any accepted change should be made there too.

## 2. Spanish equivalents with a problem (12 of 329)

| Headword | Current Spanish | Proposed Spanish | Issue type | Confidence | Note |
|---|---|---|---|---|---|
| rancidity, oxidative rancidity, hydrolytic rancidity | rancidez oxidativa, rancidez hidrolítica | rancidez, rancidez oxidativa, rancidez hidrolítica | headword mismatch | high | Three English terms, two Spanish; the bare term is missing. |
| ribosomal RNA, rRNA | ARN ribosómico, ARNr | ARN ribosomal (ribosómico), ARNr | regional usage | medium | Latin American texts mostly print "ARN ribosomal"; "ribosómico" is the Spain/RAE form. Both are correct; show both. |
| tetrahedral | tetraédrico | tetraédrica | gender consistency | medium | Sister entry is "trigonal plana" (feminine, agreeing with geometría). Make both the same gender. The alternative is to change the other one to "trigonal plano". |
| β-pleated sheet, beta-pleated sheet | lámina β plegada (beta) | lámina β (beta) plegada, hoja β plegada | format / variant | medium | "(beta)" is stranded after "plegada"; compare "hélice α (alfa)". "Hoja plegada β" is a frequent Latin American textbook form. |
| condensed structural formula | fórmula estructural condensada | fórmula estructural condensada, fórmula semidesarrollada | missing regional term | medium | "Fórmula semidesarrollada" is what students schooled in Mexico learned; it pairs with "fórmula estructural desarrollada", already used for *expanded structural formula*. |
| lone pair, nonbonding pair | par solitario, par no enlazante | par solitario, par libre, par no enlazante | missing common term | medium | "Par libre" / "par no compartido" is the usual wording in Latin American general chemistry texts. |
| disulfide, disulfide bond | disulfuro, enlace disulfuro | disulfuro, enlace disulfuro (puente disulfuro) | missing common term | medium | "Puente disulfuro" is the standard biochemistry term for the protein cross-link. |
| sickle cell disease, sickle-cell anemia | anemia de células falciformes, drepanocitosis | enfermedad de células falciformes, anemia de células falciformes (drepanocitosis) | headword order | medium | First English term is the disease, second the anemia; Spanish gives anemia first and no "enfermedad". |
| quaternary ammonium ion | ion de amonio cuaternario | ion amonio cuaternario | consistency | low | The page writes "ion carboxilato" without "de". Both forms are in print. |
| amino acid pool | reserva de aminoácidos | reserva de aminoácidos (pool de aminoácidos) | variant | low | Spanish biochemistry texts often keep "pool" or say "fondo común de aminoácidos". Instructor's call. |
| omega-3 fatty acid, omega-6 fatty acid, omega number | ácido graso omega-3, omega-6 | ácido graso omega-3, ácido graso omega-6, número omega | headword mismatch | low | Third headword has no equivalent. |
| induced-fit model, induced fit | modelo de ajuste inducido | modelo de ajuste inducido, ajuste inducido | headword mismatch | low | Cosmetic. |

Checked and left alone (correct; variants exist but no change needed): hidrofílico / hidrofóbico (RAE also has hidrófilo / hidrófobo; the -ico forms are normal in Latin American texts); sitio activo (Spain: centro activo); carbohidrato (Spain: hidrato de carbono, glúcido); teoría RPECV (also TRPECV); balance de nitrógeno (also balance nitrogenado); glucogénesis (also glucogenogénesis); regla de Zaitsev (also Saytzeff); estructura de esqueleto, estructura de líneas y ángulos (also fórmula de líneas); enzima alostérica (enzima treated as feminine, the normal usage); hidrólisis de amidas (plural for a singular headword, idiomatic); mitocondria (singular only, fine); ATP sintasa, ADN polimerasa, alcohol deshidrogenasa (enzyme name order is standard).

## 3. Definition problems

| Headword | Problem | Proposed fix | Confidence |
|---|---|---|---|
| polypeptide | "A long chain of amino acids" contradicts the course ranges (CONVENTIONS.md, Section 10.4: oligopeptide 2–20, polypeptide 21–40, protein >40). | State the ranges; note the word is also used for one chain of a protein (the glossary itself uses it that way under hemoglobin, collagen, α helix). | high |
| glycol, diol | The intro says comma-separated terms "mean the same thing", but Section 4.6 teaches "a glycol is a diol with OH groups on adjacent carbons". | Define diol, then glycol as the adjacent-carbon case. | medium |
| water-soluble vitamins | "most are coenzymes": vitamins are the starting materials for coenzymes, not the coenzymes (11.5 table links each vitamin to its coenzyme; the coenzyme entry says "usually made from a vitamin"). | "the body turns most of them into coenzymes". | medium |
| feedback inhibition, feedback control | Does not say the enzyme is allosteric; CONVENTIONS.md files feedback inhibition under allosteric regulation (11.6). | "…inhibits an allosteric enzyme early in the pathway." | medium |
| essential amino acids | Correct but omits the course count (ten, arginine counted). | Add "this course counts ten (arginine included)". | low |
| substitution reaction | Example is an alkane (taught 2.7) but the pointer is 3.7 (benzene). | Move pointer to 2.7 (see section 4). | medium |
| ketone bodies | "used as fuel by the brain and muscle" reads as if all three are fuels; acetone is not used (15.5: acetoacetate and β-hydroxybutyrate are the fuels). | Optional: "acetoacetate and β-hydroxybutyrate are used as fuel…". No edit proposed. | low |
| allosteric enzyme, allosteric regulation | Defines only the first headword. | Optional: add "; this kind of control is allosteric regulation". No edit proposed. | low |
| omega-3 fatty acid, omega-6 fatty acid, omega number | Defines the omega number ("A label…"), not the two fatty-acid classes. | Optional: add "omega-3: first C=C at carbon 3 from the CH₃ end; omega-6: at carbon 6". No edit proposed. | low |
| lipid | Correct, but the hydrolyzable / non-hydrolyzable sort that CONVENTIONS.md lists (9.1, 9.6) appears nowhere in the glossary. | Add the missing headword (section 5). | high |

No circular definitions found. "aminotransferase = an enzyme that catalyzes transamination" leans on another entry, but that entry is defined independently. Everything else read as correct at GOB level.

## 4. Pointer problems (13 of 329)

Wrong or clearly better elsewhere:

| Headword | Current | Better | Evidence | Confidence |
|---|---|---|---|---|
| alkane | 2.1 | 2.2 | 2.1 has the word once, in a lab note. 2.2 "Structures and Names of Alkanes" teaches it. | high |
| hydrocarbon | 2.1 | 1.6 | One passing mention in 2.1; defined in bold in 1.6. | high |
| digestion | 13.1 | 13.3 | 13.3 is "Digestion (Stage I of Catabolism)" (28 uses); 13.1 only names the stage. | high |
| Cori cycle | 13.4 | 13.8 | 13.4 itself says "the Cori cycle, Section 13.8". | high |
| condensed structural formula | 2.2 | 2.4 | In 2.2 it is only a table heading; 2.4 is "Condensed Structural and Line-Angle Formulas" (1.7 introduces it). | high |
| molecular formula | 2.2 | 1.7 | Table heading only in 2.2; defined in bold in 1.7. | medium |
| substitution reaction | 3.7 | 2.7 | 2.7 introduces the reaction type in bold; the definition's example is an alkane. | medium |
| mitochondrial matrix | 14.1 | 14.2 | One passing mention in 14.1; 14.2 describes the two compartments of the mitochondrion. | medium |
| DNA, deoxyribonucleic acid | 12.3 | 12.2 | The definition is the double-helix structure, taught in 12.2 "Nucleic Acid Structure"; 12.3 is replication. | medium |
| anticodon | 12.6 | 12.5 | 12.5 has the anticodon learning objective and 16 uses; 12.6 uses it in translation. 12.6 is defensible. | low |
| ATP synthase | 14.2 | 14.4 | Named in the 14.2 overview, taught in 14.4 (chemiosmotic model and electron transport chain already point to 14.4). | low |
| coenzyme Q, ubiquinone | 14.2 | 14.4 | Same. | low |
| cytochrome | 14.2 | 14.4 | Same. | low |

Looked odd but are acceptable (the section defines the term, a later section goes deeper): alcohol, phenol, thiol → 4.1 (functional-group overview; depth in 4.2, 4.7, 4.9); essential amino acids → 10.1 (bold definition there; 15.11 goes deeper); lipoprotein → 9.6; oxaloacetate → 14.2; introns, exons → 12.4; amphipathic → 9.2 (one unbolded use, but it is the defining one); hydroxyl group → 4.1 (single use).

Method: for each entry, every headword variant was counted in the text of the linked page and of every other content section, bold uses were noted, and every entry with zero or few hits, or with more or bolded hits elsewhere, was read in context. The two zero-hit results (α helix in 10.7, frameshift mutation in 12.7) were false alarms caused by a hyphen and by "frameshift" standing alone; both pointers are right.

## 5. Missing headwords (15 most valuable) and duplicates

| # | Proposed headword | Español | Taught in | Why |
|---|---|---|---|---|
| 1 | protein | proteína | 10.4 | 892 uses in 86 pages; the >40 aa convention has no entry (only fibrous / globular protein exist). |
| 2 | oligopeptide | oligopéptido | 10.4 | Completes the 2–20 / 21–40 / >40 convention. |
| 3 | hydrolyzable lipid, non-hydrolyzable lipid (saponifiable, nonsaponifiable) | lípido hidrolizable (saponificable), lípido no hidrolizable (insaponificable) | 9.1, 9.6 | A listed course convention with no entry. |
| 4 | catalyst | catalizador | 11.1 (first used 3.4) | 100 uses in 27 pages; the enzyme entry depends on it. |
| 5 | kinase, phosphorylation | cinasa (quinasa), fosforilación | 11.7 | "kinase" 225 uses, "phosphorylation" 99; used inside two glossary definitions without an entry. |
| 6 | substituent | sustituyente | 2.5 | 118 uses in 22 pages; core naming word. |
| 7 | cytosol | citosol | 13.1 | A listed convention ("cytosol" for glycolysis and lipogenesis); 72 uses. |
| 8 | dehydrogenase | deshidrogenasa | 11.1 | 178 uses in 33 pages. |
| 9 | hormone | hormona | 13.9 | 167 uses; insulin, glucagon and prostaglandins are defined with it. |
| 10 | epimers | epímeros | 8.2 | Bold in 8.2, 8.8, 13.6; sits beside enantiomers / diastereomers. |
| 11 | elimination reaction | reacción de eliminación | 2.7 | One of the three reaction types introduced in 2.7; addition and substitution have entries. |
| 12 | NADPH | NADPH | 13.6 | 78 uses; appears in three glossary definitions. |
| 13 | template strand, coding strand | cadena molde, cadena codificante | 12.4 | A listed convention (12.4). |
| 14 | insertion mutation, deletion mutation (with missense, nonsense, silent) | mutación por inserción, mutación por deleción (de sentido erróneo, sin sentido, silenciosa) | 12.7 | Convention separates these from point mutation; frameshift has an entry, its causes do not. |
| 15 | substrate-level phosphorylation | fosforilación a nivel de sustrato | 13.5 | Bold in 13.2, 13.5, 14.5; the contrast to oxidative phosphorylation, which has an entry. |

Runners-up: amylose and amylopectin (8.7), glycerol (4.6 / 9.2), oxidizing agent and reducing agent (5.4), positional / skeletal / functional group isomers (2.3, 5.5), stop codon and start codon (12.6), VLDL (15.1), pyruvate dehydrogenase complex (14.1), antioxidant (11.5), epinephrine (7.11).

The Spanish for these new terms is my proposal and falls under the same native-speaker check (cinasa vs quinasa and deleción vs supresión vary by country).

**Duplicates:** no headword or variant appears in two entries. Near-duplicates that are fine as separate entries: acid hydrolysis / amide hydrolysis / hydrolysis / saponification; eicosanoids / prostaglandins; ketosis / ketoacidosis; fat / triacylglycerol; coenzyme A / acetyl CoA. The one overlap worth a look is **acid hydrolysis** and **amide hydrolysis**, which both describe acid hydrolysis of an amide and both point to 7.7; acid hydrolysis of an ester is taught in 6.8.

## 6. Proposed find/replace edits

29 edits. Each `old` string was copied from the raw HTML of pages/live/488232.html and verified to occur exactly once; the set was also verified to apply in sequence without collisions. The condensed-structural-formula entry carries its Spanish and pointer change in one edit because the two overlap. Pointer edits change both the href page id and the "Section x.y" label. Missing-headword rows are not included (they are new rows, not replacements).

```json
[
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> rancidez oxidativa, rancidez hidrol&iacute;tica</span>",
  "new": "Espa&ntilde;ol:</em> rancidez, rancidez oxidativa, rancidez hidrol&iacute;tica</span>",
  "reason": "Headword lists three terms (rancidity, oxidative, hydrolytic); Spanish omitted the bare term.",
  "confidence": "high"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> ARN ribos&oacute;mico, ARNr</span>",
  "new": "Espa&ntilde;ol:</em> ARN ribosomal (ribos&oacute;mico), ARNr</span>",
  "reason": "Latin American textbooks mostly use \"ARN ribosomal\"; \"ribosómico\" is the RAE/Spain-preferred form. Give both.",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> tetra&eacute;drico</span>",
  "new": "Espa&ntilde;ol:</em> tetra&eacute;drica</span>",
  "reason": "Gender consistency with the sister entry \"trigonal plana\" (both agree with geometría/forma).",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> l&aacute;mina &beta; plegada (beta)</span>",
  "new": "Espa&ntilde;ol:</em> l&aacute;mina &beta; (beta) plegada, hoja &beta; plegada</span>",
  "reason": "Gloss \"(beta)\" should follow the letter as in \"hélice α (alfa)\"; \"hoja plegada\" is the common Latin American textbook variant.",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> par solitario, par no enlazante</span>",
  "new": "Espa&ntilde;ol:</em> par solitario, par libre, par no enlazante</span>",
  "reason": "\"Par libre / par no compartido\" is the more common term in Latin American general-chemistry texts; keep \"par solitario\".",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> disulfuro, enlace disulfuro</span>",
  "new": "Espa&ntilde;ol:</em> disulfuro, enlace disulfuro (puente disulfuro)</span>",
  "reason": "\"Puente disulfuro\" is the usual biochemistry term for the protein cross-link.",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> anemia de c&eacute;lulas falciformes, drepanocitosis</span>",
  "new": "Espa&ntilde;ol:</em> enfermedad de c&eacute;lulas falciformes, anemia de c&eacute;lulas falciformes (drepanocitosis)</span>",
  "reason": "Match the two English headwords in order (disease, anemia); keep the clinical synonym.",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> ion de amonio cuaternario</span>",
  "new": "Espa&ntilde;ol:</em> ion amonio cuaternario</span>",
  "reason": "Consistency with \"ion carboxilato\" (apposition, no \"de\"); both forms occur in print.",
  "confidence": "low"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> reserva de amino&aacute;cidos</span>",
  "new": "Espa&ntilde;ol:</em> reserva de amino&aacute;cidos (pool de amino&aacute;cidos)</span>",
  "reason": "Many Spanish-language biochemistry texts keep \"pool\" or say \"fondo común de aminoácidos\"; add the form students will meet.",
  "confidence": "low"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> &aacute;cido graso omega-3, omega-6</span>",
  "new": "Espa&ntilde;ol:</em> &aacute;cido graso omega-3, &aacute;cido graso omega-6, n&uacute;mero omega</span>",
  "reason": "Match the three English headwords.",
  "confidence": "low"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> modelo de ajuste inducido</span>",
  "new": "Espa&ntilde;ol:</em> modelo de ajuste inducido, ajuste inducido</span>",
  "reason": "Match the two English headwords.",
  "confidence": "low"
 },
 {
  "page_id": 488232,
  "old": "A long chain of amino acids joined by peptide bonds.<br />",
  "new": "A chain of amino acids joined by peptide bonds. In this course&rsquo;s size ranges an oligopeptide has 2&ndash;20 amino acids, a polypeptide 21&ndash;40 and a protein more than 40; the word is also used for any one chain of a protein.<br />",
  "reason": "CONVENTIONS.md / Section 10.4: polypeptide = 21-40 aa, protein > 40. \"A long chain\" contradicts the taught ranges.",
  "confidence": "high"
 },
 {
  "page_id": 488232,
  "old": "An alcohol with two &ndash;OH groups, such as ethylene glycol and propylene glycol.<br />",
  "new": "A diol is an alcohol with two &ndash;OH groups; a glycol is a diol with the two &ndash;OH groups on neighboring carbons, such as ethylene glycol and propylene glycol.<br />",
  "reason": "Section 4.6 defines a glycol as a diol with OH groups on adjacent carbons; the glossary treats the two words as exact synonyms.",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "needed regularly; most are coenzymes.<br />",
  "new": "needed regularly; the body turns most of them into coenzymes.<br />",
  "reason": "Vitamins are the starting materials for coenzymes (11.5 table \"links each water-soluble vitamin to its coenzyme\"); they are not themselves the coenzymes.",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "in which its end product inhibits an enzyme early in the pathway.<br />",
  "new": "in which its end product inhibits an allosteric enzyme early in the pathway.<br />",
  "reason": "CONVENTIONS.md: feedback inhibition is taught as allosteric regulation (11.6).",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Amino acids the body cannot make in sufficient amounts and must get from the diet.<br />",
  "new": "Amino acids the body cannot make in sufficient amounts and must get from the diet; this course counts ten (arginine included).<br />",
  "reason": "CONVENTIONS.md: ten essential amino acids, arginine counted (10.1, 15.11).",
  "confidence": "low"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> alcano</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597065\">Section 2.1</a>",
  "new": "Espa&ntilde;ol:</em> alcano</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597066\">Section 2.2</a>",
  "reason": "2.1 mentions alkanes once (lab note); 2.2 \"Structures and Names of Alkanes\" teaches the term.",
  "confidence": "high"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> hidrocarburo</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597065\">Section 2.1</a>",
  "new": "Espa&ntilde;ol:</em> hidrocarburo</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597059\">Section 1.6</a>",
  "reason": "2.1 has one passing mention; 1.6 defines hydrocarbons in bold.",
  "confidence": "high"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> digesti&oacute;n</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597188\">Section 13.1</a>",
  "new": "Espa&ntilde;ol:</em> digesti&oacute;n</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597191\">Section 13.3</a>",
  "reason": "13.3 is \"Digestion (Stage I of Catabolism)\"; 13.1 only names the stage.",
  "confidence": "high"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> ciclo de Cori</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597192\">Section 13.4</a>",
  "new": "Espa&ntilde;ol:</em> ciclo de Cori</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597197\">Section 13.8</a>",
  "reason": "13.4 itself says \"the Cori cycle, Section 13.8\"; 13.8 teaches it.",
  "confidence": "high"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> f&oacute;rmula molecular</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597066\">Section 2.2</a>",
  "new": "Espa&ntilde;ol:</em> f&oacute;rmula molecular</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597060\">Section 1.7</a>",
  "reason": "2.2 only uses the phrase as a table heading; 1.7 defines it in bold.",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> f&oacute;rmula estructural condensada</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597066\">Section 2.2</a>",
  "new": "Espa&ntilde;ol:</em> f&oacute;rmula estructural condensada, f&oacute;rmula semidesarrollada</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597068\">Section 2.4</a>",
  "reason": "Combined edit. Spanish (medium): add \"formula semidesarrollada\", the Mexican/Latin American school name for a condensed formula. Pointer (high): 2.2 only uses the phrase as a table heading; 2.4 \"Condensed Structural and Line-Angle Formulas\" teaches it (1.7 introduces it).",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> reacci&oacute;n de sustituci&oacute;n</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597084\">Section 3.7</a>",
  "new": "Espa&ntilde;ol:</em> reacci&oacute;n de sustituci&oacute;n</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597071\">Section 2.7</a>",
  "reason": "2.7 introduces substitution as a reaction type in bold, and the definition’s own example is an alkane; 3.7 is the second use (benzene).",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> matriz mitocondrial</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597200\">Section 14.1</a>",
  "new": "Espa&ntilde;ol:</em> matriz mitocondrial</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597201\">Section 14.2</a>",
  "reason": "14.1 has one passing mention; 14.2 describes the mitochondrion’s two compartments.",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> anticod&oacute;n</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597179\">Section 12.6</a>",
  "new": "Espa&ntilde;ol:</em> anticod&oacute;n</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597183\">Section 12.5</a>",
  "reason": "12.5 \"Structure and Function of RNA\" teaches the tRNA anticodon (learning objective, 16 uses); 12.6 uses it. 12.6 is defensible.",
  "confidence": "low"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> ADN, &aacute;cido desoxirribonucleico</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597177\">Section 12.3</a>",
  "new": "Espa&ntilde;ol:</em> ADN, &aacute;cido desoxirribonucleico</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597176\">Section 12.2</a>",
  "reason": "The definition describes the double-helix structure, taught in 12.2 \"Nucleic Acid Structure\"; 12.3 is replication.",
  "confidence": "medium"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> ATP sintasa</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597201\">Section 14.2</a>",
  "new": "Espa&ntilde;ol:</em> ATP sintasa</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597203\">Section 14.4</a>",
  "reason": "14.2 names it in the overview; 14.4 teaches it (with the chemiosmotic model, which already points to 14.4).",
  "confidence": "low"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> coenzima Q, ubiquinona</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597201\">Section 14.2</a>",
  "new": "Espa&ntilde;ol:</em> coenzima Q, ubiquinona</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597203\">Section 14.4</a>",
  "reason": "Same: overview mention in 14.2, taught in 14.4 (electron transport chain entry already points to 14.4).",
  "confidence": "low"
 },
 {
  "page_id": 488232,
  "old": "Espa&ntilde;ol:</em> citocromo</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597201\">Section 14.2</a>",
  "new": "Espa&ntilde;ol:</em> citocromo</span></td><td data-th=\"Image\">&nbsp;</td><td data-th=\"Caption\">&nbsp;</td><td data-th=\"Link\"><a href=\"/@go/page/597203\">Section 14.4</a>",
  "reason": "Same: overview mention in 14.2, taught in 14.4.",
  "confidence": "low"
 }
]
```
