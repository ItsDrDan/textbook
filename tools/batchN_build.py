"""Batch N: the rows of tools/REVIEW_2026-11-13.md that batch M left undrafted and that need no instructor decision.
DRAFT ONLY until the instructor approves. Count-checked against pages/live (which matches the live book after batch M).
Not here: anything that needs a decision, a source, a new drawing or an image check (listed in the review addendum).
Output: tools/batchN_2026-11-13.json {uploads, edits:{pageid:[{old,new,count,note}]}}"""
import json, re

L = 'pages/live/'
pages, edits, uploads = {}, {}, []


def page(p):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read()
    return pages[p]


def e(p, old, new, note, n=1):
    t = page(p); assert t.count(old) == n, (p, note, t.count(old))
    assert old != new, (p, note)
    pages[p] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


A = lambda pid, sec: f'<a style="text-decoration:underline" href="/@go/page/{pid}">{sec}</a>'

# ---------------- Tier 1 / 2 ----------------
e('597073', 'because it forms explosive mixtures with air at nearly all concentrations.',
  'because it forms explosive mixtures with air and, especially, with the oxygen used in anesthesia.', 'T1 2.9: cyclopropane is explosive over a wide range in oxygen, not at nearly all concentrations in air')
e('597061', 'Covalent compounds do not ionize when they dissolve: the molecule stays whole, just surrounded by solvent.',
  'Most covalent compounds do not ionize when they dissolve: the molecule stays whole, just surrounded by solvent (acids and amines are the exceptions, Chapters 6 and 7).',
  'T1 1.8: carboxylic acids and amines do ionize')
e('597063', 'Molecular compounds do not ionize in water (C), and ionic bonding',
  'Most molecular compounds do not ionize in water (C); the acids and amines of Chapters 6 and 7 are the exceptions. Ionic bonding', 'T1 P1.65 (inline and key): same', n=2)
e('597057', '<strong>treat C&ndash;H as nonpolar, always</strong>.',
  '<strong>treat C&ndash;H as nonpolar, always</strong>. In the same way, C&ndash;Br falls just under the 0.4 line on the chart, but every carbon&ndash;halogen bond is treated as polar.',
  'T2 1.4 tip: C-Br is listed as polar although its difference on the chart is under 0.4')
e('597070', '<strong>Branching lowers them</strong>: branched molecules cannot pack as tightly together as straight chains, so there is less contact and less dispersion force between neighbors.',
  '<strong>Branching lowers the boiling point</strong>: branched molecules have less surface contact with their neighbors than straight chains, so there is less dispersion force between them. (Melting points are less regular, because compact, symmetrical molecules can pack well in a crystal.)',
  'T2 2.6: branching reliably lowers boiling points, not melting points')
e('597164', '<p>At pH 7.4 an amino acid is a <strong>zwitterion</strong>:', '<p>At pH 7.4 an amino acid with a neutral R group is a <strong>zwitterion</strong>:',
  'T2 10.11 Key Idea 2: true only for a neutral R group (Key Idea 6)')
e('597094', 'Each step removes hydrogen (oxidation), just as ethanol', 'Each step is an oxidation (more C&ndash;O bonds, fewer C&ndash;H bonds), just as ethanol',
  'T2 4.5 Valley answer (inline and key): HCHO to HCOOH adds O', n=2)
e('597101', '<td>about 7 g/100 mL</td>', '<td>about 8 g/100 mL</td>', 'T2 P4.53: 4.8 and Cumulative 4.4 say about 8 g', n=2)
e('597199', '<strong>peptide hormones</strong> (proteins, Chapter 10).', '<strong>peptide hormones</strong> (chains of amino acids, Chapter 10).',
  'T2 Cumulative 13.4 (inline and key): glucagon, 29 aa, is a polypeptide by 10.4', n=2)

