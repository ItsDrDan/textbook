# Source-audit fixes, group t1_front_ch1-3 (front matter + Chapters 1-3): all P1 and P2 items.
# Uses the caller's helper e(pageid, old, new, note, why). Run from the textbook-git root.
# Each source below was re-fetched on 2026-11-18 and states what the sentence says.

A = '<a style="text-decoration:underline" href="%s" rel="noopener" target="_blank">%s</a>'
def src(publisher, url, title):
    return '(Source: %s, %s)' % (publisher, A % (url, title))

FDA = src('U.S. FDA', 'https://www.fda.gov/food/food-additives-petitions/trans-fat', 'Trans Fat')
CDC_GUM = src('CDC', 'https://www.cdc.gov/tobacco/campaign/tips/diseases/periodontal-gum-disease.html', 'Smoking, Gum Disease, and Tooth Loss')
MLP_O2 = src('MedlinePlus', 'https://medlineplus.gov/ency/patientinstructions/000049.htm', 'Oxygen safety')

# ---------------------------------------------------------------- P1 2.8 (597072): dead NASA Ozone Watch link
e(597072,
'href="http://ozonewatch.gsfc.nasa.gov/daily.php?date=2006-09-24"',
'href="https://ozonewatch.gsfc.nasa.gov/Scripts/big_image.php?date=2006-09-24&amp;hem=S"',
"P1 2.8 CFC figure credit: Ozone Watch link moved",
"Old daily.php URL returns HTTP 404. New URL loads 'Ozone Hole Watch: Southern ozone map for 24 September 2006'.")

