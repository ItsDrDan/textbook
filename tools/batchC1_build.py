"""Batch C1: figure numbering (review 2026-11-12).

Rules
- \\PageIndex{n} captions keep their numbers (they render as X.Y.n), except where noted below.
- Hard-typed captions "Figure X.Y.k" that clash continue after the page's highest \\PageIndex number, in page order.
- Chapter Guide two-part captions "Figure X.k" become "Figure X.Y.k" (Y = the guide's section number).
- In-text references follow the figure they point to (8.3 x2, 12.1 Professor Tip).
- 1.6: the uncaptioned ethyne image becomes Figure \\(\\PageIndex{3}\\).
- 5.4: source figures 2,3,4 -> 1,2,3 (captions and references); 9.1: source figure 2 -> 1 (2a/2b references).
Each change is applied in sequence to a working copy, and every edit's old string is checked to be unique at
that point, so the edit list can be replayed on the live page in the same order.
Output: tools/batchC1_fignum_2026-11-12.json  {page: [{old,new,count,note}]}
"""
import json, re

L = 'pages/live/'
import os, tempfile
TMP = os.environ.get('C1_TMP', tempfile.gettempdir() + '/')
scan = json.load(open('tools/figscan_2026-11-12.json'))
CAP = re.compile(r'(<figcaption>|<p[^>]*>\s*(?:<strong>|<em>)*)\s*(?:<strong>|<em>)*\s*Figure\s+(\\\(\\PageIndex\{(\w+)\}\\\)|(\d+)\.(\d+)(?:\.(\d+))?)(?=\s*[:.])', re.S)
edits = {}
log = []


class Page:
    def __init__(self, p):
        self.p = p; self.t = open(L + p + '.html', encoding='utf-8').read(); self.es = []

    def rep(self, old, new, note, ctx=30):
        """Replace the unique occurrence of `old` (grow context until unique)."""
        i = self.t.find(old); assert i >= 0, (self.p, note, old[:60])
        a, b = i, i + len(old)
        while self.t.count(self.t[a:b]) != 1:
            a = max(0, a - ctx); b = min(len(self.t), b + ctx)
        o = self.t[a:b]; n = o[:i - a] + new + o[i - a + len(old):]
        self.t = self.t[:a] + n + self.t[b:]
        self.es.append({'old': o, 'new': n, 'count': 1, 'note': note})

    def rep_at(self, start, end, new, note):
        old = self.t[start:end]
        # anchor on enough context to be unique
        a, b = start, end
        while self.t.count(self.t[a:b]) != 1:
            a = max(0, a - 30); b = min(len(self.t), b + 10)
        o = self.t[a:b]; n = o[:start - a] + new + o[end - a:]
        self.t = self.t[:a] + n + self.t[b:]
        self.es.append({'old': o, 'new': n, 'count': 1, 'note': note})


def captions(t):
    return list(CAP.finditer(t))


def is_ref_para(t, m):
    """A <p> that starts 'Figure \\(\\PageIndex{n}\\) shows ...' is a reference, not a caption."""
    return not m.group(1).startswith('<figcaption') and not re.match(r'\s*[:]', t[m.end():m.end() + 2])


def renumber_hard(pg, sec, start_after):
    k = start_after
    for _ in range(50):
        ms = [m for m in captions(pg.t) if m.group(6) and not is_ref_para(pg.t, m)]
        ms = [m for m in ms if f'{m.group(4)}.{m.group(5)}' == sec]
        todo = [m for m in ms if not getattr(pg, 'done', set()).__contains__(m.start())]
        break
    new_map = {}
    hard = [m for m in captions(pg.t) if m.group(6) and not is_ref_para(pg.t, m) and f'{m.group(4)}.{m.group(5)}' == sec]
    # process from the end so earlier offsets stay valid
    labels = [(m.start(2), m.end(2), m.group(2)) for m in hard]
    targets = []
    for s, e, lab in labels:
        k += 1; targets.append((s, e, lab, f'{sec}.{k}'))
    for s, e, lab, nl in reversed(targets):
        if lab != nl:
            pg.rep_at(s, e, nl, f'caption {lab} -> {nl}')
        new_map[lab] = nl
    return new_map


