#!/usr/bin/env python3
"""House-style structure SVGs from SMILES (Python stand-in for the draw.js engine; no node needed).

RDKit is used only for 2D coordinates. Output matches the existing fig-p*.svg files: ink #2d3f4b lines 2.4 px,
O red #c0392b, N blue #2f5fc4, 19 px bold Inter labels with a separate white halo copy underneath (Prince ignores
paint-order, ledger R01), bond length 36.

Usage (in a venv with rdkit):
    from rdsvg import Scene
    s = Scene(); s.mol('CCO', name='ethanol'); s.arrow('enzyme'); s.mol('CC=O'); s.svg('alt text')
"""
import math, re
from rdkit import Chem
from rdkit.Chem import AllChem, rdDepictor

INK = '#2d3f4b'; BLUE = '#2f5fc4'; RED = '#c0392b'; GREEN = '#2e7d4f'; GREY = '#6b7a85'
FONT = 'Inter,Helvetica,Arial,sans-serif'
COL = {'O': RED, 'N': BLUE, 'S': '#b7950b', 'P': '#c46a1b', 'Cl': GREEN, 'Br': '#8e3b2f'}
L = 36.0
rdDepictor.SetPreferCoordGen(True)


def _fmt(lab):
    """Subscript digits, superscript + and −."""
    out = ''
    for ch in lab:
        if ch.isdigit():
            out += f'<tspan font-size="13" dy="4">{ch}</tspan><tspan dy="-4"></tspan>'
        elif ch in '+−':
            out += f'<tspan font-size="14" dy="-8">{ch}</tspan><tspan dy="8"></tspan>'
        else:
            out += ch
    return out


def text(x, y, s, col=INK, size=19, weight=800, anchor='middle', halo=True, fmt=True):
    at = f'x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" font-family="{FONT}"'
    t = _fmt(s) if fmt else s
    h = f'<text {at} fill="#fff" stroke="#fff" stroke-width="5" stroke-linejoin="round" aria-hidden="true">{t}</text>' if halo else ''
    return h + f'<text {at} fill="{col}">{t}</text>'


