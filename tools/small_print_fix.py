"""Raise figure labels that print under 6 pt (2026-11-13, 18:41 compile).
Input: a JSON list made from the full-book PDF: for each PDF page with words under 6 pt, the page id, the label texts
and their printed sizes (scratch file small.json; see tools/ISSUE_LEDGER.md for how it is made).
For each SVG on that book page that contains one of those labels, the script works out the file's print scale
(printed pt per SVG px) from the matched label, then raises every font-size value that carries a too-small WORD label
so it prints at about 6.2 pt. Only font-size attribute values are changed. Subscript-size text is left alone.
Usage: python3 tools/small_print_fix.py small.json svg_cache_dir out_dir   -> writes changed SVGs to out_dir and a report JSON"""
import json, re, sys, os, html, subprocess, math, collections

small = json.load(open(sys.argv[1])); cache = sys.argv[2]; outdir = sys.argv[3]
TARGET = 6.1
# Hand placement for labels that would touch a box or an arrow at the larger size: file -> [(start of the label's first line, dx, dy)]
NUDGE = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'small_print_nudges.json'))) if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'small_print_nudges.json')) else {}
os.makedirs(outdir, exist_ok=True)


def texts(svg):
    """[(font_size, text)] for every <text> element; font-size from the element or the nearest enclosing <g>"""
    out = []; stack = [None]
    for m in re.finditer(r'<(/?)(g|text)\b([^>]*)>|<text\b[^>]*/>', svg):
        if m.group(0).startswith('<text') and m.group(0).endswith('/>'): continue
        close, tag, attrs = m.group(1), m.group(2), m.group(3) or ''
        if tag == 'g':
            if close: stack.pop() if len(stack) > 1 else None
            else:
                f = re.search(r'font-size="([\d.]+)', attrs); stack.append(f.group(1) if f else stack[-1])
        elif tag == 'text' and not close:
            f = re.search(r'font-size="([\d.]+)', attrs); fs = f.group(1) if f else stack[-1]
            end = svg.find('</text>', m.end()); body = svg[m.end():end]
            # tspans may carry their own size
            parts = re.split(r'(<tspan\b[^>]*>|</tspan>)', body); cur = [fs]
            for p in parts:
                if p.startswith('<tspan'):
                    g = re.search(r'font-size="([\d.]+)', p); cur.append(g.group(1) if g else cur[-1])
                elif p == '</tspan>':
                    cur.pop() if len(cur) > 1 else None
                else:
                    t = html.unescape(re.sub(r'<[^>]+>', '', p)).strip()
                    if t and cur[-1]: out.append((cur[-1], t))
    return out


def load(src):
    url = src if src.startswith('http') else 'https://chem.libretexts.org' + src
    m = re.match(r'https://itsdrdan\.github\.io/textbook/(.*?)(\?.*)?$', url)
    if m and os.path.exists(m.group(1)): return m.group(1), open(m.group(1), encoding='utf-8').read(), 'repo'
    fn = os.path.join(cache, re.sub(r'[^A-Za-z0-9._-]', '_', url.split('/@api/deki/files/')[-1].split('?')[0])[-90:])
    if not os.path.exists(fn): subprocess.run(['curl', '-s', '-L', '-m', '30', '-o', fn, url])
    return fn, open(fn, encoding='utf-8').read(), 'libretexts'


