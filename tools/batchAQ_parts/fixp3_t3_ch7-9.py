"""fixp3_t3_ch7-9.py -- DRAFT round 2 (P3 polish) for CHEM 3B Chapters 7-9 (source audit 2026-11-18).
Audit: SCRATCH/srcaudit_t3_ch7-9.md   Notes: SCRATCH/fixp3_t3_ch7-9_notes.md
e(pageid, old, new, note, why): `old` must occur exactly once in the CURRENT pages/live/<pageid>.html (after Batch AP
and after earlier edits in this file). Running this file is a dry run: it checks the edits and writes
SCRATCH/fixp3_t3_ch7-9_out/ (edits JSON + patched page copies). It does not touch the repo.
Run: python3 fixp3_t3_ch7-9.py
"""
import json, os

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixp3_t3_ch7-9_out')
pages, edits = {}, []


def page(p):
    if p not in pages:
        t = open(os.path.join(LIVE, p + '.html'), encoding='utf-8').read()
        pages[p] = [t, t]
    return pages[p][1]


def e(p, old, new, note, why):
    t = page(p)
    n = t.count(old)
    assert n == 1, (p, note, n)
    pages[p][1] = t.replace(old, new)
    edits.append({'page': p, 'old': old, 'new': new, 'note': note, 'why': why})


def a(url, text):
    return '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>' % (url, text)


def src(publisher, url, title, extra=''):
    return '(Source: %s, %s%s)' % (publisher, a(url, title), extra)


# ===================== Chapter 7 =====================
e('597123',
  'The effective dose of caffeine is about 200 mg, corresponding to about two cups of strong coffee or tea.</p>',
  'The effective dose of caffeine is about 200 mg, about two 8-ounce cups of coffee at 80&ndash;100 mg each '
  + src('U.S. Food and Drug Administration', 'https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much', 'Spilling the Beans: How Much Caffeine Is Too Much?') + '.</p>',
  'P3. 7.3 To Your Health (alkaloids): caffeine 200 mg = "two cups of strong coffee or tea" had no source',
  'FDA consumer update: an 8-ounce cup of coffee has 80-100 mg (and 400 mg/day is the amount not generally linked to harm). '
  '"Strong coffee or tea" -> "8-ounce cups of coffee" because tea has far less (FDA: black tea 71 mg per 12 oz), so two cups of tea is not 200 mg. '
  'The "effective dose" itself is Ball\'s wording; FDA does not state one (listed in the notes).')
e('597123',
  'When smoked, cocaine reaches the brain in 15 s.</p>',
  'When smoked, cocaine enters the bloodstream almost as fast as an injection, and the high lasts only 5 to 10 minutes '
  + src('National Institute on Drug Abuse', 'https://nida.nih.gov/publications/research-reports/cocaine/what-are-short-term-effects-cocaine-use', 'What Are the Short-Term Effects of Cocaine Use?') + '.</p>',
  'P3. 7.3 To Your Health: "When smoked, cocaine reaches the brain in 15 s." had no source',
  'No source gives 15 s (NIDA-derived sources say "within seconds", "less than 10 seconds", or 19 s). Rewritten to what NIDA says: '
  '"absorption into the bloodstream is almost as rapid as by injection"; the high lasts "only 5 to 10 minutes". The last part also '
  'fits the next paragraph of the box (dopamine depleted, craving).')

e('597130',
  'Nylon-6,6 was first invented in 1935 and has been used',
  'Nylon-6,6 was first made by Wallace Carothers&rsquo;s group at DuPont on February 28, 1935 '
  + src('A. B. Costa, EBSCO Research Starters', 'https://ebsco.com/research-starters/history/carothers-invents-nylon', 'Carothers Invents Nylon') + ' and has been used',
  'P3. 7.10 section text (CK-12): "Nylon-6,6 was first invented in 1935" had no source',
  'History date a reader would question. EBSCO Research Starters (Albert B. Costa, 2021): "it was the nylon 6-6, prepared on February 28, 1935, '
  'that became Du Pont\'s nylon." The ACS National Historic Chemical Landmark page would be better but returned no text to my fetch.')

e('597131',
  'so that a drop can be caught before symptoms appear.</p>',
  'so that a drop can be caught before symptoms appear.<sup>2</sup></p>',
  'P3. 7.11 Valley Connection: source list had no superscript anchors (medical supervision sentence)',
  'Anchors source 2 (3 CCR 6728) to its sentence.')
e('597131',
  'sales ended in 2020 after state regulators linked it to harm to the developing brains of children.</p>',
  'sales ended in February 2020, and growers had to stop using it by the end of that year, after state regulators linked it to harm to the developing brains of children.<sup>1</sup></p>',
  'P3. 7.11 Valley Connection: chlorpyrifos sentence had no anchor; dates made exact',
  'CalEPA release (Oct 9, 2019): sales to growers end Feb. 6, 2020; possession and use end Dec. 31, 2020; "impaired brain and neurological development".')
