"""Batch B1 slides: alt text + cache-busting src for the instructor's slides patched in figures/ (2026-11-12).
Publish only after the slide PNGs are on main (GitHub Pages serves main)."""
import json
L = 'pages/live/'
E = {}
def e(p, old, new, n=1, note=''): E.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})
V = '?v=20261112'
for p, s in [('597121', 'Slide21'), ('597123', 'Slide22'), ('597145', 'Slide48'), ('597145', 'Slide49'), ('597145', 'Slide51'), ('597145', 'Slide52')]:
    e(p, f'figures/{s}.png"', f'figures/{s}.png{V}"', 1, f'{s} cache-bust')
e('597123', 'First: ammonia, NH3, plus H2O gives the ammonium ion', 'First: ammonia, NH3, plus H2O, with an equilibrium (double half-arrow) arrow, gives the ammonium ion', 1, 'Slide22 alt')
e('597123', 'Second: methylamine, CH3-NH2, plus H2O gives the methylammonium ion', 'Second: methylamine, CH3-NH2, plus H2O, again with an equilibrium arrow, gives the methylammonium ion', 1, 'Slide22 alt')
e('597123', 'Third: methylamine plus HCl gives', 'Third: methylamine plus HCl, with a one-way arrow, gives', 1, 'Slide22 alt')
e('597145', 'Glyceryl palmitate (tripalmitin) plus 3 H2O', 'Glyceryl tripalmitate (tripalmitin) plus 3 H2O', 1, 'Slide48 alt')
e('597145', 'and a chain with two cis double bonds, plus 3 H2O with KOH and heat over the arrow.', 'and a chain with two cis double bonds, plus 3 KOH with heat under the arrow.', 1, 'Slide48 alt')
e('597145', 'Glyceryl palmitate (tripalmitin) plus 3 NaOH', 'Glyceryl tripalmitate (tripalmitin) plus 3 NaOH', 1, 'Slide49 alt')
e('597145', 'on glycerol, plus Br2, arrow to the product', 'on glycerol, plus 3 Br2, arrow to the product', 1, 'Slide51 alt')
e('597145', 'the same glyceryl trioleate plus 3 H2O with LiOH and heat over the arrow.', 'the same glyceryl trioleate plus 3 LiOH with heat under the arrow.', 1, 'Slide51 alt')
e('597145', 'C(=O)(CH2)7CH=CH(CH2)7CH3, plus H2 with Ni written over the arrow.', 'C(=O)(CH2)7CH=CH(CH2)7CH3, plus 3 H2 with Ni written over the arrow.', 1, 'Slide52 alt')
bad = 0
for p, es in E.items():
    t = open(L + p + '.html', encoding='utf-8').read()
    for x in es:
        c = t.count(x['old'])
        if c != x['count']: bad += 1; print('MISMATCH', p, x['note'], c)
json.dump(E, open('tools/batchB1_slides_fixes_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in E.values()), 'edits;', bad, 'mismatches')
