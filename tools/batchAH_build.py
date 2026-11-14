"""Batch AH (2026-11-14, final publication gate): DRAFT for the author's decision, not published.
Part A: lab-manual promises worded so they do not claim an unpublished manual exists (1.5, For Instructors, About).
Part B: small verified science/wording fixes found by the independent answer-key re-solve (all 15 chapters).
Part C: citrate synthase switched from "ligase" to transferase everywhere (author decision 2026-11-14).
Output: tools/batchAH_2026-11-14.json, tools/batchAH_sha_2026-11-14.json, audit/BATCH_AH_REVIEW.md, audit/preview/<id>.html
Run from the repo root: python3 tools/batchAH_build.py"""
import json, hashlib, re, html
pages, edits = {}, {}
def page(p):
    if p not in pages: pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
    return pages[p][1]
def e(p, old, new, note, why, part, count=1):
    t = page(p); assert t.count(old) == count, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': count, 'note': note, 'why': why, 'part': part})

# ---------- Part A: lab manual promises ----------
e('597058', '<li>The lab manual appendix has a VSEPR chart for organic geometries and an electronegativity chart you can use with this chapter.</li>',
  '<li>For a VSEPR chart of organic geometries, use the table &ldquo;Electron groups, molecular shapes and bond angles&rdquo; above; electronegativity values are in Figure 1.4.3.</li>',
  'F1. 1.5 In the Lab: "The lab manual appendix has a VSEPR chart ... and an electronegativity chart"',
  'The new lab manual is not published, so students cannot find that appendix. Both charts already exist in the book: the VSEPR table earlier on this page and the Pauling electronegativity figure in 1.4. When the manual is out, the appendix pointer can be added back (LAB_MANUAL_INTEGRATION_BACKLOG.md, row 2).', 'A')
e('597396', 'experiment numbers and links will be added when the manual is published.',
  'where a box already gives an experiment number, that number is provisional; numbers and links will be checked and added when the manual is published.',
  'F2. For Instructors: "experiment numbers and links will be added when the manual is published"',
  'Thirteen In the Lab boxes already print experiment numbers (1, 2, 3, 4, 6, 7, 8a, 8b, 9, 11, 12, 13, 14), so the sentence contradicted the book. The numbers themselves are not changed; whether they are final is unknown until the manual is done.', 'A')
e('597270', 'together with the free lab manual and the free study tools, qualify',
  'together with a free lab manual and the free study tools, qualify',
  'F3. About This Book, zero-textbook-cost sentence: "the free lab manual"',
  '"The free lab manual" reads as if a specific free manual is already available; the one written for this book is in preparation (For Instructors). "A free lab manual" keeps the ZTC condition true either way. Restore "the" when the manual is published.', 'A')
e('597396', 'pages hold 60&ndash;80 original problems per chapter',
  'pages hold 67&ndash;83 original problems per chapter',
  'F4. For Instructors: "60-80 original problems per chapter"',
  'Counted on 2026-11-14: Chapter 14 has 67, Chapters 8 and 10 have 81, Chapter 2 has 83 (plus 6 cumulative problems in Chapters 2-15).', 'A')

# ---------- Part B: verified science and wording ----------
e('597091', 'and a CH3 group two carbons further around the ring."',
  'and a CH3 group on the ring carbon directly across from the isopropyl group (2-isopropyl-5-methylphenol)."',
  'B1. 4.2 Figure alt text, thymol: methyl "two carbons further around the ring"',
  'Read the usual way (OH on C1, isopropyl on C2, two carbons further = C4) this describes 2-isopropyl-4-methylphenol, not thymol. In thymol the CH3 (C5) is para to the isopropyl (C2). Screen-reader users get the wrong structure; the visible figure is correct.', 'B')
e('597145', 'is sucrose with all eight OH groups esterified to fatty acids',
  'is sucrose with six to eight of its eight OH groups esterified to fatty acids',
  'B2. 9.2 Lecture Connection: olestra "all eight OH groups esterified"',
  'Commercial olestra is a mixture of sucrose hexa-, hepta- and octaesters (FDA food-additive listing, 21 CFR 172.867).', 'B')
e('597140', 'hydrolyzes starch that sticks to teeth into maltose and glucose that plaque bacteria can ferment',
  'hydrolyzes starch that sticks to teeth into maltose and other small sugars that plaque bacteria can ferment',
  'B3. 8.7 Dental Hygiene box: amylase gives "maltose and glucose"',
  'Alpha-amylase gives mainly maltose, maltotriose and short dextrins, very little free glucose (glucose comes from brush-border enzymes, as 13.3 says).', 'B')
