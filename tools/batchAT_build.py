"""Batch AT (2026-11-19): final reviewer-readiness fixes from the accessibility and link verification.
1. 11.1 Figure 1: the GLmol 3-D viewer scripts (libretexts.org/awesomefiles/GLmol/...) return 404, so the page showed a caption
   with no figure. Replaced by the RCSB PDB image of entry 1CDO (CC0: "Molecular images from RCSB PDB Structure Summary pages are
   available under the same conditions" as PDB data, CC0 1.0; rcsb.org/pages/usage-policy, read 2026-11-19), with alt text and a
   link to the interactive 3-D view at RCSB. Citation from data.rcsb.org entry 1CDO: Ramaswamy, el Ahmad, Danielsson, Jornvall,
   Eklund, Protein Sci 5:663 (1996).
2. Side-scrolling tables (batch Z CSS) get tabindex="0" where they scroll at 320 px (WCAG 2.1.1 / axe scrollable-region-focusable),
   so keyboard users can scroll them. List from the live axe scan (tools/batchAT_tables.json).
3. 15.4 "Fat and obesity" box title h4 -> h3 (heading skipped a level after an h2).
4. 12.2 empty duplicate <ul id="gob-ch19_s02_s02_l04"></ul> removed (duplicate id).
5. rel="noopener" on 9 new-tab links (5 YouTube, 4 VCell); the VCell links also lose leftover Google search attributes.
uploads: PUT /@api/deki/pages/597166/files/=fig-p597166-adh-1cdo.jpg from figures/pages/batchAT; {{ADH}} -> new file id.
Output: tools/batchAT_2026-11-19.json, tools/batchAT_sha_2026-11-19.json (sha 'after' computed with ADH=FILEID placeholder), audit/preview/<id>.html"""
import json, hashlib, re, os

pages, E, order = {}, {}, []


def e(p, old, new, note, count=1):
    p = str(p)
    if p not in pages:
        pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
        order.append(p)
    t = pages[p][1]
    assert t.count(old) == count, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new)
    E.setdefault(p, []).append({'old': old, 'new': new, 'count': count, 'note': note})


uploads = [{'page': '597166', 'name': 'fig-p597166-adh-1cdo.jpg', 'path': 'figures/pages/batchAT/fig-p597166-adh-1cdo.jpg', 'key': 'ADH', 'old_fileid': None}]

U = lambda href, text: '<a style="text-decoration:underline" href="%s" target="_blank" rel="noopener">%s</a>' % (href, text)
OLD = ('<script type="text/javascript" src="https://libretexts.org/awesomefiles/GLmol/js/Three49custom.js"></script>'
       '<script type="text/javascript" src="https://libretexts.org/awesomefiles/GLmol/js/GLmol.js"></script>'
       '<script type="text/javascript" src="https://libretexts.org/awesomefiles/GLmol/js/GLWrapper.js" data-id="=1CDO"></script>\n\n\n\n'
       '<p class="mt-align-center"><em><strong>Figure \\(\\PageIndex{1}\\): </strong>Interactive 3-D model of the enzyme alcohol dehydrogenase '
       '(EC 1.1.1.1) with its coenzyme NAD and zinc ions bound. The model can be rotated in the online book; it does not appear in print. '
       '(Structure: Protein Data Bank entry 1CDO, shown with the GLmol viewer.)</em></p>')
NEW = ('<p class="mt-align-center"><img alt="Ribbon model of alcohol dehydrogenase from cod liver (PDB entry 1CDO): two identical protein '
       'chains, one green and one orange, each folded into coils (alpha helices) and flat arrows (beta sheets). Small stick models of the '
       'coenzyme NAD+ sit inside each chain, next to its zinc ions." class="internal" width="360" style="max-width:100%;height:auto;" '
       'src="/@api/deki/files/{{ADH}}/fig-p597166-adh-1cdo.jpg" fileid="{{ADH}}" /></p>\n'
       '<p class="mt-align-center"><em><strong>Figure \\(\\PageIndex{1}\\): </strong>Alcohol dehydrogenase (EC 1.1.1.1), the cod-liver enzyme '
       'in Protein Data Bank entry 1CDO: two identical protein chains (green and orange), each with its coenzyme NAD<sup>+</sup> and zinc '
       'ions bound. ' + U('https://www.rcsb.org/3d-view/1CDO', 'Rotate the 3-D model at the RCSB Protein Data Bank') + '. (Image: RCSB PDB, '
       'CC0, from PDB entry 1CDO; Ramaswamy et al., <em>Protein Science</em> 5, 663&ndash;671, 1996.)</em></p>')
