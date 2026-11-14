"""Item-level ledger of every exercise, problem, case question and worked example in the live page snapshot.
Usage: python3 tools/question_ledger.py   -> writes audit/QUESTION-LEDGER.csv and prints a summary.
The cognitive level is assigned from the problem-set heading (a heuristic, stated as such in the ledger), not by reading each item."""
import re, csv, json, html, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INV = json.load(open(f'{ROOT}/audit/inventory.json'))
LEVEL = [(r'Multiple Choice|Matching|True or False', 1, 'recognize'), (r'Short Answer', 2, 'explain'),
         (r'Naming|Classif', 3, 'apply'), (r'Reactions|Exam-Style|Calculat', 3, 'apply'),
         (r'Properties|Analyze|Compare', 2, 'explain/compare'), (r'Find the Error', 4, 'integrate'),
         (r'Cumulative', 4, 'integrate'), (r'Clinical|Integrative|Case|Rosa', 5, 'transfer')]
CLIN = re.compile(r'patient|nurse|nursing|dental|dentist|clinic|blood|dose|drug|diabet|insulin|hospital|medic|Rosa|hygien|respiratory|radiolog', re.I)
txt = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()
rows = []
for r in INV:
    m = re.match(r'(\d+(?:\.\d+)?):\s*(.*)', r['title'])
    if not m: continue
    sec, name = m.group(1), m.group(2)
    h = open(f"{ROOT}/pages/live/{r['id']}.html").read()
    kind = 'practice' if 'Practice Problems' in name else 'guide' if 'Chapter Guide' in name else 'games' if 'Practice Games' in name else 'landing' if '.' not in sec else 'section'
    keyblock = h[h.find('showprint answer-key'):] if 'showprint answer-key' in h else ''
    keylabels = [txt(k) for k in re.findall(r'class="answer-key-item"[^>]*>(.*?)</', keyblock, flags=re.S)]
    # walk headings and boxes in document order
    toks = list(re.finditer(r'<h([2-4])[^>]*>(.*?)</h\1>|<(?:div|section) class="(box-exercise|box-example)[^"]*">', h, flags=re.S))
    head = ''
    n_in_page = collections.Counter()
    for i, t in enumerate(toks):
        if t.group(1):
            ht = txt(t.group(2))
            if not re.match(r'(Example|Exercise|Solution|Answer)', ht): head = ht
            if not re.match(r'(Example|Exercise)', ht): continue
            continue
        end = toks[i + 1].start() if i + 1 < len(toks) else len(h)
        # a box ends at the next box/heading; trim at the print key
        body = h[t.start():end]
        if 'showprint answer-key' in body: body = body[:body.find('showprint answer-key')]
        typ = 'example' if t.group(3) == 'box-example' else 'exercise'
        tm = re.search(r'class="boxtitle"[^>]*>(.*?)</p>|class="box-legend[^"]*"[^>]*>(.*?)</|<h[45][^>]*>(.*?)</h[45]>', body, flags=re.S)
        title = txt(next((g for g in (tm.groups() if tm else []) if g), '')) or typ.title()
        title = re.sub(r'\\\(\\PageIndex\{(\d+)\}\\\)', r'\1', title)
        n_in_page[typ] += 1
        ans = re.findall(r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>', body, flags=re.S)
        ans = [a for a in ans if re.match(r'\s*(Answer|Solution|Show answer|Check)', txt(a[0]))]
        sol = bool(re.search(r'>Solution<|Solution:|<strong>Solution', body)) or bool(ans)
        atext = ' '.join(txt(a[1]) for a in ans)
        lvl, lname = next(((l, n) for p, l, n in LEVEL if re.search(p, head + ' ' + title)), (3 if kind == 'section' else 2, 'apply' if kind == 'section' else 'explain'))
        stem = txt(re.sub(r'<details.*?</details>', ' ', body, flags=re.S))
        rows.append(dict(id=f"{sec}|{title}|{n_in_page[typ]}", section=sec, page_id=r['id'], page_kind=kind, type=typ, set_heading=head, title=title,
                         stem=stem[len(title):len(title) + 110].strip(), level=lvl, level_name=lname + ' (by set heading)',
                         has_inline_answer=int(bool(ans) or (typ == 'example' and sol)), answer_words=len(atext.split()),
                         bare_answer=int(bool(ans) and len(atext.split()) < 4), n_parts_answers=len(ans),
                         print_key_on_page=int(bool(keyblock)), figure_dependent=int('<img' in body or 'shown' in stem[:400].lower() and '<img' in body),
                         has_tryit_widget=int('practice.html' in body), review_pointer=int(bool(re.search(r'Review: Section|\(Section', atext))),
                         clinical=int(bool(CLIN.search(stem))), objectives='; '.join(r['objectives_cor']), outline='; '.join(r['outline_units'])))
os.makedirs(f'{ROOT}/audit', exist_ok=True)
with open(f'{ROOT}/audit/QUESTION-LEDGER.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
C = collections.Counter
print('items', len(rows), C(r['type'] for r in rows), C(r['page_kind'] for r in rows))
print('levels', sorted(C(r['level'] for r in rows if r['type'] == 'exercise').items()))
noans = [r for r in rows if r['type'] == 'exercise' and not r['has_inline_answer']]
print('exercises with no answer on the page:', len(noans))
by = collections.defaultdict(list)
for r in noans: by[(r['section'], r['page_id'], r['page_kind'])].append(r['title'])
for k, v in sorted(by.items(), key=lambda kv: [float(x) for x in kv[0][0].split('.')]): print('  ', k, v[:8], len(v))
print('bare answers (<4 words):', sum(r['bare_answer'] for r in rows))
per = collections.defaultdict(C)
for r in rows:
    if r['page_kind'] == 'practice': per[r['section'].split('.')[0]][r['level']] += 1
for ch in sorted(per, key=int): print('ch', ch, dict(sorted(per[ch].items())), 'total', sum(per[ch].values()))
