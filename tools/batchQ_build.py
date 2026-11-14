"""Batch Q (master refinement pass, 2026-11-13). DRAFT ONLY until the instructor says "publish".
Count-checked against pages/live (which matched the live book after batch P and the Index tag moves; page bodies only).
Parts:
  A  stale "This is version 1.1" line (About This Book)
  B  answers for the 24 inherited exercises that had none (inline + print key), and the two list items that sat outside their box (4.2)
  C  exemplar section 4.5 (oxidation defined at first use; Summary; outline bridge)
  D  pedagogy edits from the three chapter reviews (audit/PEDAGOGY-AND-READABILITY-REVIEW.md)
  E  Glossary: Spanish equivalents, definitions and section pointers (audit/glossary edits)
  F  Rosa / Valley Connection edits and Try It widget selections, when their JSON files exist in audit/
Output: tools/batchQ_2026-11-13.json {uploads, edits} and tools/batchQ_sha_2026-11-13.json."""
import json, re, hashlib, os

L = 'pages/live/'
pages, edits, uploads, orig, skipped = {}, {}, [], {}, []


def page(p):
    p = str(p)
    if p not in pages:
        pages[p] = open(L + p + '.html', encoding='utf-8').read(); orig[p] = pages[p]
    return pages[p]


def e(p, old, new, note, n=1):
    p = str(p); t = page(p); assert t.count(old) == n, (p, note, t.count(old))
    assert old != new, (p, note)
    pages[p] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})


def soft(p, old, new, note, n=1):
    """edit from a reviewer's list: skip (and report) instead of failing if an earlier edit already changed the spot"""
    if page(p).count(old) == n and old != new: e(p, old, new, note, n=n)
    else: skipped.append((str(p), note[:70], page(p).count(old)))


# ---------------- A: version line ----------------
e('597270', '<p>This is version 1.1. It has been reviewed by the author', '<p>This is version 1.2. It has been reviewed by the author', 'A About This Book: stale version number (page header and history already say 1.2)')