def line(x1, y1, x2, y2, w=2.4, col=INK, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"{d}/>'


class Mol:
    """One structure: elements in local coords (y down) + bbox."""

    def __init__(self, smiles, rotate=0.0, flip=False, labels=None, coords=None, show_c=(), coordgen=True, level=None):
        m = Chem.MolFromSmiles(smiles)
        assert m is not None, smiles
        self.m = m
        if coords:
            conf = Chem.Conformer(m.GetNumAtoms())
            for i, (x, y) in enumerate(coords):
                conf.SetAtomPosition(i, (x, y, 0))
            m.AddConformer(conf)
        else:
            rdDepictor.SetPreferCoordGen(coordgen)
            rdDepictor.Compute2DCoords(m)
            rdDepictor.SetPreferCoordGen(True)
        c = m.GetConformer()
        # scale to bond length L
        bl = [ (c.GetAtomPosition(b.GetBeginAtomIdx()) - c.GetAtomPosition(b.GetEndAtomIdx())).Length() for b in m.GetBonds()]
        sc = L / (sum(bl) / len(bl)) if bl else 1
        a = math.radians(rotate)
        self.p = []
        for i in range(m.GetNumAtoms()):
            q = c.GetAtomPosition(i)
            x, y = q.x * sc, q.y * sc
            x, y = x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a)
            if flip: x = -x
            self.p.append((x, -y))
        if level:
            (x1, y1), (x2, y2) = self.p[level[0]], self.p[level[1]]
            ang = -math.atan2(y2 - y1, x2 - x1)
            self.p = [(x * math.cos(ang) - y * math.sin(ang), x * math.sin(ang) + y * math.cos(ang)) for x, y in self.p]
        self.labels = labels or {}
        self.show_c = set(show_c)
        self._build()

    def _label(self, at):
        i = at.GetIdx()
        if i in self.labels: return self.labels[i]
        sym = at.GetSymbol(); h = at.GetTotalNumHs(); ch = at.GetFormalCharge()
        if sym == 'C' and i not in self.show_c and ch == 0: return None
        hs = '' if h == 0 else ('H' if h == 1 else f'H{h}')
        chs = '' if ch == 0 else ('+' if ch > 0 else '−')
        # put H on the side away from the bonds
        nb = [self.p[n.GetIdx()] for n in at.GetNeighbors()]
        x, y = self.p[i]
        left = bool(nb) and sum(n[0] for n in nb) / len(nb) > x + 1 and hs
        return (hs + sym + chs) if left else (sym + hs + chs)

    def _build(self):
        m, P = self.m, self.p
        self.lab = {at.GetIdx(): self._label(at) for at in m.GetAtoms()}
        ring = m.GetRingInfo()
        els = []
        for b in m.GetBonds():
            i, j = b.GetBeginAtomIdx(), b.GetEndAtomIdx()
            (x1, y1), (x2, y2) = P[i], P[j]
            dx, dy = x2 - x1, y2 - y1; Lb = math.hypot(dx, dy); ux, uy = dx / Lb, dy / Lb
            s1 = 12 if self.lab[i] else 0; s2 = 12 if self.lab[j] else 0
            ax, ay, bx, by = x1 + ux * s1, y1 + uy * s1, x2 - ux * s2, y2 - uy * s2
            order = 1.5 if b.GetIsAromatic() else b.GetBondTypeAsDouble()
            nx, ny = -uy, ux
            if order == 1:
                els.append(line(ax, ay, bx, by))
                continue
            # side for the second line: ring centre if in a ring, else toward the side with more neighbours
            rings = [r for r in ring.BondRings() if b.GetIdx() in r]
            if rings:
                atoms = set()
                for bi in rings[0]:
                    bb = m.GetBondWithIdx(bi); atoms |= {bb.GetBeginAtomIdx(), bb.GetEndAtomIdx()}
                cx = sum(P[k][0] for k in atoms) / len(atoms); cy = sum(P[k][1] for k in atoms) / len(atoms)
                if (cx - (x1 + x2) / 2) * nx + (cy - (y1 + y2) / 2) * ny < 0: nx, ny = -nx, -ny
                off, sh = 5.5, 0.14 * Lb
                els.append(line(ax, ay, bx, by))
                els.append(line(x1 + ux * (s1 + sh) + nx * off, y1 + uy * (s1 + sh) + ny * off,
                                x2 - ux * (s2 + sh) + nx * off, y2 - uy * (s2 + sh) + ny * off))
            elif order == 3:
                els.append(line(ax, ay, bx, by))
                for sgn in (1, -1):
                    els.append(line(ax + nx * 5 * sgn, ay + ny * 5 * sgn, bx + nx * 5 * sgn, by + ny * 5 * sgn))
            else:
                terminal = (self.lab[i] and m.GetAtomWithIdx(i).GetDegree() == 1) or (self.lab[j] and m.GetAtomWithIdx(j).GetDegree() == 1)
                if terminal:  # C=O style: centred pair
                    for sgn in (1, -1):
                        els.append(line(ax + nx * 3 * sgn, ay + ny * 3 * sgn, bx + nx * 3 * sgn, by + ny * 3 * sgn))
                else:
                    nbs = [P[n.GetIdx()] for k in (i, j) for n in m.GetAtomWithIdx(k).GetNeighbors() if n.GetIdx() not in (i, j)]
                    if nbs:
                        cx = sum(q[0] for q in nbs) / len(nbs); cy = sum(q[1] for q in nbs) / len(nbs)
                        if (cx - (x1 + x2) / 2) * nx + (cy - (y1 + y2) / 2) * ny < 0: nx, ny = -nx, -ny
                    off, sh = 5.5, 0.14 * Lb
                    els.append(line(ax, ay, bx, by))
                    els.append(line(x1 + ux * (s1 + sh) + nx * off, y1 + uy * (s1 + sh) + ny * off,
                                    x2 - ux * (s2 + sh) + nx * off, y2 - uy * (s2 + sh) + ny * off))
        for i, lab in self.lab.items():
            if not lab: continue
            sym = self.m.GetAtomWithIdx(i).GetSymbol()
            x, y = P[i]
            # anchor the heavy atom letter on the vertex: shift text so the element sits on the atom
            w = 12.5  # approx width of one bold glyph at 19px
            hl = lab.index(sym) if sym in lab else 0
            core = len(re.sub(r'\d', '', lab.replace('−', '').replace('+', '')))
            shift = (core / 2 - hl - 0.5) * w * 0.92
            els.append(text(x + shift, y + 6.5, lab, COL.get(sym, INK)))
        self.els = els
        xs = [q[0] for q in P]; ys = [q[1] for q in P]
        self.box = [min(xs) - 14, min(ys) - 20, max(xs) + 14, max(ys) + 20]
        for i, lab in self.lab.items():
            if lab:
                hw = len(re.sub(r'[\d+−]', '', lab)) * 7 + 6
                self.box[0] = min(self.box[0], P[i][0] - hw - 4); self.box[2] = max(self.box[2], P[i][0] + hw + 4)

    def shifted(self, dx, dy):
        out = []
        for e in self.els:
            out.append(re.sub(r'\b(x1|x2|x)="(-?[\d.]+)"', lambda m: f'{m.group(1)}="{float(m.group(2)) + dx:.1f}"',
                       re.sub(r'\b(y1|y2|y)="(-?[\d.]+)"', lambda m: f'{m.group(1)}="{float(m.group(2)) + dy:.1f}"', e)))
        return out


