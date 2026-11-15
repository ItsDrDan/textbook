"""Batch AK (2026-11-15): carbonyl reduction written as [H], not H2/Ni (CHEM 3B co-author: use [O] and [H]
so students do not confuse reduction with hydrogenation). Hydrogenation of C=C keeps H2 with Pt/Ni.

uploads: PUT /@api/deki/pages/{page}/files/={name} from figures/pages/batchAK (raw.githubusercontent on this branch);
         same-name files get a new revision (same file id); new names give {{key}} -> new file id.
edits:   {page: [{old, new, count}]}, applied to the live page text (fetched fresh, counts checked first).
Writes tools/batchAK_2026-11-15.json."""
import json

uploads = [
    {'page': '597105', 'name': 'fig-p597105-1.svg'},
    {'page': '597105', 'name': 'fig-p597105-2.svg'},
    {'page': '597107', 'name': 'fig-p597107-2.svg'},
    {'page': '597107', 'name': 'fig-p597107-5.svg'},
    {'page': '597105', 'name': 'fig-p597105-red-butanal.svg', 'key': 'BUTANAL'},
    {'page': '597105', 'name': 'fig-p597105-red-cyclohexanone.svg', 'key': 'CYCLOHEX'},
]
E = {}
def e(p, old, new, n=1): E.setdefault(p, []).append({'old': old, 'new': new, 'count': n})

ROW_OLD = '<td>H<sub>2</sub> with Ni adds across the C=O: an aldehyde gives a 1&deg; alcohol, a ketone gives a 2&deg; alcohol.</td>'
ROW_NEW = '<td>[H] (a reducing agent) adds H atoms across the C=O: an aldehyde gives a 1&deg; alcohol, a ketone gives a 2&deg; alcohol.</td>'

# 5.4 Redox
P = '597105'
e(P, '<h4 class="editable">Catalytic hydrogenation of aldehydes and ketones</h4>\n\n<p>Hydrogen (\\(\\ce{H2}\\)) reduces aldehydes and ketones to alcohols in the presence of a metal catalyst such as finely divided \\(\\ce{Ni}\\), \\(\\ce{Pd}\\) or \\(\\ce{Pt}\\), as shown in the following examples.</p>',
     '<h4 class="editable">Reduction of aldehydes and ketones</h4>\n\n<p>A reducing agent, written [H] over the arrow, reduces aldehydes and ketones to alcohols: one H adds to the carbonyl carbon and one H adds to the oxygen, as shown in the following examples.</p>')
e(P, '<img alt="Butanal, CH3CH2CH2CH=O, plus H-H, with Ni over the arrow, gives 1-butanol, CH3CH2CH2CH2OH." class="internal" src="/@api/deki/files/428357/clipboard_eaa97acffbd4cb342e067ad23f4b2da9e.png" fileid="428357" />',
     '<img alt="Butanal, CH3CH2CH2CH=O, with [H] over the arrow, gives 1-butanol, CH3CH2CH2CH2OH." class="internal" width="545" style="max-width:100%;height:auto;" src="/@api/deki/files/{{BUTANAL}}/fig-p597105-red-butanal.svg" fileid="{{BUTANAL}}" />')
e(P, '<img alt="Cyclohexanone (a hexagon with C=O) plus H-H, with Ni over the arrow, gives cyclohexanol (a hexagon with OH)." class="internal" src="/@api/deki/files/428358/clipboard_eecc65630ff897e76d3e43e26c9d9a9bd.png" fileid="428358" />',
     '<img alt="Cyclohexanone (a hexagon with C=O), with [H] over the arrow, gives cyclohexanol (a hexagon with OH)." class="internal" width="430" style="max-width:100%;height:auto;" src="/@api/deki/files/{{CYCLOHEX}}/fig-p597105-red-cyclohexanone.svg" fileid="{{CYCLOHEX}}" />')
e(P, '<p>If a \\(\\ce{C=C}\\) bond and a \\(\\ce{C=O}\\) bond are present in the same molecule, catalytic hydrogenation reduces both, as shown below.</p>',
     '<p>Do not confuse reduction with hydrogenation. Hydrogenation (<a href="/@go/page/597081">Section 3.4</a>) is H<sub>2</sub> with a metal catalyst (Ni, Pd or Pt) adding across a C=C; reduction ([H]) turns a C=O into C&ndash;OH. When a molecule has both a C=C and a C=O, H<sub>2</sub> with a metal catalyst adds to both, as shown below.</p>')
e(P, 'In the laboratory an aldehyde or ketone can also be reduced by a hydride reagent such as sodium borohydride (NaBH<sub>4</sub>). Whatever the reagent,',
     'In the laboratory a common reducing agent is a hydride reagent such as sodium borohydride (NaBH<sub>4</sub>); in the body it is NADH (Chapter 13). Whatever the reagent,')