# ---------------- Tier 3: numbering and captions ----------------
# 1.5: Example 1 / Exercise 1 were each used twice
def renum(p, kind, frm, to, which, note):
    """Renumber the which-th (0-based) '<kind> \\(\\PageIndex{frm}\\)' legend, using the 130 characters before it to make the match unique."""
    t = page(p); lab = f'{kind} \\(\\PageIndex{{{frm}}}\\)'
    pos = [m.start() for m in re.finditer(re.escape(lab), t)]
    i = pos[which]; old = t[i - 130:i + len(lab)]
    new = old[:-len(lab)].replace(f'PageIndex.7B{frm}.7D.5C)_2', f'PageIndex.7B{to}.7D.5C)').replace(f'PageIndex.7B{frm}.7D', f'PageIndex.7B{to}.7D') + f'{kind} \\(\\PageIndex{{{to}}}\\)'
    e(p, old, new, note)


renum('597058', 'Example', 2, 3, 0, 'T4 1.5: third example renumbered 3')
renum('597058', 'Exercise', 2, 3, 0, 'T4 1.5: third exercise renumbered 3')
renum('597058', 'Example', 1, 2, 1, 'T4 1.5: second "Example 1" is now Example 2')
renum('597058', 'Exercise', 1, 2, 1, 'T4 1.5: second "Exercise 1" is now Exercise 2')
e('597058', '<strong>Exercise 1.5.1</strong></p><div><p>Focus on the central atom, N.', '<strong>Exercise 1.5.2</strong></p><div><p>Focus on the central atom, N.',
  'T4 1.5 print key: the answer belongs to the renumbered Exercise 2')
e('597061', '<h4 class="box-legend editable">Effect of Hydrogen Bonding on Boiling Points</h4>',
  '<h4 class="box-legend editable">Example \\(\\PageIndex{2}\\): Effect of Hydrogen Bonding on Boiling Points</h4>', 'T4 1.8: this example had no number (1, -, 3, 4)')
for p, sec, caps in (('597196', '13.7', ['Steps of glycogen metabolism: enzymes and reaction types', 'Glycogenesis versus glycogenolysis']),
                     ('597197', '13.8', ['The four bypasses of gluconeogenesis', 'Signals that switch between glycolysis and gluconeogenesis'])):
    for i, c in enumerate(caps, 1):
        new = 'Steps of glycogenesis: enzymes and reaction types' if c.startswith('Steps of glycogen metabolism') else c
        e(p, f'<caption>{c}</caption>', f'<caption>Table {sec}.{i}: {new}</caption>', f'T3 {sec}: the text cites Table {i}; the caption had no number')
e('597091', '1,2-Ethanediol and propane-1,2,3-triol are shown to highlight rule 3<br />', 'Ethane-1,2-diol and propane-1,2,3-triol are shown to highlight rule 3.<br />',
  'T4 4.2 Figure 1: name style matches the figure; final period')
e('597103', '<figcaption>Figure \\(\\PageIndex{2}\\) Some Interesting Aldehydes.', '<figcaption>Figure \\(\\PageIndex{2}\\): Some Interesting Aldehydes.', 'T4 5.2 Figure 2: missing colon')
e('597104', 'Le Ch&acirc;telier&rsquo;s principle', 'Le Chatelier&rsquo;s principle', 'T4 5.3: one spelling throughout (Chapter 4 uses Le Chatelier)')

# ---------------- Tier 4: cross-references, links, wording ----------------
e('597206', 'when the chain cannot (Section <a href="/@go/page/597193">13.5</a>).', 'when the chain cannot (Section <a href="/@go/page/597192">13.4</a>).',
  'T4 Case Set 14.3 (inline and key): lactate is taught in 13.4', n=2)
e('597165', 'not 0. Review: Section 10.2.', 'not 0. Review: Sections 10.2 and 10.4.', 'T4 P10.81 (inline and key): peptide net charge is taught in 10.4', n=2)
e('597102', '(an alcohol and a carboxylic acid, with no ketone despite its name)', '(an alcohol and a carboxylic acid; it has no ketone group even though it is called a ketone body)',
  'T4 5.1: the name has no "ketone" in it')
