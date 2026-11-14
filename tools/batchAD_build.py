"""Batch AD (2026-11-13): tables on phones.
LibreTexts styles tables with class mt-responsive-table; below 37.49em (600 px) it hides every <th> and stacks the
cells into one column with an empty blue label strip (its data-th labels do not render), so on a phone every table
lost its column headers. This adds one phone-only style block per page that puts the table back as a real grid
(header row shown); a table wider than the screen scrolls sideways inside itself. Desktop and print are untouched
(the rule is inside "@media screen and (max-width: 600px)"). The Glossary page (488232) is left alone: LibreTexts
builds it differently. The style block goes just before the first table, never inside a <p>.
Output: tools/batchAD_2026-11-13.json, tools/batchAD_sha_2026-11-13.json, audit/preview/<id>.html"""
import json, hashlib, re, glob, os
T = '.mt-content-container table.mt-responsive-table'
CSS = ('@media screen and (max-width: 600px) { '
       f'{T} {{ display: block !important; overflow-x: auto; -webkit-overflow-scrolling: touch; max-width: 100%; min-width: 0 !important; border-collapse: collapse; }} '
       f'{T} > caption {{ display: block; }} '
       f'{T} thead {{ display: table-header-group !important; }} '
       f'{T} tbody {{ display: table-row-group !important; }} '
       f'{T} tr {{ display: table-row !important; }} '
       f'{T} col {{ display: table-column !important; }} '
       f'{T} th, {T} td {{ display: table-cell !important; padding: 0.4em 0.5em !important; background-image: none !important; min-width: 6em; vertical-align: top; }} '
       f'{T} th::before, {T} td::before {{ content: none !important; display: none !important; }} }}')
STYLE = '<style type="text/css">/*<![CDATA[*/' + CSS + '/*]]>*/</style>'
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
edits, sha, skipped = {}, {}, []
for pf in sorted(glob.glob('pages/live/*.html')):
    p = os.path.basename(pf)[:-5]
    if p == '488232': continue
    t = open(pf, encoding='utf-8').read()
    m = re.search(r'<table\b[^>]*class="[^"]*mt-responsive-table', t)
    if not m: continue
    i = m.start()
    # not inside an open <p>
    o = max(t.rfind('<p>', 0, i), t.rfind('<p ', 0, i)); c = t.rfind('</p>', 0, i)
    if o > c: skipped.append((p, 'table inside <p>')); continue
    k = 80
    while t.count(t[i:i + k]) > 1 or t.count(t[max(0, i - k):i + 80]) > 1:
        k += 80
        if k > 4000: raise SystemExit('no unique anchor ' + p)
    old = t[max(0, i - k):i + 80]; pre = t[max(0, i - k):i]
    assert t.count(old) == 1, p
    n = t[:i] + STYLE + t[i:]
    edits[p] = [{'old': old, 'new': pre + STYLE + old[len(pre):], 'count': 1, 'note': 'phone: tables keep their header row and scroll sideways if wider than the screen'}]
    sha[p] = {'before': h(t), 'after': h(n)}
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(n)
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAD_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAD_sha_2026-11-13.json', 'w'))
print(len(edits), 'pages; skipped', skipped)
