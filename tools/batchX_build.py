"""Batch X (2026-11-13): phone versions for the eight wide figures whose panels stack cleanly (same pattern as batch W,
which passed desktop, phone and PDF checks on 12.6). The wide <img> gains class fig-wide; a stacked <img class="fig-phone">
(figures/phone/, built by tools/phone_figs.py) follows it with the same alt text; a screen-only rule swaps them below 600 px.
Output: tools/batchX_2026-11-13.json, tools/batchX_sha_2026-11-13.json, audit/preview/<id>.html"""
import json, hashlib, re
FIGS = [('597056', 'fig-p597056-lewis-errors', 500), ('597111', 'fig-p597111-acid-dimer', 440), ('597140', 'fig-p597140-polysaccharides', 360),
        ('597147', 'myelin_ms', 430), ('597148', 'fig-p597148-rbc-tonicity', 340), ('597203', 'atp_rotation', 336),
        ('597160', 'collagen', 360), ('597169', 'fig-p597169-rate-inhibitors', 380)]
STYLE = '<style type="text/css">/*<![CDATA[*/.fig-phone { display: none; } @media screen and (max-width: 600px) { .fig-wide { display: none !important; } .fig-phone { display: block !important; margin: 0 auto; } }/*]]>*/</style>'
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
edits, sha = {}, {}
for p, name, W in FIGS:
    t = open('pages/live/%s.html' % p, encoding='utf-8').read()
    tags = [m.group(0) for m in re.finditer(r'<img\b[^>]*>', t) if re.search(r'/' + re.escape(name) + r'\.svg', m.group(0))]
    assert len(tags) == 1 and t.count(tags[0]) == 1 and 'fig-wide' not in tags[0], (p, name, len(tags))
    old = tags[0]; alt = re.search(r'alt="([^"]*)"', old).group(1)
    wide = old.replace('class="internal"', 'class="internal fig-wide"') if 'class="' in old else old.replace('<img ', '<img class="fig-wide" ', 1)
    assert 'fig-wide' in wide
    new = ('' if '.fig-phone {' in t else STYLE) + wide + '<img class="fig-phone" alt="%s" width="%d" style="max-width:100%%;height:auto;" src="https://itsdrdan.github.io/textbook/figures/phone/%s-phone.svg?v=20261113x" />' % (alt, W, name)
    n = t.replace(old, new)
    edits[p] = [{'old': old, 'new': new, 'count': 1, 'note': 'phone version of %s shown below 600 px; wide figure unchanged on desktop and in print' % name}]
    sha[p] = {'before': h(t), 'after': h(n)}
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(n)
json.dump({'uploads': [], 'edits': edits}, open('tools/batchX_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchX_sha_2026-11-13.json', 'w'))
print(len(edits), 'pages')