# ---------------- B: answers for inherited exercises that had none ----------------
sub = lambda s: re.sub(r'(?<=[A-Za-z\)])(\d+)', r'<sub>\1</sub>', s)
ol = lambda items: '<ol style="list-style-type: lower-alpha;">\n' + ''.join('    <li>' + i + '</li>\n' for i in items) + '</ol>'
ANS = {
 '597091': {1: ol(['1,2-propanediol (propane-1,2-diol): three carbons, with OH groups on C1 and C2.',
                   '1-methylcyclopentanol: the ring carbon that holds the OH is C1, and the CH<sub>3</sub> is on that same carbon.']),
            2: ol([sub('CH3CH2CH(OH)CH2CH2CH2CH3') + ': seven carbons with the OH on C3.',
                   sub('CH3CH(CH3)CH(OH)CH2CH2CH3') + ': six carbons, a CH<sub>3</sub> on C2 and the OH on C3.'])},
 '597093': {1: '<p>cyclopentene + H<sub>2</sub>O &rarr; cyclopentanol, with H<sub>3</sub>PO<sub>4</sub> written over the arrow (C<sub>5</sub>H<sub>8</sub> + H<sub>2</sub>O &rarr; C<sub>5</sub>H<sub>9</sub>OH). The H goes to one carbon of the C=C and the OH to the other; the ring is symmetrical, so only one product is possible.</p>'},
 '597094': {1: ol(['3-Methyl-3-hexanol is a tertiary alcohol (the OH carbon has no H), so: no reaction.',
                   '2-Methyl-1-propanol is a primary alcohol. [O] gives the aldehyde 2-methylpropanal, ' + sub('(CH3)2CHCHO') + ', and further oxidation gives the carboxylic acid 2-methylpropanoic acid, ' + sub('(CH3)2CHCOOH') + '.',
                   '3-Methyl-2-hexanol is a secondary alcohol. [O] gives the ketone 3-methyl-2-hexanone, ' + sub('CH3COCH(CH3)CH2CH2CH3') + '.'])},
 '597097': {1: ol(['dibutyl ether (two butyl groups on the oxygen)', 'cyclobutyl ethyl ether'])},
 '597102': {1: ol(['Ketone (the C=O carbon is bonded to two carbons): ethyl propyl ketone.',
                   'Aldehyde (the C=O carbon carries an H).',
                   'Ketone: cyclobutyl methyl ketone.']),
            2: ol(['3,3-dimethylbutanal (the CHO carbon is C1)', '2-methyl-3-hexanone (number from the end nearer the C=O)', 'cyclobutanone']),
            3: ol([sub('CH3CH2CHBrCH2CHICH2CHO') + ' (seven carbons; CHO is C1, I on C3, Br on C5)',
                   sub('CH3COCH2CH(CH2CH3)CHBrCH2CH3') + ' (seven carbons; C=O on C2, ethyl on C4, Br on C5)'])},
 '597109': {1: ol(['5-chloropentanoic acid (the COOH carbon is C1)', '2-bromo-4-methylpentanoic acid']),
            2: '<p>' + sub('CH3CH(CH3)CHBrCH2CH2COOH') + ' (six carbons counting the COOH carbon as C1; Br on C4, CH<sub>3</sub> on C5)</p>'},
 '597112': {1: ol(['HCOOH + H<sub>2</sub>O &#8652; HCOO<sup>&minus;</sup> + H<sub>3</sub>O<sup>+</sup>',
                   'ClC<sub>6</sub>H<sub>4</sub>COOH + H<sub>2</sub>O &#8652; ClC<sub>6</sub>H<sub>4</sub>COO<sup>&minus;</sup> + H<sub>3</sub>O<sup>+</sup> (only the COOH hydrogen is lost; the ring and the Cl do not change)']),
            2: ol(['C<sub>6</sub>H<sub>5</sub>COOH + NaOH &rarr; C<sub>6</sub>H<sub>5</sub>COO<sup>&minus;</sup>Na<sup>+</sup> + H<sub>2</sub>O (sodium benzoate and water)',
                   'C<sub>6</sub>H<sub>5</sub>COOH + NaHCO<sub>3</sub> &rarr; C<sub>6</sub>H<sub>5</sub>COO<sup>&minus;</sup>Na<sup>+</sup> + H<sub>2</sub>O + CO<sub>2</sub> (the same salt, plus bubbles of CO<sub>2</sub>)'])},
 '597113': {1: ol(['ethyl pentanoate (IUPAC); ethyl valerate (common). The alcohol part, ethyl, is named first.',
                   'propyl propanoate (IUPAC); propyl propionate (common)']),
            2: '<p>' + sub('CH3CH2CH2CH2COO') + '&ndash;C<sub>6</sub>H<sub>5</sub>: the five-carbon acid part (pentanoate) with a benzene ring on the single-bonded oxygen.</p>'},
 '597116': {1: '<p>' + sub('CH3CH2CH2COOCH3') + ' + H<sub>2</sub>O &#8652; ' + sub('CH3CH2CH2COOH') + ' + ' + sub('CH3OH') + ', with H<sup>+</sup> over the arrows. The products are butanoic acid and methanol.</p>',
            2: '<p>' + sub('CH3CH2COOCH2CH3') + ' + NaOH &rarr; ' + sub('CH3CH2COO') + '<sup>&minus;</sup>Na<sup>+</sup> + ' + sub('CH3CH2OH') + '. The products are sodium propanoate (a salt, because the base is used up) and ethanol.</p>'},
 '597121': {1: ol(['isopropylmethylamine (N-methyl-2-propanamine); secondary (2&deg;): two carbon groups on N',
                   'diethylmethylamine; tertiary (3&deg;)', 'butylamine (1-butanamine); primary (1&deg;)', 'dipropylamine; secondary (2&deg;)']),
            2: ol([sub('CH3CH2NHCH(CH3)2') + '; secondary (2&deg;)', sub('(CH3CH2)2NCH2CH2CH3') + '; tertiary (3&deg;)']),
            3: '<p><em>o</em>-chloroaniline (2-chloroaniline): the Cl is on the ring carbon next to the one that holds the NH<sub>2</sub>.</p>',
            4: '<p>A benzene ring with an NH<sub>2</sub> group and, directly across the ring (para), an isopropyl group, ' + sub('CH(CH3)2') + '. One carbon group on N, so it is a primary (1&deg;) amine.</p>',
            5: '<p>' + sub('ClCH2CH(NH2)CH(CH2CH3)CH2CH2CH2CH3') + ' (seven carbons; Cl on C1, NH<sub>2</sub> on C2, ethyl on C3)</p>',
            6: ol(['ethylammonium ion', 'triethylammonium ion', 'dipropylammonium ion', 'tetrabutylammonium ion'])},
 '597123': {1: '<p>The acid is HI (hydroiodic acid) and the base is tripropylamine, ' + sub('(CH3CH2CH2)3N') + '. The amine accepts the H<sup>+</sup>, and the I<sup>&minus;</sup> is left as the other ion of the salt.</p>'},
 '597127': {1: ol([sub('CH3CH2CONH2') + ' + H<sub>2</sub>O &rarr; ' + sub('CH3CH2COOH') + ' + NH<sub>3</sub> (propanoic acid and ammonia)',
                   sub('CH3(CH2)4CONH2') + ' + H<sub>2</sub>O &rarr; ' + sub('CH3(CH2)4COOH') + ' + NH<sub>3</sub> (hexanoic acid and ammonia)'])
               + '<p>In both, the C(=O)&ndash;N bond is the one that breaks. With HCl the ammonia ends up as NH<sub>4</sub><sup>+</sup>; with NaOH the acid ends up as its carboxylate salt.</p>'},
}
SEC = {'597091': '4.2', '597093': '4.4', '597094': '4.5', '597097': '4.8', '597102': '5.1', '597109': '6.1', '597112': '6.4', '597113': '6.5',
       '597116': '6.8', '597121': '7.1', '597123': '7.3', '597127': '7.7'}

