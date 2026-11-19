"""Batch AQ (2026-11-18): P3 polish from the source and science-verification audit
(audit/source-audit-2026-11-18/SUMMARY.md). Each claim corrected and/or given a verified source.
Drafts per chapter group in tools/batchAQ_parts/fixp3_t*.py (each defines its own e(); here it is replaced by ours).
Output: tools/batchAQ_2026-11-18.json, tools/batchAQ_sha_2026-11-18.json, audit/preview/<id>.html"""
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


for f in ['fixp3_t1_front_ch1-3.py', 'fixp3_t2_ch4-6.py', 'fixp3_t3_ch7-9.py', 'fixp3_t4_ch10-12.py', 'fixp3_t5_ch13-15.py']:
    src = open('tools/batchAQ_parts/' + f, encoding='utf-8').read()
    src = re.sub(r'^def e\(', 'def _their_e(', src, flags=re.M)
    exec(compile(src, f, 'exec'), {'e': e, '__name__': 'batchAP', '__file__': '/dev/null/' + f})

# 9.2: point the Dietary Guidelines citation (batch AP) at the PDF itself, as 1.6 now does
e('597145', 'href="https://www.dietaryguidelines.gov/"', 'href="https://www.realfood.gov/documents/DGA.pdf"',
  '9.2 Dietary Guidelines link to the PDF', 'Verified 2026-11-18: realfood.gov/documents/DGA.pdf p. 4 "saturated fat consumption should not exceed 10% of total daily calories".')

h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAQ_2026-11-18.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAQ_sha_2026-11-18.json', 'w'))
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
