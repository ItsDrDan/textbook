r"""Round 3 (author decisions, 2026-11-18) for group t5_ch13-15.
1) 597193 glycolysis step list and 597202 citric acid cycle steps: rewrite every step sentence that still followed
   a Wikipedia/Malik ordering into the book's own plain wording, then remove the "adapted from ... Wikipedia ...
   CC BY-SA 4.0" credit sentences (all step figures are already Daniel Kwasniewski's own SVGs).
2) 597213 ketone figures: blood level re-sourced and given as mmol/L with mg/100 mL; the unsourced "20 mg/day"
   urinary figure removed.
Same helper e(pageid, old, new, note, why); `old` must occur exactly once in the CURRENT pages/live/<id>.html
(after earlier edits on the same page). Running this file is a dry run: edits are applied in memory only and
written to SCRATCH/fixr3_t5_ch13-15.json. Nothing in the repo is written."""
import json, os, sys

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live'
SCRATCH = '/private/tmp/claude-501/-Users-dan-Desktop-Study-Games/4c975f86-6f1d-43c3-b73a-277836ad0562/scratchpad'
EDITS = []


def e(pageid, old, new, note, why):
    EDITS.append({'page': str(pageid), 'old': old, 'new': new, 'note': note, 'why': why})


def a(url, title):
    return '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>' % (url, title)


IND = 'Rewritten in the book\'s own wording so the step no longer follows the source sentence; chemistry unchanged.'

# ============================ 597193 (13.5) glycolysis ============================
e('597193',
  'The ten reactions of glycolysis are the following. (Step list adapted from the Italian Wikipedia article <a title="https://it.Wikipedia.org/wiki/Glicolisi" href="https://it.Wikipedia.org/wiki/Glicolisi" target="_blank" rel="external noopener nofollow" class="link-https">Glicolisi</a>, <a style="text-decoration:underline" href="https://creativecommons.org/licenses/by-sa/4.0/" rel="noopener" target="_blank">CC BY-SA 4.0</a>.)',
  'The ten reactions of glycolysis are the following.',
  'Remove the Wikipedia CC BY-SA credit (step list is now the author\'s own text)',
  'Author decision (round 3): every step sentence is now his own writing (see notes for the step-by-step comparison); the page\'s existing Malik CC0 credit line stays.')
e('597193',
  '2. Glucose-6-phosphate, which is an aldohexose, isomerizes to fructose-6-phosphate, which is a ketohexose.',
  '2. Phosphoglucose isomerase rearranges glucose 6-phosphate into fructose 6-phosphate. The C=O moves from C1 to C2, so an aldose becomes a ketose with the same formula.',
  'Step 2 rewritten', IND)
e('597193',
  '4. The open-chain form of fructose-1,6-bisphosphate, which is in equilibrium with the cyclic form, splits into two compounds, glyceraldehyde-3-phosphate and dihydroxyacetone phosphate.',
  '4. Aldolase cuts fructose 1,6-bisphosphate between C3 and C4. It works on the open-chain form of the sugar, which is in equilibrium with the ring. Each three-carbon piece keeps one phosphate: one is dihydroxyacetone phosphate (DHAP), the other glyceraldehyde 3-phosphate (G3P).',
  'Step 4 rewritten', IND)
e('597193',
  '5. This reaction is an isomerization reaction between glyceraldehyde-3-phosphate and its isomer dihydroxyacetone phosphate.',
  '5. Triose phosphate isomerase converts DHAP and G3P back and forth. Only G3P goes on to step 6, so as G3P is used up, DHAP keeps turning into more of it.',
  'Step 5 rewritten', IND)
e('597193',
  'The ketone group in dihydroxyacetone phosphate does not oxidize directly but converts to glyceraldehyde-3-phosphate due to the equilibrium in reaction 5. So, reaction 6 and the reactions after it happen twice for each glucose molecule.',
  'DHAP is never oxidized itself; step 5 turns it into G3P first. Each glucose therefore gives two G3P, and steps 6 to 10 run twice per glucose.',
  'Note after step 6 rewritten', IND)
