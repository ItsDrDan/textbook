"""Batch E3 (review 2026-11-12): replace the remaining CC BY-SA images and the uncredited photos (author's decision).
Replacements: Wikimedia Commons files with licences read from the Commons API (public domain or CC0; none
ShareAlike), resized to about the old display size and stored in figures/pages/batchE/; the 10.7 triple-helix
panel is cropped from the book's own collagen diagram (Daniel Kwasniewski, CC BY 4.0).
  3.3   tomatoes            Healthy_Vegetables_(Unsplash).jpg        Ivan Timov, CC0
  4.7   phenol crystals     Air-oxidized_phenol.jpg                  Alit Variatos, CC0
  15.8  treadmill test      Finding_the_max_130305-A-UK001-003.jpg   Cpl. William Smith, U.S. Army, public domain
  15.4  polar bears         Polar_Bears_(6383864837).jpg             U.S. Fish and Wildlife Service, public domain
  15.4  orcas               Killerwhales_jumping.jpg                 Robert Pittman, NOAA, public domain
  15.4  camels              Dromadery_and_camel.jpg                  Bgag, CC0
  15.4  snow geese          Snow_geese_taking_flight_(49565159567)   N. Horne, USFWS, public domain
  9.3   venom collection    Venin_Geneve_24102014.jpg                Vassil, CC0
  10.7  triple helix panel  fig-p597160-triple-helix.svg             Daniel Kwasniewski, CC BY 4.0
The About page bullet that claimed every ShareAlike figure was replaced is now true; it is rewritten without
the stray "also:" and the run-on clause.
Output: tools/batchE3_images_2026-11-12.json {uploads:[...], edits:{page:[...]}} (same format as batch B2).
"""
import json, re

L = 'pages/live/'
A = 'figures/pages/batchE/'
uploads, edits = [], {}
C = lambda f: f'<a href="https://commons.wikimedia.org/wiki/File:{f}" target="_blank" rel="noopener">Wikimedia Commons</a>'
CC0 = '<a href="https://creativecommons.org/publicdomain/zero/1.0/" target="_blank" rel="noopener">CC0</a>'


def page(p): return open(L + p + '.html', encoding='utf-8').read()


def e(p, old, new, note):
    assert page(p).count(old) == 1, (p, note, page(p).count(old))
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})


def tag_with(p, needle):
    t = page(p); i = t.find(needle); assert i >= 0, (p, needle)
    return t[t.rfind('<img', 0, i):t.find('>', i) + 1]


def swap(p, needle, fname, key, alt, width=None, note=''):
    old = tag_with(p, needle)
    new = re.sub(r'src="[^"]*"', f'src="/@api/deki/files/{{{{{key}}}}}/{fname}"', old)
    new = re.sub(r'fileid="\d+"', f'fileid="{{{{{key}}}}}"', new)
    new = re.sub(r'alt="[^"]*"', 'alt="' + alt + '"', new)
    if width:
        new = re.sub(r'\s(width|height)="[^"]*"', '', new)
        new = new.replace('<img', f'<img width="{width}"', 1)
        if 'style="' not in new: new = new.replace('<img', '<img style="max-width:100%;height:auto;"', 1)
    uploads.append({'page': p, 'name': fname, 'path': A + fname, 'key': key, 'old_fileid': None})
    e(p, old, new, note or fname)
    return new


# 3.3 tomatoes
old = tag_with('597080', 'Tomato_je1.jpg')
new = swap('597080', 'Tomato_je1.jpg', 'fig-p597080-tomatoes.jpg', 'tom', 'Close-up photograph of ripe red tomatoes.', 300, '3.3 tomatoes (CC0)')
edits['597080'][-1] = {'old': old + '</p>\n<p class="mt-align-center"><small>Photo: Softeis, <a href="https://commons.wikimedia.org/wiki/File:Tomato_je.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC BY-SA 3.0</a>.</small></p>',
                       'new': new + '</p>\n<p class="mt-align-center"><small>Photo: Ivan Timov, ' + C('Healthy_Vegetables_(Unsplash).jpg') + ', ' + CC0 + '.</small></p>',
                       'count': 1, 'note': '3.3 tomatoes (CC0) and credit'}
assert page('597080').count(edits['597080'][-1]['old']) == 1

# 4.7 phenol crystals
swap('597096', 'Phenol_2_grams.jpg', 'fig-p597096-phenol-oxidized.jpg', 'phen',
     'Photograph of a small heap of phenol crystals on a glass dish, discolored to a dark pinkish brown.', 219, '4.7 phenol crystals (CC0)')
e('597096', '(Left) Ball-and-stick model of phenol. (Right) About two grams of phenol crystals in a glass tube. (Model: Benjah-bmm27, public domain; photo: W. Oelen, <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC BY-SA 3.0</a>; both via Wikimedia Commons.)',
  '(Left) Ball-and-stick model of phenol. (Right) Phenol crystals that have darkened during long storage, because phenol is slowly oxidized by oxygen in the air. (Model: Benjah-bmm27, public domain; photo: Alit Variatos, ' + CC0 + '; both via Wikimedia Commons.)',
  '4.7 Fig 1 caption')

