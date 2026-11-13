import json, re
SP = '/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/'
ALTS = json.load(open(SP + 'K1_alts.json'))
LIVE = 'pages/live/'
CR = ' (Diagram: Daniel Kwasniewski, CC BY 4.0.)'
def fig(key, name, num, cap):
    alt = ALTS[name]
    assert '"' not in alt and '&' not in alt and '<' not in alt
    return (f'<figure class="figure"><img class="internal" alt="{alt}" width="760" style="max-width:100%;height:auto;" '
            f'src="/@api/deki/files/{{{{{key}}}}}/{name}" fileid="{{{{{key}}}}}" /><figcaption>Figure {num}: {cap}{CR}</figcaption></figure>')
PI = lambda n: '\\(\\PageIndex{%d}\\)' % n
F = {
 'k1dimer': ('597111', 'fig-p597111-acid-dimer.svg', PI(2), 'Two acetic acid molecules line up head-to-head and hold each other with <strong>two</strong> hydrogen bonds, forming a dimer; a pair of ethanol molecules is held by only one. That is why carboxylic acids boil higher than alcohols of similar size.'),
 'k1rbc': ('597148', 'fig-p597148-rbc-tonicity.svg', '9.5.6', 'Red blood cells in hypotonic (0.45% NaCl), isotonic (0.9% NaCl, normal saline) and hypertonic (3% NaCl) solutions. Water moves toward the side with more dissolved particles: into the cell (it swells and may burst), in and out equally (normal biconcave shape), or out of the cell (it shrinks and crenates).'),
 'k1poly': ('597140', 'fig-p597140-polysaccharides.svg', '8.7.6', 'The glucose polymers side by side (each circle is one glucose). Amylose: unbranched &alpha;(1&rarr;4) chain that coils into a helix. Glycogen: &alpha;(1&rarr;4) chains with frequent &alpha;(1&rarr;6) branches, so it has many chain ends. Cellulose: straight &beta;(1&rarr;4) chains held side by side by hydrogen bonds.'),
 'k1glyc': ('597196', 'fig-p597196-glycogen-branches.svg', '13.7.1', 'One glycogen molecule. Glycogenin holds the single reducing end; &alpha;(1&rarr;4) chains branch at &alpha;(1&rarr;6) links, and every branch ends in a non-reducing end (green), where glycogen synthase adds glucose and glycogen phosphorylase removes it.'),
 'k1acoa': ('597209', 'fig-p597209-acyl-coa-numbering.svg', '15.4.3', 'Numbering a fatty acyl CoA. C1 is the thioester carbon, C(=O)&ndash;S&ndash;CoA; C2 is the &alpha; carbon and C3 is the &beta; carbon, the one oxidized to C=O. So 3-ketoacyl CoA and &beta;-ketoacyl CoA are the same compound, and thiolase cuts between the &alpha; and &beta; carbons.'),
 'k1omega': ('597144', 'fig-p597144-linoleic-omega.svg', '9.1.4', 'Linoleic acid (18:2, both C=C cis) numbered two ways. From the COOH carbon, the last double bond starts at C12; from the CH<sub>3</sub> end, the first double bond starts at &omega;6 (C13). 18 &minus; 12 = 6, so linoleic acid is an omega-6 fatty acid.'),
 'k1lewis': ('597056', 'fig-p597056-lewis-errors.svg', PI(1), 'The four structures of Example 1 drawn out, each beside its corrected form. (a) too many electrons on O; (b) correct; (c) S without an octet; (d) N with four bonds and no lone pair, which is the pattern of N<sup>+</sup>.'),
 'k1lido': ('597123', 'fig-p597123-lidocaine-neutral.svg', '7.3.2', 'Where lidocaine is in its neutral, membrane-crossing form (R<sub>3</sub>N). In the acidic cartridge almost all of it is the charged salt; at tissue pH 7.4 more of it is neutral and reaches the nerve; in an acidic abscess more stays charged, so anesthesia is slower and weaker. (Qualitative, not to scale.)'),
}
anchors = {
 'k1dimer': ('dispersion forces grow with the chain.</p>', 'after'),
 'k1rbc': ('it ends up acting like free water that can move into cells (Section 8.3).</p>', 'after'),
 'k1poly': ('Figure 8.7.5: Cellulose, an unbranched &beta;(1&rarr;4) glucose polymer. (Figure: Daniel Kwasniewski, CC BY 4.0.)</figcaption></figure>', 'after'),
 'k1glyc': ('can be built and dismantled far faster than one long chain.</p>', 'after'),
 'k1acoa': ('<figure class="figure"><img class="internal" alt="The beta-oxidation cycle drawn as a square.', 'before'),
 'k1omega': ('<p><strong>Check.</strong> Shortcut: 18 &minus; 12 = 6.', 'before'),
 'k1lewis': ('so the molecule should be CH<sub>3</sub>NH<sub>2</sub>.</li>\n</ul>', 'after'),
 'k1lido': ('to protect its phenol groups from oxidation.</p>', 'after'),
}
renum = {
 '597196': [('<figcaption>Figure 13.7.2: The hormonal switch.', '<figcaption>Figure 13.7.3: The hormonal switch.'),
            ('<figcaption>Figure 13.7.1: The glycogen pathway map.', '<figcaption>Figure 13.7.2: The glycogen pathway map.')],
 '597209': [('<figcaption>Figure 15.4.4: Glycerol metabolism', '<figcaption>Figure 15.4.5: Glycerol metabolism'),
            ('<figcaption>Figure 15.4.3: One turn of', '<figcaption>Figure 15.4.4: One turn of')],
 '597144': [('<figcaption>Figure 9.1.5: Arachidonic acid', '<figcaption>Figure 9.1.6: Arachidonic acid'),
            ('<figcaption>Figure 9.1.4: One eicosanoid', '<figcaption>Figure 9.1.5: One eicosanoid')],
}
uploads, edits = [], {}
for key, (page, name, num, cap) in F.items():
    uploads.append({'page': page, 'name': name, 'path': 'figures/pages/batchK/' + name, 'key': key})
    html = open(LIVE + page + '.html').read()
    lst = edits.setdefault(page, [])
    for o, n in renum.get(page, []):
        assert html.count(o) == 1, (page, o)
        lst.append({'old': o, 'new': n, 'count': 1, 'note': f'renumber hard-typed caption so the new Figure {num} stays in page order'})
    anc, where = anchors[key]
    assert html.count(anc) == 1, (page, anc, html.count(anc))
    f = fig(key, name, num, cap)
    new = anc + '\n' + f if where == 'after' else f + '\n' + anc
    lst.append({'old': anc, 'new': new, 'count': 1, 'note': f'insert Figure {num} ({name})'})
# simulate application
for page, lst in edits.items():
    html = open(LIVE + page + '.html').read()
    for e in lst:
        assert html.count(e['old']) == 1, (page, e['old'])
        html = html.replace(e['old'], e['new'])
    caps = re.findall(r'<figcaption>(Figure [^:]*):', html)
    print(page, caps)
json.dump({'uploads': uploads, 'edits': edits}, open(SP + 'K1_figs.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
