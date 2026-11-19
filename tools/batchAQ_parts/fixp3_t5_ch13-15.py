"""Round 2 (P3 polish) for group t5_ch13-15 (CHEM 3B textbook Ch 13-15), from srcaudit_t5_ch13-15.md.
Sources re-verified 2026-11-18. Same helper: e(pageid, old, new, note, why); `old` must occur exactly once in the
current pages/live/<pageid>.html (after earlier edits on the same page). Running this file is a dry run only:
it applies the edits in memory, checks counts, and writes SCRATCH/fixp3_t5_ch13-15.json. It never writes to the repo."""
import json, os, sys

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live'
SCRATCH = '/private/tmp/claude-501/-Users-dan-Desktop-Study-Games/4c975f86-6f1d-43c3-b73a-277836ad0562/scratchpad'
EDITS = []


def e(pageid, old, new, note, why):
    EDITS.append({'page': str(pageid), 'old': old, 'new': new, 'note': note, 'why': why})


def a(url, title):
    return '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>' % (url, title)


CCBYSA = a('https://creativecommons.org/licenses/by-sa/4.0/', 'CC BY-SA 4.0')
UMPIERREZ_URL = 'https://doi.org/10.2337/dci24-0032'
UMPIERREZ_T = 'Hyperglycemic Crises in Adult Patients With Diabetes: A Consensus Report'

# ---------------- 597213 (15.5) DKA box + main text ----------------
e('597213',
  'in DKA the blood pH is 7.30 or lower.<sup>2</sup>',
  'in DKA the blood pH falls below 7.3.<sup>4</sup>',
  'P3: DKA pH criterion updated to the 2024 consensus and cited',
  'Umpierrez GE et al. 2024 (ADA/EASD/JBDS/AACE/DTS consensus): DKA = glucose >=200 mg/dL or known diabetes, beta-hydroxybutyrate >=3.0 mmol/L (or urine ketones 2+), and "pH <7.3 and/or bicarbonate concentration <18 mmol/L" (criteria confirmed via ACP Diabetes Guide and CCJM 2025 summaries; publisher pages refuse automated fetch).')
e('597213',
  'Treatment usually starts with IV isotonic saline (0.9% NaCl) to replace lost fluid,',
  'Treatment starts with IV fluids to replace what was lost, either isotonic saline (0.9% NaCl) or a balanced salt solution such as lactated Ringer&rsquo;s,',
  'P3: fluid choice updated to the 2024 consensus (saline or balanced crystalloid)',
  'Outdated detail. The 2024 consensus recommends isotonic saline or balanced crystalloids and now suggests balanced crystalloids when available (CCJM 2025;92:152 summary of the consensus). The sentence already cites ^1,2 at its end; ^4 is added at the potassium sentence below.')
e('597213',
  'potassium is added to the IV fluids to replace this key electrolyte.<sup>1,2</sup>',
  'potassium is added to the IV fluids to replace this key electrolyte.<sup>1,2,4</sup>',
  'P3: add the 2024 consensus to the treatment citation',
  'Chiasson 2003 (PMC151994): 0.9% saline first, low-dose IV insulin, insulin delayed until K+ >3.3 mmol/L. 2024 consensus: postpone insulin until K+ >3.5 mmol/L. Both support "ruled out (or corrected) before insulin".')
e('597213',
  '2. Chiasson JL, et al., <a style="text-decoration:underline" href="https://cmaj.ca/content/cmaj/168/7/859.full-text.pdf" rel="noopener" target="_blank">',
  '2. Chiasson JL, et al., <a style="text-decoration:underline" href="https://pmc.ncbi.nlm.nih.gov/articles/PMC151994/" rel="noopener" target="_blank">',
  'P3: Chiasson 2003 link moved to the open PMC copy (CMAJ PDF returns 403)',
  'PMC151994 loads and states: "DKA will have a pH of 7.30 or less"; breath acetone with Kussmaul breathing; beta-hydroxybutyric and acetoacetic acids plus acetone; 0.9% saline; continuous low-dose insulin; K+ above 3.3 mmol/L before insulin. Kept because it still supports the ketone-body and acetone sentences (^2).')
e('597213',
  '2023 data).</p>\n</div></div>',
  '2023 data). 4. Umpierrez GE, et al., %s, <em>Diabetes Care</em>, 2024.</p>\n</div></div>' % a(UMPIERREZ_URL, UMPIERREZ_T),
  'P3: add Source 4, the 2024 hyperglycemic-crises consensus',
  'Umpierrez GE, Davis GM, ElSayed NA, et al. Diabetes Care 2024;47(8):1257-1275, doi 10.2337/dci24-0032 (also Diabetologia 2024;67:1455-1479). Number 4 is free since round 1 removed the 2020 CHNA source.')
