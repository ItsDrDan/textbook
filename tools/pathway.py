"""Python port of tools/pathway.js (same spec, same output style), so diagrams can be rebuilt without node.
Usage: python3 tools/pathway.py spec.json > out.svg   or   from pathway import render; render(spec) -> svg string
Spec: {title?, colw?, rowh?, pad?, font?, edgefont?, nodes:[{id,label,col,row,kind?,w?,h?}],
       edges:[{from,to,label?,kind?,via?,curve?,labelPos?,labelSide?}], groups?:[{label,cols,rows,fill?}], alt?}
"""
import json, math, sys

FONT = 'Nunito,Inter,Helvetica,Arial,sans-serif'
INK, MUTED, LINE = '#2d3f4b', '#4f5a74', '#c9d1dc'
KIND = {'mol': dict(fill='#ffffff', stroke='#8fa6b8', text=INK, bold=700),
        'energy': dict(fill='#fff6e2', stroke='#e2c77a', text='#80601a', bold=800),
        'enzyme': dict(fill='none', stroke='none', text='#3b5f7a', bold=700, italic=True),
        'note': dict(fill='#f3effd', stroke='#c9b8ea', text='#4a3a73', bold=600),
        'tissue': dict(fill='#e8f6ef', stroke='#a9d9c2', text='#23704f', bold=800),
        'ghost': dict(fill='none', stroke='none', text=MUTED, bold=600),
        'start': dict(fill='#f2e8f7', stroke='#b48cc8', text='#5b3a72', bold=800)}


def esc(s): return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
def f1(v): return f'{v:.1f}'


