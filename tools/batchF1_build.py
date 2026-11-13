"""Batch F1 (review 2026-11-12, elevation): the 15 recommended items.
- 11 text items (worked examples, a table, the 15-15 rule, Table 14.2.1 yields) drafted into
  tools/batchF1_text_drafts_2026-11-12.json; codons, deletions, balancing and charges re-checked.
- 4 new figures drawn by tools/batchF_figs.py (house style, landscape so they print at full width):
  11.4 rate vs [S] for inhibitors; 12.3 replication fork; 8.4 Fischer -> Haworth in three steps; 12.6 one elongation cycle (P/A sites).
Output: tools/batchF1_2026-11-12.json {uploads, edits} (same format as batches B2/E3; {{key}} = new file id).
"""
import json

L = 'pages/live/'
A = 'figures/pages/batchF/'
CR = '(Diagram: Daniel Kwasniewski, CC BY 4.0.)'
text = json.load(open('tools/batchF1_text_drafts_2026-11-12.json'))
uploads, edits = [], {p: list(v) for p, v in text.items()}


def page(p): return open(L + p + '.html', encoding='utf-8').read()


def svgalt(fname):
    import re
    return re.search(r'aria-label="([^"]*)"', open(A + fname).read()).group(1)


def fig(p, key, fname, width, label, caption, old, before=True, note=''):
    html = (f'<figure><img class="internal" alt="{svgalt(fname)}" width="{width}" style="max-width:100%;height:auto;" '
            f'src="/@api/deki/files/{{{{{key}}}}}/{fname}" fileid="{{{{{key}}}}}" />\n'
            f'<figcaption>Figure {label}: {caption} {CR}</figcaption>\n</figure>\n')
    assert page(p).count(old) == 1, (p, note)
    new = (html + old) if before else (old + '\n' + html)
    uploads.append({'page': p, 'name': fname, 'path': A + fname, 'key': key, 'old_fileid': None})
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})


fig('597169', 'rate', 'fig-p597169-rate-inhibitors.svg', 760, '\\(\\PageIndex{2}\\)',
    'Reaction rate against substrate concentration with no inhibitor, a competitive inhibitor and a noncompetitive inhibitor. More substrate restores the maximum rate only for the competitive inhibitor.',
    '<table class="mt-responsive-table"><caption>Types of enzyme inhibition compared</caption>', True, '11.4 rate vs [S] figure')
fig('597177', 'fork', 'fig-p597177-replication-fork.svg', 760, '12.3.4',
    'A replication fork. Helicase unwinds the DNA; primase lays down RNA primers; DNA polymerase builds each new strand 5&prime;&rarr;3&prime;, continuously on the leading strand and in Okazaki fragments on the lagging strand; ligase joins the fragments.',
    '</ul>\n<div class="box-note">\n<p class="boxtitle">Professor Tip</p>\n<p>For exams ', True, '12.3 replication fork figure')
fig('597137', 'haw', 'fig-p597137-fischer-to-haworth.svg', 760, '8.4.5',
    'From Fischer to Haworth in three steps, for D-glucose: rotate, twist, close. The new OH on C1 points down in the &alpha; anomer and up in the &beta; anomer.',
    '<p><strong>From Haworth back to Fischer:</strong>', True, '8.4 Fischer to Haworth figure')
fig('597179', 'elong', 'fig-p597179-elongation.svg', 760, '\\(\\PageIndex{4}\\)',
    'One elongation cycle on the mRNA 5&prime;-AUG GGU GAA AAG-3&prime;: a tRNA enters the A site, a peptide bond forms, and the ribosome moves one codon (translocation), so the growing chain is back in the P site.',
    '<p>Many ribosomes can read one mRNA at t', True, '12.6 elongation cycle figure (P and A sites)')

bad = 0
for p, es in edits.items():
    t = page(p)
    for x in es:
        if t.count(x['old']) != x['count']: bad += 1; print('REPLAY FAIL', p, x['note'])
        t = t.replace(x['old'], x['new'])
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchF1_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages;', bad, 'replay failures')
