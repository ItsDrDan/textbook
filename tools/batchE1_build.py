"""Batch E1 (review 2026-11-12): figure credits and attribution statements on the book pages.
Every credit below was checked against its source before writing it:
- Malik's own pages credit these figures only as "(Copyright; Public domain)" with no creator, so the credit
  names the source book.
- Four photos match Wikimedia Commons files (compared visually; author and licence from the Commons API):
  Tomato_je.jpg (Softeis, CC BY-SA 3.0), Phenol-3D-balls.png (Benjah-bmm27, public domain),
  Phenol_2_grams.jpg (W. Oelen, CC BY-SA 3.0), Ergospirometry_laboratory.jpg (Cosmed, CC BY-SA 3.0).
- The 1.8 DNA figures appear in OpenStax Chemistry 2e, section 10.1 (CC BY-NC-SA 4.0 per the OpenStax catalogue).
- The 15.1 lipoprotein diagram's linked source: Jairam, Uchida and Narayanaswami, "Pathophysiology of Lipoprotein
  Oxidation", in Lipoproteins: Role in Health and Diseases (IntechOpen, 2012), CC BY 3.0 (chapter page).
Not changed after checking: 11.6 Biology 2e credit (OpenStax lists Biology 2e as CC BY-NC-SA 4.0, so the credit is
right); the 11 Fundamentals rows naming "LibreTexts" as author (LibreTexts' own metadata names no other author).
Output: tools/batchE1_fixes_2026-11-12.json
"""
import json

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


MALIK = '(Figure from <em>Introduction to Organic and Biochemistry</em> (Malik), public domain.)'
for p, n in (('597060', 1), ('597161', 1), ('597188', 2)):
    rep(p, '(Public domain)</figcaption>', MALIK + '</figcaption>', 'Malik figure credit', n)
for p, n in (('597060', 2), ('597106', 1)):
    rep(p, '(Public domain).</figcaption>', MALIK + '</figcaption>', 'Malik figure credit', n)
rep('597188', '(Public domain; N5 of FADH<sub>2</sub> corrected by Daniel Kwasniewski.)',
    '(Figure from <em>Introduction to Organic and Biochemistry</em> (Malik), public domain; N5 of FADH<sub>2</sub> corrected by Daniel Kwasniewski.)', 'Malik figure credit (FAD)')
rep('597209', 'stearic acid. (Public domain)</figcaption>',
    'stearic acid. (Figure from <em>Introduction to Organic and Biochemistry</em> (Malik), public domain; label spellings corrected by Daniel Kwasniewski.)</figcaption>', 'Malik figure credit (beta-oxidation; labels fixed in batch B2)')

# Commons photos
rep('597080', 'src="/@api/deki/files/51927/Tomato_je1.jpg" fileid="51927" /></p>',
    'src="/@api/deki/files/51927/Tomato_je1.jpg" fileid="51927" /></p>\n<p class="mt-align-center"><small>Photo: Softeis, <a href="https://commons.wikimedia.org/wiki/File:Tomato_je.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC BY-SA 3.0</a>.</small></p>',
    '3.3 tomato photo credit')
rep('597096', '(Left) Structure of Phenol (right) Approximately two grams of phenol in a glass vial. from Wikipedia</figcaption>',
    '(Left) Ball-and-stick model of phenol. (Right) About two grams of phenol crystals in a glass tube. (Model: Benjah-bmm27, public domain; photo: W. Oelen, <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC BY-SA 3.0</a>; both via Wikimedia Commons.)</figcaption>',
    '4.7 Fig 1 credits')
rep('597208', 'during a graded exercise test on a treadmill. from Wikipedia. (Figure from <em>The Basics of General, Organic, and Biological Chemistry</em> by Ball, Hill and Scott, CC BY-NC-SA 3.0.)',
    'during a graded exercise test on a treadmill. (Photo: Cosmed, <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC BY-SA 3.0</a>, via Wikimedia Commons.)',
    '15.8 ergospirometry photo credit')

