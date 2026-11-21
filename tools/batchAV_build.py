"""Batch AV (2026-11-20): five hands-on lab boxes from the new CHEM 3A games, placed in CHEM 3B sections that had no lab.
Same box format as batch AJ (green "Hands-on Lab" box, hideprint frame, "Not loading?" link, print-only QR line + short link).
These games have no compact ?view=lab mode; like the CHEM 3A book's Explore It boxes they are framed at 900 px, and they carry
the frame-scroll shim (scrolling inside the game never moves the textbook page).
Deep links checked in the browser 2026-11-20: acidbase ?mode=buffer (Buffer Lab + blood buffer + patient cases);
equilibrium ?mode=lab&sys=blood (CO2 + H2O <=> H+ + HCO3-, stresses: hyperventilate, COPD, lactic acid, kidneys, bicarbonate IV,
diarrhea) and &sys=hb (Hb + O2 <=> HbO2: altitude, oxygen mask, anemia); lewisstructures ?course=3B (builder, 3B molecules) and
&mode=geometry (VSEPR with 3-D models), &mode=polarity.
Also writes t/<code>.html (short-link redirect) and qr/<code>.svg (segno: full https URL, error M, scale 4, border 2, viewBox only; reproduces batch AK's files byte for byte).
Run: python3 tools/batchAV_build.py  (needs segno; scratchpad venv has it)"""
import json, hashlib, os, sys

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


G = 'https://itsdrdan.github.io/'
LINKS = {}


def box(code, title, game, url, body):
    LINKS[code] = url
    u = url.replace('&', '&amp;')
    return ('<div class="box-note" style="border-left:6px solid #1f8a70;">\n'
            '<p class="boxtitle">Hands-on Lab: %s</p>\n%s\n'
            '<p class="hideprint"><iframe src="%s" width="100%%" height="900" style="border:0;border-radius:12px;background:#f5f6fb;" '
            'title="Hands-on Lab: %s" loading="lazy"></iframe></p>\n'
            '<div class="hideprint dd-noprint">\n<p style="font-size:0.9em;">Not loading? <a style="text-decoration:underline" '
            'target="_blank" rel="noopener" href="%s">Open this lab in a new tab</a>.</p>\n</div>\n'
            '<div class="showprint" style="font-size:0.9em;overflow:hidden;"><img src="https://itsdrdan.github.io/textbook/qr/%s.svg" '
            'alt="QR code for itsdrdan.github.io/textbook/t/%s" width="96" height="96" style="float:right;width:96px;height:96px;margin:0 0 6px 12px;" />'
            '<p>This lab runs online in <em>%s</em>. Scan the QR code or go to <strong>itsdrdan.github.io/textbook/t/%s</strong>.</p></div>\n'
            '</div>\n') % (title, body, u, title, u, code, code, game, code)


TRY = '<div class="box-note" style="border-left:6px solid #86509b;">\n<p class="boxtitle">Try It: '

# 1. 15.5 Ketone Bodies and Ketoacidosis: Proton Swap! Buffer Lab
B1 = box('597213lab', 'Buffers, blood gases and DKA', 'Proton Swap!', G + 'acidbase/?mode=buffer',
         '<p>Add acid to plain water and to a blood-like buffer of H<sub>2</sub>CO<sub>3</sub> and HCO<sub>3</sub><sup>&minus;</sup>, '
         'and watch which pH holds. Then work patient cases: a patient in DKA breathing deep and fast, arterial blood gases, lactic '
         'acid after a sprint. They are the chemistry behind Kussmaul breathing: breathing out CO<sub>2</sub> removes acid. '
         '<em>Proton Swap!</em> is a CHEM 3A game; the Buffer Lab is the part this section needs.</p>')
e('597213', '</div>\n\n' + TRY + 'Ketone Bodies</p>', '</div>\n\n' + B1 + TRY + 'Ketone Bodies</p>', '15.5: Hands-on Lab box (Proton Swap! Buffer Lab)')

# 2. 6.10 Acid-base reactions: Equilibrium Park! blood buffer
B2 = box('597118lab', 'Lactic acid and the blood buffer', 'Equilibrium Park!', G + 'equilibrium/?mode=lab&sys=blood',
         '<p>The blood buffer, CO<sub>2</sub> + H<sub>2</sub>O &#8652; H<sup>+</sup> + HCO<sub>3</sub><sup>&minus;</sup>, runs here as '
         'moving particles. Add lactic acid (more H<sup>+</sup>), hold your breath, breathe fast, or give bicarbonate, and watch the '
         'equilibrium shift and the pH tube change color: the Clinical Connection above, one stress at a time. '
         '<em>Equilibrium Park!</em> is a CHEM 3A game; this lab is the part that fits this section.</p>')
