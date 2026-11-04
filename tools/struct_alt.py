"""Write alt text for the Try It bank's drawn structures and figures from their data.
Describes what is drawn (atoms, bonds, rings, positions, cis/trans layout) without naming the answer.
Used by tools/adapt_more.py."""
import re, math, html
import networkx as nx

HAL = {'F': 'F', 'Cl': 'Cl', 'Br': 'Br', 'I': 'I'}
SUBS = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
NUMW = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
RINGW = {3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight'}

def plain(s):
    return re.sub(r'<[^>]+>', '', html.unescape(str(s)))

def parse_label(lab):
    """element counts in a label like OH, NH2, CH3(CH2)7, (CH2)7COOH, Na."""
    lab = plain(lab).replace('​', '')
    def p(s):
        cnt = {}; i = 0
        while i < len(s):
            if s[i] == '(':
                depth = 1; j = i + 1
                while depth:
                    depth += {'(': 1, ')': -1}.get(s[j], 0); j += 1
                inner = p(s[i + 1:j - 1]); m = re.match(r'\d+', s[j:]); k = int(m.group()) if m else 1
                for e, n in inner.items(): cnt[e] = cnt.get(e, 0) + n * k
                i = j + (len(m.group()) if m else 0); continue
            m = re.match(r'([A-Z][a-z]?)(\d*)', s[i:])
            if not m: i += 1; continue
            cnt[m.group(1)] = cnt.get(m.group(1), 0) + int(m.group(2) or 1); i += len(m.group())
        return cnt
    return p(lab)

class Mol:
    def __init__(self, m):
        self.skel = bool(m.get('skel'))
        self.atoms = [{'lab': a[0], 'x': a[1], 'y': a[2], 'lp': a[3] if len(a) > 3 else 0, 'ch': a[4] if len(a) > 4 else 0} for a in m['a']]
        self.G = nx.Graph()
        for i, a in enumerate(self.atoms):
            cnt = parse_label(a['lab']) or {'C': 1}
            heavy = [e for e in cnt if e != 'H']
            a['cnt'] = cnt
            a['el'] = 'C' if (a['lab'] in ('C', '') or a['lab'].startswith('C​')) else (heavy[0] if len(heavy) == 1 and cnt[heavy[0]] == 1 else 'X')
            if a['lab'].startswith('CH') and len(heavy) == 1: a['el'] = 'C'
            if not heavy and cnt.get('H') == 1: a['el'] = 'H'
            a['tag'] = m['a'][i][5] if len(m['a'][i]) > 5 and m['a'][i][5] else ''
            self.G.add_node(i)
        self.dotted = []; self.reported = set()
        for b in m['b']:
            o = b[2] if len(b) > 2 else 1
            w = o if o in (4, 5) else 0
            o = 1 if o in (4, 5) else o
            if o == 0: self.dotted.append((b[0], b[1])); continue
            self.G.add_edge(b[0], b[1], o=o, w=w, start=b[0])
        for i, a in enumerate(self.atoms):
            if a['el'] == 'C' and a['lab'] == 'C':
                val = sum(self.G[i][j]['o'] for j in self.G[i])
                a['H'] = max(0, 4 - val - abs(a['ch'])) if self.skel else 0
            else:
                a['H'] = a['cnt'].get('H', 0)

    def formula(self):
        cnt = {}
        for a in self.atoms:
            for e, n in a['cnt'].items():
                if e == 'H': continue
                cnt[e] = cnt.get(e, 0) + n
            if a['lab'] == 'C': cnt['H'] = cnt.get('H', 0) + a['H']
            else: cnt['H'] = cnt.get('H', 0) + a['cnt'].get('H', 0)
        order = (['C', 'H'] if 'C' in cnt else []) + sorted(e for e in cnt if e not in ('C', 'H')) + (['H'] if 'C' not in cnt and 'H' in cnt else [])
        f = ''.join(e + (str(cnt[e]) if cnt[e] > 1 else '') for e in order if cnt.get(e))
        q = sum(a['ch'] for a in self.atoms)
        return f + ('' if not q else ('+' if q == 1 else '−' if q == -1 else f'{abs(q)}{"+" if q > 0 else "−"}'))

def side(p, a, b):
    return (b['x'] - a['x']) * (p['y'] - a['y']) - (b['y'] - a['y']) * (p['x'] - a['x'])

SUPC = {1: '⁺', -1: '⁻', 2: '²⁺', -2: '²⁻'}
NORM = {'HO': 'OH', 'H2N': 'NH2', 'HS': 'SH', 'HN': 'NH', 'H3N': 'NH3', 'HOOC': 'COOH', 'OHC': 'CHO', 'H3C': 'CH3', 'H2C': 'CH2', 'HC': 'CH'}

def hcount(M, i):
    return M.atoms[i]['H'] + sum(1 for k in M.G[i] if M.atoms[k]['el'] == 'H')

def atom_text(M, i):
    a = M.atoms[i]; lab = plain(a['lab']).replace('​', '')
    if a['el'] == 'C' and lab in ('C', ''):
        n = hcount(M, i); t = 'C' + ('H' + (str(n) if n > 1 else '') if n else '')
    else:
        t = NORM.get(lab, lab)
        n = sum(1 for k in M.G[i] if M.atoms[k]['el'] == 'H')
        if n and t in ('O', 'N', 'S', 'C'): t += 'H' + (str(n) if n > 1 else '')
    if a['ch'] and not re.search(r'[+−-]$', t): t += SUPC.get(a['ch'], '')
    return t.translate(SUBS)

def bsym(M, i, k):
    o = M.G[i][k]['o']; return '=' if o == 2 else '≡' if o == 3 else ''

def heavy_nb(M, i, excl):
    return [k for k in M.G[i] if k not in excl and M.atoms[k]['el'] != 'H']

def depth(M, i, parent, ban):
    best = 0
    for k in heavy_nb(M, i, {parent} | ban):
        best = max(best, 1 + depth(M, k, i, ban | {i}))
    return best

def cond(M, i, parent, ban, ringname=None, end=None):
    """condensed formula of the fragment reached at atom i (coming from parent), never entering `ban`.
    Ring atoms met on the way are written as their ring name (ringname[atom])."""
    ringname = ringname or {}
    out = []; prev = parent; cur = i; seen = set(ban) | ({parent} if parent is not None else set())
    while cur is not None:
        seen.add(cur)
        if cur in ringname and cur != i:
            out.append(f'({ringname[cur]})'); break
        nb = [k for k in heavy_nb(M, cur, seen) if k not in seen]
        if end is not None and end in nb: main = end
        else:
            cand = [k for k in nb if k not in ringname]
            main = max(cand, key=lambda k: (depth(M, k, cur, seen | set(ringname)), M.atoms[k]['el'] == 'C'), default=None) if cand else (nb[0] if nb else None)
            if cand and len(cand) == len(nb) and len(cand) > 1 and all(not heavy_nb(M, k, {cur}) for k in cand) and M.atoms[cur]['el'] == 'C':
                lt0 = sorted(('=' if M.G[cur][k]['o'] == 2 else '') + atom_text(M, k) for k in cand)
                if lt0 in (['=O', 'OH'], ['=O', 'O⁻'], ['=O', 'NH₂']): main = None
                else: main = next((k for k in cand if M.atoms[k]['el'] == 'C' and M.G[cur][k]['o'] == 1), main)
        leaves = [k for k in nb if k != main and not heavy_nb(M, k, {cur}) and k not in ringname]
        others = [k for k in nb if k != main and k not in leaves]
        t = atom_text(M, cur)
        lt = [('=' if M.G[cur][k]['o'] == 2 else '≡' if M.G[cur][k]['o'] == 3 else '') + atom_text(M, k) for k in leaves]
        if main is None and M.atoms[cur]['el'] == 'C':
            # end groups written the usual way
            st = sorted(lt)
            if st == ['=O', 'OH'] and t == 'C': t, lt = 'COOH', []
            elif st == ['=O', 'O⁻'] and t == 'C': t, lt = 'COO⁻', []
            elif st == ['=O'] and t == 'CH': t, lt = 'CHO', []
            elif st == ['=O', 'NH₂'] and t == 'C': t, lt = 'CONH₂', []
        grp = {}
        for x in lt: grp[x] = grp.get(x, 0) + 1
        br = ''.join(f'({x})' + (str(n).translate(SUBS) if n > 1 else '') for x, n in grp.items())
        br += ''.join('(' + (ringname[k] if k in ringname else bsym(M, cur, k) + cond(M, k, cur, seen | {cur}, ringname)) + ')' for k in others)
        out.append(t + br)
        if main is None: break
        out.append(bsym(M, cur, main))
        prev, cur = cur, main
    s = ''.join(out)
    # (CH2)n for long runs
    s = re.sub(r'\(CH₃\)CH₃(?=$|\))', '(CH₃)₂', s)
    return re.sub(r'(?:CH₂){4,}', lambda m: f'(CH₂){str(len(m.group()) // 3).translate(SUBS)}', s)

def compass(dx, dy):
    ang = math.degrees(math.atan2(-dy, dx)) % 360   # screen y points down
    return ['right side', 'upper right', 'top', 'upper left', 'left side', 'lower left', 'bottom', 'lower right'][int(((ang + 22.5) % 360) // 45)]

def tag_notes(M):
    return [f'{atom_desc(M, i, None) if a["el"] == "C" else "the " + atom_text(M, i)} is marked with the label "{plain(a["tag"])}"' for i, a in enumerate(M.atoms) if a.get('tag')]

def extra_stereo(M):
    A = M.atoms; G = M.G; ringat = {i for c in nx.cycle_basis(G) for i in c}; notes = []
    for a, b, d in G.edges(data=True):
        if not d.get('w') or frozenset((a, b)) in M.reported: continue
        c = d['start']; k = b if c == a else a
        if A[k]['el'] == 'H': grp = 'H'
        else:
            grp = cond(M, k, c, set())
            if len(grp) > 12: grp = atom_text(M, k)
        nbt = []
        for nb in G[c]:
            if nb == k or A[nb]['el'] == 'H': continue
            if nb in ringat: nbt.append('the ring'); continue
            t = cond(M, nb, c, set()); nbt.append(t if len(t) <= 12 else atom_text(M, nb))
        kind = 'a solid wedge (toward the viewer)' if d['w'] == 4 else 'a dashed wedge (away from the viewer)'
        nbt.sort(key=lambda t: t != 'the ring')
        notes.append(f'at the {atom_text(M, c)} bonded to ' + ' and '.join(nbt) + f', the {grp} is on {kind}, drawn toward the {compass(A[k]["x"] - A[c]["x"], A[k]["y"] - A[c]["y"])}'.replace('toward the right side', 'toward the right').replace('toward the left side', 'toward the left'))
    return notes

def wnote(M, i, k):
    w = M.G[i][k].get('w')
    if w: M.reported.add(frozenset((i, k)))
    return ' (on a solid wedge bond, pointing toward the viewer)' if w == 4 else ' (on a dashed wedge bond, pointing away from the viewer)' if w == 5 else ''

def group_name(M, root, start, ban):
    """name the substituent reached from ring/chain atom `root` through atom `start` (not crossing `ban`)."""
    sub = {start}; stack = [start]
    while stack:
        n = stack.pop()
        for k in M.G[n]:
            if k not in sub and k != root and k not in ban and M.atoms[k]['el'] != 'H':
                sub.add(k); stack.append(k)
    A = M.atoms; s = A[start]; o = M.G[root][start]['o']
    els = sorted(A[i]['el'] for i in sub)
    lab = plain(s['lab'])
    if len(sub) == 1:
        if s['el'] in HAL: return f'a {s["el"]} atom'
        if lab in ('OH', 'HO'): return 'an OH group'
        if lab in ('NH2', 'H2N'): return 'an NH₂ group'
        if lab in ('SH', 'HS'): return 'an SH group'
        if s['el'] == 'O' and o == 2: return 'a double-bonded O (C=O)'
        if s['el'] in ('S', 'N') and o == 2: return f'a double-bonded {atom_text(M, start)} (C={atom_text(M, start)})'
        if s['el'] == 'O' and s['ch'] == -1: return 'an O⁻'
        if s['el'] == 'C' and o == 1: return 'a methyl group (CH₃)'
        if s['el'] == 'C' and o == 2: return 'a double-bonded CH₂ (=CH₂)'
        return an(f'{atom_text(M, start)} group')
    if s['el'] == 'N' and els.count('O') == 2 and len(sub) == 3: return 'a nitro group (NO₂)'
    if all(A[i]['el'] == 'C' for i in sub):
        n = len(sub); maxdeg = max(len([k for k in M.G[i] if k in sub]) for i in sub)
        dbl = any(M.G[i][k]['o'] == 2 for i in sub for k in M.G[i] if k in sub)
        if n == 2: return 'a vinyl group (CH=CH₂)' if dbl else 'an ethyl group'
        if n == 3 and not dbl: return 'an isopropyl group (a CH bonded to two CH₃)' if len([k for k in M.G[start] if k in sub]) == 2 else 'a propyl chain (three carbons in a row)'
        if n == 4 and not dbl and len([k for k in M.G[start] if k in sub]) == 3: return 'a tert-butyl group (a C bonded to three CH₃)'
        if nx.cycle_basis(M.G.subgraph(sub)): return f'a ring of {n} carbons'
        return an(f'{n}-carbon side chain ({cond(M, start, root, ban)})')
    if s['el'] == 'C':
        nb = [k for k in M.G[start] if k in sub]
        dO = [k for k in nb if A[k]['el'] == 'O' and M.G[start][k]['o'] == 2]
        sO = [k for k in nb if A[k]['el'] == 'O' and M.G[start][k]['o'] == 1]
        if dO and sO and len(sub) == 3:
            k = sO[0]
            return 'a carboxyl group (COOH)' if A[k]['H'] or plain(A[k]['lab']) in ('OH', 'HO') else ('a carboxylate group (COO⁻)' if A[k]['ch'] == -1 else 'a COO group')
        if dO and len(sub) == 2: return 'a CHO group (C=O with an H)'
        if len(sub) == 2 and any(A[k]['el'] in HAL for k in nb): return f'a CH₂{A[[k for k in nb if A[k]["el"] in HAL][0]]["el"]} group'
        if len(sub) == 2 and sO: return 'a CH₂OH group'
    if s['el'] == 'O' and o == 1 and len(sub) == 2 and A[[k for k in sub if k != start][0]]['el'] == 'C': return 'a methoxy group (O–CH₃)'
    return an(f'{bsym(M, root, start)}{cond(M, start, root, ban)} group')

def an(t):
    """'a' or 'an' before a group written as letters (an OH, an NH₂, an 8-carbon, a CH₃)."""
    return ('an ' if re.match(r'(?:[AEFHILMNORSX](?![a-z])|[aeiou]|8|11|18)', t) else 'a ') + t

def atom_desc(M, i, comp_of):
    a = M.atoms[i]
    if a['el'] == 'H':
        nb = list(M.G[i])
        return f'the H on the {M.atoms[nb[0]]["el"]}' + (f' of molecule {comp_of[i]}' if comp_of else '') if nb else 'an H'
    if a['el'] == 'C':
        t = 'the C=O carbon' if any(M.atoms[k]['el'] == 'O' and M.G[i][k]['o'] == 2 for k in M.G[i]) else f'the {atom_text(M, i)} carbon'
    else: t = f'the {a["el"]}'
    return t + (f' of molecule {comp_of[i]}' if comp_of else '')

def describe_mol(m):
    if not isinstance(m, dict) or 'a' not in m: return ''
    M = Mol(m); A = M.atoms; G = M.G
    comps = sorted(nx.connected_components(G), key=min)
    if len(comps) > 1 and all(any(A[i]['el'] != 'H' for i in c) for c in comps):
        # several molecules in one drawing (often joined by dotted hydrogen bonds)
        comp_of = {i: n for n, c in enumerate(comps, 1) for i in c}
        parts = []
        for n, c in enumerate(comps, 1):
            idx = sorted(c); re_ = {o: k for k, o in enumerate(idx)}
            sub = {'skel': m.get('skel'), 'a': [m['a'][o] for o in idx],
                   'b': [[re_[b[0]], re_[b[1]]] + list(b[2:]) for b in m['b'] if b[0] in c and b[1] in c and (len(b) < 3 or b[2] != 0)]}
            parts.append(f'molecule {n}: ' + describe_mol(sub).rstrip('.'))
        for a, b in M.dotted:
            parts.append(f'a dotted line joins {atom_desc(M, a, comp_of)} to {atom_desc(M, b, comp_of)}')
        if m.get('cap'): parts.append(f'labeled "{plain(m["cap"])}"')
        return f'{NUMW.get(len(comps), len(comps)).capitalize()} molecules drawn together. ' + '; '.join(parts) + '.'
    form = M.formula().translate(SUBS)
    kind = 'Skeletal structure' if M.skel else 'Structure (all atoms shown)'
    heavy = [i for i in G if not (A[i]['el'] == 'H')]
    Hv = G.subgraph(heavy)
    if heavy and (len(heavy) <= 4 or not any(A[i]['el'] == 'C' for i in heavy)) and not nx.cycle_basis(Hv) and nx.is_connected(Hv):
        if len(heavy) == 1:
            i0 = heavy[0]; a = A[i0]; nH = hcount(M, i0)
            if a['el'] == 'O' and plain(a['lab']) in ('O', 'OH2', 'H2O'): txt = ('H' + (str(nH) if nH > 1 else '') if nH else '') + 'O' + SUPC.get(a['ch'], '')
            else: txt = atom_text(M, i0)
            txt = txt.translate(SUBS)
        else:
            ends = [i for i in heavy if Hv.degree(i) <= 1]
            a0 = max(ends, key=lambda e: (A[e]['el'] == 'C', -e))
            txt = cond(M, a0, None, set())
        lp = sum(a['lp'] for a in A)
        k2 = 'Structure with all atoms shown' if not M.skel else 'Structure'
        return f'{k2}: {txt}' + (f' ({lp} lone pair{"s" if lp != 1 else ""} drawn)' if lp else '') + '.'
    cyc = nx.cycle_basis(G)
    rings = []
    for c in cyc:
        dbl = sum(1 for i in range(len(c)) if G[c[i]][c[(i + 1) % len(c)]]['o'] == 2)
        het = [A[i]['el'] for i in c if A[i]['el'] != 'C']
        rings.append({'atoms': c, 'n': len(c), 'dbl': dbl, 'het': het, 'arom': len(c) == 6 and dbl == 3 and not het})
    out = [f'{kind}, {form}']
    if len(rings) == 1:
        r = rings[0]; ra = r['atoms']; n = r['n']
        desc = 'a benzene ring (six-membered ring with three alternating double bonds)' if r['arom'] else \
               f'a {RINGW.get(n, n)}-membered ring' + (ring_word(r)[len(f'a {RINGW.get(n, n)}-membered ring'):].split(' with ')[0] if r['het'] else ' of carbon atoms') + \
               (f' with {NUMW.get(r["dbl"], r["dbl"])} double bond{"s" if r["dbl"] > 1 else ""} in the ring' if r['dbl'] else ' with single bonds only')
        subs = []
        for pos, i in enumerate(ra):
            for k in G[i]:
                if k not in ra and A[k]['el'] != 'H':
                    wn = wnote(M, i, k)
                    if wn:
                        cx = sum(A[j]['x'] for j in ra) / n; cy = sum(A[j]['y'] for j in ra) / n
                        wn = f' drawn at the {compass(A[k]["x"] - cx, A[k]["y"] - cy)} of the ring' + wn
                    subs.append((pos, group_name(M, i, k, set(ra)) + wn))
        if subs:
            # number ring positions 1..n from the first substituent, choosing the direction with the lowest locants
            best = None
            hetpos = [p for p, i in enumerate(ra) if A[i]['el'] != 'C']
            for st in (hetpos or sorted({p for p, _ in subs})):
                for d in (1, -1):
                    loc = (sorted(((p - st) * d) % n + 1 for p in hetpos), sorted(((p - st) * d) % n + 1 for p, _ in subs))
                    if best is None or loc < best[0]: best = (loc, st, d)
            _, st, d = best
            items = sorted(((((p - st) * d) % n + 1), g) for p, g in subs)
            if hetpos:
                hl = sorted((((p - st) * d) % n + 1, A[ra[p]]['el']) for p in hetpos)
                hd = f'the {hl[0][1]} is ring position 1' if len(hl) == 1 else 'ring heteroatoms: ' + ', '.join(f'{e} at position {q}' for q, e in hl)
                desc += f' ({hd}), with ' + '; '.join(f'{g} at position {p}' for p, g in items)
            elif len(items) == 1:
                desc += f', with {items[0][1]} attached' + (' (that ring carbon is position 1)' if r['dbl'] and not r['arom'] else '')
            elif len(items) == 2 and n != 6 and items[0][0] == items[1][0]:
                desc += f', with {items[0][1]} and {items[1][1]} both on the same ring carbon'
            elif len(items) == 2 and n == 6 and not (r['dbl'] and not r['arom']):
                gap = items[1][0] - items[0][0]
                rel = {0: 'both on the same ring carbon', 1: 'on adjacent ring carbons', 2: 'separated by one ring carbon', 3: 'directly across the ring from each other'}[min(gap, 6 - gap)]
                same = items[0][1] == items[1][1]
                desc += f', with two {items[0][1].split(" ", 1)[1].replace("group", "groups").replace("atom", "atoms")} {rel}' if same else f', with {items[0][1]} and {items[1][1]} {rel}'
            else:
                desc += ', with substituents at ring positions ' + '; '.join(f'{p}: {g}' for p, g in items)
            if r['dbl'] and not r['arom'] and n in (5, 6, 7):
                dpos = sorted(sorted(((((ra.index(a) - st) * d) % n) + 1, (((ra.index(b) - st) * d) % n) + 1)) for a, b in G.subgraph(ra).edges if G[a][b]['o'] == 2)
                desc += '; ring double bond' + ('s' if len(dpos) > 1 else '') + ' between ring positions ' + ' and '.join(f'{x}–{y}' for x, y in dpos)
        out.append(desc)
    elif len(rings) > 1:
        out.append(multi_ring(M, rings))
    else:
        cs = [i for i in G if A[i]['el'] == 'C']
        Gc = G.subgraph(cs)
        Hv = G.subgraph([i for i in G if A[i]['el'] != 'H'])
        if cs and nx.number_connected_components(Gc) > 1 and nx.is_connected(Hv):
            # heteroatoms inside the backbone (ester, amide, ether, ...): give the condensed formula
            ends = [i for i in Hv if Hv.degree(i) <= 1]
            a0 = max(ends, key=lambda e: (max(len(p) for p in nx.single_source_shortest_path(Hv, e).values()), A[e]['el'] == 'C', -e))
            far = nx.single_source_shortest_path(Hv, a0); b0 = max(far, key=lambda t: len(far[t]))
            out.append(f'condensed formula {cond(M, a0, None, set(), end=None)}')
            geo = cistrans_notes(M)
            if geo: out.append(geo)
            ch = [(plain(a['lab']), a['ch']) for a in A if a['ch']]
            out += extra_stereo(M) + tag_notes(M)
            if m.get('cap'): out.append(f'labeled "{plain(m["cap"])}"')
            return ': '.join(out[:2]) + ('; ' + '; '.join(out[2:]) if len(out) > 2 else '') + '.'
        best = []
        for comp in nx.connected_components(Gc):
            ends = [i for i in comp if Gc.degree(i) <= 1] or list(comp)
            for a in ends:
                for b in ends:
                    if a < b or len(comp) == 1:
                        try: p = nx.shortest_path(Gc, a, b)
                        except nx.NetworkXNoPath: continue
                        if len(p) > len(best): best = p
        chain = best or cs[:1]
        def score(pth):
            sc = []
            for pos, i in enumerate(pth):
                if any(A[k]['el'] not in ('C', 'H') for k in G[i]) or any(G[i][k]['o'] > 1 for k in G[i]): sc.append(pos)
            return sc
        if score(list(reversed(chain))) < score(chain): chain = list(reversed(chain))
        n = len(chain); onchain = set(chain)
        anyw = any(d.get('w') for _, _, d in G.edges(data=True))
        nbr = sum(1 for i in chain for k in G[i] if k not in onchain and A[k]['el'] == 'C')
        desc = (f'a chain of {n} carbon atom{"s" if n > 1 else ""}' if n > 1 else 'one carbon atom') + ('' if nbr else (' (unbranched)' if n > 2 else ''))
        det = []
        for idx in range(n - 1):
            a, b = chain[idx], chain[idx + 1]; o = G[a][b]['o']
            if o == 2:
                # cis/trans: compare the chain neighbors on each side of the double bond
                pa = [k for k in G[a] if k != b and A[k]['el'] != 'H']; pb = [k for k in G[b] if k != a and A[k]['el'] != 'H']
                geo = ''
                if pa and pb and len(pa) == 1 and len(pb) == 1:
                    s1 = side(A[pa[0]], A[a], A[b]); s2 = side(A[pb[0]], A[a], A[b])
                    geo = ' (the chain continues on the same side of the double bond)' if s1 * s2 > 0 else ' (the chain continues on opposite sides of the double bond)'
                det.append(f'a C=C double bond between carbons {idx + 1} and {idx + 2}{geo}')
            elif o == 3: det.append(f'a C≡C triple bond between carbons {idx + 1} and {idx + 2}')
        for idx, i in enumerate(chain):
            for k in G[i]:
                if k in onchain or A[k]['el'] == 'H': continue
                ud = ''
                if anyw: ud = ' drawn ' + ('below' if A[k]['y'] > A[i]['y'] + 0.2 else 'above' if A[k]['y'] < A[i]['y'] - 0.2 else 'level with') + ' the chain'
                det.append(f'{group_name(M, i, k, onchain)} on carbon {idx + 1}{ud}{wnote(M, i, k)}')
        if anyw and n > 1: desc += f' drawn as a zigzag with carbon 1 at the {"left" if A[chain[0]]["x"] < A[chain[-1]]["x"] else "right"} end'
        if det: desc += '; ' + '; '.join(det)
        out.append(desc)
    ch = [(plain(a['lab']), a['ch']) for a in A if a['ch']]
    if ch and not M.skel: out.append('charges: ' + ', '.join(f'{l} {"+" if c > 0 else "−"}' for l, c in ch))
    out += extra_stereo(M)
    out += tag_notes(M)
    if m.get('cap'): out.append(f'labeled "{plain(m["cap"])}"')
    return ': '.join(out[:2]) + ('; ' + '; '.join(out[2:]) if len(out) > 2 else '') + '.'

def cistrans_notes(M):
    A = M.atoms; G = M.G; notes = []
    for a, b, d in G.edges(data=True):
        if d['o'] != 2 or A[a]['el'] != 'C' or A[b]['el'] != 'C': continue
        pa = heavy_nb(M, a, {b}); pb = heavy_nb(M, b, {a})
        if len(pa) == 1 and len(pb) == 1:
            s1 = side(A[pa[0]], A[a], A[b]); s2 = side(A[pb[0]], A[a], A[b])
            notes.append('at the C=C double bond the chain continues on ' + ('the same side' if s1 * s2 > 0 else 'opposite sides'))
    return '; '.join(notes)

def ring_word(r):
    if r['arom']: return 'a benzene ring'
    het = r['het']
    hs = ''
    if het:
        c = {}
        for e in het: c[e] = c.get(e, 0) + 1
        hs = ' containing ' + ' and '.join((f'{NUMW[v]} {e} atoms' if v > 1 else f'one {e} atom') for e, v in c.items())
    return f'a {RINGW.get(r["n"], r["n"])}-membered ring{hs}' + (f' with {NUMW.get(r["dbl"], r["dbl"])} double bond{"s" if r["dbl"] > 1 else ""}' if r['dbl'] else '')

def plural(g, v):
    g = re.sub(r'^an? ', '', g)
    g = re.sub(r'\b(group|atom|chain)\b', r'\1s', g, count=1)
    return f'{NUMW.get(v, v)} {g}'

def multi_ring(M, rings):
    A = M.atoms; G = M.G
    # fuse rings that share a bond into ring systems
    sys_ = []
    for r in rings:
        hit = [s_ for s_ in sys_ if len(set(r['atoms']) & s_['atoms']) >= 2]
        new = {'atoms': set(r['atoms']), 'rings': [r]}
        for h in hit: new['atoms'] |= h['atoms']; new['rings'] += h['rings']; sys_.remove(h)
        sys_.append(new)
    sys_.sort(key=lambda s_: min(s_['atoms']))
    rn = {}
    for n, s_ in enumerate(sys_, 1):
        for i in s_['atoms']: rn[i] = f'ring {n}' if len(s_['rings']) == 1 else f'ring system {n}'
    descs = []
    for n, s_ in enumerate(sys_, 1):
        if len(s_['rings']) == 1: descs.append(f'ring {n} is {ring_word(s_["rings"][0])}')
        else: descs.append(f'ring system {n} is {NUMW.get(len(s_["rings"]), len(s_["rings"]))} fused rings (' + ' fused to '.join(ring_word(r) for r in s_['rings']) + ')')
    allring = set(rn)
    links = []; done = set(); on = {}
    for n, s_ in enumerate(sys_, 1):
        for i in sorted(s_['atoms']):
            for k in G[i]:
                if k in s_['atoms'] or A[k]['el'] == 'H': continue
                if k in allring:
                    key = frozenset((rn[i], rn[k]))
                    if key not in done: done.add(key); links.append(f'{rn[i]} is bonded directly to {rn[k]}')
                    continue
                # the fragment hanging off ring atom i through k
                frag = {k}; st = [k]
                while st:
                    x = st.pop()
                    for y in G[x]:
                        if y not in frag and y not in allring and A[y]['el'] != 'H': frag.add(y); st.append(y)
                touches = {rn[y] for x in frag for y in G[x] if y in allring} - {rn[i]}
                if touches:
                    key = frozenset(frag)
                    if key in done: continue
                    done.add(key)
                    links.append(f'{rn[i]} is connected to ' + ' and '.join(sorted(touches)) + f' through {cond(M, k, i, s_["atoms"], rn)}')
                else:
                    on.setdefault(rn[i], []).append(group_name(M, i, k, allring) + wnote(M, i, k))
    parts = ['; '.join(descs)]
    for r_, gs in on.items():
        c = {}
        for g in gs: c[g] = c.get(g, 0) + 1
        parts.append(f'on {r_}: ' + ', '.join(g if v == 1 else plural(g, v) for g, v in c.items()))
    parts += links
    return '; '.join(parts)

def features(M, ban):
    A = M.atoms; G = M.G; f = []
    for i, a in enumerate(A):
        lab = plain(a['lab'])
        if lab in ('OH', 'HO'): f.append('OH')
        elif a['el'] == 'O' and any(G[i][k]['o'] == 2 for k in G[i]): f.append('C=O')
        elif a['el'] == 'O' and len(G[i]) == 2: f.append('C–O–C')
        elif lab in ('NH2', 'H2N'): f.append('NH₂')
        elif a['el'] == 'N': f.append('N')
        elif a['el'] in HAL: f.append(a['el'])
        elif a['el'] in ('S', 'P'): f.append(a['el'])
    c = {}
    for x in f: c[x] = c.get(x, 0) + 1
    dbl = sum(1 for a, b, d in G.edges(data=True) if d['o'] == 2 and A[a]['el'] == 'C' and A[b]['el'] == 'C')
    res = [f'{v} {k}' if v > 1 else k for k, v in c.items()]
    return res

def describe_struct(sp):
    """sp: the 's' list (molecules, '+' strings, arrow dicts)."""
    if not sp: return ''
    parts = []
    for p in sp:
        if isinstance(p, str): parts.append('plus' if p.strip() == '+' else plain(p))
        elif isinstance(p, dict) and 'arrow' in p:
            t = 'reaction arrow' + (f' labeled "{plain(p["arrow"])}"' if p.get('arrow') else '') + (f', with "{plain(p["below"])}" below it' if p.get('below') else '')
            parts.append(t)
        elif isinstance(p, dict): parts.append(describe_mol(p).rstrip('.'))
    if len(parts) == 1: return parts[0] + '.'
    if not any(isinstance(p, dict) and 'arrow' in p for p in sp) and not any(isinstance(p, str) and p.strip() == '+' for p in sp):
        return f'{NUMW.get(len(parts), len(parts)).capitalize()} structures shown. ' + ' '.join(f'{p.rstrip(".")}.' for p in parts)
    return 'Reaction scheme: ' + '; then '.join(parts) + '.'

def describe_choices(cs, labels='ABCDEF'):
    return 'Answer choices drawn as structures. ' + ' '.join(f'{labels[k]}: {describe_mol(m)}' for k, m in enumerate(cs) if m)

# ---------- figures ----------
# D-sugars in standard Haworth orientation: group above ("up") or below ("down") the ring at each ring carbon
HAWP = {  # pyranoses (ring: C1-C5 + O); C5 carries CH2OH up
 'glucose': {2: 'OH down', 3: 'OH up', 4: 'OH down'}, 'galactose': {2: 'OH down', 3: 'OH up', 4: 'OH up'},
 'mannose': {2: 'OH up', 3: 'OH up', 4: 'OH down'}}
def haworth_ring(r, tags=None, link=None):
    sug = r.get('sugar', ''); an = r.get('anomer', '')
    tags = r.get('tags', tags) or {}
    g = []
    if sug in HAWP:
        first = 1; g.append(('C1', 'OH ' + {'a': 'down', 'b': 'up'}.get(an, 'shown')))
        g += [(f'C{k}', v) for k, v in HAWP[sug].items()]; g.append(('C5', 'CH₂OH up'))
        ring = 'six-membered ring (five carbons and one oxygen)'
    elif sug == 'fructose':
        first = 2; g.append(('C2', {'a': 'OH down and CH₂OH up', 'b': 'OH up and CH₂OH down'}.get(an, 'OH and CH₂OH')))
        g += [('C3', 'OH up'), ('C4', 'OH down'), ('C5', 'CH₂OH up')]
        ring = 'five-membered ring (four carbons and one oxygen)'
    elif sug in ('ribose', 'deoxyribose'):
        first = 1; g.append(('C1', 'OH ' + {'a': 'down', 'b': 'up'}.get(an, 'shown')))
        g += [('C2', 'OH down' if sug == 'ribose' else 'H only, no OH'), ('C3', 'OH down'), ('C4', 'CH₂OH up')]
        ring = 'five-membered ring (four carbons and one oxygen)'
    else:
        return f'a sugar ring ({sug})'
    if link:
        g = [(c, f'bonded to the bridging O, which points {link[1]}' + (', and H on the other side' if 'CH₂OH' not in t else '')) if c == f'C{link[0]}' else (c, t) for c, t in g]
    lab = []
    for k, v in tags.items():
        lab.append(f'label "{v}" on the ring oxygen' if k == 'O' else f'label "{v}" on C{int(k) + first}')
    return f'a {ring} with ' + ', '.join(f'{c} {t}' for c, t in g) + (('; ' + ', '.join(lab)) if lab else '')

def describe_plot(f):
    xs, ys = f['x'], f['y']
    xnum = bool(xs.get('ticks')); ynum = bool(ys.get('ticks')) and not ys.get('noTicks')
    ymin, ymax = ys.get('min', 0), ys['max']
    def yv(v):
        if ynum: return f'{v:.0f}'
        fr = (v - ymin) / (ymax - ymin)
        return 'zero' if fr < 0.03 else f'about {round(fr * 20) * 5}% of the y-axis height'
    def xv(v): return f'{v:g}' if xnum else None
    out = [f'Graph of {plain(ys["label"])} (y-axis' + (f', {ymin} to {ys["max"]}' if ynum else ', no numbers') + f') against {plain(xs["label"])} (x-axis' + (f', {xs["min"]} to {xs["max"]}' if xnum else ', no numbers') + ')']
    bars = [s_ for s_ in f['series'] if s_.get('bars')]
    if bars:
        for s_ in bars:
            labs = s_.get('barLabels') or [f'{p[0]:g}' for p in s_['pts']]
            out.append('bar chart: ' + '; '.join(f'{plain(l)}: {yv(p[1])}' for l, p in zip(labs, s_['pts'])))
    for s_ in f['series']:
        if s_.get('bars'): continue
        pts = s_['pts']; Y = [p[1] for p in pts]; X = [p[0] for p in pts]
        y0, yN, hi, lo = Y[0], Y[-1], max(Y), min(Y); rng = (ymax - ymin) or 1
        k = Y.index(hi)
        sl = [(Y[n + 1] - Y[n]) / ((X[n + 1] - X[n]) or 1) for n in range(len(Y) - 1)]
        if hi - lo < 0.05 * rng: shape = f'is a flat horizontal line at {yv(y0)}' if not ynum else f'is a flat horizontal line at about {y0:.0f}'
        elif max(sl) - min(sl) < 0.05 * max(abs(x) for x in sl) and sl[0] > 0: shape = f'is a straight line rising steadily from {yv(y0)} to {yv(yN)}'
        elif sl[0] < 0 and yN < y0 and k == 0: shape = f'falls from {yv(y0)} to {yv(yN)}'
        elif yN < hi - 0.25 * (hi - lo) and 0 < k < len(Y) - 1:
            px = xv(X[k]); shape = f'starts at {yv(y0)}, rises to a peak of {yv(hi)}' + (f' at x ≈ {px}' if px else ' near the middle') + f', then falls to {yv(yN)}'
            if any(abs(Y[n] - lo) < 0.03 * rng for n in range(k, len(Y))) and lo < 0.05 * rng: shape += (f' (about zero from x ≈ {xv(X[next(n for n in range(k, len(Y)) if Y[n] < 0.03 * rng)])} on)' if xnum else '')
        else:
            hx = next(X[n] for n in range(len(Y)) if Y[n] >= y0 + (hi - y0) / 2)
            hh = f'x ≈ {hx:g}' if xnum else f'about {round((hx - xs["min"]) / (xs["max"] - xs["min"]) * 100)}% of the way along the x-axis'
            shape = f'starts at {yv(y0)}, rises steeply at first, then levels off (plateau) at {yv(hi)}; it reaches half of that height at {hh}'
        lab = plain(s_.get('label', '')).strip()
        out.append((f'curve {lab} ' if lab else ('the curve ' if len(f['series']) == 1 else 'a curve ')) + shape)
    if f.get('points'):
        s0 = [s_ for s_ in f['series'] if not s_.get('bars')][0]['pts']
        def where(x):
            n = max([m for m in range(len(s0) - 1) if s0[m][0] <= x] or [0])
            sl = [(s0[m + 1][1] - s0[m][1]) / ((s0[m + 1][0] - s0[m][0]) or 1) for m in range(len(s0) - 1)]
            r = sl[n] / (max(sl) or 1)
            return 'on the steep early rise' if r > 0.35 else 'at the bend' if r > 0.05 else 'on the flat plateau'
        out.append('marked points: ' + '; '.join(f'{p[2]} {where(p[0])}' for p in f['points']))
    if f.get('vlines'):
        out.append('dashed vertical lines marked ' + ' and '.join(plain(v.get('label', f'{v["x"]:g}')) for v in f['vlines']))
    if f.get('hlines'):
        out.append('dashed horizontal line' + ('s' if len(f['hlines']) > 1 else '') + ' marked ' + ' and '.join(plain(h.get('label', '')) for h in f['hlines']))
    if f.get('marks'):
        out.append('labels on the graph: ' + ', '.join(f'"{plain(m_[2])}" ' + ('near the start' if m_[0] < (xs['min'] + xs['max']) / 2 else 'near the end') for m_ in f['marks']))
    return out[0] + ': ' + '; '.join(out[1:]) + '.'

def describe_fig(f):
    t = f.get('type')
    if t == 'eq': return None
    if t == 'table': return None
    if t == 'path':
        steps = []
        for i, nd in enumerate(f['nodes']):
            s = plain(nd)
            if i < len(f['nodes']) - 1:
                ins = ', '.join(map(plain, f['ins'][i])) if i < len(f.get('ins', [])) and f['ins'][i] else ''
                outs = ', '.join(map(plain, f['outs'][i])) if i < len(f.get('outs', [])) and f['outs'][i] else ''
                extra = '; '.join(x for x in [f'{ins} in' if ins else '', f'{outs} out' if outs else ''] if x)
                lab = plain(f['steps'][i]) if i < len(f.get('steps', [])) and f['steps'][i] else ''
                inner = '; '.join(x for x in [lab, extra] if x)
                s += f' → ({inner})' if inner else ' →'
            steps.append(s)
        return f'Pathway diagram{" titled " + plain(f["title"]) if f.get("title") else ""}: ' + ' '.join(steps) + '.'
    if t == 'cycle':
        n = f['nodes']; L = []
        for i, nd in enumerate(n):
            ins = ', '.join(map(plain, f['ins'][i])) if f.get('ins') and f['ins'][i] else ''
            outs = ', '.join(map(plain, f['outs'][i])) if f.get('outs') and f['outs'][i] else ''
            extra = '; '.join(x for x in [f'{ins} in' if ins else '', f'{outs} out' if outs else ''] if x)
            L.append(f'{plain(nd)} → {plain(n[(i + 1) % len(n)])}' + (f' ({extra})' if extra else ''))
        e = f.get('entry'); ent = f' {plain(e["label"])} enters the cycle at {plain(n[e["at"]])}.' if e else ''
        return f'Cycle diagram titled {plain(f.get("title", "")).replace("|", " ")}, with {len(n)} steps: ' + '; '.join(L) + '.' + ent
    if t == 'plot':
        return describe_plot(f)
    if t == 'enzyme':
        K = {'free': 'the enzyme with its empty active site and the substrate (yellow) nearby, not bound',
             'fit': 'the substrate (yellow) bound in the enzyme’s active site',
             'competitive': 'an inhibitor (red) sitting in the active site, so the substrate (yellow) cannot bind',
             'noncompetitive': 'an inhibitor (red) bound at a different site on the enzyme, and the active site’s shape is changed',
             'product': 'products leaving the active site',
             'nofit': 'a triangular substrate (yellow) next to a square active site it cannot fit into',
             'induced': 'the active site changing shape as the substrate (yellow) binds (induced fit)',
             'denatured': 'the enzyme unfolded (denatured), with no active site, and the substrate (yellow) not bound'}
        return 'Cartoon panels of an enzyme: ' + '; '.join(f'panel {p.get("cap", i + 1)}: {K.get(p["kind"], p["kind"])}' for i, p in enumerate(f['panels'])) + '.'
    if t == 'fischer' and f.get('items'):
        return 'Fischer projections: ' + ' '.join(f'Structure {it.get("cap", i + 1)}: ' + describe_fig(dict(it, type='fischer'))[len('Fischer projection: '):] for i, it in enumerate(f['items']))
    if t == 'fischer':
        parts = []
        for i, r in enumerate(f['rows']):
            if isinstance(r, str):
                parts.append(f'carbon {i + 2}: {plain(r).replace("C=O", "C=O (carbonyl group)")}')
            else:
                parts.append(f'carbon {i + 2}: {plain(r[0])} on the left, {plain(r[1])} on the right')
        rows = '; '.join(parts)
        return f'Fischer projection: {plain(f["top"])} at the top; {rows}; {plain(f["bottom"])} at the bottom.'
    if t == 'haworth':
        if f.get('items'):
            return 'Haworth projections: ' + '; '.join(f'structure {it.get("cap", i + 1)}: ' + haworth_ring(it) for i, it in enumerate(f['items'])) + '.'
        if f.get('rings'):
            R = f['rings']; L = f.get('link', {})
            def cnum(r, pos): return pos + (2 if r.get('sugar') == 'fructose' else 1)
            fr, to = L.get('from', [0, '']), L.get('to', [0, ''])
            link = (f'The rings are joined by an oxygen bridge (glycosidic bond) from C{cnum(R[0], fr[0])} of the first ring (bond pointing {fr[1]}) '
                    f'to C{cnum(R[1], to[0])} of the second ring (bond pointing {to[1]}).') if L else ''
            l0 = (cnum(R[0], fr[0]), fr[1]) if L else None; l1 = (cnum(R[1], to[0]), to[1]) if L else None
            return 'Haworth projection of two sugar rings. First ring: ' + haworth_ring(R[0], link=l0) + '. Second ring' + (' (drawn flipped)' if R[1].get('flip') else '') + ': ' + haworth_ring(R[1], link=l1) + '. ' + link
        return 'Haworth projection: ' + haworth_ring(f) + '.'
    return None
