"""Batch D3 (review 2026-11-12): Figure 13.5.1 glycolysis overview prints readably.
The two tall SVGs (full-investment, full-payoff) are replaced by six horizontal strips each
(figures/pathways/glycolysis/print/), cut along blank bands between steps. On screen the strips stack
seamlessly (display:block); in print each strip is sized like a normal figure instead of being capped
at ~3 in high. The first strip carries the alt text; the others are decorative (alt="").
The 14.3 citric acid cycle wheel is left as is (no blank bands to cut; step figures print readably).
Output: tools/batchD3_print_2026-11-12.json {page: [{old,new,count,note}]}, checked against pages/live.
"""
import json, re

L = 'pages/live/'
BASE = 'https://itsdrdan.github.io/textbook/figures/pathways/glycolysis/'
p = '597193'
t = open(L + p + '.html', encoding='utf-8').read()
edits = {p: []}
for name in ('full-investment', 'full-payoff'):
    m = re.search(r'<img src="' + re.escape(BASE + name + '.svg') + r'" alt="([^"]*)"[^>]*/>', t)
    old, alt = m.group(0), m.group(1)
    assert t.count(old) == 1
    strips = []
    for k in range(1, 7):
        a = alt if k == 1 else ''
        strips.append(f'<img src="{BASE}print/{name}-{k}.svg" alt="{a}" width="600" style="display:block;max-width:100%;height:auto;margin:0" />')
    edits[p].append({'old': old, 'new': ''.join(strips), 'count': 1, 'note': f'13.5 Fig 13.5.1 {name} as 6 print strips'})
json.dump(edits, open('tools/batchD3_print_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(len(edits[p]), 'edits')
