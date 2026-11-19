"""ROUND 2 (P3 polish) for group t2_ch4-6 (Chapters 4-6), from srcaudit_t2_ch4-6.md.
e(pageid, old, new, note, why): `old` must occur exactly once in the CURRENT
/Users/dan/Desktop/Study Games/textbook-git/pages/live/<pageid>.html (after earlier edits on the same page).
None of these pages overlap the round-1 edits' strings. Running this file only TESTS the edits in memory
(no repo file is written) and dumps SCRATCH/fixp3_t2_ch4-6.json.
"""
import json, os, sys

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live'
SCRATCH = '/private/tmp/claude-501/-Users-dan-Desktop-Study-Games/4c975f86-6f1d-43c3-b73a-277836ad0562/scratchpad'
EDITS = []


def e(pageid, old, new, note, why):
    EDITS.append({'page': str(pageid), 'old': old, 'new': new, 'note': note, 'why': why})


A = '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>'

# 597094 (4.5 Valley Connection, "In the clinic"): NIAAA lists overdose risk for anxiety medicines only.
e('597094',
  'with anxiety or sleep medicines it raises overdose risk, and older adults are at especially high risk.<sup>6</sup>',
  'with anxiety medicines it raises overdose risk, with sleep medicines it can slow breathing, and older adults are at especially high risk.<sup>6</sup>',
  'P3 597094 VC: sleep-medicine wording matched to NIAAA fn 6',
  'NIAAA Harmful Interactions (rev. 2014): anxiety medicines row lists "increased risk for overdose"; sleep medicines row lists drowsiness, "slowed or difficult breathing", impaired motor control (no overdose).')

# 597098 (4.9 Valley Connection): footnotes appeared in the order 1, 3, 2. Renumber in reading order.
e('597098',
  'ten highest-value crops in 2024.<sup>3</sup> In 2022 the state&rsquo;s garlic crop was worth $309 million, and California supplies 99% or more of the garlic the United States exports.<sup>2</sup>',
  'ten highest-value crops in 2024.<sup>2</sup> In 2022 the state&rsquo;s garlic crop was worth $309 million, and California supplies 99% or more of the garlic the United States exports.<sup>3</sup>',
  'P3 597098 VC: footnote markers renumbered to reading order (3,2 -> 2,3)',
  'Style: sources must be numbered in order of first citation.')
e('597098',
  '2. California Department of Food and Agriculture, ' + A % ('https://www.cdfa.ca.gov/Statistics/PDFs/2022-2023_california_agricultural_statistics_review.pdf', 'California Agricultural Statistics Review 2022&ndash;2023') + ', 2023. 3. GV Wire, ' + A % ('https://gvwire.com/2025/11/04/fresno-is-nations-top-ag-county-at-9-billion-but-what-does-future-hold/', 'Fresno Is Nation&rsquo;s Top Ag County at $9 Billion') + ', 2025.',
  '2. GV Wire, ' + A % ('https://gvwire.com/2025/11/04/fresno-is-nations-top-ag-county-at-9-billion-but-what-does-future-hold/', 'Fresno Is Nation&rsquo;s Top Ag County at $9 Billion') + ', 2025. 3. California Department of Food and Agriculture, ' + A % ('https://www.cdfa.ca.gov/Statistics/PDFs/2022-2023_california_agricultural_statistics_review.pdf', 'California Agricultural Statistics Review 2022&ndash;2023') + ', 2023.',
  'P3 597098 VC Sources: entries 2 and 3 swapped to match the renumbered markers',
  'Same renumbering; no source changed. ($309 M re-verified: NASS Vegetables 2022 Summary, garlic value $309 million; 99%+: CDFA 2022-2023 Agricultural Exports, California share of U.S. garlic exports 100.0% in 2021 and 2022.)')

# 597096 (4.7 Lecture Connection): history date -> source (Ball text above is "reproduced unchanged", so cite in the author's own sentence).
e('597096',
  'The section text tells the story of phenol as Lister\'s surgical antiseptic in the 1860s and of 4-hexylresorcinol as a milder successor.',
  'The section text tells the story of phenol as Lister\'s surgical antiseptic in the 1860s (Source: Pitt and Aubin, ' + A % ('https://pmc.ncbi.nlm.nih.gov/articles/PMC3468637/', 'Joseph Lister: father of modern surgery') + ', <em>Can J Surg</em>, 2012) and of 4-hexylresorcinol as a milder successor.',
  'P3 597096 Lecture Connection: source for Lister and phenol (1867)',
  'Pitt & Aubin 2012 (fetched): "he applied carbolic acid compounds as an antiseptic on surgical wounds"; published in the Lancet "the first in March 1867".')