# 1.8 OpenStax figures
OS = '<a href="https://openstax.org/books/chemistry-2e/pages/10-1-intermolecular-forces" target="_blank" rel="noopener"><em>Chemistry 2e</em></a> (Flowers et al., OpenStax), <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener">CC BY-NC-SA 4.0</a>'
rep('597061', 'held together via hydrogen bonding. (credit: modification of work by Jerome Walker, Dennis Myts)',
    'held together via hydrogen bonding. (Figure from ' + OS + '; credit: modification of work by Jerome Walker, Dennis Myts.)', '1.8 Fig 10 OpenStax credit')
rep('597061', '(Figure from <em>The Basics of General, Organic, and Biological Chemistry</em> by Ball, Hill and Scott, CC BY-NC-SA 3.0; thymine methyl group and one backbone CH<sub>2</sub> corrected by Daniel Kwasniewski.)',
    '(Figure from ' + OS + '; thymine methyl group and one backbone CH<sub>2</sub> corrected by Daniel Kwasniewski.)', '1.8 Fig 11 is OpenStax, not Ball')

# 10.7 Fig 1
rep('597160', 'Basic secondary structures of proteins illustrated.</figcaption>',
    'Basic secondary structures of proteins illustrated. (The creator and license of each panel are printed on the panel.)</figcaption>', '10.7 Fig 1 credit pointer')

# 15.1 lipoprotein diagram
rep('597211', 'The classification of the major types of lipoproteins are based on their densities.', 'The classification of the major types of lipoproteins is based on their densities.', '15.1 grammar')
rep('597211', '(<a href="https://www.intechopen.com/books/lipoproteins-role-in-health-and-diseases/pathophysiology-of-lipoprotein-oxidation" target="_blank" rel="external noopener nofollow" class="link-https">Diagram</a> not to scale) / <a href="https://creativecommons.org/licenses/by/3.0" target="_blank" rel="external noopener nofollow" class="link-https">CC BY 3.0</a></figcaption>',
    'Not to scale. (Diagram from Vikram Jairam, Koji Uchida and Vasanthy Narayanaswami, &ldquo;<a href="https://www.intechopen.com/books/lipoproteins-role-in-health-and-diseases/pathophysiology-of-lipoprotein-oxidation" target="_blank" rel="external noopener nofollow" class="link-https">Pathophysiology of Lipoprotein Oxidation</a>,&rdquo; in <em>Lipoproteins: Role in Health and Diseases</em>, IntechOpen, 2012, <a href="https://creativecommons.org/licenses/by/3.0" target="_blank" rel="external noopener nofollow" class="link-https">CC BY 3.0</a>.)</figcaption>',
    '15.1 lipoprotein diagram credit with authors')

# Source Attributions page
rep('597271', "<li><strong>Videos</strong> are the author's own CHEM 3B lessons on YouTube (@itsdrdan), embedded by link; they are not part of the licensed text.</li>",
    "<li><strong>Videos</strong> are mostly the author's own CHEM 3B lessons on YouTube (@itsdrdan). Third-party videos (Amoeba Sisters, BioMan Biology, NDSU Virtual Cell Animations, Biotech Review and NHLBI) are credited where they appear. All videos are embedded by link and are not part of the licensed text.</li>",
    'videos statement includes third-party videos')
rep('597271', '<li><strong>Figures inside adapted sections</strong> belong to the source book and carry its license (see the table above); only their alt-text descriptions were rewritten for this book.</li>',
    '<li><strong>Figures inside adapted sections</strong> belong to the source book and carry its license (see the table above), except third-party images (for example from Wikimedia Commons, OpenStax or IntechOpen), which are credited individually in their captions with their own licenses. Only their alt-text descriptions were rewritten for this book.</li>',
    'figures statement covers third-party images')

# About page
rep('597270', '<td>21 section pages, mostly in Chapters 5, 10, 12&ndash;15</td>', '<td>20 section pages, mostly in Chapters 5, 10, 12&ndash;15</td>', 'About: Malik count is 20 (84+20+11+10 = 125)')

bad = 0
for p, es in edits.items():
    t = open(L + p + '.html', encoding='utf-8').read()
    for x in es:
        if t.count(x['old']) != x['count']: bad += 1; print('REPLAY FAIL', p, x['note'])
        t = t.replace(x['old'], x['new'])
json.dump(edits, open('tools/batchE1_fixes_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'replay failures')
