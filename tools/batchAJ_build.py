"""Batch AJ (2026-11-14): hands-on lab boxes from the study games, placed in the sections they teach.
Author's request 2026-11-14: "Add the six" (pH Dial, Enzyme Bench lab, Enzyme Bench free play, Build and break fats,
Spot It, Condense & Hydrolyze) plus the H-Bond Lab in 1.8 as an option. Each box embeds the game in its compact
"?view=lab" view (only the demo plus an "Open the full game" link), added to the games on 2026-11-14 so the box can stay
short enough on a phone for the student to scroll the page around it. 1.8 is already the longest page in the book with
five embedded frames, so the H-Bond Lab gets a link box there, not a frame.
Print: the frame and the "Not loading?" line are hideprint; a showprint line says where the lab is online.
Output: tools/batchAJ_2026-11-14.json, tools/batchAJ_sha_2026-11-14.json, audit/preview/<id>.html, audit/BATCH_AJ_REVIEW.md"""
import json, hashlib, html, re

G = 'https://itsdrdan.github.io/'
BORDER = '#1f8a70'


def box(title, intro, url, height, label, game_name):
    u = html.escape(url)
    return (
        '<div class="box-note" style="border-left:6px solid %s;">\n'
        '<p class="boxtitle">%s</p>\n'
        '<p>%s</p>\n'
        '<p class="hideprint"><iframe src="%s" width="100%%" height="%d" style="border:0;border-radius:12px;background:#f5f6fb;" title="%s" loading="lazy"></iframe></p>\n'
        '<p class="hideprint" style="font-size:0.9em;">Not loading? <a style="text-decoration:underline" target="_blank" rel="noopener" href="%s">Open this lab in a new tab</a>.</p>\n'
        '<p class="showprint" style="font-size:0.9em;">This lab runs online: open this section in the web edition of the book, or play it in <em>%s</em> at itsdrdan.github.io.</p>\n'
        '</div>\n') % (BORDER, title, intro, u, height, html.escape(label), u, game_name)


SPOT = G + 'organic/?mode=spot&groups=alcohol,phenol,ether,thiol,alkene&view=lab'
FATS = G + 'lipids/?topic=lab&view=lab'
DIAL = G + 'pHcharge/?topic=dial&view=lab'
PEP = G + 'aminoacids/?mode=build&view=lab'
FREE = G + 'enzymes/?explore=1&view=lab'
GUIDED = G + 'enzymes/?topic=bench&fam=temp,pH,sub&view=lab'
INH = G + 'enzymes/?topic=bench&fam=inh&view=lab'
HBOND = G + 'IMF/?course=3B&mode=lab&view=lab'

