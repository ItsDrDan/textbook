"""Batch M: draft fixes from the fresh full check of 2026-11-13 (tools/REVIEW_2026-11-13.md).
PUBLISHED 2026-11-13 on the instructor's OK (64 pages; each read back identical). pages/live now holds the post-edit pages,
so this script only re-runs against the pre-batch-M copies (git history).
Items that need a decision, a new drawing or a source check are NOT in this file; see the review's "Not drafted" lists.
Output: tools/batchM_2026-11-13.json {uploads, edits:{pageid:[{old,new,count,note}]}}"""
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


GO = lambda pid: f'/@go/page/{pid}'

# ---------------- Tier 1: wrong facts ----------------
e('597078', '<td data-th="Melting Point (&deg;C)" style="text-align:center;">&ndash;138</td>\n            <td data-th="Boiling Point (&deg;C)" style="text-align:center;">30</td>',
  '<td data-th="Melting Point (&deg;C)" style="text-align:center;">&ndash;165</td>\n            <td data-th="Boiling Point (&deg;C)" style="text-align:center;">30</td>',
  'T1 3.1 Table 1: 1-pentene melts at -165 C, not -138 C')
e('597125', '<td data-th="Boiling Point (&deg;C)" style="text-align:center;">193</td>', '<td data-th="Boiling Point (&deg;C)" style="text-align:center;">210</td>',
  'T1 7.5 Table 1: formamide boils at about 210 C (193 is from the source table)')
e('597061', 'greater than about six times normal atmospheric pressure', 'greater than about five times normal atmospheric pressure',
  'T1 1.8: liquid CO2 needs more than 5.1 atm (triple point)')
e('597098', 'Thiols are responsible for the smells of onions, garlic, rotten eggs and skunk spray,',
  'Thiols and related sulfur compounds are responsible for the smells of onions, garlic and skunk spray (the rotten-egg smell is hydrogen sulfide, H<sub>2</sub>S, which is not a thiol),',
  'T1 4.9: rotten-egg smell is H2S, not a thiol')
e('597109', 'The bites of some ants inject formic acid, and the stings of wasps and bees contain formic acid (as well as other poisonous materials).',
  'The bites and stings of some ants inject formic acid.', 'T1 6.1: bee and wasp venom is mostly peptides and enzymes, not formic acid')
e('597109', '<td>Ant and bee stings; the toxic product', '<td>Ant stings; the toxic product', 'T1 6.1 table: same')
e('597130', 'Its resistance to wrinkling comes from the cross-linking of the polymer strands.',
  'Its resistance to wrinkling comes from its stiff, regular polymer chains, which pack tightly and spring back into shape.',
  'T1 7.10: PET is a linear polymer, not cross-linked')
e('597129', 'they are used as stimulants, anesthetics, and antidepressants, and many are habit forming',
  'they are used as stimulants, anesthetics, and pain relievers, and many are habit forming', 'T1 7.9: none of the alkaloids taught is an antidepressant')
e('597138', 'Five or six OH groups on a six-carbon molecule hydrogen bond strongly with water.', 'Five OH groups on a six-carbon molecule hydrogen bond strongly with water.',
  'T1 8.5: a hexose has five OH groups (matches Cumulative 8.3)')
OLD139 = 'By day three the brain is burning mostly ketone bodies made in the liver from fatty acids. The remaining glucose demand (red cells, some brain) is met by gluconeogenesis'
NEW139 = 'By day three the brain still runs mainly on glucose, now made by gluconeogenesis, while ketone bodies made in the liver from fatty acids supply a growing share (they become its main fuel only after more days of fasting). The glucose demand (red cells, brain) is met by gluconeogenesis'
e('597195', OLD139, NEW139, 'T1 13.9 Exercise 4: matches the page\'s own fed-fasting timeline (inline answer and print key)', n=2)

