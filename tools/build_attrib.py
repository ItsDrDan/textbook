#!/usr/bin/env python3
"""Generate the back-matter 'Source Attributions by Section' page from tools/transclusions.json → sections/back_sources.html"""
import json, re, urllib.parse, html, os
HERE = os.path.dirname(os.path.abspath(__file__))
b = json.load(open(os.path.join(HERE, 'transclusions.json')))
titles = dict(l.split(' ', 1) for l in open(os.path.join(HERE, 'section_ids.txt')).read().splitlines() if l.strip())
BOOKS = {
 'The_Basics_of_General_Organic_and_Biological_Chemistry_(Ball_et_al.)': ('<em>The Basics of General, Organic, and Biological Chemistry</em>', 'David W. Ball, John W. Hill and Rhonda J. Scott (Saylor Foundation edition, on LibreTexts)', 'CC BY-NC-SA 3.0', 'https://creativecommons.org/licenses/by-nc-sa/3.0/'),
 'Introduction_to_Organic_and_Biochemistry_(Malik)': ('<em>Introduction to Organic and Biochemistry</em>', 'Muhammad Arif Malik (LibreTexts)', 'Public domain (CC0)', 'https://creativecommons.org/publicdomain/zero/1.0/'),
 'Fundamentals_of_General_Organic_and_Biological_Chemistry_(LibreTexts)': ('<em>Fundamentals of General, Organic, and Biological Chemistry</em>', 'LibreTexts', 'CC BY-NC-SA 3.0', 'https://creativecommons.org/licenses/by-nc-sa/3.0/'),
}
NEW = {597099:'4.10: Acidity of Alcohols and Phenols',597131:'7.11: Neurotransmitters',597172:'11.7: Enzyme Regulation - Covalent Modification and Genetic Control',597183:'12.9: Structure and Function of RNA',597194:'13.7: Entry of Other Sugars into Glycolysis',597195:'13.8: Regulation of Glucose Metabolism and Metabolism During Stress',597196:'13.9: Glycogen Metabolism- Glycogenesis and Glycogenolysis',597197:'13.10: Gluconeogenesis- Glucose Synthesis from Noncarbohydrates',597204:'14.5: Energy Output in Complete Glucose Catabolism',597212:'15.6: Storage and Mobilization of Triacylglycerols'}
rows = []
for pid, body in b.items():
    m = re.search(r'data-page="([^"]+)"', body); path = urllib.parse.unquote(m.group(1))
    book = path.split('/')[2]; src_title = path.split('/')[-1].replace('_', ' ')
    name, author, lic, licurl = BOOKS[book]
    url = 'https://chem.libretexts.org/' + m.group(1)
    rows.append((titles[pid], f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{html.escape(src_title)}</a>', name, author, f'<a href="{licurl}" target="_blank" rel="noopener">{lic}</a>'))
def key(r):
    a, b_ = r[0].split(':')[0].split('.'); return (int(a), int(b_))
rows.sort(key=key)
out = ['<p>Every section page in this book that carries text from another open textbook is listed here with its title, author, source link and license (the TASL elements). Each such page also shows the source\'s own attribution notice at its foot. Pages not listed here (the Chapter Guides, Practice Problems, Practice Games, About This Book, and the ten sections below) were written for this book and are licensed CC BY-NC-SA 4.0 by Dr. Dan (Daniel Kwasniewski), Fresno City College.</p>',
 '<h2>Sections adapted from other open textbooks</h2>',
 '<p>The text of every section listed here is reproduced unchanged from its source. Sections that contain figures were copied into this book so that every figure could be given a rewritten, accessible text description (alt text); each of those pages carries an &ldquo;Adapted from&rdquo; note at the end of the source text. Sections with no figures are still shown by transclusion (a live copy of the source page). Every page was then extended with a &ldquo;Lecture Connection&rdquo; block written for this course (see the adaptation statement in About This Book).</p>',
 '<table class="mt-responsive-table"><caption>Source of each adapted section</caption><thead><tr><th scope="col">Section in this book</th><th scope="col">Source section</th><th scope="col">Source book</th><th scope="col">Author(s)</th><th scope="col">License</th></tr></thead><tbody>']
for r in rows:
    out.append('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (html.escape(r[0]), r[1], r[2], html.escape(r[3]), r[4]))
out.append('</tbody></table>')
out.append('<h2>Sections written for this book</h2><p>These sections replaced empty placeholder pages in the source book and are entirely original: ' + '; '.join(html.escape(t) for t in NEW.values()) + '. License: <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener">CC BY-NC-SA 4.0</a>, Dr. Dan (Daniel Kwasniewski), Fresno City College.</p>')
op = json.load(open(os.path.join(HERE, '..', 'figures', 'openers', 'credits.json')))
out.append('<h2>Chapter-opener photographs</h2><p>Each chapter page opens with a photograph from Wikimedia Commons. All are public-domain, CC0 or CC BY works (no ShareAlike-only images were used, so they combine freely with this book\'s CC BY-NC-SA 4.0 license). Each was cropped to a 16:9 banner; no other changes were made.</p>')
out.append('<table class="mt-responsive-table"><caption>Chapter-opener image credits (TASL)</caption><thead><tr><th scope="col">Chapter</th><th scope="col">Title</th><th scope="col">Author</th><th scope="col">Source</th><th scope="col">License</th></tr></thead><tbody>')
for c in op:
    out.append('<tr><td>%d</td><td>%s</td><td>%s</td><td><a href="%s" target="_blank" rel="noopener">Wikimedia Commons</a></td><td><a href="%s" target="_blank" rel="noopener">%s</a></td></tr>' % (c['ch'], html.escape(c['title']), html.escape(c['author']), html.escape(c['source']), c['licurl'], html.escape(c['license'])))
out.append('</tbody></table>')
out.append('<h2>Figures and media</h2><ul><li><strong>Lecture-slide figures</strong> (file names SlideNN): drawn by the author for CHEM 3B; CC BY-NC-SA 4.0.</li><li><strong>Structure and reaction drawings</strong> captioned &ldquo;drawn with the Bond Voyage! engine&rdquo;: generated by the author\'s own software; CC BY-NC-SA 4.0.</li><li><strong>Pathway and concept diagrams</strong> captioned &ldquo;Diagram: Dr. Dan&rdquo;: original; CC BY-NC-SA 4.0.</li><li><strong>Figures inside adapted sections</strong> belong to the source book and carry its license (see the table above); only their alt-text descriptions were rewritten for this book.</li><li><strong>Videos</strong> are the author\'s own CHEM 3B lessons on YouTube (@itsdrdan), embedded by link; they are not part of the licensed text.</li><li><strong>Try It practice widgets and the study games</strong> are the author\'s own software, served from itsdrdan.github.io and embedded by link; they are tools provided free for educational use and are not part of the licensed text. The question bank used by the widgets was written by the author.</li></ul>')
out.append('<h2>Attribution statement for reuse</h2><p>If you reuse this book, please attribute it as: &ldquo;<em>Introductory Organic and Biological Chemistry for FCC</em> by Dr. Dan (Daniel Kwasniewski), Fresno City College, licensed CC BY-NC-SA 4.0; adapted from <em>The Basics of General, Organic, and Biological Chemistry</em> by David W. Ball, John W. Hill and Rhonda J. Scott (CC BY-NC-SA 3.0), <em>Introduction to Organic and Biochemistry</em> by Muhammad Arif Malik (public domain) and <em>Fundamentals of General, Organic, and Biological Chemistry</em> (LibreTexts, CC BY-NC-SA 3.0).&rdquo;</p>')
out.append('<div class="box-note"><p class="boxtitle">Attribution</p><p>Compiled by Dr. Dan (Daniel Kwasniewski), Fresno City College, for CHEM 3B, with AI assistance; reviewed by the author. Licensed <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener">CC BY-NC-SA 4.0</a>.</p></div>')
open(os.path.join(HERE, '..', 'sections', 'back_sources.html'), 'w').write('\n'.join(out) + '\n')
print(len(rows), 'rows')
