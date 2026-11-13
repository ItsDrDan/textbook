"""Batch C6 (review 2026-11-12): Index (488231) entries that disagree with the Glossary (488232), and six glossary
links retargeted to the section where the term is taught. Output: tools/batchC6_index_2026-11-12.json"""
import json, re, html
L = 'pages/live/'
snap = open('pages/LIVE_SNAPSHOT.md').read()
sec2pid = {t.split(':')[0].strip(): p for p, t in re.findall(r'\[(\d+)\]\([^)]*\) \| ([^|\n]+?) \|', snap) if re.match(r'\d+\.\d+:', t)}
g = open(L + '488232.html').read(); ix = open(L + '488231.html').read()
edits = {'488231': [], '488232': []}
# 1. six glossary links to better targets (medium confidence in the review; term counts confirm)
RETARGET = {'amide': ('7.3', '7.4'), 'reduction': ('4.4', '5.4'), 'intermolecular forces': ('1.5', '1.8'),
            'glycol': ('4.2', '4.6'), 'transfer RNA': ('12.3', '12.5'), 'complementary base pairs': ('1.8', '12.2')}
for row in re.findall(r'<tr>.*?</tr>', g, re.S):
    w = re.search(r'data-th="Word\(s\)">(.*?)</td>', row, re.S)
    if not w: continue
    first = re.split(r',\s*', html.unescape(re.sub(r'<[^>]+>', '', w.group(1))).strip())[0]
    if first in RETARGET:
        a, b = RETARGET[first]
        old_link = f'<a href="/@go/page/{sec2pid[a]}">Section {a}</a>'
        if old_link in row:
            new_row = row.replace(old_link, f'<a href="/@go/page/{sec2pid[b]}">Section {b}</a>')
            assert g.count(row) == 1
            edits['488232'].append({'old': row, 'new': new_row, 'count': 1, 'note': f'glossary {first}: {a} -> {b}'})
# 2. glossary map (after retargets) and index fixes
gl = {}
for e in edits['488232']: g = g.replace(e['old'], e['new'])
for row in re.findall(r'<tr>.*?</tr>', g, re.S):
    w = re.search(r'data-th="Word\(s\)">(.*?)</td>', row, re.S); l = re.search(r'Section (\d+\.\d+)', row)
    if w and l:
        for term in re.split(r',\s*', html.unescape(re.sub(r'<[^>]+>', '', w.group(1))).strip()):
            gl[term.lower()] = l.group(1)
for li, term, s in re.findall(r'(<li>([^<]*?), (\d+\.\d+)</li>)', ix):
    t = html.unescape(term).strip().lower()
    if t in gl and gl[t] != s:
        assert ix.count(li) == 1
        edits['488231'].append({'old': li, 'new': li.replace(f', {s}</li>', f', {gl[t]}</li>'), 'count': 1, 'note': f'index {t}: {s} -> {gl[t]}'})
json.dump(edits, open('tools/batchC6_index_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
for p, es in edits.items():
    for e in es: print(p, e['note'])
print(sum(len(v) for v in edits.values()), 'edits')
