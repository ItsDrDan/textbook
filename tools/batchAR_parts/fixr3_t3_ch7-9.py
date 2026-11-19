"""fixr3_t3_ch7-9.py -- DRAFT round 3 (author decisions 2026-11-18) for CHEM 3B Chapters 7-9.
Notes: SCRATCH/fixr3_t3_ch7-9_notes.md. PDFs read are in SCRATCH/dl/t3/.
e(pageid, old, new, note, why): `old` must occur exactly once in the CURRENT pages/live/<pageid>.html (after batch AQ).
Running this file is a dry run: it checks the edits and writes SCRATCH/fixr3_t3_ch7-9_out/. It does not touch the repo.
Run: python3 fixr3_t3_ch7-9.py
"""
import json, os

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixr3_t3_ch7-9_out')
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


# ---------- 597145 (9.2) Valley Connection: almond facts updated to the newest Almanac ----------
e('597145',
  '<p>California grows nearly 80% of the world&rsquo;s almonds on about 7,600 farms, roughly 90% of them family farms, and Fresno County alone produced about 20% of the state&rsquo;s 2022/23 crop.<sup>1</sup>',
  '<p>In the 2024/25 crop year the United States, almost all of it California, grew about 73% of the world&rsquo;s almonds. California has more than 7,600 almond farms, nearly 90% of them family farms, and Fresno County alone produced about 21% of the state&rsquo;s crop.<sup>1</sup>',
  'R3-1. 9.2 Valley Connection: "nearly 80% ... about 7,600 farms, roughly 90% ... Fresno ... about 20% of the 2022/23 crop"',
  'CONFIRMED, then updated to the newest Almanac. Almond Almanac 2023 (Annual Report 2023), p. 32 (PDF p. 34), table "California Almond Production '
  'by County, crop years 2013/14-2022/23": Fresno 518.3 of 2,571.3 million lb = 20.2% (receipts table on the same page: Fresno "20.2%"), so "about 20%" '
  'was right. Its p. 4 says "nearly 80%", but its own pie chart gives U.S. 76% for 2022/23. Newer: Almond Almanac 2025 (Annual Report 2025), p. 24 '
  '(PDF p. 26), same table through 2024/25: Fresno 559.5 of 2,713.5 million lb = 20.6% (receipts table: Fresno "20.6%", the largest county). '
  'p. 29 (PDF p. 31): world production pie for 2024/25, "U.S. 73%"; "more than 7,600 almond farmers in California: NEARLY 90% ARE FAMILY FARMS". '
  'Cross-check: USDA NASS 2025 California Almond Objective Measurement Report (July 10, 2025), p. 1: "last year\'s crop of 2.73 billion meat pounds", '
  'matching the Almanac total of 2,713.5 million lb (Almanac uses handler receipts). The Fresno County crop report could not be used for tonnage '
  '(the county server denies automated downloads).')
e('597145',
  '1. Almond Board of California, ' + a('https://www.almonds.org/sites/default/files/2023-12/Almanac_2023.pdf', 'Almond Almanac 2023') + ', 2023.',
  '1. Almond Board of California, ' + a('https://www.almonds.org/sites/default/files/2025-12/Digital-Almanac-2025.pdf', 'Almond Almanac 2025') + ', pp. 24 and 29, 2025.',
  'R3-1. 9.2 Valley Connection source 1: Almanac 2023 -> Almanac 2025 (with page numbers)',
  'Downloaded and read with PyMuPDF (SCRATCH/dl/t3/almanac2025.pdf, 104 MB). Page numbers are the printed ones (PDF pp. 26 and 31).')

# ---------- 597123 (7.3) Valley Connection: LBNL news release -> Valley Air District document ----------
e('597123',
  '4. Lawrence Berkeley National Laboratory, ' + a('https://newscenter.lbl.gov/2014/08/20/air-quality-in-san-joaquin-valley/', 'Air Quality in San Joaquin Valley') + ', 2014.',
  '4. San Joaquin Valley Air Pollution Control District, '
  + a('https://archive.valleyair.org/Workshops/postings/2019/04-15-19_rules/nh3.pdf', 'Demonstration of NH<sub>3</sub> Precursor Contributions to PM2.5 in the San Joaquin Valley')
  + ', 2019, appendix (2018 PM2.5 Plan conceptual model), pp. 28&ndash;29.',
  'R3-2. 7.3 Valley Connection source 4: LBNL news release (2014) -> Valley Air District document',
  'Local primary source for "Ammonium nitrate is an especially large part of the Valley\'s wintertime PM2.5." Same 2019 District PDF as source 3, '
  'appendix "San Joaquin Valley PM2.5 SIP (2018)", pp. 28-29 (PDF pp. 163-164): winter stagnation with "high relative humidity also enhance[s] the '
  'formation of secondary particulate matter, especially ammonium nitrate"; "summertime PM2.5 concentrations ... much lower compared to wintertime"; '
  '"Ammonium nitrate, the dominant PM2.5 component throughout the Valley". Kept as a separate numbered entry with page numbers so the list is not renumbered.')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for p, (orig, new) in pages.items():
        assert orig != new, p
        open(os.path.join(OUT, p + '.html'), 'w', encoding='utf-8').write(new)
    json.dump(edits, open(os.path.join(OUT, 'edits.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('OK: %d edits on %d pages -> %s' % (len(edits), len(pages), OUT))
    for x in edits:
        print(' ', x['page'], x['note'][:100])
