"""Fix drafts for group t5_ch13-15 (CHEM 3B textbook Ch 13-15): P1 + P2 items from srcaudit_t5_ch13-15.md,
plus one free moved-link fix (P3). Sources re-verified 2026-11-18.
e(pageid, old, new, note, why): `old` must occur exactly once in the current pages/live/<pageid>.html
(after earlier edits on the same page). Running this file does a dry run only: it applies the edits in memory,
checks every count, and writes SCRATCH/fix_t5_ch13-15.json. It never writes to the repo."""
import json, os, sys

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live'
SCRATCH = '/private/tmp/claude-501/-Users-dan-Desktop-Study-Games/4c975f86-6f1d-43c3-b73a-277836ad0562/scratchpad'
EDITS = []


def e(pageid, old, new, note, why):
    EDITS.append({'page': str(pageid), 'old': old, 'new': new, 'note': note, 'why': why})


def a(url, title):
    return '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>' % (url, title)


CDC_ABOUT = a('https://www.cdc.gov/diabetes/about/index.html', 'About Diabetes')
CDC_NDSR = a('https://www.cdc.gov/diabetes/php/data-research/index.html', 'National Diabetes Statistics Report')
CDC_HEART = a('https://www.cdc.gov/diabetes/diabetes-complications/diabetes-and-your-heart.html', 'Diabetes and Your Heart')
COCHRANE = a('https://doi.org/10.1002/14651858.CD004714.pub4', 'Treatment of periodontitis for glycaemic control in people with diabetes mellitus')
ADA_HYPO = a('https://diabetes.org/living-with-diabetes/hypoglycemia-low-blood-glucose', 'Hypoglycemia (Low Blood Glucose)')
NIDDK = a('https://www.niddk.nih.gov/health-information/health-statistics/overweight-obesity', 'Overweight &amp; Obesity Statistics')
USDA = a('https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/1718/Table_5_EIN_MaleFemale_17.pdf', 'What We Eat in America, NHANES 2017&ndash;2018, Table 5')
BLS = a('https://www.bls.gov/ooh/healthcare/exercise-physiologists.htm', 'Occupational Outlook Handbook: Exercise Physiologists')

# ---------------- 597192 (13.4) To Your Health: Diabetes ----------------
e('597192',
  'Some of the serious complications of diabetes are as follows:</p>',
  'Some of the serious complications of diabetes are as follows (Source: Centers for Disease Control and Prevention, %s):</p>' % CDC_ABOUT,
  'P2: cite CDC for the complications list (amputations, blindness, kidney failure)',
  'Unsourced statistics. CDC About Diabetes (updated Jan 2 2026): diabetes is "the No. 1 cause of kidney failure, lower-limb amputations, and adult blindness."')
e('597192',
  '<li>It increases the risk of having a heart attack or stroke by two to four times.</li>',
  '<li>It doubles the risk of heart disease and also raises the risk of stroke (Source: Centers for Disease Control and Prevention, %s).</li>' % CDC_HEART,
  'P1: "two to four times" -> "doubles", with CDC source',
  'Wrong/unsourced multiplier. CDC Diabetes and Your Heart: people with diabetes have "twice the risk for heart disease"; the page links reduced blood flow to the brain with stroke but gives no stroke multiplier, so the stroke clause states only "raises the risk".')
e('597192',
  'about 90&ndash;95% of people with diabetes have type 2. (Current CDC estimates are about 38 million Americans with diabetes; Section 13.9 gives the figures for Valley counties.)',
  'about 90&ndash;95%% of people with diagnosed diabetes have type 2 (Source: Centers for Disease Control and Prevention, %s). CDC estimates that 40.1 million Americans, 12.0%% of the population, had diabetes in 2023 (Source: Centers for Disease Control and Prevention, %s); Section 13.9 gives the figures for Valley counties.' % (CDC_ABOUT, CDC_NDSR),
  'P1: 38 million -> 40.1 million (2023 data), cited; P2: cite CDC for 90-95% type 2',
  'Outdated number. CDC National Diabetes Statistics Report (updated Sept 16 2026): "40.1 million" people with diagnosed or undiagnosed diabetes in 2023, "12.0%" of the U.S. population. CDC About Diabetes: type 2 is "about 90% to 95% of all diagnosed cases of diabetes." The parenthetical was made a sentence to avoid nested parentheses.')

# ---------------- 597195 (13.9) ----------------
e('597195',
  'For a patient who is awake and can swallow, the American Diabetes Association&rsquo;s &ldquo;15-15 rule&rdquo; applies:',
  'For a patient who is awake and can swallow, the American Diabetes Association&rsquo;s &ldquo;15-15 rule&rdquo; applies (Source: American Diabetes Association, %s):' % ADA_HYPO,
  'P2: link the ADA 15-15 rule',
  'In-text attribution with no link. ADA hypoglycemia page: use the "15/15 rule of 15g fast-acting carbs/15 minutes"; low blood glucose is below 70 mg/dL.')
e('597195',
  'and periodontal treatment measurably improves glucose control.',
  'and periodontal treatment lowers HbA1c by about 0.4 percentage points on average (Source: Cochrane review, %s, 2022).' % COCHRANE,
  'P2: quantify and cite periodontal treatment and glucose control (dental box)',
  'Unsourced health claim. Simpson TC et al., Cochrane Database Syst Rev 2022, CD004714.pub4: moderate-certainty evidence, absolute HbA1c reduction of 0.43% at 3-4 months after periodontal treatment (0.30% at 6 months).')

