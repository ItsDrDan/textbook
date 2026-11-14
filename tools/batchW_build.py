"""Batch W (2026-11-13): phone version of Figure 12.6.4, shown only on narrow screens. One-page test.
The wide <img> is unchanged apart from a class; a second <img> (stacked panels, GitHub-hosted) follows it.
A screen-only media query swaps them below 600 px, so desktop and print keep the wide figure.
Output: tools/batchW_2026-11-13.json, tools/batchW_sha_2026-11-13.json, audit/preview/597179.html"""
import json, hashlib, re
p = '597179'; t = open('pages/live/%s.html' % p, encoding='utf-8').read()
m = re.search(r'<img class="internal" alt="([^"]*)" width="760" style="max-width:100%;height:auto;" src="/@api/deki/files/512767/fig-p597179-elongation\.svg" fileid="512767" />', t)
assert m and t.count(m.group(0)) == 1
old = m.group(0)
STYLE = '<style type="text/css">/*<![CDATA[*/.fig-phone { display: none; } @media screen and (max-width: 600px) { .fig-wide { display: none !important; } .fig-phone { display: block !important; margin: 0 auto; } }/*]]>*/</style>'
new = (STYLE + old.replace('class="internal"', 'class="internal fig-wide"') +
       '<img class="fig-phone" alt="%s" width="340" style="max-width:100%%;height:auto;" src="https://itsdrdan.github.io/textbook/figures/phone/fig-p597179-elongation-phone.svg?v=20261113w" />' % m.group(1))
n = t.replace(old, new)
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
json.dump({'uploads': [], 'edits': {p: [{'old': old, 'new': new, 'count': 1, 'note': '12.6 Figure 4: stacked phone version shown below 600 px; wide figure unchanged on desktop and in print'}]}}, open('tools/batchW_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
json.dump({p: {'before': h(t), 'after': h(n)}}, open('tools/batchW_sha_2026-11-13.json', 'w'))
open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(n)
print('1 edit')
