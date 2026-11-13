"""Batch C5 (review 2026-11-12): leftovers after edits and section moves.
Output: tools/batchC5_fixes_2026-11-12.json {page: [{old,new,count,note}]}, replay-checked against pages/live.
Dated statistics (sugar, cotton, methanol, measles, ozone hole, MyPlate) are not here: they need sources (separate batch).
"""
import json, re, glob

L = 'pages/live/'
pages, edits = {}, {}


def T(p):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read()
    return pages[p]


def rep(p, old, new, note, n=1):
    t = T(p); c = t.count(old)
    assert c == n, (p, note, c)
    pages[p] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


# 1. LibreTexts auto-credit prefix "(Copyright; ...)" -> "(...)" everywhere
for f in sorted(glob.glob(L + '*.html')):
    p = f.split('/')[-1][:-5]; c = T(p).count('(Copyright; ')
    if c: rep(p, '(Copyright; ', '(', 'credit: drop "Copyright; " prefix', c)

# 2. internal production note on four pages
for p in ('597098', '597114', '597170', '597217'):
    rep(p, 'Copied into this book (no longer live-linked) so it can be edited for CHEM 3B. ',
        'The text was edited for CHEM 3B by Daniel Kwasniewski, Fresno City College. ', 'internal note -> standard editing line')

# 3. stale learning objectives after section moves
rep('597203', 'accounting for the ATP yield, body heating, and reactive oxygen species produced.', 'accounting for the ATP yield and body heating.', '14.4 objective: ROS no longer on page')
rep('597209', 'Understand obesity, ketogenesis, ketosis, ketoacidosis, and catabolism of glycerol, associated with \\(\\beta\\)-oxidation of fatty acids.',
    'Understand obesity and the catabolism of glycerol, associated with \\(\\beta\\)-oxidation of fatty acids (ketone bodies are in Section 15.5).', '15.4 objective: ketone bodies moved to 15.5')
rep('597207', 'To describe the reactions needed to completely oxidize a fatty acid to carbon dioxide and water.',
    'Describe how a fatty acid is activated and carried into the mitochondrion by the carnitine shuttle.', '15.3 objective matches the page')
rep('597210', 'Understand the catabolism of amino acids, including transamination, oxidative deamination, and urea cycle that takes care of the \\(\\ce{N}\\) and processing of the \\(\\ce{C}\\) skeleton of the amino acid to intermediates that enter into citric acid cycle for energy production.',
    'Describe how the carbon skeletons of amino acids enter the citric acid cycle, and classify amino acids as glucogenic or ketogenic (removing the nitrogen is covered in Sections 15.8 and 15.9).', '15.10 objective: N removal moved to 15.8/15.9')

# 4. one-off leftovers
rep('597058', ' the effect of a B-F bond is cancelled by the sum of the other two B-F bonds (see video).', ' the effect of a B-F bond is cancelled by the sum of the other two B-F bonds.', '1.5 no BF3 video on page')
rep('597060', '-H}\\), is condensed as \\(\\ce{CH3CHClCH3}\\)</td>', '-H}\\)</td>', '1.7 Table 4 Lewis cell had pasted condensed text')
rep('597060', 'In lecture they are presented side by side for a single molecule, because this book, the games, and your exams switch among them without warning and you must translate on the spot.',
    'In lecture they are presented side by side for a single molecule, because you must translate between them on the spot.', '1.7 same sentence twice in a row')
rep('597061', 'Applying the skills acquired in the chapter on chemical bonding and molecular geometry, all of these compounds', 'Using Sections 1.4 and 1.5, all of these compounds', '1.8 refers to an OpenStax chapter')
rep('597118', '<li>The \\(\\ce{pH}\\) inside cells and in blood is close to neutral (blood is about 7.4). Carboxylic acids', '<li>Carboxylic acids', '6.10 sentence repeats the one above')
rep('597132', 'clinical boxes behind it now sit on the section pages', 'clinical boxes behind it are on the section pages', '7.12 "now" refers to an old layout')
rep('597159', '<p>Vasopressin and oxytocin are two nonapeptide hormones released by the pituitary gland. Vasopressin is an antidiuretic hormone that regulates blood pressure by adjusting the water reabsorbed by the kidneys. Oxytocin stimulates uterine contractions in labor.</p>',
    '<p>Vasopressin and oxytocin are two nonapeptide hormones released by the pituitary gland (their roles are described above).</p>', '10.6 paragraph repeated')
