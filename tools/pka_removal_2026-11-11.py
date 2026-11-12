"""Remove pKa/Ka from CHEM 3B (instructor decision 2026-11-11: GOB course, no pKa).

Builds tools/pka_removal_fixes_2026-11-11.json ({page: [{old, new, count}]}) from
pages/live/*.html. Acid strength is taught as a ranking (carboxylic acid > phenol
~ thiol > alcohol ~ water) plus the NaHCO3/NaOH bench tests, and ionization at body
pH by rule: -COOH -> -COO-, amines -> -NH3+, phenols/alcohols stay neutral.
"""
import json, re

def L(p):
    return open(f'pages/live/{p}.html').read()

F = {}
def add(page, old, new):
    F.setdefault(page, []).append({'old': old, 'new': new})

# ---------------------------------------------------------------- 4.10 (597099)
P = '597099'
add(P, '<li>Compare the acidity of water, alcohols, thiols, phenols, and carboxylic acids using pK<sub>a</sub> values.</li>',
       '<li>Rank water, alcohols, thiols, phenols, and carboxylic acids from least to most acidic.</li>')
add(P, 'This section gives you the pK<sub>a</sub> numbers, the reason behind them, and a bench test',
       'This section gives you the order of acid strength, the reason behind it, and a bench test')
add(P, '<p>Strong acids (HCl, H<sub>2</sub>SO<sub>4</sub>) ionize completely. Weak acids reach an equilibrium that lies mostly on the left, and the <strong>acid ionization constant</strong> K<sub>a</sub> measures how far to the right it goes. Chemists usually quote <strong>pK<sub>a</sub> = &minus;log K<sub>a</sub></strong>, which turns a wide range of K<sub>a</sub> values into a small, readable number. The rule to remember: <strong>the lower the pK<sub>a</sub>, the stronger the acid.</strong> Each unit of pK<sub>a</sub> is a factor of ten in K<sub>a</sub>, so an acid with pK<sub>a</sub> 10 is about a million times stronger than one with pK<sub>a</sub> 16.</p>',
       '<p>Strong acids (HCl, H<sub>2</sub>SO<sub>4</sub>) ionize completely. Weak acids ionize only slightly: the equilibrium lies mostly on the left, and most molecules keep their H. In this course you compare weak acids by <strong>ranking</strong> them, not with numbers: a stronger acid gives up its H<sup>+</sup> more readily, and you can see the difference at the bench by which bases (sodium bicarbonate or sodium hydroxide) it reacts with.</p>')
add(P, ' &nbsp;&nbsp;&nbsp; pK<sub>a</sub> &asymp; 16</p>', '</p>')
add(P, '<p>That pK<sub>a</sub> is almost the same as water\'s (15.7). Think about why:',
       '<p>Ethanol is about as acidic as water itself, which is to say barely at all. Think about why:')
add(P, ' Alcohols with more alkyl branching are a little <em>weaker</em> (2-methyl-2-propanol, pK<sub>a</sub> about 18), because the bulky alkyl groups crowd the oxygen and keep water molecules from surrounding and stabilizing the alkoxide ion.</p>',
       ' Alcohols with more alkyl branching, such as 2-methyl-2-propanol, are even a little <em>weaker</em>.</p>')
add(P, 'Its pK<sub>a</sub> is about 10: phenol is a weak acid, in the same general range as the bicarbonate ion or the ammonium ion, and about a million times more acidic than ethanol.</p>',
       'Phenol is a weak acid: much weaker than acetic acid, but far more acidic than ethanol, and acidic enough to react with sodium hydroxide.</p>')
add(P, 'stays in the same neighborhood, pK<sub>a</sub> roughly 10. For CHEM 3B,',
       'stays a weak acid of about the same strength. For CHEM 3B,')
add(P, '<p>Thiols, R&ndash;SH, have pK<sub>a</sub> values near 10&ndash;11, close to phenol and well below alcohols.',
       '<p>Thiols, R&ndash;SH, are about as acidic as phenols and much more acidic than alcohols.')
add(P, '<h2 class="editable">Putting the numbers side by side</h2>\n<p>The table and scale below compare the acids you have met so far with the carboxylic acids you will meet in Chapter 6. The practical dividing line for this course is <strong>pK<sub>a</sub> about 12</strong>: anything below it is acidic enough to be neutralized by NaOH in the lab; anything above it is not.</p>',
       '<h2 class="editable">Putting the acids side by side</h2>\n<p>The table below ranks the acids you have met so far, with the carboxylic acids of Chapter 6 for comparison. The practical test for this course is <strong>which base each one reacts with</strong>: carboxylic acids react with both sodium bicarbonate and sodium hydroxide, phenols and thiols react with hydroxide only, and alcohols react with neither.</p>')
add(P, '<thead><tr><th>Compound</th><th>Class</th><th>Approximate pK<sub>a</sub></th><th>Conjugate base</th><th>Reacts with NaOH(aq)?</th></tr></thead>',
       '<thead><tr><th>Compound</th><th>Class</th><th>Acid strength</th><th>Conjugate base</th><th>Reacts with NaOH(aq)?</th><th>Reacts with NaHCO<sub>3</sub>(aq)?</th></tr></thead>')
