"""Batches I (held items) and J (optional work), review 2026-11-12.
I  held items: dated statistics fact-checked (8.6, 8.7, 4.4, 12.9 Valley fever, 2.8, 3.5, 3.8, 1.6), methane bp,
   About Valley list order, 12.5 preview labels, 10.2/10.3 ninhydrin duplicate (+ Ball credit on 10.3),
   6.12/7.13 answer keys, 6.6 chart 163 °C, video embed titles on 1.5/1.8 (match YouTube; the 1.9 list already did),
   "(opens in new window)" residue, figure fixes: 12.2.3 base pairs (cytosine NH2 and C4=N3, purine C4=C5),
   14.1.1 phosphate charges, 9.3.1 condensed formula (own redraw), 8.4.1(b) curved-arrow mechanism removed,
   Slide 47 "Glyceryl tripalmitate". (5.4/5.5 title case is done through the title API, not here.)
J  optional: 13.5.2 glycolysis flow redrawn landscape; 14.4 ETC uses the inner-membrane version (prints larger);
   14.4 ATP synthase as two print strips and Figure 14.4.2 parts stacked (were side by side, printing at ~1/3 width);
   14.5 yield flow cropped to its content; 18 clarity fixes (tools/batchJ_text_drafts_2026-11-12.json).
Output: tools/batchIJ_2026-11-12.json {uploads, edits}
"""
import json, re

L = 'pages/live/'
PG = 'https://itsdrdan.github.io/textbook/'
pages, edits, uploads = {}, {}, []


def page(p):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read()
    return pages[p]


def e(p, old, new, note, n=1):
    t = page(p); assert t.count(old) == n, (p, note, t.count(old))
    pages[p] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


def load(fn, skip=lambda p, x: False):
    for p, es in json.load(open(fn)).items():
        for x in es:
            if skip(p, x): continue
            e(p, x['old'], x['new'], x['note'], x.get('count', 1))


load('tools/batchI_text_drafts_2026-11-12.json', skip=lambda p, x: p == '597062' and x['note'].startswith('3:'))
load('tools/batchJ_text_drafts_2026-11-12.json')

# video embed titles = real YouTube titles (oEmbed checked)
e('597058', 'title="Electronegativity and Polarity (Part 2: Polar Molecules) (Daniel Kwasniewski (ItsDrDan), YouTube video)"',
  'title="Electronegativity and Polarity (Part II: Polar Molecules) (Daniel Kwasniewski (ItsDrDan), YouTube video)"', 'embed title matches YouTube')
e('597061', 'title="Dipole-Dipole, Hydrogen Bonding, and Ion-Dipole (Daniel Kwasniewski (ItsDrDan), YouTube video)"',
  'title="Dipole-Dipole, Hydrogen Bonding, and Ion-Dipole: Properties of Intermolecular Forces (Part 3) (Daniel Kwasniewski (ItsDrDan), YouTube video)"', 'embed title matches YouTube')

# "(opens in new window)" residue
for p, n in (('597158', 1), ('597179', 1), ('597200', 1), ('597201', 2)):
    e(p, '(opens in new window)', '', 'link residue removed', n)

# ninhydrin image on 10.3: credit (Ball source page)
e('597156', 'src="/@api/deki/files/25912/ninhydrin.jpg" fileid="25912" /></p>',
  'src="/@api/deki/files/25912/ninhydrin.jpg" fileid="25912" /></p>\n<p class="mt-align-center"><small>(Figure from <em>The Basics of General, Organic, and Biological Chemistry</em> by Ball, Hill and Scott, CC BY-NC-SA 3.0.)</small></p>',
  '10.3 ninhydrin figure credit')


def img_with(p, needle):
    t = page(p); i = t.find(needle); assert i >= 0, (p, needle)
    return t[t.rfind('<img', 0, i):t.find('>', i) + 1]


def repoint(p, needle, fname, path, key, note, alt=None, width=None):
    old = img_with(p, needle)
    new = re.sub(r'src="[^"]*"', f'src="/@api/deki/files/{{{{{key}}}}}/{fname}"', old)
    new = re.sub(r'\sfileid="[^"]*"', f' fileid="{{{{{key}}}}}"', new) if 'fileid=' in new else new.replace('<img', f'<img fileid="{{{{{key}}}}}"', 1)
    if alt: new = re.sub(r'alt="[^"]*"', 'alt="' + alt + '"', new)
    if width:
        new = re.sub(r'\s(width|height)="[^"]*"', '', new)
        new = re.sub(r'style="[^"]*"', 'style="max-width:100%;height:auto;"', new) if 'style="' in new else new.replace('<img', '<img style="max-width:100%;height:auto;"', 1)
        new = new.replace('<img', f'<img width="{width}"', 1)
    uploads.append({'page': p, 'name': fname, 'path': path, 'key': key, 'old_fileid': None})
    e(p, old, new, note)


