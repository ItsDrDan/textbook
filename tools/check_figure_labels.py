"""Regression check for figure label sizes (2026-11-13).
Every figure listed in tools/figure_label_floors.json had labels that printed under 6 pt and was enlarged. The manifest
records, per file, the smallest font size (SVG px) a WORD label may have; at that size it prints at 6 pt or more.
Run this after regenerating or editing any figure:   python3 tools/check_figure_labels.py        (exit 1 on a regression)
To record a new floor after a deliberate change:      python3 tools/check_figure_labels.py --update
Word label = a text run with four or more letters in a row (subscripts, charges and single symbols are ignored)."""
import json, re, sys, os, html
MAN = 'tools/figure_label_floors.json'

def smallest(svg):
    best = None; stack = [None]
    for m in re.finditer(r'<(/?)(g|text)\b([^>]*)>', svg):
        close, tag, attrs = m.groups()
        if tag == 'g':
            if close:
                if len(stack) > 1: stack.pop()
            else:
                f = re.search(r'font-size="([\d.]+)', attrs); stack.append(float(f.group(1)) if f else stack[-1])
        elif not close and not attrs.rstrip().endswith('/'):
            f = re.search(r'font-size="([\d.]+)', attrs); cur = [float(f.group(1)) if f else stack[-1]]
            body = svg[m.end():svg.find('</text>', m.end())]
            for p in re.split(r'(<tspan\b[^>]*>|</tspan>)', body):
                if p.startswith('<tspan'):
                    g = re.search(r'font-size="([\d.]+)', p); cur.append(float(g.group(1)) if g else cur[-1])
                elif p == '</tspan>':
                    if len(cur) > 1: cur.pop()
                elif cur[-1] and re.search(r'[A-Za-z]{4}', html.unescape(re.sub(r'<[^>]+>', '', p))):
                    best = cur[-1] if best is None else min(best, cur[-1])
    return best

man = json.load(open(MAN)) if os.path.exists(MAN) else {}
if '--update' in sys.argv:
    for f in list(man): man[f]['floor'] = smallest(open(f, encoding='utf-8').read())
    json.dump(man, open(MAN, 'w'), indent=1); print('floors recorded for', len(man), 'files'); sys.exit(0)
bad = 0
for f, m in sorted(man.items()):
    if not os.path.exists(f): print('MISSING', f); bad += 1; continue
    s = smallest(open(f, encoding='utf-8').read())
    if s is None or s + 1e-6 < m['floor']: print('TOO SMALL %s: smallest word label %s px, floor %s px (%s)' % (f, s, m['floor'], m.get('note', ''))); bad += 1
print(len(man), 'figures checked;', bad, 'below their floor')
sys.exit(1 if bad else 0)
