"""fixp3_t4_ch10-12 (2026-11-18, round 2): P3 polish from srcaudit_t4_ch10-12.md (CHEM 3B textbook Ch 10-12).
Written against pages/live after batch AP (round-1 fixes live).
Module level only defines helpers (if the batch builder has not already supplied e()) and calls e().
File output and self-checks run only under __main__:  python3 fixp3_t4_ch10-12.py [--dry]"""

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live/%s.html'

if 'e' not in globals():
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


def _a(href, text):
    return '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>' % (href, text)


def _src(pub, href, title):
    return '(Source: %s, %s)' % (pub, _a(href, title))


# ===== 597162 10.9 nitrate box: primary report for 254,000 (A8) =====
e('597162',
  '2. <em>Scientific American</em>, <a style="text-decoration:underline" href="https://www.scientificamerican.com/article/pollution-poverty-people-color-dont-drink-water/" rel="noopener" target="_blank">&ldquo;Pollution, Poverty and People of Color: Don&rsquo;t Drink the Water&rdquo;</a>.',
  '2. Harter, Lund et al., UC Davis Center for Watershed Sciences, '
  + _a('https://aesm.assembly.ca.gov/sites/aesm.assembly.ca.gov/files/SBX2%201%20Main%20Report%20FINAL.pdf', 'Addressing Nitrate in California&rsquo;s Drinking Water (report to the Legislature)') + ', 2012.',
  'A8 P3: nitrate box source 2, Scientific American news story -> the UC Davis report itself',
  'The 254,000 figure comes from this report; the magazine only quoted it. Main report (copy hosted by the California Assembly): "Lake Basin and Salinas Valley, roughly 254,000 people" are at risk. Replaced in place; numbering unchanged.')

# ===== 597163 10.10 Title 8 wording (A15/C5) =====
e('597163',
  'and reminding workers to drink water. Farmworkers also get a 10-minute cool-down rest every two hours. New workers in high heat must be watched closely for their first 14 days,',
  'and reminding workers to drink water. At 95&nbsp;&deg;F or above, farmworkers also get a 10-minute cool-down rest every two hours. Workers newly assigned to a high-heat area must be watched closely for their first 14 days,',
  'C5 P3: 10.10 Valley Connection, Title 8 heat rule wording',
  '8 CCR 3395(e)(6): the 10-minute rest every two hours applies to agricultural employees "When temperatures reach 95 degrees or above"; (g)(2): employees "newly assigned to a high heat area" are closely observed for the first 14 days. Existing source 3 covers both.')

# ===== 597169 11.4 chlorpyrifos box: drop Feedstuffs, CalEPA becomes 1 (A17) =====
e('597169',
  'all possession and use ended after December 31, 2020.<sup>5</sup>',
  'all possession and use ended after December 31, 2020.<sup>1</sup>',
  'A17 P3: chlorpyrifos box, ban sentence cites new source 1 (CalEPA)', 'Follows the source-list change below.')
e('597169',
  '1. <a style="text-decoration:underline" href="https://www.feedstuffs.com/agribusiness-news/corteva-ends-production-of-chlorpyrifos" rel="noopener" target="_blank">&ldquo;Corteva ends production of chlorpyrifos,&rdquo; Feedstuffs, 2020</a>.',
  '1. CalEPA, ' + _a('https://calepa.ca.gov/2019/10/09/press-release-agreement-reached-to-end-sale-of-chlorpyrifos-in-ca-by-feb-2020/', '&ldquo;Agreement Reached to End Sale of Chlorpyrifos in California by February 2020,&rdquo; October 9, 2019') + '.',
  'A17 P3: chlorpyrifos box source 1, Feedstuffs (trade press, blocks access) -> CalEPA press release',
  'CalEPA release lists the crops ("alfalfa, almonds, citrus, cotton, grapes, and walnuts") and the dates (sales end Feb 6, 2020; possession/use end Dec 31, 2020). It was already source 5, so 5 is removed below and ^5 becomes ^1; sources 2-4 keep their numbers. Trailing slash added (the old URL 301-redirects).')
