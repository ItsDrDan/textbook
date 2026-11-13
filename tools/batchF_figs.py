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
                cy = my - 118 - 28*k
                o.append(f'<circle cx="{cx}" cy="{cy}" r="14" fill="{AACOL[aa]}"/>' + T(cx, cy + 4.5, aa, 12, 900, '#ffffff', 'middle'))
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


# ---------- 9.3 labelled phosphatidylcholine (replaces an image with no known source; batch G)
def phospholipid():
    W, H = 410, 480
    b = []
    cx = 180
    # head
    heads = [(cx, 62, '#cfe0fb', BLUE, 'choline', 'N<tspan dy="-6" font-size="11">+</tspan>'),
             (cx, 112, '#fde3d6', '#d35400', 'phosphate', 'P<tspan dy="-6" font-size="11">&#8722;</tspan>'),
             (cx, 162, '#fff3c4', '#9a7b00', 'glycerol', '')]
    for x, y, fill, col, name, sym in heads:
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="46" ry="22" fill="{fill}" stroke="{col}" stroke-width="2.4"/>')
        b.append(T(x, y + 5, name, 14, 800, col, 'middle'))
        if sym: b.append(T(x + 54, y - 8, sym, 15, 900, col, 'start'))
    # ester links to two tails
    lx, rx = cx - 22, cx + 22
    b.append(f'<line x1="{cx-16}" y1="182" x2="{lx}" y2="204" stroke="{INK}" stroke-width="2.4"/>')
    b.append(f'<line x1="{cx+16}" y1="182" x2="{rx}" y2="204" stroke="{INK}" stroke-width="2.4"/>')
    def zig(x0, y0, n, kink_at=None):
        pts = [(x0, y0)]; x, y = x0, y0; dx = 7
        for i in range(n):
            y += 13; x = x0 + (dx if i % 2 == 0 else -dx)
            if kink_at is not None and i >= kink_at: x -= 30
            pts.append((x, y))
        return 'M' + ' L'.join(f'{a:.1f} {c:.1f}' for a, c in pts)
    b.append(f'<path d="{zig(rx, 204, 16)}" fill="none" stroke="#596779" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>')
    b.append(f'<path d="{zig(lx, 204, 17, kink_at=8)}" fill="none" stroke="#596779" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>')
    b.append(T(lx - 30, 452, 'oleic acid', 13, 800, INK, 'middle')); b.append(T(lx - 30, 468, 'chain', 13, 800, INK, 'middle'))
    b.append(T(rx + 14, 452, 'palmitic acid', 13, 800, INK, 'middle')); b.append(T(rx + 14, 468, 'chain', 13, 800, INK, 'middle'))
    b.append(T(lx - 50, 318, 'cis C=C bend', 12, 700, MUTED, 'end'))
    # brackets
    bx = 282
    b.append(f'<path d="M{bx} 40 h10 v144 h-10" fill="none" stroke="{RED}" stroke-width="2"/>')
    b.append(T(bx + 18, 108, 'polar head', 14, 900, RED, 'start'))
    b.append(T(bx + 18, 124, '(hydrophilic)', 12, 700, RED, 'start'))
    b.append(f'<path d="M{bx} 200 h10 v230 h-10" fill="none" stroke="{MUTED}" stroke-width="2"/>')
    b.append(T(bx + 18, 306, 'nonpolar', 14, 900, MUTED, 'start'))
    b.append(T(bx + 18, 322, 'tails', 14, 900, MUTED, 'start'))
    b.append(T(bx + 18, 338, '(hydrophobic)', 12, 700, MUTED, 'start'))
    alt = ('Labeled sketch of a phosphatidylcholine (lecithin) molecule: a polar, hydrophilic head made of choline (positive charge), phosphate (negative charge) '
           'and glycerol, and two nonpolar, hydrophobic tails: a straight palmitic acid chain and an oleic acid chain with a bend at its cis C=C double bond.')
    open(OUT + 'fig-p597146-phosphatidylcholine.svg', 'w').write(svg(W, H, alt, ''.join(b)))


phospholipid()
print('pl ok')


