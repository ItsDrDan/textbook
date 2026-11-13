"""Batch D4 (review 2026-11-12): wrap narrow figures so text runs beside them, in print as on screen.
The PDF ignores LibreTexts' float classes but honours inline styles (tested on 1.8, Figure 1.8.9).
Group A  images with class "internal left/right" (float on screen only):
         small ones get an inline float (class wrap-left/right, max-width 45%);
         seven large diagrams get display:block instead, so screen and print both show them full width.
Group B  captioned figures that print alone and narrow: the outer <figure> gets class wrap-right and an inline
         float with a width close to its current printed width; images inside get max-width:100%;height:auto.
Every edited page gets the phone rule (un-float below 640 px) in its style block (added if missing).
Output: tools/batchD4_wraps_2026-11-12.json {page:[{old,new,count,note}]}, replay-checked.
"""
import json, re

L = 'pages/live/'
pages, edits = {}, {}
PHONE = ('@media screen and (max-width: 640px) { figure.wrap-right, figure.wrap-left, img.wrap-right, img.wrap-left '
         '{ float: none !important; width: auto !important; max-width: 100% !important; margin: 1em auto !important; display: block; } }')


def T(p):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read()
    return pages[p]


def rep(p, old, new, note):
    t = T(p); assert t.count(old) == 1, (p, note, t.count(old))
    pages[p] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})


def img_fix(tag):
    """Images inside a wrapped figure must shrink with it."""
    if 'style="' in tag:
        if 'max-width' in tag:  # side-by-side composites keep their own share (e.g. max-width:48%)
            return tag
        return re.sub(r'style="([^"]*)"', lambda m: 'style="' + m.group(1).rstrip('; ') + ';max-width:100%;height:auto;"', tag, 1)
    return tag.replace('<img', '<img style="max-width:100%;height:auto;"', 1)


def outer_figure(t, i):
    """Span of the outermost <figure> element that contains index i."""
    best = None
    for m in re.finditer(r'<figure\b[^>]*>', t[:i]):
        depth, j = 1, m.end()
        while depth:
            o = t.find('<figure', j); c = t.find('</figure>', j)
            if o != -1 and o < c: depth += 1; j = o + 7
            else: depth -= 1; j = c + 9
        if m.start() < i < j and (best is None or m.start() < best[0]): best = (m.start(), j)
    return best


# ---- Group A
def find_float(t, a):
    for m in re.finditer(r'<img\b[^>]*class="internal (left|right)"[^>]*>', t):
        if re.search(r'alt="' + re.escape(a), m.group(0)): return m
    return None


FLOAT = {  # page: alt-text starts of the small images that should float in print too
    '597057': ['Two ways to show the polar H-Cl bond'],
    '597146': ['A phospholipid space-filling model', 'Photograph of a snake wrangler', 'Line-angle structure of a lysophospholipid', 'Line-angle structure of a phosphatidic acid'],
    '597159': ['Medical illustration comparing (A) normal'],
    '597160': ['An alpha-helix model', 'Ribbon model of a beta-sheet', 'An antiparallel beta-pleated sheet', 'A parallel beta-pleated sheet'],
    '597188': ['Illustration of the human digestive system', 'Diagram of an animal cell', 'Cutaway diagram of a mitochondrion'],
    '597203': ['Coenzyme Q (ubiquinone', 'The heme of cytochrome c'],
    '597209': ['Photograph of two polar bears', 'Photograph of an orca', 'Photograph of a camel', 'Photograph of a large flock'],
}
BLOCK = {
    '597188': ['Overview of metabolism inside a cell', 'Stages of food catabolism'],
    '597203': ['Complex I of the electron transport chain', 'Complex II: succinate', 'Complex IV: four reduced', 'ATP synthase in the inner membrane', 'Summary of glucose catabolism'],
}
for p, alts in FLOAT.items():
    for a in alts:
        m = find_float(T(p), a)
        assert m, (p, a)
        side = m.group(1); tag = m.group(0)
        st = (f'float:{side};max-width:45%;height:auto;' + ('margin:0 16px 8px 0;' if side == 'left' else 'margin:0 0 8px 16px;'))
        new = tag.replace(f'class="internal {side}"', f'class="internal wrap-{side}"')
        new = new.replace('<img', f'<img style="{st}"', 1) if 'style="' not in new else re.sub(r'style="[^"]*"', f'style="{st}"', new, 1)
        rep(p, tag, new, f'A float in print: {a}')
