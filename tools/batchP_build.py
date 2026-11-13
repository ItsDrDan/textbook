"""Batch P: the instructor's decisions of 2026-11-13 (3.4 Example 3, 11.1 Figure 1, version 1.2) and the remaining page-level rows
of tools/REVIEW_2026-11-13.md (image credits confirmed on Wikimedia Commons, 9.3 photo position, small sketch size).
DRAFT ONLY until the instructor approves. Count-checked against pages/live (which matches the live book after batch O).
Output: tools/batchP_2026-11-13.json {uploads, edits} and tools/batchP_sha_2026-11-13.json."""
import json, re, hashlib

L = 'pages/live/'
pages, edits, uploads, orig = {}, {}, [], {}


def page(p):
    if p not in pages:
        pages[p] = open(L + p + '.html', encoding='utf-8').read(); orig[p] = pages[p]
    return pages[p]


def e(p, old, new, note, n=1):
    t = page(p); assert t.count(old) == n, (p, note, t.count(old))
    assert old != new, (p, note)
    pages[p] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


# ---------------- 3.4 Example 3: 1-butene instead of 3-methyl-1-butene (which rearranges on hydration) ----------------
e('597081', '(a) Draw the line structure of 3-methyl-1-butene. (b) Classify carbon 3 as', '(a) Draw the line structure of 1-butene. (b) Classify carbon 3 as', 'T1 3.4 Example 3: alkene swapped to 1-butene')
e('597081', 'suffix <em>-1-ene</em> (double bond starting at C1), prefix <em>3-methyl</em>. Draw a four-carbon zigzag, make the first bond double, and add a methyl branch at C3:</p>',
  'suffix <em>-1-ene</em> (double bond starting at C1), no branches. Draw a four-carbon zigzag and make the first bond double:</p>', 'T1 3.4 Example 3(a)')
e('597081', 'aria-label="Line structure of 3-methyl-1-butene: a double bond at one end of a four-carbon zigzag, with a methyl branch on the third carbon"',
  'aria-label="Line structure of 1-butene: a four-carbon zigzag with a double bond at one end"', 'T1 3.4 Example 3 figure label')
e('597081', '<line x1="62.4" y1="-6.2" x2="65.6" y2="29.6" stroke="#2d3f4b" stroke-width="2.4" stroke-linecap="round"></line></svg><figcaption>Figure 3.4.2: 3-Methyl-1-butene.',
  '</svg><figcaption>Figure 3.4.2: 1-Butene.', 'T1 3.4 Example 3 figure: methyl branch removed from the drawing; caption')
e('597081', '(b) C3 is bonded to C2, C4, and the methyl carbon: three carbon neighbors, so it is <strong>tertiary (3&deg;)</strong>.',
  '(b) C3 is bonded to C2 and C4: two carbon neighbors, so it is <strong>secondary (2&deg;)</strong>.', 'T1 3.4 Example 3(b)')
e('597081', 'so the new H goes to C1 and the OH to C2: CH<sub>3</sub>CH(OH)CH(CH<sub>3</sub>)CH<sub>3</sub>, <strong>3-methyl-2-butanol</strong>.',
  'so the new H goes to C1 and the OH to C2: CH<sub>3</sub>CH(OH)CH<sub>2</sub>CH<sub>3</sub>, <strong>2-butanol</strong>.', 'T1 3.4 Example 3(c)')
e('597081', 'Product formula C<sub>5</sub>H<sub>12</sub>O = alkene C<sub>5</sub>H<sub>10</sub> + H<sub>2</sub>O. The alcohol in Example 2 is this same compound. Dehydrating it (Example 2) gives mostly 2-methyl-2-butene, not this alkene, so addition',
  'Product formula C<sub>4</sub>H<sub>10</sub>O = alkene C<sub>4</sub>H<sub>8</sub> + H<sub>2</sub>O. Dehydrating 2-butanol gives mostly 2-butene (Zaitsev, as in Example 2), not 1-butene, so addition',
  'T1 3.4 Example 3 check')

# ---------------- 11.1 Figure 1: the figure is an online 3-D viewer; say so, and name the source ----------------
e('597166', '</strong>Structure of the alcohol dehydrogenase protein (E.C.1.1.1.1) (EE ISOZYME) complexed with nicotinamide adenine dinucleotide (NAD) and zinc (PDB: 1CDO).</em></p>',
  '</strong>Interactive 3-D model of the enzyme alcohol dehydrogenase (EC 1.1.1.1) with its coenzyme NAD and zinc ions bound. The model can be rotated in the online book; it does not appear in print. (Structure: Protein Data Bank entry 1CDO, shown with the GLmol viewer.)</em></p>',
  'T3 11.1 Figure 1: script-only viewer; caption now says it is an online model and names the source')

# ---------------- About This Book and title page: version 1.2 ----------------
V12 = ('<li><strong>1.2 (November 13, 2026).</strong> Sections were reordered and renumbered so that each chapter builds in teaching order: old 12.9 is now 12.5 and old 12.5&ndash;12.8 are 12.6&ndash;12.9; '
       'old 13.7 is now 13.9 and old 13.8&ndash;13.9 are 13.7&ndash;13.8; Chapter 15 is now a lipid block (15.1&ndash;15.6) followed by a protein block (15.7&ndash;15.11). Page links did not change. '
       'Also in this version: corrections from a full accuracy check of every chapter, clinical updates, seven more Valley Connections, new figures and worked examples, larger print figures, and a print answer key on every section with exercises.</li>\n')
