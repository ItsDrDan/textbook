"""Batch AM (2026-11-17): tie the book to the companion CHEM 3B Lab Manual (itsdrdan.github.io/chem3b-lab-manual,
main 2a2ac86: 15 experiments + 2 workshops).
Part A: every "In the Lab" box names the manual's experiment (new numbering), says only what that experiment does
        (checked against source/src/expNN.js), and ends with a link to the experiment's PDF. New boxes on 5.5
        (Chirality Stations workshop) and 8.4 (Types of Carbohydrates workshop). Drafts in tools/batchAM_parts/.
Part B: 4.10 text outside the box that still described the old NaOH lab test.
Part C: front matter: lab manual link on the book home page, a Companion lab manual box and version note in About,
        an experiment-to-section table in Course Outline Alignment, For Instructors no longer says "in preparation".
Closes audit/LAB_MANUAL_INTEGRATION_BACKLOG.md rows 1-26 except the decisions listed in audit/BATCH_AM_REVIEW.md.
Output: tools/batchAM_2026-11-17.json, tools/batchAM_sha_2026-11-17.json, audit/BATCH_AM_REVIEW.md, audit/preview/<id>.html
Run from the repo root: python3 tools/batchAM_build.py"""
import json, hashlib, html as H

pages, edits, order = {}, {}, []
SKIP = {'6.11 Example 2: pentyl acetate odor matched to Exp 6'}  # held for the author (pear vs banana), see review


def page(p):
    p = str(p)
    if p not in pages:
        pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
        order.append(p)
    return pages[p][1]


def e(p, old, new, note, why, part='A', count=1):
    if note in SKIP:
        return
    p = str(p)
    t = page(p)
    assert t.count(old) == count, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': count, 'note': note, 'why': why, 'part': part})


for f in ['tiein_ch01_05.py', 'tiein_ch06_09.py', 'tiein_ch10_15.py']:
    exec(open('tools/batchAM_parts/' + f, encoding='utf-8').read(), {'e': e})

M = 'https://itsdrdan.github.io/chem3b-lab-manual/'
MLINK = '<a href="%s" target="_blank" rel="noopener">itsdrdan.github.io/chem3b-lab-manual</a>' % M

# ---------- Part B: 4.10 outside the box ----------
e('597099', '<li>Use the NaOH reaction as a laboratory test to distinguish a phenol from an alcohol.</li>',
  '<li>Use the NaOH reaction to distinguish a phenol from an alcohol.</li>',
  '4.10 objective: NaOH "as a laboratory test"',
  'Experiment 4 no longer runs a NaOH test (exp04.js: pH paper, FeCl3, Lucas). The chemistry objective stays.', 'B')
e('597099', '<h2 class="editable">Reaction of phenol with sodium hydroxide: a lab test</h2>',
  '<h2 class="editable">Reaction of phenol with sodium hydroxide: a bench test</h2>',
  '4.10 heading: "a lab test"', 'Same reason; it is still a classic bench test, just not one in this manual.', 'B')
e('597099', 'and hydroxide distinguishes a phenol from an alcohol. You will use both ideas in the lab unknown.</p>',
  'and hydroxide distinguishes a phenol from an alcohol. These are classic bench tests; in Experiment 4 you pick out the phenol with the iron(III) chloride test instead (Section 4.7).</p>',
  '4.10: "You will use both ideas in the lab unknown"',
  'Neither Experiment 4 nor Experiment 6 runs a NaHCO3 or NaOH test to tell phenols from alcohols.', 'B')

# ---------- Part C: front matter ----------
# Book home page (488223): one note under the license box
e('488223', 'provided where it appears.</p></div>',
  'provided where it appears.</p></div>\n<div class="mt-note" style="margin-top:1em"><p><strong>Companion lab manual.</strong> '
  'The free CHEM 3B Lab Manual (Daniel Kwasniewski and Alexandra Aloia, CC BY 4.0) goes with this book: 15 experiments and '
  '2 workshops, as PDF and Word files, at ' + MLINK + '. Each chapter&rsquo;s &ldquo;In the Lab&rdquo; boxes link to the '
  'matching experiment.</p></div>',
  'Home page: lab manual link', 'Author request 2026-11-17: a link in the front matter to where the lab manual can be found.', 'C')

