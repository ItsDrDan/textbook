"""Phone versions of wide multi-panel figures: the same drawing with the panels stacked top to bottom.
The wide file is untouched; the page shows the stacked file only on narrow screens.
Usage: python3 tools/phone_figs.py   (writes figures/phone/*.svg)"""
import re, os
os.makedirs('figures/phone', exist_ok=True)

def elongation():
    src = 'figures/pages/batchT/fig-p597179-elongation.svg'
    t = open(src, encoding='utf-8').read()
    head = re.match(r'<svg[^>]*>', t).group(0)
    label = re.search(r'aria-label="([^"]*)"', head).group(1)
    body = t[len(head):t.rindex('</svg>')]
    bg = re.match(r'<rect[^>]*/>', body).group(0); body = body[len(bg):]
    cuts = ['A new tRNA enters the A site</text>', 'chain moves onto the A-site amino acid</text>', 'ribosome moves one codon; A site is open</text>']
    panels = []
    for c in cuts:
        i = body.index(c) + len(c); panels.append(body[:i]); body = body[i:]
    foot = re.search(r'<text[^>]*>P site \(peptidyl\)[^<]*</text>', body).group(0)
    fattr = re.match(r'<text([^>]*)>', foot).group(1)
    fattr = re.sub(r'\s(x|y)="[^"]*"', '', fattr)
    W, PH, X0 = 340, 305, 20
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {3 * PH + 92}" width="{W}" height="{3 * PH + 92}" style="max-width:100%;height:auto" role="img" aria-label="{label}">', bg]
    for k, p in enumerate(panels):
        p = p.replace('y="28.0"', 'y="70.0"').replace('y="48.0"', 'y="90.0"')   # titles sit just above the drawing
        out.append(f'<g transform="translate({X0 - 380 * k},{PH * k - 45})">{p}</g>')
        if k: out.append(f'<line x1="20" y1="{PH * k - 3}" x2="{W - 20}" y2="{PH * k - 3}" stroke="#d5d9e2" stroke-width="1.5"/>')
    lines = ['P site (peptidyl): holds the tRNA with the', 'growing chain', 'A site (aminoacyl): where the next tRNA,', 'carrying one amino acid, binds']
    y = 3 * PH + 20
    for i, s in enumerate(lines):
        out.append(f'<text x="{W / 2}" y="{y}"{fattr}>{s}</text>'); y += 18 if i != 1 else 24
    out.append('</svg>')
    open('figures/phone/fig-p597179-elongation-phone.svg', 'w', encoding='utf-8').write(''.join(out))
    print('elongation', foot[:140])

elongation()
