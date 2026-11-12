# ch11-12 round 2 (Tier 3 + Tier 4) — draft notes

Edits: /private/tmp/claude-501/-Users-dan--claude-spares-spare-yBYqzG/5bbb54bb-5ee0-496e-b3e8-7042c11963f4/scratchpad/edits2/ch11-12.json (60 edits, 19 pages).
Builder: /private/tmp/claude-501/-Users-dan--claude-spares-spare-yBYqzG/5bbb54bb-5ee0-496e-b3e8-7042c11963f4/scratchpad/build2_ch11_12.py
Validator: /private/tmp/claude-501/-Users-dan--claude-spares-spare-yBYqzG/5bbb54bb-5ee0-496e-b3e8-7042c11963f4/scratchpad/validate2_ch11_12.py
All edits were drafted against the current live HTML, which already includes the round-1 edits.

## Tier 3 (clinical currency)
- 597181 12.7 HIV text:
  - AZT paragraph: "In the past 10 years…" → "Many other reverse transcriptase inhibitors have been approved since then."
  - Raltegravir paragraph: now "the first drug to block integrase"; integrase inhibitors are a core part of treatment. The raltegravir structure image is kept.
  - "Cocktail" paragraph rewritten: resistance to any single drug; people with HIV take combination therapy, usually an integrase inhibitor plus reverse transcriptase inhibitors, often one pill a day; undetectable viral load and U=U ("cannot pass HIV to sexual partners"); PrEP.
- 597166 11.1: the dated HIV/AIDS paragraph ending "Several of these drugs have now been approved for use by AIDS patients" now says today's HIV drugs block viral enzymes (reverse transcriptase, integrase, protease) and let people with HIV live long, healthy lives. It points to Section 12.7.
- 597182 12.8 applications list:
  - Chymosin: "~60% of hard cheese" → "most cheese made in the US today".
  - Bt crops: grown since the 1990s; the Bt protein is itself an insecticide that is toxic to certain insects but not to people.
  - Interferon: has been used for some cancers, MS and viral hepatitis, and has largely been replaced by newer drugs.
  - Influenza vaccines: most are grown in eggs or cultured cells; one licensed flu vaccine is recombinant, made in insect cells.
  - New list item: CRISPR–Cas9 (a guide RNA base-pairs with the target DNA), with the 2023 FDA approval of Casgevy for sickle cell disease (edited stem cells make fetal hemoglobin).
- 597182 12.8 other text:
  - Fingerprinting paragraph rewritten for modern STR profiling: PCR with fluorescent primers, then separation by size. The restriction-enzyme and radioactive-label steps are removed.
  - Human genome paragraph: adds "last gaps filled in 2022" and replaces "protein recognition site" with "controls when and where genes are turned on".
- 597180 12.6:
  - "Looking Closer: Recombinant DNA Technology" section deleted (the 1980s essay, the EcoRI image, the recombinant-plasmid image and the EcoRI naming note). A one-sentence pointer to Section 12.8 replaces it. The old string runs from the section's span through `<span id="Summary"></span></div>`, so the deleted section `<div>` stays balanced.
  - PKU: brain damage is caused by high phenylalanine (phenylpyruvate is only the name source and the urine marker). Newborn screening is 24–48 h after birth; the diet is lifelong and uses a medical formula. The IQ statistics are removed; the 1 in 12,000 incidence figure is kept.
  - Cystic fibrosis: "F508del (also written ΔF508)" in the Nursing box, plus one sentence on CFTR modulators (elexacaftor/tezacaftor/ivacaftor). The table cell now reads F508del.
  - Aflatoxin: added to the existing mutagen bullet: made by molds on poorly stored grain and nuts, "which is why crops such as Valley almonds and pistachios are screened for it". No statistics.
- 597184 12.10 and 597185 12.11 (count 2 for the inline answer + answer key): ΔF508 → F508del, for consistency.
- 597169 11.4:
  - Lead: added to the irreversible-inhibitor bullet: "In California, lead poisoning has also been traced to some imported candies, spices, glazed pottery, and traditional remedies such as greta and azarcón."
  - Methanol: the competitive row now lists fomepizole (first choice) or ethanol (older alternative). The same wording is in 597173 11.8 Key Idea 4 and 597174 Cumulative 11.3.
  - Methicillin: the penicillin text and the structure-image alt both now say methicillin is an older penicillinase-resistant penicillin no longer used in the US. The image itself is unchanged; no crop was needed.
- 597172 11.7: lactase decline after childhood is the most common pattern worldwide, "including in many Latino, Asian, African and Indigenous families". The lactase persistence sentence is kept.
- 597183 12.9: "first vaccines shipped at −70 °C … thawed vials are used within hours" → mRNA vaccines are shipped and stored cold (some frozen), and the label's storage temperatures and use-by times must be followed.

