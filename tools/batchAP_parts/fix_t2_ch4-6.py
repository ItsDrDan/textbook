"""Draft P1 + P2 fixes (plus free dead/moved-link fixes) from srcaudit_t2_ch4-6.md, group t2_ch4-6 (Chapters 4-6).
Each e(pageid, old, new, note, why): `old` must occur exactly once in the current
/Users/dan/Desktop/Study Games/textbook-git/pages/live/<pageid>.html (after earlier edits on the same page).
Running this file only TESTS the edits in memory (no repo file is written) and dumps
SCRATCH/fix_t2_ch4-6.json for the coordinator.
"""
import json, os, sys

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live'
SCRATCH = '/private/tmp/claude-501/-Users-dan-Desktop-Study-Games/4c975f86-6f1d-43c3-b73a-277836ad0562/scratchpad'
EDITS = []


def e(pageid, old, new, note, why):
    EDITS.append({'page': str(pageid), 'old': old, 'new': new, 'note': note, 'why': why})


A = '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>'

# ---------------------------------------------------------------- P1
# 597103 (5.2 Valley Connection): fn 5 did not support the sentence; O'Dell et al. 2020 does (and names HCN too).
e('597103',
  'Smoke studies have identified acrolein and formaldehyde, along with benzene, as the main gas-phase contributors to health risk in wildfire smoke.<sup>5</sup>',
  'Smoke studies have identified acrolein, formaldehyde, benzene and hydrogen cyanide as the main gas-phase contributors to health risk in wildfire smoke.<sup>6</sup>',
  'P1 597103 VC: add hydrogen cyanide to the list of main gas-phase risk contributors; footnote becomes 6',
  'O\'Dell et al. 2020 (the study that makes this finding): "acrolein, formaldehyde, benzene, and hydrogen cyanide are the dominant contributors to gas-phase HAPs risk in smoke plumes."')
e('597103',
  '5. Navarro, K. M., et al., ' + A % ('https://par.nsf.gov/servlets/purl/10310689', 'Exposure to Particulate Matter and Estimation of Volatile Organic Compounds across Wildland Firefighter Job Tasks') + ', <em>Environmental Science &amp; Technology</em>, 2021.',
  '5. National Cancer Institute, ' + A % ('https://www.cancer.gov/about-cancer/causes-prevention/risk/substances/formaldehyde/formaldehyde-fact-sheet', 'Formaldehyde and Cancer Risk') + '. 6. O&rsquo;Dell, K., et al., ' + A % ('https://doi.org/10.1021/acs.est.0c04497', 'Hazardous Air Pollutants in Fresh and Aged Western US Wildfire Smoke and Implications for Long-Term Exposure') + ', <em>Environmental Science &amp; Technology</em>, 2020.',
  'P1+P2 597103 VC Sources: fn 5 Navarro replaced; new 5 = National Cancer Institute (carcinogen sentence), 6 = O\'Dell et al. 2020 (smoke sentence)',
  'Navarro et al. 2021 only used acrolein, benzene and formaldehyde to estimate firefighter exposure; it does not identify them as the main risk contributors. O\'Dell et al., ES&T 54(19), 2020, doi 10.1021/acs.est.0c04497 (PubMed 32857515) does.')

# 597093 (4.4 To Your Health): numbers did not match the UKHSA source they are credited to.
e('597093',
  'Ingestion of as little as 10 mL of methanol can cause permanent blindness, and about 30 mL (1 oz) can be fatal, although the fatal dose varies widely from person to person (',
  'Ingestion of as little as 4 to 10 mL of methanol can cause permanent blindness, and the lethal dose is estimated at 300 to 1,000 mg per kg of body weight (very roughly 30 to 90 mL for an adult), although it varies widely from person to person (',
  'P1 597093: methanol blindness and lethal-dose numbers rewritten to match the UKHSA overview already cited',
  'UKHSA Methanol: toxicological overview (updated 11 Oct 2024): "Ingestion of as little as 4 to 10mL of methanol in adults may cause permanent damage"; "minimal lethal dose ... 300 to 1,000mg/kg". It gives no 30 mL / 1 oz figure. 30-90 mL = 21-70 g for 70 kg / 0.79 g/mL, rounded.')
e('597094',
  'which is why Section 4.4 warns that as little as 10 mL can cause blindness.',
  'which is why Section 4.4 warns that as little as 4 to 10 mL can cause blindness.',
  'P1 597094 Clinical Connection: cross-reference to the 4.4 methanol number kept consistent (10 mL -> 4 to 10 mL)',
  'Same UKHSA source as the 597093 fix; this sentence repeats the 4.4 number.')

# ---------------------------------------------------------------- P2
# 597103: IARC/NTP carcinogen sentence had no footnote.
e('597103',
  'Formaldehyde is also classified as a known human carcinogen by the International Agency for Research on Cancer and the U.S. National Toxicology Program.',
  'Formaldehyde is also classified as a known human carcinogen by the International Agency for Research on Cancer and the U.S. National Toxicology Program.<sup>5</sup>',
  'P2 597103 VC: footnote 5 added to the formaldehyde carcinogen sentence',
  'NCI fact sheet: "IARC classifies formaldehyde as a human carcinogen"; in 2011 NTP named it "a known human carcinogen in its 12th Report on Carcinogens."')
# 597103: Ball text normal blood acetone value (clinical reference value, unsourced).
e('597103',
  'The normal concentration of acetone in the human body is less than 1 mg/100 mL of blood.',
  'The normal concentration of acetone in the human body is less than 1 mg/100 mL of blood (Source: ATSDR, ' + A % ('https://www.atsdr.cdc.gov/toxprofiles/tp21.pdf', 'Toxicological Profile for Acetone') + ', 2022).',
  'P2 597103 To Your Health (Ball text): inline source for normal blood acetone',
  'ATSDR Toxicological Profile for Acetone (June 2022), table of acetone levels in human samples: healthy whole blood 0.84-1.90 mg/L (= 0.08-0.19 mg/100 mL), healthy nonfasted plasma 1.74 mg/L; ketoacidotic plasma 290-424 mg/L. Supports "less than 1 mg/100 mL".')
