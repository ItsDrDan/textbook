"""Batch B1 (wrong structures in figures), review of 2026-11-12.

Builds tools/batchB1_figures_2026-11-12.json:
  uploads: files to PUT to /@api/deki/pages/{page}/files/={name}; bytes come from raw.githubusercontent (path).
           key names a placeholder {{key}} used in the edits for the new file id.
           old_fileid: when set, the page already shows that file; if the upload returns a different id,
           the publisher rewrites files/{old}/ and fileid="{old}" to the new id.
  edits:   {page: [{old, new, count, note}]}; checked against pages/live.
Assets: figures/pages/batchB/ (drawn with tools/rdsvg.py, or patched rasters).
"""
import json, re

L = 'pages/live/'
A = 'figures/pages/batchB/'
uploads, edits = [], {}


def page(p):
    return open(L + p + '.html', encoding='utf-8').read()


def svg_size(path):
    s = open(path).read(200000)
    m = re.search(r'<svg[^>]*\swidth="(\d+)"\s+height="(\d+)"', s)
    return int(m.group(1)), int(m.group(2))


def svg_alt(path):
    return re.search(r'aria-label="([^"]*)"', open(path).read()).group(1)


def img_tag(p, fid):
    t = page(p); i = t.find(f'files/{fid}/'); a = t.rfind('<img', 0, i); b = t.find('>', i) + 1
    return t[a:b]


def e(p, old, new, n=1, note=''):
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


def up(p, name, path, key, old_fileid=None):
    uploads.append({'page': p, 'name': name, 'path': path, 'key': key, 'old_fileid': old_fileid})


def replace_img(p, fid, key, fname, note, width=None, alt=None):
    """Swap an existing <img> for a new house image (new file name)."""
    old = img_tag(p, fid)
    path = A + fname
    w = width or (svg_size(path)[0] if fname.endswith('.svg') else None)
    alt = alt or svg_alt(path)
    new = (f'<img class="internal" alt="{alt}"' + (f' width="{w}"' if w else '') +
           f' style="max-width:100%;height:auto;" src="/@api/deki/files/{{{{{key}}}}}/{fname}" fileid="{{{{{key}}}}}" />')
    up(p, fname, path, key)
    e(p, old, new, 1, note)


def reput(p, fid, fname, path, key, note, alt=None, width=None):
    """Upload a corrected file under the same name; update alt/width in the existing tag."""
    old = img_tag(p, fid)
    new = old
    if alt is not None:
        new = re.sub(r'alt="[^"]*"', 'alt="' + alt + '"', new)
    if width is not None:
        new = re.sub(r'\swidth="[^"]*"', f' width="{width}"', new)
    up(p, fname, path, key, old_fileid=fid)
    if new != old:
        e(p, old, new, 1, note)


BALL = '(Figure from <em>The Basics of General, Organic, and Biological Chemistry</em> by Ball, Hill and Scott, CC BY-NC-SA 3.0.)'
REDRAWN = '(Structure redrawn by Daniel Kwasniewski, CC BY 4.0.)'

# 4.3 Figure 4.3.2 printed an unrelated atom picture: the src name "%253D14.3.jpg" resolves to another file in the PDF service.
replace_img('597092', '87067', 'ethw', 'fig-p597092-ethanol-water.jpg', '4.3 Fig 4.3.2 clean file name (print showed an atom)',
            width=456, alt=re.search(r'alt="([^"]*)"', img_tag('597092', '87067')).group(1))