# ---------------- Tier 2: convention conflicts ----------------
# cofactor (inorganic ion) vs coenzyme (organic, vitamin-derived): 11.5
e('597192', 'also needs a cofactor made from thiamine (vitamin B<sub>1</sub>)', 'also needs a coenzyme made from thiamine (vitamin B<sub>1</sub>)', 'T2 13.4: thiamine pyrophosphate is a coenzyme (11.5)')
e('597188', 'coenzyme A, and the thiamine cofactor of pyruvate dehydrogenase (Section 13.4)', 'coenzyme A, and the thiamine coenzyme (TPP) of pyruvate dehydrogenase (Section 13.4)', 'T2 13.1: coenzyme')
e('597198', 'coenzyme A, and the cofactor of pyruvate dehydrogenase, so a vitamin deficiency', 'coenzyme A, and the thiamine coenzyme (TPP) of pyruvate dehydrogenase, so a vitamin deficiency', 'T2 13.10: coenzyme')
e('597200', 'plus a cofactor made from thiamine (vitamin B<sub>1</sub>).</p>', 'plus a coenzyme made from thiamine (vitamin B<sub>1</sub>).</p>', 'T2 14.1: coenzyme')
e('597200', 'and a cofactor made from thiamine (vitamin B1)."', 'and a coenzyme made from thiamine (vitamin B1)."', 'T2 14.1 Figure 14.1.3 alt: coenzyme')
e('597200', 'Without its thiamine cofactor, pyruvate dehydrogenase', 'Without its thiamine coenzyme, pyruvate dehydrogenase', 'T2 14.1 Nursing box: coenzyme')
e('597205', 'pyruvate dehydrogenase needs its thiamine cofactor;', 'pyruvate dehydrogenase needs its thiamine coenzyme;', 'T2 14.6: coenzyme')
e('597214', '(a ligase, using ATP and a biotin cofactor;', '(a ligase, using ATP and the coenzyme biotin;', 'T2 15.6: biotin is a coenzyme (same page\'s table says so)')
e('597214', 'reduction, dehydration and reduction: roughly &beta;-oxidation run in reverse.</li>',
  'reduction, dehydration and reduction. These mirror the steps of &beta;-oxidation, but the compartment, carrier, coenzyme and hormone signal are all different, so it is not &beta;-oxidation run backward.</li>',
  'T2 15.6 Summary: contradicted the Lecture Connection and 15.12 Common Mistake')
# amine angle ~107 (1.5)
e('597122', 'molecular geometry, bond angles near 109.5&deg;.', 'molecular geometry, bond angles about 107&deg; (a little under the ideal 109.5&deg;).', 'T2 7.2: amine angle about 107 (CONVENTIONS, 1.5)')
e('597133', '(c) About 109.5&deg;, a little less in practice because the lone pair pushes the bonds together.',
  '(c) About 107&deg;, a little less than the ideal 109.5&deg; because the lone pair pushes the bonds together.', 'T2 7.13 P7.76: about 107 (inline and key)', n=2)
# numbers that disagree between pages
e('597094', 'warns that as little as 15 mL can cause blindness', 'warns that as little as 10 mL can cause blindness', 'T2 4.5: 4.4 says 10 mL')
e('597062', 'dimethyl ether (&minus;24 &deg;C)', 'dimethyl ether (&minus;25 &deg;C)', 'T2 1.9 Example 4: 1.8 gives -24.8 C')
e('597113', 'propyl ethanoate (the smell of pears)', 'pentyl ethanoate (pentyl acetate, the smell of pears)', 'T2 6.5: 6.6, 6.7 and 6.11 teach pentyl acetate as the pear ester')
e('597128', 'Adenosine, acetylcholine, and dopamine, the messengers mentioned in Section 7.3, are',
  'Acetylcholine and dopamine, two of the messengers mentioned in Section 7.3, are', 'T2 7.8: 7.11 never mentions adenosine')
# triple bonds missing in condensed formulas
e('597060', '\\(\\ce{CH3CCCH2CH3}\\)', '\\(\\ce{CH3C#CCH2CH3}\\)', 'T2 1.7 Table 3: 2-pentyne condensed formula shows its triple bond (as propyne does)')
e('597060', '\\(\\ce{CH3CH2CCCH2CH2CH2CH2CH3}\\)', '\\(\\ce{CH3CH2C#CCH2CH2CH2CH2CH3}\\)', 'T2 1.7 Table 3: 3-nonyne, same')
# undefined above-level term
e('597086', 'fused benzene rings whose pi electrons are delocalized around the rings', 'fused benzene rings whose double-bond electrons are shared (delocalized) around the rings',
  'T2 3.9 Case Question 3.3: "pi electrons" is never defined (inline and key)', n=2)

# ---------------- Tier 3: figures, captions, alt text ----------------
e('597079', '<em>Models of (left) Cis-2-Butene and (right) Trans-2-Butene.</em>', '<em>Structural formulas of (left) cis-2-butene and (right) trans-2-butene.</em>',
  'T3 3.2 Figure 3: the image is structural formulas; the models are Figure 2')
e('597075', 'alt="Line structure of 2-chloro-3-methylpentane: a five-carbon zigzag with Cl drawn on the second carbon and a methyl branch on the third carbon"',
  'alt="Line structure of a chlorinated alkane: a five-carbon zigzag with Cl drawn on the second carbon and a one-carbon branch on the third carbon"',
  'T3 2.11 P2.72: alt text gave away the name asked for in part (b)')