e('597103',
  'The text is reproduced unchanged; the figure descriptions',
  'The text is reproduced unchanged except for one added source citation; the figure descriptions',
  'P2 597103 attribution line: note the added citation in the Ball text',
  'Keeps the adaptation statement accurate after the acetone citation was added to the CC BY-NC-SA source text.')

# 597093: CDC 60% advice had no source.
e('597093',
  'when soap and water are not available. 62% is above 60%',
  'when soap and water are not available (Source: CDC, ' + A % ('https://www.cdc.gov/clean-hands/about/hand-sanitizer.html', 'Hand Sanitizer Guidelines and Recommendations') + '). 62% is above 60%',
  'P2 597093 Lecture Connection example: inline CDC source for the 60% alcohol advice',
  'CDC: "If soap and water are unavailable, use a hand sanitizer with at least 60% alcohol to clean your hands."')

# 597043: A1c 8.4% -> 194 mg/dL (number correct, unsourced).
e('597043',
  'An A1c of 8.4% corresponds to an average glucose of about 194 mg/dL.',
  'An A1c of 8.4% corresponds to an average glucose of about 194 mg/dL (Source: Nathan et al., ' + A % ('https://pmc.ncbi.nlm.nih.gov/articles/PMC2742903/', 'Translating the A1C Assay Into Estimated Average Glucose Values') + ', <em>Diabetes Care</em>, 2008).',
  'P2 597043 Rosa Part 5: inline source for the A1c to average glucose conversion',
  'Nathan et al. 2008 (ADAG): "AG(mg/dl) = 28.7 x A1C - 46.7"; 28.7 x 8.4 - 46.7 = 194.4. (The ADA chart lists only 8% -> 183 and 8.5% -> 197, so the paper with the equation is cited.)')

# Enamel critical pH about 5.5 (cited where first stated in Ch 6 and where it is taught).
DAWES = A % ('https://jcda.ca/sites/default/files/back_issues/vol-69/issue-11/722.pdf', 'What Is the Critical pH and Why Does a Tooth Dissolve in Acid?')
e('597044',
  'can drop below about 5.5, the point at which enamel starts to dissolve.',
  'can drop below about 5.5, the point at which enamel starts to dissolve (Source: C. Dawes, ' + DAWES + ', <em>J Can Dent Assoc</em>, 2003).',
  'P2 597044 Rosa Part 6: inline source for the enamel critical pH of about 5.5',
  'Dawes 2003, JCDA 69(11):722-4: critical pH "may be 5.5" with high salivary calcium and phosphate (up to 6.5 with low; plaque fluid as low as 5.1). "About 5.5" is the usual value.')
e('597112',
  'Below a mouth pH of about 5.5 it starts to dissolve:',
  'Below a mouth pH of about 5.5 it starts to dissolve (Source: C. Dawes, ' + DAWES + ', <em>J Can Dent Assoc</em>, 2003):',
  'P2 597112 Dental Hygiene box: inline source for the critical pH of about 5.5',
  'Same Dawes 2003 source. The box only has a "Further reading" line, not a Sources list, so the inline style is used.')

# ---------------------------------------------------------------- free link fixes (P3, same pages)
e('597094',
  'href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6527027/"',
  'href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6527027/"',
  'P3 link 597094 VC fn 3: moved URL (301 redirect) updated',
  'Old ncbi.nlm.nih.gov/pmc URL 301-redirects to pmc.ncbi.nlm.nih.gov; article verified (Zakhari 2006, ARH 29(4)).')
e('597094',
  'href="https://webarchive.library.unt.edu/eot2008/20090131021247/http:/pubs.niaaa.nih.gov/publications/arh301/14-17.pdf"',
  'href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3860438/"',
  'P3 link 597094 VC fn 5: web-archive PDF replaced with the PMC copy of the same article',
  'Archive PDF returned empty; PMC3860438 is the same Ehlers 2007 ARH 30(1) article and states the variant is "found in approximately 40 percent of people of Far East Asian descent."')
e('597113',
  'href="https://doaj.org/article/290b3f0e98854dadbbe566fff71874f0"',
  'href="https://doi.org/10.3390/horticulturae9030382"',
  'P3 link 597113 VC fn 5: DOAJ record (403 to fetchers) replaced with the article DOI',
  'Wang et al., Horticulturae 9(3):382, 2023, doi 10.3390/horticulturae9030382; same article, more stable link.')


def run():
    pages, res, ok = {}, [], True
    for i, ed in enumerate(EDITS, 1):
        p = ed['page']
        if p not in pages:
            pages[p] = open(os.path.join(LIVE, p + '.html'), encoding='utf-8').read()
        n = pages[p].count(ed['old'])
        status = 'OK' if n == 1 else 'FAIL(count=%d)' % n
        if n != 1:
            ok = False
        else:
            pages[p] = pages[p].replace(ed['old'], ed['new'])
            if pages[p].count(ed['new']) < 1:
                ok, status = False, 'FAIL(new missing)'
        res.append((i, p, status, ed['note']))
    for r in res:
        print('%2d %s %-14s %s' % r)
    json.dump(EDITS, open(os.path.join(SCRATCH, 'fix_t2_ch4-6.json'), 'w'), ensure_ascii=False, indent=1)
    print('ALL OK' if ok else 'SOME EDITS FAILED', len(EDITS), 'edits')
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