# ---------------------------------------------------------------- P1 1.8 (597061): gecko study year
e(597061,
'In 2000, Kellar Autumn, who leads a multi-institutional gecko research team, found that geckos adhered equally well to both polar silicon dioxide and nonpolar gallium arsenide.',
'In 2002, Kellar Autumn, who leads a multi-institutional gecko research team, found that geckos adhered equally well to both polar silicon dioxide and nonpolar gallium arsenide '
+ src('Autumn et al.', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC129431/', '<em>PNAS</em>, 2002') + '.',
"P1 1.8 gecko box: 2000 -> 2002, cited",
"The SiO2 vs GaAs result is Autumn K. et al., Evidence for van der Waals adhesion in gecko setae, PNAS 99:12252 (2002): 'Adhesion to hydrophilic and hydrophobic polarizable surfaces was similar.' The 2000 Nature paper measured single-seta force. Error inherited from OpenStax Chemistry 2e 10.1.")

# ---------------------------------------------------------------- P2 3.3 (597080): tomato ethylene number
e(597080,
'Fruit processors artificially introduce ethylene to hasten the ripening process; exposure to as little as 0.1 mg of ethylene for 24 h can ripen 1 kg of tomatoes.',
'Fruit processors artificially introduce ethylene to hasten the ripening process; ripening rooms hold fruit such as tomatoes and bananas in about 100 to 150 ppm ethylene '
+ src('M. E. Saltveit, USDA Agriculture Handbook 66', 'https://webarchive.library.unt.edu/eot2008/20090305020046id_/http://www.ba.ars.usda.gov/hb66/020ethylene.pdf', 'Ethylene Effects') + '.',
"P2 3.3 Environmental Note: unsourced '0.1 mg ethylene ripens 1 kg tomatoes' replaced with the sourced commercial ripening concentration",
"No primary source found for the 0.1 mg/1 kg figure (rewritten). Saltveit: fruit treated with C2H4 before sale 'include avocados, bananas, honeydew melons, lemons, oranges and tomatoes. An effective atmosphere of 100 to 150 uL L-1 C2H4 in air'. Same source as 3.4 Valley Connection note 1.")

# ---------------------------------------------------------------- P2 3.8 (597085): benzo[a]pyrene dose sentence
e(597085,
'Only a few milligrams of benzo[a]pyrene per kilogram of body weight are required to induce cancer in experimental animals.',
'The U.S. EPA classifies benzo[a]pyrene as carcinogenic to humans '
+ src('U.S. EPA', 'https://iris.epa.gov/ChemicalLanding/&amp;substance_nmbr=136', 'IRIS: Benzo[a]pyrene, 2017') + '.',
"P2 3.8 PAHs and Cancer: unsourced animal-dose sentence replaced with EPA classification",
"No source found for 'a few milligrams per kilogram' (rewritten). EPA IRIS (updated 01/19/2017): cancer descriptor 'Carcinogenic to humans'.")

# ---------------------------------------------------------------- P2 3.8 (597085): smoking, oral cancer, periodontitis
e(597085,
'which is why smokers have a much higher rate of oral squamous cell carcinoma and of <em>periodontitis</em> (infection and bone loss around the teeth that follows untreated <em>gingivitis</em>).',
'which is why smokers have a much higher rate of oral squamous cell carcinoma '
+ src('National Cancer Institute', 'https://www.cancer.gov/types/head-and-neck/patient/oral-prevention-pdq', 'Oral Cavity Cancer Prevention')
+ ' and of <em>periodontitis</em> (infection and bone loss around the teeth that follows untreated <em>gingivitis</em>) ' + CDC_GUM + '.',
"P2 3.8 Clinical Connection: Dental Hygiene: smoking claims cited",
"NCI PDQ: 'Using tobacco is the most common cause of oral cavity ... cancers.' CDC: smokers have 'twice the risk for gum disease compared with a nonsmoker.'")

# ---------------------------------------------------------------- P2 2.6 (597070): oil slick area
e(597070,
'One liter of oil can create a slick 2.5 hectares (6.3 acres) in size.',
'Spread to the thinnest visible sheen, about 0.04 &micro;m thick, one liter of oil can cover about 2.5 hectares (6.2 acres) '
+ src('A. Lewis for the Bonn Agreement', 'https://www.bonnagreement.org/site/assets/files/3952/current-status-report-final-19jan07.pdf', 'Current Status of the Bonn Agreement Oil Appearance Code, 2007') + '.',
"P2 2.6 Figure 1 caption: oil-slick area sourced; acres corrected 6.3 -> 6.2",
"Bonn Agreement Oil Appearance Code 1 'Sheen' is 0.04 to 0.30 um, 40-300 litres per km2; 'oil layers below 0.04 microns ... cannot be easily detected'. 1 L / 40 L per km2 = 0.025 km2 = 2.5 ha. 2.5 ha x 2.471 = 6.18 acres, so 6.3 was a small conversion error.")

# ---------------------------------------------------------------- P2 3.7 (597084): benzene and leukemia
e(597084,
'in which there is a decrease in the numbers of both the red and white blood cells.</p>',
'in which there is a decrease in the numbers of both the red and white blood cells. Long-term exposure can also cause leukemia, and benzene is a known human carcinogen '
+ src('ATSDR', 'https://wwwn.cdc.gov/TSP/ToxFAQs/ToxFAQsDetails.aspx?faqid=38&amp;toxid=14', 'ToxFAQs: Benzene') + '.</p>',
"P2 3.7 Benzene and Us: leukemia and carcinogen classification added, cited",
"ATSDR ToxFAQs: reduced red and white cells 'lead to anemia'; 'Long-term exposure may also cause leukemia' (acute myelogenous leukemia); DHHS and EPA: 'known human carcinogen'. The box had no source and omitted the best-known long-term effect.")

# ---------------------------------------------------------------- P2 Ch 1 opener (597039): Rosa's chart
e(597039,
'<td data-th="Typical goal or reference range">Under 100 mg/dL (lower for some patients)</td>',
'<td data-th="Typical goal or reference range">Under 100 mg/dL; under 70 for adults 40&ndash;75 with diabetes and other heart risk factors</td>',
"P2 Ch 1 Rosa's chart: LDL goal updated to the ADA 2026 goal",
"ADA Standards of Care 2026, Sec. 10, Rec. 10.20 (Grade A): for people with diabetes aged 40-75 at higher cardiovascular risk (one or more additional ASCVD risk factors), high-intensity statin with 'an LDL cholesterol goal of <70 mg/dL'. Rosa (52, low HDL, high TG, BP 138/86) is in that group. 'Under 100' was the older general goal.")

e(597039,
'</tbody></table>',
'</tbody></table>\n<p style="font-size:0.9em;">Goals and ranges: A1c '
+ src('American Diabetes Association', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12690178/', 'Standards of Care in Diabetes&mdash;2026, Section 6') + '; LDL and blood pressure '
+ src('American Diabetes Association', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12690187/', 'Standards of Care in Diabetes&mdash;2026, Section 10') + '; fasting glucose '
+ src('MedlinePlus', 'https://medlineplus.gov/ency/article/003482.htm', 'Blood sugar test') + '; HDL and triglycerides '
+ src('MedlinePlus', 'https://medlineplus.gov/cholesterollevelswhatyouneedtoknow.html', 'Cholesterol levels') + '.</p>',
"P2 Ch 1 Rosa's chart: source line added under the table",
"ADA 2026 Sec. 6 Rec. 6.3a: 'An A1C goal of <7% ... is appropriate for many nonpregnant adults'. Sec. 10 Rec. 10.4: BP goal <130/80; Rec. 10.20: LDL <70. MedlinePlus 003482: fasting '70 to 99 mg/dL' normal. MedlinePlus Cholesterol levels: HDL in women 'less than 50 mg/dL are considered low'; 'A normal triglyceride level is below 150 mg/dL'.")

# ---------------------------------------------------------------- P2 Ch 2 opener (597040) + 2.10 guide (597074): oxygen and petroleum jelly
e(597040,
'to use a water-based moisturizer instead.',
'to use a water-based moisturizer instead ' + MLP_O2 + '.',
"P2 Ch 2 Rosa's Story: home-oxygen petroleum-jelly warning cited",
"MedlinePlus Oxygen safety: 'Do not use Vaseline or other petroleum-based creams and lotions on your face or upper part of your body'; water-based products such as K-Y Jelly are safe.")

e(597074,
'petroleum-based products on the face are discouraged as a fire risk, and water-based products are used instead.',
'petroleum-based products on the face are discouraged as a fire risk, and water-based products are used instead ' + MLP_O2 + '.',
"P2 2.10 Chapter Guide safety note: home-oxygen petroleum warning cited",
"Same MedlinePlus Oxygen safety page.")

# ---------------------------------------------------------------- P2 Ch 3 opener (597041): FDA and smoking
e(597041,
'the FDA has since removed partially hydrogenated oils from the U.S. food supply, but',
'the FDA has since removed partially hydrogenated oils from the U.S. food supply ' + FDA + ', but',
"P2 Ch 3 Rosa's Story: FDA PHO removal cited",
"FDA Trans Fat: in 2015 FDA determined PHOs, 'then the major source of artificial trans fat in the food supply', are no longer GRAS; most uses ended June 18, 2018; final compliance Jan 1, 2021.")

e(597041,
'and smoking is one of the strongest risk factors for gum disease.</p>',
'and smokers have twice the risk of gum disease that nonsmokers have ' + CDC_GUM + '.</p>',
"P2 Ch 3 Rosa's Story: smoking/gum disease reworded to the CDC figure and cited",
"CDC: 'You have twice the risk for gum disease compared with a nonsmoker.' 'One of the strongest risk factors' is not stated by the source, so the sentence now gives the source's number.")

# ---------------------------------------------------------------- P2 1.6 (597059) and 3.2 (597079): FDA PHO removal
e(597059,
'has removed partially hydrogenated oils from the US food supply.</p>',
'has removed partially hydrogenated oils from the US food supply ' + FDA + '.</p>',
"P2 1.6 To Your Health: FDA PHO removal cited",
"Same FDA Trans Fat page; it also supports 'most of the trans fat ... once came from partially hydrogenated oils' earlier in the paragraph.")

e(597079,
'Partially hydrogenated oils were removed from the U.S. food supply for this reason.',
'Partially hydrogenated oils were removed from the U.S. food supply for this reason ' + FDA + '.',
"P2 3.2 Clinical Connection: Nursing: FDA PHO removal cited",
"Same FDA Trans Fat page.")