class Scene:
    """Left-to-right layout of molecules, plus signs, arrows and captions under each item."""

    def __init__(self, gap=18):
        self.items = []; self.gap = gap; self.extra = []

    def mol(self, smiles, name=None, **kw):
        m = Mol(smiles, **kw); self.items.append(('mol', m, name)); return m

    def plus(self, s='+'):
        self.items.append(('txt', s, None))

    def poly(self, smiles, name=None, **kw):
        m = Polymer(smiles, **kw); self.items.append(('mol', m, name)); return m

    def word(self, s, w=None):
        """Free text in the row, e.g. a coefficient 'n' or '2n H2O' (digits after a letter are subscripted)."""
        self.items.append(('word', (s, w), None))

    def arrow(self, above='', below='', w=110, kind='->'):
        self.items.append(('arrow', (above, below, w, kind), None))

    def svg(self, alt, pad=14, scale=0.85):
        els, (x0, top, w, h) = self.layout(pad)
        alt = alt.replace('"', '&quot;')
        return (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg data-printfix="1" xmlns="http://www.w3.org/2000/svg" class="mol" '
                f'viewBox="{x0:.0f} {top:.0f} {w:.0f} {h:.0f}" width="{w*scale:.0f}" height="{h*scale:.0f}" role="img" aria-label="{alt}">'
                + ''.join(els) + '</svg>\n')

    def layout(self, pad=14):
        x = 0; els = []; boxes = []
        hmax = max([(it[1].box[3] - it[1].box[1]) for it in self.items if it[0] == 'mol'] + [40])
        for kind, obj, name in self.items:
            if kind == 'mol':
                b = obj.box; dx = x - b[0]; dy = -(b[1] + b[3]) / 2
                els += obj.shifted(dx, dy)
                boxes.append((x, b[1] + dy, x + b[2] - b[0], b[3] + dy))
                if name:
                    els.append(text(x + (b[2] - b[0]) / 2, b[3] + dy + 20, name, INK, 15, 600, halo=False, fmt=False))
                x += b[2] - b[0] + self.gap
            elif kind == 'txt':
                els.append(text(x + 10, 8, obj, INK, 24, 700, halo=False, fmt=False)); x += 20 + self.gap
            elif kind == 'word':
                s_, w_ = obj
                t_ = re.sub(r'(?<=[A-Za-z)])(\d)', r'<tspan font-size="13" dy="4">\1</tspan><tspan dy="-4"></tspan>', s_)
                t_ = re.sub(r'\bn\b', '<tspan font-style="italic">n</tspan>', t_)
                els.append(f'<text x="{x:.1f}" y="7" font-size="19" font-weight="700" font-family="{FONT}" fill="{INK}">{t_}</text>')
                x += (w_ or 12 * len(s_)) + self.gap * 0.5
            else:
                above, below, w, k = obj
                els.append(line(x, 0, x + w, 0, 2.2))
                if k == '<=>':
                    els[-1] = line(x, -4, x + w, -4, 2.2) + line(x + w, -4, x + w - 10, -11, 2.2) + line(x, 4, x + w, 4, 2.2) + line(x, 4, x + 10, 11, 2.2)
                else:
                    els.append(line(x + w, 0, x + w - 11, -7, 2.2) + line(x + w, 0, x + w - 11, 7, 2.2))
                if above: els.append(text(x + w / 2, -12, above, INK, 14, 600, halo=False, fmt=False))
                if below: els.append(text(x + w / 2, 24, below, INK, 14, 600, halo=False, fmt=False))
                x += w + self.gap
        els += self.extra
        top = min([bx[1] for bx in boxes] + [-30]) - pad
        bot = max([bx[3] for bx in boxes] + [30]) + pad + (28 if any(n for _, _, n in self.items) else 0)
        x0, w, h = -pad, x - self.gap + 2 * pad, bot - top
        return els, (x0, top, w, h)