e('597193',
  '7. A phosphate group is transferred from 1,3-bisphosphoglycerate to ADP producing an ATP and a 3-phosphoglycerate.',
  '7. Phosphoglycerate kinase moves the high-energy phosphate on C1 of 1,3-bisphosphoglycerate onto ADP. The products are ATP and 3-phosphoglycerate.',
  'Step 7 rewritten', IND)
e('597193',
  'Since this step happens twice for each glucose molecule processed, it compensates for the two ATP consumed, one in step 1 and the other in step 3.',
  'Because step 7 runs twice per glucose, its 2 ATP pay back the 2 ATP spent in steps 1 and 3.',
  'Note after step 7 rewritten', IND)
e('597193',
  '8. 3-Phosphoglycerate is isomerized to 2-phosphoglycerate. In this step, the enzyme phosphoglycerate mutase moves the phosphate group from carbon 3 to carbon 2.',
  '8. Phosphoglycerate mutase shifts the phosphate of 3-phosphoglycerate from C3 to C2, giving 2-phosphoglycerate. No atoms are gained or lost, so this is an isomerization.',
  'Step 8 rewritten', IND)
e('597193',
  r'9. 2-Phosphoglycerate is dehydrated, i.e., \(\ce{H2O}\) is eliminated from it, producing phosphoenolpyruvate.',
  r'9. Enolase removes a water molecule from 2-phosphoglycerate (a dehydration). The new C=C sits next to the phosphate, and the product is phosphoenolpyruvate (PEP).',
  'Step 9 rewritten', IND)
e('597193',
  '10. Phosphoenolpyruvate transfers its phosphate group to ADP producing pyruvate and ATP.',
  '10. Pyruvate kinase moves the phosphate from PEP onto ADP, giving ATP and pyruvate.',
  'Step 10 rewritten', IND)
e('597193',
  'Since the reaction happens two times for each glucose, two ATP are produced in this step.',
  'Step 10 also runs twice per glucose, so it makes 2 ATP.',
  'Note after step 10 rewritten', IND)

# ============================ 597202 (14.3) citric acid cycle ============================
e('597202',
  '<p>The following equations of the reactions are adapted from the Russian-language Wikipedia article on the citric acid cycle (<a style="text-decoration:underline" href="https://creativecommons.org/licenses/by-sa/4.0/" rel="noopener" target="_blank">CC BY-SA 4.0</a>), <a title="https://ru.Wikipedia.org/wiki/%D0%A6%D0%B8%D0%BA%D0%BB_%D1%82%D1%80%D0%B8%D0%BA%D0%B0%D1%80%D0%B1%D0%BE%D0%BD%D0%BE%D0%B2%D1%8B%D1%85_%D0%BA%D0%B8%D1%81%D0%BB%D0%BE%D1%82" href="https://ru.Wikipedia.org/wiki/%D0%A6%D0%B8%D0%BA%D0%BB_%D1%82%D1%80%D0%B8%D0%BA%D0%B0%D1%80%D0%B1%D0%BE%D0%BD%D0%BE%D0%B2%D1%8B%D1%85_%D0%BA%D0%B8%D1%81%D0%BB%D0%BE%D1%82" target="_blank" rel="external noopener nofollow" class="link-https">Wikipedia</a>.</p>',
  '<p>The eight reactions of the cycle are the following.</p>',
  'Remove the Wikipedia CC BY-SA credit paragraph',
  'Author decision (round 3): the adapted items were the ru.wikipedia equation images (Krebs_Cycle_Reaction_N_ru.png), all since replaced by Daniel Kwasniewski\'s own step SVGs; the step text is now his own wording (see notes). Replaced with a plain lead-in parallel to 13.5. The page\'s Malik CC0 credit line stays.')