# 4.2: the second part of each exercise sat outside its box as a bulleted item; move it back inside as part (b)
t = page('597091')
m = re.search(r'(</li>\n</ol>)\n(</div></section>)\n\n<ul>\n    (<li><img alt="A cyclopentane ring \(pentagon\) with an OH and a CH3 group on the same carbon\."[^>]*/></li>)\n</ul>', t)
assert m, '4.2 ex1 spill'
e('597091', m.group(0), '</li>\n    ' + m.group(3) + '\n</ol>\n' + m.group(2), 'B 4.2 Exercise 1: part (b) was outside the exercise box as a bullet')
old = '    <li>3-heptanol</li>\n</ol>\n</div></section>\n\n<ul>\n    <li>2-methyl-3-hexanol</li>\n</ul>'
e('597091', old, '    <li>3-heptanol</li>\n    <li>2-methyl-3-hexanol</li>\n</ol>\n</div></section>', 'B 4.2 Exercise 2: part (b) was outside the exercise box as a bullet')

TAIL = 'the section text above keeps its own license and attribution.</p>\n</div></div>'
n_ans = 0
for p, d in ANS.items():
    t = page(p)
    starts = [m.start() for m in re.finditer(r'<section class="box-exercise">', t)]
    spots = {}
    for st in starts:
        en = t.find('</section>', st); body = t[st:en]
        num = int(re.search(r'PageIndex\{(\d+)\}', body).group(1))
        if '<details' not in body: spots[num] = body
    assert sorted(spots) == sorted(d), (p, sorted(spots), sorted(d))
    for num in sorted(d):
        body = spots[num]; assert body.endswith('\n</div>') and page(p).count(body + '</section>') == 1, (p, num)
        inline = '\n<div class="hideprint answer-inline"><details class="hideprint"><summary>Answer</summary><div>' + d[num] + '</div></details></div>'
        e(p, body + '</section>', body[:-len('\n</div>')] + '\n' + inline + '\n</div></section>', f'B {SEC[p]} Exercise {num}: inherited exercise had no answer anywhere; answer added (worked by hand, see audit/CHEMISTRY-AND-ANSWERKEY-ERRATA.md)')
        n_ans += 1
    items = ''.join('<div class="answer-key-item"><p style="page-break-after:avoid;break-after:avoid"><strong>Exercise ' + SEC[p] + '.' + str(num) + '</strong></p><div>' + d[num] + '</div></div>\n' for num in sorted(d))
    t = page(p)
    if 'showprint answer-key' in t:
        end = '</div></div>\n</div></div>'; assert t.endswith(end) and t.count(end) == 1, p
        e(p, end, items + end, f'B {SEC[p]}: exercise answers added to the existing print key')
    else:
        assert t.endswith(TAIL) and t.count(TAIL) == 1, p
        key = '\n\n<div class="showprint answer-key"><div class="mt-section"><h2 class="editable">Answers to Exercises</h2>\n' + items + '</div></div>'
        e(p, TAIL, TAIL[:-len('\n</div></div>')] + key + '\n</div></div>', f'B {SEC[p]}: print-only answer key added (same markup as 2.5)')