# 4.7 hexylresorcinol (OH groups were 1,2)
replace_img('597096', '128173', 'hexr', 'fig-p597096-hexylresorcinol.svg', '4.7 4-hexylresorcinol 1,3-OH')
e('597096', 'for use on the skin. ' + BALL, 'for use on the skin. ' + REDRAWN, 1, '4.7 credit')
# 9.6 Table 9.6.1 estradiol (no C10 methyl), testosterone (C4=C5)
replace_img('597149', '128212', 'estr', 'fig-p597149-estradiol.svg', '9.6 estradiol', width=210)
replace_img('597149', '128211', 'test', 'fig-p597149-testosterone.svg', '9.6 testosterone', width=210)
# 5.2 Figure 5.2.2 aldehydes (vanillin was isovanillin)
replace_img('597103', '27163', 'alds', 'fig-p597103-aldehydes.svg', '5.2 Fig 5.2.2 aldehydes (vanillin)')
e('597103', 'gives a cucumber odor. ' + BALL, 'gives a cucumber odor. ' + REDRAWN, 1, '5.2 credit')
# 5.4 NAD+/NADH labels swapped (label swap in the raster)
reput('597105', '428509', 'clipboard_e088725e6d635758cd3fd48997501f928.png', A + 'fig-p597105-nad-nadh.png', 'nad', '5.4 NAD labels',
      alt=img_tag('597105', '428509').split('alt="')[1].split('"')[0].replace('Structures of NAD plus (left) and NADH (right)', 'Structures of NADH (left) and NAD plus (right)'))
# 4.5 isocitrate -> oxalosuccinate (product had CH3), Exercise 4.5.1(b)
replace_img('597094', '27099', 'isoc', 'fig-p597094-isocitrate.svg', '4.5 isocitrate')
replace_img('597094', '27103', 'ex1b', 'fig-p597094-ex1b.svg', '4.5 Exercise 1(b)', width=153)
# 7.3 octylamine has 8 carbons
replace_img('597123', '27012', 'octa', 'fig-p597123-octylamine.svg', '7.3 octylamine (CH2)7')
# 7.10 nylon synthesis: n and 2n H2O; 7.10.1 repeat units
replace_img('597130', '404867', 'nyls', 'fig-p597130-nylon-synthesis.svg', '7.10 Fig 7.10.2 nylon synthesis')
e('597130', 'Figure \\(\\PageIndex{2}\\): Nylon synthesis. (Figure from <em>Fundamentals of General, Organic, and Biological Chemistry</em> (LibreTexts), CC BY-NC-SA 3.0.)',
  'Figure \\(\\PageIndex{2}\\): Nylon synthesis. Two water molecules are released for each repeat unit. ' + REDRAWN, 1, '7.10 caption')
reput('597130', '512541', 'fig-p597130-2.svg', A + 'fig-p597130-2.svg', 'nylr', '7.10.1 nylon repeat unit',
      alt=svg_alt(A + 'fig-p597130-2.svg'), width=svg_size(A + 'fig-p597130-2.svg')[0])
reput('597130', '512542', 'fig-p597130-3.svg', A + 'fig-p597130-3.svg', 'petr', '7.10.1 PET repeat unit',
      alt=svg_alt(A + 'fig-p597130-3.svg'), width=svg_size(A + 'fig-p597130-3.svg')[0])
e('597130', '<small>a segment of nylon-6,6: amide links join a 6-carbon diacid to a 6-carbon diamine</small>',
  '<small>one repeat unit of nylon-6,6: amide links join a 6-carbon diacid unit to a 6-carbon diamine unit</small>', 1, '7.10.1 label')
# 6.7 PET formation: 2n H2O
replace_img('597115', '51930', 'petf', 'fig-p597115-pet-formation.svg', '6.7 PET formation 2n H2O')
# 2.5 Exercise 2.5.1 structure 3 (branches on C3; heptane per the answer key)
replace_img('597069', '27443', 'ex13', 'fig-p597069-ex1-3.svg', '2.5 Exercise 1 structure 3', width=256)
# 1.8 Figure 1.8.11: thymine CH3 and P-O-CH2 link (raster patch)
reput('597061', '137586', 'CNX_Chem_10_01_DNA2.jpg', A + 'fig-p597061-dna-basepairs.jpg', 'dna', '1.8 Fig 1.8.11 thymine CH3')
e('597061', 'so-called &ldquo;complementary base pairs.&rdquo;. ' + BALL,
  'so-called &ldquo;complementary base pairs.&rdquo; ' + BALL[:-2] + '; thymine methyl group and one backbone CH<sub>2</sub> corrected by Daniel Kwasniewski.)', 1, '1.8 caption')
