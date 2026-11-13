exec(open('/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/k2_common.py').read())
from rdkit import Chem
import math, sys
m = Mol('NC(CC(=O)O)C(=O)NC(Cc1ccccc1)C(=O)OC')
print(Chem.rdMolDescriptors.CalcMolFormula(m.m))
P = m.p
PURPLE = '#86509b'; ORANGE = '#c46a1b'
groups = [  # atoms, colour, pad, label, label pos (dx,dy rel to box corner logic), anchor
    ([0], BLUE, (22, 14), 'amine', 'top', None),
    ([3, 4, 5], RED, (14, 14), 'carboxylic acid', 'left', None),
    ([6, 7, 8], ORANGE, (14, 14), 'amide', 'top', None),
    ([17, 18, 19], PURPLE, (14, 14), 'ester', 'right', None),
    ([11, 12, 13, 14, 15, 16], GREEN, (12, 12), 'aromatic ring', 'right', None),
]
under = []; over = []
ext = [1e9, 1e9, -1e9, -1e9]
for atoms, col, (px, py), lab, where, _ in groups:
    xs = [P[a][0] for a in atoms]; ys = [P[a][1] for a in atoms]
    x0, x1, y0, y1 = min(xs) - px, max(xs) + px, min(ys) - py, max(ys) + py
    if atoms == [0]: x0 -= 12  # H2N text extends left of N
    if atoms == [6, 7, 8]: x1 += 12  # H of NH sits right of N
    w, h = x1 - x0, y1 - y0
    rx = min(w, h) / 2 if len(atoms) == 6 else 12
    under.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx:.1f}" fill="{col}" fill-opacity="0.08" stroke="{col}" stroke-width="2" stroke-dasharray="6 4"/>')
    if where == 'top': lx, ly, an = (x0 + x1) / 2, y0 - 8, 'middle'
    elif where == 'left': lx, ly, an = x0 - 8, (y0 + y1) / 2 + 5, 'end'
    elif where == 'right': lx, ly, an = x1 + 8, (y0 + y1) / 2 + 5, 'start'
    else: lx, ly, an = (x0 + x1) / 2, y1 + 20, 'middle'
    over.append(text(lx, ly, lab, col, 16, 800, anchor=an, fmt=False))
    lw = len(lab) * 9.2
    lx0 = lx - (lw if an == 'end' else lw / 2 if an == 'middle' else 0)
    ext = [min(ext[0], x0, lx0), min(ext[1], y0, ly - 16), max(ext[2], x1, lx0 + lw), max(ext[3], y1, ly + 4)]
m.els = under + m.els + over
els = []
b = [min(m.box[0], ext[0]) - 6, min(m.box[1], ext[1]) - 6, max(m.box[2], ext[2]) + 6, max(m.box[3], ext[3]) + 6]
dx, dy = -b[0], -b[1]
els += m.shifted(dx, dy)
W = b[2] - b[0]; H = b[3] - b[1]
els.append(label(W / 2, H + 12, 'aspartame', 16, weight=700))
alt = 'Skeletal structure of aspartame with each functional group circled and labeled in color: the amine, NH2 (blue), at the left; the carboxylic acid, C=O with OH (red), on the side chain below it; the amide, C=O bonded to NH (orange), joining the two halves of the molecule; the ester, C=O bonded to O–CH3 (purple), at the right; and the aromatic ring, a benzene ring (green), at the top right.'
save(wrap(els, 0, 0, W, H + 20, alt, 0.8), 'fig-p597059-aspartame-groups.svg', 6)
