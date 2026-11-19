"""fix_t4_ch10-12 (2026-11-18): P2 source fixes from srcaudit_t4_ch10-12.md (CHEM 3B textbook Ch 10-12),
plus free fixes of moved links. No P1 items in this group.
Reads  /Users/dan/Desktop/Study Games/textbook-git/pages/live/<id>.html (read-only).
Writes SCRATCH/fix_t4_ch10-12.json (edits) and SCRATCH/fix_t4_preview/<id>.html (edited pages) unless --dry.
Every `old` must occur exactly once (count=N where stated) in the page as it stands after earlier edits."""
import json, os, sys, hashlib
LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live/%s.html'
SCRATCH = '/private/tmp/claude-501/-Users-dan-Desktop-Study-Games/4c975f86-6f1d-43c3-b73a-277836ad0562/scratchpad'
pages, edits = {}, {}

def page(p):
    if p not in pages:
        t = open(LIVE % p, encoding='utf-8').read()
        pages[p] = [t, t]
    return pages[p][1]

def e(p, old, new, note, why, count=1):
    t = page(p)
    n = t.count(old)
    assert n == count, (p, note, n)
    pages[p][1] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': count, 'note': note, 'why': why})

def a(href, text):
    return '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>' % (href, text)

def src(pub, href, title):
    return '(Source: %s, %s)' % (pub, a(href, title))

# ---------------- 597048 Ch 10 opener: Rosa's Story ----------------
e('597048',
  'a urine albumin-to-creatinine ratio of 45 mg/g, where under 30 is normal; a result like this is repeated to confirm it.',
  'a urine albumin-to-creatinine ratio of 45 mg/g, where under 30 is normal; a result like this is repeated to confirm it '
  + src('National Kidney Foundation', 'https://www.kidney.org/kidney-topics/urine-albumin-creatinine-ratio-uacr', 'Urine albumin-creatinine ratio (uACR)') + '.',
  'B1 P2: Rosa Part 10, uACR threshold and repeat test',
  'Clinical threshold had no source. NKF: a uACR under 30 mg/g is "normal" or "at goal"; the test "often needs to be repeated one or more times to confirm the results."')

