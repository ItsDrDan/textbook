# Fix notes: t1_front_ch1-3 (P1 + P2 from srcaudit_t1_front_ch1-3.md)

Script: `fix_t1_front_ch1-3.py` (uses the caller's `e()`). It has 15 e() calls on 12 pages. All 15 were test-run with a stub against the current `pages/live/*.html`. Each `old` occurs exactly once, including the later edits on the same page. Every source was re-fetched on 2026-11-18 and states what the sentence says.

| # | P | Page | What changed | Source |
|---|---|---|---|---|
| 1 | P1 | 597072 (2.8) | Dead NASA Ozone Watch link (`daily.php`, 404) replaced with the working map URL | ozonewatch.gsfc.nasa.gov/Scripts/big_image.php?date=2006-09-24&hem=S |
| 2 | P1 | 597061 (1.8) | Gecko box: "In 2000" → "In 2002", with citation | Autumn et al., PNAS 99:12252 (2002), PMC129431 |
| 3 | P2 | 597080 (3.3) | Deleted the unsourced "0.1 mg ethylene for 24 h ripens 1 kg tomatoes". Replaced it with the sourced commercial concentration: ripening rooms hold tomatoes and bananas in about 100–150 ppm. | Saltveit, USDA AH-66, *Ethylene Effects* (same source as 3.4 note 1) |
| 4 | P2 | 597085 (3.8) | Deleted the unsourced "few milligrams per kilogram… experimental animals". Replaced it with "The U.S. EPA classifies benzo[a]pyrene as carcinogenic to humans." | EPA IRIS Benzo[a]pyrene (2017) |
| 5 | P2 | 597085 (3.8 Dental Hygiene) | Smoking claims cited: NCI after oral cancer, CDC after periodontitis | NCI PDQ Oral Cavity Cancer Prevention; CDC Smoking, Gum Disease, and Tooth Loss |
| 6 | P2 | 597070 (2.6 Fig. 1 caption) | Oil-slick claim now says it is the thinnest visible sheen (0.04 µm), with citation. **Acres fixed: 6.3 → 6.2** (2.5 ha = 6.18 acres). | A. Lewis, *Current Status of the BAOAC*, Bonn Agreement, 2007 (Code 1 sheen 0.04–0.30 µm = 40–300 L/km²) |
| 7 | P2 | 597084 (3.7) | Added: long-term exposure can also cause leukemia; benzene is a known human carcinogen | ATSDR ToxFAQs: Benzene |
| 8 | P2 | 597039 (Ch 1 Rosa's chart) | LDL goal "Under 100 mg/dL (lower for some patients)" → "Under 70 mg/dL for adults 40–75 with diabetes and other heart risk factors" | ADA Standards of Care 2026, Sec. 10, Rec. 10.20 (PMC12690187) |
| 9 | P2 | 597039 | One small source line under the table: A1c (ADA Sec. 6, Rec. 6.3a), LDL and BP (ADA Sec. 10), fasting glucose 70–99 (MedlinePlus Blood sugar test), HDL and TG (MedlinePlus Cholesterol levels) | as listed |
| 10 | P2 | 597040 (Ch 2 Rosa) | Petroleum jelly / home oxygen warning cited | MedlinePlus, Oxygen safety |
| 11 | P2 | 597074 (2.10 guide) | Same claim, same citation | MedlinePlus, Oxygen safety |
| 12 | P2 | 597041 (Ch 3 Rosa) | FDA removal of partially hydrogenated oils cited | FDA, Trans Fat |
| 13 | P2 | 597041 (Ch 3 Rosa) | "smoking is one of the strongest risk factors for gum disease" → "smokers have twice the risk of gum disease that nonsmokers have", cited. The source does not say "strongest". | CDC, Smoking, Gum Disease, and Tooth Loss |
| 14 | P2 | 597059 (1.6) | FDA PHO removal cited | FDA, Trans Fat |
| 15 | P2 | 597079 (3.2) | FDA PHO removal cited | FDA, Trans Fat |

## Format choices
- None of the edited claims sits inside a box that has a `Sources:` list, so every citation is the inline `(Source: Publisher, <a …>Title</a>)` form. This covers the To Your Health and Looking Closer boxes, figure captions, Rosa's Story and the guides.
- The Rosa chart gets one source line under the table rather than five citations inside table cells.

## Same-number check across all pages
- "2.5 hectares / 6.3 acres", "0.1 mg of ethylene", "milligrams of benzo[a]pyrene", "In 2000, Kellar" and "strongest risk factors for gum" each appear only on the page edited.
- An LDL "under 100" goal appears only on 597039.
- The group's Practice Problems pages repeat none of these numbers.
- No other chapter needs a matching change.

## Skipped
- **All P3 items** (per the brief), including:
  - ozone-hole close date
  - halons
  - Pauling Nobel citation
  - 70% alcohol reason
  - acetaminophen superlative
  - CAS count
  - CO deaths and CO–Hb ×200
  - halothane/chloroform dates
  - gas-density conditions
  - NaCl bp
  - Albany, NOAA and ABC30 source swaps
- **Not cited:** 597075 Problem 2.67 ("Hospital policy calls for a water-based product") is a problem stem that matches the cited claim on 597040 and 597074. I left it alone to avoid over-citing.
- **Not cited:** 597085 also says "Smoking also narrows gingival blood vessels, so the bleeding … may be masked." The audit did not flag it and I did not source it.

## For the author to decide
- **Rosa's LDL goal (597039).** I used the ADA 2026 "<70 mg/dL" goal for higher-risk adults 40–75 (Rec. 10.20), because Rosa has added risk factors (low HDL, high TG, BP 138/86). If you would rather keep a general-population number, MedlinePlus still lists "less than 100 mg/dL" as the general healthy level. Either way the cell now matches a source.
- **597085 benzo[a]pyrene.** The new sentence names EPA only. IARC also lists it as Group 1. I did not re-fetch the IARC monograph page, so I left IARC out.
