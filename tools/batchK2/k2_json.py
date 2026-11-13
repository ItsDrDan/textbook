import json, re, os
os.chdir('/Users/dan/Desktop/Study Games/textbook-git')
A = 'figures/pages/batchK/'
CR = '(Structures drawn by Daniel Kwasniewski, CC BY 4.0.)'
F = [
 ('597116', 'fig-p597116-saponification-tristearin.svg', 'k2sap', 760,
  'do the same job at pH 7.4 without strong acid or base.</p>', 'after',
  'Figure 6.8.2: Saponification of a fat. Heating tristearin, a triacylglycerol (three ester groups on one glycerol backbone), with NaOH splits all three esters, giving glycerol and three sodium stearate units, which are soap. One NaOH is used up for each ester.',
  '6.8 soap paragraph (Lecture Connection): new Fig 6.8.2'),
 ('597126', 'fig-p597126-amide-two-step.svg', 'k2amd', 760,
  '<figcaption>Figure 7.6.1: Amides and amidation. (Figure: Daniel Kwasniewski, CC BY 4.0.)</figcaption></figure>', 'after',
  'Figure 7.6.2: Amide formation takes two steps. Mixed at room temperature, acetic acid and ammonia only undergo an acid&ndash;base reaction, giving the salt ammonium acetate. Heating the salt drives off water and forms the amide, acetamide.',
  '7.6 Lecture Connection, after Fig 7.6.1: two-step amidation'),
 ('597106', 'fig-p597106-menthol-carvone.svg', 'k2chir', 330,
  'fit one hand of menthol far better than the other.</p>\n</div>', 'after',
  'Figure 5.5.9: Chiral carbons (*) in two molecules you can smell. Menthol has three chiral carbons, so 2<sup>3</sup> = 8 stereoisomers are possible; carvone has one, so it exists as a pair of enantiomers (one smells of spearmint, the other of caraway).',
  '5.5 Chirality matters, after Dental Hygiene box: menthol + carvone starred'),
 ('597081', 'fig-p597081-propene-hcl.svg', 'k2mark', 560,
  'so the reaction is called <em>regioselective</em>.</p>', 'after',
  'Figure 3.4.1: Markovnikov&#39;s rule for HCl and propene. The H (red) adds to the end CH<sub>2</sub> carbon, which already has more hydrogens, and the Cl adds to the middle carbon, so 2-chloropropane is the major product; 1-chloropropane forms only as a minor product.',
  '3.4 Markovnikov paragraph: new Fig 3.4.1 (old 3.4.1 renumbered 3.4.2 below)'),
 ('597073', 'fig-p597073-ring-numbering.svg', 'k2ring', 240,
  'Name: <strong>1-bromo-2-ethylcyclopentane</strong>.</p>', 'after',
  'Figure 2.9.4: Ring numbering for Example 1. Numbering starts at a substituent and runs toward the other one, giving locants 1 and 2 either way; the alphabetical tie-break gives the bromo carbon C1, and C3 to C5 continue around the ring.',
  '2.9 Lecture Example 1 solution: numbered ring'),
 ('597059', 'fig-p597059-aspartame-groups.svg', 'k2asp', 374,
  'Every O and N belongs to exactly one functional group. &#10003;</p>\n</div>', 'after',
  'Figure 1.6.7: The same carbonyl-first hunt on a bigger molecule, the sweetener aspartame. It has five functional groups: amine, carboxylic acid, amide, ester and aromatic ring. The N of the amide and the O&ndash;CH<sub>3</sub> oxygen of the ester belong to those groups and are not counted again as an amine or an ether.',
  '1.6 after Lecture Example 1 (acetaminophen): aspartame groups circled'),
 ('597118', 'fig-p597118-aspirin-stomach-blood.svg', 'k2asa', 660,
  'which is the form that crosses membranes.</p>', 'after',
  'Figure \\(\\PageIndex{1}\\): Aspirin in the stomach and in the blood. In strong stomach acid the &ndash;COOH group keeps its H, so the molecule is neutral and can cross cell membranes; at blood pH 7.4 it has lost its H, and the charged &ndash;COO<sup>&minus;</sup> form stays dissolved in water.',
  '6.10 Ionized or not at body pH: aspirin COOH vs COO-'),
]
RENUM = {
 '597116': ('Figure 6.8.2: Hydrolysis of aspirin.', 'Figure 6.8.3: Hydrolysis of aspirin.', '6.8 renumber old 6.8.2 -> 6.8.3 (new figure precedes it)'),
 '597081': ('Figure 3.4.1: 3-Methyl-1-butene.', 'Figure 3.4.2: 3-Methyl-1-butene.', '3.4 renumber old 3.4.1 -> 3.4.2 (new figure precedes it)'),
}
uploads, edits = [], {}
for p, fn, key, w, old, pos, cap, note in F:
    html = open(f'pages/live/{p}.html', encoding='utf-8').read()
    assert html.count(old) == 1, (p, old, html.count(old))
    svg = open(A + fn).read()
    alt = re.search(r'aria-label="([^"]*)"', svg).group(1)
    nat = int(re.search(r'<svg[^>]*\swidth="(\d+)"', svg).group(1))
    w = min(w, nat, 760)
    fig = (f'<figure class="figure"><img class="internal" alt="{alt}" width="{w}" style="max-width:100%;height:auto;" '
           f'src="/@api/deki/files/{{{{{key}}}}}/{fn}" fileid="{{{{{key}}}}}" /><figcaption>{cap} {CR}</figcaption></figure>')
    new = old + '\n' + fig if pos == 'after' else fig + '\n' + old
    uploads.append({'page': p, 'name': fn, 'path': A + fn, 'key': key})
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})
    if p in RENUM:
        o, n, nt = RENUM[p]; assert html.count(o) == 1, o
        edits[p].append({'old': o, 'new': n, 'count': 1, 'note': nt})
    # sanity: figure-number collisions after edit
    after = html.replace(old, new)
    if p in RENUM: after = after.replace(RENUM[p][0], RENUM[p][1])
    nums = re.findall(r'<figcaption[^>]*>Figure ([0-9.]+|\\\(\\PageIndex\{\d+\}\\\))', after)
    print(p, w, nums)
json.dump({'uploads': uploads, 'edits': edits}, open('/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/K2_figs.json', 'w'), indent=1, ensure_ascii=False)