add(P, '<td>carboxylic acid</td><td>4.8</td><td>CH<sub>3</sub>COO<sup>&minus;</sup>, acetate</td><td>yes</td></tr>',
       '<td>carboxylic acid</td><td>strongest of these (still a weak acid)</td><td>CH<sub>3</sub>COO<sup>&minus;</sup>, acetate</td><td>yes</td><td>yes (fizzes, CO<sub>2</sub>)</td></tr>')
add(P, '<td>phenol</td><td>10</td><td>C<sub>6</sub>H<sub>5</sub>O<sup>&minus;</sup>, phenoxide</td><td>yes</td></tr>',
       '<td>phenol</td><td>weak acid</td><td>C<sub>6</sub>H<sub>5</sub>O<sup>&minus;</sup>, phenoxide</td><td>yes</td><td>no</td></tr>')
add(P, '<td>thiol</td><td>10.6</td><td>CH<sub>3</sub>CH<sub>2</sub>S<sup>&minus;</sup>, thiolate</td><td>yes</td></tr>',
       '<td>thiol</td><td>weak acid, about like phenol</td><td>CH<sub>3</sub>CH<sub>2</sub>S<sup>&minus;</sup>, thiolate</td><td>yes</td><td>no</td></tr>')
add(P, '<td>&mdash;</td><td>15.7</td><td>OH<sup>&minus;</sup>, hydroxide</td><td>&mdash;</td></tr>',
       '<td>&mdash;</td><td>barely acidic</td><td>OH<sup>&minus;</sup>, hydroxide</td><td>&mdash;</td><td>&mdash;</td></tr>')
add(P, '<td>alcohol (1&deg;)</td><td>16</td><td>CH<sub>3</sub>CH<sub>2</sub>O<sup>&minus;</sup>, ethoxide</td><td>no</td></tr>',
       '<td>alcohol (1&deg;)</td><td>about like water (neutral)</td><td>CH<sub>3</sub>CH<sub>2</sub>O<sup>&minus;</sup>, ethoxide</td><td>no</td><td>no</td></tr>')
add(P, '<td>alcohol (3&deg;)</td><td>18</td><td>(CH<sub>3</sub>)<sub>3</sub>CO<sup>&minus;</sup></td><td>no</td></tr>',
       '<td>alcohol (3&deg;)</td><td>slightly weaker than water (neutral)</td><td>(CH<sub>3</sub>)<sub>3</sub>CO<sup>&minus;</sup></td><td>no</td><td>no</td></tr>')
t = L(P)
a = t.index('<figure class="figure"><img class="internal" alt="A pKa scale'); b = t.index('</figure>', a) + len('</figure>\n\n')
add(P, t[a:b], '')   # remove the pKa-scale figure (old Figure 4.10.2)
add(P, '<figcaption>Figure 4.10.3: The sodium hydroxide test.', '<figcaption>Figure 4.10.2: The sodium hydroxide test.')
add(P, '<p>Students often reverse the pK<sub>a</sub> scale. Anchor it with one pair you know: acetic acid (vinegar, pK<sub>a</sub> 4.8) is obviously an acid and ethanol (pK<sub>a</sub> 16) obviously is not, so <em>small number = strong acid</em>. Then place phenol in between. Everything else in this section follows from that one picture.</p>',
       '<p>Anchor the ranking with two things you already know: vinegar (acetic acid) is obviously an acid, and rubbing alcohol obviously is not. Phenol sits in between: acidic enough to react with NaOH, not acidic enough to react with baking soda (NaHCO<sub>3</sub>). Everything else in this section follows from that one picture.</p>')
add(P, 'Sodium bicarbonate (NaHCO<sub>3</sub>) neutralizes carboxylic acids (pK<sub>a</sub> about 5) but not phenols (pK<sub>a</sub> about 10), so',
       'Sodium bicarbonate (NaHCO<sub>3</sub>) neutralizes carboxylic acids but not the weaker phenols, so')
add(P, 'is the O&ndash;H (or S&ndash;H) acidic enough, that is, is the pK<sub>a</sub> below about 12? (a) 2-Propanol is an alcohol, pK<sub>a</sub> about 17: <strong>no reaction</strong>. (b) The OH of <em>p</em>-cresol is on the ring, so it is a phenol, pK<sub>a</sub> about 10: <strong>reacts</strong>',
       'is the O&ndash;H (or S&ndash;H) acidic enough, that is, is it a phenol, a thiol or a carboxylic acid rather than an alcohol? (a) 2-Propanol is an alcohol: <strong>no reaction</strong>. (b) The OH of <em>p</em>-cresol is on the ring, so it is a phenol: <strong>reacts</strong>')