e('597086', 'Nothing in this chapter dissolves in water.',
  'None of this chapter&rsquo;s hydrocarbons dissolves in water.',
  'B4. 3.9 Chapter Guide summary: "Nothing in this chapter dissolves in water"',
  'Section 3.8 includes phenol, aniline and benzoic acid; phenol dissolves to about 8 g per 100 mL. The paragraph is about hydrocarbons, and now says so.', 'B')
e('597063', 'which would need an O&ndash;H to be a real molecule.',
  'which would need an O&ndash;H and an extra H on the end carbon to be a real molecule (that would be C<sub>4</sub>H<sub>10</sub>O, not C<sub>4</sub>H<sub>8</sub>O).',
  'B5. 1.10 Problem 1.71(c) answer: open chain "would need an O-H"',
  'An open four-carbon chain with O on one end needs two more H (CH3CH2CH2CH2OH, C4H10O), not one. The conclusion (draw the ring) is unchanged. The text appears twice (inline answer and print answer key); both change.', 'B', count=2)
e('597208', 'After transamination the original amino acid contains only C, H, and O.',
  'After transamination the original amino acid has lost its &alpha;-amino group and is now an &alpha;-keto acid.',
  'B6. 15.8 Lecture Connection: after transamination the amino acid "contains only C, H, and O"',
  'False for amino acids with N or S in the side chain (Lys, Arg, His, Trp, Asn, Gln, Cys, Met). What transamination removes is the alpha-amino group.', 'B')
e('597217', 'phenylalanine hydroxylase that uses O<sub>2</sub> and NADPH to add an OH to the ring',
  'phenylalanine hydroxylase that uses O<sub>2</sub> to add an OH to the ring',
  'B7. 15.11 table, tyrosine row: phenylalanine hydroxylase "uses O2 and NADPH"',
  'The enzyme\'s reducing cofactor is tetrahydrobiopterin (BH4); NAD(P)H only regenerates BH4 afterward. Dropping "and NADPH" matches the section text above the table ("using O2 to add an -OH group").', 'B')

# ---------- Part C: citrate synthase is a transferase (author decision 2026-11-14: switch from the "ligase" convention) ----------
WHY = ('IUBMB classifies citrate synthase as a transferase (EC 2.3.3.1; before 2002 a lyase, EC 4.1.3.7), never a ligase, and the book\'s own rule '
       'says a ligase spends ATP; citrate synthase spends none. The author chose to switch the course to transferase (2026-11-14), which also matches '
       'Metabolic Marathon ("Dr. Dan: citrate synthase = transferase") and the Study Hub question bank, which already key Transferase.')
e('597166', 'also <em>aldolase</em> and most <em>synthases</em> (no ATP; citrate synthase is the course exception, a ligase)',
  'also <em>aldolase</em> and most <em>synthases</em> (no ATP; citrate synthase is the exception, a transferase)',
  'C1. 11.1 six-class table, lyase row: "citrate synthase is the course exception, a ligase"', WHY, 'C')
e('597166', 'The one exception in this course is <strong>citrate synthase</strong> (Chapter 14): it is classified as a <strong>ligase</strong>.',
  'The one exception you will meet is <strong>citrate synthase</strong> (Chapter 14): it is a <strong>transferase</strong>. It moves the acetyl group from acetyl CoA onto oxaloacetate (CoA&ndash;SH leaves), and it spends no ATP, so it is not a ligase.',
  'C2. 11.1 "Two traps": citrate synthase "is classified as a ligase"', WHY, 'C')
e('597173', '<strong>ligase</strong> (ATP is spent and two molecules become one; synthetase, carboxylase; plus citrate synthase, the course exception).',
  '<strong>ligase</strong> (ATP is spent and two molecules become one; synthetase, carboxylase). Citrate synthase is the one synthase that is not a lyase: it is a transferase that moves an acetyl group onto oxaloacetate.',
  'C3. 11.8 Key Idea 2: ligase list "plus citrate synthase, the course exception"', WHY, 'C')
e('597173', 'the one exception in this course is citrate synthase (Chapter 14), which is classified as a ligase.',
  'the one exception is citrate synthase (Chapter 14), a transferase: it moves the acetyl group of acetyl CoA onto oxaloacetate and spends no ATP.',
  'C4. 11.8 Common Mistakes: citrate synthase "is classified as a ligase"', WHY, 'C')
