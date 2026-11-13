"""Batch O: the "draftable next pass" rows of tools/REVIEW_2026-11-13.md, plus replacements for dead links.
DRAFT ONLY until the instructor approves. Count-checked against pages/live (which matches the live book after batch N).
Output: tools/batchO_2026-11-13.json {uploads, edits} and tools/batchO_sha_2026-11-13.json (hash of each page before and after)."""
import json, re, hashlib, html

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


def ea(p, old, new, note):
    n = page(p).count(old); assert n >= 1, (p, note); e(p, old, new, note, n=n)


# ---------------- captions that repeated the alt text word for word ----------------
e('597116', '<figcaption style="font-size:.85em;color:#555">Skeletal structure of aspirin: a benzene ring carrying a carboxylic acid group (COOH) and, on the neighboring carbon, an ester group O&ndash;C(=O)&ndash;CH3. Drawn by',
  '<figcaption style="font-size:.85em;color:#555">Aspirin (acetylsalicylic acid). Drawn by', 'T3 6.8: caption repeated the alt text')
e('597131', '<figcaption style="font-size:.85em;color:#555">Skeletal structure of epinephrine: a benzene ring with two neighboring OH groups, attached to a CH(OH)&ndash;CH2&ndash;NH&ndash;CH3 side chain. Drawn by',
  '<figcaption style="font-size:.85em;color:#555">Epinephrine (adrenaline). Drawn by', 'T3 7.11: caption repeated the alt text (and listed the groups the question asks for)')

# ---------------- 1.7 Figures 1-2: alt-text letters were one behind the visible panel letters; drop them ----------------
t = page('597060')
for m in list(re.finditer(r'alt="\(([a-e])\) ([^"]{30})', t)):
    old = m.group(0); new = 'alt="' + m.group(2)
    e('597060', old, new, f'T3 1.7 Figures 1-2 alt: letter "({m.group(1)})" did not match the visible panel letter')

# ---------------- 12.8: two drug figures had no caption or credit ----------------
e('597181', 'src="/@api/deki/files/512747/fig-p597181-dttp-azt.jpg" fileid="512747" /></p>',
  'src="/@api/deki/files/512747/fig-p597181-dttp-azt.jpg" fileid="512747" /><br /><small>Deoxythymidine triphosphate and AZT. AZT has an azide group (N<sub>3</sub>) in place of the 3&prime;-OH. (Figure adapted from <em>The Basics of General, Organic, and Biological Chemistry</em> by Ball, Hill and Scott, CC BY-NC-SA 3.0.)</small></p>',
  'T3 12.8: caption and credit for the dTTP/AZT figure')
t = page('597181'); i = t.index('files/512732/'); j = t.index('/></p>', i) + len('/></p>'); old = t[t.rfind('<img', 0, i):j]
e('597181', old, old[:-len('</p>')] + '<br /><small>Raltegravir, an integrase inhibitor. (Structure redrawn by Daniel Kwasniewski, CC BY 4.0.)</small></p>', 'T3 12.8: caption and credit for raltegravir')

# ---------------- 10.10 Valley box: sources numbered in order of first citation ----------------
e('597163', '100,000 workers).<sup>4</sup>', '100,000 workers).<sup>1</sup>', 'T4 10.10: source numbers in citation order (was 4, 3, 3, 1, 2)')
e('597163', 'clumping (aggregation).<sup>3</sup>', 'clumping (aggregation).<sup>2</sup>', 'T4 10.10: same')
e('597163', 'brain can fail.<sup>3</sup>', 'brain can fail.<sup>2</sup>', 'T4 10.10: same')
e('597163', 'adjust to heat.<sup>1</sup>', 'adjust to heat.<sup>3</sup>', 'T4 10.10: same')
e('597163', 'and groin.<sup>2</sup>', 'and groin.<sup>4</sup>', 'T4 10.10: same')
t = page('597163'); i = t.index('Sources:</strong> 1. California Department'); j = t.index('</p>', i); old = t[i:j]
a, b, c = old.index(' 2. CDC/NIOSH'), old.index(' 3. Ferrer R'), old.index(' 4. CDC, <a')
s1, s2, s3, s4 = old[len('Sources:</strong> 1. '):a], old[a + 4:b], old[b + 4:c], old[c + 4:]
e('597163', old, 'Sources:</strong> 1. ' + s4.rstrip('.') + '. 2. ' + s3 + ' 3. ' + s1 + ' 4. ' + s2, 'T4 10.10: source list reordered to match')

# ---------------- Glossary pointers to the teaching section, with the matching Index lines ----------------
SEC = {'1.5': '597058', '1.6': '597059', '10.9': '597162', '12.6': '597179', '12.2': '597176', '10.4': '597157', '10.7': '597160', '8.7': '597140',
       '4.5': '597094', '7.1': '597121', '12.5': '597183'}
