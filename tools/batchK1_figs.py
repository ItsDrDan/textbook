"""Batch K1 figures (house style of tools/batchF_figs.py). Run from repo root."""
import sys, os, math
sys.path.insert(0, 'tools')
from batchF_figs import T, svg, INK, MUTED, RED, BLUE, GREEN, PURPLE, FONT, _fc_box, _fc_arrow, _fc_pill, _sub

OUT = 'figures/pages/batchK/'
os.makedirs(OUT, exist_ok=True)
GOLD = '#9a7b00'
ALTS = {}


def L(x1, y1, x2, y2, col=INK, w=2.4, extra=''):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" {extra}/>'


def atom(x, y, s, col=INK, size=17, wpx=None):
    plain = len(s.replace('<tspan font-size="11" baseline-shift="sub">', '').replace('</tspan>', ''))
    w = wpx or (10.5 * plain + 6)
    return (f'<rect x="{x-w/2:.1f}" y="{y-12:.1f}" width="{w:.1f}" height="24" fill="#ffffff"/>'
            + T(x, y + 6, s, size, 800, col, 'middle'))


def dbl(x1, y1, x2, y2, col=INK, off=3.2, w=2.2):
    dx, dy = x2 - x1, y2 - y1; d = math.hypot(dx, dy); px, py = -dy / d * off, dx / d * off
    return L(x1 + px, y1 + py, x2 + px, y2 + py, col, w) + L(x1 - px, y1 - py, x2 - px, y2 - py, col, w)


def lp(x, y, ang, d=17, col=INK):
    a = math.radians(ang); cx, cy = x + d * math.cos(a), y + d * math.sin(a)
    px, py = -math.sin(a) * 4, math.cos(a) * 4
    return (f'<circle cx="{cx+px:.1f}" cy="{cy+py:.1f}" r="2.4" fill="{col}"/>'
            f'<circle cx="{cx-px:.1f}" cy="{cy-py:.1f}" r="2.4" fill="{col}"/>')


def hb(x1, y1, x2, y2):
    return L(x1, y1, x2, y2, GREEN, 3, 'stroke-dasharray="0.1 7"')


def save(name, W, H, alt, body):
    ALTS[name] = alt
    open(OUT + name, 'w').write(svg(W, H, alt, ''.join(body)))


# ---------------------------------------------------------------- 1. acetic acid dimer vs ethanol
def fig1():
    W, H = 980, 300
    b = []
    cy = 150
    # molecule A
    CA, OA1, OA2, HA = (180, cy), (222, cy - 46), (222, cy + 46), (268, cy + 46)
    CB, OB1, OB2, HB_ = (420, cy), (378, cy + 46), (378, cy - 46), (332, cy - 46)
    b.append(L(118, cy, *CA)); b.append(dbl(*CA, *OA1)); b.append(L(*CA, *OA2)); b.append(L(*OA2, *HA))
    b.append(L(*CB, 482, cy)); b.append(dbl(*CB, *OB1)); b.append(L(*CB, *OB2)); b.append(L(*OB2, *HB_))
    b.append(hb(HA[0] + 12, HA[1], OB1[0] - 13, OB1[1])); b.append(hb(HB_[0] - 12, HB_[1], OA1[0] + 13, OA1[1]))
    b.append(atom(100, cy, _sub('H3C'), INK, 17, 44)); b.append(atom(500, cy, _sub('CH3'), INK, 17, 44))
    b.append(atom(*CA, 'C')); b.append(atom(*CB, 'C'))
    for p in (OA1, OA2, OB1, OB2): b.append(atom(*p, 'O', RED))
    for p in (HA, HB_): b.append(atom(*p, 'H', INK, 17, 16))
    b.append(T(300, 40, 'Acetic acid (carboxylic acid)', 16, 900, INK, 'middle'))
    b.append(T(300, 62, 'head-to-head dimer', 14, 700, MUTED, 'middle'))
    b.append(T(300, 252, 'two hydrogen bonds per pair', 16, 900, GREEN, 'middle'))
    b.append(T(300, 274, 'O&#8211;H of each acid bonds to the C=O oxygen of the other', 13.5, 700, MUTED, 'middle'))
    b.append(L(600, 30, 600, 280, '#d5dbe3', 1.5))
    # ethanol pair
    ey = 140
    O1, H1, O2, H2 = (725, ey), (768, ey), (850, ey), (850, ey + 46)
    b.append(L(682, ey, *O1)); b.append(L(*O1, *H1)); b.append(hb(H1[0] + 12, ey, O2[0] - 13, ey))
    b.append(L(*O2, *H2)); b.append(L(*O2, 888, ey - 34))
    b.append(atom(650, ey, _sub('CH3CH2'), INK, 17, 72)); b.append(atom(*O1, 'O', RED)); b.append(atom(*H1, 'H', INK, 17, 16))
    b.append(atom(*O2, 'O', RED)); b.append(atom(*H2, 'H', INK, 17, 16))
    b.append(atom(905, ey - 46, _sub('CH2CH3'), INK, 17, 72))
    b.append(T(790, 40, 'Ethanol (alcohol)', 16, 900, INK, 'middle'))
    b.append(T(790, 62, 'one O&#8211;H per molecule', 14, 700, MUTED, 'middle'))
    b.append(T(790, 252, 'one hydrogen bond per pair', 16, 900, GREEN, 'middle'))
    b.append(T(790, 274, 'dotted line = hydrogen bond', 13.5, 700, MUTED, 'middle'))
    alt = ('Two side-by-side comparisons of hydrogen bonding. Left: two acetic acid molecules, CH3COOH, face each other head to head. '
           'The O-H hydrogen of each acid is joined by a dotted hydrogen bond to the C=O oxygen of the other acid, closing a ring, so the pair is held by two hydrogen bonds. '
           'Right: two ethanol molecules, CH3CH2OH; the O-H hydrogen of one is joined by a single dotted hydrogen bond to the oxygen of the other, so the pair is held by one hydrogen bond. '
           'Lone pairs are not shown.')
    save('fig-p597111-acid-dimer.svg', W, H, alt, b)