e('597193', '<p>The ten reactions of glycolysis are the following (<em>copyright: modified from a Public Domain resource at <a title="https://it.Wikipedia.org/wiki/Glicolisi" href="https://it.Wikipedia.org/wiki/Glicolisi" target="_blank" rel="external noopener nofollow" class="link-https">Wikipedia</a></em>.)</p>',
  '<p>The ten reactions of glycolysis are the following. (Step list adapted from a public-domain resource at <a title="https://it.Wikipedia.org/wiki/Glicolisi" href="https://it.Wikipedia.org/wiki/Glicolisi" target="_blank" rel="external noopener nofollow" class="link-https">Wikipedia</a>.)</p>',
  'T4 13.5: leftover "copyright:" prefix')
e('597130', 'Adipic acid is a carboxylic acid with two carboxyl groups on either end of the molecule. Hexanediamine has amino groups on either end of a six-carbon chain.',
  'Adipic acid is a dicarboxylic acid, with a carboxyl group on each end of the molecule. Hexanediamine has an amino group on each end of a six-carbon chain.', 'T4 7.10: read as four groups')
e('597130', 'give nylon-66, drawn as', 'give nylon-6,6, drawn as', 'T4 7.10 alt: one spelling, nylon-6,6 (as in the Lecture Connection and P7.59)')
e('597130', 'is a polyamide called nylon-66. Nylon-66 was first invented in 1935 and has been used in all sorts of products. Polyamides, including nylon-66,',
  'is a polyamide called nylon-6,6. Nylon-6,6 was first invented in 1935 and has been used in all sorts of products. Polyamides, including nylon-6,6,', 'T4 7.10: nylon-6,6')
e('597126', 'alt="Formation of nylon 66:', 'alt="Formation of nylon-6,6:', 'T4 7.6 alt: nylon-6,6')
e('597177', '(can also be written as <span class="acronym-ignore">TCAACTCATGGA</span>)', '(can also be written as 5&prime;&#8209;<span class="acronym-ignore">TCAACTCATGGA</span>&#8209;3&prime;)',
  'T4 12.3 Example 1: label the ends (12.2 convention)')
e('597178', 'mRNA codon GCA is complementary to the anticodon UGC on a tRNA shown in', 'mRNA codon 5&prime;&#8209;GCA&#8209;3&prime; is complementary to the anticodon 3&prime;&#8209;CGU&#8209;5&prime; on the tRNA shown in',
  'T4 12.4: ends labelled; written to line up with the codon (12.5 and P12.39 write it 3\'-CGU-5\')')
e('597136', '<a title="Exemplars_and_Case_Studies/ChemCases/Nutrasweet" mt-page-link-identifier="f906dce861ce4702a704ea04fb1bcaaf" href="/Ancillary_Materials/Exemplars_and_Case_Studies/Case_Studies/Nutrasweet">sucralose</a>',
  'sucralose', 'T4 8.3: "sucralose" linked to a NutraSweet (aspartame) case study')
e('597159', 'a medical condition called sickle cell anemia, illustrated in the figure on the right.', 'a medical condition called sickle cell anemia, illustrated in the figure here.',
  'T4 10.6: left/right fails in print')
e('597160', 'as illustrated in the model shown on the left.', 'as illustrated in the model shown here.', 'T4 10.7: left/right fails in print')
e('597160', 'pointing toward the C-terminus, as shown on the right.', 'pointing toward the C-terminus, as shown here.', 'T4 10.7: same')
# 3.8: body paragraph was wrapped in a stray bullet
t = page('597085'); i = t.index('<ul>\n    <li>\n    <div class="informalfigure large">Sometimes an aromatic group'); j = t.index('</ul>', i) + len('</ul>')
old = t[i:j]; body = re.search(r'<div class="informalfigure large">(.*?)</div>', old, re.S).group(1)
e('597085', old, '<p>' + body + '</p>', 'T4 3.8: paragraph was inside a stray bullet')
e('597067', 'Next beyond C<sub>4</sub>H<sub>10</sub> in the homologous series is pentane. Each compound has the same molecular formula: C<sub>5</sub>H<sub>12</sub>.',
  'Next beyond C<sub>4</sub>H<sub>10</sub> in the homologous series is C<sub>5</sub>H<sub>12</sub>, which has three isomers, shown in the figure below.', 'T4 2.3: garbled source sentence')