add(P, '(d) A thiol, pK<sub>a</sub> about 10&ndash;11: <strong>reacts</strong>', '(d) A thiol: <strong>reacts</strong>')
add(P, '<p><strong>Solution.</strong> Use the pK<sub>a</sub> values: 2-methyl-2-propanol about 18, ethanol 16, phenol 10, acetic acid 4.8. Lower pK<sub>a</sub> is stronger, so:',
       '<p><strong>Solution.</strong> Rank by family: alcohols are the weakest (about like water, and the more crowded 3&deg; alcohol is weakest of all), phenols are weak acids, and carboxylic acids are the strongest organic acids, so:')
add(P, 'By contrast, ethanol\'s pK<sub>a</sub> of about 16 means it is never ionized at the body\'s pH of 7.4;',
       'By contrast, ethanol is no more acidic than water, so it is never ionized at the body\'s pH of 7.4;')
add(P, '<li>A Br&oslash;nsted&ndash;Lowry acid donates H<sup>+</sup>; the lower the pK<sub>a</sub>, the stronger the acid. An acid is stronger',
       '<li>A Br&oslash;nsted&ndash;Lowry acid donates H<sup>+</sup>; a stronger acid gives it up more readily. An acid is stronger')
add(P, '<li>Alcohols (pK<sub>a</sub> about 16&ndash;18) are about as acidic as water', '<li>Alcohols are about as acidic as water')
add(P, '<li>Phenols (pK<sub>a</sub> about 10) are weak acids', '<li>Phenols are weak acids')
add(P, '<li>Thiols (pK<sub>a</sub> about 10&ndash;11) are much more acidic', '<li>Thiols are much more acidic')
add(P, '<li>Carboxylic acids (pK<sub>a</sub> about 5) are stronger still', '<li>Carboxylic acids are stronger still')
# Exercise 1 (question + inline answer + key answer)
add(P, '<p>Which is the stronger acid, a compound with pK<sub>a</sub> 9.9 or one with pK<sub>a</sub> 15.9? By roughly what factor?</p>',
       '<p>Rank from least to most acidic: ethanethiol, ethanol, acetic acid. Give a one-line reason for each step.</p>')
add(P, '<div>The compound with pK<sub>a</sub> 9.9 is stronger. The pK<sub>a</sub> values differ by 6 units, so its K<sub>a</sub> is about 10<sup>6</sup> (one million) times larger.</div>',
       '<div>Ethanol &lt; ethanethiol &lt; acetic acid. Ethanol is an alcohol, about as acidic as water. Ethanethiol is a weak acid, about like phenol, because the large sulfur atom spreads out the charge of the thiolate ion. Acetic acid is a carboxylic acid, the strongest of the three, because the charge of acetate is shared by two oxygens.</div>')
add(P, 'why phenol (pK<sub>a</sub> 10) is a much stronger acid than cyclohexanol (pK<sub>a</sub> about 17), even though',
       'why phenol is a much stronger acid than cyclohexanol, even though')
add(P, '<div>2-Methyl-2-propanol (pK<sub>a</sub> about 18) &lt; water (15.7) &lt; phenol (10) &lt; acetic acid (4.8).',
       '<div>2-Methyl-2-propanol &lt; water &lt; phenol &lt; acetic acid.')
add(P, 'Which is not ionized at all for practical purposes? Use pK<sub>a</sub> values in your answer.</p>',
       'Which is not ionized at all for practical purposes? Explain.</p>')
add(P, '<div>Acetaminophen\'s phenol group has a pK<sub>a</sub> near 10, so at pH 7.4 only a tiny fraction (well under 1%; about 0.3% for a pK<sub>a</sub> of 10) is ionized; it is mostly un-ionized but measurably acidic. Ethanol, with a pK<sub>a</sub> of about 16, is more than eight pK<sub>a</sub> units above blood pH, so essentially none of it is ionized; its acidity plays no role in the body.</div>',
       '<div>Acetaminophen\'s phenol group is a weak acid, so at pH 7.4 only a tiny fraction of it (well under 1%) is ionized; it is mostly un-ionized but measurably acidic. Ethanol is no more acidic than water, so essentially none of it is ionized; its acidity plays no role in the body.</div>')

# ---------------------------------------------------------------- 6.10 (597118)
P = '597118'
add(P, '<li>Use pK<sub>a</sub> to compare the strengths of organic acids: carboxylic acid &gt; phenol &gt; alcohol.</li>',
       '<li>Rank the strengths of organic acids: carboxylic acid &gt; phenol &gt; alcohol.</li>')
add(P, 'A refresher on pH before you compare it with pKa.', 'A refresher on pH before you compare acid strengths.')
add(P, '<h2 class="editable">Strength of an acid: p<em>K</em><sub>a</sub></h2>', '<h2 class="editable">Strength of an acid</h2>')
add(P, 'Chemists summarize it with one number, the <strong>p<em>K</em><sub>a</sub></strong>: <strong>the lower the p<em>K</em><sub>a</sub>, the stronger the acid</strong>. Strong mineral acids such as HCl have p<em>K</em><sub>a</sub> values below 0. Among the organic acids in this course, carboxylic acids (p<em>K</em><sub>a</sub> about 4&ndash;5) are much stronger than phenols (about 10), which are stronger than alcohols (about 16).',
       'A stronger acid gives up its proton more readily. Strong mineral acids such as HCl give up essentially all of their protons in water. Among the organic acids in this course, <strong>carboxylic acids are much stronger than phenols, which are stronger than alcohols</strong> (alcohols are about as weak as water itself).')
