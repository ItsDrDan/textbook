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


# ---------------------------------------------------------------------------------------------------------------
# Generic stacker: the phone file shows chosen rectangles of the wide figure one under another.
# Items:  ('crop', x, y, w, h[, scale])  a rectangle of the wide drawing (scale 1 = same label size as the wide file)
#         ('text', [lines], size, weight, fill)  a caption re-wrapped for the narrow width
#         ('raw', svg, height)  hand-written SVG, placed with its origin at the left edge of the row
#         ('rule',)  a thin divider
FONT = 'Nunito,Inter,Helvetica,Arial,sans-serif'

def stack(src, out, items, W=360, gap=10):
    t = open(src, encoding='utf-8').read()
    head = re.match(r'(?:<\?xml[^>]*>\s*)?<svg[^>]*>', t).group(0)
    label = re.search(r'aria-label="([^"]*)"', head)
    inner = t[len(head):t.rindex('</svg>')]
    y = 6; parts = []
    for it in items:
        if it[0] == 'crop':
            x0, y0, w, h = it[1:5]; s = it[5] if len(it) > 5 else 1
            s = min(s, W / w)
            n = len(parts); X = (W - w * s) / 2
            parts.append(f'<clipPath id="pc{n}"><rect x="{x0}" y="{y0}" width="{w}" height="{h}"/></clipPath>'
                         f'<g transform="translate({X - x0 * s:.2f},{y - y0 * s:.2f}) scale({s:.4f})"><g clip-path="url(#pc{n})">{inner}</g></g>')
            y += h * s + gap
        elif it[0] == 'text':
            lines, size, weight, fill = it[1:5]
            for s in lines:
                y += size * 1.3
                parts.append(f'<text x="{W / 2}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="middle">{s}</text>')
            y += gap + 4
        elif it[0] == 'raw':
            parts.append(f'<g transform="translate(0,{y:.1f})">{it[1]}</g>'); y += it[2] + gap
        elif it[0] == 'rule':
            parts.append(f'<line x1="16" y1="{y:.1f}" x2="{W - 16}" y2="{y:.1f}" stroke="#d5d9e2" stroke-width="1.5"/>'); y += gap
    H = round(y)
    aria = f' role="img" aria-label="{label.group(1)}"' if label else ''
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="max-width:100%;height:auto"{aria}><rect width="100%" height="100%" fill="#ffffff"/>' + ''.join(parts) + '</svg>'
    open(out, 'w', encoding='utf-8').write(svg)
    print(os.path.basename(out), W, 'x', H)

GREY, PURPLE = '#5a6478', '#5b4790'
K, O = 'figures/pages/batchK/', 'figures/pathways/oer/'
SPECS = {
    'fig-p597056-lewis-errors': (K + 'fig-p597056-lewis-errors.svg', 500, [('crop', 0, 0, 500, 206), ('crop', 500, 0, 500, 206), ('crop', 0, 206, 500, 206), ('crop', 500, 206, 500, 206)]),
    'fig-p597111-acid-dimer': (K + 'fig-p597111-acid-dimer.svg', 440, [('crop', 80, 18, 440, 270), ('rule',), ('crop', 605, 18, 375, 270)]),
    'fig-p597140-polysaccharides': (K + 'fig-p597140-polysaccharides.svg', 360, [('crop', 0, 18, 360, 372), ('rule',), ('crop', 360, 18, 360, 392), ('rule',), ('crop', 720, 18, 360, 372)]),
    'myelin_ms': (O + 'myelin_ms.svg', 430, [('text', ['Myelin and multiple sclerosis'], 19, 900, PURPLE), ('crop', 0, 56, 430, 215), ('rule',), ('crop', 430, 56, 430, 305),
                  ('text', ['Myelin is rich in sphingomyelin and other', 'sphingolipids. In multiple sclerosis the immune', 'system damages myelin in the brain and spinal', 'cord, so nerve signals slow down or stop.'], 13.5, 700, GREY)]),
    'fig-p597148-rbc-tonicity': (K + 'fig-p597148-rbc-tonicity.svg', 340, [('crop', 0, 14, 340, 326), ('rule',), ('crop', 330, 14, 340, 326), ('rule',), ('crop', 660, 14, 340, 326),
                  ('text', ['Blue arrows show water crossing the', 'red blood cell membrane (osmosis).'], 13.5, 700, GREY)]),
    'atp_rotation': (O + 'atp_rotation.svg', 336, [('text', ['How H⁺ flow turns the Fₒ rotor', '(view from above)'], 19, 900, PURPLE), ('crop', 0, 52, 298, 280), ('rule',), ('crop', 294, 52, 304, 280), ('rule',), ('crop', 594, 52, 336, 280)]),
    'collagen': (O + 'collagen.svg', 360, [('text', ['Collagen: a triple helix of', 'three protein chains'], 19, 900, PURPLE), ('crop', 14, 86, 560, 128),
                  ('text', ['Three left-handed chains wind around each', 'other into a right-handed &#8220;rope.&#8221;'], 13.5, 700, GREY), ('crop', 592, 72, 256, 206),
                  ('text', ['Hydrogen bonds between the chains hold the', 'triple helix together. Making hydroxyproline', 'needs vitamin C; without it, collagen is weak', '(scurvy).'], 13.5, 700, GREY)]),
    'fig-p597169-rate-inhibitors': ('figures/pages/batchF/fig-p597169-rate-inhibitors.svg', 380, [('crop', 8, 14, 545, 304), ('crop', 556, 62, 264, 184)]),
}

def build_all():
    for name, (src, W, items) in SPECS.items():
        stack(src, f'figures/phone/{name}-phone.svg', items, W=W)

build_all()
