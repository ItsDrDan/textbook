"""Batch Z (2026-11-13): side-scroll on phones for every wide SVG figure whose labels would otherwise be under 8 px.
Pattern proven on 14.5 (batch Y): the image (or a run of adjacent slices of one figure) is wrapped in a .fig-scroll box;
below 600 px the image keeps a readable width and the box scrolls sideways. One hint line per page, phone only.
Desktop (over 600 px) and print are untouched: every rule sits inside a screen-and-width media query.
  python3 tools/phone_scroll_build.py --measure <dir with hosted svgs>   refresh tools/phone_scroll_metrics.json
  python3 tools/phone_scroll_build.py                                    build tools/batchZ_2026-11-13.json
Edits are applied in order, each replacing the FIRST remaining occurrence of "old"."""
import re, glob, os, json, sys, hashlib, collections, math
PHONE = 354; TARGET = 10.0; NEED = 8.0
MET = 'tools/phone_scroll_metrics.json'

def measure(extra):
    files = {}
    for f in glob.glob(extra + '/*.svg'): files[os.path.basename(f).split('_', 1)[1]] = f
    order = lambda f: (('batchT' in f) * 2 + any(k in f for k in ('/print/', '/pathways/', '/conceptmaps/')), os.path.getmtime(f))
    loc = collections.defaultdict(list)
    for f in glob.glob('figures/**/*.svg', recursive=True):
        if '/phone/' not in f: loc[os.path.basename(f)].append(f)
    for n, c in loc.items(): files[n] = sorted(c, key=order)[-1]
    out = {}
    for n, f in files.items():
        x = open(f, encoding='utf-8', errors='ignore').read()
        vb = re.search(r'viewBox="\s*([-0-9.]+)[ ,]+([-0-9.]+)[ ,]+([0-9.]+)[ ,]+([0-9.]+)', x)
        if not vb: continue
        fs = collections.Counter()
        for m in re.finditer(r'<text[^>]*?font-size="([0-9.]+)(?:px)?"[^>]*>([^<]*)', x):
            if len(m.group(2).strip()) > 3: fs[float(m.group(1))] += 1
        nested = bool(re.search(r'<g[^>]*transform="[^"]*scale\(', x)) or x.count('<svg') > 1
        out[n] = {'W': float(vb.group(3)), 'H': float(vb.group(4)), 'font': fs.most_common(1)[0][0] if fs else None, 'nested': nested}
    json.dump(out, open(MET, 'w'), indent=0, sort_keys=True); print('measured', len(out))

if '--measure' in sys.argv:
    measure(sys.argv[sys.argv.index('--measure') + 1]); sys.exit()

