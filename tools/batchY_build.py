"""Batch Y (2026-11-13): side-scroll on phones for a wide flow diagram that cannot be stacked. One-page test (14.5).
The <img> is wrapped in <div class="fig-scroll">; below 600 px the image keeps a readable width and the box scrolls
sideways, with a one-line hint. Desktop and print are untouched (the rule is screen-only and width-limited).
Output: tools/batchY_2026-11-13.json, tools/batchY_sha_2026-11-13.json, audit/preview/597204.html"""
import json, hashlib, re
p = '597204'; t = open('pages/live/%s.html' % p, encoding='utf-8').read()
tags = [m.group(0) for m in re.finditer(r'<img\b[^>]*>', t) if 'fig-p597204-yield-flow.svg' in m.group(0)]
assert len(tags) == 1 and t.count(tags[0]) == 1
old = tags[0]
STYLE = ('<style type="text/css">/*<![CDATA[*/.fig-scroll-hint { display: none !important; } @media screen and (max-width: 600px) { '
         '.fig-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; width: 100%; max-width: 100%; min-width: 0; } '
         '.fig-scroll img { max-width: none !important; } .fig-scroll img.fig-w860 { width: 860px !important; } '
         '.fig-scroll-hint { display: block !important; font-size: 0.8em; color: #5a6478; margin: 0 0 4px; } }/*]]>*/</style>')
# first try (commit 09e8120) lacked the width limits and !important: LibreTexts lays <figure> out as a flex box, so the
# scroll box grew to the image width, and a platform rule for <p> outranked the hidden hint.
new = (STYLE + '<p class="fig-scroll-hint">Swipe sideways to see the whole figure.</p><div class="fig-scroll">' +
       old.replace('class="internal"', 'class="internal fig-w860"') + '</div>')
assert 'fig-w860' in new
n = t.replace(old, new)
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
json.dump({'uploads': [], 'edits': {p: [{'old': old, 'new': new, 'count': 1, 'note': '14.5 Figure 1: side-scroll at a readable size below 600 px, with a hint; desktop and print unchanged'}]}}, open('tools/batchY_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
json.dump({p: {'before': h(t), 'after': h(n)}}, open('tools/batchY_sha_2026-11-13.json', 'w'))
open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(n)
print('1 edit')