# About This Book (597270)
e('597270', 'together with a free lab manual and the free study tools, qualify',
  'together with the free companion lab manual and the free study tools, qualify',
  'About, ZTC sentence: restore "the free ... lab manual"', 'Batch AH F3 said to restore it once the manual is published free; it now is (CC BY 4.0).', 'C')
e('597270', 'A printed copy may be offered at cost, but it is optional.</p>\n</div>',
  'A printed copy may be offered at cost, but it is optional.</p>\n</div>\n\n<div class="box-note">\n<p class="boxtitle">Companion lab manual</p>\n'
  '<p>The <strong>CHEM 3B Lab Manual</strong> by Daniel Kwasniewski and Alexandra Aloia was written to go with this book. '
  'It has 15 experiments and 2 workshops, each with safety and waste notes, a pre-lab, a report sheet and questions, plus appendices '
  '(lab techniques, functional groups, the electronegativity table and more). It is free and openly licensed (CC BY 4.0): read or '
  'download the whole manual or one experiment at a time, as PDF or Word, at ' + MLINK + '.</p>\n'
  '<p>In this book, the &ldquo;In the Lab&rdquo; boxes name the experiment that goes with a section and link to it; the '
  '<a href="/@go/page/597272">Course Outline Alignment</a> page lists every experiment with its sections. The Fall 2026 edition '
  'of the manual is a working draft, so your instructor will tell you which experiments your section runs.</p>\n</div>',
  'About: new Companion lab manual box', 'Author request 2026-11-17 (front-matter link to the lab manual).', 'C')
e('597270', 'the laboratory itself is covered by the CHEM 3B lab manual.</td>',
  'the laboratory itself is covered by the companion CHEM 3B Lab Manual (see Companion lab manual, above).</td>',
  'About, outcome 5 row', 'Points to the new box and the published manual.', 'C')
e('597270', '<li><strong>Update (November 14, 2026).</strong>',
  '<li><strong>Update (November 17, 2026).</strong> The companion CHEM 3B Lab Manual is published (free, CC BY 4.0). Every '
  '&ldquo;In the Lab&rdquo; box now names its experiment with the manual&rsquo;s numbering, describes what that experiment '
  'actually does, and links to it; new boxes in 5.5 (Chirality Stations workshop) and 8.4 (Types of Carbohydrates workshop); '
  'the boxes in 13.9, 15.5 and 15.7 describe a urine-analysis lab that is not in the manual and now say so.</li>\n'
  '<li><strong>Update (November 14, 2026).</strong>',
  'About, version history entry', 'Records this batch for readers.', 'C')

# Course Outline Alignment (597272): Laboratory section with the crosswalk table
PDF = M + 'pdf/experiments/'
ROWS = [  # (label, pdf, [(section, page id)])
    ('Experiment 1 &ndash; Functional Groups', 'Exp01_FunctionalGroups.pdf', [('1.5', 597058)]),
    ('Experiment 2 &ndash; Structures of Alkanes', 'Exp02_StructuresOfAlkanes.pdf', [('2.4', 597068)]),
    ('Experiment 3 &ndash; Hydrocarbons', 'Exp03_Hydrocarbons.pdf', [('2.1', 597065), ('3.4', 597081), ('3.7', 597084)]),
    ('Experiment 4 &ndash; Alcohols and Phenols', 'Exp04_AlcoholsPhenols.pdf', [('4.3', 597092), ('4.5', 597094), ('4.7', 597096), ('4.10', 597099)]),
    ('Experiment 5 &ndash; Aldehydes and Ketones', 'Exp05_AldehydesKetones.pdf', [('5.2', 597103), ('5.4', 597105)]),
    ('Experiment 6 &ndash; Carboxylic Acids and Esters', 'Exp06_CarboxylicAcidsEsters.pdf', [('6.4', 597112), ('6.6', 597114), ('6.7', 597115), ('6.8', 597116)]),
    ('Experiment 7 &ndash; Amines and Amides', 'Exp07_AminesAmides.pdf', [('7.3', 597123), ('7.7', 597127)]),
    ('Experiment 8 &ndash; Tests for Carbohydrates', 'Exp08_TestsForCarbohydrates.pdf', [('8.5', 597138), ('8.7', 597140)]),
    ('Experiment 9 &ndash; Lipids', 'Exp09_Lipids.pdf', [('9.2', 597145)]),
    ('Experiment 10 &ndash; Aspirin and Analgesics', 'Exp10_Aspirin.pdf', [('6.7', 597115)]),
    ('Experiment 11 &ndash; Amino Acids', 'Exp11_AminoAcids.pdf', [('10.3', 597156)]),
    ('Experiment 12 &ndash; Peptides and Proteins', 'Exp12_PeptidesProteins.pdf', [('10.3', 597156), ('10.10', 597163), ('15.7', 597215)]),
    ('Experiment 13 &ndash; Enzymes', 'Exp13_Enzymes.pdf', [('11.3', 597168), ('13.3', 597191)]),
    ('Experiment 14 &ndash; Vitamins', 'Exp14_Vitamins.pdf', [('11.5', 597170)]),
    ('Experiment 15 &ndash; Nucleic Acids and DNA Extraction', 'Exp15_NucleicAcids.pdf', [('12.3', 597177)]),
    ('Workshop: Types of Carbohydrates', 'Workshop_Carbohydrates.pdf', [('8.4', 597137)]),
    ('Workshop: Chirality Stations', 'Workshop_Chirality.pdf', [('5.5', 597106)]),
]
trs = ''.join('<tr><td data-th="Lab manual"><a href="%s%s" target="_blank" rel="noopener">%s</a></td><td data-th="Book sections">%s</td></tr>' % (
    PDF, pdf, lab, ', '.join('<a href="/@go/page/%d">%s</a>' % (pid, s) for s, pid in secs)) for lab, pdf, secs in ROWS)