# strip the pKa labels under every equation
t = L(P)
def strip_underset(s):
    out = s
    while True:
        i = out.find('\\underset{pK_a')
        if i < 0: return out
        j = out.index('}', i)            # end of the label (no nested braces in labels)
        assert out[j+1] == '{'
        d = 0
        for k in range(j+1, len(out)):
            if out[k] == '{': d += 1
            elif out[k] == '}':
                d -= 1
                if d == 0: break
        out = out[:i] + out[j+2:k] + out[k+1:]
amph_a = t.index('<p>Alcohols are amphoteric'); amph_b = t.index('<span id="Ionization_of_acidic')
for m in re.finditer(r'<p>\\\[\\ce\{.*?\\nonumber \\\]</p>', t):
    if 'underset{pK_a' in m.group(0) and not (amph_a <= m.start() < amph_b):
        add(P, m.group(0), strip_underset(m.group(0)))
add(P, '<p>Alcohols (\\(\\ce{R-OH, pK_a \\;\\text ~16}\\)) are also weak acids and not fully neutralized with bases like \\(\\ce{^{-}OH}\\), as shown below.</p>',
       '<p>Alcohols (\\(\\ce{R-OH}\\)) are about as weak as water and are not neutralized by bases like \\(\\ce{^{-}OH}\\); only a trace reacts, as shown below.</p>')
add(P, t[amph_a:amph_b], '')   # amphoteric alcohols/carbonyl protonation by H2SO4, "intermediates in organic reactions"
add(P, '<p>Whether a group is ionized depends on the pH around it compared with its p<em>K</em><sub>a</sub>. If the pH is at least two units <strong>above</strong> the p<em>K</em><sub>a</sub> of an acid, almost all of it has lost its proton (A<sup>&minus;</sup>). If the pH is at least two units <strong>below</strong> the p<em>K</em><sub>a</sub> of a protonated amine (R&ndash;NH<sub>3</sub><sup>+</sup>), almost all of it keeps its proton.</p>\n<p>The following conclusions are drawn by applying the above rules to the functional groups commonly found in cells.</p>',
       '<p>Whether a group is ionized depends on how strong an acid (or base) it is and on the pH around it. Body fluids are close to neutral (blood is at pH 7.4), and at that pH the functional groups commonly found in cells behave as follows.</p>')
add(P, 'have \\(\\ce{pK_a}\\) 4 to 5. So, carboxylic acids exist', 'give up their proton at this pH. So, carboxylic acids exist')
add(P, '<li>The conjugate acid forms of amines \\(\\ce{R-NH3^{+}}\\) have \\(\\ce{pK_{a}}\\) 9 to 11. So, amines exist',
       '<li>Amines are bases, and at this pH they pick up a proton. So, amines exist')
add(P, 'present in DNA and RNA molecules have \\(\\ce{pK_{a}}\\) 1 to 3. So, phosphodiesters also exist',
       'present in DNA and RNA molecules are even stronger acids than carboxylic acids. So, phosphodiesters also exist')
add(P, 'the three ideas you will use most: what pK<sub>a</sub> means, where carboxylic acids sit',
       'the three ideas you will use most: how acid strength is ranked, where carboxylic acids sit')
add(P, '<p>For this section, know: (1) p<em>K</em><sub>a</sub> measures acid strength, lower = stronger; (2) the approximate order <strong>carboxylic acid (about 4&ndash;5) &lt; phenol (about 10) &lt; alcohol (about 16)</strong>, with strong mineral acids such as HCl below 0; and (3) at a pH well above its p<em>K</em><sub>a</sub>, an acid exists as its conjugate base. No K<sub>a</sub> or Henderson&ndash;Hasselbalch calculations are asked.</p>',
       '<p>For this section, know: (1) the order of acid strength, <strong>carboxylic acid &gt; phenol &gt; alcohol</strong>, with strong mineral acids such as HCl stronger than all of them; (2) the bench tests that show it: carboxylic acids react with NaHCO<sub>3</sub> and NaOH, phenols with NaOH only, alcohols with neither; and (3) the body-pH rule: at pH 7.4, carboxylic acids are carboxylate ions (RCOO<sup>&minus;</sup>) and amines are ammonium ions (RNH<sub>3</sub><sup>+</sup>). No calculations are asked.</p>')