GLOSS = [('molecular geometry', '1.5', ['molecular geometry']), ('organic chemistry', '1.6', ['organic chemistry']), ('functional group', '1.6', ['functional group']),
         ('hemoglobin', '10.9', ['hemoglobin']), ('translation', '12.6', ['translation']), ('phosphodiester bond', '12.2', ['phosphodiester bond']),
         ('peptide', '10.4', ['peptide']), ('&alpha; helix, alpha helix', '10.7', ['alpha helix']), ('secondary structure', '10.7', ['secondary structure']),
         ('cellulose', '8.7', ['cellulose']), ('starch', '8.7', ['starch']), ('glycogen', '8.7', ['glycogen']), ('dehydration', '4.5', ['dehydration']),
         ('secondary amine, 2&deg; amine', '7.1', ['secondary amine']), ('messenger RNA, mRNA', '12.5', ['messenger RNA', 'mRNA']),
         ('ribosomal RNA, rRNA', '12.5', ['ribosomal RNA', 'rRNA'])]
for head, sec, idx in GLOSS:
    t = page('488232'); h = f'<td data-th="Word(s)">{head}</td>'; assert t.count(h) == 1, head
    i = t.index(h); j = t.index('</tr>', i); row = t[i:j]
    m = re.search(r'<a href="/@go/page/\d+">Section ([\d.]+)</a>', row); oldsec = m.group(1)
    e('488232', row, row.replace(m.group(0), f'<a href="/@go/page/{SEC[sec]}">Section {sec}</a>'), f'T4 Glossary: {html.unescape(head)} {oldsec} -> {sec} (where the term is taught)')
    for term in idx:
        e('488231', f'<li>{term}, {oldsec}</li>', f'<li>{term}, {sec}</li>', f'T4 Index: {term}, {sec}')

# ---------------- Index: glossary headwords that had no Index line ----------------
NEW = [('beta-pleated sheet', '10.7'), ('C-terminus', '10.4'), ('N-terminus', '10.4'), ('fat-soluble vitamins', '11.5'), ('water-soluble vitamins', '11.5'),
       ('fluid-mosaic model', '9.5'), ('lock-and-key model', '11.2'), ('omega-3 fatty acid', '9.1'), ('omega-6 fatty acid', '9.1')]
for term, sec in NEW:
    t = page('488231'); assert f'<li>{term},' not in t
    items = [(m.group(1), m.group(0)) for m in re.finditer(r'<li>([^<,]+), [\d.]+</li>', t)]
    same = [x for x in items if x[0][0].lower() == term[0].lower() and x[0].lower() < term.lower()]
    note = f'T4 Index: new entry "{term}, {sec}" (glossary headword with no Index line)'
    if same:
        prev = same[-1][1]; e('488231', prev, prev + f'\n<li>{term}, {sec}</li>', note)
    else:  # sorts before every entry under its letter
        first = [x for x in items if x[0][0].lower() == term[0].lower()][0][1]; e('488231', first, f'<li>{term}, {sec}</li>\n' + first, note)

# ---------------- dead links: replacements that answer today ----------------
ea('597179', 'http://vcell.ndsu.nodak.edu/animations', 'https://www.vcell.science/', 'T4 12.6: the NDSU Virtual Cell site moved (old address no longer answers)')
ea('597200', 'http://vcell.ndsu.edu/animations', 'https://www.vcell.science/', 'T4 14.1: same')
ea('597201', 'http://vcell.ndsu.edu/animations', 'https://www.vcell.science/', 'T4 14.2: same')
for p in ('597179', '597200', '597201'):
    for oldtxt in ('[vcell.ndsu.nodak.edu]', '[vcell.ndsu.edu]'):
        if oldtxt in page(p): ea(p, oldtxt, '[www.vcell.science]', 'T4 visible address updated to match')
ea('597145', 'https://ressources.ciheam.org/ressources/om/pdf/a119/00007413.pdf', 'https://agris.fao.org/search/en/records/6473b0ce96fdec8b71b5aadb',
   'T4 9.2 source 3: CIHEAM PDF no longer answers; FAO AGRIS record of the same paper')
ea('597139', 'https://data.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/California/cp06107.pdf',
   'https://www.nass.usda.gov/publications/agcensus/2022/online-resources/county-profiles/california', 'T4 8.6 source 2: PDF address is 404; USDA page listing the California county profiles')
ea('597094', 'https://www.nass.usda.gov/Statistics_by_State/California/Publications/Specialty_and_Other_Releases/Grapes/Crush/Final/2025/Grape_Crush_2025_Final.pdf',
   'https://www.nass.usda.gov/statistics-by-state/california/publications/specialty-and-other-releases/grapes/crush/reports', 'T4 4.5 source 1: PDF address is 404; USDA grape crush reports page')
ea('597070', 'http://www.nasa.gov/topics/earth/features/oilspill/oil-20100519a.html', 'https://science.nasa.gov/earth/earth-observatory/oil-slick-in-the-gulf-of-mexico-44006/',
   'T4 2.6 photo source: NASA page is 404; NASA Earth Observatory page for the May 17, 2010 MODIS image')
if '[www.nasa.gov]' in page('597070'): ea('597070', '[www.nasa.gov]', '[science.nasa.gov]', 'T4 2.6: visible address updated to match')

sha = {p: {'before': hashlib.sha256(orig[p].encode()).hexdigest(), 'after': hashlib.sha256(pages[p].encode()).hexdigest()} for p in edits}
json.dump(sha, open('tools/batchO_sha_2026-11-13.json', 'w'), indent=0)
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchO_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