def render(spec):
    COLW, ROWH, PAD, FS = spec.get('colw', 150), spec.get('rowh', 90), spec.get('pad', 16), spec.get('font', 15)
    EFS = spec.get('edgefont', FS - 3)
    TT = 30 if spec.get('title') else 0
    allC = [n['col'] for n in spec['nodes']] + [v[0] for e in spec.get('edges', []) for v in e.get('via', [])]
    allR = [n['row'] for n in spec['nodes']] + [v[1] for e in spec.get('edges', []) for v in e.get('via', [])]
    cols, rows = math.ceil(max(allC)) + 1, math.ceil(max(allR)) + 1
    px = lambda c: PAD + COLW * (c + 0.5)
    py = lambda r: PAD + TT + ROWH * (r + 0.5)
    nodes = {}
    for n in spec['nodes']:
        lines = str(n['label']).split('\n'); k = KIND[n.get('kind', 'mol')]
        tw = max(len(l) for l in lines) * FS * 0.56 + 22
        n['w'] = n.get('w') or min(max(tw, 64), COLW * 1.6); n['h'] = n.get('h') or (len(lines) * (FS + 4) + 14)
        n['x'], n['y'], n['lines'], n['k'] = px(n['col']), py(n['row']), lines, k; nodes[n['id']] = n
    W, H = PAD * 2 + COLW * cols, PAD * 2 + TT + ROWH * rows
    out, labels = '', ''
    for g in spec.get('groups', []):
        x0, x1 = PAD + COLW * g['cols'][0], PAD + COLW * (g['cols'][1] + 1)
        y0, y1 = PAD + TT + ROWH * g['rows'][0], PAD + TT + ROWH * (g['rows'][1] + 1)
        out += f'<rect x="{x0+4}" y="{y0+4}" width="{x1-x0-8}" height="{y1-y0-8}" rx="16" fill="{g.get("fill", "#f7f8fb")}" stroke="{LINE}" stroke-dasharray="6 4" stroke-width="1.5"/>'
        out += f'<text x="{x0+16}" y="{y0+24}" font-size="{FS-2}" font-weight="800" fill="{MUTED}" font-family="{FONT}">{esc(g["label"])}</text>'

    def anchor(n, tx, ty):
        dx, dy = tx - n['x'], ty - n['y']
        if not dx and not dy: return [n['x'], n['y']]
        hw, hh = n['w'] / 2 + 4, n['h'] / 2 + 4
        sx = hw / abs(dx) if abs(dx) > 1e-6 else 1e9; sy = hh / abs(dy) if abs(dy) > 1e-6 else 1e9
        s = min(sx, sy); return [n['x'] + dx * s, n['y'] + dy * s]

    def head(x, y, ang, color):
        a, L = math.pi / 7, 11
        p1 = (x - L * math.cos(ang - a), y - L * math.sin(ang - a)); p2 = (x - L * math.cos(ang + a), y - L * math.sin(ang + a))
        return f'<path d="M{f1(x)} {f1(y)} L{f1(p1[0])} {f1(p1[1])} L{f1(p2[0])} {f1(p2[1])} Z" fill="{color}"/>'

    for e in spec.get('edges', []):
        a, b = nodes[e['from']], nodes[e['to']]
        side = e.get('kind') == 'side'
        color, sw = ('#8a97a6', 1.8) if side else (INK, 2.4)
        dash = ' stroke-dasharray="7 5"' if e.get('kind') in ('dashed', 'side-dashed') else ''
        via = [[px(c), py(r)] for c, r in e.get('via', [])]
        first = via[0] if via else [b['x'], b['y']]
        pts = [anchor(a, *first)] + via
        pts.append(anchor(b, *pts[-1]))
        if e.get('curve') and len(pts) == 2:
            p, q = pts; mx = (p[0] + q[0]) / 2 + (q[1] - p[1]) * 0.25; my = (p[1] + q[1]) / 2 - (q[0] - p[0]) * 0.25
            d = f'M{f1(p[0])} {f1(p[1])} Q{f1(mx)} {f1(my)} {f1(q[0])} {f1(q[1])}'
        else:
            d = 'M' + ' L'.join(f'{f1(p[0])} {f1(p[1])}' for p in pts)
        out += f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{dash}/>'
        pe, pp = pts[-1], pts[-2]; out += head(pe[0], pe[1], math.atan2(pe[1] - pp[1], pe[0] - pp[0]), color)
        if e.get('kind') == 'both':
            p0, p1_ = pts[0], pts[1]; out += head(p0[0], p0[1], math.atan2(p0[1] - p1_[1], p0[0] - p1_[0]), color)
        if e.get('label'):
            t = 0.5 if e.get('labelPos') is None else e['labelPos']
            Ls = [math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]) for i in range(1, len(pts))]
            s = t * sum(Ls); i = 0
            while i < len(Ls) - 1 and s > Ls[i]: s -= Ls[i]; i += 1
            f = s / Ls[i] if Ls[i] else 0
            x = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * f; y = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f
            ang = math.atan2(pts[i + 1][1] - pts[i][1], pts[i + 1][0] - pts[i][0]); horiz = abs(math.cos(ang)) > 0.7
            lines = str(e['label']).split('\n'); lw = max(len(l) for l in lines) * EFS * 0.56 + 10; lh = len(lines) * (EFS + 2)
            lx, ly = x, y
            if horiz: ly += (lh / 2 + 8) if e.get('labelSide') == 'below' else -(lh / 2 + 6)
            else: lx += -(lw / 2 + 6) if e.get('labelSide') == 'below' else (lw / 2 + 6)
            labels += f'<rect x="{f1(lx-lw/2)}" y="{f1(ly-lh/2-2)}" width="{f1(lw)}" height="{f1(lh+4)}" rx="6" fill="#ffffff" fill-opacity="0.92"/>'
            for j, l in enumerate(lines):
                labels += (f'<text x="{f1(lx)}" y="{f1(ly-lh/2+EFS+j*(EFS+2)-2)}" text-anchor="middle" font-size="{EFS}" font-weight="700" font-style="italic" '
                           f'fill="{"#6b7a85" if side else "#3b5f7a"}" font-family="{FONT}">{esc(l)}</text>')
    for n in spec['nodes']:
        k = n['k']
        if k['fill'] != 'none':
            out += (f'<rect x="{f1(n["x"]-n["w"]/2)}" y="{f1(n["y"]-n["h"]/2)}" width="{f1(n["w"])}" height="{f1(n["h"])}" '
                    f'rx="{n["h"]/2 if n.get("kind") == "energy" else 10}" fill="{k["fill"]}" stroke="{k["stroke"]}" stroke-width="2"/>')
        for j, l in enumerate(n['lines']):
            y = n['y'] - (len(n['lines']) - 1) * (FS + 4) / 2 + j * (FS + 4) + FS * 0.36
            it = ' font-style="italic"' if k.get('italic') else ''
            out += f'<text x="{f1(n["x"])}" y="{f1(y)}" text-anchor="middle" font-size="{FS}" font-weight="{k["bold"]}"{it} fill="{k["text"]}" font-family="{FONT}">{esc(l)}</text>'
    out += labels
    if spec.get('title'):
        out = f'<text x="{PAD+4}" y="{PAD+18}" font-size="{FS+2}" font-weight="800" fill="{INK}" font-family="{FONT}">{esc(spec["title"])}</text>' + out
    alt = esc(spec.get('alt') or spec.get('title') or 'pathway diagram')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="max-width:100%;height:auto;display:block;margin:0 auto" '
            f'role="img" aria-label="{alt}"><title>{alt}</title><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="#ffffff" stroke="#e2dccd" stroke-width="2" stroke-dasharray="6 4"/>{out}</svg>')


if __name__ == '__main__':
    sys.stdout.write(render(json.load(open(sys.argv[1]))))
