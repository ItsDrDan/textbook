#!/usr/bin/env python3
"""Hand-layout fused-ring structures in the same style as draw.js (for rings the engine cannot lay out).
atoms: list of (x, y, label, color) in math coords (y up); label '' for carbon.
bonds: list of (i, j, order, side) ; side = (cx, cy) point toward which the second line is offset.
"""
import math, sys
INK = '#2d3f4b'; BLUE = '#2f5fc4'; RED = '#c0392b'
FONT = 'Inter,Helvetica,Arial,sans-serif'

def render(atoms, bonds, alt, pad=22):
    pts = [(a[0], -a[1]) for a in atoms]
    out = []
    for (i, j, order, side) in bonds:
        (x1, y1), (x2, y2) = pts[i], pts[j]
        dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        s1 = 12 if atoms[i][2] else 0; s2 = 12 if atoms[j][2] else 0
        ax, ay, bx, by = x1 + ux * s1, y1 + uy * s1, x2 - ux * s2, y2 - uy * s2
        out.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>')
        if order == 2:
            sx, sy = side; sx, sy = sx, -sy
            # normal pointing toward side
            nx, ny = -uy, ux
            if (sx - (x1 + x2) / 2) * nx + (sy - (y1 + y2) / 2) * ny < 0: nx, ny = -nx, -ny
            off = 5.5; sh = 0.14 * L
            ax2, ay2 = x1 + ux * (s1 + sh) + nx * off, y1 + uy * (s1 + sh) + ny * off
            bx2, by2 = x2 - ux * (s2 + sh) + nx * off, y2 - uy * (s2 + sh) + ny * off
            out.append(f'<line x1="{ax2:.1f}" y1="{ay2:.1f}" x2="{bx2:.1f}" y2="{by2:.1f}" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>')
    for (x, y), a in zip(pts, atoms):
        if a[2]:
            lab = a[2]; col = a[3] if len(a) > 3 and a[3] else BLUE
            anchor = 'middle'
            txt = lab.replace('2', '<tspan font-size="13" dy="4">2</tspan><tspan dy="-4"> </tspan>').replace('+', '<tspan font-size="13" dy="-8">+</tspan>')
            out.append(f'<text x="{x:.1f}" y="{y + 6.5:.1f}" text-anchor="{anchor}" fill="{col}" font-size="19" font-weight="800" font-family="{FONT}" stroke="#fff" stroke-width="5" stroke-linejoin="round" paint-order="stroke">{txt}</text>')
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    x0, y0 = min(xs) - pad - 10, min(ys) - pad; w = max(xs) - min(xs) + 2 * pad + 20; h = max(ys) - min(ys) + 2 * pad
    sc = 0.85
    return (f'<svg xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto" class="mol" viewBox="{x0:.0f} {y0:.0f} {w:.0f} {h:.0f}" '
            f'width="{w*sc:.0f}" height="{h*sc:.0f}" role="img" aria-label="{alt}">' + ''.join(out) + '</svg>')

L = 36.0
H = [(0, 36), (31.2, 18), (31.2, -18), (0, -36), (-31.2, -18), (-31.2, 18)]  # hexagon: 90,30,-30,-90,-150,150 deg
P = [(31.2, 18), (65.5, 29.1), (86.6, 0), (65.5, -29.1), (31.2, -18)]  # pentagon fused on the right edge, top to bottom
HC = (0, 0); PC = (56, 0)

def indole():
    # N at top of pentagon (N1 adjacent to C7a which is the top fusion carbon)
    atoms = [(*H[0], '', ''), (*H[1], '', ''), (*H[2], '', ''), (*H[3], '', ''), (*H[4], '', ''), (*H[5], '', ''),
             (*P[1], 'NH', BLUE), (*P[2], '', ''), (*P[3], '', '')]
    # hex idx: 0 C7, 1 C7a, 2 C3a, 3 C4, 4 C5, 5 C6 ; 6 N1, 7 C2, 8 C3
    bonds = [(0, 1, 2, HC), (1, 2, 1, HC), (2, 3, 2, HC), (3, 4, 1, HC), (4, 5, 2, HC), (5, 0, 1, HC),
             (1, 6, 1, PC), (6, 7, 1, PC), (7, 8, 2, PC), (8, 2, 1, PC)]
    return atoms, bonds

def purine():
    # hex: 0 C6, 1 C5, 2 C4, 3 N3, 4 C2, 5 N1 ; pent: 6 N7, 7 C8, 8 N9(H)
    atoms = [(*H[0], '', ''), (*H[1], '', ''), (*H[2], '', ''), (*H[3], 'N', BLUE), (*H[4], '', ''), (*H[5], 'N', BLUE),
             (*P[1], 'N', BLUE), (*P[2], '', ''), (*P[3], 'NH', BLUE)]
    bonds = [(5, 0, 2, HC), (0, 1, 1, HC), (1, 2, 2, HC), (2, 3, 1, HC), (3, 4, 2, HC), (4, 5, 1, HC),
             (1, 6, 1, PC), (6, 7, 2, PC), (7, 8, 1, PC), (8, 2, 1, PC)]
    return atoms, bonds

def serotonin():
    # indole with N at bottom; chain on C3 (top pentagon vertex), OH on C5
    # hex: 0 C4, 1 C3a, 2 C7a, 3 C7, 4 C6, 5 C5 ; pent: 6 C3, 7 C2, 8 N1
    atoms = [(*H[0], '', ''), (*H[1], '', ''), (*H[2], '', ''), (*H[3], '', ''), (*H[4], '', ''), (*H[5], '', ''),
             (*P[1], '', ''), (*P[2], '', ''), (*P[3], 'NH', BLUE),
             (47.5, 60.3, '', ''), (65.5, 91.5, '', ''), (47.5, 122.7, 'NH2', BLUE),
             (-62.4, 36, 'HO', RED)]
    bonds = [(0, 1, 2, HC), (1, 2, 1, HC), (2, 3, 2, HC), (3, 4, 1, HC), (4, 5, 2, HC), (5, 0, 1, HC),
             (1, 6, 1, PC), (6, 7, 2, PC), (7, 8, 1, PC), (8, 2, 1, PC),
             (6, 9, 1, None), (9, 10, 1, None), (10, 11, 1, None), (5, 12, 1, None)]
    return atoms, bonds

def nicotine():
    # pyridine: 0 N1(-31.2,-18) 1 C2(0,-36) 2 C3(31.2,-18) 3 C4(31.2,18) 4 C5(0,36) 5 C6(-31.2,18)
    atoms = [(-31.2, -18, 'N', BLUE), (0, -36, '', ''), (31.2, -18, '', ''), (31.2, 18, '', ''), (0, 36, '', ''), (-31.2, 18, '', ''),
             (62.4, -36, '', ''), (95.3, -21.4, 'N', BLUE), (119.3, -48.1, '', ''), (101.3, -79.3, '', ''), (66.2, -71.8, '', ''),
             (102.8, 13.8, '', '')]
    bonds = [(0, 1, 1, HC), (1, 2, 2, HC), (2, 3, 1, HC), (3, 4, 2, HC), (4, 5, 1, HC), (5, 0, 2, HC),
             (2, 6, 1, None), (6, 7, 1, None), (7, 8, 1, None), (8, 9, 1, None), (9, 10, 1, None), (10, 6, 1, None), (7, 11, 1, None)]
    return atoms, bonds

if __name__ == '__main__':
    which = sys.argv[1]; alt = sys.argv[2]
    a, b = globals()[which]()
    sys.stdout.write(render(a, b, alt))