M = json.load(open(MET))
VOID = {'img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'col', 'wbr'}

def parent(t, pos):
    st = []
    for m in re.finditer(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>', t[:pos]):
        c, tag, sc = m.group(1), m.group(2).lower(), m.group(3)
        if tag in VOID or sc: continue
        if c:
            if tag in st:
                while st and st.pop() != tag: pass
        else: st.append(tag)
    return st

def plan(tag):
    """-> phone width for this <img>, or None when it is fine as it is."""
    s = re.search(r'src="([^"?]+\.svg)', tag)
    if not s or 'fig-wide' in tag or 'fig-phone' in tag or re.search(r'fig-w\d', tag): return None
    m = M.get(s.group(1).split('/')[-1])
    if not m: return None
    dw = re.search(r'\bwidth="(\d+)"', tag) or re.search(r'width:\s*(\d+)px', tag)
    disp = float(dw.group(1)) if dw else m['W']
    shown = min(PHONE, disp)
    if m['font'] and not m['nested'] and m['font'] * shown / m['W'] >= 3:
        px = m['font'] * shown / m['W']
        if px >= NEED: return None
        w = m['W'] * TARGET / m['font']
    else:                      # label size cannot be read from the file: go by the drawing's own width
        if disp < 640: return None
        w = min(disp, 760)
    w = int(min(1020, max(480, math.ceil(w / 60) * 60)))
    return w if w >= PHONE * 1.3 else None

h = lambda s: hashlib.sha256(s.encode()).hexdigest()
edits, sha, report, skipped, widths = {}, {}, [], [], set()
for pf in sorted(glob.glob('pages/live/*.html')):
    pid = os.path.basename(pf)[:-5]; t = open(pf, encoding='utf-8').read()
    imgs = [(m.start(), m.end(), m.group(0), plan(m.group(0))) for m in re.finditer(r'<img\b[^>]*>', t)]
    groups = []
    for a, b, tag, w in imgs:
        if w is None: continue
        if t[max(0, a - 300):a].rfind('fig-scroll">') > t[max(0, a - 300):a].rfind('</div>') and 'class="fig-scroll"' in t[max(0, a - 300):a]: continue
        if groups and not t[groups[-1][1]:a].strip(): groups[-1][1] = b; groups[-1][2] = max(groups[-1][2], w); groups[-1][3] += 1
        else: groups.append([a, b, w, 1])
    if not groups: continue
    cur = t; es = []; first = 'class="fig-scroll-hint"' not in t   # the 14.5 test page already has its hint
    for a, b, w, n in groups:
        st = parent(t, a); par = st[-1] if st else 'top'
        old = t[a:b]
        if par in ('a', 'td', 'th', 'summary', 'button') or 'a' in st:
            skipped.append((pid, par, re.search(r'src="[^"]*/([^"/?]+)', old).group(1))); continue
        el = 'span' if par in ('p', 'span', 'strong', 'em', 'h2', 'h3', 'h4', 'li') else 'div'
        body = re.sub(r'<img\b([^>]*)>', lambda m: ('<img' + re.sub(r'class="', 'class="fig-w%d ' % w, m.group(1), 1) + '>') if 'class="' in m.group(1) else '<img class="fig-w%d"%s>' % (w, m.group(1)), old)
        new = ('<span class="fig-scroll-hint">Swipe sideways to see the whole figure.</span>' if first else '') + '<%s class="fig-scroll">%s</%s>' % (el, body, el)
        assert cur.count(old) >= 1
        cur = cur.replace(old, new, 1); first = False; widths.add(w)
        es.append({'old': old, 'new': new, 'count': 'first', 'note': 'phone side-scroll at %d px (%d image%s, parent <%s>)' % (w, n, '' if n == 1 else 's', par)})
        report.append((pid, w, n, par, re.search(r'src="[^"]*/([^"/?]+)', old).group(1)))
    if not es: continue
    edits[pid] = es; sha[pid] = {'before': h(t), 'mid': cur}

WS = sorted(set(range(480, 1021, 60)))
STYLE = ('<style type="text/css">/*<![CDATA[*/.fig-scroll-hint { display: none !important; } @media screen and (max-width: 600px) { '
         '.fig-scroll { display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; width: 100%; max-width: 100%; min-width: 0; } '
         '.fig-scroll img { max-width: none !important; } ' + ' '.join('.fig-scroll img.fig-w%d { width: %dpx !important; }' % (w, w) for w in WS) +
         ' .fig-scroll-hint { display: block !important; font-size: 0.8em; color: #5a6478; margin: 0 0 4px; } }/*]]>*/</style>')
for pid in edits:
    cur = sha[pid].pop('mid')
    edits[pid].insert(0, {'old': '', 'new': STYLE, 'count': 'prepend', 'note': 'style block for phone side-scroll (screen and max-width 600 px only)'})
    cur = STYLE + cur
    sha[pid]['after'] = h(cur)
    open('audit/preview/%s.html' % pid, 'w', encoding='utf-8').write(cur)
json.dump({'uploads': [], 'edits': edits}, open('tools/batchZ_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchZ_sha_2026-11-13.json', 'w'))
json.dump({'groups': report, 'skipped': skipped}, open('tools/batchZ_report_2026-11-13.json', 'w'), indent=0)
print(len(edits), 'pages;', len(report), 'scroll boxes;', sum(r[2] for r in report), 'images; skipped', len(skipped))
print('widths', collections.Counter(r[1] for r in report).most_common()); print('parents', collections.Counter(r[3] for r in report).most_common())
print('skipped', skipped[:12])