# ---------- 13.1 overview of metabolism (replaces a CC BY-SA image; batch H)
def metabolism():
    W, H = 920, 370
    b = []
    def arr(x1, y1, x2, y2, col=INK, w=2.4, head=9):
        import math
        a = math.atan2(y2 - y1, x2 - x1); hx, hy = x2 - head * math.cos(a), y2 - head * math.sin(a)
        px, py = -math.sin(a) * head * 0.55, math.cos(a) * head * 0.55
        return (f'<line x1="{x1}" y1="{y1}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{col}" stroke-width="{w}"/>'
                f'<path d="M{x2} {y2} L{hx+px:.1f} {hy+py:.1f} L{hx-px:.1f} {hy-py:.1f} Z" fill="{col}"/>')
    def fat(x1, x2, y, col, label):
        return (f'<path d="M{x1} {y-13} L{x2-26} {y-13} L{x2-26} {y-24} L{x2} {y} L{x2-26} {y+24} L{x2-26} {y+13} L{x1} {y+13} Z" fill="{col}"/>'
                + T((x1 + x2) / 2 - 10, y + 5, label, 16, 900, '#ffffff', 'middle'))
    b.append(f'<rect x="170" y="44" width="720" height="270" rx="70" fill="#fdf1e7" stroke="#d9a06b" stroke-width="3"/>')
    b.append(T(190, 72, 'Inside the cell', 13, 800, '#b5651d'))
    # catabolism / anabolism
    b.append(T(70, 222, 'Nutrients', 15, 800, INK, 'middle')); b.append(T(70, 240, '(carbohydrates,', 12.5, 700, MUTED, 'middle')); b.append(T(70, 255, 'fats, proteins)', 12.5, 700, MUTED, 'middle'))
    b.append(arr(120, 226, 214, 226))
    b.append(fat(220, 420, 226, '#c0392b', 'Catabolism'))
    b.append(T(470, 222, 'small', 14, 800, INK, 'middle')); b.append(T(470, 239, 'intermediates', 14, 800, INK, 'middle'))
    b.append(fat(520, 712, 226, '#2f5fc4', 'Anabolism'))
    b.append(T(840, 215, 'Biomass:', 15, 800, INK, 'middle')); b.append(T(840, 233, 'proteins, polysac-', 12, 700, MUTED, 'middle'))
    b.append(T(840, 248, 'charides, fats,', 12, 700, MUTED, 'middle')); b.append(T(840, 263, 'nucleic acids', 12, 700, MUTED, 'middle'))
    b.append(arr(716, 226, 778, 226))
    # CO2 out
    b.append(arr(320, 244, 320, 350, '#c0392b')); b.append(T(332, 352, 'CO<tspan font-size="11" dy="4">2</tspan><tspan dy="-4"> out</tspan>', 14, 800, '#c0392b', 'start'))
    # minerals in
    b.append(arr(470, 352, 470, 252, '#23704f')); b.append(T(482, 340, 'minerals, nitrogen sources, vitamins in', 13, 700, '#23704f', 'start'))
    # NAD cycle + O2/H2O
    b.append(T(250, 128, 'NAD<tspan dy="-6" font-size="11">+</tspan>', 15, 800, BLUE, 'middle'))
    b.append(T(372, 128, 'NADH', 15, 800, BLUE, 'middle'))
    b.append(f'<path d="M272 140 Q311 186 350 140" fill="none" stroke="{BLUE}" stroke-width="2.2"/>' + f'<path d="M350 140 l-9 1 l5 -8 Z" fill="{BLUE}"/>')
    b.append(f'<path d="M350 114 Q311 72 272 114" fill="none" stroke="{BLUE}" stroke-width="2.2"/>' + f'<path d="M272 114 l9 -1 l-5 8 Z" fill="{BLUE}"/>')
    b.append(T(311, 162, 'catabolism', 11.5, 700, MUTED, 'middle'))
    b.append(arr(262, 10, 296, 84, MUTED)); b.append(T(256, 22, 'O<tspan font-size="11" dy="4">2</tspan>', 14, 800, INK, 'end'))
    b.append(arr(326, 84, 360, 10, MUTED)); b.append(T(370, 22, 'H<tspan font-size="11" dy="4">2</tspan><tspan dy="-4">O</tspan>', 14, 800, INK, 'start'))
    b.append(T(311, 106, 'to O<tspan font-size="9" dy="3">2</tspan>', 11, 700, MUTED, 'middle'))
    # ATP cycle
    b.append(T(530, 128, 'ADP', 15, 800, '#9a7b00', 'middle')); b.append(T(650, 128, 'ATP', 15, 800, '#9a7b00', 'middle'))
    b.append(f'<path d="M552 140 Q590 186 628 140" fill="none" stroke="#9a7b00" stroke-width="2.2"/>' + f'<path d="M628 140 l-9 1 l5 -8 Z" fill="#9a7b00"/>')
    b.append(f'<path d="M628 114 Q590 72 552 114" fill="none" stroke="#9a7b00" stroke-width="2.2"/>' + f'<path d="M552 114 l9 -1 l-5 8 Z" fill="#9a7b00"/>')
    b.append(T(590, 170, 'made by catabolism', 11.5, 700, MUTED, 'middle')); b.append(T(590, 86, 'spent by anabolism', 11.5, 700, MUTED, 'middle'))
    alt = ('Overview of metabolism inside a cell. Nutrients (carbohydrates, fats and proteins) enter and are broken down by catabolism into small intermediates, '
           'releasing CO2; catabolism also reduces NAD plus to NADH, whose electrons go to O2 to make H2O, and it makes ATP from ADP. Anabolism uses the intermediates '
           'and the energy of ATP, together with minerals, nitrogen sources and vitamins, to build biomass: proteins, polysaccharides, fats and nucleic acids.')
    open(OUT + 'fig-p597188-metabolism.svg', 'w').write(svg(W, H, alt, ''.join(b)))


