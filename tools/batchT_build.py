"""Batch T (2026-11-13). DRAFT ONLY until the instructor says "publish". Count-checked against pages/live.
Parts:
  A  duplicated prose trimmed on 14.2, 14.4, 15.4, 15.5 and conflicts fixed on 15.6   (audit/edits/t_prose.json)
  B  figures whose labels printed under 6 pt: cache-bust for the GitHub-hosted files      (audit/edits/t_figures.json)
     (the LibreTexts-hosted files are uploads: tools/batchT_uploads_2026-11-13.json)
  C  Try It selections on the twelve thin sections, now including their five new questions (audit/edits/t_widgets.json)
Output: tools/batchT_2026-11-13.json {uploads, edits}, tools/batchT_sha_2026-11-13.json, audit/preview/<id>.html"""
import json, hashlib, os
L = 'pages/live/'
pages, edits, orig, skipped = {}, {}, {}, []
def page(p):
    p = str(p)
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read(); orig[p] = pages[p]
    return pages[p]
def e(p, old, new, note, n=1):
    p = str(p); t = page(p)
    if t.count(old) != n or old == new: skipped.append((p, note[:70], t.count(old))); return
    pages[p] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})
for pid, d in json.load(open('audit/edits/t_prose.json', encoding='utf-8'))['pages'].items():
    for x in d['edits']:
        if x.get('skip'): continue
        e(pid, x['old'], x['new'], 'A %s (%s): %s' % (x.get('section', ''), x['kind'], x['idea'][:150]))
for x in json.load(open('audit/edits/t_figures.json')):
    e(x['page_id'], x['old'], x['new'], 'B ' + x['note'], n=x['count'])
for x in json.load(open('audit/edits/t_widgets.json')):
    e(x['page_id'], x['old'], x['new'], 'C ' + x['note'], n=x['count'])
uploads = json.load(open('tools/batchT_uploads_2026-11-13.json'))
sha = {p: {'before': hashlib.sha256(orig[p].encode()).hexdigest(), 'after': hashlib.sha256(pages[p].encode()).hexdigest()} for p in edits}
json.dump(sha, open('tools/batchT_sha_2026-11-13.json', 'w'), indent=0)
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchT_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
os.makedirs('audit/preview', exist_ok=True)
for f in os.listdir('audit/preview'): os.remove('audit/preview/' + f)
for p in edits: open(f'audit/preview/{p}.html', 'w', encoding='utf-8').write(pages[p])
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages'); print('skipped:', skipped)
