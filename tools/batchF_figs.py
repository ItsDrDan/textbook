"""Batch F figures (review 2026-11-12), house style (ink #2d3f4b, Nunito/Inter, white background).
Each figure is landscape (width >= 2.5 x height) so it prints at full text width (PDF caps images at 3 in high).
Output: figures/pages/batchF/*.svg
"""
import math, os

OUT = 'figures/pages/batchF/'
os.makedirs(OUT, exist_ok=True)
INK = '#2d3f4b'; MUTED = '#5a6478'; RED = '#c0392b'; BLUE = '#2f5fc4'; GREEN = '#23704f'; PURPLE = '#5b4790'
FONT = 'Nunito,Inter,Helvetica,Arial,sans-serif'


def T(x, y, s, size=15, weight=700, col=INK, anchor='start', extra=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{col}" text-anchor="{anchor}" {extra}>{s}</text>'


def svg(w, h, alt, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="max-width:100%;height:auto" '
            f'role="img" aria-label="{alt}"><rect width="100%" height="100%" fill="#ffffff"/>{body}</svg>')


# ---------- 11.4 rate vs [S]
def rate_plot():
    W, H = 820, 320
    x0, y0, x1, y1 = 80, 270, 520, 40   # plot box (y0 bottom)
    Smax = 10.0
    sx = lambda s: x0 + (x1 - x0) * s / Smax
    sy = lambda v: y0 - (y0 - y1) * v / 1.1
    def curve(vmax, km, col, dash=''):
        pts = [(sx(s), sy(vmax * s / (km + s))) for s in [i * Smax / 200 for i in range(201)]]
        d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
        return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="3.2" {dash}/>'
    b = []
    b.append(f'<line x1="{x0}" y1="{y0}" x2="{x1+10}" y2="{y0}" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1-12}" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<path d="M{x1+10} {y0-5} L{x1+20} {y0} L{x1+10} {y0+5} Z" fill="{INK}"/>')
    b.append(f'<path d="M{x0-5} {y1-12} L{x0} {y1-22} L{x0+5} {y1-12} Z" fill="{INK}"/>')
    b.append(T((x0 + x1) / 2, y0 + 34, 'Substrate concentration, [S]', 15, 700, INK, 'middle'))
    b.append(T(28, (y0 + y1) / 2, 'Reaction rate', 15, 700, INK, 'middle', f'transform="rotate(-90 28 {(y0+y1)/2})"'))
    # maximum-rate guide lines
    b.append(f'<line x1="{x0}" y1="{sy(1):.1f}" x2="{x1}" y2="{sy(1):.1f}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="6 5"/>')
    b.append(f'<line x1="{x0}" y1="{sy(0.5):.1f}" x2="{x1}" y2="{sy(0.5):.1f}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="6 5"/>')
    b.append(T(x1, sy(1) - 7, 'maximum rate', 12.5, 700, MUTED, 'end'))
    b.append(T(x1, sy(0.5) - 7, 'lowered maximum rate', 12.5, 700, MUTED, 'end'))
    b.append(curve(1.0, 0.8, BLUE))
    b.append(curve(1.0, 3.2, GREEN, 'stroke-dasharray="10 6"'))
    b.append(curve(0.5, 0.8, RED))
    # legend / labels at right
    lx = 560
    items = [(BLUE, '', 'No inhibitor', ''),
             (GREEN, 'stroke-dasharray="10 6"', 'Competitive inhibitor', 'Same maximum rate, but it takes more substrate to reach it'),
             (RED, '', 'Noncompetitive inhibitor', 'Maximum rate is lowered; more substrate does not help')]
    y = 82
    for col, dash, name, note in items:
        b.append(f'<line x1="{lx}" y1="{y-5}" x2="{lx+34}" y2="{y-5}" stroke="{col}" stroke-width="3.2" {dash}/>')
        b.append(T(lx + 44, y, name, 15, 800, col))
        if note:
            words = note.split(); line = ''; yy = y + 20
            for wd in words:
                if len(line + ' ' + wd) > 36:
                    b.append(T(lx + 44, yy, line.strip(), 12.5, 600, MUTED)); yy += 16; line = ''
                line += ' ' + wd
            b.append(T(lx + 44, yy, line.strip(), 12.5, 600, MUTED)); y = yy + 36
        else:
            y += 40
    alt = ('Graph of reaction rate against substrate concentration for three cases. With no inhibitor the rate rises and levels off at the maximum rate. '
           'With a competitive inhibitor the curve rises more slowly but reaches the same maximum rate at high substrate concentration. '
           'With a noncompetitive inhibitor the curve levels off at a lower maximum rate that more substrate cannot raise.')
    open(OUT + 'fig-p597169-rate-inhibitors.svg', 'w').write(svg(W, H, alt, ''.join(b)))


rate_plot()
print('ok')


# ---------- 12.3 replication fork
def fork():
    W, H = 920, 340
    b = []
    PAR = INK; NEW = BLUE; PRIM = RED
    def seg(x1, y1, x2, y2, col, w=5, extra=''):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" {extra}/>'
    def arrowhead(x, y, d, col):  # d = +1 right, -1 left
        return f'<path d="M{x} {y-7} L{x+11*d} {y} L{x} {y+7} Z" fill="{col}"/>'
    # parental duplex (left)
    b.append(seg(60, 150, 330, 150, PAR)); b.append(seg(60, 192, 330, 192, PAR))
    for x in range(75, 325, 16): b.append(seg(x, 155, x, 187, '#b9c2cc', 3))
    b.append(T(40, 156, '3&#8242;', 15, 800, PAR, 'middle')); b.append(T(40, 198, '5&#8242;', 15, 800, PAR, 'middle'))
    b.append(T(195, 228, 'parent DNA', 14, 700, MUTED, 'middle'))
    # template arms
    b.append(f'<path d="M330 150 L410 108 L860 108" fill="none" stroke="{PAR}" stroke-width="5" stroke-linejoin="round"/>')
    b.append(f'<path d="M330 192 L410 234 L860 234" fill="none" stroke="{PAR}" stroke-width="5" stroke-linejoin="round"/>')
    b.append(T(884, 114, '5&#8242;', 15, 800, PAR, 'middle')); b.append(T(884, 240, '3&#8242;', 15, 800, PAR, 'middle'))
    # helicase at the fork
    b.append(f'<ellipse cx="338" cy="171" rx="26" ry="30" fill="#e9e3f5" stroke="{PURPLE}" stroke-width="2.5"/>')
    b.append(T(338, 176, 'H', 16, 900, PURPLE, 'middle'))
    b.append(T(338, 52, 'helicase unwinds', 14, 800, PURPLE, 'middle')); b.append(T(338, 69, 'the double helix', 14, 800, PURPLE, 'middle'))
    b.append(f'<line x1="338" y1="76" x2="338" y2="136" stroke="{PURPLE}" stroke-width="1.6"/>')
    b.append(f'<line x1="300" y1="300" x2="200" y2="300" stroke="{MUTED}" stroke-width="2.2"/>' + f'<path d="M200 294 L188 300 L200 306 Z" fill="{MUTED}"/>')
    b.append(T(310, 305, 'fork moves this way', 13.5, 700, MUTED))
    # leading strand (bottom), built toward the fork: 5' at right, 3' at left
    b.append(seg(470, 254, 840, 254, NEW)); b.append(seg(840, 254, 860, 254, PRIM))
    b.append(arrowhead(462, 254, -1, NEW))
    b.append(f'<ellipse cx="452" cy="254" rx="22" ry="17" fill="#e3f1ea" stroke="{GREEN}" stroke-width="2.5"/>' + T(452, 259, 'P', 15, 900, GREEN, 'middle'))
    b.append(T(870, 260, '5&#8242;', 13, 800, NEW, 'start')); b.append(T(425, 274, '3&#8242;', 13, 800, NEW, 'middle'))
    b.append(T(650, 290, 'Leading strand: made continuously, toward the fork', 14.5, 800, NEW, 'middle'))
    # lagging strand (top): Okazaki fragments, each made 5'->3' away from the fork
    y = 88
    frags = [(452, 470, 552), (630, 648, 722), (752, 770, 856)]
    for i, (p0, p1, e) in enumerate(frags):
        b.append(seg(p0, y, p1, y, PRIM)); b.append(seg(p1, y, e, y, NEW))
        if i == 0: b.append(T(p0 - 4, y - 12, '5&#8242;', 12, 800, NEW, 'middle'))
        if i == 2: b.append(T(e + 2, y - 12, '3&#8242;', 12, 800, NEW, 'middle'))
    b.append(arrowhead(556, y, 1, NEW))
    b.append(f'<ellipse cx="590" cy="{y}" rx="20" ry="16" fill="#e3f1ea" stroke="{GREEN}" stroke-width="2.5"/>' + T(590, y + 5, 'P', 15, 900, GREEN, 'middle'))
    b.append(f'<ellipse cx="428" cy="{y-4}" rx="19" ry="15" fill="#fdeedd" stroke="#b5651d" stroke-width="2.5"/>' + T(428, y + 1, 'Pr', 13, 900, '#b5651d', 'middle'))
    b.append(f'<ellipse cx="737" cy="{y}" rx="16" ry="14" fill="#fff6cc" stroke="#9a7b00" stroke-width="2.5"/>' + T(737, y + 5, 'L', 14, 900, '#9a7b00', 'middle'))
    b.append(T(650, 30, 'Lagging strand: made in short Okazaki fragments, away from the fork', 14.5, 800, NEW, 'middle'))
    # key
    kx, ky = 40, 268
    keys = [('#e9e3f5', PURPLE, 'H', 'helicase'), ('#fdeedd', '#b5651d', 'Pr', 'primase: lays down a short RNA primer'),
            ('#e3f1ea', GREEN, 'P', 'DNA polymerase: adds nucleotides 5&#8242;&#8594;3&#8242;'), ('#fff6cc', '#9a7b00', 'L', 'ligase: joins the fragments')]
    b.append(f'<rect x="{kx-14}" y="{ky-10}" width="0" height="0" fill="none"/>')
    # place key in the lower-left under the duplex
    ky = 318; kx = 40
    for i, (fill, col, ab, txt) in enumerate(keys[1:], 0):
        pass
    legend = (f'<g font-family="{FONT}">' +
              T(40, 252, 'RNA primer', 13, 800, PRIM) + seg(150, 248, 174, 248, PRIM, 5) +
              T(40, 272, 'new DNA', 13, 800, NEW) + seg(150, 268, 174, 268, NEW, 5) +
              T(40, 292, 'template DNA', 13, 800, PAR) + seg(150, 288, 174, 288, PAR, 5) + '</g>')
    b.append(legend)
    b.append(T(40, 330, 'Pr = primase (makes the RNA primer)  ·  P = DNA polymerase (adds nucleotides 5&#8242;&#8594;3&#8242;)  ·  L = ligase (joins fragments)', 13, 700, MUTED))
    alt = ('Diagram of a DNA replication fork. On the left the parent double helix is unwound at the fork by helicase, and the fork moves to the left. '
           'The two separated template strands run in opposite directions. On the lower template the leading strand is made continuously toward the fork by DNA polymerase, '
           'starting from one RNA primer. On the upper template the lagging strand is made in short Okazaki fragments, each started by primase with an RNA primer and '
           'extended by DNA polymerase away from the fork; ligase joins the fragments. New strands are built 5 prime to 3 prime.')
    open(OUT + 'fig-p597177-replication-fork.svg', 'w').write(svg(W, H, alt, ''.join(b)))


fork()
print('fork ok')


# ---------- 8.4 Fischer -> Haworth in three steps (D-glucose)
def haworth_steps():
    W, H = 1180, 420
    b = []
    def L(x1, y1, x2, y2, w=2.4, col=INK):
        return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
    def lab(x, y, s, anchor='middle', col=INK, size=15, weight=800):
        s = s.replace('OH', 'O<tspan>H</tspan>')
        s = s.replace('CH2', 'CH<tspan font-size="11" dy="4">2</tspan><tspan dy="-4"></tspan>')
        if s.startswith('O<tspan>H') or 'O<tspan>H' in s:
            s = s.replace('O<tspan>H</tspan>', '<tspan fill="#c0392b">O</tspan>H')
        return T(x, y + 5, s, size, weight, col, anchor)
    def arrow(x1, x2, y, word):
        return (L(x1, y, x2 - 10, y, 2.6) + f'<path d="M{x2-12} {y-7} L{x2} {y} L{x2-12} {y+7} Z" fill="{INK}"/>' +
                T((x1 + x2) / 2, y - 14, word, 15, 900, PURPLE, 'middle'))
    # Panel 1: Fischer projection (vertical)
    cx, top = 105, 120; dy = 42
    b.append(lab(cx, top - 26, 'CHO'))
    groups = [('H', 'OH'), ('HO', 'H'), ('H', 'OH'), ('H', 'OH')]  # (left,right) for C2..C5
    b.append(L(cx, top - 14, cx, top + dy * 4 + 2))
    for i, (lf, rt) in enumerate(groups):
        y = top + dy * (i + 0.5)
        b.append(L(cx - 34, y, cx + 34, y))
        b.append(lab(cx - 42, y, lf, 'end')); b.append(lab(cx + 42, y, rt, 'start'))
    b.append(lab(cx, top + dy * 4 + 22, 'CH2OH'))
    b.append(T(cx, 380, 'D-glucose (Fischer)', 14, 700, MUTED, 'middle'))
    b.append(T(cx, 400, 'left = up, right = down', 13, 700, MUTED, 'middle'))
    b.append(arrow(180, 235, 200, '1 Rotate'))
    # Panel 2: rotated, chain horizontal with C1 (CHO) at right, C6 at left
    y0 = 200; xs = [500, 450, 400, 350]  # C2, C3, C4, C5 x positions
    b.append(L(318, y0, 522, y0))
    b.append(lab(312, y0, 'HOCH2', 'end'))
    b.append(lab(530, y0, 'CHO', 'start'))
    rot = {500: ('H', 'OH'), 450: ('OH', 'H'), 400: ('H', 'OH'), 350: ('H', 'OH')}  # (up, down)
    for x in xs:
        up, dn = rot[x]
        b.append(L(x, y0 - 30, x, y0 + 30)); b.append(lab(x, y0 - 44, up)); b.append(lab(x, y0 + 44, dn))
    for x, n in zip(xs, ['2', '3', '4', '5']):
        b.append(T(x + 6, y0 - 6, n, 11, 800, MUTED))
    b.append(T(430, 380, 'on its side: C=O at the right', 14, 700, MUTED, 'middle'))
    b.append(arrow(585, 640, 200, '2 Twist'))
    # ring geometry helper
    def ring(ox, oy, closed, anomer=None):
        P = {'C4': (ox - 70, oy), 'C5': (ox - 10, oy - 25), 'O': (ox + 62, oy - 25), 'C1': (ox + 122, oy), 'C3': (ox - 32, oy + 25), 'C2': (ox + 84, oy + 25)}
        out = []
        out.append(L(*P['C5'], *P['C4'])); out.append(L(*P['C4'], *P['C3']))
        out.append(L(*P['C3'], *P['C2'], 6)); out.append(L(*P['C2'], *P['C1']))
        if closed:
            out.append(L(*P['C5'], P['O'][0] - 10, P['O'][1])); out.append(L(P['O'][0] + 9, P['O'][1] + 4, *P['C1']))
            out.append(T(P['O'][0], P['O'][1] + 5, 'O', 15, 900, RED, 'middle'))
        def back(c, up, dn, h=22):
            x, y = P[c]
            out.append(L(x, y - h, x, y + h, 2.2)); out.append(lab(x, y - h - 11, up, size=14)); out.append(lab(x, y + h + 11, dn, size=14))
        def front(c, up, dn):
            x, y = P[c]
            out.append(L(x, y - 16, x, y + 22, 2.2)); out.append(lab(x, y - 26, up, size=14)); out.append(lab(x, y + 33, dn, size=14))
        front('C2', 'H', 'OH'); front('C3', 'OH', 'H'); back('C4', 'H', 'OH')
        x, y = P['C5']
        out.append(L(x, y, x, y - 24, 2.2)); out.append(lab(x, y - 36, 'CH2OH', size=14))
        if closed:
            back('C1', 'H', 'OH') if anomer == 'alpha' else back('C1', 'OH', 'H')
        else:
            out.append(L(x, y, x + 30, y, 2.2)); out.append(lab(x + 34, y, 'OH', 'start', size=14))
            cx1, cy1 = P['C1']
            out.append(L(cx1, cy1, cx1 - 8, cy1 - 26, 2.2)); out.append(L(cx1 + 4, cy1 - 2, cx1 - 4, cy1 - 28, 2.2))
            out.append(T(cx1 - 6, cy1 - 33, 'O', 15, 900, RED, 'middle'))
            out.append(L(cx1, cy1, cx1 + 6, cy1 + 24, 2.2)); out.append(lab(cx1 + 8, cy1 + 36, 'H', size=14))
        return out
    b += ring(745, 200, False)
    b.append(T(760, 380, 'CH2OH up for a D sugar;', 14, 700, MUTED, 'middle').replace('CH2OH', 'CH<tspan font-size="11" dy="4">2</tspan><tspan dy="-4">OH</tspan>'))
    b.append(T(760, 400, 'C5 OH reaches the C=O', 14, 700, MUTED, 'middle'))
    b.append(arrow(880, 925, 200, '3 Close'))
    b += ring(1010, 110, True, 'alpha')
    b.append(T(1158, 115, '&#945;', 20, 900, PURPLE, 'start'))
    b += ring(1010, 300, True, 'beta')
    b.append(T(1158, 305, '&#946;', 20, 900, PURPLE, 'start'))
    b.append(T(1050, 410, 'anomeric OH down = &#945;, up = &#946;', 14, 700, MUTED, 'middle'))
    alt = ('Converting D-glucose from a Fischer projection to Haworth rings in three steps. Step 1, rotate: the Fischer projection is turned on its side with the '
           'aldehyde at the right, so groups that were on the left point up and groups on the right point down. Step 2, twist: the chain is curled into a ring '
           'shape with the CH2OH group pointing up, as it does for a D sugar, and the C5 OH reaching toward the C=O. Step 3, close: the C5 oxygen bonds to C1, '
           'giving two anomers: alpha with the new OH on C1 pointing down and beta with it pointing up. In both rings the OH groups on C2 and C4 point down and the OH on C3 points up.')
    open(OUT + 'fig-p597137-fischer-to-haworth.svg', 'w').write(svg(W, H, alt, ''.join(b)))


haworth_steps()
print('haworth ok')


# ---------- 12.6 one elongation cycle with P and A sites
def elongation():
    W, H = 1140, 380
    b = []
    COD = ['AUG', 'GGU', 'GAA', 'AAG']
    ANTI = {'GGU': 'CCA', 'GAA': 'CUU'}
    AA = {'GGU': 'Gly', 'GAA': 'Glu'}
    AACOL = {'Met': '#7a8a99', 'Gly': '#2f5fc4', 'Glu': '#c0392b'}
    def panel(px, title, p_idx, p_chain, a_codon, a_chain, leaving=None, shift_note=None):
        cw = 46  # codon width
        mx = px + 10; my = 300
        out = []
        # mRNA
        out.append(f'<line x1="{mx}" y1="{my}" x2="{mx + cw*4 + 40}" y2="{my}" stroke="{INK}" stroke-width="3"/>')
        out.append(T(mx - 4, my + 22, '5&#8242;', 12, 800, MUTED, 'end')); out.append(T(mx + cw*4 + 44, my + 22, '3&#8242;', 12, 800, MUTED, 'start'))
        # ribosome around codons p_idx and p_idx+1
        rx = mx + 20 + cw*p_idx - 8; rw = cw*2 + 16
        out.append(f'<rect x="{rx-10}" y="{my-14}" width="{rw+20}" height="46" rx="20" fill="#e9e3f5" fill-opacity="0.35" stroke="{PURPLE}" stroke-width="2"/>')
        out.append(f'<rect x="{rx-34}" y="{my-150}" width="{rw+68}" height="124" rx="40" fill="#e9e3f5" fill-opacity="0.55" stroke="{PURPLE}" stroke-width="2"/>')
        for i, c in enumerate(COD):
            out.append(T(mx + 20 + cw*i + cw/2, my + 22, c, 14, 800, INK, 'middle'))
        pcx0 = mx + 20 + cw*p_idx + cw/2
        out.append(T(pcx0 - 30, my - 52, 'P', 18, 900, PURPLE, 'middle'))
        out.append(T(pcx0 + cw + 30, my - 52, 'A', 18, 900, PURPLE, 'middle'))
        def trna(cx, anti, chain):
            o = []
            o.append(f'<rect x="{cx-16}" y="{my-92}" width="32" height="70" rx="8" fill="#ffffff" stroke="{GREEN}" stroke-width="2.4"/>')
            o.append(T(cx, my - 30, anti, 11.5, 800, GREEN, 'middle'))
            o.append(f'<line x1="{cx}" y1="{my-92}" x2="{cx}" y2="{my-104}" stroke="{GREEN}" stroke-width="2.4"/>')
            for k, aa in enumerate(chain[::-1]):
                cy = my - 116 - 24*k
                o.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{AACOL[aa]}"/>' + T(cx, cy + 4, aa, 9.5, 900, '#ffffff', 'middle'))
            return o
        pcx = mx + 20 + cw*p_idx + cw/2; acx = pcx + cw
        out += trna(pcx, ANTI[COD[p_idx]], p_chain)
        if a_codon:
            out += trna(acx, ANTI[a_codon], a_chain)
        if leaving:
            lx = pcx - cw - 18
            out.append(f'<g opacity="0.55">' + ''.join(trna(lx, 'CCA', [])) + '</g>')
            out.append(f'<path d="M{lx+2} {my-100} q-10 -40 -30 -60" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="4 4"/>')
            out.append(T(lx - 30, my - 168, 'empty tRNA leaves', 12.5, 700, MUTED, 'middle'))
        out.append(T(px + 130, 28, title, 15.5, 900, INK, 'middle'))
        if shift_note: out.append(T(px + 130, 48, shift_note, 13, 700, MUTED, 'middle'))
        return out
    b += panel(20, '1  A new tRNA enters the A site', 1, ['Met', 'Gly'], 'GAA', ['Glu'])
    b += panel(400, '2  Peptide bond forms', 1, [], 'GAA', ['Met', 'Gly', 'Glu'], shift_note='chain moves onto the A-site amino acid')
    b += panel(780, '3  Translocation', 2, ['Met', 'Gly', 'Glu'], None, None, leaving=True, shift_note='ribosome moves one codon; A site is open')
    for x in (378, 758):
        b.append(f'<line x1="{x}" y1="70" x2="{x}" y2="350" stroke="#d5dbe3" stroke-width="1.5"/>')
    b.append(T(570, 372, 'P site (peptidyl): holds the tRNA with the growing chain   ·   A site (aminoacyl): where the next tRNA, carrying one amino acid, binds', 13, 700, MUTED, 'middle'))
    alt = ('One elongation cycle of translation on the mRNA 5 prime AUG GGU GAA AAG 3 prime. Panel 1: the ribosome covers codons GGU and GAA. The P site holds the tRNA '
           'with anticodon CCA carrying the growing chain Met-Gly; a tRNA with anticodon CUU carrying Glu enters the A site at codon GAA. Panel 2: a peptide bond forms '
           'and the chain Met-Gly is moved onto Glu, so the A-site tRNA now carries Met-Gly-Glu and the P-site tRNA is empty. Panel 3: translocation; the ribosome moves '
           'one codon toward the 3 prime end, the empty tRNA leaves, the tRNA carrying Met-Gly-Glu is now in the P site, and the A site is open at codon AAG for the next tRNA.')
    open(OUT + 'fig-p597179-elongation.svg', 'w').write(svg(W, H, alt, ''.join(b)))


elongation()
print('elong ok')