e(P, 'Write [O] for any oxidizing agent and [H] for any reducing agent (H<sub>2</sub> with a Ni, Pd or Pt catalyst, or NaBH<sub>4</sub>).',
     'Write [O] for any oxidizing agent and [H] for any reducing agent (such as NaBH<sub>4</sub>). Use [H] for a C=O becoming C&ndash;OH; H<sub>2</sub> with a Ni, Pd or Pt catalyst adding across a C=C is hydrogenation.')
e(P, 'Hydrogen gas with a metal catalyst (Ni, Pd or Pt) or a hydride reagent such as sodium borohydride, NaBH<sub>4</sub>, adds two H atoms across the C=O:',
     'A reducing agent, written [H] (for example sodium borohydride, NaBH<sub>4</sub>), adds two H atoms across the C=O:')
e(P, 'alt="Reduction: propanal gives 1-propanol" width="569"', 'alt="Reduction: propanal gives 1-propanol" width="485"')
e(P, 'propanal + H<sub>2</sub> (Ni) &rarr; 1-propanol.', 'propanal &rarr; 1-propanol, with [H] over the arrow.')
e(P, 'alt="Reduction: propanone (acetone) gives 2-propanol (isopropyl alcohol)" width="522"', 'alt="Reduction: propanone (acetone) gives 2-propanol (isopropyl alcohol)" width="438"')
e(P, 'propanone (acetone) + H<sub>2</sub> (Ni) &rarr; 2-propanol (isopropyl alcohol).', 'propanone (acetone) &rarr; 2-propanol (isopropyl alcohol), with [H] over the arrow.')

# 5.6 Chapter Guide
P = '597107'
e(P, '<strong>Reduction</strong> [H] (H<sub>2</sub>/Ni, Pd or Pt, or NaBH<sub>4</sub>):', '<strong>Reduction</strong> [H] (a reducing agent such as NaBH<sub>4</sub>):')
e(P, 'Reduction of a carbonyl: H&#8322; adds across the C=O, turning it into C&ndash;OH.', 'Reduction of a carbonyl: [H] (a reducing agent) adds H atoms across the C=O, turning it into C&ndash;OH.')
e(P, ROW_OLD, ROW_NEW)
e(P, 'alt="Reduction: 2-butanone gives 2-butanol" width="566"', 'alt="Reduction: 2-butanone gives 2-butanol" width="482"', 2)

# 5.7 Practice Problems
P = '597108'
e(P, 'Reduction of 3-hexanone with H<sub>2</sub> (catalyst) gives', 'Reduction of 3-hexanone with [H] gives')
e(P, 'when each is reduced with H<sub>2</sub>/Ni.', 'when each is reduced with [H].')
e(P, 'Reduction: 2-pentanone + H<sub>2</sub> &rarr; 2-pentanol; 2-pentanol is already reduced and does not add H<sub>2</sub>.',
     'Reduction: 2-pentanone + [H] &rarr; 2-pentanol; 2-pentanol is already reduced and does not react with [H].')
e(P, '[H] (a reducing agent such as H<sub>2</sub>/Pd or NaBH<sub>4</sub>)', '[H] (a reducing agent such as NaBH<sub>4</sub>)')

# 7.12 Chapter Guide (Reaction Roadmap)
P = '597132'
e(P, 'Aldehydes are reduced back to 1&deg; alcohols with H<sub>2</sub> and Ni, the same way as ketones.', 'Aldehydes are reduced back to 1&deg; alcohols with [H], the same way as ketones.')
e(P, 'ketone reduced back to alcohol with H2 and Ni', 'ketone reduced back to alcohol with [H]', None)
e(P, 'roadmap.svg?v=20261113', 'roadmap.svg?v=20261115', None)
e(P, ROW_OLD, ROW_NEW)

# 8.5 Properties of Monosaccharides
P = '597138'
e(P, '(NaBH<sub>4</sub>, or H<sub>2</sub> with a metal catalyst) gives a sugar alcohol', '([H], a reducing agent such as NaBH<sub>4</sub>) gives a sugar alcohol')
e(P, '(hydrogen gas with a metal catalyst, or an enzyme in the body)', '([H]: a reducing agent such as NaBH<sub>4</sub>, or an enzyme in the body)')

# 8.9 Practice Problems
P = '597142'
e(P, 'and (d) H<sub>2</sub> with a metal catalyst. Name each product', 'and (d) [H] (a reducing agent). Name each product')

# Glossary
e('488232', 'The addition of H<sub>2</sub> across a double or triple bond, using a metal catalyst such as Ni or Pt.<br />',
     'The addition of H<sub>2</sub> across a carbon&ndash;carbon double or triple bond, using a metal catalyst such as Ni or Pt. (A C=O becoming C&ndash;OH is a reduction, written [H].)<br />')

json.dump({'batch': 'AK', 'date': '2026-11-15', 'uploads': uploads, 'edits': E}, open('tools/batchAK_2026-11-15.json', 'w'), ensure_ascii=False, indent=1)
print({p: len(v) for p, v in E.items()})