metabolism()
print('met ok')


# ---------- 9.3.1 condensed formula of POPC (batch I): chains written CH3(CH2)n-C(=O)-O-
def popc_condensed():
    W, H = 720, 250
    b = []
    import re
    def sub(t):
        return re.sub(r'([A-Za-z\)])(\d+)', lambda m: m.group(1) + f'<tspan font-size="12" baseline-shift="sub">{m.group(2)}</tspan>', t)
    def tx(x, y, t, anchor='start', col=INK, size=17, w=700):
        return T(x, y, sub(t), size, w, col, anchor)
    def L(x1, y1, x2, y2, col=INK, sw=2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}"/>'
    def ester(y, chain, cx):
        o = [tx(cx - 14, y, chain, 'end'), L(cx - 10, y - 6, cx + 2, y - 6), tx(cx + 6, y, 'C'),
             L(cx + 12, y - 18, cx + 12, y - 32), L(cx + 18, y - 18, cx + 18, y - 32), T(cx + 15, y - 36, 'O', 17, 700, RED, 'middle'),
             L(cx + 24, y - 6, cx + 38, y - 6), T(cx + 42, y, 'O', 17, 700, RED), L(cx + 56, y - 6, cx + 70, y - 6)]
        return o
    cx = 300
    b += ester(56, 'CH3(CH2)14', cx)
    b += ester(126, 'CH3(CH2)7CH=CH(CH2)7', cx)
    gx = cx + 74
    b += [tx(gx, 56, 'CH2'), tx(gx, 126, 'CH'), tx(gx, 196, 'CH2')]
    b += [L(gx + 12, 62, gx + 12, 108), L(gx + 12, 132, gx + 12, 178)]
    x = gx + 40
    b += [L(x, 190, x + 14, 190), T(x + 18, 196, 'O', 17, 700, RED), L(x + 32, 190, x + 46, 190), T(x + 50, 196, 'P', 17, 800, '#d35400'),
          L(x + 53, 178, x + 53, 162), L(x + 59, 178, x + 59, 162), T(x + 56, 158, 'O', 17, 700, RED, 'middle'),
          L(x + 56, 200, x + 56, 214), T(x + 56, 234, 'O<tspan font-size="12" baseline-shift="super">&#8722;</tspan>', 17, 700, RED, 'middle'),
          L(x + 64, 190, x + 78, 190), T(x + 82, 196, 'O', 17, 700, RED), L(x + 96, 190, x + 110, 190),
          tx(x + 114, 196, '(CH2)2'), L(x + 172, 190, x + 186, 190),
          T(x + 190, 196, 'N<tspan font-size="12" baseline-shift="super">+</tspan>(CH<tspan font-size="12" baseline-shift="sub">3</tspan>)<tspan font-size="12" baseline-shift="sub">3</tspan>', 17, 700, BLUE)]
    alt = ('Condensed formula of 1-palmitoyl-2-oleoyl-phosphatidylcholine: glycerol carbons CH2, CH and CH2 in a column; the top CH2 is bonded through O to '
           'C(=O) of the palmitoyl chain CH3(CH2)14; the CH is bonded through O to C(=O) of the oleoyl chain CH3(CH2)7CH=CH(CH2)7; the bottom CH2 is bonded through O to a '
           'phosphate (P=O, O minus) that links through O to (CH2)2N+(CH3)3, the choline group.')
    open(OUT + 'fig-p597146-popc-condensed.svg', 'w').write(svg(W, H, alt, ''.join(b)))