e('597139', 'OH down on carbon 3, up on carbon 4). A label', 'OH up on carbon 3, down on carbon 4). A label', 'T3 8.6 Figure 8.6.3 alt: fructose OH groups were reversed (checked against Slide43)')
e('597149', 'drawn as a line structure with the carbons numbered, an HO group on carbon 3 at the lower left', 'drawn as a line structure, with an HO group on carbon 3 at the lower left',
  'T3 9.6 Figure 9.6.5 alt: the slide has no carbon numbers (checked against Slide50)')
e('597193', '(Figure: ItsDrDan, CC BY 4.0.)</figcaption>', '(Figure: Daniel Kwasniewski, CC BY 4.0.)</figcaption>', 'T3 13.5 Figure 1: house credit name')
# figure numbers out of order
e('597130', 'Figure \\(\\PageIndex{2}\\): Nylon synthesis.', 'Figure \\(\\PageIndex{1}\\): Nylon synthesis.', 'T3 7.10: figures ran 2, 3, 1; now 1, 2, 3')
e('597130', 'Figure \\(\\PageIndex{3}\\): Nylon spatula.', 'Figure \\(\\PageIndex{2}\\): Nylon spatula.', 'T3 7.10: same')
e('597130', '<figcaption>Figure 7.10.1: Spotting the links', '<figcaption>Figure 7.10.3: Spotting the links', 'T3 7.10: same')
e('597210', 'Figure \\(\\PageIndex{3}\\)', 'Figure \\(\\PageIndex{1}\\)', 'T3 15.10: figures ran 3, 1; now 1, 2 (caption and two text mentions)', n=3)
e('597210', '<figcaption>Figure 15.10.1: The metabolic hub.', '<figcaption>Figure 15.10.2: The metabolic hub.', 'T3 15.10: same')
e('597146', 'href="https://upload.wikimedia.org/Wikipedia/commons/0/02/Biology_of_ventilation.gif"', 'href="https://commons.wikimedia.org/wiki/File:Biology_of_ventilation.gif"',
  'T3 9.3 Figure 4 credit link returned 401 (capital W); point to the Commons file page')
e('597146', 'title="https://upload.wikimedia.org/Wikipedia/commons/0/02/Biology_of_ventilation.gif"', 'title="https://commons.wikimedia.org/wiki/File:Biology_of_ventilation.gif"', 'T3 9.3: same link, title attribute')

# ---------------- Tier 4: polish, links, cross-references ----------------
e('597056', '<p>Step 1 above, putting the least electronegative atom in the center,', '<p>Step 2 above, putting the least electronegative atom in the center,', 'T4 1.3 tip: the central-atom rule is Step 2')
e('597056', 'The N atoms do not satisfy the octet.', 'Each N atom would have 10 electrons around it, more than an octet.', 'T4 1.3 Example 2: clearer')
for p, old, new in (
    ('597054', '(Practice Game - Lewis Structures page at the end of this chapter) will grade', '(Section 1.11, Practice Games, at the end of this chapter) will grade'),
    ('597056', '(Practice Game - Lewis Structures page at the end of this chapter): draw', '(Section 1.11, Practice Games, at the end of this chapter): draw'),
    ('597062', 'game (Practice Game - Lewis Structures page), then use the <strong>Functional Group Flashcards</strong> (Practice Games page) to drill',
     'game, then use the <strong>Functional Group Flashcards</strong> (both are on the 1.11 Practice Games page) to drill')):
    e(p, old, new, 'T4 Ch 1: no page is called "Practice Game - Lewis Structures"; the game is on 1.11')
e('597069', 'Learn the shapes; you will see them again as the 2&deg; and 3&deg; carbons in Section 2.4.', 'Learn the shapes; sec- and tert- point to the 2&deg; and 3&deg; carbons you classified in Section 2.4.',
  'T4 2.5: Section 2.4 comes before 2.5')
