"""Scan pages/live for figure-number clashes (C1, review 2026-11-12)."""
import re, glob, json, html
snap = open('pages/LIVE_SNAPSHOT.md').read()
titles = dict(re.findall(r'\[(\d+)\]\([^)]*\) \| ([^|\n]+?) \|', snap))
CAP = re.compile(r'(<figcaption>|<p[^>]*>\s*(?:<strong>|<em>)*)\s*(?:<strong>|<em>)*\s*Figure\s+(\\\(\\PageIndex\{(\w+)\}\\\)|(\d+)\.(\d+)(?:\.(\d+))?)\s*[:.]?', re.S)
out = {}
for f in sorted(glob.glob('pages/live/*.html')):
    p = f.split('/')[-1][:-5]; t = open(f, encoding='utf-8').read(); title = titles.get(p, '')
    m = re.match(r'\s*(\d+)\.(\d+):', title)
    if not m: continue
    sec = f'{m.group(1)}.{m.group(2)}'
    labs = []
    for c in CAP.finditer(t):
        if c.group(3):
            labs.append(('pi', c.group(3), f'{sec}.{c.group(3)}', c.start()))
        elif c.group(6):
            labs.append(('hard', f'{c.group(4)}.{c.group(5)}.{c.group(6)}', f'{c.group(4)}.{c.group(5)}.{c.group(6)}', c.start()))
        else:
            labs.append(('two', f'{c.group(4)}.{c.group(5)}', f'{c.group(4)}.{c.group(5)}', c.start()))
    rendered = [l[2] for l in labs]
    dups = sorted({r for r in rendered if rendered.count(r) > 1})
    two = [l[1] for l in labs if l[0] == 'two']
    wrongsec = [l[1] for l in labs if l[0] == 'hard' and not l[1].startswith(sec + '.')]
    if dups or two or wrongsec:
        out[p] = {'sec': sec, 'title': title, 'labels': [(l[0], l[1]) for l in labs], 'dups': dups, 'two': two, 'wrongsec': wrongsec}
json.dump(out, open('tools/figscan_2026-11-12.json', 'w'), indent=1)
print(len(out), 'pages flagged')
for p, v in out.items():
    print(p, v['sec'], 'dups', v['dups'], 'two', v['two'], 'wrongsec', v['wrongsec'], '|', ' '.join(a + ':' + b for a, b in v['labels']))