popc_condensed()
print('popc ok')


# ---------- shared flow-chart helpers (batch J landscape redraws)
def _fc_box(x0, x1, yc, lines, fill='#ffffff', stroke='#8fa6b8', col=INK, size=15, h=None):
    h = h or (22 + 19 * len(lines))
    o = [f'<rect x="{x0}" y="{yc-h/2:.1f}" width="{x1-x0}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>']
    y = yc - 19 * (len(lines) - 1) / 2 + 5
    for ln in lines:
        o.append(T((x0 + x1) / 2, y, ln, size, 800, col, 'middle')); y += 19
    return ''.join(o)


def _fc_arrow(x1, y1, x2, y2, col=INK, w=2.6, head=11):
    import math
    a = math.atan2(y2 - y1, x2 - x1); hx, hy = x2 - head * math.cos(a), y2 - head * math.sin(a)
    px, py = -math.sin(a) * head * 0.55, math.cos(a) * head * 0.55
    return (f'<line x1="{x1}" y1="{y1}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{col}" stroke-width="{w}"/>'
            f'<path d="M{x2} {y2} L{hx+px:.1f} {hy+py:.1f} L{hx-px:.1f} {hy-py:.1f} Z" fill="{col}"/>')


def _fc_pill(xc, yc, text, w=None, fill='#fff3c4', stroke='#d4a72c', col='#7a5d00', size=13):
    w = w or (len(re.sub(r'<[^>]+>', '', text)) * 7.4 + 22)
    return (f'<rect x="{xc-w/2:.1f}" y="{yc-13}" width="{w:.1f}" height="26" rx="13" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
            + T(xc, yc + 5, text, size, 800, col, 'middle'))


import re


def _sub(s):
    return re.sub(r'([A-Za-z\)])(\d)(?![\d,])', r'\1<tspan font-size="11" baseline-shift="sub">\2</tspan>', s)


