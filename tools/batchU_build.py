"""Batch U (2026-11-13): the three editorial calls left from the prose pass, decided by the instructor ("fix these").
  14.4  cyanide is told in full once (Molecule in the Clinic); the Valley box and the Nursing box now point to it
  15.4  the source "Unsaturated fatty acids" box is removed (the Lecture Connection section covers it); its one extra
        fact (7n - 6 is still a close estimate) moves into the Lecture Connection
  15.4  two numbering schemes named apart: Stages I-III of catabolism (source text) vs stages 1-3 of fatty acid breakdown
Output: tools/batchU_2026-11-13.json, tools/batchU_sha_2026-11-13.json, audit/preview/<id>.html"""
import json, hashlib, os, re
L = 'pages/live/'
pages, edits, orig = {}, {}, {}
def page(p):
    if p not in pages: pages[p] = open(L + p + '.html', encoding='utf-8').read(); orig[p] = pages[p]
    return pages[p]
def e(p, old, new, note, n=1):
    t = page(p); assert t.count(old) == n, (p, note, t.count(old)); assert old != new
    pages[p] = t.replace(old, new); edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': note})

# ---- 14.4 cyanide ----
e('597203', 'Cyanide blocks the same enzyme, cytochrome c oxidase, and a high blood lactate',
  'Cyanide blocks cytochrome c oxidase too (the Molecule in the Clinic box below explains how), and a high blood lactate',
  '14.4 Valley box: cyanide mechanism left to the Molecule in the Clinic box')
t = page('597203')
a = t.index('A patient pulled from a house fire can have both carbon monoxide and cyanide'); b = t.index('because more oxygen alone cannot unblock the enzyme.</p>', a) + len('because more oxygen alone cannot unblock the enzyme.')
e('597203', t[a:b],
  'A patient pulled from a house fire can have both carbon monoxide and cyanide in the blood. CO occupies hemoglobin, so O<sub>2</sub> is not delivered; cyanide blocks cytochrome c oxidase, so the O<sub>2</sub> that does arrive cannot be used (Molecule in the Clinic, above). Either way the tissues switch to anaerobic glycolysis and blood <em>lactate</em> rises, causing <em>metabolic acidosis</em>. High-flow oxygen helps displace CO from hemoglobin, but more oxygen alone cannot unblock the enzyme, which is why cyanide needs its own antidote.',
  '14.4 Nursing box: keeps the CO-versus-cyanide comparison; the binding and antidote details are told once, in the Molecule in the Clinic box')

# ---- 15.4 stage numbering ----
e('597209', 'i.e., the 1st stage of catabolism of fats,', 'which is Stage I of catabolism (digestion, Section 13.1),', '15.4: source text now names the three stages of catabolism as Stage I, II, III')
e('597209', 'The second stage of fatty acid catabolism starts with', 'Stage II starts with', '15.4: Stage II of catabolism')
e('597209', 'for the second stage of its catabolism. In the second stage, the', 'for the rest of Stage II. There, the', '15.4: Stage II of catabolism')
e('597209', 'which is the third stage of the catabolism,', 'which is Stage III of catabolism,', '15.4: Stage III of catabolism')
e('597209', '<p>This is stage 3 of fatty acid breakdown, the <em>fatty acid spiral</em>.',
  '<p>This is stage 3 of fatty acid breakdown (after activation and transport, Section 15.3), the <em>fatty acid spiral</em>. All three of these belong to Stage II of catabolism, the stage that turns a fuel into acetyl CoA.',
  '15.4 Lecture Connection: "stage 3 of fatty acid breakdown" tied to Stage II of catabolism, so the two numberings do not clash')

# ---- 15.4 unsaturated fatty acids: one telling ----
t = page('597209')
m = re.search(r'<section class="box-note">\n<span id="Unsaturated_fatty_acids"></span><div class="mt-section"><h3 class="box-legend editable">Unsaturated fatty acids</h3>\n\n<p>Unsaturated fatty acids have .*?estimate of \\\(\\ce\{ATP\}\\\) yield\.</p>\n</div></section>\n\n', t, flags=re.S)
assert m and m.group(0).count('<section') == 1 and m.group(0).count('</section>') == 1 and m.group(0).count('<div') == 1 and m.group(0).count('</div>') == 1
e('597209', m.group(0), '', '15.4: source box "Unsaturated fatty acids" removed; the Lecture Connection section of the same name covers it in course terms')
e('597209', 'The number of acetyl CoA and the number of repetitions do not change.</p>',
  'The number of acetyl CoA and the number of repetitions do not change. Because the difference is small, 7<em>n</em> &minus; 6 still gives a close estimate for an unsaturated fatty acid.</p>',
  '15.4 Lecture Connection: keeps the one fact that only the removed box stated')

# ---- figures: cache-bust for the files changed after batch T (all 15 concept maps regenerated at edge label 15.5;
#      urea steps 1 and 4 and the glycerol step: molecule-name labels the first pass missed) ----
import glob
for f in sorted(glob.glob(L + '*.html')):
    p = os.path.basename(f)[:-5]; t = open(f, encoding='utf-8').read()
    for m in sorted(set(re.findall(r'"(https://itsdrdan\.github\.io/textbook/figures/(?:conceptmaps/ch\d\d|pathways/urea/step[14]|pathways/reactions/glycerol-glycerol-3-phosphate)\.svg(?:\?v=\w+)?)"', t))):
        new = m.split('?')[0] + '?v=20261113u'
        if new != m: e(p, '"' + m + '"', '"' + new + '"', 'figure label sizes: cache-bust for ' + m.split('/')[-1].split('?')[0], n=page(p).count('"' + m + '"'))

sha = {p: {'before': hashlib.sha256(orig[p].encode()).hexdigest(), 'after': hashlib.sha256(pages[p].encode()).hexdigest()} for p in edits}
json.dump(sha, open('tools/batchU_sha_2026-11-13.json', 'w'), indent=0)
json.dump({'uploads': [], 'edits': edits}, open('tools/batchU_2026-11-13.json', 'w'), ensure_ascii=False, indent=1)
os.makedirs('audit/preview', exist_ok=True)
for f in os.listdir('audit/preview'): os.remove('audit/preview/' + f)
for p in edits: open(f'audit/preview/{p}.html', 'w', encoding='utf-8').write(pages[p])
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