e('597080', 'None of them dissolves in water; all four float on it.', 'None of them dissolves in water, and the three liquids float on it.', 'T4 3.3 Example 1: propene is a gas')
e('597086', 'addition reaction (Key Idea 3) run backwards', 'addition reaction (Chapter Summary item 3) run backwards', 'T4 3.9: the list is now headed Chapter Summary')
e('597107', '<strong>Oxidation</strong> (oxidation): Oxidation of an aldehyde:', '<strong>Oxidation</strong>: Oxidation of an aldehyde:', 'T4 5.6 Figure 5.6.1: label read "Oxidation (oxidation):"')
e('597118', 'the circulating <em>salicylate</em> is a carboxylic acid at blood pH, so it is ionized.', 'the circulating salicylic acid is a carboxylic acid, so at blood pH it is ionized (<em>salicylate</em>).', 'T4 6.10: wording')
e('597201', 'FADH<sub>2</sub><sub>,</sub> and the production', 'FADH<sub>2</sub>, and the production', 'T4 14.2: comma was inside a subscript')
e('597150', 'on the section pages (9.1, 9.2, 9.3).', 'on the section pages (9.1, 9.2, 9.3, 9.6).', 'T4 9.7: 9.6 also has a worked example')
e('597137', 'and the videos in the Chapter Guide walk through glucose, mannose, and a ketose.', 'the videos at the top of this page walk through glucose and a ketose, and the Chapter Guide adds mannose.',
  'T4 8.4: the glucose and ketose videos are on this page; 8.8 has mannose')
# lactate and pyruvate dehydrogenase are taught in 13.4 (13.5 only points back)
e('597197', 'from working muscle and red blood cells (Section 13.5).', 'from working muscle and red blood cells (Section 13.4).', 'T4 13.8: lactate is taught in 13.4')
e('597197', 'catalyzed by pyruvate dehydrogenase (Section 13.5 and Chapter 14)', 'catalyzed by pyruvate dehydrogenase (Section 13.4 and Chapter 14)', 'T4 13.8: pyruvate dehydrogenase is taught in 13.4')
e('597197', 'reduces pyruvate to lactate to regenerate NAD<sup>+</sup> (Section 13.5).', 'reduces pyruvate to lactate to regenerate NAD<sup>+</sup> (Section 13.4).', 'T4 13.8: same')
e('597052', '<div>Lactate. <em>If you missed it, review <a href="/@go/page/597193">Section 13.5</a>.</em></div>', '<div>Lactate. <em>If you missed it, review <a href="/@go/page/597192">Section 13.4</a>.</em></div>',
  'T4 Ch 14 opener: lactate is taught in 13.4')

# path-based links inside the book -> stable /@go/page links (they work today, but break if a page is retitled or moved)
W = '/Workbench/CHEM_3B:_Introductory_Organic_and_Biochemistry/'
PATHS = {
    '05:_Aldehydes_and_Ketones/5.01:_Aldehydes_and_Ketones-_Structure_and_Names': '597102',
    '14:_Metabolism_and_Energy_Production/14.03:_Citric_acid_cycle': '597202',
    '06:_Carboxylic_Acids_and_Esters/6.07:_Preparation_of_Esters': '597115',
    '05:_Aldehydes_and_Ketones/5.05:_Introduction_to_stereochemistry': '597106',
    '08:_Carbohydrates/8.02:_Classes_of_Monosaccharides': '597135',
    '03:_Alkenes_Alkynes_and_Aromatic_Compounds/3.04:_Chemical_Properties_of_Alkenes': '597081',
    '07:_Amines_and_Amides/7.06:_Formation_of_Amides': '597126',
    '01:_Bonding_Review_-_Lewis_Structures_and_Intermolecular_Forces/1.08:_Intermolecular_Interactions': '597061',
    '13:_Carbohydrate_Metabolism/13.01:_Basics_of_metabolism': '597188',
    '09:_Lipids/9.01:_Fatty_Acids': '597144',
}
import glob, os
for f in sorted(glob.glob(L + '*.html')):
    p = os.path.basename(f)[:-5]
    for path, target in PATHS.items():
        old = f'href="{W}{path}"'
        n = page(p).count(old)
        if n: e(p, old, f'href="{GO(target)}"', f'T4 path link to page {target} -> /@go/page link', n=n)
assert not any('href="/Workbench/' in t for t in pages.values()), 'path link left'

# print-only answer keys missing on seven section pages that have inline exercise answers (every sibling page has a key)
for p, labels in (('597073', ['2.9.1']), ('597134', ['8.1.1']), ('597135', ['8.2.1']), ('597155', ['10.2.1']), ('597167', ['11.2.1']),
                  ('597177', ['12.3.1', '12.3.2']), ('597179', ['12.6.1'])):
    t = page(p)
    found = re.findall(r'<div class="hideprint answer-inline"><details class="hideprint"><summary>Answer</summary><div>(.*?)</div></details></div>', t, re.S)
    assert len(found) == len(labels) and 'answer-key' not in t, p
    tail = 'the section text above keeps its own license and attribution.</p>\n</div></div>'
    assert t.endswith(tail), p
    key = '\n\n<div class="showprint answer-key"><div class="mt-section"><h2 class="editable">Answers to Exercises</h2>\n' + ''.join(
        '<div class="answer-key-item"><p style="page-break-after:avoid;break-after:avoid"><strong>Exercise ' + lab + '</strong></p><div>' + ans + '</div></div>\n'
        for lab, ans in zip(labels, found)) + '</div></div>'
    e(p, tail, tail[:-len('\n</div></div>')] + key + '\n</div></div>', 'T4 ' + labels[0][:-2] + ': add the print-only answer key (inline answers never printed); same markup as 2.5')
