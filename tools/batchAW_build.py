"""Batch AW (2026-11-20): final touches.
1. About This Book: the November 20 version-history entry names the five new Hands-on Lab boxes (batch AV).
2. 2.8 ozone figure credit: ozonewatch.gsfc.nasa.gov timed out on 2026-11-19 and 11-20 (home page too). The credit still names
   NASA Ozone Watch and now links NASA's own page on this same date: "This image ... shows the Antarctic ozone hole on
   September 24, 2006" (science.nasa.gov/earth/earth-observatory/ozone-hole-reaches-record-size-7044/, read 2026-11-20)."""
import json, hashlib
pages, E, order = {}, {}, []


def e(p, old, new, note):
    if p not in pages:
        pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
        order.append(p)
    t = pages[p][1]
    assert t.count(old) == 1, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new)
    E.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})


END = 'page now finds no problems in the book&rsquo;s own content.</li>'
e('597270', END, END[:-5] + ' <em>New labs:</em> five Hands-on Lab boxes let students build Lewis structures (1.3), turn 3-D '
  'molecular shapes (1.5), and test the blood buffer (6.10), hemoglobin and oxygen (10.9), and buffers in DKA (15.5).</li>',
  'About: Nov 20 history entry names the five new labs')
e('597072', '<abbr title="National Aeronautics and Space Administration">NASA</abbr>, <a target="_blank" '
  'href="https://ozonewatch.gsfc.nasa.gov/Scripts/big_image.php?date=2006-09-24&amp;hem=S" rel="external noopener nofollow" '
  'class="link external">Ozone Watch</a><span> [ozonewatch.gsfc.nasa.gov]</span>.',
  '<abbr title="National Aeronautics and Space Administration">NASA</abbr> Ozone Watch; see NASA Earth Observatory, '
  '<a style="text-decoration:underline" href="https://science.nasa.gov/earth/earth-observatory/ozone-hole-reaches-record-size-7044/" '
  'rel="noopener" target="_blank">Ozone Hole Reaches Record Size</a>.', '2.8: figure credit links a working NASA page')
h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'batch': 'AW', 'date': '2026-11-20', 'uploads': [], 'edits': E}, open('tools/batchAW_2026-11-20.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAW_sha_2026-11-20.json', 'w'))
print(sum(len(v) for v in E.values()), 'edits on', len(E), 'pages')