e('597067', 'The compound at the far left is pentane', 'The compound on the left of the figure is pentane', 'T4 2.3: the figure follows the paragraph')
# 12.10: Health Career Connection box split Key Ideas 9 and 10; move it below Key Idea 10
t = page('597184'); i = t.index('<div class="box-note">\n<p class="boxtitle">Health Career Connection</p>'); j = t.index('</div>', i) + len('</div>')
box = t[i:j]; assert box.count('<div') == 1
k = t.index('<h3 class="editable">10. Recombinant DNA (overview)</h3>'); k2 = t.index('</p>', k) + len('</p>')
old = t[i:k2]; assert t[j:j + 2] == '\n\n'
new = t[j + 2:k2] + '\n\n' + box
e('597184', old, new, 'T4 12.10: Health Career Connection box moved below Key Idea 10 (it split the numbered summary)')

# Glossary and Index pointers to the teaching section
for term_old, term_new, why in (
    ('<a href="/@go/page/597169">Section 11.4</a>', '<a href="/@go/page/597171">Section 11.6</a>', 'allosteric'),
    ('<a href="/@go/page/597203">Section 14.4</a>', '<a href="/@go/page/597194">Section 13.6</a>', 'reactive oxygen species'),
    ('<a href="/@go/page/597095">Section 4.6</a>', '<a href="/@go/page/597094">Section 4.5</a>', 'alcohol dehydrogenase')):
    t = page('488232')
    head = {'allosteric': '>allosteric enzyme, allosteric regulation</td>', 'reactive oxygen species': '>reactive oxygen species</td>', 'alcohol dehydrogenase': '>alcohol dehydrogenase</td>'}[why]
    i = t.index(head); j = t.index('</tr>', i); row = t[i:j]; assert row.count(term_old) == 1
    e('488232', row, row.replace(term_old, term_new), f'T4 Glossary: {why} points to its teaching section')
e('488232', 'formed in small amounts by the electron transport chain; antioxidants protect against them.', 'formed in small amounts during metabolism; antioxidants such as glutathione (kept reduced by NADPH) protect against them.',
  'T4 Glossary: reactive oxygen species defined the way 13.6 uses the term')
e('488231', '<li>allosteric enzyme, 11.4</li>\n<li>allosteric regulation, 11.4</li>', '<li>allosteric enzyme, 11.6</li>\n<li>allosteric regulation, 11.6</li>', 'T4 Index: allosteric, 11.6')
e('488231', '<li>reactive oxygen species, 14.4</li>', '<li>reactive oxygen species, 13.6</li>', 'T4 Index: reactive oxygen species, 13.6')
e('488231', '<li>alcohol dehydrogenase, 4.6</li>', '<li>alcohol dehydrogenase, 4.5</li>', 'T4 Index: alcohol dehydrogenase, 4.5')

# About This Book: the Valley Connection list missed the seven boxes added in batch F
e('597270', A('597071', '2.7') + ' ozone and smog;', A('597070', '2.6') + ' propane tanks; ' + A('597071', '2.7') + ' ozone and smog;', 'T4 About: Valley list adds 2.6')
e('597270', A('597081', '3.4') + ' ethylene and fruit ripening;', A('597081', '3.4') + ' ethylene and fruit ripening; ' + A('597082', '3.5') + ' plastics on the farm;', 'T4 About: adds 3.5')
e('597270', A('597094', '4.5') + ' Valley wine grapes and how the liver oxidizes ethanol;', A('597094', '4.5') + ' Valley wine grapes and how the liver oxidizes ethanol; ' + A('597098', '4.9') + ' garlic and onions;', 'T4 About: adds 4.9')
e('597270', A('597162', '10.9') + ' nitrate in well water', A('597156', '10.3') + ' milk, casein and cheese; ' + A('597162', '10.9') + ' nitrate in well water', 'T4 About: adds 10.3')
e('597270', A('597170', '11.5') + ' almonds and vitamin E;', A('597170', '11.5') + ' almonds and vitamin E, and folic acid in tortillas; ' + A('597180', '12.7') + ' newborn heel-stick screening;', 'T4 About: adds the second 11.5 box and 12.7')
e('597270', A('597213', '15.5') + ' diabetic ketoacidosis.', A('597213', '15.5') + ' diabetic ketoacidosis; ' + A('597215', '15.7') + ' beans and corn tortillas.', 'T4 About: adds 15.7')