add(P, '<h3 class="editable">pK<sub>a</sub>: how weak is weak?</h3>', '<h3 class="editable">How weak is weak?</h3>')
add(P, 'so the ionization is written with equilibrium arrows (Section 6.4). Their strength is described by the acid dissociation constant, usually quoted as the <strong>pK<sub>a</sub></strong> (the lower the pK<sub>a</sub>, the stronger the acid). Most simple carboxylic acids have pK<sub>a</sub> values of about <strong>4&ndash;5</strong> (acetic acid 4.8, benzoic acid 4.2, lactic acid 3.9). For comparison, phenol has a pK<sub>a</sub> near 10 and an alcohol near 16, while HCl is a strong acid and ionizes completely. So carboxylic acids are the most acidic organic group you have met, but still far weaker than the mineral acids. Section 4.10 built the alcohol&ndash;phenol end of this scale; this section adds the carboxylic acids at the strong end.</p>',
       'so the ionization is written with equilibrium arrows (Section 6.4). Still, they are the most acidic organic group you have met: much more acidic than phenols, which are more acidic than alcohols. HCl, by contrast, is a strong acid and ionizes completely, so carboxylic acids are far weaker than the mineral acids. Section 4.10 built the alcohol&ndash;phenol end of this ranking; this section adds the carboxylic acids at the strong end. The table shows how you see the ranking at the bench.</p>')
add(P, '<th>Example</th><th>Approximate pK<sub>a</sub></th><th>Reacts with NaOH?</th>', '<th>Example</th><th>Acid strength</th><th>Reacts with NaOH?</th>')
add(P, '<td>HCl</td><td>below 0</td>', '<td>HCl</td><td>strong</td>')
add(P, '<td>Acetic acid</td><td>4.8</td>', '<td>Acetic acid</td><td>weak (strongest organic acid)</td>')
add(P, '<td>Phenol</td><td>10</td>', '<td>Phenol</td><td>weaker</td>')
add(P, '<td>Ethanol</td><td>16</td>', '<td>Ethanol</td><td>about like water</td>')
add(P, '<h3 class="editable">Ionized or not? Compare pH with pK<sub>a</sub></h3>', '<h3 class="editable">Ionized or not at body pH?</h3>')
add(P, '<p>The pK<sub>a</sub> tells you the pH at which an acid is half ionized. At any pH more than about two units above the pK<sub>a</sub>, essentially all of the molecules have lost their proton. Blood is at pH 7.4, roughly three units above the pK<sub>a</sub> of a typical carboxylic acid, so more than 99% of',
       '<p>Blood is at pH 7.4, and at that pH a carboxylic acid has lost its proton: more than 99% of')
add(P, 'Run the comparison the other way in the stomach (pH about 1&ndash;2, well below pK<sub>a</sub> 4&ndash;5) and the same molecules are un-ionized,',
       'In the stomach (pH about 1&ndash;2), a strongly acidic place, the same molecules keep their proton and are un-ionized,')
add(P, '<p>You do not need the Henderson&ndash;Hasselbalch equation to answer &quot;ionized or not.&quot; Subtract: pH minus pK<sub>a</sub>. Positive by two or more means the acid has lost its proton (carboxylate, RCOO<sup>&minus;</sup>); negative by two or more means it has kept it (RCOOH); close to zero means a roughly even mixture. The same arithmetic works for the amines of Chapter 7 and the amino acids of Chapter 10.</p>',
       '<p>Two rules answer &quot;ionized or not&quot; for almost every molecule in this course. At body pH (about 7.4), write a carboxylic acid as the carboxylate (RCOO<sup>&minus;</sup>) and an amine as the ammonium ion (RNH<sub>3</sub><sup>+</sup>). In strong acid, such as stomach acid, a carboxylic acid keeps its H (RCOOH). Phenols and alcohols are too weak to lose their H at body pH and stay neutral. The same rules work for the amines of Chapter 7 and the amino acids of Chapter 10.</p>')
add(P, 'is a carboxylic acid at a pH three units above its pK<sub>a</sub>, so it is ionized.', 'is a carboxylic acid at blood pH, so it is ionized.')
add(P, 'makes lactic acid (pK<sub>a</sub> 3.9), which gives up', 'makes lactic acid, which gives up')
add(P, 'q=pK%7Cacidic%7Cioniz', 'q=acidic%7Cioniz')
add(P, '<li>p<em>K</em><sub>a</sub> measures acid strength: the lower the p<em>K</em><sub>a</sub>, the stronger the acid. Carboxylic acid (about 4&ndash;5) &gt; phenol (about 10) &gt; alcohol (about 16).</li>',
       '<li>Acid strength: carboxylic acid &gt; phenol &gt; alcohol (alcohols are about as weak as water).</li>')
add(P, '<li>Compare pH with p<em>K</em><sub>a</sub>: two or more units above, an acid has lost its proton; two or more units below, it keeps it.</li>',
       '<li>A carboxylic acid keeps its H in strong acid (such as stomach acid) and loses it at body pH.</li>')