def respace(old, new, changes):
    """Multi-line labels (consecutive <text> elements with the same x, one line height apart) keep their old line
    spacing when only font-size is raised, so the lines collide. Re-space each such group about its vertical centre in
    proportion to the font change, and grow the white backing rectangle that sits just before it (pathway.js labels)."""
    el = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
    olds = list(el.finditer(old)); news = list(el.finditer(new))
    if len(olds) != len(news): return new
    def attr(a, k):
        m = re.search(r'\b%s="([^"]*)"' % k, a); return m.group(1) if m else None
    groups = []; cur = []
    for i, m in enumerate(olds):
        a = m.group(1); fs = attr(a, 'font-size'); x = attr(a, 'x'); y = attr(a, 'y')
        ok = fs in changes and x is not None and y is not None
        if ok and cur:
            pa = olds[cur[-1]].group(1)
            gap = old[olds[cur[-1]].end():m.start()]
            dy = float(y) - float(attr(pa, 'y'))
            if attr(pa, 'x') == x and attr(pa, 'font-size') == fs and 0.9 * float(fs) <= dy <= 1.6 * float(fs) and not gap.strip():
                cur.append(i); continue
        if len(cur) > 1: groups.append(cur)
        cur = [i] if ok else []
    if len(cur) > 1: groups.append(cur)
    edits = []   # (start, end, replacement) on `new`
    for g in groups:
        fs = attr(olds[g[0]].group(1), 'font-size'); k = float(changes[fs]) / float(fs)
        ys = [float(attr(olds[i].group(1), 'y')) for i in g]; cy = (ys[0] + ys[-1]) / 2
        k2 = max(k, 1.14 * float(changes[fs]) / (ys[1] - ys[0]))   # at least 1.14 x the new font size between baselines
        for i, y in zip(g, ys):
            m = news[i]; ny = cy + (y - cy) * k2
            a2 = re.sub(r'\by="[^"]*"', 'y="%.1f"' % ny, m.group(1), count=1)
            edits.append((m.start(1), m.end(1), a2))
        # backing rectangle right before the group
        head = new[:news[g[0]].start()]
        rm = re.search(r'<rect\b([^>]*fill-opacity="[^"]*"[^>]*)/>\s*$', head)
        if rm:
            ra = rm.group(1)
            try:
                x, y, w, h = (float(attr(ra, t)) for t in ('x', 'y', 'width', 'height'))
                nw, nh = w, h + (ys[-1] - ys[0]) * (k - 1) + float(fs) * (k - 1)   # taller, not wider: a wider white box would hide the arrows beside it
                ra2 = re.sub(r'\bx="[^"]*"', 'x="%.1f"' % (x - (nw - w) / 2), ra, count=1)
                ra2 = re.sub(r'\by="[^"]*"', 'y="%.1f"' % (y - (nh - h) / 2), ra2, count=1)
                ra2 = re.sub(r'\bwidth="[^"]*"', 'width="%.1f"' % nw, ra2, count=1)
                ra2 = re.sub(r'\bheight="[^"]*"', 'height="%.1f"' % nh, ra2, count=1)
                edits.append((rm.start(1), rm.end(1), ra2))
            except TypeError:
                pass
    for st, en, rep in sorted(edits, reverse=True):
        new = new[:st] + rep + new[en:]
    return new


def nudge(svg, moves):
    """move a label (its consecutive same-x lines and the backing rect just before them) by dx, dy"""
    el = re.compile(r'(<rect\b[^>]*fill-opacity="[^"]*"[^>]*/>\s*)?((?:<text\b[^>]*>(?:(?!</text>).)*</text>\s*)+)', re.S)
    def shift(tag, dx, dy):
        tag = re.sub(r'\bx="([-\d.]+)"', lambda m: 'x="%.1f"' % (float(m.group(1)) + dx), tag, count=1)
        return re.sub(r'\by="([-\d.]+)"', lambda m: 'y="%.1f"' % (float(m.group(1)) + dy), tag, count=1)
    for start, dx, dy in moves:
        hit = 0
        def rep(m):
            nonlocal hit
            texts = re.findall(r'<text\b[^>]*>(?:(?!</text>).)*</text>\s*', m.group(2), flags=re.S)
            # find the run of lines that begins with `start`
            out = m.group(1) or ''; i = 0; done_rect = False; res = ''
            idx = next((k for k, t in enumerate(texts) if html.unescape(re.sub(r'<[^>]+>', '', t)).strip().startswith(start)), None)
            if idx is None: return m.group(0)
            x0 = re.search(r'\bx="([-\d.]+)"', texts[idx]).group(1)
            while idx > 0 and re.search(r'\bx="([-\d.]+)"', texts[idx - 1]).group(1) == x0: idx -= 1   # the whole same-x label, whichever line was named
            j = idx
            while j < len(texts) and re.search(r'\bx="([-\d.]+)"', texts[j]).group(1) == x0: j += 1
            hit += 1
            rect = m.group(1) or ''
            if rect and idx == 0: rect = re.sub(r'<rect\b[^>]*/>', lambda r: shift(r.group(0), dx, dy), rect, count=1)
            return rect + ''.join(texts[:idx]) + ''.join(re.sub(r'<text\b[^>]*>', lambda t: shift(t.group(0), dx, dy), t, count=1) for t in texts[idx:j]) + ''.join(texts[j:])
        svg = el.sub(rep, svg)
        if hit != 1: print('   nudge', repr(start), 'matched', hit, 'times')
    return svg