e('597202', 'citrate synthase (<strong>ligase</strong> in this course: it joins two molecules)',
  'citrate synthase (<strong>transferase</strong>: it moves the acetyl group from CoA onto oxaloacetate; no ATP is spent, so it is not a ligase)',
  'C5. 14.3 step table, step 1 enzyme class: "ligase in this course"', WHY, 'C')
e('597205', 'Citrate synthase is treated as a ligase, aconitase and fumarase are lyases,',
  'Citrate synthase is a transferase (no ATP, so not a ligase), aconitase and fumarase are lyases,',
  'C6. 14.6 Chapter Guide, Key Idea: "Citrate synthase is treated as a ligase"', WHY, 'C')
e('488232', 'such as DNA ligase (this course also treats citrate synthase, which joins acetyl CoA and oxaloacetate, as a ligase).',
  'such as DNA ligase.',
  'C7. Glossary "ligase": "this course also treats citrate synthase ... as a ligase"', WHY, 'C')
e('488232', 'such as kinases, aminotransferases and thiolase.',
  'such as kinases, aminotransferases, thiolase and citrate synthase (which moves an acetyl group onto oxaloacetate).',
  'C8. Glossary "transferase": add citrate synthase as an example', WHY, 'C')

# ---------- Part D: version note ----------
e('597270', '(last updated November 13, 2026)', '(last updated November 14, 2026)',
  'D1. About This Book: last-updated date', 'Batches AG and AH were published on 2026-11-14.', 'D')
e('597270', '<li><strong>1.2 (November 13, 2026).</strong>',
  '<li><strong>Update (November 14, 2026).</strong> Final pre-release check: citrate synthase is now classified as a transferase (Sections 11.1, 11.8, 14.3, 14.6 and the Glossary); references to the lab manual, which is still in preparation, were reworded; small corrections in 1.10, 3.9, 4.2, 8.7, 9.2, 15.8 and 15.11.</li>\n<li><strong>1.2 (November 13, 2026).</strong>',
  'D2. About This Book: version history line for 2026-11-14', 'Records what changed in this update.', 'D')

h = lambda s: hashlib.sha256(s.encode()).hexdigest()
sha = {p: {'before': h(v[0]), 'after': h(v[1])} for p, v in pages.items()}
for p, v in pages.items(): open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(v[1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAH_2026-11-14.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAH_sha_2026-11-14.json', 'w'))
plain = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()
names = {'597058': '1.5', '597396': 'For Instructors', '597270': 'About This Book', '597091': '4.2', '597145': '9.2', '597140': '8.7',
         '597086': '3.9 Chapter Guide', '597063': '1.10 Practice Problems', '597208': '15.8', '597217': '15.11', '597166': '11.1', '597173': '11.8 Chapter Guide', '597202': '14.3', '597205': '14.6 Chapter Guide', '488232': 'Glossary'}
parts = {'A': 'Part A. Lab-manual promises (neutral wording; experiment numbers untouched)', 'B': 'Part B. Verified science and wording fixes (P2)', 'C': 'Part C. Citrate synthase is a transferase (author decided 2026-11-14 to switch from ligase)', 'D': 'Part D. Version note'}
out = ['# Batch AH review (draft, not published)', '',
       'Built 2026-11-14 by `tools/batchAH_build.py` from `pages/live/` (which matched all 199 live pages by SHA-256 on 2026-11-14). Approve all, or name rows to drop or reword. The matching bank change (fb-3B-2030) is in `bank/metabolism.json`; the live ADAPT question still needs updating.', '']
for part, title in parts.items():
    out += ['## ' + title, '']
    for p, es in edits.items():
        for x in es:
            if x['part'] != part: continue
            out += ['**%s** (%s, page %s)' % (x['note'], names[p], p), '', 'Why: ' + html.unescape(x['why']), '',
                    '- Before: ' + plain(x['old'])[:900], '- After: ' + plain(x['new'])[:900], '']
out += ['## Publish method (after approval)', '', 'Same as batches M-AG: push the branch, have the signed-in LibreTexts tab fetch `tools/batchAH_2026-11-14.json` at that commit, dry-run against live using the `before` hashes in `tools/batchAH_sha_2026-11-14.json`, save, read back, sync `pages/live`. Update the About This Book "last updated" date and add a version-history line in the same step.', '']
open('audit/BATCH_AH_REVIEW.md', 'w').write('\n'.join(out))
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