# 1.6: captions and text promised molecular models that are not in the images (Figure 1 image checked; the others by their alt text)
e('597059', 'Formulas and Molecular Models of the Four Simplest Alkanes', 'Formulas of the Four Simplest Alkanes', 'T3 1.6 Figure 1 caption: the image shows formulas only (image checked)')
e('597059', 'shows the formulas and the molecular models of the two simplest alkenes', 'shows the formulas of the two simplest alkenes', 'T3 1.6: no models in Figure 2')
e('597059', 'Formulas and Molecular Models of the Two Simplest Alkenes', 'Formulas of the Two Simplest Alkenes', 'T3 1.6 Figure 2 caption')
e('597059', 'Below is the formula and the molecular model of the simplest alkyne', 'Below is the formula of the simplest alkyne', 'T3 1.6: no model in the alkyne image')
e('597059', 'shows their formulas along with a molecular model of each', 'shows their formulas', 'T3 1.6: no models in Figure 4')
e('597059', 'shows the formulas and the molecular models of the two simplest carboxylic acids', 'shows the formulas of the two simplest carboxylic acids', 'T3 1.6: no models in Figure 5')
# 1.6 Exercise 1: alt text was lettered (d)-(g) for items a-d and named the family the student is asked for
e('597059', 'alt="Structure (d): CH3C triple bond CCH3, an alkyne with a carbon-carbon triple bond."', 'alt="Structure (a): CH3-C triple bond C-CH3."', 'T3 1.6 Exercise 1 alt: letter and no giveaway')
e('597059', 'alt="Structure (e): H bonded to a carbon that has a double bond to O and an OH group (methanoic acid, a carboxylic acid)."', 'alt="Structure (b): H bonded to a carbon that has a double bond to O and an OH group."', 'T3 1.6 Exercise 1 alt')
e('597059', 'alt="Structure (f): a five-carbon chain CH3-CH2-CH-CH2-CH3 with an OH group on the middle carbon (an alcohol)."', 'alt="Structure (c): a five-carbon chain CH3-CH2-CH-CH2-CH3 with an OH group on the middle carbon."', 'T3 1.6 Exercise 1 alt')
e('597059', 'alt="Structure (g): CH2=CH-COOH, a C=C double bond next to a carboxylic acid group."', 'alt="Structure (d): CH2=CH-COOH."', 'T3 1.6 Exercise 1 alt')
e('597145', 'a triglyceride (glycerol esterified with three C15H31 fatty acid chains)', 'a triglyceride (glycerol esterified with two palmitic acid chains, (CH2)14CH3, and one stearic acid chain, (CH2)16CH3)',
  'T3 9.2 soap figure alt: the image shows two C16 chains and one C18 chain (image checked)')

# ---------------- "hydride" replaced everywhere (instructor, 2026-11-13); the NaBH4 "hydride reagent" in 5.4 stays ----------------
def ea(p, old, new, note):
    e(p, old, new, note, n=page(p).count(old))