def vstack(scenes, alt, indent=(), scale=0.85, vgap=6):
    """Stack Scene rows vertically; indent[i] shifts row i right (px)."""
    allels = []; y = 0.0; wmax = 0.0
    for k, sc in enumerate(scenes):
        els, (x0, top, w, h) = sc.layout()
        dx = (indent[k] if k < len(indent) else 0) - x0; dy = y - top
        for e in els:
            allels.append(re.sub(r'\b(x1|x2|x)="(-?[\d.]+)"', lambda m: f'{m.group(1)}="{float(m.group(2)) + dx:.1f}"',
                          re.sub(r'\b(y1|y2|y)="(-?[\d.]+)"', lambda m: f'{m.group(1)}="{float(m.group(2)) + dy:.1f}"', e)))
        y += h + vgap; wmax = max(wmax, w + dx + x0)
    alt = alt.replace('"', '&quot;')
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg data-printfix="1" xmlns="http://www.w3.org/2000/svg" class="mol" '
            f'viewBox="0 0 {wmax:.0f} {y:.0f}" width="{wmax*scale:.0f}" height="{y*scale:.0f}" role="img" aria-label="{alt}">'
            + ''.join(allels) + '</svg>\n')


# ---------- repeat-unit brackets ----------
def brackets(mol, n_label='n'):
    """Draw polymer brackets across the bonds to the two dummy atoms ([*]) of a Mol; returns extra elements."""
    els = []
    dums = [a for a in mol.m.GetAtoms() if a.GetAtomicNum() == 0]
    for k, d in enumerate(sorted(dums, key=lambda a: mol.p[a.GetIdx()][0])):
        nb = d.GetNeighbors()[0]
        (x1, y1), (x2, y2) = mol.p[nb.GetIdx()], mol.p[d.GetIdx()]
        mx, my = x1 + (x2 - x1) * 0.62, y1 + (y2 - y1) * 0.62
        dx, dy = x2 - x1, y2 - y1; Lb = math.hypot(dx, dy); ux, uy = dx / Lb, dy / Lb; nx, ny = -uy, ux
        h = 24
        ax, ay, bx, by = mx + nx * h, my + ny * h, mx - nx * h, my - ny * h
        els.append(line(ax, ay, bx, by, 2.2))
        els.append(line(ax, ay, ax - ux * 7, ay - uy * 7, 2.2) + line(bx, by, bx - ux * 7, by - uy * 7, 2.2))
        if k == 1:
            lx, ly = max(ax, bx), max(ay, by)
            els.append(text(lx + 5, ly + 10, n_label, INK, 16, 700, anchor='start', halo=False, fmt=False).replace('font-weight="700"', 'font-weight="700" font-style="italic"'))
    return els


def _blank_dummies(mol):
    """Remove the '*' labels drawn for dummy atoms and let bonds run to the dummy position."""
    for a in mol.m.GetAtoms():
        if a.GetAtomicNum() == 0:
            mol.labels[a.GetIdx()] = ''
    mol._build()
    return mol


class Polymer(Mol):
    def __init__(self, smiles, **kw):
        super().__init__(smiles, **kw)
        d = [a.GetIdx() for a in self.m.GetAtoms() if a.GetAtomicNum() == 0]
        (x1, y1), (x2, y2) = self.p[d[0]], self.p[d[1]]
        if x2 < x1: (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
        ang = -math.atan2(y2 - y1, x2 - x1)
        self.p = [(x * math.cos(ang) - y * math.sin(ang), x * math.sin(ang) + y * math.cos(ang)) for x, y in self.p]
        _blank_dummies(self)
        self.els += brackets(self)


# ---------- condensed formulas drawn as text (Ball-style exercise drawings) ----------
try:
    from PIL import ImageFont
    _F = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 40)
except Exception:  # pragma: no cover
    _F = None
CFONT = 'Arial,Helvetica,sans-serif'


def _w(s, size):
    """Width of a condensed-formula string with subscripted digits, in px at font-size `size`."""
    w = 0.0
    for ch in s:
        f = 0.72 if ch.isdigit() else 1.0
        w += _F.getlength(ch) / 40 * size * f
    return w


def _ctext(x, y, s, size, anchor='start', col=INK):
    t = ''.join(f'<tspan font-size="{size*0.72:.0f}" dy="{size*0.25:.0f}">{c}</tspan><tspan dy="-{size*0.25:.0f}"></tspan>' if c.isdigit() else c for c in s)
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-family="{CFONT}" fill="{col}">{t}</text>'


