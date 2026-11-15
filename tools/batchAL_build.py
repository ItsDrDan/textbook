"""Batch AL (2026-11-15): make the "Not loading?" line actually hide in the PDF.
Full (15).pdf: batch AK's QR blocks printed on all 127 boxes (so LibreTexts' print CSS is applied), but the
<div class="hideprint"> around "Not loading?" was hidden on only 35 boxes (Chapter Guide and Practice Problems pages).
Same HTML, so the page's CSS order decides: LibreTexts ships both ".hideprint{display:block!important}" (all media)
and "@media print{.hideprint{display:none!important}}"; when the first comes later it wins. Fix: a more specific print
rule of our own (div.hideprint.dd-noprint), added once per page in the same CDATA <style> form LibreTexts already keeps
on 159 pages, so it wins whatever the order. Screen view unchanged.
Output: tools/batchAL_2026-11-15.json, tools/batchAL_sha_2026-11-15.json, audit/preview/<id>.html"""
import glob, hashlib, json, os

OLD = '<div class="hideprint">\n<p style="font-size:0.9em;">Not loading? '
NEW = '<div class="hideprint dd-noprint">\n<p style="font-size:0.9em;">Not loading? '
STYLE = ('<style type="text/css">/*<![CDATA[*/@media print { .mt-content-container div.hideprint.dd-noprint, '
         'div.hideprint.dd-noprint { display: none !important; visibility: hidden !important; } }/*]]>*/</style>\n')
h = lambda x: hashlib.sha256(x.encode()).hexdigest()
edits, sha, n = {}, {}, 0
for f in sorted(glob.glob('pages/live/*.html')):
    pid = os.path.basename(f)[:-5]
    page = open(f, encoding='utf-8').read()
    k = page.count(OLD)
    if not k:
        continue
    assert 'dd-noprint' not in page
    first = page.find(OLD)
    # one style block, placed just before the first such line; the edit "old" text is made unique by taking
    # everything from the first line's div to the end of its paragraph
    old1 = page[first:page.find('</p>', first) + 4]
    assert page.count(old1) == 1, pid
    es = [{'old': old1, 'new': STYLE + old1.replace(OLD, NEW), 'count': 1, 'note': pid + ': print rule + first line', 'why': 'Author request 2026-11-15 (hide "Not loading?" in print)'}]
    after = page.replace(old1, es[0]['new'])
    if k > 1:
        es.append({'old': OLD, 'new': NEW, 'count': k - 1, 'note': pid + ': other lines', 'why': 'same'})
        after = after.replace(OLD, NEW)
    assert after.count(NEW) == k and after.count(STYLE) == 1
    n += k
    edits[pid] = es
    sha[pid] = {'before': h(page), 'after': h(after)}
    open('audit/preview/%s.html' % pid, 'w', encoding='utf-8').write(after)
# 1.8 H-Bond Lab link box: its link sits inside a sentence; move it to its own hide-in-print line
HB_OLD = (' <a class="hideprint" style="text-decoration:underline" target="_blank" rel="noopener" '
          'href="https://itsdrdan.github.io/IMF/?course=3B&amp;mode=lab&amp;view=lab">Open the H-Bond Lab</a> (opens in a new tab).</p>\n')
HB_NEW = ('</p>\n<div class="hideprint dd-noprint">\n<p><a style="text-decoration:underline" target="_blank" rel="noopener" '
          'href="https://itsdrdan.github.io/IMF/?course=3B&amp;mode=lab&amp;view=lab">Open the H-Bond Lab</a> (opens in a new tab).</p>\n</div>\n')
pid = '597061'
cur = open('audit/preview/%s.html' % pid, encoding='utf-8').read()
assert cur.count(HB_OLD) == 1
edits[pid].append({'old': HB_OLD, 'new': HB_NEW, 'count': 1, 'note': pid + ': H-Bond link to its own hidden-in-print line', 'why': 'same'})
cur = cur.replace(HB_OLD, HB_NEW)
sha[pid]['after'] = h(cur)
open('audit/preview/%s.html' % pid, 'w', encoding='utf-8').write(cur)
n += 1
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAL_2026-11-15.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAL_sha_2026-11-15.json', 'w'))
print(n, 'lines on', len(edits), 'pages')