ea('488232', 'NAD<sup>+</sup> accepts a hydride in oxidation reactions and becomes NADH', 'NAD<sup>+</sup> accepts two electrons and an H<sup>+</sup> in oxidation reactions and becomes NADH', 'T2 Glossary NAD+: no "hydride"')
ea('597170', 'Carries a hydride (H<sup>&minus;</sup>) in dehydrogenase reactions;', 'Carries two electrons and an H<sup>+</sup> in dehydrogenase reactions;', 'T2 11.5 table: no "hydride"')
ea('597173', 'NAD<sup>+</sup> (hydride carrier; pellagra)', 'NAD<sup>+</sup> (electron carrier; pellagra)', 'T2 11.8: no "hydride"')
ea('597174', 'accepts two hydrogens (as a hydride and a proton) in oxidation reactions', 'accepts two hydrogens (two electrons and one H<sup>+</sup>; the other H<sup>+</sup> is released) in oxidation reactions', 'T2 11.9: no "hydride" (inline and key)')
ea('597188', 'sits below it ready to accept a hydride."', 'sits below it ready to accept the hydrogen."', 'T2 13.1 Figure 5 alt: no "hydride"')
ea('597194', '(a) It transfers a hydride from C1 of the sugar to NADP<sup>+</sup>:', '(a) It removes hydrogen from C1 of the sugar and passes it to NADP<sup>+</sup>:', 'T2 13.6 Example 4: no "hydride"')
ea('597199', 'NAD<sup>+</sup> accepts a hydride when a C&ndash;OH is oxidized to C=O', 'NAD<sup>+</sup> accepts two electrons and an H<sup>+</sup> when a C&ndash;OH is oxidized to C=O', 'T2 P13.2: no "hydride"')
ea('597199', 'removes a hydride and an H<sup>+</sup>; NAD<sup>+</sup> takes the hydride and becomes NADH.', 'removes two hydrogens (two electrons and two H<sup>+</sup>); NAD<sup>+</sup> takes the two electrons and one H<sup>+</sup> and becomes NADH, and the other H<sup>+</sup> is released.', 'T2 P13.14: no "hydride"')
ea('597201', 'it accepts a <strong>hydride ion</strong> (H<sup>&minus;</sup>: one proton plus two electrons) and becomes NADH;', 'it accepts <strong>two electrons and one H<sup>+</sup></strong> and becomes NADH;', 'T2 14.2: no "hydride"')
ea('597204', 'Lactate dehydrogenase transfers the hydride from NADH to pyruvate,', 'Lactate dehydrogenase transfers the hydrogen from NADH to pyruvate,', 'T2 14.5: no "hydride"')
ea('597206', 'NAD<sup>+</sup> gains a hydride (two electrons and a proton):', 'NAD<sup>+</sup> gains two electrons and a proton:', 'T2 14.7: no "hydride" (inline and key)')

# ---------------- credit lines approved by the instructor, 2026-11-13 ----------------
SLIDE = ' (Figure: Daniel Kwasniewski, CC BY 4.0.)</figcaption>'
BALL = ' (Figure from <em>The Basics of General, Organic, and Biological Chemistry</em> by Ball, Hill and Scott, CC BY-NC-SA 3.0.)</figcaption>'
MALIK = ' (Figure from <em>Introduction to Organic and Biochemistry</em> (Malik), public domain.)</figcaption>'
for p, tail, cr, what in (
    ('597091', 'Common alcohols and phenols from the lecture slides.</figcaption>', SLIDE, '4.2.2 lecture slide'),
    ('597102', 'the 2 is not needed, because the C=O can only be on C2.</figcaption>', SLIDE, '5.1.1 lecture slide'),
    ('597106', 'read the chiral carbon farthest from the C=O.</figcaption>', SLIDE, '5.5.8 lecture slide'),
    ('597112', 'carboxylate salts, from the lecture slides.</figcaption>', SLIDE, '6.4.1 lecture slide'),
    ('597094', 'is carbon 1; a methyl group is on carbon 2.</figcaption>', ' (Structure redrawn by Daniel Kwasniewski, CC BY 4.0.)</figcaption>', '4.5 Exercise 1(b) house redraw'),
    ('597057', 'unequal distribution of electron density throughout a molecule.</figcaption>', BALL, '1.4 Figure 5 (Ball)'),
    ('597169', 'no subsequent reaction occurs while malonate remains bound to the enzyme.</figcaption>', BALL, '11.4 Figure 1 (Ball)'),
    ('597203', 'with the ATP, GTP, NADH and FADH<sub>2</sub> made at each stage.</figcaption>', MALIK, '14.4 Figure 3 (Malik)')):
    e(p, tail, tail[:-len('</figcaption>')] + cr, 'T3 credit line added: ' + what)

json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchN_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
