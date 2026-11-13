"""Batch G (review 2026-11-12): leftovers from earlier sessions.
- 9.3: the labelled POPC space-filling image (file 435596) has no source in Malik or on Wikimedia Commons (checked: Commons POPC.png,
  Phospholipid_TvanBrussel, keyword searches). Replaced by an original labelled sketch (tools/batchF_figs.py: phospholipid()).
- 9.3 Fig 1 and 9.4 Fig 2: "(Copyright: Public domain)." (colon form missed by batch C5) -> Malik credit, as in batch E1.
Not here: ADAPT fb-3B-0078 (the question bank and export payloads have no pKa; the live ADAPT copy needs a sign-in);
lab experiment numbers (need the lab manual).
Output: tools/batchG_2026-11-12.json {uploads, edits}
"""
import json, re
L = 'pages/live/'
MALIK = '(Figure from <em>Introduction to Organic and Biochemistry</em> (Malik), public domain.)'
uploads, edits = [], {}
def page(p): return open(L + p + '.html', encoding='utf-8').read()
def e(p, old, new, note):
    assert page(p).count(old) == 1, (p, note); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})
t = page('597146')
old = [m.group(0) for m in re.finditer(r'<img[^>]*>', t) if 'files/435596/' in m.group(0)][0]
alt = re.search(r'aria-label="([^"]*)"', open('figures/pages/batchF/fig-p597146-phosphatidylcholine.svg').read()).group(1)
new = ('<img style="float:right;max-width:45%;height:auto;margin:0 0 8px 16px;" alt="' + alt + '" class="internal wrap-right" width="205" '
       'src="/@api/deki/files/{{pl}}/fig-p597146-phosphatidylcholine.svg" fileid="{{pl}}" />')
uploads.append({'page': '597146', 'name': 'fig-p597146-phosphatidylcholine.svg', 'path': 'figures/pages/batchF/fig-p597146-phosphatidylcholine.svg', 'key': 'pl', 'old_fileid': None})
e('597146', old, new, '9.3 labelled phospholipid: own sketch replaces unsourced image')
e('597146', 'the 2<sup>nd</sup> fatty acid attached to the secondary alcohol group of glycerol is usually an unsaturated fatty acid.</p>',
  'the 2<sup>nd</sup> fatty acid attached to the secondary alcohol group of glycerol is usually an unsaturated fatty acid.</p>\n<p style="clear:both"><small>Phosphatidylcholine sketch: Daniel Kwasniewski, CC BY 4.0.</small></p>', '9.3 sketch credit')
e('597146', 'and condensed formula (right). (Copyright: Public domain).</figcaption>', 'and condensed formula (right). ' + MALIK + '</figcaption>', '9.3 Fig 1 Malik credit')
e('597147', 'containing stearic acid and ethanolamine (right). (Copyright: Public domain).</figcaption>', 'containing stearic acid and ethanolamine (right). ' + MALIK + '</figcaption>', '9.4 Fig 2 Malik credit')
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchG_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'upload;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
