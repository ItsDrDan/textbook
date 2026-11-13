"""Batch H: fixes found in the full-book PDF of 2026-11-12 22:14 (CHEM3B-Full-2026-11-12-2215.pdf, 1,324 pp).
H1  Answer-key and exercise labels ("Problem N", "Exercise N", "Case Question N", "Cumulative Problem N (...)", "Solution")
    were stranded at page feet (43 Problem labels alone). Add page-break-after:avoid (the rule proved to work on the
    2.10 drawn-example labels). 1,553 labels on 77 pages.
H2  12.4 Figure 12.4.2: the tRNA-loading strips shared a side-by-side row with the 3-D tRNA image and printed at
    3.6 in with ~4 pt labels. Moved below the row (caption left/right -> top/bottom).
H3  13.1: the metabolism overview was CC BY-SA 4.0 (Linares-Pasten), the only ShareAlike image left. Replaced by an
    original diagram (tools/batchF_figs.py metabolism()).
H4  Credits in body text that still began "Copyright:"/"Copyright;" (13.1 x4, 9.3 Fig 3 x2) cleaned.
H5  12.6 elongation figure: amino-acid labels enlarged (re-upload, same name).
Output: tools/batchH_2026-11-12.json {uploads, edits}
"""
import json, re, glob, collections

L = 'pages/live/'
uploads, edits = [], {}
pages = {}


def page(p):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read()
    return pages[p]


def e(p, old, new, note, n=1):
    t = page(p); assert t.count(old) == n, (p, note, t.count(old))
    pages[p] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


# H1
pat = re.compile(r'<p><strong>((?:Problem|Exercise|Case Question|Cumulative Problem)(?: [\d.]+)?(?: \([^<)]{0,60}\))?|Solution\.?)</strong></p>')
total = 0
for f in sorted(glob.glob(L + '*.html')):
    p = f.split('/')[-1][:-5]
    c = collections.Counter(m.group(0) for m in pat.finditer(page(p)))
    for lab, n in c.items():
        e(p, lab, lab.replace('<p>', '<p style="page-break-after:avoid;break-after:avoid">', 1), 'H1 keep label with its answer', n)
        total += n

# H2
t = page('597178')
a = t.find('<figure><img src="https://itsdrdan.github.io/textbook/figures/print/trna_loading-v2-1.svg"')
b = t.find('</figure>\n</div>', a) + len('</figure>\n</div>')
seg = t[a:b]
strips = seg[:-len('\n</div>')]
e('597178', '\n\n' + seg, '\n</div>\n' + strips.replace('<figure>', '<figure style="margin-top:12px">', 1), 'H2 tRNA-loading strips below the row (full width in print)')
cap_old = "its 2D depiction (left), and attachment of an amino acid to the free 3' \\(\\ce{-OH}\\) group of tRNA through an ester linkage using the energy released by ATP and catalyzed by enzyme aminoacyl tRNA synthetase (right). (left: "
e('597178', cap_old, cap_old.replace('(left), and', '(top), and').replace('synthetase (right). (left: ', 'synthetase (bottom). (top: '), 'H2 caption top/bottom')
e('597178', 'Public domain, right: Diagram: Daniel Kwasniewski, CC BY 4.0)</figcaption>', 'Public domain; bottom: Diagram: Daniel Kwasniewski, CC BY 4.0)</figcaption>', 'H2 caption credits')

# H3
old = [m.group(0) for m in re.finditer(r'<img[^>]*>', page('597188')) if 'files/436176/' in m.group(0)][0]
alt = re.search(r'aria-label="([^"]*)"', open('figures/pages/batchF/fig-p597188-metabolism.svg').read()).group(1)
new = ('<img style="display:block;max-width:100%;height:auto;margin:0 auto 8px;" alt="' + alt + '" class="internal" width="760" '
       'src="/@api/deki/files/{{met}}/fig-p597188-metabolism.svg" fileid="{{met}}" />')
uploads.append({'page': '597188', 'name': 'fig-p597188-metabolism.svg', 'path': 'figures/pages/batchF/fig-p597188-metabolism.svg', 'key': 'met', 'old_fileid': None})
e('597188', old, new, 'H3 metabolism overview: own diagram replaces CC BY-SA image')
e('597188', 'The figure on the right summarizes metabolism and its sub-categories: catabolism and anabolism (<em>Copyright: Linares-Past&eacute;n, J. A. (2018), CCBYSA 4, via Wikimedia Commons</em>)</p>',
  'The figure above summarizes metabolism and its two parts, catabolism and anabolism (<em>Diagram: Daniel Kwasniewski, CC BY 4.0</em>).</p>', 'H3 text and credit')

# H4
e('597188', '(<em>Copyright: modified from Tim Vickers, vectorized by Fvasconcellos, Public domain, via Wikimedia Commons</em>)',
  '(<em>Diagram modified from Tim Vickers, vectorized by Fvasconcellos, public domain, via Wikimedia Commons</em>)', 'H4 credit')
e('597188', '(<em>Copyright: National Cancer Institute, Public domain, via Wikimedia Commons</em>)', '(<em>Image: National Cancer Institute, public domain, via Wikimedia Commons</em>)', 'H4 credit')
e('597188', '(<em>Copyright; <a title="https://www.genome.gov/genetics-glossary/Cell"', '(<em>Image: <a title="https://www.genome.gov/genetics-glossary/Cell"', 'H4 credit')
e('597188', '(<em>Copyright;  LadyofHats, Public domain, via Wikimedia Commons</em>)', '(<em>Diagram: LadyofHats, public domain, via Wikimedia Commons</em>)', 'H4 credit')
e('597146', '(left, Copyright: MDougM, Public domain, via Wikimedia Commons)', '(left, MDougM, public domain, via Wikimedia Commons)', 'H4 credit')
e('597146', '(right, Copyright: MDougM, Public domain, via Wikimedia Commons)', '(right, MDougM, public domain, via Wikimedia Commons)', 'H4 credit')

# H5 (same-name re-upload; the publisher repoints if the id changes)
uploads.append({'page': '597179', 'name': 'fig-p597179-elongation.svg', 'path': 'figures/pages/batchF/fig-p597179-elongation.svg', 'key': 'elong', 'old_fileid': '512767'})

json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchH_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print('H1 labels', total, '|', len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
