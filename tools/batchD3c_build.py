"""Batch D3c (review 2026-11-12): make every print strip of a figure print at the same scale.
Measured print rule (LibreTexts PDF): printed width = min(width attribute px x 0.75 pt, 522 pt text width,
216 pt x strip aspect), i.e. each image is capped at 3.0 in high. D3/D3b strips that were taller than
~1/2.42 of their width printed a few percent narrower than their neighbours, so edges jogged.
Fix: new cuts (tools/batchD3b_cuts_2026-11-12.json, optimal search with a strict aspect limit), and for
13.8.2, where no clean cut set exists, a 660 px width so all strips share one scale.
New files are written as <base>-v2-<k>.svg (no cached old file can be mixed in).
Replaces the strip runs already on the live pages (D3 glycolysis, D3b).
Output: tools/batchD3c_print_2026-11-12.json
"""
import json, re, glob

L = 'pages/live/'
BASE = 'https://itsdrdan.github.io/textbook/figures/print/'
cuts = json.load(open('tools/batchD3b_cuts_2026-11-12.json'))
WIDTH = {'fig-p597197-4.svg': 660}
REDO = ['fa_synthesis.svg', 'fig-p597194-1.svg', 'fig-p597197-4.svg', 'fig-p597202-1.svg', 'fig-p597210-1.svg',
        'nonessential_aa.svg', 'trna_loading.svg', 'full-investment.svg', 'full-payoff.svg']
MINW = 1040
edits = {}


def svgdims(name):
    s = open('figures/print/src/' + name, encoding='utf-8').read()
    return s, [float(v) for v in re.search(r'viewBox="([^"]+)"', re.search(r'<svg\b[^>]*>', s).group(0)).group(1).split()[2:]]


def strips(name):
    s, (W, H) = svgdims(name)
    m = re.search(r'<svg\b[^>]*>', s); root = m.group(0); body = s[m.end():]
    body = re.sub(r'(<rect\b[^>]*?)width="100%"', lambda q: q.group(1) + f'width="{W:g}"', body)
    body = re.sub(r'(<rect\b[^>]*?)height="100%"', lambda q: q.group(1) + f'height="{H:g}"', body)
    INTR = int(W) * -(-MINW // int(W))
    c = cuts[name]; out = []
    for k, (a, b) in enumerate(zip(c, c[1:]), 1):
        h = b - a
        r = re.sub(r'viewBox="[^"]+"', f'viewBox="0 {a} {W:g} {h}"', root)
        r = re.sub(r'\swidth="[^"]*"', f' width="{INTR}"', r, 1)
        r = re.sub(r'\sheight="[^"]*"', f' height="{int(INTR * h // W)}"', r, 1)
        bd = body
        if k > 1:
            r = re.sub(r'\s(role|aria-label|aria-labelledby)="[^"]*"', '', r).replace('<svg', '<svg aria-hidden="true"', 1)
            bd = re.sub(r'<title>.*?</title>', '', bd, flags=re.S); bd = re.sub(r'<desc>.*?</desc>', '', bd, flags=re.S)
        fn = f'{name[:-4]}-v2-{k}.svg'
        open('figures/print/' + fn, 'w', encoding='utf-8').write(r + bd)
        out.append(fn)
    return out, W, [b - a for a, b in zip(c, c[1:])]


def screen_px(tag):
    w = re.search(r'\swidth="(\d+)"', tag)
    if w: return int(w.group(1))
    w = re.search(r'(?:^|[;"])\s*width:\s*(\d+)px', tag)
    if w: return int(w.group(1))
    w = re.search(r'max-width:\s*(\d+)px', tag)
    return int(w.group(1)) if w else None


for f in sorted(glob.glob(L + '*.html')):
    p = f.split('/')[-1][:-5]; t = open(f, encoding='utf-8').read()
    for name in REDO:
        base = name[:-4]
        run = re.search(r'(?:<img[^>]*src="[^"]*/print/' + re.escape(base) + r'-\d+\.svg"[^>]*>)+', t)
        if not run: continue
        old = run.group(0); assert t.count(old) == 1
        first = re.match(r'<img[^>]*>', old).group(0)
        files, W, hs = strips(name)
        if name in WIDTH:
            first = re.sub(r'\swidth="\d+"', f' width="{WIDTH[name]}"', first)
        px = screen_px(first)
        P = min(px * 0.75 if px else 1e9, 522)
        caps = [216 * W / h for h in hs]
        assert min(caps) >= P - 0.5, (name, P, [round(x) for x in caps])
        new = []
        for k, fn in enumerate(files, 1):
            tag = re.sub(r'src="[^"]*"', f'src="{BASE}{fn}"', first)
            if k > 1: tag = re.sub(r'alt="[^"]*"', 'alt=""', tag)
            new.append(tag)
        edits.setdefault(p, []).append({'old': old, 'new': ''.join(new), 'count': 1,
                                        'note': f'{name}: {len(files)} strips, uniform print width {P:.0f} pt'})
        print(p, name, len(files), 'strips; print width', round(P), 'pt; tallest-strip cap', round(min(caps)))

json.dump(edits, open('tools/batchD3c_print_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