# ---------------------------------------------------------------- other Ch 4 / Ch 6 pages
add('597096', 'The acidity comparison, with pK<sub>a</sub> values and the NaOH lab test, is worked out', 'The acidity comparison and the NaOH lab test are worked out')
add('597096', 'Phenol is a weak acid (pK<sub>a</sub> about 10) because', 'Phenol is a weak acid because')
add('597096', 'Section 4.10 gives the pK<sub>a</sub> table and the full reasoning.', 'Section 4.10 gives the full ranking and the reasoning.')
add('597098', 'Thiols are much more acidic than alcohols (pK<sub>a</sub> about 10&ndash;11, close to phenol) but, like alcohols, far weaker acids than carboxylic acids; Section 4.10 puts the numbers side by side.',
              'Thiols are much more acidic than alcohols (about as acidic as phenol) but, like alcohols, far weaker acids than carboxylic acids; Section 4.10 puts them side by side.')
add('597100', 'Phenols are weak acids (pK<sub>a</sub> about 10) because', 'Phenols are weak acids because')
add('597100', 'Thiols (pK<sub>a</sub> about 10&ndash;11) are much more acidic', 'Thiols are much more acidic')
add('597100', 'Details, the pK<sub>a</sub> table and the NaOH test:', 'Details, the ranking table and the NaOH test:')
add('597101', 'Its weak acidity (pK<sub>a</sub> about 10) contributes almost nothing', 'Its weak acidity contributes almost nothing')
add('597101', 'the negative charge of the phenoxide ion (pK<sub>a</sub> about 10). Benzyl alcohol has a CH<sub>2</sub> between the ring and the OH, so it is an ordinary alcohol (pK<sub>a</sub> about 16), like A and D.',
              'the negative charge of the phenoxide ion. Benzyl alcohol has a CH<sub>2</sub> between the ring and the OH, so it is an ordinary alcohol, like A and D.')
add('597101', '(c) Ethanethiol (pK<sub>a</sub> about 10.6) is more acidic than ethanol (about 16) because', '(c) Ethanethiol is more acidic than ethanol because')
add('597112', 'Carboxylic acids are the most acidic organic group you have met (pK<sub>a</sub> about 4&ndash;5; Section 6.10 compares them with phenols and alcohols), but',
              'Carboxylic acids are the most acidic organic group you have met (Section 6.10 compares them with phenols and alcohols), but')
add('597119', 'Carboxylic acids are weak acids with pK<sub>a</sub> about <strong>4&ndash;5</strong>, stronger than phenols (about 10) and alcohols (about 16) but far weaker than HCl. At a pH two or more units above the pK<sub>a</sub> an acid is ionized, so at blood pH 7.4',
              'Carboxylic acids are weak acids, <strong>stronger than phenols and alcohols</strong> but far weaker than HCl; they are the only ones of the three that fizz with NaHCO<sub>3</sub>. At body pH a carboxylic acid is ionized, so at blood pH 7.4')
add('597119', '(&ndash;COOH; weak acids pKa &asymp; 4&ndash;5; + base carboxylate salts)', '(&ndash;COOH; weak acids RCOO&minus; in body; + base carboxylate salts)')
# 6.12 Practice Problems (597120)
P = '597120'
add(P, '<div>C. Carboxylic acids (pK<sub>a</sub> about 4&ndash;5) are strong enough', '<div>C. Carboxylic acids are strong enough')
add(P, 'Phenol is a much weaker acid (pK<sub>a</sub> about 10) and does not react', 'Phenol is a much weaker acid and does not react')
add(P, '<p><strong>Analyze the table.</strong> The table lists pK<sub>a</sub> values for several compounds that appear in this chapter.</p>',
       '<p><strong>Analyze the table.</strong> The table lists several acids that appear in this chapter.</p>')
add(P, '<caption>pKa values of acids from this chapter</caption>\n<thead><tr><th>Compound</th><th>Acidic group</th><th>pK<sub>a</sub></th></tr></thead>',
       '<caption>Acids from this chapter</caption>\n<thead><tr><th>Compound</th><th>Acidic group</th></tr></thead>')
for name, grp, val in [('Salicylic acid', 'Carboxylic acid', '3.0'), ('Lactic acid', 'Carboxylic acid', '3.9'), ('Benzoic acid', 'Carboxylic acid', '4.2'), ('Acetic acid', 'Carboxylic acid', '4.8'), ('Phenol', 'Phenol O&ndash;H', '10.0')]:
    add(P, f'<tr><td>{name}</td><td>{grp}</td><td>{val}</td></tr>', f'<tr><td>{name}</td><td>{grp}</td></tr>')
add(P, '<p>(a) Which compound is the strongest acid? (b) A pH two units above the pK<sub>a</sub> means about 99% of the molecules are ionized; two units below means about 1%. At blood pH 7.4, which compounds are essentially all in the ionized (anion) form, and which is almost entirely un-ionized? (c) Explain why the phenol &ndash;OH of salicylic acid is not listed as a second acidic group that matters at body pH.</p>',
       '<p>(a) Which compounds would fizz (give off CO<sub>2</sub>) with sodium bicarbonate, and which would not? (b) At blood pH 7.4, which compounds are essentially all in the ionized (anion) form, and which is almost entirely un-ionized? Name the ions. (c) Explain why the phenol &ndash;OH of salicylic acid is not listed as a second acidic group that matters at body pH.</p>')
