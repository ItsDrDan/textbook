"""Batch AG (2026-11-14): DRAFT for the author's decision, not published.
Part 1, repeated text still left after batch T: 14.2, 15.5, 15.6 (each cut keeps the other telling on the same page).
Part 2, the low-confidence wording list (CHEMISTRY-AND-ANSWERKEY-ERRATA.md, "not drafted"): of five items, three are
already fixed live (14.3 step 5 wording, 14.4 "-220 kJ/mol", 9.5 "4 to 5 nm"); 7.4 no longer says "is a liquid"
(it says the 3 degree amide "melts far below benzamide", which holds: N,N-dimethylbenzamide melts near 42 C).
Drafted here: the 14.3 NADH rule (adds the aldehyde oxidation of glycolysis step 6) and 10.5 "alkaloid reagents".
Output: tools/batchAG_2026-11-14.json, tools/batchAG_sha_2026-11-14.json, audit/BATCH_AG_REVIEW.md, audit/preview/<id>.html"""
import json, hashlib, re, html
pages, edits = {}, {}
def page(p):
    if p not in pages: pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
    return pages[p][1]
def e(p, old, new, note, why):
    t = page(p); assert t.count(old) == 1, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note, 'why': why})

# ---------- 14.2 (597201) ----------
e('597201', 'is the beginning of Stage 3 of catabolism.', 'is the beginning of Stage III of catabolism.',
  '14.2 numbering: "Stage 3" to "Stage III"', 'The page title and 13.3, 13.4, 14.1 and 15.4 use Roman Stage I, II, III for the stages of catabolism.')
e('597201', 'The lecture&rsquo;s one-line summary of Stage 3:', 'The lecture&rsquo;s one-line summary of Stage III:',
  '14.2 numbering: "Stage 3" to "Stage III" (Lecture Connection)', 'Same as above.')
e('597201', ' Coenzyme Q, a small fat-soluble molecule, carries the electrons from Complex I or II to Complex III. Cytochrome c, a small protein, carries them one at a time from Complex III to Complex IV. Complex IV (cytochrome oxidase) hands the electrons, together with H<sup>+</sup>, to O<sub>2</sub>, the last electron acceptor,',
  ' Two mobile carriers move them between the complexes (the Lecture Connection below gives the full route). Complex IV (cytochrome oxidase) hands the electrons, together with H<sup>+</sup>, to O<sub>2</sub>, the last electron acceptor,',
  '14.2 cut: the coenzyme Q and cytochrome c route is told twice', 'The Lecture Connection ("Electron transport: the order of appearance") gives the same route with more detail (what each carrier is, and the one-line order), so the section text now points to it.')
e('597201', 'Use these values on exams: NADH + H<sup>+</sup> &rarr; NAD<sup>+</sup> + 2.5 ATP, FADH<sub>2</sub> &rarr; FAD + 1.5 ATP, GTP = 1 ATP, so one acetyl CoA yields <strong>10 ATP</strong> (3 &times; 2.5 + 1.5 + 1) and one glucose yields <strong>32 ATP</strong> (30 with the glycerol-3-phosphate shuttle; older books say 36&ndash;38). The full tally is in Section 14.5.',
  'Use the values in the &ldquo;ATP numbers in this course&rdquo; box at the top of this page on exams; the full glucose tally (32 ATP, or 30 with the glycerol-3-phosphate shuttle) is in Section 14.5.',
  '14.2 cut: the ATP values are told in the top box, the table, the Key Takeaways and this tip', 'The box at the top of the page already gives 2.5 / 1.5 / 1 and 10 per acetyl CoA in the same words; the tip now points to it and keeps only the glucose total.')

# ---------- 15.5 (597213) ----------
e('597213', 'Two acetyl-CoA molecules combine, in a reversal of the final step of &beta;-oxidation, to produce acetoacetyl-CoA. The acetoacetyl-CoA reacts with another molecule of acetyl-CoA and water to form &beta;-hydroxy-&beta;-methylglutaryl-CoA, which is then cleaved to acetoacetate and acetyl-CoA. Most of the acetoacetate is reduced to &beta;-hydroxybutyrate, while a small amount is decarboxylated to carbon dioxide and acetone.</p>',
  'The figure below shows how they are made, and the table in the Lecture Connection classifies each step.</p>',
  '15.5 cut: the steps of ketone body formation are told twice', 'The Lecture Connection table ("Ketogenesis as a four-question table") gives the same three steps and the acetone by-product, classified; the figure right below this paragraph also draws them.')