# 13.1 Figure 13.1.3 FADH2 N5 (raster patch)
reput('597188', '436239', 'clipboard_ebfd50d4ea43cb38a2ee231dcba617316.png', A + 'fig-p597188-fad-fadh2.png', 'fad', '13.1 FADH2 N5')
e('597188', '\\(\\ce{2H^{+}}\\) + \\(\\ce{2e^{-}}\\). (Copyright; Public domain)</figcaption>',
  '\\(\\ce{2H^{+}}\\) + \\(\\ce{2e^{-}}\\). (Public domain; N5 of FADH<sub>2</sub> corrected by Daniel Kwasniewski.)</figcaption>', 1, '13.1 caption')
# 12.8 raltegravir (gem-dimethyl, amide NH)
replace_img('597181', '26486', 'ralt', 'fig-p597181-raltegravir.svg', '12.8 raltegravir')
# 9.1 Figure 9.1.3 thromboxane B2, leukotriene B4 (house files, same names)
reput('597144', '512575', 'fig-p597144-5.svg', A + 'fig-p597144-5.svg', 'txb2', '9.1 TXB2', alt=svg_alt(A + 'fig-p597144-5.svg'), width=300)
reput('597144', '512576', 'fig-p597144-6.svg', A + 'fig-p597144-6.svg', 'ltb4', '9.1 LTB4', alt=svg_alt(A + 'fig-p597144-6.svg'), width=513)
# 3.7 / 3.8 nitro groups with charges
reput('597084', '512441', 'fig-p597084-2.svg', A + 'fig-p597084-2.svg', 'nitb', '3.7 nitrobenzene', alt=svg_alt(A + 'fig-p597084-2.svg'), width=106)
reput('597085', '512447', 'fig-p597085-5.svg', A + 'fig-p597085-5.svg', 'nitp', '3.8 2-nitrophenol', alt=svg_alt(A + 'fig-p597085-5.svg'), width=156)
# 8.6 Disaccharide W, 8.9 Disaccharide Z: glucose C4
reput('597139', '512567', 'fig-p597139-1.svg', A + 'fig-p597139-1.svg', 'dsw', '8.6 Disaccharide W', alt=svg_alt(A + 'fig-p597139-1.svg'))
reput('597142', '512570', 'fig-p597142-3.svg', A + 'fig-p597142-3.svg', 'dsz', '8.9 Disaccharide Z')

# Text-side figure fixes
e('597060', ' or \\(\\ce{CH3CH2CH2CH(CH2CH3)CH2CH2CH2CH3}\\)</figure>',
  ' or CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH(CH<sub>2</sub>CH<sub>3</sub>)CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub></figure>', 1, '1.7 Fig 1.7.3 second condensed formula (did not print)')
e('597059', 'class="internal default mt-indent-3" src="/@api/deki/files/240660/Alkanes.jpg"',
  'class="internal default" style="max-width:100%;height:auto;" src="/@api/deki/files/240660/Alkanes.jpg"', 1, '1.6 Fig 1.6.1 indent cropped it in print')
e('597160', 'The two neighboring chains are <strong>parallel</strong> if both have N-terminus on the same side, as shown on the right, and <strong>antiparallel </strong>if the two adjacent chains have N-terminus on the opposite sides, as shown on the left.',
  'The two neighboring chains are <strong>parallel</strong> if both have the N-terminus on the same side, and <strong>antiparallel</strong> if the two adjacent chains have their N-termini on opposite sides; one drawing of each type is shown here.', 1, '10.7 left/right does not survive print')

bad = 0
for p, es in edits.items():
    t = page(p)
    for x in es:
        c = t.count(x['old'])
        if c != x['count']:
            bad += 1; print('MISMATCH', p, x['note'], c)
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchB1_figures_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'mismatches')
