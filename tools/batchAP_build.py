"""Batch AP (2026-11-18): P1 + P2 fixes from the source and science-verification audit
(audit/source-audit-2026-11-18/SUMMARY.md). Each claim corrected and/or given a verified source.
Drafts per chapter group in tools/batchAP_parts/fix_t*.py (each defines its own e(); here it is replaced by ours).
Output: tools/batchAP_2026-11-18.json, tools/batchAP_sha_2026-11-18.json, audit/preview/<id>.html"""
import json, hashlib, re
pages, edits, order = {}, {}, []


def e(p, old, new, note, why, count=1):
    p = str(p)
    if p not in pages:
        pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
        order.append(p)
    t = pages[p][1]
    assert t.count(old) == count, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': count, 'note': note, 'why': why})


for f in ['fix_t1_front_ch1-3.py', 'fix_t2_ch4-6.py', 'fix_t3_ch7-9.py', 'fix_t4_ch10-12.py', 'fix_t5_ch13-15.py']:
    src = open('tools/batchAP_parts/' + f, encoding='utf-8').read()
    src = re.sub(r'^def e\(', 'def _their_e(', src, flags=re.M)
    if f.startswith('fix_t4'):  # drop its own self-check and file-writing tail (it checks its private copy)
        src = src[:src.index("\nassert 'truthout'")]
    exec(compile(src, f, 'exec'), {'e': e, '__name__': 'batchAP', '__file__': '/dev/null/' + f})

# 8.3 repeats the aspartame figure corrected in 10.6 (t4 left it for the chapter owner)
e('597136', 'about 180 times', 'about 200 times', '8.3 aspartame sweetness, same as 10.6',
  'MedlinePlus (cited in 10.6): aspartame is about 200 times sweeter than sugar.')

h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAP_2026-11-18.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAP_sha_2026-11-18.json', 'w'))
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
