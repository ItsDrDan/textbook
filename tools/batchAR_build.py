"""Batch AR (2026-11-18): author decisions round 3 (Wikipedia credits removed after rewrite, ketone values sourced, local primary sources for Valley numbers) from the source and science-verification audit
(audit/source-audit-2026-11-18/SUMMARY.md). Each claim corrected and/or given a verified source.
Drafts per chapter group in tools/batchAR_parts/fixr3_t*.py (each defines its own e(); here it is replaced by ours).
Output: tools/batchAR_2026-11-18.json, tools/batchAR_sha_2026-11-18.json, audit/preview/<id>.html"""
import json, hashlib, re
pages, edits, order = {}, {}, []


def e(p, old, new, note, why, count=1):
    p = str(p)
    if p not in pages:
        pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
        order.append(p)
    t = pages[p][1]
    assert t.count(old) == count, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': count, 'note': note, 'why': why})


for f in ['fixr3_t2_ch4-6.py', 'fixr3_t3_ch7-9.py', 'fixr3_t5_ch13-15.py']:
    src = open('tools/batchAR_parts/' + f, encoding='utf-8').read()
    src = re.sub(r'^def e\(', 'def _their_e(', src, flags=re.M)
    exec(compile(src, f, 'exec'), {'e': e, '__name__': 'batchAP', '__file__': '/dev/null/' + f})

# ---- Fresno County 2024 Crop & Livestock Report, read in a browser 2026-11-18 (p. 2 letter: almonds $1,458,370,000;
# p. 3 top ten: 8 peaches $422,789,000, 9 garlic $281,204,000). Script downloads are blocked by the county site.
FC = ('Fresno County Department of Agriculture, <a style="text-decoration:underline" href="https://www.fresnocountyca.gov/files/'
      'sharedassets/county/v/1/agricultural-commissioner/ag-crop-reports/ag-crop-and-livestock-report_2024.pdf" rel="noopener" '
      'target="_blank">2024 Annual Crop &amp; Livestock Report</a>, 2025, p. 3.')
WHYFC = 'Fresno County 2024 Crop & Livestock Report p. 3 (top ten by value) and p. 2 (commissioner letter), read in a browser 2026-11-18.'
import re as _re
e('597145', 'worth about $1.45 billion', 'worth about $1.46 billion', '9.2 Fresno almonds 2024 value', WHYFC + ' Almonds $1,458,370,000.')
e('597145', '2024 Annual Crop &amp; Livestock Report</a>, 2025;', '2024 Annual Crop &amp; Livestock Report</a>, 2025, pp. 2&ndash;3;',
  '9.2 source 2 page numbers', WHYFC)

def add_source(pid, anchor_heading, entry, note):
    t = pages[pid][1] if pid in pages else open('pages/live/%s.html' % pid, encoding='utf-8').read()
    i = t.index(anchor_heading); j = t.index('<strong>Sources:</strong>', i); k = t.index('</p>', j)
    para = t[j:k]; n = max(int(x) for x in _re.findall(r'(?<![\d.])\b(\d{1,2})\. (?=[A-Z])', para)) + 1
    e(pid, para + '</p>', para + ' %d. %s</p>' % (n, entry), note, WHYFC)
    return n

n = add_source('597098', 'Valley Connection: Garlic', FC, '4.9 Valley box: Fresno County 2024 report added as a source')
e('597098', 'and garlic was one of the county&rsquo;s ten highest-value crops.<sup>2</sup>',
  'and garlic was one of the county&rsquo;s ten highest-value crops (ninth in 2024, worth about $281 million).<sup>2,%d</sup>' % n,
  '4.9 garlic rank and value from the county report', WHYFC)
n = add_source('597113', 'peaches by value', FC, '6.5 Valley box: Fresno County 2024 report added as a source')
e('597113', 'Peaches are also among Fresno County&rsquo;s top ten crops, and the county grows nearly half of California&rsquo;s peaches by value.<sup>4</sup>',
  'Peaches are also among Fresno County&rsquo;s top ten crops (eighth in 2024, worth about $423 million), and the county grows nearly half of California&rsquo;s peaches by value.<sup>4,%d</sup>' % n,
  '6.5 peach rank and value from the county report', WHYFC)

ALM = 'https://www.almonds.org/sites/default/files/2025-12/Digital-Almanac-2025.pdf'
e('597170', 'California grows nearly 80% of the world&rsquo;s almonds,',
  'The United States, almost all of it California, grows about 73% of the world&rsquo;s almonds,',
  '11.5 almond world share to the 2025 Almanac (matches 9.2)', 'Almond Board 2025 Almanac p. 29: U.S. 73% of world production (checked by the Ch 7-9 checker; 9.2 uses the same figure).')
e('597170', '<a style="text-decoration:underline" href="https://it.almonds.org/sites/default/files/2023-04/2022_Almanac.pdf" rel="noopener" target="_blank">2022 Almond Almanac (world share and production by county)</a>.',
  '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">2025 Almond Almanac (world share and production by county)</a>, pp. 24 and 29.' % ALM,
  '11.5 source 1 to the 2025 Almanac', 'Same.')


h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAR_2026-11-18.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAR_sha_2026-11-18.json', 'w'))
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