def condensed(groups, branches=None, size=20, alt=''):
    """groups: list of strings written left to right, e.g. ['CH3','CH2','C','CH2','CH3'].
    branches: {group index: (above or None, below or None)}; a vertical bond is drawn from the first
    letter of that group (the carbon)."""
    branches = branches or {}
    x = 0.0; els = []; cx = {}
    for i, g in enumerate(groups):
        cx[i] = x + _w(g[0], size) / 2
        els.append(_ctext(x, 0, g, size)); x += _w(g, size)
    top, bot = -size - 4, 8
    for i, (ab, be) in branches.items():
        if ab:
            els.append(line(cx[i], -size * 0.85, cx[i], -size * 0.85 - 18, 1.6))
            els.append(_ctext(cx[i] - _w(ab[0], size) / 2, -size * 0.85 - 24, ab, size)); top = min(top, -size * 0.85 - 24 - size)
        if be:
            els.append(line(cx[i], size * 0.3, cx[i], size * 0.3 + 18, 1.6))
            els.append(_ctext(cx[i] - _w(be[0], size) / 2, size * 0.3 + 18 + size, be, size)); bot = max(bot, size * 0.3 + 18 + size + 8)
    pad = 10; x0, y0, w, h = -pad, top - pad, x + 2 * pad, bot - top + 2 * pad
    alt = alt.replace('"', '&quot;')
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {w:.0f} {h:.0f}" '
            f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{alt}">' + ''.join(els) + '</svg>\n')


def equation(parts, size=20, alt=''):
    """One-line text equation. parts: list of (text, label-under or None); use '->' for an arrow."""
    x = 0.0; els = []
    for s, lab in parts:
        if s == '->':
            els.append(line(x + 6, -7, x + 60, -7, 1.8) + line(x + 60, -7, x + 51, -12, 1.8) + line(x + 60, -7, x + 51, -2, 1.8)); x += 70; continue
        w = _w(s.replace('+', '').replace('−', ''), size) + (8 if ('+' in s or '−' in s) else 0)
        t = ''
        for c in s:
            if c.isdigit(): t += f'<tspan font-size="{size*0.72:.0f}" dy="{size*0.25:.0f}">{c}</tspan><tspan dy="-{size*0.25:.0f}"></tspan>'
            elif c in '+−' and s.strip() not in ('+',): t += f'<tspan font-size="{size*0.8:.0f}" dy="-{size*0.55:.0f}">{c}</tspan><tspan dy="{size*0.55:.0f}"></tspan>'
            else: t += c
        if s.strip() == '+':
            t = '+'; w = _w('+', size)
        els.append(f'<text x="{x:.1f}" y="0" font-size="{size}" font-family="{CFONT}" fill="{INK}">{t}</text>')
        if lab:
            for k, ln in enumerate(lab.split('\n')):
                els.append(f'<text x="{x + w / 2:.1f}" y="{36 + k * 19:.1f}" text-anchor="middle" font-size="15" font-family="{CFONT}" fill="{INK}">{ln}</text>')
        x += w + 12
    pad = 10
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-size - pad} {x + 2 * pad:.0f} {size + 70:.0f}" '
            f'width="{x + 2 * pad:.0f}" height="{size + 70:.0f}" role="img" aria-label="{alt}">' + ''.join(els) + '</svg>\n')


def grid(rows, alt, gap=36, scale=0.85, label_size=15):
    """rows: list of rows; each row a list of (Mol, label). Labels sit under each structure."""
    els = []; y = 0.0; wmax = 0.0
    for row in rows:
        hrow = max(m.box[3] - m.box[1] for m, _ in row)
        x = 0.0
        for m, lab in row:
            b = m.box; dx = x - b[0]; dy = y + hrow / 2 - (b[1] + b[3]) / 2
            els += m.shifted(dx, dy)
            if lab:
                els.append(text(x + (b[2] - b[0]) / 2, y + hrow + 22, lab, INK, label_size, 600, halo=False, fmt=False))
            x += b[2] - b[0] + gap
        wmax = max(wmax, x - gap); y += hrow + 34 + gap * 0.5
    pad = 12; h = y - gap * 0.5 + pad
    alt = alt.replace('"', '&quot;')
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg data-printfix="1" xmlns="http://www.w3.org/2000/svg" class="mol" '
            f'viewBox="{-pad} {-pad} {wmax + 2 * pad:.0f} {h + pad:.0f}" width="{(wmax + 2 * pad) * scale:.0f}" height="{(h + pad) * scale:.0f}" role="img" aria-label="{alt}">'
            + ''.join(els) + '</svg>\n')
