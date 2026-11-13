"""Batch D3b (review 2026-11-12): tall house diagrams print readably as stacked strips.
LibreTexts' PDF caps every image at about 3 in high (and at the text width), so a tall or square diagram prints
with 3-5 pt text. Cutting it along clean rows (no text, no node boxes) into strips that are each at least
~2.3x wider than tall lets every strip print at full text width. On screen the strips stack seamlessly
(display:block, same width as before).
Sources: figures/print/src/<name>.svg (copies of the live files); cut rows: tools/batchD3b_cuts_2026-11-12.json
(found by a row-ink scan that forbids text lines and node boxes).
Outputs: figures/print/<base>-<k>.svg, tools/batchD3b_print_2026-11-12.json {page:[{old,new,count,note}]}.
"""
import json, re

L = 'pages/live/'
BASE = 'https://itsdrdan.github.io/textbook/figures/print/'
cuts = json.load(open('tools/batchD3b_cuts_2026-11-12.json'))
MINW = 1040  # intrinsic width needed for full text width in print; an integer multiple of W keeps strip heights exact
edits = {}


def strips(name):
    s = open('figures/print/src/' + name, encoding='utf-8').read()
    m = re.search(r'<svg\b[^>]*>', s)
    root = m.group(0)
    W, H = [float(v) for v in re.search(r'viewBox="([^"]+)"', root).group(1).split()[2:]]
    body = s[m.end():]
    # percentage-sized rects must become absolute, or each strip redraws them
    body = re.sub(r'(<rect\b[^>]*?)width="100%"', lambda q: q.group(1) + f'width="{W:g}"', body)
    body = re.sub(r'(<rect\b[^>]*?)height="100%"', lambda q: q.group(1) + f'height="{H:g}"', body)
    INTR = int(W) * -(-MINW // int(W)); assert INTR % W == 0
    c = cuts[name]; out = []
    for k, (a, b) in enumerate(zip(c, c[1:]), 1):
        h = b - a
        r = re.sub(r'viewBox="[^"]+"', f'viewBox="0 {a} {W:g} {h}"', root)
        r = re.sub(r'\swidth="[^"]*"', f' width="{INTR}"', r, 1)
        r = re.sub(r'\sheight="[^"]*"', f' height="{int(INTR * h // W)}"', r, 1)
        bd = body
        if k > 1:
            r = re.sub(r'\s(role|aria-label|aria-labelledby)="[^"]*"', '', r).replace('<svg', '<svg aria-hidden="true"', 1)
            bd = re.sub(r'<title>.*?</title>', '', bd, flags=re.S)
            bd = re.sub(r'<desc>.*?</desc>', '', bd, flags=re.S)
        fn = f'{name[:-4]}-{k}.svg'
        open('figures/print/' + fn, 'w', encoding='utf-8').write(r + bd)
        out.append(fn)
    return out


rows = {}
for f in __import__('glob').glob(L + '*.html'):
    t = open(f, encoding='utf-8').read()
    for name in cuts:
        if re.search(r'<img[^>]*src="[^"]*/' + re.escape(name) + '"', t):
            rows[name] = f.split('/')[-1][:-5]

for name in sorted(cuts):
    p = rows[name]; t = open(L + p + '.html', encoding='utf-8').read()
    m = re.search(r'<img[^>]*src="[^"]*/' + re.escape(name) + r'"[^>]*>', t)
    old = m.group(0); assert t.count(old) == 1
    files = strips(name)
    new = []
    for k, fn in enumerate(files, 1):
        tag = re.sub(r'src="[^"]*"', f'src="{BASE}{fn}"', old)
        tag = re.sub(r'\sfileid="[^"]*"', '', tag).replace(' class="internal"', '')
        if k > 1: tag = re.sub(r'alt="[^"]*"', 'alt=""', tag)
        if 'style="' in tag: tag = tag.replace('style="', 'style="display:block;margin:0;', 1)
        else: tag = tag.replace('<img', '<img style="display:block;margin:0;"', 1)
        new.append(tag)
    edits.setdefault(p, []).append({'old': old, 'new': ''.join(new), 'count': 1, 'note': f'{name} as {len(files)} print strips'})

bad = 0
for p, es in edits.items():
    t = open(L + p + '.html', encoding='utf-8').read()
    for x in es:
        if t.count(x['old']) != 1: bad += 1; print('REPLAY FAIL', p, x['note'])
        t = t.replace(x['old'], x['new'])
json.dump(edits, open('tools/batchD3b_print_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'replay failures')