def glycolysis_flow():
    W, H = 1220, 470
    b = []
    EN = MUTED
    def en(x, y, s, anchor='middle'): return T(x, y, s, 12.5, 700, EN, anchor, 'font-style="italic"')
    b.append(T(20, 30, 'Phase 1: energy investment (steps 1&#8211;5, once per glucose)', 15, 900, PURPLE))
    yc = 116
    boxes1 = [(20, 130, ['Glucose']), (225, 395, ['Glucose', '6-phosphate']), (490, 660, ['Fructose', '6-phosphate']), (755, 905, ['Fructose 1,6-', 'bisphosphate']), (1040, 1200, ['Glyceraldehyde', '3-phosphate (&#215;2)'])]
    for x0, x1, ln in boxes1: b.append(_fc_box(x0, x1, yc, ln, h=60))
    labs1 = [('1 hexokinase', ''), ('2 phosphoglucose', 'isomerase'), ('3 phospho-', 'fructokinase-1'), ('4 aldolase', '')]
    pills1 = ['ATP &#8594; ADP', None, 'ATP &#8594; ADP', None]
    for i in range(4):
        xa, xb = boxes1[i][1] + 6, boxes1[i + 1][0] - 6
        b.append(_fc_arrow(xa, yc, xb, yc))
        l1, l2 = labs1[i]
        b.append(en((xa + xb) / 2, yc - (24 if l2 else 12), l1))
        if l2: b.append(en((xa + xb) / 2, yc - 10, l2))
        if pills1[i]: b.append(_fc_pill((xa + xb) / 2, yc + 30, pills1[i], w=118))
    # DHAP above the aldolase arrow, with TPI to GAP
    b.append(_fc_box(915, 1015, 40, ['DHAP'], h=34))
    b.append(_fc_arrow(885, 84, 925, 58))
    b.append(_fc_arrow(1018, 44, 1070, 84)); b.append(_fc_arrow(1082, 80, 1030, 40))
    b.append(en(1040, 22, '5 triose phosphate isomerase', 'start'))
    # Phase 2 snake (right to left)
    b.append(T(1100, 222, 'Phase 2: energy payoff (steps 6&#8211;10, twice per glucose)', 15, 900, GREEN, 'end'))
    y2 = 360
    b.append(_fc_arrow(1120, 148, 1120, y2 - 32))
    b.append(en(1110, 250, '6 glyceraldehyde-3-phosphate', 'end')); b.append(en(1110, 264, 'dehydrogenase', 'end'))
    b.append(_fc_pill(1010, 294, 'NAD<tspan baseline-shift="super" font-size="10">+</tspan> &#8594; NADH, + P<tspan baseline-shift="sub" font-size="10">i</tspan> (&#215;2)', w=196, fill='#e3ecfb', stroke='#7d9bd6', col=BLUE))
    boxes2 = [(1040, 1200, ['1,3-Bisphospho-', 'glycerate']), (820, 980, ['3-Phospho-', 'glycerate']), (600, 760, ['2-Phospho-', 'glycerate']), (380, 540, ['Phosphoenol-', 'pyruvate (PEP)']), (160, 320, ['Pyruvate (&#215;2)'])]
    for x0, x1, ln in boxes2: b.append(_fc_box(x0, x1, y2, ln, fill='#f3f7f4'))
    labs2 = [('7 phosphoglycerate', 'kinase'), ('8 phosphoglycerate', 'mutase'), ('9 enolase', '(&#8722; H<tspan font-size="10" baseline-shift="sub">2</tspan>O)'), ('10 pyruvate', 'kinase')]
    pills2 = ['ADP &#8594; ATP (&#215;2)', None, None, 'ADP &#8594; ATP (&#215;2)']
    for i in range(4):
        xa, xb = boxes2[i][0] - 6, boxes2[i + 1][1] + 6
        b.append(_fc_arrow(xa, y2, xb, y2))
        b.append(en((xa + xb) / 2, y2 - 40, labs2[i][0])); b.append(en((xa + xb) / 2, y2 - 26, labs2[i][1]))
        if pills2[i]: b.append(_fc_pill((xa + xb) / 2, y2 + 46, pills2[i], w=150))
    # net box
    b.append(f'<rect x="20" y="172" width="300" height="110" rx="12" fill="#efeaf8" stroke="{PURPLE}" stroke-width="2"/>')
    for k, ln in enumerate(['Net per glucose:', '2 ATP + 2 NADH', '+ 2 pyruvate', '(no O<tspan font-size="11" baseline-shift="sub">2</tspan> needed)']):
        b.append(T(170, 202 + 24 * k, ln, 15 if k else 14, 900 if k < 3 else 700, PURPLE, 'middle'))
    alt = ('Glycolysis in two phases. Energy-investment phase: glucose is phosphorylated by hexokinase using ATP to glucose 6-phosphate, isomerized to fructose 6-phosphate, '
           'phosphorylated again by phosphofructokinase-1 using a second ATP to fructose 1,6-bisphosphate, and split by aldolase into dihydroxyacetone phosphate (DHAP) and '
           'glyceraldehyde 3-phosphate; triose phosphate isomerase converts DHAP into a second glyceraldehyde 3-phosphate. Energy-payoff phase, run twice per glucose: '
           'glyceraldehyde 3-phosphate is oxidized by its dehydrogenase with NAD+ and inorganic phosphate to 1,3-bisphosphoglycerate; phosphoglycerate kinase transfers a '
           'phosphate to ADP giving ATP and 3-phosphoglycerate; a mutase moves the phosphate to give 2-phosphoglycerate; enolase removes water to give phosphoenolpyruvate; '
           'pyruvate kinase transfers the phosphate to ADP giving ATP and pyruvate. Net per glucose: 2 ATP, 2 NADH and 2 pyruvate, with no oxygen needed.')
    open(OUT + 'fig-p597193-glycolysis-flow.svg', 'w').write(svg(W, H, alt, ''.join(b)))


glycolysis_flow()
print('gflow ok')