# ---------------- 597053 (Ch 15 opener) Rosa Part 15 ----------------
e('597053',
  'Studies suggest that treating gum disease can modestly improve blood glucose control, along with',
  'Treating gum disease can modestly improve blood glucose control (Source: Cochrane review, %s, 2022), along with' % COCHRANE,
  'P2: cite Cochrane for gum-disease treatment and glucose control (Rosa Part 15)',
  'Unsourced health claim in the case. Same Cochrane 2022 review (HbA1c about 0.4 points lower). "Studies suggest" dropped because the citation now carries the evidence.')

# ---------------- 597209 (15.4) Fat and obesity ----------------
e('597209',
  'In earlier times, major human food was vegetables, and fats in food accounted for about 20% of food calories, but these days about one-third of food calories (roughly 33&ndash;36% in the United States) come from fats.',
  'Today about 36%% of the food calories eaten in the United States come from fat (Source: U.S. Department of Agriculture, %s).' % USDA,
  'P2: replace unsourced fat-calorie history with the USDA figure',
  'The "earlier times ... about 20%" clause has no source and was deleted. USDA ARS What We Eat in America, NHANES 2017-2018, Table 5: total fat = 36% of energy for individuals 2 and over (and 36% for adults 20 and over).')
e('597209',
  'According to NIH, nearly 3 out of 4 adults aged 20 or above in the US are overweight or obese.',
  'According to NIH, nearly 3 out of 4 adults aged 20 or above in the US are overweight or obese (Source: National Institute of Diabetes and Digestive and Kidney Diseases, %s).' % NIDDK,
  'P2: link the NIH "3 out of 4" figure',
  'In-text attribution with no link. NIDDK (NHANES 2017-2018, adults 20+): overweight 30.7% + obesity 42.4% = 73.1%.')

# ---------------- 597213 (15.5) Valley Connection ----------------
e('597213',
  ' Fresno County&rsquo;s 2020 community health assessment, using California Health Interview Survey data, found 12% of Fresno County adults had ever been diagnosed with diabetes, compared with 9.8% statewide.<sup>4</sup>',
  '',
  'P2: delete the unverifiable 2020 CHNA sentence (12% vs 9.8%)',
  'The 2020 CHNA PDF could not be opened (TLS certificate rejected) and no search result confirms 12% or 9.8%. Deleted rather than kept unverified; the PLACES 2023 sentence before it already makes the point with newer data.')
e('597213',
  ' 4. Fresno County Department of Public Health and Central Valley Health Policy Institute, <a style="text-decoration:underline" href="https://chhs.fresnostate.edu/cvhpi/documents/2020-chna-report.pdf" rel="noopener" target="_blank">Fresno County Community Health Needs Assessment</a>, 2020.',
  '',
  'P2: remove Source 4 (its only claim was deleted)',
  'Source 4 is no longer cited anywhere in the box; it was the last item, so no renumbering is needed.')

# ---------------- 597208 (15.8) Career Focus ----------------
e('597208',
  'Each individual must be referred by a licensed physician. An exercise physiologist works in a variety of settings, such as a hospital or in a wellness program at a commercial business, to design and monitor individual exercise plans. A registered clinical exercise physiologist must have an undergraduate degree in exercise physiology or a related degree. Some job opportunities require a master&rsquo;s degree in exercise physiology or a related degree.',
  'Many patients are referred by a physician. An exercise physiologist works in a variety of settings, such as a hospital or in a wellness program at a commercial business, to design and monitor individual exercise plans. Most exercise physiologists need at least a bachelor&rsquo;s degree in exercise science, exercise physiology, kinesiology or a related field, and some jobs require a master&rsquo;s degree (Source: U.S. Bureau of Labor Statistics, %s).' % BLS,
  'P2: career box: physician referral not mandatory; drop retired RCEP title; cite BLS',
  'Outdated and over-stated. BLS OOH: "Most need at least a bachelor\'s degree in exercise science, exercise physiology, kinesiology, or a related" field; physicians "may prescribe exercise regimens for their patients and refer them to exercise physiologists" (not "must"). ACSM merged the RCEP credential into a single ACSM-CEP exam in 2018, so the "registered clinical exercise physiologist" title was removed.')

# ---------------- 597211 (15.1) moved link (free P3) ----------------
e('597211',
  'href="https://www.intechopen.com/books/lipoproteins-role-in-health-and-diseases/pathophysiology-of-lipoprotein-oxidation"',
  'href="https://www.intechopen.com/chapters/39567"',
  'P3 (free): update the moved IntechOpen chapter link in the Figure 1 credit',
  'Old URL 301-redirects to https://www.intechopen.com/chapters/39567, which is the same chapter (Jairam, Uchida, Narayanaswami, "Pathophysiology of Lipoprotein Oxidation", 2012, doi 10.5772/50622).')


def dry_run():
    pages, ok = {}, True
    for i, ed in enumerate(EDITS, 1):
        p = ed['page']
        if p not in pages:
            pages[p] = open(os.path.join(LIVE, p + '.html'), encoding='utf-8').read()
        n = pages[p].count(ed['old'])
        status = 'OK' if n == 1 else 'FAIL (count=%d)' % n
        ok &= n == 1
        print('%2d %s %-6s %s' % (i, p, status, ed['note'][:70]))
        if n == 1:
            pages[p] = pages[p].replace(ed['old'], ed['new'])
    # post-checks
    assert '38 million' not in pages['597192'] and 'two to four times' not in pages['597192']
    assert '2020-chna-report' not in pages['597213'] and '<sup>4</sup>' not in pages['597213']
    return ok


if __name__ == '__main__':
    ok = dry_run()
    json.dump(EDITS, open(os.path.join(SCRATCH, 'fix_t5_ch13-15.json'), 'w'), ensure_ascii=False, indent=1)
    print('ALL OK' if ok else 'SOME EDITS FAILED')
    sys.exit(0 if ok else 1)