e('597131',
  '2. California Code of Regulations, Title 3, section 6728 (medical supervision of pesticide handlers); see the sources in Section 11.4.</p>',
  '2. California Code of Regulations, Title 3, section 6728 (medical supervision of pesticide handlers); California Department of Pesticide Regulation, '
  + a('https://www.cdpr.ca.gov/docs/whs/pdf/medical_supervision_program.pdf', 'Medical Supervision Program') + '; see also the sources in Section 11.4.</p>',
  'P3. 7.11 Valley Connection source 2: no direct link',
  'DPR Worker Health and Safety page: the program protects workers who "regularly mix, load, or apply" Category I and II organophosphate and '
  'carbamate pesticides, with a physician tracking cholinesterase by blood tests. (Search indexed the URL as cdpr.ca.gov:/docs/...; written here without the stray colon.)')

# ===================== Chapter 8 =====================
e('597136',
  ' It should be noted, though, that a glass of tomato juice has six times as much methanol as a similar amount of a diet soda containing aspartame.',
  '',
  'P3. 8.3 Artificial Sweeteners: "a glass of tomato juice has six times as much methanol as ... diet soda" (DELETED)',
  'The only document with this figure (UK Committee on Toxicity paper TOX/2010/04) is marked as a discussion paper that "should not be cited"; '
  'the other sources are a pro-aspartame explainer and a blog. Deleted rather than cited weakly. The paragraph still explains the methanol '
  'concern and the PKU risk.')

e('597138',
  'and fetal red blood cells are broken down faster.<sup>1</sup>',
  'and the newborn&rsquo;s red blood cells have a shorter life span, so more bilirubin is made.<sup>1</sup>',
  'P3. 8.5 Nursing: "fetal red blood cells are broken down faster"',
  'Matches the cited MSD Manual wording: "Shorter neonatal red blood cell life span increases bilirubin production."')

e('597139',
  'Lactose makes up about 40% of an infant&rsquo;s diet during the first year of life.',
  'Lactose supplies about 40% of the energy that a fully breast-fed infant takes in '
  + src('B. Grenov et al.', 'https://doi.org/10.1177/0379572116629024', 'Undernourished Children and Milk Lactose', ', <em>Food and Nutrition Bulletin</em>, 2016') + '.',
  'P3. 8.6 To Your Health: "Lactose makes up about 40% of an infant\'s diet during the first year of life" had no source',
  'Grenov et al., Food Nutr Bull 37(1):85-99 (2016): lactose "constitutes about 40% of the daily energy consumption" in exclusively breast-fed '
  'infants (human milk about 70 g/L lactose). Confirmed via the abstract in two searches; the publisher page refused my fetch (403). '
  '"of an infant\'s diet ... first year" was vague (by mass? all infants?), so it now says energy and breast-fed.')

e('597142',
  "<summary>Answer</summary><div>(a) Glucose mutarotates through its open-chain form, which has a free aldehyde at C1. That aldehyde reacts with an amine group on hemoglobin (the N-terminal valine of the &beta; chain) and the product rearranges to a stable attachment: the same reducing-sugar reactivity that gives a positive Benedict's test. (b) A fingerstick reports glucose right now; HbA1c reports the fraction of hemoglobin glycated over the 120-day life of red blood cells, so a normal reading today is consistent with high average glucose over the past two to three months. (c) The open-chain aldehyde, which is less than 0.1% of the glucose",
  "<summary>Answer</summary><div>(a) Glucose mutarotates through its open-chain form, which has a free aldehyde at C1. That aldehyde reacts with an amine group on hemoglobin (the N-terminal valine of the &beta; chain) and the product rearranges to a stable attachment: the same reducing-sugar reactivity that gives a positive Benedict's test. (b) A fingerstick reports glucose right now; HbA1c reports the fraction of hemoglobin glycated over the 120-day life of red blood cells, so a normal reading today is consistent with high average glucose over the past two to three months. (c) The open-chain aldehyde, which is less than 0.02% of the glucose",
  'P3. 8.9 Practice Problems (inline answer): open-chain glucose "less than 0.1%" vs 8.4 figure "less than 0.02%"',
  'Consistency with Section 8.4 (Figure 8.4.4: "less than 0.02% open chain"). Not an error (0.02% is less than 0.1%), just two numbers for one fact.')
e('597142',
  'less than 0.1% of the glucose',
  'less than 0.02% of the glucose',
  'P3. 8.9 Practice Problems (answer key, Problem 8.64): same change',
  'Second copy of the same answer, in the printed answer key.')

# ===================== Chapter 9 =====================
e('597145',
  'href="https://it.almonds.org/sites/default/files/2023-12/Almanac_2023.pdf"',
  'href="https://www.almonds.org/sites/default/files/2023-12/Almanac_2023.pdf"',
  'P3 link fix. 9.2 Valley Connection source 1: Almanac linked on the Almond Board\'s Italian site',
  'Same PDF on the U.S. site (almonds.com/... redirects here; the file exists, too large to fetch). '
  'Fresno\'s "about 20%" share is still unconfirmed (listed for the author).')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for p, (orig, new) in pages.items():
        assert orig != new, p
        open(os.path.join(OUT, p + '.html'), 'w', encoding='utf-8').write(new)
    json.dump(edits, open(os.path.join(OUT, 'edits.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('OK: %d edits on %d pages -> %s' % (len(edits), len(pages), OUT))
    for x in edits:
        print(' ', x['page'], x['note'][:95])
