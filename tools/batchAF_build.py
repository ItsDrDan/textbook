"""Batch AF (2026-11-14): book-wide sweep at 375 px (all 199 pages) found one page still sliding sideways:
10.8, the disulfide-formation equation. Same rule as batches AC/AE (a paragraph holding MathJax scrolls inside
itself on phones). Style block placed just before the first centered equation paragraph, never inside a <p>.
Output: tools/batchAF_2026-11-14.json, tools/batchAF_sha_2026-11-14.json, audit/preview/597161.html"""
import json, hashlib, re
EQ = ('<style type="text/css">/*<![CDATA[*/@media screen and (max-width: 600px) { '
      '.mt-content-container p:has(> mjx-container) { overflow-x: auto; overflow-y: hidden; -webkit-overflow-scrolling: touch; max-width: 100%; padding-bottom: 2px; } }/*]]>*/</style>')
p = '597161'; t = open('pages/live/%s.html' % p, encoding='utf-8').read()
m = re.search(r'<p class="mt-align-center">\s*\\[\(\[]', t); i = m.start()
k = 60
while t.count(t[max(0, i - k):i + 60]) > 1: k += 60
old = t[max(0, i - k):i + 60]; pre = t[max(0, i - k):i]
new = pre + EQ + old[len(pre):]; n = t.replace(old, new)
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
json.dump({'uploads': [], 'edits': {p: [{'old': old, 'new': new, 'count': 1, 'note': 'phone: equation paragraphs scroll sideways inside themselves'}]}}, open('tools/batchAF_2026-11-14.json', 'w'), ensure_ascii=False, indent=1)
json.dump({p: {'before': h(t), 'after': h(n)}}, open('tools/batchAF_sha_2026-11-14.json', 'w'))
open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(n)
print('1 edit; first centered equation:', repr(t[i:i+90]))