## Tier 4 (structure and redundancy)
- 597169 11.4: deleted the Ball "Poisons as Enzyme Inhibitors" table (arsenate, iodoacetate, DIFP). The intro sentence that cited it now ends "…bonding covalently to particular enzymes and inactivating them." The DIFP paragraph and the serine–DIFP reaction image are kept, because the organophosphate Valley Connection box says "work exactly like DIFP above". Noncompetitive "(an allosteric site)" → "At a site other than the active site".
- 597170 11.5: deleted both Ball vitamin tables; the sentence that cited them now points to the Lecture Connection tables. The Ball prose (13 vitamins; fat- vs water-soluble polarity; antioxidants) is kept. This removes the "deoxyadenoxylcobalamin" typo and the conflicting B6 entry.
- 597177 12.3:
  - Ball template/coding-strand paragraph → a short summary with a pointer to 12.4. The three replication-vs-transcription differences, Figure 2, Example 2 and Exercise 2 are kept.
  - Deleted: the RNA-types paragraph, the E. coli RNA table, the ribosome paragraph, the tRNA paragraph, the tRNA figure and the cloverleaf paragraph. A pointer to 12.4 and 12.9 replaces them.
  - Answers added to Exercises 1 and 2, as inline `<details>`; this page has no answer-key block.
- 597183 12.9: the four-stage translation list and the polysome paragraph (near-duplicates of 12.5) are replaced by a pointer to 12.5. The "team effort" lead-in and Figure 12.9.3 are kept. The hepatitis B explanation in Example 3 is now one parenthetical sentence.
- 597180 12.6: the genetic-disease table lead-in now says "You do not need to memorize this table; know PKU, sickle cell disease, cystic fibrosis and Tay–Sachs disease."
- 597176 12.2:
  - Missing answers added for items 2, 4 and 6 in the page's existing Ball qandadiv style. The blank answer placeholders are replaced by `<ol start=2>` and `<ol start=4>`; answer 6 = 24.
  - Item 4 reworded: "During transcription, which base in the new RNA pairs with each of these bases in the DNA template?"
  - Exercise 1 and 2 alt text no longer names the bases (it describes the rings and groups instead).
  - "Skills to Develop" → "Learning Objectives".
  - Duplicate Try It removed: I kept "DNA structure and replication" (also linked from 12.12 Practice Games) and deleted "DNA structure and base pairing" in the Lecture Connection. The two drew from the same quiz bank. This deletes a Try It widget, which the general spec forbids, but the coordinator explicitly requested it.
- 597179 12.5:
  - Exercise 4 answer added (Met-Leu-Asn-Cys-Val-Gly).
  - Figure 1 caption and alt now say the drawing is simplified: the synthetase uses ATP → AMP + PPi, not water.
  - "the vast majority of polypeptides do not begin with methionine" → "In many proteins this first methionine is removed…, so the finished protein often does not begin with methionine."
- 597178 12.4: "except that T replaces U" → "except that it has T where the mRNA has U".
- 597181 12.7: duplicate "Career Focus: Genetics Counselor" box deleted, with its photo and credit. The Chapter 12 intro keeps its Career Spotlight. The Professor Tip's sentence "The Career Focus box is background." is removed.
- 597168 11.3: "even a shift of less than one pH unit can denature some enzymes" → "can sharply reduce activity; far from the optimum, the enzyme denatures."
- 597171 11.6: "The slower switches (zymogens, covalent modification, genetic control)" → covalent modification (seconds to minutes), zymogen activation (minutes), genetic control (hours to days), matching 11.7.
- 597175 12.1: "about 3 × 10⁹ nucleotides" → "about 6 billion base pairs: two sets of about 3 billion, one set from each parent".
- 597173 11.8: the learning objective now reads "give an example (a drug or a poison) of each", because the noncompetitive examples taught are poisons.

## Skipped / needs image work
- Image redraw: 597179 Figure 1 (Ball 19.12, fileid 26476) shows "+ H2O" and no ATP. It should show amino acid + tRNA + ATP → aminoacyl-tRNA + AMP + PPi. For now the caption and alt are corrected.
- Image error found: 597176 Exercise 2 (E2c.jpg, fileid 139719). The top base is drawn without the 2-NH2, so as drawn it is hypoxanthine, not guanine. The answer I added assumes the intended G (GTC). Either redraw the base as guanine, or let the answer note the drawing.
- Image (optional): the penicillin structure image (fileid 129751) still includes methicillin. It is now described as an older drug that is no longer used, so cropping it is not required.
- Not done: the 12.3 inline answers have no matching answer-key entries, because the page has no answer key. A full Chapter 12 reorder is a page move and was not attempted.

## Page-move / retitle proposals (not in the JSON)
- Move 12.9 "Structure and Function of RNA" so it follows 12.2 or 12.4, ahead of translation (12.5). Students would then meet RNA structure before translation, and 12.5 could point back to it.
- Optional: retitle 12.3 "Replication and Expression of Genetic Information" → "DNA Replication", since transcription and the RNA types are now taught in 12.4 and 12.9. Its exercises still include one transcription item, so keeping the current title is also fine.
