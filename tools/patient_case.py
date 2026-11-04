"""Rosa's Story: a running patient case, one part per chapter, inserted into each Chapter Guide before Practice.
Fictional patient. Written for this book by Dr. Dan (Daniel Kwasniewski), Fresno City College, CC BY-NC-SA 4.0."""
import re, os
HERE = os.path.dirname(os.path.abspath(__file__))
ID = {}
for l in open(os.path.join(HERE, 'section_ids.txt')):
    m = re.match(r'(\d+) (\d+\.\d+):', l)
    if m: ID[m.group(2)] = int(m.group(1))
ID.update({'4.10': 597099, '7.11': 597131, '11.7': 597172, '12.9': 597183, '13.7': 597194, '13.8': 597195, '13.9': 597196,
           '13.10': 597197, '14.5': 597204, '15.6': 597212, '15.11': 597217})

def S(n):
    return f'<a href="/@go/page/{ID[n]}">Section {n}</a>'

COLOR = '#2d8a6a'

CHART = """<table class="mt-responsive-table">
<caption>Rosa&rsquo;s chart at the start of the story (fictional patient)</caption>
<thead><tr><th scope="col">Item</th><th scope="col">Rosa</th><th scope="col">Typical goal or reference range</th></tr></thead>
<tbody>
<tr><td data-th="Item">Hemoglobin A1c</td><td data-th="Rosa">8.4%</td><td data-th="Typical goal or reference range">Under 7% for many adults with diabetes</td></tr>
<tr><td data-th="Item">Fasting blood glucose</td><td data-th="Rosa">168 mg/dL</td><td data-th="Typical goal or reference range">70&ndash;99 mg/dL without diabetes</td></tr>
<tr><td data-th="Item">LDL cholesterol</td><td data-th="Rosa">142 mg/dL</td><td data-th="Typical goal or reference range">Under 100 mg/dL (lower for some patients)</td></tr>
<tr><td data-th="Item">HDL cholesterol</td><td data-th="Rosa">38 mg/dL</td><td data-th="Typical goal or reference range">50 mg/dL or higher for women</td></tr>
<tr><td data-th="Item">Triglycerides</td><td data-th="Rosa">230 mg/dL</td><td data-th="Typical goal or reference range">Under 150 mg/dL</td></tr>
<tr><td data-th="Item">Blood pressure</td><td data-th="Rosa">138/86 mm Hg</td><td data-th="Typical goal or reference range">Under 130/80 mm Hg for many adults with diabetes</td></tr>
<tr><td data-th="Item">Medicines</td><td data-th="Rosa">Metformin, atorvastatin, lisinopril</td><td data-th="Typical goal or reference range">&mdash;</td></tr>
<tr><td data-th="Item">Dental findings</td><td data-th="Rosa">Bleeding gums, bad breath, dry mouth, moderate periodontitis</td><td data-th="Typical goal or reference range">&mdash;</td></tr>
</tbody></table>"""

