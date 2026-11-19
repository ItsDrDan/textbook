"""ROUND 3 (author decisions 2026-11-18) for group t2_ch4-6: replace the GV Wire citations on 597098 and 597113
with local primary sources and upgrade other Valley numbers where a primary source states them.
e(pageid, old, new, note, why): `old` must occur exactly once in the CURRENT pages/live/<pageid>.html.
Running this file only TESTS the edits in memory and dumps SCRATCH/fixr3_t2_ch4-6.json.

Primary sources read (downloaded to SCRATCH/dl/, read with PyMuPDF):
- CDFA, California Agricultural Statistics Review 2023-2024 (PDF created 2025-09-04; newest edition on cdfa.ca.gov/statistics):
  printed p. 9 (PDF p. 11): California "supplying 99 percent or more of the nation's exported ... garlic"
  printed p. 12 (PDF p. 14), table "Commodity Rank, Acreage, Production, and Value, 2023": Garlic, CA rank 1,
      CA share of U.S. receipts 100.0 (%), total value $311,708 (thousand)
  printed p. 23 (PDF p. 25), "Leading Commodities for Gross Value of Agricultural Production by County, 2023":
      Fresno 8 Peaches, All 352,946; 9 Garlic 309,396 ($1,000)
  printed p. 27 (PDF p. 29), "Commodity Rank and Leading Counties ..., 2023": Peaches, All - Fresno 47.0%,
      Tulare 19.5%; Garlic - Fresno 62.7%, Kern 25.6% (percent of state total value)
- USDA AMS 2024 raisin hearing, Exhibit 7 (M. Schutz, RAC): p. 1 counties and "about 1,500 producers";
  p. 2 "approximately 86% of raisins sold in the US are California Raisins".
The Fresno County Crop & Livestock Reports (2024, 2025) could NOT be downloaded (county server returns
403 Access Denied to curl), so no county-report citation is drafted; see notes.
"""
import json, os, sys

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live'
SCRATCH = '/private/tmp/claude-501/-Users-dan-Desktop-Study-Games/4c975f86-6f1d-43c3-b73a-277836ad0562/scratchpad'
EDITS = []


def e(pageid, old, new, note, why):
    EDITS.append({'page': str(pageid), 'old': old, 'new': new, 'note': note, 'why': why})


A = '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>'
CDFA2324 = A % ('https://www.cdfa.ca.gov/Statistics/PDFs/2023-2024_california_agricultural_statistics_review.pdf',
                'California Agricultural Statistics Review 2023&ndash;2024')

# ------------------------------------------------------------------ 597098 (4.9 Valley Connection: garlic)
e('597098',
  'California grows most of the nation&rsquo;s garlic (86%, by a 2007 UC Davis estimate).<sup>1</sup> Garlic was one of Fresno County&rsquo;s ten highest-value crops in 2024.<sup>2</sup> In 2022 the state&rsquo;s garlic crop was worth $309 million, and California supplies 99% or more of the garlic the United States exports.<sup>3</sup></p>',
  'California grows nearly all of the nation&rsquo;s garlic. In 2023 the state&rsquo;s crop was worth about $312 million, California&rsquo;s share of U.S. garlic sales was listed as 100%, and California supplies 99% or more of the garlic the United States exports.<sup>1</sup> Fresno County alone grew about 63% of the state&rsquo;s garlic by value, and garlic was one of the county&rsquo;s ten highest-value crops.<sup>2</sup></p>',
  'R3 597098 VC: garlic numbers moved to the newest CDFA review (2023 data); 2007 UC Davis 86% and GV Wire 2024 claim replaced; Fresno share added',
  'CDFA Ag Statistics Review 2023-2024: p. 12 Garlic CA share of U.S. receipts 100.0, value $311,708K (2023); p. 9 "supplying 99 percent or more of the nation\'s exported ... garlic"; p. 23 Fresno 2023 top ten: 9 Garlic $309,396K (8 Peaches); p. 27 Garlic: Fresno 62.7% of state value. "In 2024" became 2023 because the Fresno County 2024/2025 reports could not be downloaded (403); 2023 is the newest year in a primary source read.')