# ---------------- 597154 10.1 protein RDA ----------------
e('597154',
  'protein is not stored, so it must be eaten every day (about 0.8 g per kilogram of body weight for adults).',
  'protein is not stored, so it must be eaten every day: about 0.8 g per kilogram of body weight for adults '
  + src('Wolfe et al., <em>Advances in Nutrition</em>', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5347101/', 'Optimizing Protein Intake in Adults, 2017') + '.',
  'B2 P2: 10.1 Lecture Connection, protein 0.8 g/kg/day',
  'Nutrition reference value had no source. Wolfe RR et al., Adv Nutr 2017;8:266: "the EAR and the RDA for protein are 0.66 and 0.80 g/kg/d." (The National Academies DRI chapter could not be read by the fetcher; this peer-reviewed review restates the DRI value.)')

# ---------------- 597159 10.6 aspartame + albumin ----------------
e('597159',
  'For example, aspartame, about 180 times sweeter than sucrose and used as a sugar substitute, is a methyl ester of a dipeptide Asp-Phe, shown below.',
  'For example, aspartame, a sugar substitute about 200 times sweeter than sucrose '
  + src('MedlinePlus', 'https://medlineplus.gov/ency/article/007492.htm', 'Sweeteners &ndash; sugar substitutes')
  + ', is a methyl ester of a dipeptide Asp-Phe, shown below.',
  'C1/B5 P2: 10.6 aspartame "about 180 times" -> "about 200 times"',
  'Number was the low end of an old range and unsourced. MedlinePlus: aspartame is "200 times sweeter than sucrose" (FDA also says about 200 times, but its aspartame page now returns Page Not Found, so MedlinePlus is cited).')
e('597159',
  '(normal about 3.5&ndash;5.0 g/dL)',
  '(normal about 3.4&ndash;5.4 g/dL; '
  + 'Source: MedlinePlus, ' + a('https://medlineplus.gov/ency/article/003480.htm', 'Albumin blood test') + ')',
  'B4 P2: 10.6 Clinical Connection: Nursing, serum albumin normal range',
  'Clinical reference range had no source. MedlinePlus gives "3.4 to 5.4 g/dL (34 to 54 g/L)"; the range is changed to match the cited source.')

# ---------------- 597165 10.12 Practice Problems (same range) ----------------
e('597165',
  'a serum albumin of 2.1 g/dL (normal about 3.5&ndash;5.0 g/dL)',
  'a serum albumin of 2.1 g/dL (normal about 3.4&ndash;5.4 g/dL)',
  'B4 P2: Problem 10.63, same albumin range',
  'Keeps the practice problem consistent with 10.6 (MedlinePlus 3.4-5.4 g/dL). Cited once on 10.6; not re-cited here. 2.1 g/dL is still low under either range, so the answer does not change.')

# ---------------- 597160 10.7 collagen ----------------
e('597160',
  'It is the most abundant protein of vertebrates making up 30% to 35% of their proteins by weight.',
  'It is the most abundant protein in mammals, making up about 30% of their protein by mass '
  + src('Ricard-Blum, <em>Cold Spring Harbor Perspectives in Biology</em>', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3003457/', 'The Collagen Family, 2011') + '.',
  'B7 P2: 10.7 Triple helix, collagen share of protein',
  'Statistic had no source; 30-35% not found in a reliable source. Ricard-Blum 2011: "Collagens are the most abundant proteins in mammals (~30% of total protein mass)." Wording follows the source (mammals, about 30%).')

# ---------------- 597162 10.9 Lecture Connection: CO ----------------
e('597162',
  'Carbon monoxide is poisonous because it binds that same Fe<sup>2+</sup> about 200 times more tightly than O<sub>2</sub> does,',
  'Carbon monoxide is poisonous because it binds that same Fe<sup>2+</sup> more than 200 times more tightly than O<sub>2</sub> does '
  + src('ATSDR', 'https://www.atsdr.cdc.gov/ToxProfiles/tp201-c2.pdf', 'Toxicological Profile for Carbon Monoxide, ch. 2') + ',',
  'B8 P2: 10.9 Lecture Connection, CO affinity for hemoglobin',
  'Quantitative clinical claim had no source. ATSDR Tox Profile ch. 2: "The binding affinity of carbon monoxide for hemoglobin is over 200 times greater than" that of oxygen. "about 200" -> "more than 200" to match. The "about 200 times" in the Think-about-it answer and 10.12 answer is left as is (not wrong).')

# ---------------- 597162 Valley Connection: nitrate (renumbered source list) ----------------
e('597162',
  'In the eastern San Joaquin Valley, about one in three domestic wells has nitrate above the public health limit,<sup>1</sup>',
  'When UC Davis tested 200 domestic wells in Stanislaus, Merced, Tulare and Kings counties, 42&ndash;46% had nitrate above the drinking-water limit,<sup>1</sup>',
  'C3/A7 P2: nitrate box, "about one in three domestic wells" -> UC Davis sample result',
  'The 1-in-3 figure came from a 2010 news reprint (Truthout) that names no study. Lockhart, King and Harter (UC Davis, 2013), already cited in this box: "Forty six percent of well water samples in Tul/Kings and 42% of well water samples in Stan/Mer exceeded the MCL for nitrate (10 mg/L NO3-N)." Two hundred wells were sampled. Source 1 is replaced in place by that report (see the source-list edit).')
e('597162',
  'comes from crop fertilizer and dairy manure that soaks down into the groundwater.<sup>3</sup>',
  'comes from crop fertilizer and dairy manure that soaks down into the groundwater.<sup>1</sup>',
  'C3 P2: nitrate box, manure/fertilizer sentence now cites new source 1 (same UC Davis report)',
  'The UC Davis report moves to slot 1, so its old slot 3 is freed for the replacement of the misattributed "CDC" source; list renumbered once.')
e('597162',
  'cannot carry oxygen.<sup>4</sup>',
  'cannot carry oxygen.<sup>3</sup>',
  'C4 P2: nitrate box, renumber 4 -> 3 (ATSDR replaces the misattributed source)',
  'ATSDR CSEM: nitrites oxidize hemoglobin to methemoglobin, which cannot carry oxygen effectively.')
e('597162',
  'back to Fe<sup>2+</sup>.<sup>4,5</sup> The federal limit of 10 mg/L nitrate-nitrogen was set to protect infants. Boiling does not help; it concentrates the nitrate.<sup>6</sup>',
  'back to Fe<sup>2+</sup>.<sup>3,4</sup> The federal limit of 10 mg/L nitrate-nitrogen was set to protect infants.<sup>4</sup> Boiling does not help; it concentrates the nitrate.<sup>5</sup>',
  'C4 + B9 P2: nitrate box, renumber 4,5 -> 3,4 and 6 -> 5; cite the 10 mg/L sentence',
  'ATSDR CSEM: "Fetal hemoglobin (HbF) is more readily oxidized to MetHb by nitrites than is adult hemoglobin"; the reducing enzyme "has only about half the activity it has in adults." UW PEHSU factsheet (new 4): "The 10 mg/L standard was set to protect infants from nitrates." Iowa HHS (new 5): boiling "can concentrate them."')
e('597162',
  '<strong>Sources:</strong> 1. J. Scott, California Watch, <a style="text-decoration:underline" href="https://www.truthout.org/articles/nitrate-contamination-spreading-in-california-communities" rel="noopener" target="_blank">&ldquo;Nitrate Contamination Spreading in California Communities&rdquo;</a>, May 2010 (reprint at Truthout). 2. <em>Scientific American</em>, <a style="text-decoration:underline" href="https://www.scientificamerican.com/article/pollution-poverty-people-color-dont-drink-water/" rel="noopener" target="_blank">&ldquo;Pollution, Poverty and People of Color: Don&rsquo;t Drink the Water&rdquo;</a>. 3. Lockhart, King and Harter, UC Davis, <a style="text-decoration:underline" href="https://ccfruitandnuts.ucanr.edu/sites/default/files/2014-12/202721.pdf" rel="noopener" target="_blank">nitrate in San Joaquin Valley domestic wells</a>. 4. CDC, <a style="text-decoration:underline" href="https://stacks.cdc.gov/view/cdc/222399/cdc_222399_DS1.pdf" rel="noopener" target="_blank">Nitrate and nitrite in drinking water and methemoglobinemia</a>. 5. University of Washington DEOHS,',
  '<strong>Sources:</strong> 1. Lockhart, King and Harter, UC Davis, ' + a('https://ccfruitandnuts.ucanr.edu/sites/default/files/2014-12/202721.pdf', 'Identifying Sources of Groundwater Nitrate Contamination in the San Joaquin Valley') + ', 2013. 2. <em>Scientific American</em>, <a style="text-decoration:underline" href="https://www.scientificamerican.com/article/pollution-poverty-people-color-dont-drink-water/" rel="noopener" target="_blank">&ldquo;Pollution, Poverty and People of Color: Don&rsquo;t Drink the Water&rdquo;</a>. 3. Agency for Toxic Substances and Disease Registry (CDC), ' + a('https://archive.cdc.gov/www_atsdr_cdc_gov/csem/nitrate-nitrite/who_risk.html', 'Nitrate/Nitrite Toxicity: Who Is at Most Risk') + '. 4. University of Washington DEOHS,',
  'C3/C4 P2: nitrate box source list: drop Truthout reprint, UC Davis report to slot 1, ATSDR replaces the misattributed "CDC" PDF, renumber 5,6 -> 4,5',
  'Truthout reprint was a weak source and its claim is reworded. The "CDC" PDF on stacks.cdc.gov is really Chapter 33 of the AAP book Pediatric Environmental Health (c 2012 AAP), not a CDC document; the ATSDR (CDC) case study says the same things (HbF oxidized more readily; reductase about half adult activity). Renumbering was unavoidable to keep one entry per source.')
e('597162',
  'fact sheet for health professionals</a>, 2014. 6. Iowa HHS,',
  'fact sheet for health professionals</a>, 2014. 5. Iowa HHS,',
  'C4 P2: nitrate box, renumber 6 -> 5', 'Follows the renumbering above.')

# ---------------- 597169 11.4 penicillin allergy ----------------
e('597169',
  'However, most people whose charts say &ldquo;penicillin allergy&rdquo; turn out not to be allergic when they are tested, and an allergy evaluation can let them receive the most effective drug.',
  'However, about 10% of U.S. patients report a penicillin allergy, and fewer than 1% of them are truly allergic when evaluated '
  + src('CDC', 'https://www.cdc.gov/antibiotic-use/hcp/clinical-signs/index.html', 'Clinical Features of Penicillin Allergy')
  + '. An allergy evaluation can let them receive the most effective drug.',
  'B10 P2: 11.4 To Your Health: Penicillin, allergy labels',
  'Health statistic had no source. CDC: "10% of U.S. patients reported having a penicillin allergy"; when evaluated, "less than 1% of those patients were truly allergic." Rewritten to the source numbers.')

# ---------------- 597180 12.7 PKU incidence ----------------
e('597180',
  'PKU affects about 1 in 12,000 newborns in North America.',
  'In the United States, PKU affects about 1 in 25,000 newborns '
  + src('MedlinePlus Genetics', 'https://medlineplus.gov/genetics/condition/phenylketonuria/', 'Phenylketonuria') + '.',
  'C2/B15 P2: 12.7 PKU incidence 1 in 12,000 (North America) -> 1 in 25,000 (U.S.)',
  'Older, unsourced figure. MedlinePlus Genetics: "In the United States, PKU occurs in 1 in 25,000 newborns."')

# ---------------- 597181 12.8 + 597184 12.10 HPV ----------------
e('597181',
  'type 16 is a DNA virus whose proteins disable two of the cell\'s growth-control proteins, and it now causes most <strong>oropharyngeal cancers</strong> (base of tongue, tonsils);',
  'type 16 is a DNA virus whose proteins disable two of the cell\'s growth-control proteins, and HPV is now linked to about 60% to 70% of <strong>oropharyngeal cancers</strong> (base of tongue, tonsils) '
  + src('CDC', 'https://www.cdc.gov/cancer/hpv/basic-information.html', 'Basic Information about HPV and Cancer') + ';',
  'B16 P2: 12.8 Clinical Connection: Dental Hygiene, HPV and oropharyngeal cancer',
  'Health statistic had no source. CDC: "about 60% to 70% of cancers of the oropharynx may be linked to HPV." The CDC page does not attribute this to type 16 alone, so the share is given for HPV.')
e('597184',
  'HPV-16 (a DNA virus) causes most oropharyngeal cancers, so screen at every recall;',
  'HPV (type 16 above all, a DNA virus) is linked to about 60% to 70% of oropharyngeal cancers, so screen at every recall;',
  'B16 P2: 12.10 Chapter Guide, Health Career Connection, same HPV claim',
  'Keeps the guide consistent with 12.8 (CDC: about 60-70% of oropharyngeal cancers may be linked to HPV). Cited once on 12.8; not re-cited here.')

# ---------------- free moved-link fixes (P3, URL only) ----------------
e('597158', 'href="http://www.pdb.org"', 'href="https://www.rcsb.org/structure/1I3D"',
  'Link P3: 10.5 hemoglobin Bart\'s image source, pdb.org (now redirects to wwpdb.org) -> RCSB entry 1I3D', 'Moved link; link text www.pdb.org left as is.')
OLDJ = 'https://bio.libretexts.org/TextMaps/Biochemistry/Book%3A_Biochemistry_Online_(Jakubowski)/06%3A_TRANSPORT_AND_KINETICS/6C%3A_Enzyme_Inhibition/C4._Noncompetitive_and_Mixed_Inhibition'
e('597169', OLDJ, 'https://bio.libretexts.org/Bookshelves/Biochemistry/Fundamentals_of_Biochemistry_(Jakubowski_and_Flatt)/01%3A_Unit_I-_Structure_and_Catalysis/06%3A_Enzyme_Activity',
  'Link P3: 11.4 "noncompetitive inhibitor" link (title + href)', 'Old page now redirects into LibreTexts "Under_Construction/Purgatory"; new target is the same author\'s current book chapter (Jakubowski and Flatt, Fundamentals of Biochemistry, Ch. 6, which includes 6.4 Enzyme Inhibition).', count=2)
e('597170', 'href="https://publications.ca.uky.edu/files/FCS3644.pdf"', 'href="https://publications.mgcafe.uky.edu/files/FCS3644.pdf"',
  'Link P3: 11.5 vitamin E source 4, UKY PDF moved', '301 redirect to publications.mgcafe.uky.edu; same document (FCS3-644, issued 08-2024).')
e('597170', 'href="https://www.almonds.it/sites/default/files/2023-04/2022_Almanac.pdf"', 'href="https://it.almonds.org/sites/default/files/2023-04/2022_Almanac.pdf"',
  'Link P3: 11.5 almond source 2, Almanac PDF moved', '301 redirect from almonds.it to it.almonds.org; same 2022 Almond Almanac.')

# ---------------- checks + output ----------------
assert 'truthout' not in page('597162') and 'stacks.cdc.gov' not in page('597162')
assert page('597162').count('<sup>6</sup>') == 0
for p, (t0, t1) in pages.items():
    assert t1.count('<a ') == t1.count('</a>'), p
if '--dry' not in sys.argv:
    h = lambda x: hashlib.sha256(x.encode()).hexdigest()
    os.makedirs(SCRATCH + '/fix_t4_preview', exist_ok=True)
    for p, (t0, t1) in pages.items():
        open(SCRATCH + '/fix_t4_preview/%s.html' % p, 'w', encoding='utf-8').write(t1)
    json.dump({'edits': edits, 'sha': {p: {'before': h(t0), 'after': h(t1)} for p, (t0, t1) in pages.items()}},
              open(SCRATCH + '/fix_t4_ch10-12.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages:', {p: len(v) for p, v in edits.items()})