e('597202',
  r'<strong>4. </strong>The fourth reaction resembles the previous link reaction\'s oxidative decarboxylation of pyruvate to acetyl-\(\ce{CoA}\). In this reaction, \(\ce{NAD^{+}}\) is reduced into \(\ce{NADH}\) at the expense of oxidative decarboxylation of \(\alpha\)-ketoglutarate and the resulting acyl-group is transferred to \(\ce{HS-CoA}\) resulting in succinyl-\(\ce{CoA}\) product as shown in the reaction below.'.replace("\\'", "'"),
  r'<strong>4. </strong>&alpha;-Ketoglutarate dehydrogenase does the same chemistry as pyruvate dehydrogenase (Section 14.1). A carboxylate leaves as CO<sub>2</sub>, the remaining four-carbon piece is oxidized while NAD<sup>+</sup> is reduced to NADH, and the piece is attached to HS&ndash;CoA as a thioester. The product is succinyl CoA, as shown below.',
  'Step 4 rewritten', IND)
e('597202',
  r'<strong>5. </strong>The fifth reaction has two steps. In the first step, a phosphate (\(\ce{Pi}\)) group takes the place of the \(\ce{-S-CoA}\) group of succinyl-\(\ce{CoA}\). The table below calls this a hydrolysis because the thioester bond is split in the same way, but here phosphate does the splitting instead of water, and that is how the energy is kept to make GTP. In the second step, the phosphate group is transferred to \(\ce{GDP}\) that converts to a \(\ce{GTP}\) in the same way as in steps 7 and 10 of glycolysis. \(\ce{GTP}\) reverts back to \(\ce{GDP}\) and transfers its phosphate group to \(\ce{ADP}\) that converts to one \(\ce{ATP}\). So, production of one \(\ce{GTP}\) is equal to production of one \(\ce{ATP}\). The overall reaction five is shown below.',
  r'<strong>5. </strong>Succinyl-CoA synthetase breaks the thioester of succinyl CoA in two moves. First, phosphate (P<sub>i</sub>) replaces the &ndash;S&ndash;CoA group and HS&ndash;CoA is released. The table below calls this a hydrolysis because the thioester bond is split the same way, but phosphate does the splitting instead of water, so the bond&rsquo;s energy is kept. Second, that phosphate goes to GDP, making GTP and succinate, the same kind of substrate-level phosphorylation as steps 7 and 10 of glycolysis. GTP then hands its phosphate to ADP, so one GTP counts as one ATP. The overall reaction is shown below.',
  'Step 5 rewritten', IND)
e('597202',
  r'<strong>6. </strong>In the sixth reaction, one \(\ce{FAD}\) is reduced into \(\ce{FADH_{2}}\) at the expense of oxidation of succinate to fumarate by the following overall reaction.',
  r'<strong>6. </strong>Succinate dehydrogenase takes two hydrogens from the &ndash;CH<sub>2</sub>&ndash;CH<sub>2</sub>&ndash; of succinate, making the C=C of fumarate. FAD accepts them and becomes FADH<sub>2</sub>, as shown below.',
  'Step 6 rewritten', IND)
e('597202',
  r'<strong>7.</strong> In the seventh reaction \(\ce{H2O}\) hydrates the \(\ce{C=C}\) of fumarate producing malate, as shown below.',
  r'<strong>7.</strong> Fumarase adds water across the C=C of fumarate (a hydration): &ndash;OH goes on one carbon and H on the other. The product is malate, as shown below.',
  'Step 7 rewritten', IND)
e('597202',
  'Recall that the enzymes are stereospecific. In this case, only fumarate (not its cis-isomer) reacts with the enzyme, and only one enantiomer of malate, L-malate, is produced.',
  'Fumarase is stereospecific. It accepts fumarate, the trans isomer, but not its cis isomer, and it makes only one enantiomer of malate, L-malate.',
  'Note after step 7 rewritten', IND)
e('597202',
  r'<strong>8. </strong>In the eighth step, one more \(\ce{NAD^{+}}\) is reduced into \(\ce{NADH}\) at the expense of oxidation of malate into oxaloacetate, as shown in the reaction below.',
  r'<strong>8. </strong>Malate dehydrogenase oxidizes the 2&deg; &ndash;OH of malate to a ketone, giving oxaloacetate, and NAD<sup>+</sup> is reduced to NADH, as shown below.',
  'Step 8 rewritten', IND)