e('597201', '<div class="answer-key-item"><p><strong>Example 1: Oxidized or reduced?</strong></p>', '<div class="answer-key-item"><p><strong>Practice: the reduced form of NAD</strong></p>',
  'T4 14.2 print key: the label named Example 1 but the answer is for the Practice question')

# ---------------- Chapters 10-12, glossary, front matter ----------------
e('597168', 'We sterilize objects by placing them in boiling water, which denatures the enzymes of any bacteria that may be in or on them.',
  'We disinfect objects by placing them in boiling water, which denatures the enzymes of most bacteria that may be in or on them (true sterilization needs an autoclave at 121&deg;C).',
  'T1 11.3: boiling disinfects; the same page says sterilizing needs the autoclave')
e('597154', '<td data-th="Molar Mass" style="text-align:center;vertical-align:middle;">175</td>', '<td data-th="Molar Mass" style="text-align:center;vertical-align:middle;">174</td>',
  'T1 10.1 Table 1: arginine C6H14N4O2 is 174.2 g/mol')
e('597158', 'ionic bonding, hydrogen bonding, disulfide linkages, and dispersion forces. A wide',
  'salt bridges (ionic bonds), hydrogen bonds, disulfide bonds, and hydrophobic interactions (dispersion forces between nonpolar side chains). A wide',
  'T2 10.5 Summary: use the four graded names (CONVENTIONS)')
e('597158', '(a) ionic bonding, (b) hydrogen bonding, (c) disulfide linkages, and (d) dispersion forces.',
  '(a) ionic bonding (salt bridges), (b) hydrogen bonding, (c) disulfide linkages, and (d) dispersion forces (hydrophobic interactions).', 'T2 10.5 Figure 5 caption: bridge to the graded names')
e('488232', 'A non-protein helper that an enzyme needs to work: a metal ion or an organic coenzyme.',
  'An inorganic ion, such as Zn<sup>2+</sup>, Mg<sup>2+</sup> or Fe<sup>2+</sup>, that an enzyme needs to work (organic helpers are called coenzymes in this course).',
  'T2 Glossary cofactor: match 11.5 (cofactor = inorganic ion)')
e('488232', 'An organic cofactor, usually made from a vitamin, such as', 'An organic helper molecule that an enzyme needs, usually made from a vitamin, such as', 'T2 Glossary coenzyme: match 11.5')
e('597176', '<figcaption>Figure 12.2.1: Primary structure:', '<figcaption>Figure 12.2.5: Primary structure:', 'T3 12.2: duplicate Figure 12.2.1 (source figures are already 1-4)')
e('597176', '<figcaption>Figure 12.2.2: Secondary structure:', '<figcaption>Figure 12.2.6: Secondary structure:', 'T3 12.2: duplicate Figure 12.2.2')
e('597160', 'Ayacop, Public domain, via Wikimedia Commons<span style="font-size:1rem;">. (</span>Ayacop, Public domain, via Wikimedia Commons<span style="font-size:1rem;">.)</span>',
  '(Ayacop, Public domain, via Wikimedia Commons.)', 'T3 10.7 Figure 4: credit was printed twice')
e('597159', 'that binds parts of the same chain or two different chains, as shown in Figure \\(\\PageIndex{2}\\). Examples', 'that binds parts of the same chain or two different chains. Examples',
  'T4 10.6: same figure cited twice in two sentences')
e('597179', '<span id="Exercise_.5C(.5CPageIndex.7B4.7D.5C)"></span><div class="mt-section"><h5 class="box-legend editable">Exercise \\(\\PageIndex{4}\\)</h5>',
  '<span id="Exercise_.5C(.5CPageIndex.7B1.7D.5C)"></span><div class="mt-section"><h5 class="box-legend editable">Exercise \\(\\PageIndex{1}\\)</h5>',
  'T4 12.6: the only exercise on the page was numbered 4')
e('597270', 'Carb Lab and Peptide Builder games', 'Sweet Structures and Peptide Party games', 'T4 About This Book: the games are called Sweet Structures and Peptide Party on the Practice Games pages')

#__MORE__

json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchM_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