e('597213', 'breathing becomes labored and very painful.', 'breathing becomes deep and rapid (Kussmaul breathing) as the body tries to blow off CO<sub>2</sub>.',
  '15.5 conflict: "labored and very painful" breathing vs. Kussmaul breathing', 'The Nursing box on the same page describes "deep rapid Kussmaul breathing as the body blows off CO2"; painful breathing is not a recognized sign of ketoacidosis.')
e('597213', ' The 70% figure for the brain applies to prolonged starvation; the point to remember is that the brain, which cannot burn fatty acids, switches to ketone bodies after a few days without carbohydrate.</p>', '</p>',
  '15.5 cut: the brain and ketone bodies is told three times', 'The source text (about 70% in prolonged starvation) and the Lecture Connection paragraph "Who uses them?" (after two to three days of fasting) already say it.')

# ---------- 15.6 (597214) ----------
e('597214', 'Two molecules can play roles in moving it to the cytosol &ndash; citrate and acetylcarnitine. Joining of oxaloacetate with acetyl-CoA in the mitochondrion creates citrate which moves across the membrane, followed by action of citrate lyase in the cytosol of the cell to release acetyl-CoA and oxaloacetate. Additionally, when free acetyl-CoA accumulates in the mitochondrion, it may combine with carnitine and be transported out to the cytosol. </p>',
  'It travels as citrate: oxaloacetate and acetyl-CoA join in the mitochondrion to make citrate, which crosses the membrane, and citrate lyase in the cytosol splits it back into acetyl-CoA and oxaloacetate.</p>',
  '15.6 conflict: two routes out of the mitochondrion (citrate and acetylcarnitine) vs. one in the Lecture Connection', 'The Lecture Connection teaches only the citrate route (the citrate&ndash;malate shuttle), which is the route that supplies fatty acid synthesis; the acetylcarnitine sentence is cut so the page tells one story.')
e('597214', '<p>The fatty acid chain is built two carbons at a time (opposite of beta-oxidation), beginning with two acetyl-CoA molecules. One is converted to malonyl-CoA by carboxylation, catalyzed by the enzyme acetyl-CoA carboxylase (ACC). Next, both acetyl-CoA and malonyl-CoA have their CoA portions replaced by a carrier protein known as ACP (acyl carrier protein) to form acetyl-ACP and malonyl-ACP. Joining acetyl-ACP with malonyl-ACP releases the CO<sub>2</sub> that was added and gives a four-carbon chain, acetoacetyl-ACP (see the figure in the Lecture Connection below).</p>\n\n\n\n<p>From this point forward, the reaction types mirror those of beta-oxidation in reverse order, although the pathway is not beta-oxidation run backward (see the Lecture Connection). First, the ketone is reduced to a hydroxyl using NADPH. Next, water is removed from carbons 2 and 3 of the hydroxyl intermediate to produce a trans double-bonded molecule. Last, the double bond is hydrogenated to yield a saturated intermediate. The process cycles with the addition of another malonyl-ACP to the growing chain until a 16-carbon chain is reached and released as palmitate. At this point, the cytosolic synthesis ceases. </p>',
  '<p>The fatty acid chain is built two carbons at a time on an acyl carrier protein (ACP), using malonyl-CoA as the donor and NADPH as the reducing agent. Four reactions repeat (condensation, reduction, dehydration, reduction) until a 16-carbon chain is released as palmitate. The Lecture Connection below shows how the starting complexes are made and classifies each reaction.</p>',
  '15.6 cut: the start-up and the four elongation reactions are told twice', 'The Lecture Connection ("Getting started" and the "Chain elongation" table, with the figure) gives every step with more detail; the section text becomes a short overview that points to it.')
