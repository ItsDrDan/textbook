"""fix_t3_ch7-9.py -- DRAFT P1 + P2 source/science fixes for CHEM 3B Chapters 7-9 (source audit 2026-11-18).
Audit: SCRATCH/srcaudit_t3_ch7-9.md   Notes: SCRATCH/fix_t3_ch7-9_notes.md
Each e(pageid, old, new, note, why): `old` must occur exactly once in the CURRENT pages/live/<pageid>.html
(after earlier edits on the same page). Running this file is a dry run: it only checks the edits and writes
SCRATCH/fix_t3_ch7-9_out/ (edits JSON + patched page copies). It does not touch the repo or publish anything.
Run: python3 fix_t3_ch7-9.py
"""
import json, os, sys

LIVE = '/Users/dan/Desktop/Study Games/textbook-git/pages/live'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fix_t3_ch7-9_out')
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


ADA2 = 'https://doi.org/10.2337/dc26-S002'
ADA6 = 'https://doi.org/10.2337/dc26-S006'

# ===================== Chapter 7 =====================
e('597123',
  'The lethal dose for an adult was long quoted as about 50 mg, but current estimates are much higher, roughly 0.5 to 1 g.',
  'The lethal dose for an adult was long quoted as about 50&ndash;60 mg, but current estimates are much higher, roughly 0.5 to 1 g '
  + src('B. Mayer', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3880486/', 'How Much Nicotine Kills a Human?', ', <em>Archives of Toxicology</em>, 2014') + '.',
  'P2. 7.3 To Your Health (alkaloids): nicotine lethal dose had no source',
  'Mayer 2014 (Arch Toxicol 88:5-7): "the lower limit causing fatal outcomes is 0.5-1 g of ingested nicotine"; he traces the old '
  'figure (60 mg) to a 1906 textbook. "50" -> "50-60" so the old figure matches the cited paper.')

# ===================== Chapter 8 =====================
e('597134',
  '(about 60%&ndash;65% by mass of the average diet)',
  '(about half of the calories in the average U.S. diet; '
  + 'Source: USDA Agricultural Research Service, '
  + a('https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/1718/Table_7_EIN_INC_17.pdf', 'What We Eat in America, NHANES 2017&ndash;2018') + ')',
  'P2. 8.1 section text: carbohydrates "about 60%-65% by mass of the average diet"',
  'WWEIA NHANES 2017-2018 Table 7: carbohydrate supplies about 47% of energy for U.S. adults (44-49% across income groups). '
  'By mass it is about 60% of macronutrient grams (Table 1: men 281 g carbohydrate vs 95 g protein + 101 g fat), so "60-65% by mass" '
  'was only defensible at the low end; calories are the figure students meet in nutrition.')
e('597134',
  'Carbohydrates are about 65% of the diet and a major source of energy',
  'Carbohydrates supply about half of our calories (47% for U.S. adults) and are a major source of energy',
  'P2. 8.1 Lecture Connection: "Carbohydrates are about 65% of the diet"',
  'Same source as the section-text edit above (cited there, same page). 65% overstated the share of calories.')
e('597141',
  'O<sub><em>n</em></sub>, about 65% of the diet.',
  'O<sub><em>n</em></sub>, about half of dietary calories.',
  'P2. 8.8 Chapter Guide Key Idea 1: "about 65% of the diet"',
  'Matches the corrected 8.1 wording (USDA WWEIA 2017-2018, cited in 8.1). No citation added in the guide: it points to Section 8.1.')

e('597136',
  'and normal urine may contain anywhere from a trace to 20 mg glucose/dL urine.</p>',
  'and normal urine contains little or no glucose, 0&ndash;15 mg/dL '
  + src('MedlinePlus', 'https://medlineplus.gov/ency/article/003581.htm', 'Glucose Urine Test') + '.</p>',
  'P1. 8.3 section text: normal urine glucose "a trace to 20 mg/dL"',
  'MedlinePlus: "Normal glucose range in urine: 0 to 0.8 mmol/l (0 to 15 mg/dL)" and glucose "is not usually found in urine".')
e('597136',
  'a persistently high level is <em>hyperglycemia</em>. (Many other countries',
  'a persistently high level is <em>hyperglycemia</em> (Source: American Diabetes Association, '
  + a(ADA2, 'Standards of Care in Diabetes&mdash;2026, Section 2') + ' and ' + a(ADA6, 'Section 6') + '). (Many other countries',
  'P2. 8.3 Lecture Connection "Glucose in the blood": fasting 70-99, hypoglycemia <70, prediabetes 100-125, diabetes >=126 had no source',
  'ADA 2026 Section 2 (Diabetes Care 49 Suppl 1:S27-S49): Table 2.1 "FPG >=126 mg/dL"; Table 2.2 "FPG 100 mg/dL ... to 125 mg/dL (IFG)" '
  '(so normal is below 100). Section 6 (S132-S149) Table 6.4: Level 1 hypoglycemia "Glucose <70 mg/dL". One citation for the sentence.')
e('597136',
  '<p>All of the extensive clinical studies completed to date have indicated that these artificial sweeteners approved for use in the United States are safe for consumption by healthy individuals in moderate amounts.</p>',
  '<p>In 2023 the World Health Organization&rsquo;s cancer agency (IARC) listed aspartame as &ldquo;possibly carcinogenic to humans&rdquo; on limited evidence, '
  'but the WHO&ndash;FAO expert committee on food additives (JECFA) kept its acceptable daily intake of 40 mg per kg of body weight '
  + src('World Health Organization', 'https://www.who.int/news/item/14-07-2023-aspartame-hazard-and-risk-assessment-results-released', 'Aspartame Hazard and Risk Assessment Results Released', ', 2023')
  + '. The sweeteners approved in the United States are considered safe for healthy people in moderate amounts.</p>',
  'P2. 8.3 Looking Closer: Artificial Sweeteners: "All of the extensive clinical studies ... are safe"',
  'Outdated: WHO/IARC/JECFA joint release, 14 July 2023: "IARC classified aspartame as possibly carcinogenic to humans (Group 2B)"; '
  '"JECFA reaffirmed the acceptable daily intake of 40 mg/kg body weight." "All ... studies" could not be sourced and is no longer true '
  '(IARC weighed some studies as positive), so it was rewritten; the closing safety sentence keeps the author\'s point without "all studies".')

e('597137',
  '6.5% or higher supports a diagnosis of diabetes)',
  '6.5% or higher supports a diagnosis of diabetes; source: American Diabetes Association, '
  + a(ADA2, 'Standards of Care in Diabetes&mdash;2026, Section 2') + ')',
  'P2. 8.4 Nursing box: HbA1c cutoffs had no source',
  'ADA 2026 Section 2: Table 2.1 "A1C >=6.5% (>=48 mmol/mol)"; Table 2.2 "A1C 5.7-6.4% (39-47 mmol/mol)". The cutoffs are already '
  'inside parentheses, so the source is added there after a semicolon instead of a second pair of parentheses.')

e('597139',
  'The incidence of galactosemia in the United States is 1 in every 65,000 newborn babies.</p>',
  'Classic galactosemia occurs in about 1 in 30,000 to 60,000 newborns '
  + src('MedlinePlus Genetics', 'https://medlineplus.gov/genetics/condition/galactosemia/', 'Galactosemia') + '.</p>',
  'P1. 8.6 To Your Health: galactosemia "1 in every 65,000 newborn babies"',
  'MedlinePlus Genetics: "Classic galactosemia occurs in 1 in 30,000 to 60,000 newborns." 65,000 was outside that range.')
e('597139',
  'href="https://www.nass.usda.gov/publications/agcensus/2022/online-resources/county-profiles/california"',
  'href="https://www.nass.usda.gov/sites/default/files/publications/agcensus/2022/Online_Resources/County_Profiles/California/cp06107.pdf"',
  'P3 link fix (free). 8.6 Valley Connection source 2 pointed to the California index page, not the Tulare profile',
  'The Tulare County profile (cp06107) lists milk from cows $2,814,167 thousand, ranked 1 of 1,770 U.S. counties. The www.nass.usda.gov '
  'path for this PDF returned 404; the data.nass.usda.gov path is the one search indexes.')

# ===================== Chapter 9 =====================
e('597144',
  'The average daily diet should contain about 4&ndash;6 g of the essential fatty acids.</p>',
  'Adults need about 12&ndash;17 g of linoleic acid and 1.1&ndash;1.6 g of &alpha;-linolenic acid each day '
  + src('Penn State Extension', 'https://extension.psu.edu/omega-fatty-acids', 'Omega Fatty Acids', ', citing the Institute of Medicine Adequate Intakes') + '.</p>',
  'P1. 9.1 section text: "about 4-6 g of the essential fatty acids"',
  'Wrong (Ball). Penn State Extension: the Institute of Medicine "has established an adequate intake of ALA and LA at 1.1 to 1.6 grams per day" '
  'and 12 to 17 grams per day. NIH ODS (omega-3 fact sheet) gives the same ALA AIs, 1.6 g men and 1.1 g women. The ranges span women to men.')

e('597145',
  'Partially hydrogenated oils have since been phased out of U.S. processed foods.',
  'In 2015 the FDA ruled that partially hydrogenated oils are no longer &ldquo;generally recognized as safe,&rdquo; and they were phased out of U.S. foods by 2018&ndash;2021 '
  + src('U.S. Food and Drug Administration', 'https://www.fda.gov/food/food-additives-petitions/final-determination-regarding-partially-hydrogenated-oils-removing-trans-fat', 'Final Determination Regarding Partially Hydrogenated Oils') + '.',
  'P2. 9.2 section text: PHO phase-out had no source',
  'FDA page: "In 2015, FDA released its final determination that Partially Hydrogenated Oils (PHOs) are not" GRAS; compliance June 18, 2018, '
  'extended to Jan 1, 2020 (non-petitioned) and Jan 1, 2021 (petitioned uses). The Lecture Connection repeats the phase-out; not re-cited (same page).')
e('597145',
  'keep saturated fat at or below 10% of daily calories.</p>',
  'keep saturated fat at or below 10% of daily calories '
  + src('USDA and HHS', 'https://www.dietaryguidelines.gov/', 'Dietary Guidelines for Americans, 2025&ndash;2030') + '.</p>',
  'P2. 9.2 section text: "keep saturated fat at or below 10% of daily calories" had no source in the main text',
  'DGA 2025-2030 PDF (realfood.gov, linked from dietaryguidelines.gov): "In general, saturated fat consumption should not exceed 10% of total daily" calories.')
e('597145',
  'Tulare County&rsquo;s milk was worth about $2.3 billion.<sup>2</sup>',
  'Tulare County sold about $2.8 billion of milk in 2022, more than any other U.S. county.<sup>2</sup>',
  'P2. 9.2 Valley Connection: Tulare milk "about $2.3 billion" sourced only to a news site (GV Wire)',
  'The official Tulare 2024 crop report could not be reached (agcomm.tularecounty.ca.gov 403); news reports give $2.27 B for 2024, '
  'unconfirmed. Switched to the verified USDA 2022 Census figure ($2,814,167 thousand, rank 1 of 1,770 counties), which also matches '
  'Section 8.6. The year is stated so readers see why it differs from a county crop report.')
e('597145',
  '2. GV Wire, ' + a('https://gvwire.com/2025/11/04/fresno-is-nations-top-ag-county-at-9-billion-but-what-does-future-hold/', 'Fresno Is Nation&rsquo;s Top Ag County at $9 Billion') + ', 2025.',
  '2. Fresno County Department of Agriculture, '
  + a('https://www.fresnocountyca.gov/files/sharedassets/county/v/1/agricultural-commissioner/ag-crop-reports/ag-crop-and-livestock-report_2024.pdf', '2024 Annual Crop &amp; Livestock Report')
  + ', 2025; USDA National Agricultural Statistics Service, '
  + a('https://www.nass.usda.gov/sites/default/files/publications/agcensus/2022/Online_Resources/County_Profiles/California/cp06107.pdf', '2022 Census of Agriculture County Profile: Tulare County, California')
  + ', 2024.',
  'P2. 9.2 Valley Connection source 2: GV Wire (news) replaced with the primary reports',
  'Fresno County 2024 report: the link is from the county Agricultural Commissioner page. The PDF is over the fetch size limit; '
  'almonds = $1.45 B and top commodity were confirmed through Agri-Pulse and The Business Journal coverage of this report. '
  'Tulare: see the previous edit. One numbered source keeps the list numbering.')
e('597145',
  'href="https://www.webpages.uidaho.edu/ruminant_nutrition/Optional%20Reading%20Materials/Palmitic%20and%20stearic%20acid%20metabolism%20in%20lactating%20dairy%20cows.pdf"',
  'href="https://doi.org/10.3168/jds.2014-7919"',
  'P1. 9.2 Valley Connection source 5: broken link (uidaho.edu now redirects to a 404 page)',
  'Same paper via its DOI: Loften JR et al., J Dairy Sci 97(8):4661-4674 (2014). The abstract names palmitic acid as the fatty acid present in '
  'the largest amount in milk fat; the "oleic second" part was seen only in a truncated abstract snippet.')

e('597146',
  'The risk is highest in babies born before about 28 weeks of gestation and is still significant up to about 34 weeks.',
  'The earlier a baby is born, the higher the risk; the problem is uncommon in babies born at 39 weeks or later '
  + src('MedlinePlus', 'https://medlineplus.gov/ency/article/001563.htm', 'Neonatal Respiratory Distress Syndrome') + '.',
  'P2. 9.3 IRDS: "highest before about 28 weeks ... significant up to about 34 weeks" had no source',
  'Could not source the 28/34-week cutoffs (StatPearls blocked by CAPTCHA). Rewritten to what MedlinePlus says: "The more premature the baby is, '
  'the higher the chance of RDS"; "uncommon in babies born full-term or later (39 weeks or after)". The 24-34-week steroid window stays in the Nursing box (CRICO).')

e('597149',
  'triglycerides</strong> (the lab name for triacylglycerols) below 150. Many labs',
  'triglycerides</strong> (the lab name for triacylglycerols) below 150 '
  + src('MedlinePlus', 'https://medlineplus.gov/cholesterollevelswhatyouneedtoknow.html', 'Cholesterol Levels: What You Need to Know') + '. Many labs',
  'P2. 9.6 Lecture Connection: lipid-panel targets had no source',
  'MedlinePlus (adults 20+): total under 200; LDL under 100; HDL 60 or higher is best, under 40 (men) / under 50 (women) is low; triglycerides under 150. Matches every number.')
e('597149',
  ' A long-term investigation by the National Institutes of Health showed that among men ages 30 to 49, the incidence of heart disease was five times greater for those whose cholesterol levels were above 260 mg/100 mL of serum than for those with cholesterol levels of 200 mg/100 mL or less.',
  '',
  'P2. 9.6 section text: NIH "five times greater" statistic (men 30-49, >260 vs <=200)',
  'DELETED: no source with this figure could be found (searched Framingham/NHLBI and Castelli 1986). The paragraph still says that elevated '
  'cholesterol is associated with heart disease risk, and the lipid targets are now sourced in the Lecture Connection.')
e('597149',
  'Young adults average about 170 mg of cholesterol per 100 mL of blood, whereas males at age 55 may have cholesterol levels at 250 mg/100 mL or higher because the rate of cholesterol breakdown decreases with age. Females tend to have lower blood cholesterol levels than males.</p>',
  'It tends to rise in middle age: in 2021&ndash;2023, about 11% of U.S. adults had high total cholesterol (240 mg/dL or more), '
  'the share was highest in men aged 40&ndash;59 (18%), and men and women did not differ overall '
  + src('CDC National Center for Health Statistics', 'https://www.cdc.gov/nchs/products/databriefs/db515.htm', 'Total and HDL Cholesterol in Adults, 2021&ndash;2023') + '.</p>',
  'P2. 9.6 section text: outdated averages (170 young adults; 250 men at 55; "females tend to have lower")',
  'NCHS Data Brief 515 (Nov 2024): high total cholesterol 11.3% of adults; men 10.6% vs women 11.9% (not significantly different); men 40-59: 18.3%. '
  'The old means and the "breakdown decreases with age" reason had no source, and "females lower" is not supported by current data, so they were replaced.')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for p, (orig, new) in pages.items():
        assert orig != new, p
        open(os.path.join(OUT, p + '.html'), 'w', encoding='utf-8').write(new)
    json.dump(edits, open(os.path.join(OUT, 'edits.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('OK: %d edits on %d pages -> %s' % (len(edits), len(pages), OUT))
    for x in edits:
        print(' ', x['page'], x['note'][:90])
