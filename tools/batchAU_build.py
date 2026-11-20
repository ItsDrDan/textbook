"""Batch AU (2026-11-20): About This Book brought up to date before faculty review.
- "last updated November 14, 2026" -> November 20, 2026.
- New version-history entry for November 18-20: source check (batches AP, AQ, AR, AS) and accessibility check (AT, AT2).
The version number (1.2) is left as is: the author decides whether the review copy is 1.3.
Output: tools/batchAU_2026-11-20.json, tools/batchAU_sha_2026-11-20.json, audit/preview/<id>.html"""
import json, hashlib

pages, E, order = {}, {}, []


def e(p, old, new, note, count=1):
    p = str(p)
    if p not in pages:
        pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
        order.append(p)
    t = pages[p][1]
    assert t.count(old) == count, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new)
    E.setdefault(p, []).append({'old': old, 'new': new, 'count': count, 'note': note})


e('597270', '<strong>Version 1.2, November 2026</strong> (last updated November 14, 2026).',
  '<strong>Version 1.2, November 2026</strong> (last updated November 20, 2026).', 'About: last-updated date')

NEW = ('<li><strong>Update (November 20, 2026).</strong> Checked before faculty review. <em>Sources:</em> every statistic, '
       'clinical value, date and regional fact that needs a source was checked against it; wrong numbers were corrected, weak or '
       'broken sources were replaced with government, journal and local primary sources (CDC, NIH, FDA, USDA, CDFA, the Fresno County '
       'Crop &amp; Livestock Report, the Almond Board&rsquo;s Almond Almanac), and citations were added where a number had none. The '
       'adapted step lists in 13.5 and 14.3 were rewritten, and the figure credits in 14.4 now name their real source. '
       '<em>Accessibility:</em> Figure 11.1.1 (alcohol dehydrogenase) is back; tables and figures that scroll sideways on a phone can '
       'now be reached and scrolled with the keyboard, and each is named for a screen reader; the &ldquo;Answer&rdquo; buttons are '
       'larger and show an arrow; small fixes in 3.7, 5.2, 11.6, 12.2, 12.3 and 15.4. An automated WCAG 2.1/2.2 AA scan of every '
       'page now finds no problems in the book&rsquo;s own content.</li>\n')
e('597270', '<li><strong>Update (November 17, 2026).</strong>', NEW + '<li><strong>Update (November 17, 2026).</strong>',
  'About: version history entry for November 18-20')

h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'batch': 'AU', 'date': '2026-11-20', 'uploads': [], 'edits': E}, open('tools/batchAU_2026-11-20.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAU_sha_2026-11-20.json', 'w'))
print(sum(len(v) for v in E.values()), 'edits on', len(E), 'pages')
