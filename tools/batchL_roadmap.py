"""Reaction Roadmap (7.12) redrawn for print: same spec (sections/reactions/roadmap_spec.json), rows packed,
larger type (16/13), cropped to content so width >= 2.5 x height (the PDF caps images at 3 in high).
Writes sections/reactions/roadmap.svg (the old one printed its labels at ~4.3 pt)."""
import json, re, sys
sys.path.insert(0, 'tools')
from pathway import render

spec = json.load(open('sections/reactions/roadmap_spec.json'))
old = open('sections/reactions/roadmap.svg', encoding='utf-8').read()
alt = re.search(r'aria-label="([^"]*)"', old).group(1)
for n in spec['nodes']:
    if n['id'] == 'ester': n['row'] = 0.3
for e in spec['edges']:
    if (e['from'], e['to']) == ('ester', 'salt'): e['label'] = 'NaOH\n(saponify)'
    if (e['from'], e['to']) == ('acid', 'salt'): e['labelSide'] = 'below'
    if (e['from'], e['to']) == ('acid', 'amide'): e.update(labelSide='below', labelPos=0.42)
r0 = min(n['row'] for n in spec['nodes'])
for n in spec['nodes']: n['row'] = round(n['row'] - r0, 2)
spec.update(colw=180, rowh=95, font=16, edgefont=13, pad=16, alt=alt)
s = render(spec)
W = 16 * 2 + 180 * 6
H = int(16 + 95 * (max(n['row'] for n in spec['nodes']) + 0.5) + 46)
s = re.sub(r'viewBox="0 0 \d+ \d+" width="\d+" height="\d+"', f'viewBox="0 0 {W} {H}" width="{W}" height="{H}"', s, 1)
s = re.sub(r'<rect x="1" y="1" width="\d+" height="\d+"', f'<rect x="1" y="1" width="{W-2}" height="{H-2}"', s, 1)
# superscript plus is missing from the book's PDF fonts (ledger R02): raise a plain + instead
s = re.sub(r'>([^<]*)⁺</text>', r'>\1<tspan dy="-0.5em" font-size="70%">+</tspan></text>', s)
assert '⁺' not in s.split('<title>')[1].split('</title>')[1].replace(alt, '')
open('sections/reactions/roadmap.svg', 'w', encoding='utf-8').write(s)
print(W, H, round(W / H, 2))