e('597213',
  'href="https://www.msdmanuals.com/professional/endocrine-and-metabolic-disorders/diabetes-mellitus-and-disorders-of-carbohydrate-metabolism/diabetic-ketoacidosis-dka" rel="noopener" target="_blank">Diabetic Ketoacidosis (DKA)</a>',
  'href="https://www.msdmanuals.com/professional/endocrine-and-metabolic-disorders/diabetes-mellitus-and-hypoglycemia/acute-complications-of-diabetes-mellitus" rel="noopener" target="_blank">Acute Complications of Diabetes Mellitus</a>',
  'P3: MSD DKA link/title moved (anion-gap example, Source 2)',
  'The old URL now serves the chapter "Acute Complications of Diabetes Mellitus" (new path .../diabetes-mellitus-and-hypoglycemia/acute-complications-of-diabetes-mellitus loads, H1 confirmed), which states "Anion gap > 10 to 12 mEq/L".')
e('597213',
  'causes a marked decrease in blood pH (to as low as 6.9 from a normal value of 7.4).',
  'causes a marked decrease in blood pH (below 7.3, and in severe cases below 7.0, from a normal value of 7.4) (Source: Umpierrez GE, et al., %s, <em>Diabetes Care</em>, 2024).' % a(UMPIERREZ_URL, UMPIERREZ_T),
  'P3: "as low as 6.9" was a false floor; now below 7.3, severe below 7.0',
  'DKA can fall below 6.9. The 2024 consensus defines DKA as pH <7.3 and reserves bicarbonate for pH <7.0 (severe acidosis).')

# ---------------- 597203 (14.4) CO box + lecture table ----------------
e('597203',
  '6. California Senate Rules Committee, <a style="text-decoration:underline" href="https://www.leginfo.ca.gov/pub/09-10/bill/sen/sb_0151-0200/sb_183_cfa_20100414_131831_sen_floor.html" rel="noopener" target="_blank">SB 183 Floor Analysis (Carbon Monoxide Poisoning Prevention Act of 2010)</a>, 2010.',
  '6. California Legislature, %s (Carbon Monoxide Poisoning Prevention Act of 2010, SB 183).' % a('https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&amp;sectionNum=17926', 'Health and Safety Code &sect;17926'),
  'P3: SB 183 floor analysis replaced by the enacted statute',
  'The floor analysis contradicts itself on the deadlines. H&S Code 17926(a) (text read via FindLaw; official leginfo page refuses automated fetch): CO device required in each existing dwelling unit "having a fossil fuel burning heater or appliance, fireplace, or an attached garage"; single-family by July 1, 2011; all other units by January 1, 2013. The text sentence needs no change.')
e('597203',
  'Once sold as a diet drug; fatal overheating led to its ban.',
  'Once sold as a diet drug; fatal overheating led to its ban (Source: Grundlingh J, et al., %s, <em>J Med Toxicol</em>, 2011).' % a('https://pmc.ncbi.nlm.nih.gov/articles/PMC3550200/', '2,4-Dinitrophenol (DNP): A Weight Loss Agent with Significant Acute Toxicity and Risk of Death'),
  'P3: cite the DNP history (lecture table)',
  'Grundlingh 2011: DNP popular for weight loss from 1933; 1930s deaths were all in people taking it for weight loss; labelled "extremely dangerous and not fit for human consumption" in 1938; uncoupling releases energy as heat.')
e('597203',
  'and why, as Section 14.2 notes, working skeletal muscle can account for almost 90% of the body&rsquo;s oxygen use.',
  'and why, as Section 14.2 notes, working skeletal muscle uses most of the oxygen the body takes in.',
  'P3: remove the unsourced "almost 90%"',
  'No source found for 90% (checked Zurlo 1990 JCI and physiology searches). Rewritten to the qualitative statement; see 597201.')

# ---------------- 597201 (14.2) ----------------
e('597201',
  'resting skeletal muscles use about 30% of a resting adult&rsquo;s oxygen consumption, but when the same muscles are working strenuously, they account for almost 90% of the total oxygen consumption of the organism.',
  'resting skeletal muscles use only a modest share of a resting adult&rsquo;s oxygen, but when the same muscles are working strenuously, they use most of the oxygen the body takes in.',
  'P3: remove the unsourced 30% / 90% figures',
  'Could not verify either number (Zurlo et al. 1990 abstract gives no percentage; no source for 90%). Kept the point (respiratory control) without numbers. Author may restore numbers with a physiology source.')