titles = dict(re.findall(r'\[(\d+)\]\([^)]*\) \| ([^|\n]+?) \|', open('pages/LIVE_SNAPSHOT.md').read()))
hard_maps = {}

for p, v in scan.items():
    sec = v['sec']; pg = Page(p)
    if p == '597059':  # 1.6: caption the ethyne image as Figure 3
        pg.rep('<p class="para mt-align-center"><strong>Ethyne</strong></p>',
               '<p class="para mt-align-center"><strong>Figure \\(\\PageIndex{3}\\):</strong> Ethyne (acetylene), the simplest alkyne.</p>', '1.6 caption ethyne as Figure 3')
    if p == '597105':  # 5.4: source figures 2,3,4 -> 1,2,3
        for a, b in (('2', '1'), ('3', '2'), ('4', '3')):
            while 'Figure \\(\\PageIndex{%s}\\)' % a in pg.t:
                pg.rep('Figure \\(\\PageIndex{%s}\\)' % a, 'Figure \\(\\PageIndex{%s}\\)' % b, f'5.4 source figure {a} -> {b}')
    if p == '597144':  # 9.1: source figure 2 -> 1
        for a in ('2a', '2b', '2'):
            while 'Figure \\(\\PageIndex{%s}\\)' % a in pg.t:
                pg.rep('Figure \\(\\PageIndex{%s}\\)' % a, 'Figure \\(\\PageIndex{%s}\\)' % a.replace('2', '1'), f'9.1 source figure {a} -> {a.replace("2", "1")}')
    pis = [int(n) for n in re.findall(r'Figure \\\(\\PageIndex\{(\d+)[a-z]?\}\\\)', pg.t)]
    if v['two']:
        # Chapter Guide: two-part -> three-part, in page order, continuing after any \PageIndex captions
        chap = sec.split('.')[0]; k = max(pis or [0])
        two = [m for m in captions(pg.t) if m.group(4) and not m.group(6) and m.group(4) == chap and not is_ref_para(pg.t, m)]
        tg = []
        for m in two:
            k += 1; tg.append((m.start(2), m.end(2), m.group(2), f'{sec}.{k}'))
        for s, e, lab, nl in reversed(tg):
            pg.rep_at(s, e, nl, f'guide caption {lab} -> {nl}')
            hard_maps.setdefault(p, {})[lab] = nl
    else:
        m = renumber_hard(pg, sec, max(pis or [0]))
        hard_maps[p] = m
    if pg.es:
        edits[p] = pg.es; open(TMP + '_c1_' + p, 'w').write(pg.t)

# cross-references that follow the renumbered lecture figures
XREF = [('597136', 'shown in Figure 8.3.1. Notice', 'shown in Figure 8.3.3. Notice'),
        ('597136', 'also shown in Figure 8.3.1, is', 'also shown in Figure 8.3.3, is'),
        ('597175', 'name nucleotides as in Figure 12.1.3:', 'name nucleotides as in Figure 12.1.6:')]
for p, a, b in XREF:
    t = open(TMP + '_c1_' + p).read() if p in edits else open(L + p + '.html').read()
    assert t.count(a) == 1, (p, a)
    edits.setdefault(p, []).append({'old': a, 'new': b, 'count': 1, 'note': 'cross-reference follows renumbered figure'})

# replay check against pages/live
bad = 0
for p, es in edits.items():
    t = open(L + p + '.html', encoding='utf-8').read()
    for x in es:
        if t.count(x['old']) != 1: bad += 1; print('REPLAY FAIL', p, x['note'])
        t = t.replace(x['old'], x['new'])
json.dump(edits, open('tools/batchC1_fignum_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
json.dump(hard_maps, open('tools/batchC1_label_map_2026-11-12.json', 'w'), indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'replay failures')
for p, m in hard_maps.items():
    ch = {a: b for a, b in m.items() if a != b}
    if ch: print(p, ch)
