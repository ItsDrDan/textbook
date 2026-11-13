"""Batch L: fixes from the full-book PDF of 2026-11-12 23:50.
- 14.3.1 citric acid cycle wheel (printed ~2 pt) replaced by a landscape loop (tools/batchL_figs.py).
- 7.12 Reaction Roadmap redrawn larger (tools/batchL_roadmap.py; GitHub Pages, cache-bust).
- 9.3.1 condensed formula taken out of the three-across row so it prints full width (~10 pt, was 4 pt).
- Labels stranded at page bottoms kept with their text: 1.3 "Check", 8.9 "Case Set Question 8.2",
  4.4 and 10.2 Example "Solution" headings.
Output: tools/batchL_2026-11-13.json {uploads, edits}"""
import json, re

L = 'pages/live/'
PG = 'https://itsdrdan.github.io/textbook/'
pages, edits, uploads = {}, {}, []


def page(p):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read()
    return pages[p]


def e(p, old, new, note, n=1):
    t = page(p); assert t.count(old) == n, (p, note, t.count(old))
    pages[p] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


# 14.3.1
t = page('597202'); i = t.find('oer/cac_wheel.svg'); old = t[t.rfind('<img', 0, i):t.find('>', i) + 1]
path = 'figures/pages/batchL/fig-p597202-cac-flow.svg'
alt = re.search(r'aria-label="([^"]*)"', open(path).read()).group(1)
uploads.append({'page': '597202', 'name': 'fig-p597202-cac-flow.svg', 'path': path, 'key': 'cac'})
e('597202', old, f'<img width="760" style="max-width:100%;height:auto;" alt="{alt}" src="/@api/deki/files/{{{{cac}}}}/fig-p597202-cac-flow.svg" fileid="{{{{cac}}}}" />',
  '14.3.1 citric acid cycle as a landscape loop (the wheel printed at ~2 pt)')

# 7.12 roadmap (img src and the full-size links)
e('597132', PG + 'sections/reactions/roadmap.svg"', PG + 'sections/reactions/roadmap.svg?v=20261113"', '7.12 roadmap cache-bust (larger print version)',
  n=page('597132').count(PG + 'sections/reactions/roadmap.svg"'))

# 9.3.1: condensed formula out of the row
t = page('597146'); i = t.find('files/512773/'); f0 = t.rfind('<figure>', 0, i); f1 = t.find('</figure>', i) + len('</figure>')
fig = t[f0:f1]
e('597146', '\n\n' + fig + '\n</div>\n', '\n</div>\n' + fig.replace('<figure>', '<figure style="margin-top:8px">', 1) + '\n',
  '9.3.1 condensed formula below the row so it prints full width')
e('597146', 'and condensed formula (right).', 'and condensed formula (below).', '9.3.1 caption: condensed formula now below')

# stranded labels
e('597056', '<p><strong>Check</strong></p>', '<p style="page-break-after:avoid"><strong>Check</strong></p>', '1.3 keep "Check" with its text')
e('597142', '<p class="boxtitle">Case Set Question 8.2</p>', '<p class="boxtitle" style="page-break-after:avoid">Case Set Question 8.2</p>', '8.9 keep box title with its question')
for p, sec in (('597093', '4.4'), ('597155', '10.2')):
    e(p, '<div class="mt-section"><h4 class="editable">Solution</h4>', '<div class="mt-section"><h4 style="page-break-after:avoid" class="editable">Solution</h4>',
      f'{sec} keep Example Solution heading with its text (the server strips attributes on mt-section divs)')

json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchL_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