# Each part: (title, scenario_html, [(question_html, answer_html), ...], [sections])
CASE = {
1: ("Meet Rosa",
 f"""<p>Rosa Delgado is 52 and manages a school cafeteria in Fresno County. Three years ago a routine blood test showed she has <strong>type 2 diabetes</strong>. Today she has two appointments: a check-up with her nurse practitioner in the morning and a cleaning with the dental hygienist in the afternoon. You will follow Rosa through every chapter of this book, because nearly every topic in CHEM 3B shows up somewhere in her care.</p>
{CHART}
<p>At the pharmacy, Rosa picks up her three medicines. The pharmacist reminds her to take <strong>metformin</strong> with meals and a full glass of water. Metformin is a small molecule with several N&ndash;H bonds and no large hydrocarbon part, and it dissolves easily in water. <strong>Atorvastatin</strong>, her cholesterol medicine, is a much larger molecule built mostly from carbon&ndash;carbon and carbon&ndash;hydrogen bonds, with only a few polar groups.</p>""",
 [("Metformin has several polar N&ndash;H bonds. Explain, in terms of intermolecular forces, why it dissolves so easily in water.",
   "The N&ndash;H bonds are polar (N is more electronegative than H), and the nitrogen atoms have lone pairs. Metformin can hydrogen bond with water both as a donor (its N&ndash;H hydrogens) and as an acceptor (its N lone pairs), so water molecules surround it readily. Polar dissolves polar: like dissolves like."),
  ("What is the strongest intermolecular force between the water molecules in Rosa&rsquo;s glass?",
   "Hydrogen bonding: the H of one water molecule (bonded to O) is attracted to a lone pair on the O of a neighboring water molecule."),
  ("Atorvastatin is mostly nonpolar C&ndash;C and C&ndash;H bonds. Would you expect it to be more soluble in water or in a fat-like (nonpolar) environment? Why?",
   "In a nonpolar environment. Its large nonpolar regions interact through London dispersion forces, which match a fat-like environment better than water&rsquo;s hydrogen-bonding network. Even sold as a calcium salt, atorvastatin is only slightly soluble in water, and it moves easily into cell membranes.")],
 ['1.4', '1.5', '1.8']),
2: ("Dry lips and a gas stove",
 """<p>Diabetes often leaves the mouth dry, and Rosa&rsquo;s lips are cracked. Before the cleaning, the hygienist coats them with <strong>petroleum jelly</strong> (petrolatum), a mixture of large alkanes with roughly 25 or more carbon atoms. Rosa jokes that her lips now feel &ldquo;waterproof.&rdquo;</p>
<p>That evening, Rosa&rsquo;s mother, who lives with her, uses home oxygen through a nasal cannula. Her home-health nurse has warned the family never to use petroleum jelly on the mother&rsquo;s nose or lips and to use a water-based moisturizer instead. In the kitchen, Rosa cooks dinner on a gas stove that burns <strong>methane</strong>, and a carbon monoxide detector hangs on the wall.</p>""",
 [("Why doesn&rsquo;t saliva wash the petroleum jelly off Rosa&rsquo;s lips?",
   "Petrolatum is made of nonpolar alkanes. They attract one another only through London dispersion forces and cannot hydrogen bond with water, so they do not dissolve in saliva. That is exactly why it works as a moisture barrier."),
  ("Why is a petroleum-based product a hazard for a patient on oxygen?",
   "Alkanes are fuels. Combustion needs fuel and oxygen, and a cannula raises the oxygen concentration right at the nose and lips. A spark or flame can ignite the petroleum product much more easily there. Water-based products are not fuels, so they are used instead."),
  ("Write the balanced equation for the complete combustion of methane. What dangerous product forms if the stove burns with too little oxygen?",
   "CH<sub>4</sub> + 2 O<sub>2</sub> &rarr; CO<sub>2</sub> + 2 H<sub>2</sub>O. With too little oxygen, incomplete combustion produces carbon monoxide, CO, which binds hemoglobin far more tightly than O<sub>2</sub> does. Hence the detector.")],
 ['2.6', '2.7']),
3: ("Reading the food label",
 """<p>At her diabetes class, a dietitian shows Rosa how to read food labels. She explains that for decades many shortenings and margarines were made by <strong>partial hydrogenation</strong>: hydrogen gas was added across some of the C=C double bonds of a liquid vegetable oil to make it more solid. The process also turned some of the remaining cis double bonds into <strong>trans</strong> double bonds. Trans fats raise LDL cholesterol, and the FDA has since removed partially hydrogenated oils from the U.S. food supply, but Rosa still checks the labels on imported snacks.</p>
<p>The dietitian also asks whether anyone at home smokes. Rosa&rsquo;s husband does. Tobacco smoke contains <strong>polycyclic aromatic hydrocarbons</strong> such as benzo[<em>a</em>]pyrene, and smoking is one of the strongest risk factors for gum disease.</p>""",
 [("What happens to a C=C double bond when it is hydrogenated? Name the reaction type.",
   "An H atom adds to each carbon of the double bond, converting C=C into C&ndash;C (an alkene becomes an alkane). It is an addition reaction and needs a metal catalyst such as Ni or Pt."),
  ("Why does a trans fatty acid pack more like a saturated fat than a cis fatty acid does?",
   "A cis double bond puts a bend in the chain, which keeps chains from packing closely. A trans double bond keeps the chain nearly straight, so trans chains pack tightly, like saturated chains, and the fat is more solid at room temperature."),
  ("What structural feature makes benzo[<em>a</em>]pyrene an aromatic compound?",
   "It is built from fused benzene rings whose pi electrons are delocalized around the rings. That aromatic ring system makes it a polycyclic (polynuclear) aromatic hydrocarbon; several PAHs in smoke are carcinogens.")],
 ['3.2', '3.4', '3.8']),
4: ("Bad breath and mouthwash",
 """<p>The hygienist measures deep pockets around several of Rosa&rsquo;s teeth and notices strong bad breath. She explains that the bacteria living in those pockets break down proteins and release <strong>volatile sulfur compounds</strong>, mainly hydrogen sulfide and <strong>methanethiol</strong>, CH<sub>3</sub>SH.</p>
<p>Rosa uses a strong mouthwash that contains about 20% ethanol. Because her mouth is already dry, the hygienist suggests an <strong>alcohol-free</strong> rinse instead. One rinse she recommends contains thymol, a compound with an &ndash;OH group bonded directly to a benzene ring. Another works by oxidizing sulfur compounds into products that do not smell.</p>""",
 [("Classify CH<sub>3</sub>SH and explain why such compounds are noticed at very low concentrations.",
   "It is a thiol (an &ndash;SH group on a carbon). Thiols have strong, unpleasant odors that the nose detects at extremely low concentrations, which is why a small amount of bacterial methanethiol causes noticeable bad breath."),
  ("Ethanol and thymol both have an &ndash;OH group. Which is an alcohol and which is a phenol?",
   "Ethanol, CH<sub>3</sub>CH<sub>2</sub>OH, is an alcohol: the &ndash;OH is on a saturated carbon. Thymol is a phenol: the &ndash;OH is bonded directly to an aromatic ring."),
  ("When two thiol molecules are oxidized, what kind of bond forms between them?",
   "A disulfide bond, &ndash;S&ndash;S&ndash;: 2 CH<sub>3</sub>SH &rarr; CH<sub>3</sub>S&ndash;SCH<sub>3</sub> (two hydrogens are removed, so it is an oxidation). A disulfide is only the first oxidation product; oxidizing rinses push sulfur compounds further, to odorless products, which is one way they freshen breath.")],
 ['4.5', '4.7', '4.9']),
5: ("What the A1c measures",
 """<p>Rosa asks her nurse practitioner why her A1c matters when her glucose meter readings are &ldquo;usually fine.&rdquo; The nurse explains that glucose in the blood is always switching between its ring form and a small amount of its <strong>open-chain form</strong>, which has an aldehyde group. That aldehyde can react with free amino groups on hemoglobin inside red blood cells, attaching the sugar permanently. Red blood cells live about three months, so the percentage of hemoglobin carrying glucose, the <strong>A1c</strong>, reflects average blood glucose over the past two to three months. An A1c of 8.4% corresponds to an average glucose of about 194 mg/dL.</p>
<p>Rosa&rsquo;s mother remembers checking her own urine for sugar decades ago with tablets that turned from blue to orange-red.</p>""",
 [("Is glucose an aldose or a ketose? Which carbon carries the aldehyde group in the open-chain form?",
   "An aldose (an aldohexose). Carbon 1 is the aldehyde carbon, &ndash;CHO."),
  ("The old urine tablets worked like Benedict&rsquo;s reagent. What happens to glucose and to the copper in a positive test?",
   "The aldehyde of glucose is oxidized (to a carboxylic acid group), and blue Cu<sup>2+</sup> is reduced to brick-red Cu<sub>2</sub>O. Glucose is a reducing sugar."),
  ("Open-chain D-glucose has four chiral carbons. Why does it matter to the body that glucose is chiral?",
   "Enzymes and transporters are chiral, so they fit one stereoisomer. Cells use D-glucose; its mirror image, L-glucose, is not recognized by the same transporters and enzymes.")],
 ['5.1', '5.4', '5.5']),
6: ("An aspirin burn and acid attack",
 """<p>A week before her next dental visit, a sore tooth kept Rosa awake, so she held an aspirin tablet against her gum. The hygienist finds a painful white patch there: an <strong>aspirin burn</strong>. Aspirin (acetylsalicylic acid) is an acid, and pressed against soft tissue it damages the surface cells. The hygienist reminds her that aspirin is meant to be swallowed, not placed on the gums.</p>
<p>Rosa also mentions that an old bottle of aspirin in her cupboard smells like vinegar. Meanwhile, the hygienist explains that each time Rosa sips sweetened coffee, plaque bacteria ferment the sugar into <strong>lactic acid</strong>, and the pH at the tooth surface can drop below about 5.5, the point at which enamel starts to dissolve.</p>""",
 [("Aspirin contains two of this chapter&rsquo;s functional groups. Name them.",
   "A carboxylic acid group (&ndash;COOH) and an ester group (the acetyl group joined to the ring through an oxygen, &ndash;O&ndash;CO&ndash;CH<sub>3</sub>)."),
  ("Why does old aspirin smell like vinegar? Name the reaction.",
   "Moisture slowly hydrolyzes the ester. Ester hydrolysis splits aspirin into salicylic acid and acetic acid, and acetic acid is the acid in vinegar."),
  ("Lactic acid is a weak acid. What does it form when it gives up H<sup>+</sup> at the tooth surface, and why does the extra H<sup>+</sup> matter?",
   "It forms the lactate ion (a carboxylate ion). The released H<sup>+</sup> lowers the pH; below about 5.5 the hydroxyapatite in enamel begins to dissolve (demineralization), which starts a cavity.")],
 ['6.4', '6.8']),
7: ("Numbing for a deep cleaning",
 """<p>Rosa returns for <strong>scaling and root planing</strong>, a deep cleaning below the gum line. The hygienist numbs the area with <strong>lidocaine with epinephrine</strong>. Lidocaine contains an amide group and a tertiary amine nitrogen, and it is supplied as <strong>lidocaine hydrochloride</strong>, the ammonium salt. Rosa&rsquo;s metformin is also sold as a hydrochloride salt.</p>
<p>One area near a badly inflamed pocket stays sensitive, so the hygienist waits and adds a little more anesthetic. She explains that inflamed tissue is more acidic than healthy tissue, and local anesthetics often work less well there.</p>""",
 [("Why are lidocaine and metformin sold as hydrochloride salts?",
   "The amine reacts with HCl to form an ammonium salt (R<sub>3</sub>NH<sup>+</sup> Cl<sup>&minus;</sup>). The ionic salt dissolves well in water, so it can be made into an injectable solution or a tablet that dissolves readily, and it is more stable on the shelf."),
  ("Lidocaine is called an &ldquo;amide-type&rdquo; local anesthetic. What atoms make up an amide group?",
   "A carbonyl carbon bonded to a nitrogen: &ndash;CO&ndash;N&ndash;. Amide-type local anesthetics are broken down mainly in the liver."),
  ("To block a nerve, the uncharged amine form must cross the nerve cell membrane. Use acid&ndash;base reasoning to explain why lidocaine works poorly in acidic, inflamed tissue.",
   "In acidic tissue there is extra H<sup>+</sup>, so more of the amine is protonated as the charged ammonium ion. Charged ions cross the nonpolar membrane poorly, so less anesthetic reaches the nerve.")],
 ['7.3', '7.4']),
8: ("Sugar, fiber and xylitol gum",
 """<p>At her next nutrition visit, Rosa learns to count carbohydrates. The dietitian points out that starch in tortillas and rice is digested to glucose, while the <strong>fiber</strong> in beans and vegetables, including cellulose, is not digested; it passes through without being absorbed, and soluble fiber slows the rise in blood glucose after a meal. Table sugar, <strong>sucrose</strong>, breaks down into glucose and fructose.</p>
<p>For her dry mouth, the hygienist suggests chewing sugar-free gum sweetened with <strong>xylitol</strong>. Chewing increases saliva, and the mouth bacteria that make acid cannot ferment xylitol.</p>""",
 [("Xylitol is a sugar alcohol. How is a sugar alcohol made from a sugar?",
   "By reducing the sugar&rsquo;s carbonyl group (aldehyde or ketone) to an &ndash;OH group. Xylitol comes from reducing the aldehyde of xylose, so every carbon in xylitol carries an &ndash;OH."),
  ("Starch and cellulose are both polymers of glucose. Why can Rosa digest one but not the other?",
   "Starch is joined by &alpha;(1&rarr;4) glycosidic bonds (with &alpha;(1&rarr;6) branches), which human digestive enzymes, starting with amylase, hydrolyze. Cellulose is joined by &beta;(1&rarr;4) bonds, and humans have no enzyme that breaks them."),
  ("Is sucrose a reducing sugar? Explain.",
   "No. The glycosidic bond in sucrose joins the anomeric carbons of both glucose and fructose, so neither ring can open to a free aldehyde or ketone, and sucrose gives a negative Benedict&rsquo;s test.")],
 ['8.5', '8.6', '8.7']),
9: ("The lipid panel",
 """<p>Rosa&rsquo;s nurse practitioner goes over her lipid panel: LDL 142 mg/dL, HDL 38 mg/dL and triglycerides 230 mg/dL. High triglycerides and low HDL are common in type 2 diabetes. She keeps Rosa on <strong>atorvastatin</strong>, which lowers the liver&rsquo;s production of cholesterol, and suggests eating fish such as salmon or sardines twice a week for their <strong>omega-3 fatty acids</strong>.</p>
<p>Rosa asks why cholesterol is called &ldquo;bad&rdquo; when the nurse also said her body needs it.</p>""",
 [("What is a triglyceride, chemically?",
   "A triacylglycerol: glycerol joined by three ester bonds to three fatty acids."),
  ("What does &ldquo;omega-3&rdquo; tell you about a fatty acid&rsquo;s structure?",
   "Counting from the methyl (omega) end of the chain, the first C=C double bond starts at carbon 3. Omega-3 fatty acids are polyunsaturated, with cis double bonds."),
  ("Cholesterol is a steroid. Name two things the body uses it for, and explain the difference between LDL and HDL.",
   "Cholesterol is part of every cell membrane and is the starting material for bile salts, steroid hormones and vitamin D. LDL carries cholesterol out to the tissues, and high LDL is linked to plaque in arteries; HDL carries cholesterol back to the liver, so higher HDL is protective.")],
 ['9.1', '9.2', '9.6']),
10: ("Protein in the urine and damaged gums",
 """<p>A yearly urine test shows a small amount of <strong>albumin</strong> in Rosa&rsquo;s urine: a urine albumin-to-creatinine ratio of 45 mg/g, where under 30 is normal. Albumin is a globular protein that healthy kidneys keep in the blood. A little leaking through is an early warning sign of kidney damage from diabetes and high blood pressure; her lisinopril helps protect the kidneys.</p>
<p>At the dental office, the hygienist explains that in periodontitis, enzymes from bacteria and from Rosa&rsquo;s own immune cells break down the <strong>collagen</strong> fibers that hold her teeth in their sockets.</p>""",
 [("Albumin is a globular protein that dissolves in blood plasma. Where are its polar and nonpolar side chains mostly found?",
   "Polar and charged side chains are mostly on the outside, facing water; nonpolar side chains are mostly buried inside the folded protein (hydrophobic interactions). That arrangement makes globular proteins water-soluble."),
  ("Collagen is a fibrous protein built from three chains wound into a triple helix. When enzymes break collagen down, which bonds do they hydrolyze?",
   "The peptide (amide) bonds between amino acids in the polypeptide chains. Hydrolysis destroys the primary structure, so the fibers lose their strength."),
  ("The glucose attached to hemoglobin in the A1c test is bonded to the amino group of the first amino acid in the chain. Does this change the protein&rsquo;s primary structure? Explain.",
   "No. The amino acid sequence is unchanged; a sugar has been chemically attached to an amino group on the existing chain. The primary structure is the sequence of amino acids, which stays the same.")],
 ['10.5', '10.6', '10.10']),
11: ("How Rosa&rsquo;s medicines work",
 """<p>Rosa makes a chart of her medicines for a class at the senior center where she volunteers. <strong>Atorvastatin</strong> blocks <strong>HMG-CoA reductase</strong>, a key enzyme in cholesterol synthesis; part of the drug resembles the enzyme&rsquo;s natural substrate. <strong>Lisinopril</strong> blocks angiotensin-converting enzyme (ACE), which lowers blood pressure.</p>
<p>Her dentist adds a low dose of <strong>doxycycline</strong> for a few months. At that dose it does not act as an antibiotic; instead it slows the collagen-destroying enzymes (collagenases) in her gums. These enzymes need a zinc ion to work, and doxycycline binds metal ions. Before starting the statin, her nurse practitioner also checked her <strong>ALT</strong>, a liver enzyme measured in the blood.</p>""",
 [("Atorvastatin resembles the enzyme&rsquo;s substrate and binds the active site. What type of inhibition is this, and can it be overcome?",
   "Competitive inhibition. The inhibitor and the substrate compete for the same active site, so a high enough substrate concentration can overcome it."),
  ("Zn<sup>2+</sup> is a cofactor for collagenase. What is a cofactor, and why would binding it slow the enzyme?",
   "A cofactor is a non-protein helper (a metal ion or a coenzyme) that an enzyme needs in order to work. If the metal ion is tied up, the enzyme loses activity."),
  ("ALT is an enzyme that works inside liver cells. Why does a high ALT level in the blood suggest liver damage?",
   "When liver cells are damaged, their contents leak into the blood, so enzymes that normally stay inside the cells show up at higher levels. That is why ALT is used as a liver test.")],
 ['11.4', '11.5']),
12: ("Adding insulin",
 """<p>A year later, Rosa&rsquo;s A1c is 8.1%, still above her goal, so her nurse practitioner adds a once-daily, long-acting insulin called <strong>insulin glargine</strong>. Rosa is surprised to learn that her insulin is made by microorganisms. The human insulin gene, or an engineered version of it, is inserted into bacteria or yeast using <strong>recombinant DNA</strong>, and the cells produce the protein.</p>
<p>Insulin glargine differs from human insulin by three amino acids: a glycine replaces an asparagine at the end of one chain, and two arginines are added to the other. These changes make it release slowly from the injection site, and they were made by changing the DNA, not the protein.</p>""",
 [("Describe in one or two sentences how bacteria are made to produce human insulin.",
   "The insulin gene is inserted into a plasmid, the plasmid is put into bacteria, and the bacteria transcribe the gene into mRNA and translate it into the insulin protein chains as they grow."),
  ("To replace asparagine with glycine in the protein, what has to change in the gene?",
   "The codon for that position must be changed from an asparagine codon (AAU or AAC in mRNA) to a glycine codon (GGU, GGC, GGA or GGG), so the DNA sequence for that triplet is changed."),
  ("Human genes contain introns, but bacteria cannot splice them out. How is this problem solved?",
   "The gene that is inserted is made without introns, for example copied from processed mRNA or synthesized directly, so the bacteria get only the coding sequence.")],
 ['12.5', '12.6', '12.8']),
13: ("A low blood sugar in the dental chair",
 """<p>Two weeks after starting insulin, Rosa skips lunch before a 2 p.m. dental appointment. In the chair she becomes shaky, sweaty and confused. The hygienist checks her blood glucose: <strong>62 mg/dL</strong>, which is hypoglycemia (below 70 mg/dL). Following the office&rsquo;s emergency plan, she gives Rosa <strong>15 grams of fast-acting carbohydrate</strong>, four glucose tablets, and rechecks in 15 minutes: 104 mg/dL. The appointment continues after Rosa eats a snack.</p>
<p>Later her nurse practitioner reviews how insulin, glucagon and metformin control blood glucose, adjusts her glargine dose, and reminds her not to skip meals.</p>""",
 [("Why do glucose tablets raise blood glucose faster than a chocolate bar with the same amount of carbohydrate?",
   "Glucose is a monosaccharide that is absorbed directly without digestion. The chocolate bar contains sucrose that must be hydrolyzed first, and its fat slows stomach emptying, so its sugar reaches the blood more slowly."),
  ("If Rosa could not swallow, glucagon would be given. What does glucagon tell the liver to do with its glycogen?",
   "Break it down: glycogenolysis releases glucose 1-phosphate, which is converted to glucose 6-phosphate and then to free glucose that the liver releases into the blood."),
  ("Metformin&rsquo;s main effect is to lower the liver&rsquo;s production of new glucose. Name that pathway and two starting materials it uses.",
   "Gluconeogenesis, the synthesis of glucose from noncarbohydrate sources such as lactate, glycerol and most amino acids.")],
 ['13.8', '13.9', '13.10']),
14: ("An evening walk",
 """<p>Rosa starts walking for 30 minutes after dinner. Working muscles take up glucose and break it down through glycolysis, the citric acid cycle and the electron transport chain to make ATP; this uptake of glucose lowers her after-dinner readings.</p>
<p>Her pharmacist mentions a rare but serious side effect of metformin: <strong>lactic acidosis</strong>, a build-up of lactate in the blood. The risk is higher when the body cannot get enough oxygen to its tissues, for example in severe infection, heart failure or dehydration, or when the kidneys cannot clear metformin.</p>""",
 [("In aerobic metabolism, what is the final electron acceptor of the electron transport chain, and what does it form?",
   "Oxygen, O<sub>2</sub>. It accepts electrons and H<sup>+</sup> to form water."),
  ("When oxygen is low, why do cells convert pyruvate to lactate instead of sending it to the citric acid cycle?",
   "Without enough O<sub>2</sub>, the electron transport chain cannot reoxidize NADH. Reducing pyruvate to lactate regenerates NAD<sup>+</sup>, which glycolysis needs in order to keep making a small amount of ATP. Lactate (and acid) build up as a result."),
  ("About how many ATP does one glucose yield with oxygen compared with glycolysis alone?",
   "Roughly 30&ndash;32 ATP per glucose with complete aerobic oxidation, compared with a net of 2 ATP from glycolysis alone.")],
 ['13.5', '14.3', '14.4', '14.5']),
15: ("A sick day, and one year later",
 """<p>In the winter, Rosa catches a stomach virus and cannot keep food down for two days. Following the written <strong>sick-day plan</strong> from her care team, she sips fluids, checks her glucose more often and tests her urine with a ketone strip, which shows moderate <strong>ketones</strong>. Her nurse practitioner adjusts her medicines until she can eat again. Her daughter notices a fruity smell on her breath.</p>
<p>At a follow-up visit, her lab report includes <strong>BUN</strong> (blood urea nitrogen) and creatinine to check her kidneys. One year after her deep cleaning, Rosa&rsquo;s gums bleed much less and her A1c is 7.0%. Studies suggest that treating gum disease can modestly improve blood glucose control, along with the medicines, diet and exercise you have followed through this book.</p>""",
 [("Why does a person who cannot eat for a couple of days start making ketone bodies?",
   "With little glucose coming in, the body breaks down stored fat. &beta;-Oxidation of fatty acids produces more acetyl CoA than the citric acid cycle can use (oxaloacetate is being diverted to gluconeogenesis), so the liver converts the excess acetyl CoA into ketone bodies."),
  ("Which ketone body causes the fruity breath, and how is it formed?",
   "Acetone. It forms when acetoacetate loses CO<sub>2</sub> (decarboxylation), and because it is volatile it is exhaled."),
  ("What does BUN measure, and which pathway produces it?",
   "BUN measures urea nitrogen in the blood. Urea is made in the liver by the urea cycle, which converts toxic ammonium ion from amino acid breakdown into urea that the kidneys excrete. When the kidneys are not working well, BUN rises.")],
 ['15.3', '15.7', '15.10']),
}