rep('597173', '<h3 class="editable">6. Specificity and regulation</h3>', '<h3 class="editable">6. Regulation</h3>', '11.8 Key Idea 6 has no specificity content')
rep('597158', 'a marker for alpha-thalassemia. Protein Sci. 1739&ndash;1749).', 'a marker for alpha-thalassemia. Protein Sci. 10(9): 1739&ndash;1749).', '10.5 citation volume')
rep('597182', 'fingerprinting, and human genome project. </li>', 'fingerprinting, and the Human Genome Project.</li>', '12.9 objective')
rep('597243', '<strong>New: Rosa&rsquo;s Case Files.</strong>', '<strong>Rosa&rsquo;s Case Files.</strong>', '13.12 "New:" will date')
rep('597202', 'The following equations of the reactions are modified from a public domain at ', 'The following equations of the reactions are adapted from a public-domain source on the Russian-language ', '14.3 wording; link is ru.wikipedia')
rep('597216', 'Note Everyday Connection: Gout</h3>', 'Everyday Connection: Gout</h3>', '15.9 stray "Note"')
for x in ('Oxidation</strong> (oxidation): ', 'Reduction</strong> (reduction): '):
    pass
rep('597100', '<strong>Oxidation</strong> (oxidation): ', '<strong>Oxidation:</strong> ', '4.11 redundant "(oxidation)"', 3)
rep('597107', '<strong>Reduction</strong> (reduction): ', '<strong>Reduction:</strong> ', '5.6 redundant "(reduction)"')
rep('597107', '<strong>Hemiacetal formation</strong> (addition): Hemiacetal formation: ', '<strong>Hemiacetal formation (addition):</strong> ', '5.6 repeated lead-in')
rep('597094', 'The following reaction occurs in the &quot;Embden&ndash;Meyerhof&quot; pathway:', 'The following reaction occurs in glycolysis (Chapter 13):', '4.5 name used nowhere else')
rep('597090', 'We first introduced the idea of the functional group,', 'In Chapter 1 we introduced the idea of the functional group,', '4.1 dropped chapter reference')
rep('597166', 'under the oversight of the Nomenclature Commission of the International Union of Biochemistry, enzymes are arranged into six groups according to',
    'under the oversight of the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (IUBMB), enzymes are arranged into classes according to', '11.1 committee name; class count is in the Lecture Connection')
rep('597136', 'One of the newest artificial sweeteners to gain FDA approval (April 1998) for use in the United States is ', 'An artificial sweetener approved by the FDA in April 1998 is ', '8.3 "newest" is dated')
rep('597140', 'Career Focus: Certified Diabetes Educator</h3>', 'Career Focus: Certified Diabetes Care and Education Specialist (CDCES)</h3>', '8.7 credential renamed 2020')
rep('597140', '<p>Certified diabetes educators come from', '<p>Certified diabetes care and education specialists (called certified diabetes educators before 2020) come from', '8.7 credential renamed 2020')

bad = 0
for p, es in edits.items():
    t = open(L + p + '.html', encoding='utf-8').read()
    for x in es:
        if t.count(x['old']) != x['count']: bad += 1; print('REPLAY FAIL', p, x['note'])
        t = t.replace(x['old'], x['new'])
json.dump(edits, open('tools/batchC5_fixes_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'replay failures')
print('Copyright prefixes:', sum(x['count'] for es in edits.values() for x in es if 'Copyright' in x['note']))