report = []; done = {}
for o in small:
    page = open('pages/live/%s.html' % o['pid'], encoding='utf-8').read()
    srcs = list(dict.fromkeys(html.unescape(s) for s in re.findall(r'<img\b[^>]*src="([^"]+\.svg[^"]*)"', page)))
    want = {re.sub(r'\s+', ' ', t): sz for sz, t in o['spans']}
    for src in srcs:
        path, svg, where = load(src)
        tx = texts(svg)
        # match small printed labels to SVG text runs (exact text, same font size for all runs of one label)
        scale_votes = []; raise_sizes = collections.defaultdict(list)
        for fs, t in tx:
            t2 = re.sub(r'\s+', ' ', t)
            if t2 in want and len(t2) >= 4:
                scale_votes.append(want[t2] / float(fs)); raise_sizes[fs].append((t2, want[t2]))
        if not scale_votes: continue
        scale_votes.sort(); scale = scale_votes[len(scale_votes) // 2]
        # keep only sizes whose own implied scale agrees with the file's scale (guards against a label that exists at two sizes)
        changes = {}
        for fs, labs in raise_sizes.items():
            if abs(float(fs) * scale - labs[0][1]) > 0.35: continue
            new = math.ceil(TARGET / scale * 2) / 2   # one target size per file, so labels that were 12 and 13 px both become the same readable size
            if new > float(fs): changes[fs] = ('%g' % new)
        if not changes: continue
        key = path
        prev = done.get(key)
        if prev:
            # same file seen from another PDF page: merge (take the larger new size)
            # same file seen from another PDF page: add sizes not seen yet, at this file's own scale
            for fs in changes:
                if fs not in prev['changes']:
                    nv = math.ceil(TARGET / prev['scale'] * 2) / 2
                    if nv > float(fs): prev['changes'][fs] = '%g' % nv
            prev['pdf'].append(o['pdf']); continue
        done[key] = {'src': src, 'path': path, 'where': where, 'page_id': o['pid'], 'pdf': [o['pdf']], 'scale': round(scale, 4), 'changes': changes,
                     'labels': sorted(set(l[0] for v in raise_sizes.values() for l in v))[:6]}

for key, r in done.items():
    svg = open(r['path'], encoding='utf-8').read(); new = svg
    # replace via placeholders so a size that is both an old and a new value is not changed twice
    for i, (fs, nv) in enumerate(r['changes'].items()):
        new = re.sub(r'font-size="%s(px)?"' % re.escape(fs), 'font-size="@@%d@@"' % i, new)
    for i, (fs, nv) in enumerate(r['changes'].items()):
        new = new.replace('font-size="@@%d@@"' % i, 'font-size="%s"' % nv)
    new = respace(svg, new, r['changes'])
    new = nudge(new, NUDGE.get(os.path.basename(r['path']), []))
    r['n_replaced'] = sum(len(re.findall(r'font-size="%s(?:px)?"' % re.escape(fs), svg)) for fs in r['changes'])
    r['printed_before'] = {fs: round(float(fs) * r['scale'], 2) for fs in r['changes']}
    r['printed_after'] = {nv: round(float(nv) * r['scale'], 2) for nv in r['changes'].values()}
    out = os.path.join(outdir, os.path.basename(r['path'])); r['out'] = out
    open(out, 'w', encoding='utf-8').write(new)
    report.append(r)
json.dump(report, open(os.path.join(outdir, 'report.json'), 'w'), indent=1)
for r in sorted(report, key=lambda r: r['pdf'][0]):
    print(r['pdf'], r['page_id'], r['where'][:4], os.path.basename(r['path'])[:44].ljust(44), 'scale %.3f' % r['scale'], r['changes'], 'print', r['printed_before'], '->', r['printed_after'], 'n', r['n_replaced'])
print(len(report), 'files')
