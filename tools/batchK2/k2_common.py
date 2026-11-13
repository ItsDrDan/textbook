import sys, os, re
sys.path.insert(0, '/Users/dan/Desktop/Study Games/textbook-git/tools')
os.chdir('/Users/dan/Desktop/Study Games/textbook-git')
from rdsvg import *
import resvg_py
OUT = 'figures/pages/batchK/'
SP = '/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/'
def save(svg, fname, n, width=None):
    open(OUT + fname, 'w').write(svg)
    m = re.search(r'width="(\d+)" height="(\d+)"', svg)
    w, h = int(m.group(1)), int(m.group(2))
    png = resvg_py.svg_to_bytes(svg_path=OUT + fname, width=(width or w * 2))
    open(SP + f'K2_{n}.png', 'wb').write(bytes(png))
    print(fname, w, h, 'ratio %.2f' % (w / h))
def insert(svg, extra):
    return svg.replace('</svg>', ''.join(extra) + '</svg>')

import rdsvg
def ct(x, y, s, size=20, col=INK, anchor='start', weight=None):
    """condensed text: digits after a letter/')' subscripted; '^-' '^+' superscript. Each run is a tspan with explicit dy."""
    runs = []  # (text, level, small)
    i = 0
    while i < len(s):
        c = s[i]
        if c == '^':
            runs.append((s[i+1], -1)); i += 2; continue
        if c.isdigit() and i > 0 and (s[i-1].isalpha() or s[i-1] == ')' or (s[i-1].isdigit() and runs and runs[-1][1] == 1)):
            runs.append((c, 1))
        else:
            runs.append((c.replace('&', '&amp;'), 0))
        i += 1
    merged = []
    for t, l in runs:
        if merged and merged[-1][1] == l: merged[-1] = (merged[-1][0] + t, l)
        else: merged.append((t, l))
    off = {0: 0, 1: size * 0.25, -1: -size * 0.45}
    cur = 0; out = ''
    for t, l in merged:
        dy = off[l] - cur; cur = off[l]
        fs = f' font-size="{size*0.72:.0f}"' if l else ''
        out += f'<tspan dy="{dy:.1f}"{fs}>{t}</tspan>'
    wt = f' font-weight="{weight}"' if weight else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-family="{CFONT}"{wt} fill="{col}">{out}</text>'
def cw(s, size=20):
    s2 = re.sub(r'\^.', '', s)
    return rdsvg._w(s2, size) + (size*0.5 if '^' in s else 0)
def label(x, y, s, size=15, col=INK, anchor='middle', weight=600):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" font-family="{FONT}" fill="{col}">{s}</text>'
def arrow(x, y, w, above='', below='', size=14):
    e = [line(x, y, x + w, y, 2.2), line(x + w, y, x + w - 11, y - 7, 2.2), line(x + w, y, x + w - 11, y + 7, 2.2)]
    if above: e.append(label(x + w/2, y - 10, above, size))
    if below: e.append(label(x + w/2, y + 22, below, size))
    return e
def wrap(els, x0, y0, w, h, alt, scale=1.0):
    alt = alt.replace('"', '&quot;')
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg data-printfix="1" xmlns="http://www.w3.org/2000/svg" class="mol" '
            f'viewBox="{x0:.0f} {y0:.0f} {w:.0f} {h:.0f}" width="{w*scale:.0f}" height="{h*scale:.0f}" role="img" aria-label="{alt}">'
            + ''.join(els) + '</svg>\n')
def cmol(x, y, groups, size=20, colors=None, branches=None, bonds='–', dbl=()):
    """groups: list of str (joined with bond dash); branches {i: (above, below)}; colors {i or (i,'a'|'b'): col}.
    returns els, end-x, dict of group-centre x"""
    colors = colors or {}; branches = branches or {}
    els = []; cx = {}
    for i, g in enumerate(groups):
        if i: 
            sep = bonds if isinstance(bonds, str) else bonds[i-1]
            if sep:
                els.append(ct(x, y, sep, size)); x += cw(sep, size)
        first = re.match(r'[A-Z][a-z]?', g).group(0) if re.match(r'[A-Z]', g) else g[0]
        lead = g[:g.index(first)] if first in g else ''
        cx[i] = x + cw(lead, size) + cw(first, size) / 2
        els.append(ct(x, y, g, size, colors.get(i, INK))); x += cw(g, size)
    for i, (ab, be) in branches.items():
        if ab:
            if i in dbl:
                for d in (-2.6, 2.6): els.append(line(cx[i] + d, y - size * 0.85, cx[i] + d, y - size * 0.85 - 16, 1.6))
            else:
                els.append(line(cx[i], y - size * 0.85, cx[i], y - size * 0.85 - 16, 1.6))
            els.append(ct(cx[i], y - size * 0.85 - 21, ab, size, colors.get((i, 'a'), INK), anchor='middle'))
        if be:
            els.append(line(cx[i], y + size * 0.3, cx[i], y + size * 0.3 + 16, 1.6))
            els.append(ct(cx[i], y + size * 0.3 + 16 + size, be, size, colors.get((i, 'b'), INK), anchor='middle'))
    return els, x, cx

SUB2 = '<tspan dy="3" font-size="11">2</tspan><tspan dy="-3">O</tspan>'