add(P, '<div>(a) Salicylic acid: the lowest pK<sub>a</sub> means the largest fraction ionized in water. (b) pH 7.4 is 2.6 to 4.4 units above the pK<sub>a</sub> of every carboxylic acid in the table, so salicylic, lactic, benzoic, and acetic acids all exist more than 99% as their carboxylate ions (salicylate, lactate, benzoate, acetate). Phenol\'s pK<sub>a</sub> is 2.6 units <em>above</em> 7.4, so it is more than 99% un-ionized in blood. (c) The phenol &ndash;OH on salicylic acid behaves like phenol (pK<sub>a</sub> about 13 in this molecule, even higher than phenol itself) and stays protonated at pH 7.4, so only the carboxyl group contributes a charge; salicylate carries a single negative charge in the body.</div>',
       '<div>(a) The four carboxylic acids (salicylic, lactic, benzoic and acetic acid) fizz with NaHCO<sub>3</sub>; phenol is too weak an acid and does not. (b) At body pH every carboxylic acid has lost its proton, so salicylic, lactic, benzoic and acetic acids exist almost entirely as their carboxylate ions (salicylate, lactate, benzoate, acetate). Phenol is too weak an acid to lose its proton at pH 7.4, so it stays un-ionized. (c) The phenol &ndash;OH on salicylic acid behaves like phenol: it is too weak an acid to lose its H at pH 7.4, so only the carboxyl group contributes a charge; salicylate carries a single negative charge in the body.</div>')
add(P, '(b) The lab reports &quot;lactate,&quot; not &quot;lactic acid.&quot; Using the pK<sub>a</sub> of lactic acid (3.9), explain why.',
       '(b) The lab reports &quot;lactate,&quot; not &quot;lactic acid.&quot; Explain why.')
add(P, '(b) Blood pH (7.2&ndash;7.4) is more than three units above the pK<sub>a</sub>, so over 99.9% of the molecules have lost their carboxyl proton',
       '(b) Lactic acid is a carboxylic acid, and at blood pH (7.2&ndash;7.4) a carboxylic acid is ionized: essentially all of the molecules have lost their carboxyl proton')
add(P, '<p>Acetic acid has a p<em>K</em><sub>a</sub> of 4.8. (a) Write', '<p>Acetic acid is a typical carboxylic acid. (a) Write')
add(P, '(b) When the pH is above the p<em>K</em><sub>a</sub> the acid has given up its proton, so at pH 7.4 (almost three units above 4.8) essentially all of it is',
       '(b) At body pH a carboxylic acid gives up its proton, so at pH 7.4 essentially all of it is')

# ---------------------------------------------------------------- Ch 10
add('597048', '<div>&ndash;COO<sup>&minus;</sup>. Its p<em>K</em><sub>a</sub> (about 2&ndash;5) is well below 7.', '<div>&ndash;COO<sup>&minus;</sup>. A carboxylic acid loses its H<sup>+</sup> at body pH.')
add('597048', '<div>&ndash;NH<sub>3</sub><sup>+</sup>. The p<em>K</em><sub>a</sub> of its protonated form (about 9&ndash;11) is above 7.', '<div>&ndash;NH<sub>3</sub><sup>+</sup>. An amine picks up H<sup>+</sup> at body pH.')
P = '597154'
add(P, 'the only amino acid whose R group has a pK<sub>a</sub> (6.0) near physiological pH',
       'the only amino acid whose R group can gain or lose H<sup>+</sup> near physiological pH (mostly neutral at pH 7.4)')
add(P, '<p>(d) The pI (about 5.6) tells you the sign of the overall charge; the p<em>K</em><sub>a</sub> of each group tells you which form it is in. Threonine&rsquo;s &alpha;-COOH has p<em>K</em><sub>a</sub> &asymp; 2.1 and its &alpha;-NH<sub>3</sub><sup>+</sup> has p<em>K</em><sub>a</sub> &asymp; 9.1. At pH 1 (below both) both groups hold their H<sup>+</sup>:',
       '<p>(d) Use the acid and base rules for each group. In strong acid (pH 1) both groups hold their H<sup>+</sup>:')
add(P, 'net +1. At pH 11 (above both) both have lost it:', 'net +1. In strong base (pH 11) both have lost it:')
add(P, 'net &minus;1. Between the two p<em>K</em><sub>a</sub> values, including at the pI, the zwitterion drawn above is the main form.',
       'net &minus;1. In between, including at body pH and at the pI (about 5.6), the zwitterion drawn above is the main form.')
P = '597165'
add(P, 'whose side-chain carboxyl groups are deprotonated at pH 7 (their side-chain pK<sub>a</sub> values, about 3.9 for Asp and 4.1 for Glu, are well below 7).',
       'whose side-chain carboxyl groups are deprotonated at pH 7 (like every carboxylic acid, they lose their H<sup>+</sup> at body pH).')
