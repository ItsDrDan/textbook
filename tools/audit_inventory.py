"""Inventory of every live page for the coverage ledger (master refinement pass, 2026-11-13).
Usage: python3 tools/audit_inventory.py [pdf.json] > audit/inventory.json
pdf.json (optional) = {'toc': PyMuPDF get_toc(), 'pages': [{'p','label',...}]} from the full-book PDF."""
import re, json, sys, html, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
snap = open(f'{ROOT}/pages/LIVE_SNAPSHOT.md').read()
order = re.findall(r'\| \[(\d+)\]\(live/\d+\.html\) \| (.*?) \|', snap)
norm = lambda s: re.sub(r'[^a-z0-9]+', '', html.unescape(s).lower())
pdf = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else None
start = {}
if pdf:
    for lvl, t, p in pdf['toc']:
        if lvl == 1: start.setdefault(norm(t), []).append(p)
# course-outline map
al = open(f'{ROOT}/pages/live/597272.html').read()
obj, unit = {}, {}
for r in re.findall(r'<tr>(.*?)</tr>', al, flags=re.S):
    ids = re.findall(r'/@go/page/(\d+)', r)
    m = re.search(r'data-th="Course objective">(\d+)\.', r)
    if m:
        for i in ids: obj.setdefault(i, []).append(m.group(1))
    m = re.search(r'data-th="Outline item">(.*?)</td>', r)
    if m:
        for i in ids: unit.setdefault(i, []).append(html.unescape(m.group(1)).replace('–', '-'))
out = []
seen = {}
for pid, title in order:
    f = f'{ROOT}/pages/live/{pid}.html'
    h = open(f).read() if os.path.exists(f) else ''
    cnt = lambda pat, fl=0: len(re.findall(pat, h, flags=fl))
    iframes = re.findall(r'<iframe[^>]*src="([^"]+)"[^>]*>', h)
    ifr_full = re.findall(r'<iframe[^>]*>', h)
    rec = dict(id=pid, title=html.unescape(title), bytes=len(h),
        objectives=cnt(r'box-objectives'), lecture_connection=cnt(r'>Lecture Connection<'),
        professor_tip=cnt(r'Professor Tip'), examples=cnt(r'box-example'), exercises=cnt(r'box-exercise'),
        figures=cnt(r'<img\b'), imgs_no_alt=len([m for m in re.findall(r'<img\b[^>]*>', h) if not re.search(r'alt="[^"]+"', m)]),
        tables=cnt(r'<table\b'), valley=cnt(r'class="valley-connection|Valley Connection:'), rosa=cnt(r'Rosa'),
        in_the_lab=cnt(r'In the Lab'), summary=cnt(r'>(Summary|Chapter Summary|Key Ideas?)<'),
        details=cnt(r'<details'), print_key=cnt(r'showprint answer-key'), key_items=cnt(r'answer-key-item'),
        videos=[u for u in iframes if 'youtube' in u], widgets=[html.unescape(u) for u in iframes if 'itsdrdan.github.io' in u],
        other_iframes=[u for u in iframes if 'youtube' not in u and 'itsdrdan.github.io' not in u],
        iframes_no_title=len([m for m in ifr_full if 'title="' not in m]),
        game_links=sorted(set(re.findall(r'href="(https://itsdrdan\.github\.io/[^"]+)"', h))),
        headings=[(int(l), re.sub(r'<[^>]+>', '', t)) for l, t in re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>', h, flags=re.S)],
        objectives_cor=sorted(set(obj.get(pid, [])), key=int), outline_units=unit.get(pid, []))
    if pdf:
        k = norm(title); n = seen.get(k, 0); seen[k] = n + 1
        ps = start.get(k, [])
        rec['pdf_start'] = ps[n] if n < len(ps) else None
    out.append(rec)
if pdf:
    starts = sorted(set(r['pdf_start'] for r in out if r.get('pdf_start')))
    total = len(pdf['pages'])
    for r in out:
        s = r.get('pdf_start')
        if s:
            nxt = [x for x in starts if x > s]
            e = (nxt[0] - 1) if nxt else total
            r['pdf_end'] = max(e, s)
            r['print_start'] = pdf['pages'][s - 1]['label']; r['print_end'] = pdf['pages'][r['pdf_end'] - 1]['label']
json.dump(out, sys.stdout, indent=1)
