"""Batch AE (2026-11-13): the last pages that slid sideways (found while checking batch AD).
  12.1, 14.3, 15.4: wide equations; the batch AC rule (a paragraph holding MathJax scrolls inside itself, phones only).
  3.7: the benzene substitution diagram already sits in an overflow box, but the flex <figure> let that box grow to
       the drawing's width; phone-only rule "figure > * { min-width: 0; max-width: 100% }" (as in batch Z).
  1.7: three long condensed formulas (octane to decane) widen a table past the page even on desktop; the table is
       wrapped in a box that scrolls sideways on screen (print untouched: the rule is "@media screen").
Style blocks sit just before the element they serve, never inside a <p>.
Output: tools/batchAE_2026-11-13.json, tools/batchAE_sha_2026-11-13.json, audit/preview/<id>.html"""
import json, hashlib, re
EQ = ('<style type="text/css">/*<![CDATA[*/@media screen and (max-width: 600px) { '
      '.mt-content-container p:has(> mjx-container) { overflow-x: auto; overflow-y: hidden; -webkit-overflow-scrolling: touch; max-width: 100%; padding-bottom: 2px; } }/*]]>*/</style>')
FIG = ('<style type="text/css">/*<![CDATA[*/@media screen and (max-width: 600px) { .mt-content-container figure > * { min-width: 0; max-width: 100%; } }/*]]>*/</style>')
TBL = ('<style type="text/css">/*<![CDATA[*/@media screen { .tbl-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; max-width: 100%; } }/*]]>*/</style>')
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
pages, edits = {}, {}
def page(p):
    if p not in pages: pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
    return pages[p][1]
def e(p, old, new, note):
    t = page(p); assert t.count(old) == 1, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})
for p in ('597175', '597202', '597209'):
    t = page(p); m = re.search(r'<p class="mt-align-center">\s*\\[\(\[]', t); i = m.start()
    k = 60
    while t.count(t[max(0, i - k):i + 60]) > 1: k += 60
    old = t[max(0, i - k):i + 60]; pre = t[max(0, i - k):i]
    e(p, old, pre + EQ + old[len(pre):], 'phone: equation paragraphs scroll sideways inside themselves')
t = page('597084'); i = t.index('<figure class="figure"><div style="text-align:center;overflow-x:auto">')
old = t[i:i + 90]; e('597084', old, FIG + old, 'phone: the substitution diagram stays inside its own scroll box')
t = page('597060'); n = t.index('CH3CH2CH2CH2CH2CH2CH2CH2CH3'); s = t.rfind('<table', 0, n); f = t.index('</table>', n) + len('</table>')
o = max(t.rfind('<p>', 0, s), t.rfind('<p ', 0, s)); c = t.rfind('</p>', 0, s); assert o < c
tbl = t[s:f]; e('597060', tbl, TBL + '<div class="tbl-scroll">' + tbl + '</div>', 'long condensed formulas: the table scrolls sideways inside its box on screen')
sha = {p: {'before': h(v[0]), 'after': h(v[1])} for p, v in pages.items()}
for p, v in pages.items(): open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(v[1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAE_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAE_sha_2026-11-13.json', 'w'))
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
