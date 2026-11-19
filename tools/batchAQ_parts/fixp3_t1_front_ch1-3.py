# Round 2 (P3 polish), group t1_front_ch1-3. Uses the caller's helper e(pageid, old, new, note, why).
# Run from the textbook-git root against the current pages/live (after batch AP). Sources re-fetched 2026-11-18.

A = '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>'
def src(publisher, url, title):
    return '(Source: %s, %s)' % (publisher, A % (url, title))

# ---------------------------------------------------------------- 1.8 (597061)
e(597061,
'a chain-reaction pileup closed Highway 99 near Earlimart and sent people to the hospital.',
'a chain-reaction pileup closed Highway 99 in Tulare County and sent people to the hospital.',
"P3 1.8 Valley Connection: 'near Earlimart' -> 'in Tulare County' to match cited note 6",
"ABC30 (note 6) places the crash on Highway 99 in Tulare County 'near Avenue 24' and never names Earlimart.")

e(597061,
'Acetaminophen is the most widely used medicine for pain and fever.',
'Acetaminophen is one of the most widely used medicines for pain and fever.',
"P3 1.8 Molecule in the Clinic: superlative softened",
"'The most widely used' is a contestable superlative; StatPearls says 'one of the most widely used'. With the softer wording no citation is needed (NCBI Bookshelf blocked automated fetch, so none added).")

e(597061,
'Pure alcohol evaporates too fast to do this well, which is one reason swabs are 70% rather than 100%.',
'Pure alcohol evaporates too fast, and without water it denatures microbial proteins more slowly, so swabs are 70% rather than 100% '
+ src('CDC', 'https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html', 'Chemical Disinfectants') + '.',
"P3 1.8 Clinical Connection: Nursing: second (main) reason for 70% added, cited",
"CDC Guideline for Disinfection: optimum bactericidal concentration '60%-90% solutions in water'; absolute alcohol is less bactericidal 'because proteins are denatured more quickly in the presence of water'.")

# ---------------------------------------------------------------- 1.4 (597057)
e(597057,
'he was awarded the 1954 Nobel Prize in Chemistry for his work on protein structure.',
'he was awarded the 1954 Nobel Prize in Chemistry for his research on the chemical bond and its use in working out the structures of complex substances such as proteins '
+ src('Royal Swedish Academy of Sciences', 'https://kva.se/en/prize-laureate/linus-carl-pauling-2', 'Linus Carl Pauling') + '.',
"P3 1.4 Looking Closer: Pauling 1954 prize description matched to the official citation, cited",
"Prize motivation: 'for his research into the nature of the chemical bond and its application to the elucidation of the structure of complex substances' (kva.se; nobelprize.org refused fetch).")

# ---------------------------------------------------------------- 1.6 (597059)
e(597059,
'MyPlate recommends minimizing daily intake of sugars, the &quot;bad fats&quot;, trans and saturated fat, and sodium. &quot;Good fats&quot;, unsaturated fats or oils, are not considered a food group but do contain essential nutrients and therefore are included as part of a healthy eating pattern.',
'The new guidelines still say saturated fat should not exceed 10% of daily calories, advise against added sugars, set sodium below 2,300 mg a day for people 14 and older, and favor oils with essential fatty acids, such as olive oil '
+ src('USDA and HHS', 'https://realfood.gov/documents/DGA.pdf', '<em>Dietary Guidelines for Americans, 2025&ndash;2030</em>') + '.',
"P3 1.6 To Your Health: superseded MyPlate advice replaced with the 2025-2030 Guidelines' own fat, sugar and sodium advice, cited",
"DGA 2025-2030 PDF: 'saturated fat consumption should not exceed 10% of total daily calories'; 'no amount of added sugars ... is recommended'; 'ages 14 and above, should consume less than 2,300 mg per day of sodium'; 'prioritize oils with essential fatty acids, such as olive oil'. The old sentences described MyPlate, which the paragraph says has been replaced.")

# ---------------------------------------------------------------- 2.1 (597065)
e(597065,
'of tens of millions of compounds that have been characterized, the overwhelming majority are carbon compounds.',
'of the more than 300 million substances registered by Chemical Abstracts Service, the overwhelming majority are carbon compounds '
+ src('CAS', 'https://www.cas.org/content', 'CAS Content') + '.',
"P3 2.1 text: outdated 'tens of millions' updated to the CAS figure, cited",
"cas.org/content: CAS REGISTRY, 'the authoritative database of chemical substances (300M+)'.")

# ---------------------------------------------------------------- 2.7 (597071)
e(597071,
'can cause carbon monoxide poisoning, which still kills people in the United States every year, most often in winter.',
'can cause carbon monoxide poisoning, which still kills hundreds of people in the United States every year, most often in winter '
+ src('CDC', 'https://www.cdc.gov/mmwr/volumes/66/wr/mm6608a9.htm', '<em>MMWR</em>, 2017') + '.',
"P3 2.7 text: CO deaths given a size and cited",
"CDC MMWR 66(8): 2,244 unintentional CO deaths in 2010-2015, 393 in 2015; highest numbers each year in winter months.")

# ---------------------------------------------------------------- 2.8 (597072)
e(597072,
'They occur mainly over Antarctica from late August through early October and fill in about mid-November.',
'They occur mainly over Antarctica, grow from late August through early October, and usually close in December '
+ src('Copernicus Atmosphere Monitoring Service', 'https://atmosphere.copernicus.eu/smallest-and-shortest-lived-ozone-hole-5-years-closes', 'ozone hole report, 2025') + '.',
"P3 2.8 CFC figure caption: ozone-hole closing time corrected, cited",
"CAMS 2025: the hole closed on 1 December, 'one of the earliest closures in the past four decades'; 2020 closed 28 December (latest on record). So 'mid-November' was too early for a typical year.")

e(597072,
'Bromine-containing compounds are widely used in fire extinguishers and as fire retardants on clothing and other materials. Because they too',
'Bromine-containing halons were once widely used in fire extinguishers, but U.S. production ended in 1994 because they destroy ozone; only recycled halons are used today '
+ src('U.S. EPA', 'https://www.epa.gov/ozone-layer-protection/halons-program', 'Halons Program')
+ '. Bromine compounds are also used as flame retardants. Because they too',
"P3 2.8 To Your Health: outdated 'widely used in fire extinguishers' corrected, cited",
"EPA: 'On January 1, 1994, production and import of virgin halons were phased out in the United States'; 'recycled halons are the only supply'. The unsourced 'on clothing' detail was dropped (rewritten to a general statement).")

e(597072,
'and halothane, a bromo-chloro-fluoro haloalkane adopted in 1956, was later linked to a rare hepatitis.',
'and halothane, a bromo-chloro-fluoro haloalkane adopted in 1956, was later linked to a rare hepatitis '
+ src('OpenAnesthesia', 'https://www.openanesthesia.org/keywords/halothane/', 'Halothane') + '.',
"P3 2.8 Clinical Connection: Nursing: halothane history date cited",
"OpenAnesthesia (IARS), Halothane: 'Halothane entered clinical practice in 1956'; 'Halothane hepatitis is a major limiting adverse effect'. Chloroform 1847 left uncited (Wood Library-Museum refused fetch; the date is correct).")
