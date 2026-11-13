"""Batch K (optional work, review 2026-11-12): concept maps reprinted larger (cache-bust edits only; the SVGs are on
GitHub Pages), 7 structure figures (tools/batchK2_figs_2026-11-13.json) and 8 schematic figures
(tools/batchK1_figs_2026-11-13.json, generator tools/batchK1_figs.py). Replays every edit against pages/live.
Output: tools/batchK_2026-11-13.json {uploads, edits}"""
import json

L = 'pages/live/'
pages, edits, uploads = {}, {}, []


def apply(p, x):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read()
    n = x.get('count', 1); assert pages[p].count(x['old']) == n, (p, x['note'], pages[p].count(x['old']))
    pages[p] = pages[p].replace(x['old'], x['new'])
    edits.setdefault(p, []).append({'old': x['old'], 'new': x['new'], 'count': n, 'note': x['note']})


for p, es in json.load(open('tools/batchK_maps_2026-11-13.json')).items():
    for x in es: apply(p, x)
for fn in ('tools/batchK2_figs_2026-11-13.json', 'tools/batchK1_figs_2026-11-13.json'):
    d = json.load(open(fn)); uploads += d['uploads']
    for p, es in d['edits'].items():
        for x in es: apply(p, x)
keys = [u['key'] for u in uploads]; assert len(set(keys)) == len(keys)
for u in uploads: open(u['path']).close(); assert any('{{' + u['key'] + '}}' in pages[u['page']] for _ in [0]), u
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchK_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