def svgalt(path): return re.search(r'aria-label="([^"]*)"', open(path).read()).group(1)


repoint('597176', 'files/512746/', 'fig-p597176-base-pairs-v2.jpg', 'figures/pages/batchI/fig-p597176-base-pairs-v2.jpg', 'bp', '12.2.3 base pairs: cytosine NH2 and C4=N3, purine C4=C5')
repoint('597200', 'fig-p597200-acetyl-coa.jpg', 'fig-p597200-acetyl-coa-v2.jpg', 'figures/pages/batchI/fig-p597200-acetyl-coa-v2.jpg', 'acoa', '14.1.1 phosphate O- charges')
repoint('597137', 'fig-p597137-glucose-cyclization.jpg', 'fig-p597137-glucose-cyclization-v2.jpg', 'figures/pages/batchI/fig-p597137-glucose-cyclization-v2.jpg', 'glc', '8.4.1(b) curved-arrow mechanism removed',
        alt='Cyclization of D-glucose in three panels: (a) the Fischer projection with carbons numbered 1 to 6; (b) a three-dimensional representation in which the chain curls so the OH on carbon 5 comes close to the aldehyde carbon 1; (c) the resulting six-membered ring (Haworth projection) with the ring oxygen and the new OH on carbon 1.')
repoint('597146', 'files/435618/', 'fig-p597146-popc-condensed.svg', 'figures/pages/batchF/fig-p597146-popc-condensed.svg', 'popc', '9.3.1 condensed formula: CH3(CH2)n written correctly (own redraw)',
        alt=svgalt('figures/pages/batchF/fig-p597146-popc-condensed.svg'), width=560)
repoint('597193', 'fig-p597193-1.svg', 'fig-p597193-glycolysis-flow.svg', 'figures/pages/batchF/fig-p597193-glycolysis-flow.svg', 'gflow', '13.5.2 glycolysis flow redrawn landscape',
        alt=svgalt('figures/pages/batchF/fig-p597193-glycolysis-flow.svg'), width=760)
repoint('597204', 'fig-p597204-1.svg', 'fig-p597204-yield-flow.svg', 'figures/pages/batchF/fig-p597204-yield-flow.svg', 'yflow', '14.5 yield flow cropped to content (prints larger)', width=760)

# GitHub Pages assets (served after merge)
e('597145', 'figures/Slide47.png" alt="', 'figures/Slide47.png?v=20261113" alt="', 'Slide 47 cache-bust (Glyceryl tripalmitate)')
e('597145', 'Right: glyceryl palmitate (tripalmitin)', 'Right: glyceryl tripalmitate (tripalmitin)', 'Slide 47 alt name')
e('597114', 'src="' + PG + 'figures/pathways/ester_bp.svg"', 'src="' + PG + 'figures/pathways/ester_bp.svg?v=20261113"', '6.6 chart cache-bust (163 °C)')
e('597203', PG + 'figures/pathways/etc/etc.svg"', PG + 'figures/pathways/etc/etc_inner.svg"', '14.4 ETC: inner-membrane version prints larger')
t = page('597203'); i = t.find('oer/atp_synthase.svg'); a = t.rfind('<div class="row">', 0, i); b = t.find('</div>', i) + 6
row = t[a:b]
inner = row[len('<div class="row">'):-len('</div>')]
atp_old = img_with('597203', 'oer/atp_synthase.svg')
alt = re.search(r'alt="([^"]*)"', atp_old).group(1)
strips = ''.join(f'<img src="{PG}figures/print/atp_synthase-v3-{k}.svg" alt="{alt if k == 1 else ""}" style="display:block;margin:0;width:700px;max-width:100%;height:auto" />' for k in (1, 2))
inner = inner.replace(atp_old, strips)
e('597203', row, inner.strip('\n') + '\n', '14.4 Fig 2: parts a, b, c stacked; ATP synthase as two full-width print strips')
e('597203', '<strong>a)</strong> \\(\\ce{ATP}\\)-synthase in the inner mitochondrial membrane (Diagram: Daniel Kwasniewski, CC BY 4.0),',
  '<strong>a)</strong> \\(\\ce{ATP}\\)-synthase in the inner mitochondrial membrane; in human mitochondria the rotor has 8 c subunits, so 8 H<sup>+</sup> turn it once and one turn makes 3 ATP (Diagram: Daniel Kwasniewski, CC BY 4.0),',
  '14.4 Fig 2 caption keeps the removed footnote')

json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchIJ_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
