"""Enlarge the circled phosphate "P" in figures where it printed under 6 pt (21:39 compile, 2026-11-13).
Per circled P: font x1.19, circle radius x1.14, baseline kept centred; a text run that starts just right of the circle
(the "i" of Pi, an "O", a minus) moves right by the radius increase so it does not touch. Idempotent per file
(a file already done carries data-circledp="1").   Usage: python3 tools/enlarge_circled_p.py file.svg ...
tools/glycolysis.js uses the same ratios, so regenerating a pathway figure keeps the larger P."""
import re, sys
CIRC = re.compile(r'<circle cx="([0-9.]+)" cy="([0-9.]+)" r="([0-9.]+)" fill="#ffe1c2" stroke="#d9822b" stroke-width="1.6"/><text x="([0-9.]+)" y="([0-9.]+)" text-anchor="middle" font-family="([^"]+)" font-size="([0-9.]+)" font-weight="900" fill="#8a4a0e">P</text>(<text x=")?([0-9.]+)?')
r1 = lambda v: ('%.1f' % v).rstrip('0').rstrip('.')
for f in sys.argv[1:]:
    t = open(f, encoding='utf-8').read()
    if 'data-circledp="1"' in t: print(f, 'already done'); continue
    n = 0
    def sub(m):
        global n; n += 1
        cx, cy, r, tx, ty, fam, fs = float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4), float(m.group(5)), m.group(6), float(m.group(7))
        r2, fs2 = r * 1.14, fs * 1.19; ty2 = cy + (ty - cy) * 1.19
        out = (f'<circle cx="{m.group(1)}" cy="{m.group(2)}" r="{r1(r2)}" fill="#ffe1c2" stroke="#d9822b" stroke-width="1.6"/>'
               f'<text x="{tx}" y="{r1(ty2)}" text-anchor="middle" font-family="{fam}" font-size="{r1(fs2)}" font-weight="900" fill="#8a4a0e">P</text>')
        if m.group(8):
            nx = float(m.group(9))
            out += '<text x="' + (r1(nx + (r2 - r)) if cx < nx <= cx + r + 4 else m.group(9))
        return out
    t2 = CIRC.sub(sub, t)
    t2 = re.sub(r'<svg\b', '<svg data-circledp="1"', t2, count=1)
    open(f, 'w', encoding='utf-8').write(t2); print(f, n, 'circled P enlarged')
