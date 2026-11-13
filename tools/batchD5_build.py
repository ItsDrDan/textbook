"""Batch D5 (review 2026-11-12): print layout leftovers.
1. Six exercise boxes print their heading as "1.1.2Exerc": they use a <header><h5 class="editable"> form.
   Convert them to the standard form used by every other box (<h5 class="box-legend editable"> inside the
   box's mt-section div, closed at the end of the box).
2. 1.7 "Four ways to draw the same molecule" table runs off the right margin: shrink the three structure
   images (the width attribute is the print maximum).
3. Table 11.1.2 runs off the right margin: the reaction image (976 px wide) has no width; give it width 440.
4. Chapter-guide "Show a drawn example" panels: the bold reaction label can be stranded at a page foot.
   Add page-break-after:avoid / break-after:avoid to the label paragraph (inline styles reach the PDF).
Output: tools/batchD5_fixes_2026-11-12.json {page:[{old,new,count,note}]}, replay-checked.
"""
import json, re, glob

L = 'pages/live/'
pages, edits = {}, {}


def T(p):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read()
    return pages[p]


def rep(p, old, new, note, n=1):
    t = T(p); c = t.count(old)
    assert c == n, (p, note, c)
    pages[p] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


# 1. exercise boxes
BOX = re.compile(r'<section class="box-exercise">\s*<header>\s*(<span id="[^"]*"></span>)<div class="mt-section"><h5 class="editable">(.*?)</h5>\s*</div></header>(.*?)</section>', re.S)
for f in sorted(glob.glob(L + '*.html')):
    p = f.split('/')[-1][:-5]
    for m in list(BOX.finditer(T(p))):
        assert '<section' not in m.group(3)
        new = f'<section class="box-exercise">\n{m.group(1)}<div class="mt-section"><h5 class="box-legend editable">{m.group(2)}</h5>{m.group(3)}</div></section>'
        rep(p, m.group(0), new, f'exercise box heading form ({m.group(2)})')

# 2. 1.7 table
t = T('597060'); a = t.find('<table class="mt-responsive-table"><caption>Four ways to draw the same molecule'); b = t.find('</table>', a)
seg = t[a:b]
new = seg.replace('width="218" style="max-width:100%;height:auto;" src="/@api/deki/files/512418/', 'width="160" style="max-width:100%;height:auto;" src="/@api/deki/files/512418/')
new = new.replace('width="218" style="max-width:100%;height:auto;" src="/@api/deki/files/512419/', 'width="160" style="max-width:100%;height:auto;" src="/@api/deki/files/512419/')
new = new.replace('width="141" style="max-width:100%;height:auto;" src="/@api/deki/files/512420/', 'width="104" style="max-width:100%;height:auto;" src="/@api/deki/files/512420/')
assert new.count('width="160"') == 2 and 'width="104"' in new
rep('597060', seg, new, '1.7 Four ways table: smaller structure images so all four columns fit in print')

# 3. Table 11.1.2
rep('597166', 'class="internal" src="/@api/deki/files/25927/Table.jpg" fileid="25927" />',
    'class="internal" width="440" style="max-width:100%;height:auto;" src="/@api/deki/files/25927/Table.jpg" fileid="25927" />', 'Table 11.1.2 reaction image width')

# 4. drawn-example labels
for f in sorted(glob.glob(L + '*.html')):
    p = f.split('/')[-1][:-5]; c = T(p).count('<p style="margin:.8em 0 .2em"><strong>')
    if c: rep(p, '<p style="margin:.8em 0 .2em"><strong>', '<p style="margin:.8em 0 .2em;page-break-after:avoid;break-after:avoid"><strong>', 'drawn-example label stays with its drawing', c)

bad = 0
for p, es in edits.items():
    t = open(L + p + '.html', encoding='utf-8').read()
    for x in es:
        if t.count(x['old']) != x['count']: bad += 1; print('REPLAY FAIL', p, x['note'])
        t = t.replace(x['old'], x['new'])
json.dump(edits, open('tools/batchD5_fixes_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'replay failures')