LAB_OLD = ('<h2 class="editable">Laboratory</h2><p>The outline&rsquo;s laboratory topics are taught in the CHEM 3B lab manual. '
           'Each chapter&rsquo;s &ldquo;In the Lab&rdquo; boxes connect the reading to those experiments.</p>')
LAB_NEW = ('<h2 class="editable">Laboratory</h2><p>The outline&rsquo;s laboratory topics are taught in the companion '
           '<strong>CHEM 3B Lab Manual</strong> (Daniel Kwasniewski and Alexandra Aloia, CC BY 4.0), free at ' + MLINK + '. '
           'Each chapter&rsquo;s &ldquo;In the Lab&rdquo; boxes connect the reading to those experiments; the table lists '
           'the sections whose boxes point to each one.</p>'
           '<table class="mt-responsive-table" style="width:100%;"><thead><tr><th>Lab manual (PDF)</th><th>Book sections</th></tr></thead><tbody>'
           + trs + '</tbody></table>'
           '<p>Two outline lab topics are not yet in the manual: digestion of foods (Section 13.3 ties it to the amylase work in '
           'Experiment 13) and analysis of simulated urine for glucose, ketone bodies and protein (Sections '
           '<a href="/@go/page/597195">13.9</a>, <a href="/@go/page/597213">15.5</a> and <a href="/@go/page/597215">15.7</a> '
           'describe it for courses that run it).</p>')
e('597272', LAB_OLD, LAB_NEW, 'Course Outline Alignment: Laboratory section with experiment-to-section table',
  'Author request 2026-11-17: tie experiments to sections; this is the one-page crosswalk (backlog step 1).', 'C')

# For Instructors (597396)
e('597396', '<li>A CHEM 3B lab manual written to accompany this book is in preparation. The &ldquo;In the Lab&rdquo; boxes already tie '
  'each chapter to the lab topics in the course outline; where a box already gives an experiment number, that number is provisional; '
  'numbers and links will be checked and added when the manual is published.</li>',
  '<li>The companion <strong>CHEM 3B Lab Manual</strong> (Daniel Kwasniewski and Alexandra Aloia, CC BY 4.0) is free at ' + MLINK +
  ': 15 experiments and 2 workshops, each as PDF and as an editable Word file, plus the full manual. Each &ldquo;In the Lab&rdquo; '
  'box names its experiment and links to that experiment&rsquo;s PDF; the <a href="/@go/page/597272">Course Outline Alignment</a> '
  'page has the experiment-to-section table. The Fall 2026 edition is a working draft, so experiment numbers may still change; '
  'the manual&rsquo;s page always has the current files. Digestion of foods and simulated-urine analysis (outline lab topics) are '
  'not yet in the manual.</li>',
  'For Instructors: lab manual published, link', 'Replaces the "in preparation / provisional numbers" bullet from batch AH F2.', 'C')

# ---------- output ----------
h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAM_2026-11-17.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAM_sha_2026-11-17.json', 'w'))
n = sum(len(v) for v in edits.values())
print(n, 'edits on', len(edits), 'pages')