e('597202',
  'The oxaloacetate is the reactant of step 1 and begins the cycle again by reacting with another acetyl-CoA. One citric acid cycle has the following overall reaction with one acetyl-\\(\\ce{CoA}\\).',
  'Oxaloacetate is where the cycle started, so it can now pick up another acetyl CoA and begin a new turn. One turn, for one acetyl CoA, adds up to this overall reaction.',
  'Note after step 8 rewritten', IND)
e('597202',
  r'Recall that the catabolism of one glucose molecule produces two pyruvates that, in turn, produce two acetyl-\(\ce{CoA}\) in the oxidative decarboxylation of pyruvate under aerobic conditions. So, the citric acid cycle runs twice for the catabolism of one glucose molecule. One \(\ce{GTP}\) ultimately converts into one \(\ce{ATP}\).',
  'One glucose gives two pyruvate, and each pyruvate gives one acetyl CoA in the link reaction, so the cycle turns twice per glucose. Each GTP counts as one ATP.',
  'Two-turns note rewritten', IND)

# ============================ 597213 (15.5) ketone figures ============================
e('597213',
  'Under normal conditions, the kidneys excrete about 20 mg of ketone bodies each day, and the blood levels are maintained at about 1 mg of ketone bodies per 100 mL of blood.',
  'Under normal conditions, blood ketone bodies stay low, about 0.1 to 0.25 mmol/L (roughly 1 to 3 mg per 100 mL of blood), and only a very small amount is lost in the urine (Source: Puchalska P, Crawford PA, %s, <em>Cell Metabolism</em>, 2017).' % a('https://pmc.ncbi.nlm.nih.gov/articles/PMC5313038/', 'Multi-dimensional roles of ketone bodies in fuel metabolism, signaling, and therapeutics'),
  'Ketone figures re-sourced: blood 0.1-0.25 mmol/L (~1-3 mg/100 mL); "20 mg/day" removed',
  'Puchalska & Crawford, Cell Metab 2017;25:262 (PMC5313038): total ketone bodies in healthy adults "normally exhibit circadian oscillations between approximately 100-250 uM", rising to ~1 mM after 24 h fasting; "A very small fraction of liver-derived ketone bodies can be readily measured in the urine." Conversion: 0.1-0.25 mmol/L x ~103 g/mol = 10-26 mg/L = about 1-3 mg/100 mL, so the old "about 1 mg/100 mL" sits at the low end. No legitimate source found for 20 mg/day (NCBI Bookshelf and StatPearls blocked automated access; a 1958 field study, seen only as a secondary copy, implies much more than 20 mg/day), so the number was removed rather than kept unsourced.')


def dry_run():
    pages, ok = {}, True
    for i, ed in enumerate(EDITS, 1):
        p = ed['page']
        if p not in pages:
            pages[p] = open(os.path.join(LIVE, p + '.html'), encoding='utf-8').read()
        n = pages[p].count(ed['old'])
        ok &= n == 1
        print('%2d %s %-14s %s' % (i, p, 'OK' if n == 1 else 'FAIL count=%d' % n, ed['note'][:70]))
        if n == 1:
            pages[p] = pages[p].replace(ed['old'], ed['new'])
    if ok:
        for p in ('597193', '597202'):
            assert 'wikipedia' not in pages[p].lower(), p
            assert 'by-sa' not in pages[p].lower(), p
        assert '20 mg of ketone' not in pages['597213']
    return ok


if __name__ == '__main__':
    ok = dry_run()
    json.dump(EDITS, open(os.path.join(SCRATCH, 'fixr3_t5_ch13-15.json'), 'w'), ensure_ascii=False, indent=1)
    print('ALL OK (%d edits)' % len(EDITS) if ok else 'SOME EDITS FAILED')
    sys.exit(0 if ok else 1)