# ---------------- C: exemplar, Section 4.5 ----------------
e('597094', '<p>Primary and secondary alcohols are readily oxidized. We saw earlier',
  '<p>Primary and secondary alcohols are readily oxidized. For an organic molecule, oxidation means gaining bonds to oxygen or losing bonds to hydrogen; here the alcohol loses two H atoms and its C&ndash;O single bond becomes a C=O double bond. We saw earlier',
  'C 4.5: oxidation was used for a whole section before it was defined (the definition sat only in the Lecture Connection)')
e('597094', 'Primary alcohols are oxidized to form aldehydes. Secondary alcohols',
  'Primary alcohols are oxidized to form aldehydes, which are oxidized further to carboxylic acids. Secondary alcohols',
  'C 4.5 Summary stopped at the aldehyde; the page, the Valley box and Example 1 all carry it on to the acid')

# ---------------- D: pedagogy edits from the chapter reviews ----------------
for f in ('audit/edits/pedagogy_ch01-05.json', 'audit/edits/pedagogy_ch06-10.json', 'audit/edits/pedagogy_ch11-15.json'):
    for x in json.load(open(f)):
        new = x['new']
        if str(x['page_id']) == '597202' and '2GTP' in new:   # keep the book's "2 ATP" wording for the citric acid cycle (convention table)
            new = 'Two turns of the citric acid cycle per glucose molecule yield \\(\\ce{6NADH}\\), \\(\\ce{2FADH_{2}}\\), and \\(\\ce{2ATP}\\), worth 20 ATP in all after electron transport (Section 14.5)'
        soft(x['page_id'], x['old'], new, 'D ' + x['severity'] + ' ' + str(x['section'])[:60] + ': ' + x['reason'][:200])

# ---------------- E: Glossary ----------------
for x in json.load(open('audit/edits/glossary.json')):
    soft('488232', x['old'], x['new'], 'E Glossary (' + x.get('confidence', '') + '): ' + x['reason'][:200])

# ---------------- F: optional lists ----------------
for f, tag in (('audit/edits/rosa_valley.json', 'F Rosa/Valley'), ('audit/edits/widgets.json', 'F Try It selection')):
    if os.path.exists(f):
        for x in json.load(open(f)):
            if x.get('skip'): continue
            soft(x['page_id'], x.get('old', x.get('old_src')), x.get('new', x.get('new_src')), tag + ' ' + str(x.get('section', '')) + ': ' + x.get('reason', '')[:200], n=2 if 'occurs twice' in str(x.get('section', '')) + x.get('reason', '') else 1)

sha = {p: {'before': hashlib.sha256(orig[p].encode()).hexdigest(), 'after': hashlib.sha256(pages[p].encode()).hexdigest()} for p in edits}
json.dump(sha, open('tools/batchQ_sha_2026-11-13.json', 'w'), indent=0)
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchQ_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
os.makedirs('audit/preview', exist_ok=True)
for p in edits: open(f'audit/preview/{p}.html', 'w', encoding='utf-8').write(pages[p])
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', n_ans, 'exercise answers')
print('skipped:', skipped)
