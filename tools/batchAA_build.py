"""Batch AA (2026-11-13): cache-busts for the figures whose circled P / CoQ were enlarged (21:39 compile leftovers).
Output: tools/batchAA_2026-11-13.json, tools/batchAA_sha_2026-11-13.json, audit/preview/<id>.html"""
import json, hashlib, re, glob, os
FILES = ['figures/pathways/glycolysis/step4.svg', 'figures/pathways/cac/step5.svg', 'figures/pathways/urea/step1.svg',
         'figures/print/atp_synthase-v3-1.svg', 'figures/print/atp_synthase-v3-2.svg', 'figures/pathways/etc/etc_inner.svg']
V = '20261113aa'
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
edits, sha = {}, {}
for pf in sorted(glob.glob('pages/live/*.html')):
    pid = os.path.basename(pf)[:-5]; t = open(pf, encoding='utf-8').read(); n = t; es = []
    for f in FILES:
        url = 'https://itsdrdan.github.io/textbook/' + f
        for m in sorted(set(re.findall(re.escape(url) + r'(?:\?v=[0-9a-z]+)?"', n))):
            new = url + '?v=' + V + '"'
            if m == new: continue
            c = n.count(m); n = n.replace(m, new); es.append({'old': m, 'new': new, 'count': c, 'note': 'cache-bust: ' + f.split('/')[-2] + '/' + f.split('/')[-1]})
    if es:
        edits[pid] = es; sha[pid] = {'before': h(t), 'after': h(n)}
        open('audit/preview/%s.html' % pid, 'w', encoding='utf-8').write(n)
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAA_2026-11-13.json', 'w'), indent=1)
json.dump(sha, open('tools/batchAA_sha_2026-11-13.json', 'w'))
for p, es in edits.items(): print(p, [(e['note'][12:], e['count']) for e in es])