PLAN = [
    ('597090', '4.1', 'Spot It (before the Professor Tip in "Sorting a molecule into the right family")',
     '<div class="box-note">\n<p class="boxtitle">Professor Tip</p>\n<p>Many real molecules carry more than one of these groups.',
     'before',
     box('Hands-on Lab: Spot the group',
         'Tap any atom of the named group in a real molecule: a drug, a flavor or an amino acid. A right tap lights up the whole group; '
         'a wrong tap tells you which group that atom belongs to. This set asks only about groups you know so far: alcohol, phenol, ether, '
         'thiol, and the alkene from Chapter 3. Your progress is saved in this browser.',
         SPOT, 560, 'Hands-on Lab: Spot the group', 'Functional Group Flashcards')),
    ('597145', '9.2', 'Build and break fats (end of "The three reactions", before "Oxidation of fats")',
     '</div><div class="mt-section" id="section_8"><h3 class="editable">Oxidation of fats (rancidity)</h3>',
     'before',
     box('Hands-on Lab: Build and break fats',
         'Build a triacylglycerol one ester bond at a time by tapping the &ndash;OH of a fatty acid and the H of glycerol that leave as water, '
         'then take fats and waxes apart by hydrolysis (acid or lipase) or saponification (NaOH or KOH). A wrong pick tells you why it is wrong. '
         'Your progress is saved in this browser.',
         FATS, 600, 'Hands-on Lab: Build and break fats', 'Lipid Lab')),
    ('597155', '10.2', 'pH Dial (after the worked examples, before the second Try It box)',
     '<div class="box-note" style="border-left:6px solid #86509b;">\n<p class="boxtitle">Try It: Amino acids and charge</p>',
     'before-last',
     box('Hands-on Lab: pH Dial',
         'Predict an amino acid&rsquo;s net charge, then turn the dial between strongly acidic, the pI, pH 7.4 and strongly basic. '
         'Watch each group gain or lose H<sup>+</sup> and the electrophoresis spot move, explain what happened, and apply it to a second amino acid. '
         'Your progress is saved in this browser.',
         DIAL, 640, 'Hands-on Lab: pH Dial', 'Proton Patrol')),
    ('597157', '10.4', 'Condense & Hydrolyze (end of "Condensation builds it, hydrolysis breaks it")',
     '</div><div class="mt-section" id="section_4"><h3 class="editable">Naming and writing peptides</h3>',
     'before',
     box('Hands-on Lab: Condense and hydrolyze',
         'Build a peptide by picking the H and the OH that leave as water, or pick the peptide bond that hydrolysis breaks. '
         'Some rounds ask how many peptide bonds or water molecules a chain has (<em>n</em> amino acids, <em>n</em> &minus; 1 bonds). '
         'Your progress is saved in this browser.',
         PEP, 560, 'Hands-on Lab: Condense and hydrolyze', 'Peptide Party')),
    ('597168', '11.3', 'Enzyme Bench free play (end of "Four variables, four curves", before "Worked examples")',
     '</div><div class="mt-section" id="section_8"><h3 class="editable">Worked examples</h3>',
     'before',
     box('Hands-on Lab: Enzyme Bench',
         'Every control is live: amount of substrate, amount of enzyme, temperature, pH, and the enzyme itself (pepsin, trypsin or a typical body enzyme). '
         'The red dot shows the rate at your settings. Work through the goals, such as finding where more substrate stops helping, or denaturing the enzyme '
         'with heat and cooling it again. The inhibitor controls belong to Section 11.4. For guided questions (predict, change one control, explain), '
         'open the <a style="text-decoration:underline" target="_blank" rel="noopener" href="%s">Enzyme Bench lab</a>.' % html.escape(GUIDED),
         FREE, 640, 'Hands-on Lab: Enzyme Bench', 'Enzyme Engine')),
    ('597169', '11.4', 'Enzyme Bench inhibitor lab (end of "Competitive, noncompetitive, irreversible", before "Drugs that are inhibitors")',
     '</div><div class="mt-section" id="section_6"><h3 class="editable">Drugs that are inhibitors</h3>',
     'before',
     box('Hands-on Lab: Inhibitors on the Enzyme Bench',
         'An inhibitor is present and the substrate is low. Predict what flooding the enzyme with substrate will do, turn the substrate up, '
         'then explain the result and apply it to a new case. A competitive inhibitor can be outcompeted by more substrate; a noncompetitive inhibitor cannot. '
         'Your progress is saved in this browser.',
         INH, 600, 'Hands-on Lab: Inhibitors on the Enzyme Bench', 'Enzyme Engine')),
    ('597061', '1.8', 'H-Bond Lab link box (end of "Hydrogen Bonding Intermolecular Forces", before "Hydrogen Bonding and DNA")',
     '<span id="Hydrogen_Bonding_and_DNA"></span>',
     'before',
     '<div class="box-note" style="border-left:6px solid %s;">\n<p class="boxtitle">See It Move: H-Bond Lab</p>\n'
     '<p>Heat or cool a box of water, ammonia, hydrogen fluoride, methanol or methane and watch hydrogen bonds form and break. Predict first, then check. '
     '<a class="hideprint" style="text-decoration:underline" target="_blank" rel="noopener" href="%s">Open the H-Bond Lab</a> '
     '(opens in a new tab).</p>\n'
     '<p class="showprint" style="font-size:0.9em;">The H-Bond Lab is in <em>Sticky Molecules</em> at itsdrdan.github.io; the web edition links to it.</p>\n'
     '</div>\n' % (BORDER, html.escape(HBOND))),
]

h = lambda x: hashlib.sha256(x.encode()).hexdigest()
edits, sha, rows = {}, {}, []
for pid, sec, where, anchor, mode, new_box in PLAN:
    page = open('pages/live/%s.html' % pid, encoding='utf-8').read()
    n = page.count(anchor)
    if mode == 'before':
        assert n == 1, (pid, n)
        old = anchor
    else:  # before-last: the anchor occurs twice; insert before the second
        assert n == 2, (pid, n)
        i = page.rfind(anchor)
        # make the "old" text unique by taking the anchor plus the iframe line after it
        old = page[i:page.find('</p>', page.find('<iframe', i)) + 4]
        assert page.count(old) == 1, pid
    new = new_box + old
    after = page.replace(old, new, 1)
    assert after.count(new_box) == 1
    edits[pid] = [{'old': old, 'new': new, 'count': 1, 'note': '%s: %s' % (sec, where), 'why': 'Author request 2026-11-14 ("Add the six"; H-Bond Lab in 1.8 as an option)'}]
    sha[pid] = {'before': h(page), 'after': h(after)}
    open('audit/preview/%s.html' % pid, 'w', encoding='utf-8').write(after)
    rows.append((sec, pid, where, re.search(r'href="([^"]+)"', new_box).group(1)))

json.dump({'uploads': [], 'edits': edits}, open('tools/batchAJ_2026-11-14.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAJ_sha_2026-11-14.json', 'w'))
print(len(edits), 'pages')
for r in rows:
    print(' | '.join(r))
