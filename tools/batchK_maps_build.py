"""Batch K (optional work): concept maps regenerated larger for print (tools/concept_maps.py now renders with
tools/pathway.py, a Python port of pathway.js; font 17 / edge labels 14, notes wrap at 16 characters, rowh 100).
The 15 Chapter Guide pages get a cache-bust on the map's img src and full-size link so browsers and the PDF
service fetch the new files from GitHub Pages.
Output: tools/batchK_maps_2026-11-13.json"""
import json, re, glob
edits = {}
for f in sorted(glob.glob('pages/live/*.html')):
    t = open(f, encoding='utf-8').read(); p = f.split('/')[-1][:-5]
    for m in re.finditer(r'(src|href)="(https://itsdrdan\.github\.io/textbook/figures/conceptmaps/ch\d\d\.svg)"', t):
        old = m.group(0); assert t.count(old) == 1
        edits.setdefault(p, []).append({'old': old, 'new': f'{m.group(1)}="{m.group(2)}?v=20261113"', 'count': 1, 'note': 'concept map cache-bust (larger print type)'})
json.dump(edits, open('tools/batchK_maps_2026-11-13.json', 'w'), indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