# 597097 (4.8 figure caption, Ball text edited): history date -> source.
e('597097',
  'William Morton, a Boston dentist, introduced diethyl ether into surgical practice in 1846.',
  'William Morton, a Boston dentist, introduced diethyl ether into surgical practice in 1846 (Source: Makris et al., ' + A % ('https://pmc.ncbi.nlm.nih.gov/articles/PMC10431324/', 'Henry Jacob Bigelow (1818&ndash;1890): A Champion for Anesthesia') + ', <em>Annals of Surgery Open</em>, 2022).',
  'P3 597097 figure caption: source for Morton and ether, 1846',
  'Makris et al. 2022 (fetched): October 16, 1846 "Ether Day"; Morton\'s "successful public demonstration of surgical anesthesia" at Massachusetts General Hospital.')

# 597105 (5.4 Malik text, edited): contestable physiology claim -> source.
e('597105',
  'but lactate itself is no longer thought to be the main cause of that fatigue.</p>',
  'but lactate itself is no longer thought to be the main cause of that fatigue (Source: Allen, Lamb and Westerblad, ' + A % ('https://doi.org/10.1152/physrev.00015.2007', 'Skeletal muscle fatigue: cellular mechanisms') + ', <em>Physiological Reviews</em>, 2008).</p>',
  'P3 597105: source for "lactate is no longer thought to be the main cause of fatigue"',
  'Allen, Lamb & Westerblad, Physiol Rev 88:287-332 (2008), abstract (via QxMD/PubMed 18195089): the lactate and H+ explanation is "probably of limited importance in mammals". Publisher page returns 403.')

# 597106 (5.5 Lecture Connection): surprising drug-safety claim -> source.
e('597106',
  'Naproxen (the pain reliever in Aleve) has a toxic enantiomer, so care is taken to manufacture it as a single enantiomer.',
  'Naproxen (the pain reliever in Aleve) has a toxic enantiomer, so care is taken to manufacture it as a single enantiomer (Source: Papp et al., ' + A % ('https://pmc.ncbi.nlm.nih.gov/articles/PMC9101765/', 'Determination of Chiral Impurity of Naproxen') + ', <em>Molecules</em>, 2022).',
  'P3 597106 Lecture Connection: source for the naproxen enantiomer claim',
  'Papp et al., Molecules 27(9):2986, 2022 (fetched): "Naproxen is used as a single enantiomer, in the form of S-naproxen"; "R-naproxen is hepatotoxic."')

# 597114 (6.6 Table 1): ethyl butyrate melting point wrong.
e('597114',
  '<td data-th="Melting Point (&deg;C)" style="text-align:center;vertical-align:middle;">&minus;101</td>',
  '<td data-th="Melting Point (&deg;C)" style="text-align:center;vertical-align:middle;">&minus;97 (Source: ' + A % ('https://pubchem.ncbi.nlm.nih.gov/compound/7762', 'PubChem, Ethyl butyrate') + ', CRC Handbook value)</td>',
  'P3 597114 Table 6.6.1: ethyl butyrate melting point -101 -> -97 deg C, with source',
  'PubChem CID 7762 melting point: -97 C (CRC Handbook of Chemistry and Physics, 95th ed., p. 3-252); also -93.3 C (HMDB), -135 F (USCG CHRIS). No source gives -101. Only occurrence in the page set.')


def run():
    pages, res, ok = {}, [], True
    for i, ed in enumerate(EDITS, 1):
        p = ed['page']
        if p not in pages:
            pages[p] = open(os.path.join(LIVE, p + '.html'), encoding='utf-8').read()
        n = pages[p].count(ed['old'])
        status = 'OK' if n == 1 else 'FAIL(count=%d)' % n
        if n == 1:
            pages[p] = pages[p].replace(ed['old'], ed['new'])
        else:
            ok = False
        res.append((i, p, status, ed['note']))
    for r in res:
        print('%2d %s %-14s %s' % r)
    json.dump(EDITS, open(os.path.join(SCRATCH, 'fixp3_t2_ch4-6.json'), 'w'), ensure_ascii=False, indent=1)
    print('ALL OK' if ok else 'SOME EDITS FAILED', len(EDITS), 'edits')
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