# ---------------------------------------------------------------- 2. RBC tonicity
def fig2():
    W, H = 1000, 380
    b = []
    def warrow(x1, y1, x2, y2):
        return _fc_arrow(x1, y1, x2, y2, BLUE, 3, 12)
    panels = [(170, 'Hypotonic', '0.45% NaCl', 'in'), (500, 'Isotonic', '0.9% NaCl (normal saline)', 'both'), (830, 'Hypertonic', '3% NaCl', 'out')]
    for cx, name, conc, mode in panels:
        b.append(f'<rect x="{cx-150}" y="78" width="300" height="196" rx="16" fill="#eef5fb" stroke="#9fbfdd" stroke-width="2"/>')
        b.append(T(cx, 36, name, 17, 900, INK, 'middle')); b.append(T(cx, 60, conc, 14.5, 700, MUTED, 'middle'))
        cy = 176
        if mode == 'in':
            b.append(f'<circle cx="{cx}" cy="{cy}" r="60" fill="#e9837d" stroke="{RED}" stroke-width="2.5"/>')
            for a in (225, 315, 45, 135):
                r = math.radians(a)
                b.append(warrow(cx + 128 * math.cos(r), cy + 92 * math.sin(r) / 0.95, cx + 70 * math.cos(r), cy + 64 * math.sin(r)))
            lines = ['Water moves in', 'Cell swells and may burst']
        elif mode == 'both':
            b.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="#d9534f" stroke="{RED}" stroke-width="2.5"/>')
            b.append(f'<circle cx="{cx}" cy="{cy}" r="19" fill="#f2b3ad"/>')
            for s in (-1, 1):
                b.append(warrow(cx + s * 128, cy - 12, cx + s * 58, cy - 12)); b.append(warrow(cx + s * 58, cy + 12, cx + s * 128, cy + 12))
            lines = ['Water in = water out (no net flow)', 'Normal biconcave disc']
        else:
            pts = []
            for i in range(241):
                t = 2 * math.pi * i / 240; r = 34 + 5.5 * math.cos(11 * t)
                pts.append(f'{cx + r*math.cos(t):.1f} {cy + r*math.sin(t):.1f}')
            b.append(f'<path d="M{" L".join(pts)} Z" fill="#b8322c" stroke="#8e1f1a" stroke-width="2"/>')
            for a in (225, 315, 45, 135):
                r = math.radians(a)
                b.append(warrow(cx + 48 * math.cos(r), cy + 48 * math.sin(r), cx + 128 * math.cos(r), cy + 88 * math.sin(r)))
            lines = ['Water moves out', 'Cell shrinks (crenates)']
        if mode == 'both':
            b.append(T(cx - 93, cy - 26, _sub('H2O'), 14, 800, BLUE, 'middle')); b.append(T(cx + 93, cy - 26, _sub('H2O'), 14, 800, BLUE, 'middle'))
        else:
            b.append(T(cx - 98, cy - 66, _sub('H2O'), 14, 800, BLUE, 'end')); b.append(T(cx + 98, cy + 80, _sub('H2O'), 14, 800, BLUE, 'start'))
        b.append(T(cx, 306, lines[0], 15.5, 900, INK, 'middle')); b.append(T(cx, 330, lines[1], 15, 700, MUTED, 'middle'))
    b.append(T(500, 366, 'Blue arrows show water crossing the red blood cell membrane (osmosis).', 13.5, 700, MUTED, 'middle'))
    alt = ('Three red blood cells, each in a different salt solution. Left, hypotonic, 0.45 percent NaCl: blue arrows point from the solution into the cell; '
           'water moves in, and the cell is drawn swollen and round because it swells and may burst. '
           'Middle, isotonic, 0.9 percent NaCl (normal saline): pairs of arrows point both in and out, showing no net movement of water; the cell is a normal biconcave disc with a pale center. '
           'Right, hypertonic, 3 percent NaCl: arrows point out of the cell; water moves out, and the cell is drawn small with a spiky, crenated edge because it shrinks.')
    save('fig-p597148-rbc-tonicity.svg', W, H, alt, b)


# ---------------------------------------------------------------- staircase glycogen tree (unscaled layout, main chain on y=210)
GLY = [  # name, parent, parent_idx, segments [(angle_deg, n)]
    ('M', None, None, [(0, 15)]),
    ('U1', 'M', 1, [(-60, 2), (0, 5)]), ('U2', 'U1', 3, [(-60, 2), (0, 5)]), ('U3', 'U2', 3, [(-60, 2), (0, 3)]),
    ('U4', 'M', 8, [(-60, 2), (0, 5)]), ('U5', 'U4', 3, [(-60, 2), (0, 3)]),
    ('D1', 'M', 3, [(60, 2), (0, 5)]), ('D2', 'D1', 3, [(60, 2), (0, 4)]), ('D3', 'D2', 3, [(60, 2), (0, 2)]),
    ('D4', 'M', 10, [(60, 2), (0, 4)]), ('D5', 'D4', 3, [(60, 2), (0, 2)]),
]