e('597201',
  'was first proposed by Hans Krebs in 1937. (He was awarded the 1953 Nobel Prize in Physiology or Medicine.)',
  'was first proposed by Hans Krebs in 1937. (He was awarded the 1953 Nobel Prize in Physiology or Medicine; Source: %s.)' % a('https://www.nobelprize.org/prizes/medicine/1953/krebs/facts/', 'NobelPrize.org, Hans Krebs'),
  'P3: cite the Krebs Nobel Prize',
  'NobelPrize.org: Krebs, 1953 Physiology or Medicine, "for his discovery of the citric acid cycle"; cycle presented in 1937 (confirmed via search; nobelprize.org refuses automated fetch).')
e('597201',
  'resulting in Mitchell being awarded the 1978 Nobel Prize in Chemistry.',
  'resulting in Mitchell being awarded the 1978 Nobel Prize in Chemistry (Source: %s).' % a('https://www.nobelprize.org/prizes/chemistry/1978/mitchell/facts/', 'NobelPrize.org, Peter Mitchell'),
  'P3: cite the Mitchell Nobel Prize',
  'NobelPrize.org: Mitchell, 1978 Chemistry, for the chemiosmotic theory of biological energy transfer (confirmed via search).')

# ---------------- 597206 (14.7 Practice Problems) ----------------
e('597206',
  '2,4-Dinitrophenol (DNP) was sold as a diet pill in the 1930s and killed several users;',
  '2,4-Dinitrophenol (DNP) was sold as a diet pill in the 1930s and killed several users (Source: Grundlingh J, et al., %s, <em>J Med Toxicol</em>, 2011);' % a('https://pmc.ncbi.nlm.nih.gov/articles/PMC3550200/', '2,4-Dinitrophenol (DNP)'),
  'P3: cite the DNP history (practice problem)',
  'Same Grundlingh 2011 review: 1930s over-the-counter weight-loss use; deaths in that decade were all in people taking it for weight loss.')

# ---------------- 597211 / 597218 TAG share ----------------
e('597211',
  'About 98% of dietary lipids are <strong>triacylglycerols (TAG)</strong>,',
  'About 95%% of dietary lipids are <strong>triacylglycerols (TAG)</strong> (Source: Wang TY, et al., %s, <em>Eur J Clin Invest</em>, 2013),' % a('https://pmc.ncbi.nlm.nih.gov/articles/PMC3996833/', 'New insights into the molecular mechanism of intestinal fatty acid absorption'),
  'P3: TAG share 98% -> 95%, cited',
  'Wang et al. 2013 (PMC3996833): "In the Western diet, ~95% of dietary lipids are triacylglycerols".')
e('597218',
  'About 98% of dietary lipids are <strong>triacylglycerols (TAG)</strong>;',
  'About 95% of dietary lipids are <strong>triacylglycerols (TAG)</strong>;',
  'P3: Chapter Guide summary matches 15.1 (95%)',
  'Same source as 597211; summary text, so no second citation.')

# ---------------- 597209 BMI wording ----------------
e('597209',
  'BMI 18.5 kg/m<sup>2</sup> to 24.9 kg/m<sup>2</sup> is normal, less is underweight, more is overweight, and over 30 kg/m<sup>2</sup> is obese,',
  'BMI 18.5 kg/m<sup>2</sup> to 24.9 kg/m<sup>2</sup> is normal, less is underweight, 25.0 to 29.9 kg/m<sup>2</sup> is overweight, and 30 kg/m<sup>2</sup> or higher is obese,',
  'P3: BMI boundaries corrected (obesity is 30 or higher)',
  'NIDDK Overweight & Obesity Statistics (already cited later in this paragraph): overweight 25 to 29.9; obesity "30 or higher".')

# ---------------- 597192 car efficiency ----------------
e('597192',
  'automobiles are only about 20%&ndash;25% efficient in using the energy released by the combustion of gasoline.',
  'only about 12%%&ndash;30%% of the energy in gasoline is used to move a car down the road (Source: U.S. Department of Energy, %s).' % a('https://www.fueleconomy.gov/feg/atv.shtml', 'Where the Energy Goes: Gasoline Vehicles'),
  'P3: car efficiency figure sourced (12-30%)',
  'fueleconomy.gov (DOE/EPA): "Only about 12%-30% of the energy from the fuel you put in a conventional vehicle is used to move it down the road." The old 20-25% had no source; the sentence keeps its comparison with the 35% cell figure.')