for p, alts in BLOCK.items():
    for a in alts:
        m = find_float(T(p), a)
        assert m, (p, a)
        tag = m.group(0)
        new = tag.replace(f'class="internal {m.group(1)}"', 'class="internal"')
        new = new.replace('<img', '<img style="display:block;max-width:100%;height:auto;margin:0 auto 8px;"', 1) if 'style="' not in new else re.sub(r'style="[^"]*"', 'style="display:block;max-width:100%;height:auto;margin:0 auto 8px;"', new, 1)
        rep(p, tag, new, f'A full width on screen and in print: {a}')

# ---- Group B: (page, caption snippet, width %)
B = [('597057', 'Linus Pauling was one of', 28),
     ('597061', 'Sodium Chloride. Solid NaCl', 40), ('597061', 'Two separate DNA molecules f', 28),
     ('597070', 'Oil Spills. Crude oil coats', 30), ('597073', 'Ball-and-Spring Model of Cyc', 31),
     ('597092', 'Hydrogen Bonding between Eth', 36), ('597105', "Tollens' test for aldehydes", 30),
     ('597130', 'Nylon spatula', 22), ('597136', 'Fischer projection of D-gluc', 22), ('597146', 'Lipid bilayer cross-section', 36),
     ('597148', 'Spontaneously Formed Polar L', 26), ('597158', 'A Ball-and-Stick Model of an', 33),
     ('597159', 'Illustration of disulfide li', 38), ('597163', 'Illustration of plaque forma', 40),
     ('597181', 'Viruses. Viruses come in a v', 40)]
skipped = []
for p, snip, w in B:
    t = T(p)
    i = t.find('<figcaption>' + 'Figure'); k = -1
    for m in re.finditer(r'<figcaption>', t):
        e = t.find('</figcaption>', m.end())
        if snip in t[m.end():e] or snip.replace("'", '&#39;') in t[m.end():e] or snip.replace("'", '&rsquo;') in t[m.end():e]:
            k = m.end(); break
    if k < 0: skipped.append((p, snip, 'caption not in a figcaption')); continue
    span = outer_figure(t, k)
    if not span: skipped.append((p, snip, 'no enclosing figure')); continue
    a, b = span; seg = t[a:b]
    open_tag = re.match(r'<figure\b[^>]*>', seg).group(0)
    if 'float' in open_tag: skipped.append((p, snip, 'already floats')); continue
    new_open = f'<figure class="wrap-right" style="float:right;width:{w}%;margin:0 0 8px 16px">'
    if 'class=' in open_tag and 'class="figure"' not in open_tag: skipped.append((p, snip, 'figure has a class: ' + open_tag)); continue
    new = new_open + re.sub(r'<img\b[^>]*>', lambda m: img_fix(m.group(0)), seg[len(open_tag):])
    rep(p, seg, new, f'B wrap right {w}%: {snip}')

# ---- phone rule
for p in list(edits):
    t = T(p)
    m = re.search(r'<style type="text/css">/\*<!\[CDATA\[\*/(.*?)/\*\]\]>\*/</style>', t, re.S)
    if m:
        if 'img.wrap-left' in m.group(1): continue
        rep(p, m.group(0), m.group(0).replace('/*]]>*/', ' ' + PHONE + '/*]]>*/'), 'phone rule for wraps')
    else:
        assert '<style' not in t, p
        first = t[:200]
        rep(p, first, f'<style type="text/css">/*<![CDATA[*/{PHONE}/*]]>*/</style>\n' + first, 'phone rule for wraps (new style block)')

bad = 0
for p, es in edits.items():
    t = open(L + p + '.html', encoding='utf-8').read()
    for x in es:
        if t.count(x['old']) != 1: bad += 1; print('REPLAY FAIL', p, x['note'])
        t = t.replace(x['old'], x['new'])
json.dump(edits, open('tools/batchD4_wraps_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'replay failures')
for s in skipped: print('SKIPPED', s)