e('597118', '</div>\n\n' + TRY + 'Acidity and carboxylate salts</p>', '</div>\n\n' + B2 + TRY + 'Acidity and carboxylate salts</p>',
  '6.10: Hands-on Lab box (Equilibrium Park! blood buffer)')

# 3. 10.9 Quaternary structure: Equilibrium Park! hemoglobin
B3 = box('597162lab', 'Hemoglobin and oxygen', 'Equilibrium Park!', G + 'equilibrium/?mode=lab&sys=hb',
         '<p>Hb + O<sub>2</sub> &#8652; HbO<sub>2</sub> runs here as moving particles. Climb to high altitude, put on an oxygen mask, '
         'or lower the hemoglobin (anemia), and watch how much oxygen the blood carries. The lab counts each oxygen-binding site '
         'as one Hb; real hemoglobin has four subunits, and each one binds one O<sub>2</sub> at its heme. '
         '<em>Equilibrium Park!</em> is a CHEM 3A game; this lab is the part that fits this section.</p>')
A3 = ('anything that denatures a protein (Section 10.10) also pulls its subunits apart.</p>\n'
      '<div class="valley-connection" role="note" aria-label="Valley Connection"')
e('597162', A3, A3.replace('</p>\n<div class="valley', '</p>\n' + B3 + '<div class="valley'), '10.9: Hands-on Lab box (Equilibrium Park! hemoglobin)')
PRINT = ('<style type="text/css">/*<![CDATA[*/@media print { .mt-content-container div.hideprint.dd-noprint, div.hideprint.dd-noprint '
         '{ display: none !important; visibility: hidden !important; } }/*]]>*/</style>')
t = pages['597162'][1]
if 'div.hideprint.dd-noprint {' not in t and 'div.hideprint.dd-noprint, div' not in t:
    tail = t[-200:]
    assert t.count(tail) == 1
    e('597162', tail, tail + '\n' + PRINT, '10.9: print rule that hides the "Not loading?" line (same as batch AL pages)')

# 4. 1.5 Characteristics of Molecules: Lewis Structure Studio VSEPR (+ link to Polarity Lab)
POL = G + 'lewisstructures/?course=3B&mode=polarity'
B4 = box('597058lab', '3-D shapes and polarity', 'Lewis Structure Studio', G + 'lewisstructures/?course=3B&mode=geometry',
         '<p>The organic molecules here come from this course. Use the completed Lewis structure to name the shape around each atom, '
         'then turn the 3-D model to check it. When the shapes are easy, switch to the '
         '<a style="text-decoration:underline" target="_blank" rel="noopener" href="%s">Polarity Lab</a>, which asks this '
         'section&rsquo;s two questions in order: are the bonds polar, and do they cancel?</p>' % POL.replace('&', '&amp;'))
e('597058', '</div>\n' + TRY + 'Shapes and polarity</p>', '</div>\n' + B4 + TRY + 'Shapes and polarity</p>', '1.5: Hands-on Lab box (Lewis Structure Studio, VSEPR)')

# 5. 1.3 Drawing Lewis Structures: Lewis Structure Builder
B5 = box('597056lab', 'Lewis Structure Builder', 'Lewis Structure Studio', G + 'lewisstructures/?course=3B',
         '<p>Build the Lewis structure of an organic molecule from this course, one bond and one lone pair at a time, then check it. '
         'Use the same count-first routine as the worked examples: valence electrons, skeleton, bonds, then lone pairs.</p>')
e('597056', '</div>\n' + TRY + 'Lewis structures</p>', '</div>\n' + B5 + TRY + 'Lewis structures</p>', '1.3: Hands-on Lab box (Lewis Structure Builder)')

# short links and QR codes
try:
    import segno
except ImportError:
    sys.exit('needs segno (use the scratchpad venv)')
RED = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" '
       'content="width=device-width,initial-scale=1"><title>Open the lab</title><meta http-equiv="refresh" content="0; url=%s">'
       '<script>location.replace("%s")</script></head><body style="font-family:system-ui,sans-serif;padding:24px"><p><a href="%s">'
       'Open the lab</a></p></body></html>')
for code, url in LINKS.items():
    ua = url.replace('&', '&amp;')
    open('t/%s.html' % code, 'w').write(RED % (ua, url, ua))
    segno.make('https://itsdrdan.github.io/textbook/t/' + code, micro=False, error='m').save(
        'qr/%s.svg' % code, kind='svg', scale=4, border=2, dark='#1f2a44', xmldecl=False, svgclass='segno', lineclass='qrline', omitsize=True)

h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'batch': 'AV', 'date': '2026-11-20', 'uploads': [], 'edits': E}, open('tools/batchAV_2026-11-20.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAV_sha_2026-11-20.json', 'w'))
print(sum(len(v) for v in E.values()), 'edits on', len(E), 'pages;', len(LINKS), 'short links')