e('597270', '<li><strong>1.1 (November 11, 2026).</strong>', V12 + '<li><strong>1.1 (November 11, 2026).</strong>', 'T4 About: version 1.2 entry records the renumbering')
e('597270', '<strong>Version 1.1, November 2026</strong> (last updated November 11, 2026).', '<strong>Version 1.2, November 2026</strong> (last updated November 13, 2026).', 'T4 About: version line')
e('488226', 'Version 1.1, November 2026', 'Version 1.2, November 2026', 'T4 Title page: version 1.2')

# ---------------- credits confirmed on Wikimedia Commons (file names match; licence read from the Commons API on 2026-11-13) ----------------
e('597080', '<em>The bright red color of tomatoes is due to lycopene&mdash;a polyene.</em>',
  '<em>The bright red color of tomatoes is due to lycopene&mdash;a polyene. (Structure: Jeff Dahl, public domain, via <a href="https://commons.wikimedia.org/wiki/File:Lycopene.svg" target="_blank" rel="noopener">Wikimedia Commons</a>.)</em>',
  'T3 3.3: lycopene structure credit')
e('597096', 'antiseptics were used.</em></p>',
  'antiseptics were used. (Gaspare Traversi, public domain, via <a href="https://commons.wikimedia.org/wiki/File:1753_Traversi_Operation_anagoria.JPG" target="_blank" rel="noopener">Wikimedia Commons</a>.)</em></p>',
  'T3 4.7: Traversi painting credit')
e('597097', 'Source: Painting of William Morton by Ernest Board.</figcaption>',
  'Source: Painting of William Morton by Ernest Board (public domain, via <a href="https://commons.wikimedia.org/wiki/File:Morton_Ether_1846.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>).</figcaption>',
  'T3 4.8: Morton painting licence')

# ---------------- 9.3: snake photo moved into its box; small labelled sketch enlarged for print ----------------
t = page('597146'); i = t.index('fig-p597146-venom.jpg'); a = t.rfind('<img', 0, i); b = t.index('/>', i) + 2; venom = t[a:b]
assert t[b:b + 30].startswith('The hydrophobic tails')
e('597146', venom + 'The hydrophobic tails of fatty acids', 'The hydrophobic tails of fatty acids', 'T3 9.3: snake photo taken out of the bilayer paragraph')
box = '<div class="mt-section"><h4 class="box-legend editable">Snake venom</h4>\n\n<p>'
e('597146', box, box + venom, 'T3 9.3: snake photo placed in the Snake venom box, beside its credit')
e('597146', 'The structure of the lysophospholipid example is shown in the figure on the left.', 'The structure of the lysophospholipid example is shown here.', 'T4 9.3: left/right fails in print')
e('597146', 'class="internal wrap-right" width="205" src="/@api/deki/files/512768/fig-p597146-phosphatidylcholine.svg"', 'class="internal wrap-right" width="300" src="/@api/deki/files/512768/fig-p597146-phosphatidylcholine.svg"',
  'T3 9.3: labelled sketch printed with 4.5-5.2 pt labels; wider so they print at about 6.5-7.5 pt')

# ---------------- small print: 14.3.2 "CoA-SH released" label 11 -> 13 px in the three strips (GitHub Pages); cache-bust ----------------
for k in (1, 2, 3):
    e('597202', f'figures/print/fig-p597202-1-v2-{k}.svg"', f'figures/print/fig-p597202-1-v2-{k}.svg?v=20261113b"', '14.3.2 strip cache-bust (small label enlarged; printed at 4.8 pt)')

# ---------------- hot-linked images re-hosted on their own pages ----------------
# Also uploaded in this batch as new revisions of existing files (no page edit needed): fig-p597192-1.svg (13.4.2, 11 -> 13 px labels),
# fig-p597212-1.svg (15.2.1, 12/13 -> 14.5 px) and fig-p597212-2.svg (15.2.2, 12/13 -> 14 px, blank band cropped: viewBox 0 55 832 447).
import os
IDS = json.load(open('tools/batchP_ids_2026-11-13.json')) if os.path.exists('tools/batchP_ids_2026-11-13.json') else {'insulin': '{{insulin}}', 'allo': '{{allo}}'}
uploads.append({'page': '597160', 'name': 'fig-p597160-insulin.gif', 'source': 'https://upload.wikimedia.org/wikipedia/commons/3/30/Insulin_1AI0_animation.gif', 'key': 'insulin'})
uploads.append({'page': '597171', 'name': 'fig-p597171-allosteric.jpeg', 'path': 'figures/pages/batchP/fig-p597171-allosteric.jpeg', 'key': 'allo'})
e('597160', 'class="default" src="https://upload.wikimedia.org/wikipedia/commons/3/30/Insulin_1AI0_animation.gif" />',
  f'class="internal" src="/@api/deki/files/{IDS["insulin"]}/fig-p597160-insulin.gif" fileid="{IDS["insulin"]}" />', 'T3 10.7 Figure 4: image was hot-linked from Wikimedia; now a file on this page')
e('597160', 'Rotating 3d cartoon model of the human insulin monomer', 'Cartoon model of the human insulin monomer (it rotates in the online book)', 'T3 10.7 Figure 4 caption: the animation does not rotate in print')
e('597171', 'src="https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/1950/2017/05/31183107/figure-06-05-05.jpeg"',
  f'class="internal" src="/@api/deki/files/{IDS["allo"]}/fig-p597171-allosteric.jpeg" fileid="{IDS["allo"]}"', 'T3 11.6 Figure 1: image was hot-linked from an outside server; now a file on this page')

sha = {p: {'before': hashlib.sha256(orig[p].encode()).hexdigest(), 'after': hashlib.sha256(pages[p].encode()).hexdigest()} for p in edits}
json.dump(sha, open('tools/batchP_sha_2026-11-13.json', 'w'), indent=0)
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchP_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