e('597098',
  '<strong>Sources:</strong> 1. UC Davis News, ' + A % ('https://www.ucdavis.edu/news/natural-fungicide-gives-garlic-growers-hope', 'Natural Fungicide Gives Garlic Growers Hope') + ', 2007. 2. GV Wire, ' + A % ('https://gvwire.com/2025/11/04/fresno-is-nations-top-ag-county-at-9-billion-but-what-does-future-hold/', 'Fresno Is Nation&rsquo;s Top Ag County at $9 Billion') + ', 2025. 3. California Department of Food and Agriculture, ' + A % ('https://www.cdfa.ca.gov/Statistics/PDFs/2022-2023_california_agricultural_statistics_review.pdf', 'California Agricultural Statistics Review 2022&ndash;2023') + ', 2023.</p>',
  '<strong>Sources:</strong> 1. California Department of Food and Agriculture, ' + CDFA2324 + ', 2025, pp. 9 and 12. 2. California Department of Food and Agriculture, ' + CDFA2324 + ', 2025, pp. 23 and 27 (county agricultural commissioners&rsquo; data, 2023).</p>',
  'R3 597098 VC Sources: UC Davis 2007, GV Wire and CDFA 2022-2023 replaced by CDFA 2023-2024 (two entries, with pages)',
  'Local/state primary source (CDFA) with page numbers; GV Wire (news) and the 2007 UC Davis news estimate retired. Pages as printed in the review.')

# ------------------------------------------------------------------ 597113 (6.5 Valley Connection: raisins, peaches)
e('597113',
  'Peaches are also among Fresno County&rsquo;s top ten crops.<sup>4</sup>',
  'Peaches are also among Fresno County&rsquo;s top ten crops, and the county grows nearly half of California&rsquo;s peaches by value.<sup>4</sup>',
  'R3 597113 VC: peach claim kept, Fresno share of state peach value added from the same primary source',
  'CDFA Ag Statistics Review 2023-2024 p. 23: Fresno 2023 top ten, 8 Peaches, All $352,946K; p. 27: Peaches, All - Fresno 47.0% of state value.')
e('597113',
  '4. GV Wire, ' + A % ('https://gvwire.com/2025/11/04/fresno-is-nations-top-ag-county-at-9-billion-but-what-does-future-hold/', 'Fresno Is Nation&rsquo;s Top Ag County at $9 Billion') + ', 2025.',
  '4. California Department of Food and Agriculture, ' + CDFA2324 + ', 2025, pp. 23 and 27 (county agricultural commissioners&rsquo; data, 2023).',
  'R3 597113 VC Sources fn 4: GV Wire replaced by CDFA 2023-2024 review (pp. 23, 27)',
  'Primary state source for the Fresno County top-ten list and peach share (2023 data).')
e('597113',
  'California Raisin Industry overview (USDA AMS 2024 raisin hearing, Exhibit 7)</a>, 2024.',
  'California Raisin Industry overview (USDA AMS 2024 raisin hearing, Exhibit 7)</a>, 2024, pp. 1&ndash;2.',
  'R3 597113 VC fn 2: page numbers added to the raisin hearing exhibit',
  'Exhibit 7 now read in full (3 pp.): p. 1 "production area of California Raisins consists of Fresno, Madera, Tulare, Kern, and Kings Counties with the biggest production in Fresno & Madera Counties"; "about 1,500 producers"; p. 2 "approximately 86% of raisins sold in the US are California Raisins".')


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
    # sanity: no GV Wire left on these pages
    for p in ('597098', '597113'):
        if p in pages and 'gvwire' in pages[p]:
            ok = False
            print('GV Wire still present on', p)
    json.dump(EDITS, open(os.path.join(SCRATCH, 'fixr3_t2_ch4-6.json'), 'w'), ensure_ascii=False, indent=1)
    print('ALL OK' if ok else 'SOME EDITS FAILED', len(EDITS), 'edits')
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