def gly_tree(tx, ty, s, r, fill, stroke, endfill, endstroke, sp=27):
    pos = {}
    bonds = []
    for name, par, pidx, segs in GLY:
        if par is None:
            x, y = 160 - sp, 210; prev = None
        else:
            x, y = pos[par][pidx]; prev = (x, y)
        pts = []
        for ang, n in segs:
            a = math.radians(ang)
            for _ in range(n):
                x, y = x + sp * math.cos(a), y + sp * math.sin(a)
                if prev: bonds.append((prev, (x, y)))
                prev = (x, y); pts.append((x, y))
        pos[name] = pts
    f = lambda p: (tx + (p[0] - 160) * s, ty + (p[1] - 210) * s)
    out = [L(*f(p), *f(q), stroke, 2) for p, q in bonds]
    ends = [pts[-1] for pts in pos.values()]
    for pts in pos.values():
        for p in pts:
            X, Y = f(p)
            e = p in ends
            out.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{r}" fill="{endfill if e else fill}" stroke="{endstroke if e else stroke}" stroke-width="1.7"/>')
    tpos = {k: [f(p) for p in v] for k, v in pos.items()}
    return out, tpos


# ---------------------------------------------------------------- 3. starch / glycogen / cellulose
def fig3():
    W, H = 1080, 420
    b = []
    SF, SS = '#f6dc8f', '#b8860b'
    # --- amylose helix (a coil seen from the side: axis horizontal)
    x0, cy, A, rx, p = 48, 196, 46, 7, 46   # p = advance per turn / 6 units per turn
    def hp(th):
        return (x0 + p * th / (2 * math.pi) * 2.0 + rx * math.sin(th), cy - A * math.cos(th), math.sin(th))
    N = 19
    seg = []
    for i in range(N * 10 - 9):
        th1, th2 = (i / 10) * math.pi / 3, ((i + 1) / 10) * math.pi / 3
        (xa, ya, za), (xb, yb, zb) = hp(th1), hp(th2)
        seg.append(((za + zb) / 2, f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="{SS}" stroke-width="2.4" stroke-linecap="round" opacity="{0.45 if (za+zb)/2 < 0 else 1}"/>'))
    units = []
    for i in range(N):
        x, y, z = hp(i * math.pi / 3)
        units.append((z, f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{SF}" stroke="{SS}" stroke-width="1.8" opacity="{0.55 if z < -0.05 else 1}"/>'))
    items = sorted(seg + units, key=lambda t: t[0])
    for kind in ('<line', '<circle'):
        for z, s_ in items:
            if z < 0 and s_.startswith(kind): b.append(s_.replace(' opacity="0.45"', '').replace(' opacity="0.55"', ''))
    b.append(f'<rect x="{x0-22}" y="{cy-A-4}" width="{2*3*p+44}" height="{2*A+8}" rx="16" fill="#ffffff" fill-opacity="0.6" stroke="#e4d3a1" stroke-width="1.2" stroke-dasharray="4 4"/>')
    for z, s_ in items:
        if z >= 0 and s_.startswith('<line'): b.append(s_)
    for z, s_ in items:
        if z >= 0 and s_.startswith('<circle'): b.append(s_)
    b.append(T(180, 40, 'Starch: amylose', 17, 900, INK, 'middle'))
    b.append(T(180, 62, 'unbranched, coils into a helix', 14, 700, MUTED, 'middle'))
    b.append(_fc_pill(180, 312, '&#945;(1&#8594;4) links', 150))
    b.append(T(180, 348, 'about six glucose units per turn', 14, 700, MUTED, 'middle'))
    b.append(T(180, 370, 'digested by amylase', 14, 700, MUTED, 'middle'))
    b.append(L(360, 30, 360, 400, '#d5dbe3', 1.5))
    # --- glycogen
    out, tp = gly_tree(398, 186, 0.62, 7, SF, SS, '#bfe3cf', GREEN, 27)
    b += out
    bx, by = tp['M'][1]
    b.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="11.5" fill="none" stroke="{PURPLE}" stroke-width="2.4"/>')
    b.append(T(540, 40, 'Glycogen', 17, 900, INK, 'middle'))
    b.append(T(540, 62, 'highly branched tree', 14, 700, MUTED, 'middle'))
    b.append(_fc_pill(462, 312, '&#945;(1&#8594;4) chains', 140))
    b.append(_fc_pill(622, 312, '&#945;(1&#8594;6) branches', 156, '#ece6f7', PURPLE, PURPLE))
    b.append(T(540, 348, 'branch (circled) about every 8&#8211;12 units', 14, 700, MUTED, 'middle'))
    b.append(T(540, 370, 'green = chain ends, where glucose', 14, 700, MUTED, 'middle'))
    b.append(T(540, 390, 'is added or removed', 14, 700, MUTED, 'middle'))
    b.append(L(720, 30, 720, 400, '#d5dbe3', 1.5))
    # --- cellulose
    CF, CS = '#d7ecd9', GREEN
    for row, y in enumerate((130, 190, 250)):
        xs = [762 + 30 * i for i in range(10)]
        for i in range(9): b.append(L(xs[i], y, xs[i + 1], y, CS, 2))
        if row < 2:
            for i in range(10): b.append(L(xs[i], y + 13, xs[i], y + 47, BLUE, 2.4, 'stroke-dasharray="0.1 6"'))
        for i, x in enumerate(xs):
            b.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{CF}" stroke="{CS}" stroke-width="1.8"/>')
            b.append(L(x, y - 5 if i % 2 == 0 else y + 5, x, y - 11 if i % 2 == 0 else y + 11, CS, 2))
    b.append(T(898, 40, 'Cellulose', 17, 900, INK, 'middle'))
    b.append(T(898, 62, 'straight chains in sheets', 14, 700, MUTED, 'middle'))
    b.append(_fc_pill(898, 312, '&#946;(1&#8594;4) links', 150, '#e3f1ea', GREEN, GREEN))
    b.append(T(898, 348, 'blue dots = hydrogen bonds between chains', 14, 700, MUTED, 'middle'))
    b.append(T(898, 370, 'humans cannot digest it', 14, 700, MUTED, 'middle'))
    alt = ('Schematic comparison of three glucose polymers, each glucose unit drawn as a circle. Left, starch amylose: an unbranched chain of glucose joined by alpha 1,4 links '
           'that coils into a helix, about six glucose units per turn; digested by amylase. '
           'Middle, glycogen: a highly branched tree; straight runs are alpha 1,4 chains and each branch starts at an alpha 1,6 link, one branch point circled, with a branch about every 8 to 12 units; '
           'the many chain ends are shaded green because glucose is added or removed there. '
           'Right, cellulose: three straight, parallel chains of glucose joined by beta 1,4 links, with each unit flipped relative to its neighbor, '
           'and rows of dotted blue hydrogen bonds holding neighboring chains together in a sheet; humans cannot digest it.')
    save('fig-p597140-polysaccharides.svg', W, H, alt, b)


# ---------------------------------------------------------------- 4. glycogen with glycogenin
def fig4():
    W, H = 1040, 420
    b = []
    SF, SS = '#f6dc8f', '#b8860b'
    gx, gy = 96, 210
    out, tp = gly_tree(160, gy, 1.0, 10, SF, SS, '#bfe3cf', GREEN, 27)
    b.append(f'<ellipse cx="{gx}" cy="{gy}" rx="36" ry="28" fill="#e9e3f5" stroke="{PURPLE}" stroke-width="2.5"/>')
    b.append(L(gx + 36, gy, 150, gy, PURPLE, 2.5))
    b += out
    b.append(T(gx, gy + 5, 'G', 17, 900, PURPLE, 'middle'))
    b.append(T(gx, gy + 54, 'glycogenin', 14.5, 900, PURPLE, 'middle'))
    b.append(T(gx, gy + 72, '(protein core)', 13, 700, PURPLE, 'middle'))
    fx, fy = tp['M'][0]
    b.append(_fc_arrow(fx - 22, gy - 70, fx - 4, gy - 15, MUTED, 1.8, 9))
    b.append(T(fx - 30, gy - 110, 'reducing end,', 13.5, 800, MUTED, 'middle'))
    b.append(T(fx - 30, gy - 93, 'tied to glycogenin', 13.5, 800, MUTED, 'middle'))
    bx, by = tp['M'][1]
    b.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="15" fill="none" stroke="{PURPLE}" stroke-width="2.6"/>')
    b.append(_fc_arrow(bx + 6, by + 84, bx + 2, by + 18, PURPLE, 1.8, 9))
    b.append(T(bx + 10, by + 104, '&#945;(1&#8594;6) branch point', 14, 900, PURPLE, 'middle'))
    ex, ey = tp['M'][-1]
    b.append(T(ex + 18, ey + 5, '&#8592; &#945;(1&#8594;4) chain', 14, 900, GOLD))
    kx, ky = 712, 150
    b.append(f'<circle cx="{kx}" cy="{ky}" r="10" fill="{SF}" stroke="{SS}" stroke-width="1.6"/>')
    b.append(T(kx + 20, ky + 5, 'glucose unit', 14.5, 800, INK))
    b.append(f'<circle cx="{kx}" cy="{ky+38}" r="10" fill="#bfe3cf" stroke="{GREEN}" stroke-width="1.8"/>')
    b.append(T(kx + 20, ky + 43, 'non-reducing end (free C4&#8211;OH)', 14.5, 900, GREEN))
    b.append(T(kx + 20, ky + 66, 'Glycogen synthase adds glucose here.', 14, 700, INK))
    b.append(T(kx + 20, ky + 86, 'Glycogen phosphorylase removes it here.', 14, 700, INK))
    b.append(T(kx + 20, ky + 116, 'Many branches = many ends, so', 14, 700, MUTED))
    b.append(T(kx + 20, ky + 136, 'glucose is stored and released fast.', 14, 700, MUTED))
    alt = ('Sketch of one glycogen molecule. A small protein, glycogenin, sits at the core on the left. A main chain of glucose units, drawn as circles, runs to the right from it; '
           'the first glucose, the reducing end, is tied to glycogenin. Straight runs are joined by alpha 1,4 links, and side chains branch off above and below the main chain, '
           'with smaller branches growing off the side chains. One branch point, where a new chain starts with an alpha 1,6 link, is circled. '
           'Every chain ends in a green non-reducing end with a free carbon 4 OH; there are many of them. A key explains that glycogen synthase adds glucose at the non-reducing ends '
           'and glycogen phosphorylase removes glucose there, so a highly branched molecule with many ends stores and releases glucose quickly.')
    save('fig-p597196-glycogen-branches.svg', W, H, alt, b)


# ---------------------------------------------------------------- 5. numbered acyl CoA
def chain_pts(x_c1, y_c1, n, bl=50):
    """carbons C1..Cn; C1 is a peak at (x_c1, y_c1); chain runs to the left."""
    pts = {}
    for k in range(1, n + 1):
        i = k - 1
        pts[k] = (x_c1 - i * bl * math.cos(math.radians(30)), y_c1 + (0 if i % 2 == 0 else bl * 0.5))
    return pts


def fig5():
    W, H = 1000, 420
    b = []
    S_COL = GOLD
    def row(yc, keto):
        o = []
        P = chain_pts(560, yc, 8)
        for k in range(1, 8): o.append(L(*P[k], *P[k + 1], INK, 2.6))
        # C1 carbonyl O up, S down-right
        c1 = P[1]; oy = c1[1] - 46
        o.append(dbl(c1[0], c1[1], c1[0], oy + 11, RED)); o.append(atom(c1[0], oy, 'O', RED))
        sx, sy = c1[0] + 43, c1[1] + 25
        o.append(L(*c1, sx - 8, sy - 5, INK, 2.6)); o.append(atom(sx, sy, 'S', S_COL))
        o.append(L(sx + 9, sy, sx + 42, sy, INK, 2.6)); o.append(T(sx + 46, sy + 6, 'CoA', 17, 900, INK))
        if keto:
            c3 = P[3]; o.append(dbl(c3[0], c3[1], c3[0], c3[1] - 35, RED)); o.append(atom(c3[0], c3[1] - 46, 'O', RED))
        # numbers
        for k in range(1, 9):
            x, y = P[k]
            peak = (k % 2 == 1)
            ny = y + (22 if peak else 26)
            o.append(T(x, ny + 5, str(k), 14.5, 900, BLUE, 'middle'))
        # greek
        o.append(T(P[2][0], P[2][1] + 52, '&#945;', 18, 900, PURPLE, 'middle'))
        o.append(T(P[3][0], P[3][1] + 48, '&#946;', 18, 900, RED, 'middle'))
        o.append(T(P[8][0] - 14, P[8][1] + 6, '&#8230;', 16, 900, MUTED, 'end'))
        return o, P
    # row 1: acyl CoA
    o, P = row(120, False)
    x3, y3 = P[3]
    b.append(f'<circle cx="{x3:.1f}" cy="{y3:.1f}" r="15" fill="#f9dcd8" stroke="none"/>')
    b += o
    b.append(T(30, 40, 'Fatty acyl CoA', 17, 900, INK))
    b.append(T(30, 62, 'numbered from the thioester carbon', 14, 700, MUTED))
    b.append(f'<rect x="{P[1][0]-24:.0f}" y="{P[1][1]-62:.0f}" width="150" height="104" rx="12" fill="none" stroke="{S_COL}" stroke-width="1.8" stroke-dasharray="6 4"/>')
    b.append(T(P[1][0] + 140, P[1][1] - 36, 'thioester: C1 is the', 14, 800, S_COL))
    b.append(T(P[1][0] + 140, P[1][1] - 18, 'C(=O)&#8211;S&#8211;CoA carbon', 14, 800, S_COL))
    b.append(T(P[1][0] + 140, P[1][1] + 22, 'C2 = &#945; carbon', 14, 800, PURPLE))
    b.append(T(P[1][0] + 140, P[1][1] + 42, 'C3 = &#946; carbon: this CH<tspan font-size="11" baseline-shift="sub">2</tspan> is', 14, 800, RED))
    b.append(T(P[1][0] + 140, P[1][1] + 60, 'oxidized to C=O in &#946;-oxidation', 14, 800, RED))
    b.append(L(20, 205, 980, 205, '#d5dbe3', 1.5))
    # row 2: 3-ketoacyl CoA
    o, P2 = row(312, True)
    b += o
    xc = (P2[2][0] + P2[3][0]) / 2
    b.append(L(xc, 240, xc, 380, MUTED, 2, 'stroke-dasharray="7 5"'))
    b.append(T(30, 236, '3-Ketoacyl CoA', 17, 900, INK))
    b.append(T(30, 256, '= &#946;-ketoacyl CoA', 17, 900, RED))
    b.append(T(30, 278, '(after reactions 1&#8211;3)', 14, 700, MUTED))
    b.append(T(xc, 404, 'thiolase cuts here, between &#945; and &#946;', 14, 800, MUTED, 'middle'))
    b.append(T(P2[1][0] + 140, P2[1][1] - 26, 'C=O now on C3, the &#946; carbon:', 14, 800, RED))
    b.append(T(P2[1][0] + 140, P2[1][1] - 8, '&#8220;3-keto&#8221; and &#8220;&#946;-keto&#8221; name', 14, 800, RED))
    b.append(T(P2[1][0] + 140, P2[1][1] + 10, 'the same carbon', 14, 800, RED))
    alt = ('Two skeletal structures of a fatty acyl CoA chain, drawn as zigzag lines running left from the thioester end, which is at the right. '
           'Top, fatty acyl CoA: carbon 1 is the thioester carbon, C double-bonded to O and single-bonded to S of coenzyme A, written C(=O)-S-CoA. '
           'The carbons are numbered 1, 2, 3 and onward from that carbon. Carbon 2 is labeled alpha and carbon 3 is labeled beta; carbon 3 is highlighted as the CH2 that is oxidized to C=O in beta-oxidation. '
           'Bottom, the 3-ketoacyl CoA formed after reactions 1 to 3: the same chain with a C=O on carbon 3, the beta carbon, so 3-ketoacyl CoA and beta-ketoacyl CoA are the same compound. '
           'A dashed line between carbons 2 and 3 marks where thiolase cuts, between the alpha and beta carbons.')
    save('fig-p597209-acyl-coa-numbering.svg', W, H, alt, b)


# ---------------------------------------------------------------- 6. linoleic acid omega numbering
def lin_pts(x1, y1, bl=46):
    heads = [30, -30, 30, -30, 30, -30, 30, -30, 30, 90, 30, -30, -90, -30, 30, -30, 30]  # bond k: Ck -> Ck+1 (math angles)
    P = {1: (x1, y1)}
    x, y = x1, y1
    for k, h in enumerate(heads, start=1):
        a = math.radians(h); x, y = x + bl * math.cos(a), y - bl * math.sin(a)
        P[k + 1] = (x, y)
    return P


def fig6():
    W, H = 1000, 416
    b = []
    def draw(y1, mode):
        o = []
        P = lin_pts(150, y1)
        dbonds = {(9, 10), (12, 13)}
        for k in range(1, 18):
            p, q = P[k], P[k + 1]
            if (k, k + 1) in dbonds:
                o.append(L(*p, *q, INK, 2.6))
                # inner line toward the cis side (toward neighbours k-1 and k+2)
                mx, my = (P[k - 1][0] + P[k + 2][0]) / 2, (P[k - 1][1] + P[k + 2][1]) / 2
                dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy); nx, ny = -dy / d, dx / d
                cx, cy = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
                if (mx - cx) * nx + (my - cy) * ny < 0: nx, ny = -nx, -ny
                o.append(L(p[0] + nx * 7 + dx * 0.17, p[1] + ny * 7 + dy * 0.17, q[0] + nx * 7 - dx * 0.17, q[1] + ny * 7 - dy * 0.17, INK, 2.6))
            else:
                o.append(L(*p, *q, INK, 2.6))
        # COOH at C1: =O at 150 deg, OH at 270 deg (math)
        c = P[1]
        ox, oy = c[0] + 40 * math.cos(math.radians(150)), c[1] - 40 * math.sin(math.radians(150))
        o.append(dbl(c[0], c[1], ox + 8, oy + 5, RED)); o.append(atom(ox, oy, 'O', RED))
        o.append(L(c[0], c[1], c[0], c[1] + 30, INK, 2.6)); o.append(atom(c[0], c[1] + 40, 'OH', RED, 17, 32))
        # labels at each vertex, outward
        for k in range(1, 19):
            x, y = P[k]
            if k == 1:
                ux, uy = 0.9, 0.6
            elif k == 18:
                ux, uy = 0.7, -0.7
            else:
                a = (P[k - 1][0] - x, P[k - 1][1] - y); c2 = (P[k + 1][0] - x, P[k + 1][1] - y)
                na, nc = math.hypot(*a), math.hypot(*c2)
                sx, sy = a[0] / na + c2[0] / nc, a[1] / na + c2[1] / nc
                ns = math.hypot(sx, sy)
                if ns < 1e-6: ux, uy = 0, -1
                else: ux, uy = -sx / ns, -sy / ns
            if mode == 'C':
                lab, col = str(k), BLUE
            else:
                lab, col = '&#969;' + str(19 - k), PURPLE
            hi = (mode == 'C' and k == 12) or (mode == 'W' and k == 13)
            d = 21 if mode == 'C' else 24
            if hi:
                o.insert(0, f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="#f9dcd8"/>')
            o.append(T(x + ux * d, y + uy * d + 5, lab, 14 if mode == 'C' else 13, 900, RED if hi else col, 'middle'))
        return o, P
    o, P = draw(120, 'C'); b += o
    b.append(T(30, 32, 'Linoleic acid, 18:2 (both C=C cis)', 17, 900, INK))
    b.append(T(30, 54, 'Chemist&#8217;s numbering: C1 = the COOH carbon', 14.5, 800, BLUE))
    b.append(T(870, 100, 'Last C=C starts at C12', 14.5, 900, RED, 'middle'))
    b.append(L(20, 196, 980, 196, '#d5dbe3', 1.5))
    o, P = draw(334, 'W'); b += o
    b.append(T(30, 226, 'Omega numbering: &#969;1 = the CH<tspan font-size="11" baseline-shift="sub">3</tspan> carbon', 14.5, 800, PURPLE))
    b.append(T(870, 310, 'First C=C from the', 14.5, 900, RED, 'middle'))
    b.append(T(870, 328, 'CH<tspan font-size="11" baseline-shift="sub">3</tspan> end starts at &#969;6', 14.5, 900, RED, 'middle'))
    b.append(T(870, 362, '18 &#8722; 12 = 6: omega-6', 16, 900, RED, 'middle'))
    alt = ('Linoleic acid, an 18-carbon fatty acid with two cis double bonds, drawn twice as the same zigzag chain with the COOH group at the left and the CH3 end at the right. '
           'Each cis double bond bends the chain. Top drawing, chemist numbering: carbons are numbered 1 to 18 starting from the COOH carbon; the double bonds are between C9 and C10 and between C12 and C13, '
           'and C12, where the last double bond starts, is highlighted. Bottom drawing, omega numbering: the same carbons are numbered omega 1 to omega 18 starting from the CH3 carbon, '
           'so C18 is omega 1 and C13 is omega 6. Omega 6 is highlighted as the first double-bonded carbon reached from the CH3 end. A note reads 18 minus 12 equals 6: omega-6.')
    save('fig-p597144-linoleic-omega.svg', W, H, alt, b)


# ---------------------------------------------------------------- 7. Lewis structure errors
def fig7():
    W, H = 1000, 412
    b = []
    BL = 40
    def H_(x, y): return atom(x, y, 'H', INK, 17, 16)
    def methanol(cx, cy, olp):
        o = [L(cx, cy, cx, cy - BL), L(cx, cy, cx, cy + BL), L(cx, cy, cx - BL, cy), L(cx, cy, cx + BL, cy)]
        ox = cx + BL; hx, hy = ox + 28, cy + 28
        o.append(L(ox, cy, hx, hy))
        o += [H_(cx, cy - BL), H_(cx, cy + BL), H_(cx - BL, cy), atom(cx, cy, 'C'), atom(ox, cy, 'O', RED), H_(hx, hy)]
        for a in olp: o.append(lp(ox, cy, a))
        return o
    def formaldehyde(cx, cy):
        o = [L(cx, cy, cx - 34, cy - 22), L(cx, cy, cx - 34, cy + 22), dbl(cx, cy, cx + 42, cy, INK, 3.4)]
        o += [H_(cx - 40, cy - 26), H_(cx - 40, cy + 26), atom(cx, cy, 'C'), atom(cx + 44, cy, 'O', RED)]
        o += [lp(cx + 44, cy, -55), lp(cx + 44, cy, 55)]
        return o
    def thiol(cx, cy, slp):
        c2, sx = cx + BL, cx + 2 * BL
        o = [L(cx, cy, cx, cy - BL), L(cx, cy, cx, cy + BL), L(cx, cy, cx - BL, cy), L(cx, cy, c2, cy),
             L(c2, cy, c2, cy - BL), L(c2, cy, c2, cy + BL), L(c2, cy, sx, cy), L(sx, cy, sx + 28, cy + 28)]
        o += [H_(cx, cy - BL), H_(cx, cy + BL), H_(cx - BL, cy), H_(c2, cy - BL), H_(c2, cy + BL), H_(sx + 28, cy + 28),
              atom(cx, cy, 'C'), atom(c2, cy, 'C'), atom(sx, cy, 'S', GOLD)]
        for a in slp: o.append(lp(sx, cy, a))
        return o
    def amine(cx, cy, wrong):
        nx = cx + BL
        o = [L(cx, cy, cx, cy - BL), L(cx, cy, cx, cy + BL), L(cx, cy, cx - BL, cy), L(cx, cy, nx, cy),
             L(nx, cy, nx + BL, cy), L(nx, cy, nx, cy + BL)]
        if wrong: o.append(L(nx, cy, nx, cy - BL))
        o += [H_(cx, cy - BL), H_(cx, cy + BL), H_(cx - BL, cy), atom(cx, cy, 'C'), atom(nx, cy, 'N', BLUE), H_(nx + BL, cy), H_(nx, cy + BL)]
        if wrong: o.append(H_(nx, cy - BL))
        else: o.append(lp(nx, cy, -90))
        return o
    cells = [
        (0, 0, '(a) Methanol, CH<tspan font-size="11" baseline-shift="sub">3</tspan>OH', lambda x, y: methanol(x, y, (-90, -10, 125)), lambda x, y: methanol(x, y, (-90, -10)),
         'Too many electrons: O has 3 lone pairs (16 e<tspan font-size="11" baseline-shift="super">&#8722;</tspan>; needs 14)'),
        (1, 0, '(b) Formaldehyde, H<tspan font-size="11" baseline-shift="sub">2</tspan>C=O', lambda x, y: formaldehyde(x, y), None,
         'Correct: 12 e<tspan font-size="11" baseline-shift="super">&#8722;</tspan>, C has 4 bonds, O has 2 bonds + 2 lone pairs'),
        (0, 1, '(c) Ethanethiol, CH<tspan font-size="11" baseline-shift="sub">3</tspan>CH<tspan font-size="11" baseline-shift="sub">2</tspan>SH', lambda x, y: thiol(x, y, (-45,)), lambda x, y: thiol(x, y, (-90, -10)),
         'Octet not satisfied: S with one lone pair has only 6 e<tspan font-size="11" baseline-shift="super">&#8722;</tspan>'),
        (1, 1, '(d) Methylamine, CH<tspan font-size="11" baseline-shift="sub">3</tspan>NH<tspan font-size="11" baseline-shift="sub">2</tspan>', lambda x, y: amine(x, y, True), lambda x, y: amine(x, y, False),
         'Wrong bond count: 4 bonds, no lone pair is N<tspan font-size="11" baseline-shift="super">+</tspan> (CH<tspan font-size="11" baseline-shift="sub">3</tspan>NH<tspan font-size="11" baseline-shift="sub">3</tspan><tspan font-size="11" baseline-shift="super">+</tspan>)'),
    ]
    for col, rw, title, drawn, fixed, err in cells:
        x0, y0 = 10 + col * 500, 6 + rw * 204
        b.append(f'<rect x="{x0}" y="{y0}" width="480" height="194" rx="12" fill="#ffffff" stroke="#d5dbe3" stroke-width="1.5"/>')
        b.append(T(x0 + 14, y0 + 24, title, 15.5, 900, INK))
        cy = y0 + 104
        if fixed:
            b.append(T(x0 + 120, y0 + 42, 'as drawn', 13.5, 800, RED, 'middle'))
            b.append(T(x0 + 360, y0 + 42, 'corrected', 13.5, 800, GREEN, 'middle'))
            b += drawn(x0 + 95, cy)
            b.append(_fc_arrow(x0 + 218, cy, x0 + 266, cy, MUTED, 2.4, 10))
            b += fixed(x0 + 335, cy)
            b.append(T(x0 + 240, y0 + 176, err, 14, 800, RED, 'middle'))
        else:
            b.append(T(x0 + 240, y0 + 42, 'as drawn', 13.5, 800, GREEN, 'middle'))
            b += drawn(x0 + 240, cy)
            b.append(T(x0 + 240, y0 + 176, err, 14, 800, GREEN, 'middle'))
    alt = ('Four Lewis structures that students drew, each in its own box. '
           '(a) Methanol, CH3OH, as drawn: carbon bonded to three H and to O, and the O bonded to one H with three lone pairs. Corrected: the O has two lone pairs. '
           'Error: too many electrons; the drawing uses 16 electrons but methanol has 14. '
           '(b) Formaldehyde, H2C=O: carbon bonded to two H and double-bonded to O, which has two lone pairs. This one is correct: 12 electrons, carbon has four bonds, oxygen has two bonds and two lone pairs. '
           '(c) Ethanethiol, CH3CH2SH, as drawn: the sulfur has two bonds and only one lone pair. Corrected: the sulfur has two lone pairs. Error: octet not satisfied; S has only 6 electrons. '
           '(d) Methylamine, as drawn: the nitrogen is bonded to the carbon and to three H, with no lone pair. Corrected: CH3NH2, nitrogen bonded to carbon and two H with one lone pair. '
           'Error: four bonds and no lone pair is the pattern of a positive nitrogen, as in CH3NH3+.')
    save('fig-p597056-lewis-errors.svg', W, H, alt, b)


# ---------------------------------------------------------------- 8. lidocaine neutral share
def fig8():
    W, H = 1000, 360
    b = []
    x0, xmax = 330, 930
    b.append(T(30, 34, 'How much of the lidocaine is in the neutral, membrane-crossing form (R<tspan font-size="11" baseline-shift="sub">3</tspan>N)?', 16.5, 900, INK))
    rows = [(92, 'In the cartridge', 'acidic, pH about 3.5&#8211;6.5', 22, '#8fa6b8', 'almost all charged R<tspan font-size="11" baseline-shift="sub">3</tspan>NH<tspan font-size="11" baseline-shift="super">+</tspan>Cl<tspan font-size="11" baseline-shift="super">&#8722;</tspan>: the dissolved salt', None),
            (174, 'Healthy tissue', 'buffered to pH 7.4', 380, GREEN, None, 'more neutral R<tspan font-size="11" baseline-shift="sub">3</tspan>N: crosses the nerve membrane'),
            (256, 'Abscess or inflamed tissue', 'pH lower than 7.4', 90, RED, 'more stays as R<tspan font-size="11" baseline-shift="sub">3</tspan>NH<tspan font-size="11" baseline-shift="super">+</tspan>: slower, weaker anesthesia', None)]
    for y, name, ph, w, col, note_out, note_in in rows:
        b.append(T(x0 - 16, y - 3, name, 15.5, 900, INK, 'end'))
        b.append(T(x0 - 16, y + 17, ph, 14, 700, MUTED, 'end'))
        b.append(f'<rect x="{x0}" y="{y-20}" width="{w}" height="40" rx="6" fill="{col}"/>')
        if note_out: b.append(T(x0 + w + 12, y + 5, note_out, 14, 800, col if col != '#8fa6b8' else MUTED))
        if note_in: b.append(T(x0 + 12, y + 5, note_in, 14, 800, '#ffffff'))
    b.append(L(x0, 60, x0, 286, INK, 2))
    b.append(_fc_arrow(x0, 300, xmax, 300, INK, 2, 11))
    b.append(T(x0, 322, 'less', 14, 800, MUTED, 'start'))
    b.append(T(xmax, 322, 'more', 14, 800, MUTED, 'end'))
    b.append(T((x0 + xmax) / 2, 344, 'share in the neutral form (qualitative, not to scale)', 14, 800, INK, 'middle'))
    alt = ('Qualitative horizontal bar chart of how much of the lidocaine is in the neutral, uncharged amine form, R3N, the only form that crosses the nerve membrane, in three places. No numbers are given. '
           'In the cartridge, which is acidic at about pH 3.5 to 6.5, the bar is very short: almost all the drug is the charged, dissolved salt R3NH+ Cl-. '
           'In healthy tissue, buffered to pH 7.4, the bar is much longer: more of the drug is neutral R3N, which crosses the nerve membrane. '
           'In an abscess or inflamed tissue, where the pH is lower than 7.4, the bar is short again: more drug stays as R3NH+, so anesthesia is slower and weaker.')
    save('fig-p597123-lidocaine-neutral.svg', W, H, alt, b)


for f in (fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8):
    f()
import json
json.dump(ALTS, open('/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/K1_alts.json', 'w'), indent=1)
print('K1 done')