# 15.8 treadmill test
swap('597208', 'Ergospirometry_laboratory.jpg', 'fig-p597208-vo2max-test.jpg', 'vo2',
     'Photograph of a man running on a treadmill while breathing through a mask connected to an oxygen analyzer; two staff members watch the test.', 300, '15.8 VO2 max test photo (public domain)')
e('597208', 'Ergospirometry laboratory for the measurement of metabolic changes during a graded exercise test on a treadmill. (Photo: Cosmed, <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC BY-SA 3.0</a>, via Wikimedia Commons.)',
  'A VO<sub>2</sub> max test: during graded exercise on a treadmill, a mask and analyzer measure how much oxygen the body uses. (Photo: Cpl. William Smith, U.S. Army, public domain, via ' + C('Finding_the_max_130305-A-UK001-003.jpg') + '.)',
  '15.8 caption')

# 15.4 four animals
swap('597209', 'two polar bears', 'fig-p597209-polar-bears.jpg', 'bear', 'Photograph of two polar bears walking across snow.', None, '15.4 polar bears (public domain)')
swap('597209', 'an orca', 'fig-p597209-orcas.jpg', 'orca', 'Photograph of two orcas (killer whales) leaping out of the sea.', None, '15.4 orcas (public domain)')
swap('597209', 'a camel walking', 'fig-p597209-camels.jpg', 'caml', 'Photograph of two camels standing in a desert.', None, '15.4 camels (CC0)')
swap('597209', 'large flock of migrating geese', 'fig-p597209-snow-geese.jpg', 'geese', 'Photograph of a large flock of snow geese taking flight.', None, '15.4 snow geese (public domain)')
e('597209', 'Migratory birds also store fat and use it as an energy source during migration. </p>',
  'Migratory birds also store fat and use it as an energy source during migration. </p>\n<p style="clear:both"><small>Photos: polar bears, U.S. Fish and Wildlife Service; orcas, Robert Pittman, NOAA; snow geese, N. Horne, U.S. Fish and Wildlife Service (all public domain); camels, Bgag, ' + CC0 + '. All via Wikimedia Commons.</small></p>',
  '15.4 photo credits')

# 9.3 venom
swap('597146', 'snake wrangler', 'fig-p597146-venom.jpg', 'venom',
     "Photograph of venom being collected from a snake: a handler holds the snake's head so that its fangs pierce a film stretched over a glass, and venom drips inside.", None, '9.3 venom collection (CC0)')
e('597146', 'The structure of the lysophospholipid example is shown in the figure on the left.</p>',
  'The structure of the lysophospholipid example is shown in the figure on the left.</p>\n<p style="clear:both"><small>Photo: Vassil, ' + C('Venin_Gen%C3%A8ve_24102014.jpg') + ', ' + CC0 + '.</small></p>',
  '9.3 photo credit')

# 10.7 triple-helix panel
old = tag_with('597160', 'files/432358/')
new = ('<img alt="Three protein chains (red, blue and green) wound around one another, labeled \'Triple helix\'." class="internal" width="118" style="max-width:100%;height:auto;" '
       'src="/@api/deki/files/{{thx}}/fig-p597160-triple-helix.svg" fileid="{{thx}}" />')
uploads.append({'page': '597160', 'name': 'fig-p597160-triple-helix.svg', 'path': A + 'fig-p597160-triple-helix.svg', 'key': 'thx', 'old_fileid': None})
e('597160', old, new, '10.7 Fig 1 triple-helix panel (own drawing)')
e('597160', 'Basic secondary structures of proteins illustrated. (The creator and license of each panel are printed on the panel.)</figcaption>',
  'Basic secondary structures of proteins illustrated. (The creator and license of the first three panels are printed on each panel; triple helix: Daniel Kwasniewski, CC BY 4.0.)</figcaption>',
  '10.7 Fig 1 caption')

# About bullet
t = page('597270'); i = t.find('<li>also: some source figures'); j = t.find('</li>', i) + 5
e('597270', t[i:j],
  '<li>replaces some source figures with original structure and pathway figures drawn for this book (glycolysis, the citric acid cycle, &beta;-oxidation, the urea cycle, the electron transport chain, ATP synthase and key reactions in Chapters 13&ndash;15), and replaces every source image that carried a ShareAlike (CC BY-SA) license with an original figure or a public-domain or CC0 image (for example in Sections 3.3, 4.7, 5.3, 5.4, 9.4, 10.7, 12.4 and 15.8); source headings were also renumbered so heading levels run in order for screen readers;</li>',
  'About: bullet rewritten (no stray "also:", no run-on; ShareAlike statement now true)')

for p, es in edits.items():
    t = page(p)
    for x in es:
        assert t.count(x['old']) == 1, (p, x['note']); t = t.replace(x['old'], x['new'])
json.dump({'uploads': uploads, 'edits': edits}, open('tools/batchE3_images_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print(len(uploads), 'uploads;', sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
