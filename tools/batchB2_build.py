"""Batch B2 (label typos baked into images), review of 2026-11-12.

Builds tools/batchB2_figures_2026-11-12.json in the same format as batch B1:
  uploads: PUT to /@api/deki/pages/{page}/files/={name}; key -> {{key}} placeholder for the new file id.
  edits:   {page: [{old, new, count, note}]}, checked against pages/live.
Raster fixes are uploaded under new clean names (fig-p<page>-<slug>.*) and the <img> src/fileid are repointed;
the two house SVGs keep their names (new revision, same id).
"""
import json, re

L = 'pages/live/'
A = 'figures/pages/batchB2/'
uploads, edits = [], {}


def page(p):
    return open(L + p + '.html', encoding='utf-8').read()


def img_tag(p, fid):
    t = page(p); i = t.find(f'files/{fid}/'); a = t.rfind('<img', 0, i); b = t.find('>', i) + 1
    return t[a:b]


def e(p, old, new, n=1, note=''):
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


def repoint(p, fid, fname, key, note, alt=None):
    """Upload fname to page p and point the existing <img> (fileid fid) at it; keep every other attribute."""
    old = img_tag(p, fid)
    new = re.sub(r'src="[^"]*"', f'src="/@api/deki/files/{{{{{key}}}}}/{fname}"', old)
    new = re.sub(r'fileid="\d+"', f'fileid="{{{{{key}}}}}"', new)
    if alt is not None:
        new = re.sub(r'alt="[^"]*"', 'alt="' + alt + '"', new)
    uploads.append({'page': p, 'name': fname, 'path': A + fname, 'key': key, 'old_fileid': None})
    e(p, old, new, 1, note)


def reput(p, fid, fname, key, note):
    uploads.append({'page': p, 'name': fname, 'path': A + fname, 'key': key, 'old_fileid': fid})


repoint('597060', '437067', 'fig-p597060-steps-butane.png', 's1', '1.7 Example 1 steps: also, This is the')
repoint('597060', '437068', 'fig-p597060-steps-amine.png', 's2', '1.7 Example 2 steps: also, This is the')
repoint('597060', '437069', 'fig-p597060-steps-chlorobutane.png', 's3', '1.7 Example 3 steps: also, treat, This is the')
repoint('597104', '443598', 'fig-p597104-hemiacetal.png', 'hemi', '5.3 A hemiacetal')
repoint('597121', '26885', 'fig-p597121-anilines.jpg', 'anil', '7.1 m-chloroaniline')
repoint('597137', '128185', 'fig-p597137-glucose-cyclization.jpg', 'cycl', '8.4 Fig 8.4.1 representation; C2-OH bond')
repoint('597154', '25889', 'fig-p597154-zwitterion.jpg', 'zwit', '10.1 representation')
repoint('597159', '444684', 'fig-p597159-ghk.png', 'ghk', '10.6 GHK')
repoint('597159', '431812', 'fig-p597159-aspartame.png', 'aspt', '10.6 Aspartylphenylalanine, Aspartame')
repoint('597159', '431969', 'fig-p597159-backbone.png', 'bbone', '10.6 Fig 10.6.1 English terminus labels, N left / C right',
        alt='Ball-and-stick model of a polypeptide backbone with each planar peptide group drawn as a flat blue card; the chain runs from the N-terminus (labeled at the left) to the C-terminus (labeled at the right), and the R groups (purple) alternate above and below the chain.')
repoint('597161', '432382', 'fig-p597161-val-phe.png', 'valphe', '10.8 side chains')
repoint('597171', '129750', 'fig-p597171-feedback.jpg', 'thr', '11.6 Fig 11.6.2 Threonine x3')
repoint('597176', '139715', 'fig-p597176-base-pairs.jpg', 'bp', '12.2 Fig 12.2.3 1.08 nm')
repoint('597181', '26487', 'fig-p597181-dttp-azt.jpg', 'dttp', '12.8 triphosphate')
repoint('597188', '436240', 'fig-p597188-nad-nadh.png', 'nic', '13.1 Fig 13.1.2 Nicotinamide')
repoint('597191', '25812', 'fig-p597191-energy-conversions.jpg', 'econv', '13.3 Fig 13.3.1 Pyruvate, oxidation')
repoint('597200', '128220', 'fig-p597200-acetyl-coa.jpg', 'acoa', '14.1 Fig 14.1.1 Phosphorylated ADP')
repoint('597201', '86861', 'fig-p597201-etc.jpg', 'etc', '14.2 Fig 14.2.3 Fumarate, CoQ, NAD+, Pi, 2H+')
repoint('597203', '436865', 'fig-p597203-summary.png', 'summ', '14.4 Fig 14.4.3 pyruvate formula, for, net ATP, 2Pi, 2HS-CoA')
repoint('597209', '446290', 'fig-p597209-beta-oxidation.png', 'box', '15.4 Fig 15.4.1 acyl-CoA dehydrogenase, trans-enoyl-CoA, palmitoyl-CoA, FADH2')
repoint('597213', '26819', 'fig-p597213-ketone-bodies.png', 'ket', '15.5 HSCoA')
reput('597197', '512617', 'fig-p597197-4.svg', 'gng', '13.8 Fig 13.8.2 six reversible steps')
reput('597210', '512629', 'fig-p597210-1.svg', 'hub', '15.10 Fig 15.10.1 pyruvate carboxylase one-way')
e('597210', 'Double-headed arrows are two-way connections; the single arrow from pyruvate to acetyl CoA is the one-way street that keeps fat from becoming glucose.',
  'Double-headed arrows are two-way connections. Single arrows are one-way: pyruvate to acetyl CoA (the step that keeps fat from becoming glucose) and pyruvate to oxaloacetate (pyruvate carboxylase).', 1, '15.10.1 caption')
# instructor slide on GitHub Pages: cache-bust after merge
e('597167', 'figures/Slide26.png"', 'figures/Slide26.png?v=20261112"', 1, '11.2 Slide26 cache-bust (stray arrows removed)')

bad = 0
for p, es in edits.items():
    t = page(p)
    for x in es:
        if t.count(x['old']) != x['count']:
            bad += 1; print('MISMATCH', p, x['note'], t.count(x['old']))
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchB2_figures_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'mismatches')
