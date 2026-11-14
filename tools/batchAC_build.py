"""Batch AC (2026-11-13): last phone fixes from the final walkthrough.
  1. Three figures inside links (6.6 ester boiling points, 15.6 fatty acid synthesis, 15.11 nonessential amino acids)
     printed ~5-6 px labels on phones; the batch Z side-scroll box now wraps the link (the link itself is unchanged).
  2. Wide reaction equations on 13.1, 13.5 and 14.4 made the whole page slide sideways on phones; on screens under
     600 px a paragraph that holds MathJax now scrolls sideways inside itself instead.
  3. 12.6 genetic code table: LibreTexts' mt-responsive-table style collapsed it to one column on phones and hid the
     base labels; the class is dropped and the full grid scrolls sideways on phones. (Every rule of that class
     except a min-width sits inside a phone-width media query, so desktop and print are unchanged.)
All new rules are inside "@media screen and (max-width: 600px)"; style blocks sit just before the element they serve,
never inside a <p>. The hint line carries inline display:none (batch Z2 lesson).
Output: tools/batchAC_2026-11-13.json, tools/batchAC_sha_2026-11-13.json, audit/preview/<id>.html"""
import json, hashlib, re
WS = list(range(480, 1021, 60))
ZSTYLE = ('<style type="text/css">/*<![CDATA[*/.fig-scroll-hint { display: none !important; } @media screen and (max-width: 600px) { '
          'figure > * { min-width: 0; max-width: 100%; } '
          '.fig-scroll { display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; width: 100%; max-width: min(100%, calc(100vw - 20px)); min-width: 0; } '
          '.fig-scroll img { max-width: none !important; } ' + ' '.join('.fig-scroll img.fig-w%d { width: %dpx !important; }' % (w, w) for w in WS) +
          ' .fig-scroll-hint { display: block !important; font-size: 0.8em; color: #5a6478; margin: 0 0 4px; } }/*]]>*/</style>')
EQSTYLE = ('<style type="text/css">/*<![CDATA[*/@media screen and (max-width: 600px) { '
           '.mt-content-container p:has(> mjx-container) { overflow-x: auto; overflow-y: hidden; -webkit-overflow-scrolling: touch; max-width: 100%; padding-bottom: 2px; } }/*]]>*/</style>')
TSTYLE = ('<style type="text/css">/*<![CDATA[*/@media screen and (max-width: 600px) { '
          '.codon-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; max-width: 100%; } .codon-scroll table { min-width: 520px; } }/*]]>*/</style>')
HINT = '<span class="fig-scroll-hint" style="display:none">Swipe sideways to see the whole figure.</span>'
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
pages, edits = {}, {}
def page(p):
    if p not in pages: pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
    return pages[p][1]
def e(p, old, new, note):
    t = page(p); assert t.count(old) == 1, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})

# 1. linked figures
for p, key, w in (('597114', 'ester_bp', 660), ('597214', 'fa_synthesis', 720), ('597217', 'nonessential_aa', 660)):
    t = page(p)
    m = re.search(r'<figure class="figure" style="margin:1em 0">(<a\b[^>]*href="[^"]*%s\.svg"[^>]*>.*?</a>)' % key, t, flags=re.S)
    a = m.group(1); old = m.group(0)
    a2 = re.sub(r'<img\b', '<img class="fig-w%d"' % w, a)
    assert 'class="fig-w' in a2 and a2.count('<img') == a.count('<img')
    new = ZSTYLE + '<figure class="figure" style="margin:1em 0">' + HINT + '<div class="fig-scroll">' + a2 + '</div>'
    e(p, old, new, 'phone side-scroll around the linked %s figure at %d px' % (key, w))

# 2. wide equations
for p in ('597188', '597193', '597203'):
    t = page(p)
    m = re.search(r'<p class="mt-align-center">\s*\\\(', t)
    i = m.start(); old = t[i:i + 60]
    e(p, old, EQSTYLE + old, 'phone: paragraphs holding equations scroll sideways inside themselves (style before the first centered equation)')

# 3. codon table
t = page('597179')
old = '<table class="mt-responsive-table" style="text-align:center">'
j = t.index(old); k = t.index('</table>', j) + len('</table>')
tbl = t[j:k]
new = TSTYLE + '<div class="codon-scroll">' + tbl.replace(old, '<table class="codon-table" style="text-align:center">') + '</div>'
e('597179', tbl, new, '12.6 genetic code table: drop mt-responsive-table (phone collapse), full grid scrolls sideways on phones')

sha = {p: {'before': h(v[0]), 'after': h(v[1])} for p, v in pages.items()}
for p, v in pages.items(): open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(v[1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAC_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAC_sha_2026-11-13.json', 'w'))
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
for p in edits:
    n = pages[p][1]; print(p, 'styles', n.count('<style'), 'style inside <p>?', bool(re.search(r'<p\b[^>]*>(?:(?!</p>).)*<style', n, flags=re.S)))