INTRO_NOTE = ('<p style="font-size:0.9em;color:#555;">Rosa Delgado is a fictional patient created for this book. Her story simplifies real care to show the chemistry; '
              'it is not medical advice, and real treatment decisions follow current clinical guidelines and a patient&rsquo;s own care team.</p>')

def case_block(ch):
    title, scen, qs, secs = CASE[ch]
    parts = [f'<h2>Patient Case: Rosa&rsquo;s Story, Part {ch} of 15</h2>',
             f'<div class="box-note" style="border-left:6px solid {COLOR};">',
             f'<p class="boxtitle">{title}</p>', scen]
    if ch == 1:
        parts.append(INTRO_NOTE)
    parts.append('</div>')
    for i, (q, a) in enumerate(qs, 1):
        parts.append(f'<div class="box-exercise">\n<p class="boxtitle">Case Question {ch}.{i}</p>\n<p>{q}</p>\n'
                     f'<details><summary>Answer</summary><div>{a}</div></details>\n</div>')
    nxt = f' Rosa&rsquo;s story continues in the Chapter {ch + 1} Guide.' if ch < 15 else ' This is the last part of Rosa&rsquo;s story.'
    parts.append(f'<p><strong>Where this chemistry is taught:</strong> {", ".join(S(s) for s in secs)}.{nxt}</p>')
    return '\n'.join(parts) + '\n'