e('597169',
  ' 5. CalEPA, <a style="text-decoration:underline" href="https://calepa.ca.gov/2019/10/09/press-release-agreement-reached-to-end-sale-of-chlorpyrifos-in-ca-by-feb-2020" rel="noopener" target="_blank">&ldquo;Agreement Reached to End Sale of Chlorpyrifos in California by February 2020,&rdquo; October 9, 2019</a>.',
  '',
  'A17 P3: chlorpyrifos box, remove the duplicate CalEPA entry (old 5)', 'Now source 1.')

# ===== 597169 11.4 To Your Health: Penicillin history (B11) =====
e('597169',
  'Penicillin was discovered by Alexander Fleming in 1928, in a mold growing on a bacterial culture plate. It became the first antibiotic produced in large amounts, in the 1940s.',
  'Penicillin was discovered by Alexander Fleming in 1928, in a mold growing on a bacterial culture plate. It became the first antibiotic produced in large amounts, in the 1940s '
  + _src('Gaynes, <em>Emerging Infectious Diseases</em>', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5403050/', 'The Discovery of Penicillin, 2017') + '.',
  'B11 P3: 11.4 penicillin history, cited',
  'Named discovery and date. Gaynes 2017 (CDC journal EID): "In 1928, a chance event in Alexander Fleming\'s London laboratory changed the course of medicine"; by 1943 wartime production met the Allied forces\' demand.')

# ===== 597169 Molecule in the Clinic: amoxicillin (B12) =====
e('597169',
  'Amoxicillin, a penicillin, is the most common antibiotic for dental infections.',
  'Amoxicillin, a penicillin, is a first-choice antibiotic for a dental infection that needs one '
  + _src('American Dental Association and CDC', 'https://www.cdc.gov/antibiotic-use/pdfs/ada-treatment-guidelines-508.pdf', 'Antibiotics for dental pain and swelling') + '.',
  'B12 P3: 11.4 amoxicillin "most common" -> "a first-choice", cited',
  '"Most common" had no source. ADA chairside guide (hosted by CDC): "ADA Antibiotic Recommendations: Amoxicillin (500mg, 3 times per day, 3-7 days) [or] Penicillin V potassium". Wording follows what the guideline says.')

# ===== 597169 Lecture Connection: lead sources (B13) =====
e('597169',
  'In California, lead poisoning has also been traced to some imported candies, spices, glazed pottery, and traditional remedies such as greta and azarc&oacute;n.',
  'In California, lead poisoning has also been traced to some imported candies, spices, glazed pottery, and traditional remedies such as greta and azarc&oacute;n '
  + '(Source: CDPH, ' + _a('https://www.cdph.ca.gov/Programs/CCDPHP/DEODC/CLPPB/Pages/prov_overview.aspx', 'Lead Poisoning Overview') + ' and '
  + _a('https://www.cdph.ca.gov/Programs/CCDPHP/DEODC/CLPPB/CDPH%20Document%20Library/RemediesBrochureEnSp.pdf', 'Lead in Traditional Remedies') + ').',
  'B13 P3: 11.4 Lecture Connection, California lead sources, cited',
  'Regional health claim. CDPH overview lists "Foods such as chapulines, candy, spices", "Imported or handmade pottery and tableware with leaded glaze", "Imported home remedies". CDPH brochure names "Greta and Azarcon" (up to 90% lead).')

# ===== 597169 moved link: none left (done in round 1) =====

# ===== 597170 11.5 almond box: 80% claim (A23) =====
e('597170',
  'California grows about 80% of the world&rsquo;s almonds,<sup>1</sup> and most of the orchards are in San Joaquin Valley counties from Stanislaus and Merced through Madera, Fresno and Kern.<sup>2</sup> A one-ounce handful of almonds supplies about 7.3 mg of vitamin E (as &alpha;-tocopherol), roughly half of the 15 mg an adult needs each day.<sup>3</sup>',
  'California grows nearly 80% of the world&rsquo;s almonds, and most of the orchards are in San Joaquin Valley counties from Stanislaus and Merced through Madera, Fresno and Kern.<sup>1</sup> A one-ounce handful of almonds supplies about 7.3 mg of vitamin E (as &alpha;-tocopherol), roughly half of the 15 mg an adult needs each day.<sup>2</sup>',
  'A23 P3: almond box, "about 80%" -> "nearly 80%", both statistics cite the Almanac (new 1); renumber 3 -> 2',
  'Old source 1 (UC Davis FNRIC "breeding projects" page) blocks access and is not a production-statistics page. Almond Board 2022 Almanac: "CALIFORNIA GROWS NEARLY 80% OF THE WORLD\'S ALMONDS" (U.S. 79% of crop year 2021/22) and p. 35 production by county. Industry figures for the industry\'s own production are acceptable when labeled.')
e('597170',
  '<strong>Sources:</strong> 1. UC Davis Fruit &amp; Nut Research and Information Center, <a style="text-decoration:underline" href="https://fruitsandnuts.ucdavis.edu/es/node/246" rel="noopener" target="_blank">Almond Board of California breeding projects</a>. 2. Almond Board of California, <a style="text-decoration:underline" href="https://it.almonds.org/sites/default/files/2023-04/2022_Almanac.pdf" rel="noopener" target="_blank">2022 Almond Almanac (production by county)</a>. 3. Almond Board of California,',
  '<strong>Sources:</strong> 1. Almond Board of California, <a style="text-decoration:underline" href="https://it.almonds.org/sites/default/files/2023-04/2022_Almanac.pdf" rel="noopener" target="_blank">2022 Almond Almanac (world share and production by county)</a>. 2. Almond Board of California,',
  'A23 P3: almond box source list, drop UC Davis page, Almanac -> 1, almonds.org -> 2', 'Follows the sentence edit above.')
e('597170',
  ', citing the NIH recommended intake of 15 mg/day. 4. NIH Office of Dietary Supplements,',
  ', citing the NIH recommended intake of 15 mg/day. 3. NIH Office of Dietary Supplements,',
  'A23 P3: almond box, renumber 4 -> 3', 'Follows the renumbering.')

e('597170',
  'asked about vitamin E supplements.<sup>4</sup>',
  'asked about vitamin E supplements.<sup>3</sup>',
  'A23 P3: almond box, in-text ^4 -> ^3 (NIH ODS / UKY, renumbered)', 'Follows the renumbering.')

# ===== 597182 12.9 Valley fever: chronic 5-10% (A43/C7) + PCR glossary slug (A42) =====
e('597182',
  'may show lasting nodules or cavities in the lungs.<sup>5</sup>',
  'may show lasting nodules or cavities in the lungs.<sup>2,5</sup>',
  'C7 P3: Valley fever Careers, add CDC (^2) for "roughly 5 to 10%"',
  'CDC clinical overview: about 5 to 10% "fail to recover and develop complications or chronic pulmonary disease." The RadioGraphics review (^5) supports the imaging findings but gives about 5%.')
e('597182',
  'href="https://www.genome.gov/genetics-glossary/Polymerase-Chain-Reaction" rel="noopener"',
  'href="https://www.genome.gov/genetics-glossary/Polymerase-Chain-Reaction-PCR" rel="noopener"',
  'A42 P3 link: Valley fever source 4, genome.gov glossary slug', 'Old slug 301-redirects to Polymerase-Chain-Reaction-PCR.')

# ===== 597182 12.9 Human genome (B21) and CRISPR (B20) =====
e('597182',
  'was launched in October 1990 and completed in April 2003; the last gaps in the sequence were filled in 2022.',
  'was launched in October 1990 and completed in April 2003; the last gaps in the sequence were filled in 2022 '
  + '(Source: NHGRI, ' + _a('https://www.genome.gov/human-genome-project/Timeline-of-Events', 'Human Genome Project Timeline') + ' and '
  + _a('https://www.genome.gov/human-genome-project/Completion-FAQ', 'Completion FAQ') + ').',
  'B21 P3: 12.9 Human Genome Project dates, cited',
  'NHGRI timeline: "On Oct. 1, 1990, the project officially begins"; completion announced April 14, 2003. NHGRI Completion FAQ: the Telomere-to-Telomere consortium filled the remaining gaps on March 31, 2022.')
e('597182',
  'In 2023 the FDA approved the first CRISPR-based therapy, Casgevy, for sickle cell disease: a patient&rsquo;s own blood stem cells are edited so they make fetal hemoglobin again, then returned to the patient.',
  'In 2023 the FDA approved the first CRISPR-based therapy, Casgevy, for sickle cell disease: a patient&rsquo;s own blood stem cells are edited so they make fetal hemoglobin again, then returned to the patient '
  + _src('FDA', 'https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapies-treat-patients-sickle-cell-disease', 'press release, December 8, 2023') + '.',
  'B20 P3: 12.9 Casgevy, cited',
  'FDA, Dec 8, 2023: "Casgevy is the first FDA-approved therapy utilizing CRISPR/Cas9"; patients\' own edited blood stem cells raise fetal hemoglobin.')

# ===== 597181 12.8 AZT (B18), U=U (B19), HBV on surfaces (B17) =====
e('597181',
  'became the first drug approved for the treatment of <span class="acronym-ignore">AIDS</span>.',
  'became the first drug approved for the treatment of <span class="acronym-ignore">AIDS</span> '
  + _src('FDA', 'https://www.fda.gov/about-fda/fda-history-exhibits/history-fdas-role-preventing-spread-hivaids', 'History of FDA&rsquo;s Role in Preventing the Spread of HIV/AIDS') + '.',
  'B18 P3: 12.8 AZT 1987, cited',
  'FDA history exhibit: "In March of 1987, FDA approved zidovudine (AZT) as the first antiretroviral drug for the treatment of AIDS."')
e('597181',
  'cannot pass HIV to sexual partners (<strong>U=U</strong>, &ldquo;undetectable = untransmittable&rdquo;).',
  'cannot pass HIV to sexual partners (<strong>U=U</strong>, &ldquo;undetectable = untransmittable&rdquo;) '
  + _src('CDC', 'https://www.cdc.gov/hivpartners/php/hiv-treatment/index.html', 'HIV Treatment as Prevention') + '.',
  'B19 P3: 12.8 U=U, cited',
  'CDC: a person who stays virally suppressed or undetectable "will not transmit HIV to their sex partners."')
e('597181',
  '<strong>Hepatitis B</strong> is a bloodborne DNA virus that survives for days on surfaces,',
  '<strong>Hepatitis B</strong> is a bloodborne DNA virus that stays infectious on surfaces for at least 7 days '
  + _src('CDC', 'https://www.cdc.gov/hepatitis-b/hcp/clinical-overview/index.html', 'Clinical Overview of Hepatitis B') + ',',
  'B17 P3: 12.8 Dental Hygiene, HBV survival on surfaces, made specific and cited',
  'CDC clinical overview: HBV "Is infectious for at least 7 days on surfaces."')

# ===== 597183 12.5 hepatitis B vaccine wording (C6) =====
e('597183',
  'while the vaccine for hepatitis B, a DNA virus, has not changed since the 1980s.',
  'while the hepatitis B vaccine, against a DNA virus, has been made from the same viral surface protein since the 1980s '
  + _src('CDC', 'https://www.cdc.gov/pinkbook/hcp/table-of-contents/chapter-10-hepatitis-b.html', 'Pink Book, Hepatitis B') + '.',
  'C6 P3: 12.5 Example 3, "has not changed since the 1980s" -> same surface protein since the 1980s',
  'Newer HBV vaccines exist (Heplisav-B, licensed 2017 with a new adjuvant), so "has not changed" is not quite true; the antigen is the same. CDC Pink Book: recombinant HepB vaccine is made by putting "the gene for HBsAg into yeast"; the first, Recombivax HB, "was licensed in the United States in 1986"; Heplisav-B is "a third recombinant vaccine". The solution text (surface protein tolerates few changes) still fits.')

# ===== 597172 11.7 lactase (B14) =====
e('597172',
  'This decline after childhood is the most common pattern worldwide,',
  'This decline after childhood is the most common pattern worldwide, about two-thirds of all people '
  + _src('MedlinePlus Genetics', 'https://medlineplus.gov/genetics/condition/lactose-intolerance/', 'Lactose intolerance') + ',',
  'B14 P3: 11.7 lactase non-persistence, quantified and cited',
  'MedlinePlus Genetics: "Approximately 65 percent of the human population has a reduced ability to digest lactose after infancy"; about 5% of people of Northern European descent.')

# ===== 597167 11.2 Fischer 1894 / Koshland 1958 (B22) =====
e('597167',
  'In the <strong>lock-and-key model</strong> (Emil Fischer, 1894)',
  'In the <strong>lock-and-key model</strong> (Emil Fischer, 1894; Source: Koshland, '
  + _a('https://doi.org/10.1002/anie.199423751', '<em>Angewandte Chemie</em>, 1995') + ')',
  'B22 P3: 11.2 Lecture Connection, Fischer 1894 / Koshland 1958, cited once',
  'Named discoveries with dates. Koshland DE Jr., "The Key-Lock Theory and the Induced Fit Theory," Angew Chem Int Ed Engl 1995;33:2375 (abstract via search): induced fit "extends the lock-and-key principle that Emil Fischer proposed exactly 100 years ago"; the induced-fit theory is Koshland\'s 1958 proposal. The DOI resolves; Wiley blocks the full text to the fetcher. The sentence is on 597167 (11.2); the audit listed it under 597166.')

# ===== 597178 12.4 genome.gov figure-credit links: new slugs (A35) =====
e('597178', 'https://www.genome.gov/genetics-glossary/RNA-Ribonucleic-Acid', 'https://www.genome.gov/genetics-glossary/Ribonucleic-Acid-RNA',
  'A35 P3 link: 12.4 figure credit (title + href), RNA glossary slug', 'Old slug 301-redirects to Ribonucleic-Acid-RNA.', count=2)
e('597178', 'https://www.genome.gov/genetics-glossary/Transfer-RNA"', 'https://www.genome.gov/genetics-glossary/Transfer-RNA-tRNA"',
  'A35 P3 link: 12.4 figure credit (title + href), tRNA glossary slug', 'Old slug 301-redirects to Transfer-RNA-tRNA.', count=2)


if __name__ == '__main__':
    import json, os, sys, hashlib
    SCRATCH = '/private/tmp/claude-501/-Users-dan-Desktop-Study-Games/4c975f86-6f1d-43c3-b73a-277836ad0562/scratchpad'
    t = pages['597169'][1]
    assert 'feedstuffs' not in t and t.count('calepa.ca.gov') == 1 and '<sup>5</sup>' not in t
    t = pages['597170'][1]
    assert 'fruitsandnuts.ucdavis.edu' not in t and ' 4. NIH' not in t
    for p, (t0, t1) in pages.items():
        assert t1.count('<a ') == t1.count('</a>'), p
    if '--dry' not in sys.argv:
        h = lambda x: hashlib.sha256(x.encode()).hexdigest()
        os.makedirs(SCRATCH + '/fixp3_t4_preview', exist_ok=True)
        for p, (t0, t1) in pages.items():
            open(SCRATCH + '/fixp3_t4_preview/%s.html' % p, 'w', encoding='utf-8').write(t1)
        json.dump({'edits': edits, 'sha': {p: {'before': h(t0), 'after': h(t1)} for p, (t0, t1) in pages.items()}},
                  open(SCRATCH + '/fixp3_t4_ch10-12.json', 'w'), ensure_ascii=False, indent=1)
    print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages:', {p: len(v) for p, v in edits.items()})