e('597166', OLD, NEW, '11.1 Figure 1: broken GLmol viewer replaced by the RCSB 1CDO image, alt text and a 3-D link')

e('597209', '<h4 class="box-legend editable">Fat and obesity</h4>', '<h3 class="box-legend editable">Fat and obesity</h3>',
  '15.4: box title h4 -> h3 (no skipped heading level)')
e('597176', '</ol>\n\n<ul class="itemizedlist" id="gob-ch19_s02_s02_l04">\n</ul>\n', '</ol>\n', '12.2: empty duplicate list (duplicate id) removed')

for p, vid in [('597062', 'RNQKJ1hnHes'), ('597074', 'gSKpPWYVnTU'), ('597074', 'xbsGe976lZ4'), ('597141', 'ckrRl0L3sr4'), ('597141', 'fBVx-i_Ehmc')]:
    e(p, '<a href="https://www.youtube.com/watch?v=%s" target="_blank">' % vid,
      '<a href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">' % vid, 'rel=noopener on a YouTube link')
for p in ['597179', '597200', '597201']:
    t = pages.get(p, [open('pages/live/%s.html' % p, encoding='utf-8').read()])[-1]
    for m in sorted(set(re.findall(r'<a data-servicelink="[^"]*" data-url="https://www\.vcell\.science/" href="https://www\.vcell\.science/" rel="nofollow" target="_blank">', t))):
        e(p, m, '<a href="https://www.vcell.science/" target="_blank" rel="noopener">', 'VCell link: rel=noopener, Google search attributes removed')

# 2. keyboard-focusable scrolling tables (filled from the live scan)
TF = 'tools/batchAT_tables.json'
for p in sorted(json.load(open(TF))):   # pages where a table scrolls sideways at 320 px or axe flagged scrollable-region-focusable
    t = pages.get(p, [open('pages/live/%s.html' % p, encoding='utf-8').read()])[-1]
    for tag in sorted(set(re.findall(r'<table[^>]*class="mt-responsive-table[^"]*"[^>]*>', t))):
        if 'tabindex' in tag:
            continue
        e(p, tag, tag[:-1] + ' tabindex="0">', 'side-scrolling table can take keyboard focus (tabindex=0)', count=t.count(tag))
        t = pages[p][1]

# 6. Hint/Answer buttons (same screen-only rule as the CHEM 3A book, 2026-11-19 iPhone Safari check): LibreTexts shows <summary>
#    inline with no arrow, so "Answer" was a plain ~17 px word (below the WCAG 2.2 24 px target size, and not visibly tappable).
#    Screen only: 44 px outlined button, arrow hidden from screen readers ("/ ''"), focus ring; print rules unchanged.
#    Checked: no 3B glossary term occurs in the style text (the glossary script would break it).
SCREEN = ('<style type="text/css">@media screen { '
          '.mt-content-container details > summary { display:inline-flex; align-items:center; gap:0.45em; list-style:none; '
          'min-height:44px; box-sizing:border-box; padding:0 1em; margin:0.35em 0; border:0; box-shadow:inset 0 0 0 1.5px #2f6f9f; border-radius:8px; '
          'background:#fff; color:#1d4f7a; font-weight:600; font-size:1rem; line-height:1.2; cursor:pointer; } '
          '.mt-content-container details > summary::-webkit-details-marker { display:none; } '
          '.mt-content-container details > summary::before { content:"▸"; content:"▸" / ""; font-size:1.1em; } '
          '.mt-content-container details[open] > summary::before { content:"▾"; content:"▾" / ""; } '
          '.mt-content-container details[open] > summary { background:#e3eef8; } '
          '.mt-content-container details > summary:focus-visible { outline:3px auto #1d4f7a; box-shadow:inset 0 0 0 1.5px #2f6f9f, 0 0 0 3px #fff, 0 0 0 6px #1d4f7a; } }</style>\n')
