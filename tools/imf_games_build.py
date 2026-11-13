"""IMF batch (DRAFT): add Sticky Molecules (https://itsdrdan.github.io/IMF/?course=3B) to the Practice Games
pages of the chapters that teach intermolecular forces. Nothing is published by this script.

Pages (all Practice Games pages; none is on the batch L list):
  1.11 (597232)  1.8 the forces, H bonding, boiling points, like dissolves like  + H-Bond Lab
  4.13 (597234)  4.3, 4.8 alcohol and ether boiling points and solubility          + Mixing Beaker
  7.14 (597237)  7.2, 7.5 amines (1°/2° vs 3°) and amides
  8.10 (597238)  8.5, 8.7 sugars dissolve; cellulose fibers vs starch
  9.9  (597239)  9.1 fatty-acid melting points; 9.2, 9.5 soaps, bilayer, tonicity  + Cell Lab
  10.13 (597240) 10.7, 10.8, 10.10 side-chain interactions, folding, denaturation  + Protein Fold Lab
  12.12 (597242) 12.2 base-pair hydrogen bonds, strand separation
Each new section goes just before the page's Final Boss section, in the house pattern of
tools/build_pages.py build_games_page (h2, blurb, "For this chapter", iframe, open-in-new-tab link).
The page's existing footer already credits the games to ItsDrDan; the games are embedded by link and
are not part of the licensed text, so no licence line is added.
Output: tools/imf_games_2026-11-13.json {uploads, edits}
Run from the textbook repo root: python3 tools/imf_games_build.py
"""
import json, html

L = 'pages/live/'
BASE = 'https://itsdrdan.github.io/IMF/?course=3B'
NAME = 'Sticky Molecules'
BLURB = ('Intermolecular forces in organic and biological molecules: name the forces, win boiling point battles, '
         'predict what mixes, and run predict-first labs on hydrogen bonds, cells in salt water and protein folding.')
LABS = {'lab': 'H-Bond Lab', 'mix': 'Mixing Beaker', 'cell': 'Cell Lab', 'fold': 'Protein Fold Lab'}

PLAN = {
    '597232': ('1.11', 'Spot the Forces first (who can hydrogen bond, and the forces in each organic family), then Boiling Point Battles and Liquids &amp; Mixing. Every pair is the reasoning of Section 1.8: same size, so the stronger force wins; same force, so the bigger molecule wins.',
               ('lab', 'Watch hydrogen bonds form and break in water, ammonia, methanol and methane as you change the temperature.')),
    '597234': ('4.13', 'Boiling Point Battles &rarr; &ldquo;Organic boiling points&rdquo; and Liquids &amp; Mixing &rarr; &ldquo;Like dissolves like&rdquo;: why an alcohol boils higher than an alkane or ether of similar size, and why water solubility drops after about four carbons (Sections 4.3 and 4.8).',
               ('mix', 'Predict, then drop methanol, hexane or salt into water or hexane and see what mixes.')),
    '597237': ('7.14', 'Spot the Forces &rarr; &ldquo;Forces in organic families&rdquo; and Boiling Point Battles &rarr; &ldquo;Organic boiling points&rdquo;: 1&deg; and 2&deg; amines hydrogen bond, 3&deg; amines cannot, and amides boil highest of all (Sections 7.2 and 7.5).', None),
    '597238': ('8.10', 'Biomolecules &rarr; &ldquo;Sugars, starch and cellulose&rdquo;: why sugars dissolve so well and why straight cellulose chains hydrogen bond into strong, insoluble fibers (Sections 8.5 and 8.7).', None),
    '597239': ('9.9', 'Boiling Point Battles &rarr; &ldquo;Fatty acids: melting points&rdquo; (Section 9.1), Biomolecules &rarr; the membrane and soap questions (Sections 9.2 and 9.5), and Cells &amp; Osmosis for hypotonic, isotonic and hypertonic solutions (Section 9.5).',
               ('cell', 'Put a red blood cell in pure water, normal saline or 3% NaCl and count the water going in and out.')),
    '597240': ('10.13', 'Biomolecules &rarr; &ldquo;Amino acid side chains&rdquo; and &ldquo;Protein folding&rdquo;: match each pair of side chains to its interaction (hydrophobic, hydrogen bond, salt bridge, disulfide) and decide what heat or a pH change breaks (Sections 10.7, 10.8 and 10.10).',
               ('fold', 'Heat a short protein chain and watch the attractions let go while the peptide and disulfide bonds stay.')),
    '597242': ('12.12', 'Biomolecules &rarr; &ldquo;DNA base pairs&rdquo;: count the hydrogen bonds (A&ndash;T two, G&ndash;C three) and explain why heating separates the strands without breaking them (Section 12.2).', None),
}

A = 'style="text-decoration:underline" '   # live pages carry this on every link


def section(tip, lab):
    url = html.escape(BASE)
    s = (f'<div class="mt-section"><h2 class="editable">{NAME}</h2>\n<p>{html.escape(BLURB)}</p>\n'
         f'<p><strong>For this chapter:</strong> {tip}</p>\n'
         f'<p><iframe src="{url}" width="100%" height="900" style="border:0;border-radius:12px;" title="{NAME}" loading="lazy" allowfullscreen="allowfullscreen"></iframe></p>\n'
         f'<p style="font-size:0.9em;"><a {A}href="{url}" target="_blank" rel="noopener">Open {NAME} in a new tab</a></p>\n')
    if lab:
        mode, what = lab; lu = html.escape(f'{BASE}&mode={mode}')
        s += f'<p style="font-size:0.9em;"><strong>Lab:</strong> <a {A}href="{lu}" target="_blank" rel="noopener">{LABS[mode]}</a>. {what}</p>\n'
    return s + '</div>'


edits, pages = {}, {}
for pid, (num, tip, lab) in PLAN.items():
    t = open(L + pid + '.html', encoding='utf-8').read()
    assert 'itsdrdan.github.io/IMF' not in t, pid
    i = t.find('<h2 class="editable">Final Boss</h2>'); assert i > 0, pid
    j = t.rfind('<div class="mt-section" id="section_', 0, i); old = t[j:i + len('<h2 class="editable">Final Boss</h2>')]
    assert t.count(old) == 1, pid
    new = section(tip, lab) + old
    edits[pid] = [{'old': old, 'new': new, 'count': 1, 'note': f'{num} Practice Games: add Sticky Molecules (IMF game, ?course=3B) before Final Boss'}]
    pages[pid] = t.replace(old, new)

json.dump({'uploads': [], 'edits': edits}, open('tools/imf_games_2026-11-13.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# preview copies for review (not the live mirror)
import os; os.makedirs('tools/imf_preview', exist_ok=True)
for pid, t in pages.items(): open(f'tools/imf_preview/{pid}.html', 'w', encoding='utf-8').write(t)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages; previews in tools/imf_preview/')