add(P, 'Strong acid would protonate the carboxylates to neutral &ndash;COOH (the pH would be below the side-chain pK<sub>a</sub> of Asp and Glu, about 4), removing',
       'Strong acid would protonate the carboxylates to neutral &ndash;COOH (in strong acid a carboxylic acid keeps its H), removing')
add(P, 'and the lysine side chain +1 (its &ndash;NH<sub>3</sub><sup>+</sup> has p<em>K</em><sub>a</sub> &asymp; 10.5, so at pH 7.4, well below that p<em>K</em><sub>a</sub>, it stays protonated; the pI of free lysine, about 9.7, is not the side-chain p<em>K</em><sub>a</sub>).',
       'and the lysine side chain +1 (lysine is a basic amino acid: like every amine, its side-chain &ndash;NH<sub>2</sub> picks up H<sup>+</sup> at body pH).')
add(P, '<p>A student explains: &ldquo;At pH 10, the lysine side chain in the peptide Ala-Lys-Gly is neutral, because pH 10 is above lysine&rsquo;s pI of 9.7.&rdquo; Find the error and correct it.</p>',
       '<p>A student explains: &ldquo;At pH 7.4, the peptide Ala-Lys-Gly has a net charge of 0, because only the two ends of a peptide carry charges and they cancel.&rdquo; Find the error and correct it.</p>')
add(P, '<div>The pI is the pH at which a <strong>whole free amino acid</strong> has a net charge of zero; it does not tell you the form of one group in a peptide. For the side chain, compare the pH with the <strong>side-chain p<em>K</em><sub>a</sub></strong> of lysine&rsquo;s &ndash;NH<sub>3</sub><sup>+</sup>, about 10.5. pH 10 is still below 10.5, so most lysine side chains are <strong>still protonated (+1)</strong>. They lose the proton only at higher pH. Review: Section 10.2.</div>',
       '<div>Side chains can carry charges too. Lysine is a <strong>basic amino acid</strong>: its side chain ends in an amine, and like every amine it picks up H<sup>+</sup> at body pH, so it is <strong>&ndash;NH<sub>3</sub><sup>+</sup> (+1)</strong>. The N-terminus (+1) and C-terminus (&minus;1) cancel, so the peptide&rsquo;s net charge is <strong>+1</strong>, not 0. Review: Section 10.2.</div>')
add(P, 'An amino acid carries a carboxylic acid (p<em>K</em><sub>a</sub> about 2) and an amine (p<em>K</em><sub>a</sub> about 9&ndash;10). At pH 7',
       'An amino acid carries a carboxylic acid and an amine. At pH 7')
# ---------------------------------------------------------------- Ch 13 / 14
add('597192', 'Lactic acid (pK<sub>a</sub> about 3.9) is fully ionized at blood pH,', 'Lactic acid, a carboxylic acid, is fully ionized at blood pH,')
add('597206', 'a carboxylic acid (pK<sub>a</sub> about 3.9), so the fermentation', 'a carboxylic acid, so the fermentation')
# ---------------------------------------------------------------- glossary / index
t = L('488232'); a = t.index('<tr><td data-th="Word(s)">pKa</td>'); b = t.index('</tr>', a) + len('</tr>')
nl = t[b:b+1] if t[b:b+1] == '\n' else ''
add('488232', t[a:b] + nl, '')
add('488231', '<li>pKa, 6.10</li>', '')

# ---------------------------------------------------------------- scope notes
add('597270', 'LiAlH<sub>4</sub> reductions, the Henderson&ndash;Hasselbalch equation, E/Z names',
              'LiAlH<sub>4</sub> reductions, pK<sub>a</sub> values and the Henderson&ndash;Hasselbalch equation, E/Z names')
add('597396', '<li>No reaction mechanisms with curved arrows, no R/S, no Henderson&ndash;Hasselbalch calculations.</li>',
              '<li>No reaction mechanisms with curved arrows, no R/S, no pK<sub>a</sub> values or Henderson&ndash;Hasselbalch calculations. Acid strength is a ranking (carboxylic acid &gt; phenol &gt; alcohol) shown with the NaHCO<sub>3</sub> and NaOH tests; at body pH, &ndash;COOH is written &ndash;COO<sup>&minus;</sup> and amines &ndash;NH<sub>3</sub><sup>+</sup>.</li>')

if __name__ == '__main__':
    bad = 0
    for p, es in F.items():
        t = L(p)
        for e in es:
            e['count'] = t.count(e['old'])
            if e['count'] < 1: print('MISSING', p, e['old'][:90]); bad += 1
        for e in es: t = t.replace(e['old'], e['new'])
        F_left = len(re.findall(r'(?<![A-Za-z])p(?:<[^>]+>|\\[a-z]+\{|[{}_\s])*K(?:<[^>]+>|[{}_\s])*a(?![a-z])', t))
        print(p, len(es), 'edits; pKa left:', F_left)
    json.dump(F, open('tools/pka_removal_fixes_2026-11-11.json', 'w'), ensure_ascii=False, indent=1)
    print('bad', bad)
