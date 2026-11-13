"""Batches C2-C4 (review 2026-11-12).
C2  old alt text printed as a visible caption: delete second captions that repeat the alt; replace captions that
    are only screen-reader descriptions with a short real caption (credit kept).
C3  double-escaped &amp;ndash; inside alt attributes -> &ndash;
C4  <span style="display:none;"> </span> fragments (two split words: "propion ic", "oxidoreduc tase") removed.
Output: tools/batchC2_4_fixes_2026-11-12.json  {page: [{old,new,count,note}]}, replay-checked against pages/live.
"""
import json, re

L = 'pages/live/'
pages = {}
edits = {}


def T(p):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read()
    return pages[p]


def rep(p, old, new, note):
    t = T(p); c = t.count(old)
    assert c == 1, (p, note, c, old[:80])
    pages[p] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})


def cap(p, starts):
    """Full <figcaption>…</figcaption> whose text begins with `starts`."""
    t = T(p); i = t.find('<figcaption>' + starts); assert i >= 0, (p, starts)
    j = t.find('</figcaption>', i) + len('</figcaption>')
    return t[i:j]


def drop_second(p, starts, note):
    c = cap(p, starts); t = T(p); i = t.find(c)
    k = i
    while t[k - 1] in ' \n': k -= 1   # also drop the blank line before it
    rep(p, t[k:i] + c, '', note)


CREDIT_BALL = ' (Figure from <em>The Basics of General, Organic, and Biological Chemistry</em> by Ball, Hill and Scott, CC BY-NC-SA 3.0.)'


def recaption(p, starts, text, note):
    c = cap(p, starts)
    m = re.search(r'\s*\((?:Figure from|credit)[^<]*(?:<em>[^<]*</em>[^<]*)*\)\s*</figcaption>$', c)
    credit = m.group(0)[:-len('</figcaption>')].rstrip() if m else ''
    rep(p, c, f'<figcaption>{text}{(" " + credit.strip()) if credit else ""}</figcaption>', note)


# ---- C2: second captions that repeat the alt text
drop_second('597061', 'Two pairs of molecules are shown', '1.8 Fig 7 second caption (old alt)')
drop_second('597061', 'Five water molecules are shown', '1.8 Fig 8 second caption (old alt)')
drop_second('597061', 'Three figures are shown', '1.8 Fig 12 second caption (old alt)')
drop_second('597094', 'A flow diagram of three possible reactions', '4.5 Fig 1 second caption (old alt)')
drop_second('597103', 'A person wearing gloves', '5.2 Fig 1 second caption (old alt)')
drop_second('597148', 'Phosphoglycerides are composed', '9.5 Fig 4 second caption (old alt)')
# 1.4: an empty first caption holds the credit; the real caption follows
rep('597057', '<figcaption>&nbsp;. (Figure from <em>The Basics of General, Organic, and Biological Chemistry</em> by Ball, Hill and Scott, CC BY-NC-SA 3.0.)</figcaption>\n\n<figcaption>Figure \\(\\PageIndex{3}\\) The electronegativity values derived by Pauling follow predictable periodic trends with the higher electronegativities toward the upper right of the periodic table. Fluorine has the highest value (4.0).</figcaption>',
    '<figcaption>Figure \\(\\PageIndex{3}\\): The electronegativity values derived by Pauling follow predictable periodic trends with the higher electronegativities toward the upper right of the periodic table. Fluorine has the highest value (4.0).' + CREDIT_BALL + '</figcaption>',
    '1.4 Fig 3: merge empty credit caption into the real caption')

# ---- C2: captions that were only screen-reader descriptions
R = [
    ('597054', "Two F's with two dots in between them", 'Lewis structure of F<sub>2</sub>: the shared pair of electrons is drawn as two dots between the atoms.'),
    ('597054', "Two F's with a long dash in between them", 'The same F<sub>2</sub> molecule with the shared pair drawn as a dash, a single covalent bond.'),
    ('597054', 'An H and F connected by two dots', 'HF drawn two ways: the shared pair as two dots and as a dash.'),
    ('597054', 'Cl with 7 dots surrounding it', 'Two chlorine atoms, each with seven valence electrons, share one pair to form Cl<sub>2</sub>.'),
    ('597054', 'H with one dot plus Br with 7 dots', 'Hydrogen and bromine share one pair of electrons to form HBr.'),
    ('597054', 'H with one dot + O with 6 dots', 'Two hydrogen atoms each share a pair of electrons with oxygen to form H<sub>2</sub>O.'),
    ('597054', 'F surrounded by 6 dots, connected to O', 'Lewis structure of OF<sub>2</sub>: two single bonds, F&ndash;O&ndash;F.'),
    ('597055', 'NH<sub>3</sub><sub>.</sub> An arrow points', 'Reading a molecular formula: in NH<sub>3</sub>, no subscript on N means one nitrogen atom, and the subscript 3 means three hydrogen atoms.'),
    ('597056', 'H dash C dash N with 6 dots', 'Completing the octets in HCN: two lone pairs on N become shared, giving a C&equiv;N triple bond.'),
    ('597071', 'Butane plus O H superscript', 'Alkanes such as butane do not react with strong bases, strong acids or oxidizing agents such as permanganate.'),
    ('597094', 'Structural formula of ethanol dehydrating', 'Dehydration of ethanol: excess concentrated H<sub>2</sub>SO<sub>4</sub> at 180 &deg;C gives ethylene and water.'),
    ('597094', 'Structural formula of 2 phosphoglycerate forming', 'An enzyme dehydrates 2-phosphoglycerate to phosphoenolpyruvate, a step in glycolysis.'),
    ('597094', 'Formula of ethanol reacting to form acetaldehyde', 'Oxidation of ethanol to acetaldehyde; [O] over the arrow stands for an oxidizing agent.'),
    ('597061', 'A line graph, titled &ldquo;Carbon Family,&rdquo;', 'Boiling points of the group 14 hydrides, CH<sub>4</sub> through SnH<sub>4</sub>: boiling point rises as the molecules get larger and dispersion forces get stronger.'),
]
for p, s, txt in R:
    recaption(p, s, txt, f'{p} caption was old alt text')

# ---- C3: &amp;ndash; in alt attributes
for p in ('597061', '597082', '597096', '597116', '597131', '597197'):
    t = T(p)
    for m in list(re.finditer(r'alt="[^"]*&amp;ndash;[^"]*"', t)):
        rep(p, m.group(0), m.group(0).replace('&amp;ndash;', '&ndash;'), 'alt: &amp;ndash; -> &ndash;')

# ---- C4: hidden display:none spans
for p, old in [('597111', 'propion<span style="display:none;"> </span>ic acid'), ('597166', 'oxidoreduc<span style="display:none;"> </span>tase')]:
    rep(p, old, old.replace('<span style="display:none;"> </span>', ''), 'hidden span split a word')
for p in ('597090', '597098', '597102', '597144', '597180', '597192'):
    for sp in ('<span style="display:none;"> </span>', '<span style="display:none;">&nbsp;</span>'):
        while sp in T(p):
            t = T(p); i = t.find(sp); a, b = i, i + len(sp)
            while t.count(t[a:b]) != 1: a -= 20; b += 20
            o = t[a:b]; rep(p, o, o.replace(sp, '', 1), 'hidden span removed')

bad = 0
for p, es in edits.items():
    t = open(L + p + '.html', encoding='utf-8').read()
    for x in es:
        if t.count(x['old']) != 1: bad += 1; print('REPLAY FAIL', p, x['note'])
        t = t.replace(x['old'], x['new'])
json.dump(edits, open('tools/batchC2_4_fixes_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'replay failures')