# ---------------- 597191 lactose ----------------
e('597191',
  'In most of the world&rsquo;s adults, brush-border lactase declines after early childhood;',
  'In most of the world&rsquo;s adults (about 65%% of people), brush-border lactase declines after early childhood (Source: MedlinePlus Genetics, %s);' % a('https://medlineplus.gov/genetics/condition/lactose-intolerance/', 'Lactose intolerance'),
  'P3: cite lactase decline prevalence',
  'MedlinePlus Genetics: "Approximately 65 percent of the human population has a reduced ability to digest lactose after infancy."')

# ---------------- 597194 galactosemia screening ----------------
e('597194',
  '<strong>Galactosemia</strong> is on every U.S. state&rsquo;s newborn screening panel',
  '<strong>Galactosemia</strong> is on every U.S. state&rsquo;s newborn screening panel (Source: Pyhtila BM, et al., %s, <em>JIMD Reports</em>, 2014)' % a('https://pmc.ncbi.nlm.nih.gov/articles/PMC4413015/', 'Newborn Screening for Galactosemia in the United States'),
  'P3: cite universal U.S. galactosemia newborn screening',
  'Pyhtila et al. 2014 (PMC4413015): "By 2004, essentially all infants born in the USA were screened for galactosemia"; 2004 was when the last state added it.')

# ---------------- 597216 OTC ----------------
e('597216',
  '(ornithine transcarbamoylase deficiency is the most common)',
  '(ornithine transcarbamoylase deficiency is the most common; Source: Batshaw ML, et al., %s, <em>Mol Genet Metab</em>, 2014)' % a('https://pmc.ncbi.nlm.nih.gov/articles/PMC4178008/', 'A longitudinal study of urea cycle disorders'),
  'P3: cite OTC deficiency as the most common urea cycle disorder',
  'Batshaw et al. 2014 (Urea Cycle Disorders Consortium, PMC4178008): "The most common disorder is ornithine transcarbamylase deficiency, accounting for more than half of the participants."')

# ---------------- Licensing credits 597193 / 597202 ----------------
e('597193',
  '(Step list adapted from a public-domain resource at <a title="https://it.Wikipedia.org/wiki/Glicolisi" href="https://it.Wikipedia.org/wiki/Glicolisi" target="_blank" rel="external noopener nofollow" class="link-https">Wikipedia</a>.)',
  '(Step list adapted from the Italian Wikipedia article <a title="https://it.Wikipedia.org/wiki/Glicolisi" href="https://it.Wikipedia.org/wiki/Glicolisi" target="_blank" rel="external noopener nofollow" class="link-https">Glicolisi</a>, %s.)' % CCBYSA,
  'Licensing: Wikipedia credit corrected from "public-domain" to CC BY-SA 4.0',
  'The adapted item is article text (the step list), not a Commons image; the figures in this list are Daniel Kwasniewski\'s own SVGs. it.wikipedia footer: text under "Creative Commons Attribuzione-Condividi allo stesso modo" (CC BY-SA; Wikimedia projects use 4.0 since 2023).')
e('597202',
  'adapted from a public-domain source on the Russian-language <a',
  'adapted from the Russian-language Wikipedia article on the citric acid cycle (%s), <a' % CCBYSA,
  'Licensing: Wikipedia credit corrected from "public-domain" to CC BY-SA 4.0',
  'The adapted items are the reaction equations/text; the step figures are Daniel Kwasniewski\'s own SVGs. ru.wikipedia footer: text under Creative Commons "С указанием авторства - С сохранением условий" (CC BY-SA). The existing link (text "Wikipedia") is kept right after.')


def dry_run():
    pages, ok = {}, True
    for i, ed in enumerate(EDITS, 1):
        p = ed['page']
        if p not in pages:
            pages[p] = open(os.path.join(LIVE, p + '.html'), encoding='utf-8').read()
        n = pages[p].count(ed['old'])
        ok &= n == 1
        print('%2d %s %-14s %s' % (i, p, 'OK' if n == 1 else 'FAIL count=%d' % n, ed['note'][:72]))
        if n == 1:
            pages[p] = pages[p].replace(ed['old'], ed['new'])
    if ok:
        assert 'as low as 6.9' not in pages['597213'] and 'cmaj.ca/content' not in pages['597213']
        assert 'About 98%' not in pages['597211'] + pages['597218']
        assert 'public-domain resource at' not in pages['597193'] and 'public-domain source on' not in pages['597202']
        assert '90%' not in pages['597201'].split('resting skeletal muscles')[1][:300]
    return ok


if __name__ == '__main__':
    ok = dry_run()
    json.dump(EDITS, open(os.path.join(SCRATCH, 'fixp3_t5_ch13-15.json'), 'w'), ensure_ascii=False, indent=1)
    print('ALL OK (%d edits)' % len(EDITS) if ok else 'SOME EDITS FAILED')
    sys.exit(0 if ok else 1)