e('597214', ', and the phosphorylation of acetyl CoA carboxylase are background', ' are background',
  '15.6 conflict: the tip calls ACC phosphorylation "background" while the section text teaches it', 'The "Enzymes of Fatty Acid Synthesis" paragraph teaches that glucagon and epinephrine switch ACC off by adding a phosphate (covalent modification, Chapter 11), so the tip no longer tells students to skip it.')
e('597214', ' insulin also activates acetyl CoA carboxylase, while glucagon and epinephrine inhibit it. At the same time', ' at the same time',
  '15.6 cut: ACC regulation is told three times', 'The "Enzymes of Fatty Acid Synthesis" paragraph and the comparison table row "Key regulated enzyme" already say it.')
e('597214', 'Longer fatty acids are made from palmitate by special enzymes that add C<sub>2</sub> units, and unsaturated fatty acids are made by an oxidation step that requires O<sub>2</sub>. ', '',
  '15.6 cut: elongation and desaturation are told twice', 'The "Elongation" and "Desaturation" headings in the section text, and the Summary, already cover them.')

# ---------- 14.3 (597202): NADH rule ----------
e('597202', ') conversion. These oxidations produce \\(\\ce{NADH}\\).',
  ') conversion, or aldehyde to acid-level conversion (glycolysis step 6, where glyceraldehyde 3-phosphate becomes 1,3-bisphosphoglycerate). These oxidations produce \\(\\ce{NADH}\\).',
  '14.3 rule: "all other oxidations" left out glycolysis step 6', 'Glycolysis step 6 oxidizes an aldehyde to an acyl phosphate (the acid oxidation level) and makes NADH (Section 13.5); it is neither alcohol to carbonyl nor ketone to thioester, so the sentence was not true as written.')

# ---------- 10.5 (597158): alkaloid reagents ----------
e('597158', 'Alkaloid reagents, such as tannic acid (used in tanning leather)</td>', 'Tannic acid and similar polyphenols (used in tanning leather)</td>',
  '10.5 wording: "alkaloid reagents"', '"Alkaloid reagent" is an old name for reagents that precipitate alkaloids; students will not meet it elsewhere. The row keeps tannic acid, which is what the lab (Experiment 12) uses.')
e('597158', 'These reagents combine with positively charged amino groups in proteins to disrupt ionic bonds.</td>', 'Their many &ndash;OH groups hydrogen bond to the protein, and they also bind positively charged amino groups, disrupting the protein&rsquo;s own hydrogen bonds and ionic bonds so it clumps and precipitates.</td>',
  '10.5 wording: how tannic acid denatures', 'Tannins bind proteins mainly through hydrogen bonds from their phenol &ndash;OH groups (and hydrophobic contacts), not only through ionic bonds; the cell now says both.')

h = lambda s: hashlib.sha256(s.encode()).hexdigest()
sha = {p: {'before': h(v[0]), 'after': h(v[1])} for p, v in pages.items()}
for p, v in pages.items(): open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(v[1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAG_2026-11-14.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAG_sha_2026-11-14.json', 'w'))
plain = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'\\\(|\\\)|\\ce\{|<[^>]+>', '', s))).strip()
names = {'597201': '14.2 Stage III of Catabolism', '597213': '15.5 Ketone Bodies and Ketoacidosis', '597214': '15.6 Biosynthesis of Fatty Acids', '597202': '14.3 Citric acid cycle', '597158': '10.5 Proteins'}
out = ['# Batch AG review (draft, not published)', '', 'Each row: what changes, why, then the text before and after. Approve all, or name rows to drop or reword.', '']
k = 0
for p, es in edits.items():
    out.append('## ' + names[p]); out.append('')
    for x in es:
        k += 1
        out += ['**%d. %s**' % (k, x['note']), '', 'Why: ' + html.unescape(x['why']), '', '- Before: ' + plain(x['old'])[:900], '- After: ' + (plain(x['new'])[:900] or '(removed)'), '']
words = {p: len(plain(v[0]).split()) - len(plain(v[1]).split()) for p, v in pages.items()}
out.insert(3, 'Words removed per page: ' + ', '.join('%s %d' % (names[p].split()[0], w) for p, w in words.items()) + '.\n')
open('audit/BATCH_AG_REVIEW.md', 'w').write('\n'.join(out))
print(k, 'edits on', len(edits), 'pages;', words)