for f in sorted(os.listdir('pages/live')):
    p = f[:-5]
    t = pages.get(p, [open('pages/live/' + f, encoding='utf-8').read()])[-1]
    if '<summary' in t and 'details > summary { display:inline-flex' not in t:
        first = t[:200]
        e(p, first, SCREEN + first, 'Hint/Answer shown as a 44 px button (screen only)')

# 7. 11.6 math speech: "\ " spaces inside math are read as "empty" by MathJax speech; use \; (same fix as the 3A book).
OLDM = r'\(A\ \xrightarrow{Enzyme\ 1}\ B\ \xrightarrow{Enzyme\ 2}\ C\ \xrightarrow{Enzyme\ 3}\ D\)'
e('597171', OLDM, OLDM.replace('\\ ', '\;'), 'math spacing \\ -> \; (screen-reader speech)')

# 8. 5.2 Figure 1: fixed 436 px image made the caption run 11 px past a 320 px screen (WCAG 1.4.10 reflow).
e('597103', 'style="width: 436px; height: 305px;" class="internal" src="/@api/deki/files/27166/14.5.jpg"',
  'style="width: 436px; max-width:100%; height:auto;" class="internal" src="/@api/deki/files/27166/14.5.jpg"', '5.2 Figure 1 scales to the screen')

# 9. Course Outline Alignment: the lab-manual table (added in batch AM) was the only table in the book without a caption.
e('597272', '<table class="mt-responsive-table" style="width:100%;" tabindex="0"><thead><tr><th>Lab manual (PDF)</th>',
  '<table class="mt-responsive-table" style="width:100%;" tabindex="0"><caption>Lab manual experiments and the book sections whose &ldquo;In the Lab&rdquo; boxes point to them</caption><thead><tr><th>Lab manual (PDF)</th>',
  'Course Outline Alignment: caption on the lab-manual table')

# 10. 12.3: the replication-fork figure sat inside the <ul> after the last <li> (invalid list; axe "list"). Close the list first.
e('597177', 'nucleotides.</li>\n<figure>', 'nucleotides.</li>\n</ul>\n<figure>', '12.3: list closed before the replication-fork figure')
e('597177', '</figure>\n</ul>\n<div class="box-note">\n<p class="boxtitle">Professor Tip', '</figure>\n<div class="box-note">\n<p class="boxtitle">Professor Tip', '12.3: (same) old list end removed')

# 11. Side-scrolling figure boxes (<div class="fig-scroll">, phone figure batches W/X) are also scrollable regions that the
#     keyboard could not reach (axe scrollable-region-focusable). Make each one a named, focusable region.
for f in sorted(os.listdir('pages/live')):
    p = f[:-5]
    t = pages.get(p, [open('pages/live/' + f, encoding='utf-8').read()])[-1]
    c = t.count('<div class="fig-scroll">')
    if c:
        e(p, '<div class="fig-scroll">', '<div class="fig-scroll" tabindex="0" role="region" aria-label="Wide figure: scroll sideways">',
          'side-scrolling figure box can take keyboard focus', count=c)

h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after_template': h(pages[p][1])} for p in order}
os.makedirs('audit/preview', exist_ok=True)
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'batch': 'AT', 'date': '2026-11-19', 'uploads': uploads, 'edits': E}, open('tools/batchAT_2026-11-19.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAT_sha_2026-11-19.json', 'w'))
print(sum(len(v) for v in E.values()), 'edits on', len(E), 'pages')
