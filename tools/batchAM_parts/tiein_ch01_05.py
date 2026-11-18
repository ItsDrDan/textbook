# Lab tie-in edits, group ch01_05 (Sections 1.5, 2.1, 2.4, 3.4, 3.7, 4.3, 4.5, 4.7, 4.10, 5.2, 5.4, 5.5).
# Uses the caller's helper e(pageid, old, new, note, why). Run from the textbook-git root.

BASE = "https://itsdrdan.github.io/chem3b-lab-manual/pdf/experiments/"

def labp(*links):
    """One 'Lab manual:' paragraph; links = (pdf_file, label) pairs."""
    parts = ['<a href="%s%s" target="_blank" rel="noopener">%s (PDF)</a>' % (BASE, f, lab) for f, lab in links]
    return '<p style="font-size:0.95em;"><strong>Lab manual:</strong> ' + "; ".join(parts) + '</p>'

EXP1 = ("Exp01_FunctionalGroups.pdf", "Experiment 1 &ndash; Functional Groups")
EXP2 = ("Exp02_StructuresOfAlkanes.pdf", "Experiment 2 &ndash; Structures of Alkanes")
EXP3 = ("Exp03_Hydrocarbons.pdf", "Experiment 3 &ndash; Hydrocarbons")
EXP4 = ("Exp04_AlcoholsPhenols.pdf", "Experiment 4 &ndash; Alcohols and Phenols")
EXP5 = ("Exp05_AldehydesKetones.pdf", "Experiment 5 &ndash; Aldehydes and Ketones")
WCHI = ("Workshop_Chirality.pdf", "Workshop: Chirality Stations")
APPX = BASE + "16_Appendices.pdf"

# ---------------------------------------------------------------- 1.5 (597058)
e(597058,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<ul>
<li><strong>Model kits (Experiments 1&ndash;7):</strong> Black = C (4 bonds), white = H (1), red = O (2), blue = N (3), green = Cl, orange = Br, purple = I (1 each). Short sticks are single bonds; two or three long flexible sticks make a double or triple bond. Build a molecule whenever a 3-D shape is hard to picture.</li>
<li>For a VSEPR chart of organic geometries, use the table &ldquo;Electron groups, molecular shapes and bond angles&rdquo; above; electronegativity values are in Figure 1.4.3.</li>
</ul>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<ul>
<li><strong>Experiment 1 &ndash; Functional Groups:</strong> you build a model of each compound, name its functional group, and predict its shape and bond angle, its polarity, its strongest intermolecular force (Section 1.8), and its molar mass. You use the model kit again in Experiments 2&ndash;7.</li>
<li><strong>Model kits:</strong> in the lab manual&rsquo;s color key, black = C (4 bonds), white = H (1), red = O (2), blue = N (3), green = a halogen (F, Cl, Br or I; 1), yellow = S (2), purple = P (3). Colors vary from kit to kit, so check the key that comes with your kit. Join two atoms with one connection for a single bond; use two or three bond pieces (or flexible bonds) for a double or triple bond. Lone pairs have no pieces, so count them on paper. Build a molecule whenever a 3-D shape is hard to picture.</li>
<li>For a VSEPR chart of organic geometries, use the table &ldquo;Electron groups, molecular shapes and bond angles&rdquo; above; electronegativity values are in Figure 1.4.3. The lab manual&rsquo;s Appendix D (Molecular Shapes and Electronegativity) has both in one place: <a href="''' + APPX + '''" target="_blank" rel="noopener">Appendices (PDF)</a>.</li>
</ul>
''' + labp(EXP1) + '''
</div>''',
"1.5 In the Lab: tied to Experiment 1 Functional Groups; kit color key fixed; Appendix D pointer added",
"exp01.js Parts A and B: build models, name functional group, VSEPR shape/angle, polarity, strongest IMF, molar mass; Table 3 key is black C, white H, red O, blue N, green halogen (F, Cl, Br, I), yellow S, purple P, 'colors vary'; no brand named (no Snatoms); model kits listed in exp02-exp07 too. appendix.js Appendix D = D.1 VSEPR table, D.2 Pauling electronegativity.")

# ---------------------------------------------------------------- 2.1 (597065)
e(597065,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<ul>
<li><strong>Experiment 2 &ndash; Properties of Alkanes:</strong> compare color, odor, physical state, water solubility, and combustion of organic vs. inorganic compounds, and identify functional groups on models.</li>
</ul>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<ul>
<li><strong>Experiment 3 &ndash; Hydrocarbons</strong> (Parts B&ndash;D): compare the color, odor, and physical state of organic compounds (cyclohexane, toluene, benzoic acid) with inorganic ones (NaCl, KI, water), and decide whether each has ionic or covalent bonds; test whether NaCl and toluene dissolve in water and in cyclohexane; and watch your instructor burn small samples in the fume hood. NaCl does not burn; the hydrocarbons do, and toluene gives the sootiest flame.</li>
</ul>
''' + labp(EXP3) + '''
</div>''',
"2.1 In the Lab: old Experiment 2 Properties of Alkanes -> Experiment 3 Hydrocarbons Parts B-D",
"exp03.js Part B (color, odor, state, ionic vs covalent; NaCl, KI, benzoic acid, cyclohexane, toluene, water), Part C (solubility of NaCl and toluene in cyclohexane and water), Part D (combustion is an instructor demonstration; NaCl does not burn, toluene heavy soot). Model functional-group work is Experiment 1, so that clause was dropped.")

# ---------------------------------------------------------------- 2.4 (597068)
e(597068,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<ul>
<li><strong>Experiment 1 &ndash; Structures of Alkanes:</strong> build methane, ethane, and larger alkanes; draw them as 3-D (wedge-dash), complete, and condensed formulas; build constitutional isomers; draw cycloalkanes and haloalkanes.</li>
</ul>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<ul>
<li><strong>Experiment 2 &ndash; Structures of Alkanes:</strong> build methane, ethane, and propane; draw methane in 3-D (wedge-dash) and each alkane as complete and condensed formulas; build the constitutional isomers of C<sub>4</sub>H<sub>10</sub> and C<sub>5</sub>H<sub>12</sub>, name them, and look up their melting points, boiling points, and densities; build and draw the three-, four-, and five-carbon cycloalkanes and several haloalkanes, including the four isomers of dichloropropane.</li>
</ul>
''' + labp(EXP2) + '''
</div>''',
"2.4 In the Lab: old Experiment 1 -> Experiment 2 Structures of Alkanes",
"exp02.js A.1-A.3 (methane wedge-dash, ethane, propane complete/condensed), B.1-B.5 (C4H10 and C5H12 isomers, look up mp, bp, density), C.1-C.3 (cyclopropane to cyclopentane), D.1-D.4 (chloromethane, 1,2-dibromoethane, 2-iodopropane, four dichloropropanes).")

# ---------------------------------------------------------------- 3.4 (597081) cross-reference
e(597081,
'''the disappearance of bromine color is a qualitative test for an alkene (In the Lab, Section 3.7).</p>''',
'''the disappearance of bromine color is a qualitative test for an alkene (Experiment 3 &ndash; Hydrocarbons; In the Lab, Section 3.7).</p>''',
"3.4 body cross-reference: names Experiment 3 Hydrocarbons beside the 3.7 In the Lab pointer",
"exp03.js Part E is the bromine test (red-orange Br2 in CH2Cl2 decolorizes at once with an alkene).")

# ---------------------------------------------------------------- 3.7 (597084)
e(597084,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<ul>
<li><strong>Experiment 3 &ndash; Reactions of Hydrocarbons</strong></li>
<li><strong>Bromine test:</strong> the red color of Br<sub>2</sub> disappears quickly with an alkene (addition across the C=C). With an alkane the color lingers and fades only slowly in light (substitution, which also releases HBr). Benzene gives no reaction.</li>
<li><strong>KMnO<sub>4</sub> test:</strong> purple permanganate adds to a C=C to make a diol and turns into a muddy brown MnO<sub>2</sub> solid. Alkanes and aromatic rings stay purple.</li>
<li>You will use these two tests to identify an unknown hydrocarbon as saturated or unsaturated.</li>
</ul>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<ul>
<li><strong>Experiment 3 &ndash; Hydrocarbons:</strong> you test cyclohexane (an alkane), cyclohexene (an alkene), toluene (an aromatic compound), and an unknown.</li>
<li><strong>Bromine test:</strong> the red-orange color of Br<sub>2</sub> (dissolved in methylene chloride) disappears immediately with an alkene (addition across the C=C), even in the dark. With an alkane the color stays and fades only slowly in bright light (substitution, which also releases HBr; moist blue litmus paper held above the tube turns red). The benzene ring of toluene does not react without a catalyst, so the color stays; only its CH<sub>3</sub> group may react slowly in light, like an alkane.</li>
<li><strong>KMnO<sub>4</sub> test:</strong> purple permanganate adds two OH groups to a C=C to make a diol and turns into a muddy brown MnO<sub>2</sub> solid within 60 seconds. Alkanes and aromatic rings stay purple.</li>
<li>With these two tests and the combustion demonstration (an aromatic compound burns with a yellow, sooty flame), you classify your unknown as an alkane, an alkene, or an aromatic compound.</li>
</ul>
''' + labp(EXP3) + '''
</div>''',
"3.7 In the Lab: Experiment 3 Hydrocarbons (title fixed); toluene not benzene; red-orange; litmus; 3-way unknown",
"exp03.js Parts E (1% Br2 in CH2Cl2; alkene decolorizes immediately even in dark; alkane fades in bright light, HBr turns moist blue litmus red; toluene ring no reaction, CH3 may react slowly in light), F (1% KMnO4, brown within 60 s), G (unknown classified as alkane, alkene, or aromatic using D, E, F). Toluene is used; benzene is not.")

# ---------------------------------------------------------------- 4.3 (597092)
e(597092,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>In the alcohols and phenols experiment you test solubility directly: alcohols with four or fewer carbons dissolve in water; longer ones form a separate layer. Phenol is only moderately soluble in water (its OH hydrogen bonds, but the ring is nonpolar), yet it dissolves completely in sodium hydroxide solution because it is converted to the ionic phenoxide salt; Sections 4.7 and 4.10 explain why.</p>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>In Experiment 4 &ndash; Alcohols and Phenols you test solubility directly. Ethanol, 2-propanol and t-butyl alcohol (four carbons) dissolve in water to give one clear layer; cyclohexanol (six carbons) gives a cloudy mixture or a separate layer. The phenol you test is salicylic acid, because phenol itself is too toxic and corrosive for a teaching lab. Salicylic acid is only slightly soluble in cold water: its OH and COOH groups hydrogen bond with water, but its benzene ring is nonpolar. Section 4.7 describes the ferric chloride test you then use to pick out the phenol.</p>
''' + labp(EXP4) + '''
</div>''',
"4.3 In the Lab: Experiment 4 Alcohols and Phenols; real compounds; salicylic acid as the phenol; NaOH removed",
"exp04.js Intro B and B.2: ethanol, 2-propanol, t-butyl alcohol soluble; cyclohexanol (6 C) only slightly soluble; salicylic acid ~0.2 g/100 mL cold water (ring nonpolar). Intro A: phenol too hazardous, salicylic acid is the phenol. No NaOH solubility test anywhere in exp04.js.")

# ---------------------------------------------------------------- 4.5 (597094)
e(597094,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p><strong>Chromate oxidation test</strong> (alcohols and phenols experiment): orange chromium(VI) (dichromate, Cr<sub>2</sub>O<sub>7</sub><sup>2&minus;</sup>, in the acidic reagent) turns <strong>green</strong> (Cr<sup>3+</sup>) when it oxidizes a 1&deg; or 2&deg; alcohol. A 3&deg; alcohol cannot be oxidized, so the solution <strong>stays orange</strong>. The balanced equation in the section text is this same color change written out: dichromate is the orange reactant, Cr<sup>3+</sup> the green product.</p>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p><strong>Chromate oxidation test</strong> (Figure 4.5.3): orange chromium(VI) (dichromate, Cr<sub>2</sub>O<sub>7</sub><sup>2&minus;</sup>, in the acidic reagent) turns <strong>green</strong> (Cr<sup>3+</sup>) when it oxidizes a 1&deg; or 2&deg; alcohol. A 3&deg; alcohol cannot be oxidized, so the solution <strong>stays orange</strong>. The balanced equation in the section text is this same color change written out: dichromate is the orange reactant, Cr<sup>3+</sup> the green product.</p>
<p>Experiment 4 &ndash; Alcohols and Phenols does not use the chromate test. It sorts alcohols with the <strong>Lucas test</strong> instead: zinc chloride in concentrated HCl replaces the &ndash;OH with &ndash;Cl, and the alkyl chloride that forms does not dissolve, so the tube turns cloudy. A 3&deg; alcohol turns cloudy almost at once, a 2&deg; alcohol in about 3&ndash;10 minutes (some need a warm water bath), and a 1&deg; alcohol stays clear. This is a substitution, not an oxidation, so the order is reversed: the 3&deg; alcohol that chromate cannot oxidize reacts fastest with the Lucas reagent.</p>
''' + labp(EXP4) + '''
</div>''',
"4.5 In the Lab: chromate test kept as chemistry but no longer called part of the lab; Experiment 4 Lucas test added",
"exp04.js has no chromate/dichromate test; Part C is the Lucas test (ZnCl2 in conc. HCl; R-OH -> R-Cl, cloudy; 3 deg < 1 min, 2 deg 3-10 min or warm 50-60 C bath, 1 deg no change; phenols do not react).")

# ---------------------------------------------------------------- 4.7 (597096)
e(597096,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>Two bench tests tell a phenol from an alcohol in the alcohols and phenols experiment. <strong>NaOH test:</strong> phenol dissolves in 5% NaOH (it is neutralized to sodium phenoxide, an ionic salt); an alcohol such as cyclohexanol does not react and stays as a separate layer (details in Section 4.10). <strong>Ferric chloride (FeCl<sub>3</sub>) test:</strong> phenols form strongly colored complexes with Fe<sup>3+</sup> (from yellow to purple). Ordinary alcohols do not.</p>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>In Experiment 4 &ndash; Alcohols and Phenols the <strong>ferric chloride (FeCl<sub>3</sub>) test</strong> tells a phenol from an alcohol. The pale yellow FeCl<sub>3</sub> solution turns violet or purple when a phenol bonds to Fe<sup>3+</sup> to form a colored complex ion (Figure 4.7.2); some phenols give blue, green or red instead. This is not an oxidation. Alcohols form no colored complex, so the mixture stays yellow. The phenol in the lab is salicylic acid, which gives a strong violet color; phenol itself is too hazardous to use. The NaOH test in Section 4.10 is not part of the experiment.</p>
''' + labp(EXP4) + '''
</div>''',
"4.7 In the Lab: Experiment 4 FeCl3 test only; NaOH test removed; salicylic acid as the phenol",
"exp04.js Intro D and D.1: 1% FeCl3, yellow -> violet/purple (some phenols blue, green, red), not an oxidation, alcohols stay yellow; salicylic acid strong violet. No NaOH test in exp04.js.")

# ---------------------------------------------------------------- 4.10 (597099)
e(597099,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>In Experiment 4 you test each unknown with 5% NaOH: a phenol dissolves, an alcohol does not. Pair that result with the ferric chloride test (phenols give a purple to green color with Fe<sup>3+</sup>; alcohols do not) and the chromate oxidation test (1&deg; and 2&deg; alcohols turn the orange reagent green; 3&deg; alcohols do not), and you can place an unknown in one of three boxes: 1&deg;/2&deg; alcohol, 3&deg; alcohol, or phenol.</p>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>Experiment 4 &ndash; Alcohols and Phenols checks acidity with pH paper rather than NaOH. The alcohol&ndash;water mixtures give a pH near 7. Salicylic acid, the lab&rsquo;s phenol, gives a pH of about 2&ndash;3 because it also has a carboxylic acid group, which gives up H<sup>+</sup> much more easily than its phenol OH. Your unknown is ethanol, 2-propanol, t-butyl alcohol, cyclohexanol or salicylic acid. The ferric chloride test tells you whether it is a phenol (the yellow reagent turns violet; alcohols stay yellow). The Lucas test sorts the alcohols: a 3&deg; alcohol turns cloudy almost at once, a 2&deg; alcohol in a few minutes, and a 1&deg; alcohol stays clear (phenols do not react). Solubility and odor separate the rest.</p>
''' + labp(EXP4) + '''
</div>''',
"4.10 In the Lab: Experiment 4 as revised (pH paper, FeCl3, Lucas; five possible unknowns); NaOH and chromate removed",
"exp04.js B.3 pH paper (alcohols ~7; salicylic acid pH 2-3 from its COOH), C Lucas test, D FeCl3, Intro E: unknown is ethanol, 2-propanol, t-butyl alcohol, cyclohexanol, or salicylic acid; 'Use FeCl3 ... Lucas ... solubility and odor'. No NaOH or chromate test.")

# ---------------------------------------------------------------- 5.2 (597103)
e(597103,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>In the aldehydes and ketones experiment you will meet three of the section's compounds by smell: formaldehyde (specimen preservative), acetone (nail-polish remover) and benzaldehyde (almond). The chemical tests you then run on an unknown (Tollens', iodoform) are described in Section 5.4.</p>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>In Experiment 5 &ndash; Aldehydes and Ketones you meet six of this section&rsquo;s compounds by smell: acetone (nail-polish remover), benzaldehyde (almond), cinnamaldehyde (cinnamon), vanillin (vanilla), camphor, and 2,3-butanedione (butter flavoring). You also mix samples with water: a small compound such as acetone dissolves, while an aromatic aldehyde such as benzaldehyde, with its large nonpolar ring, is much less soluble. The chemical tests you then run on an unknown (Tollens&rsquo;, iodoform) are described in Section 5.4.</p>
''' + labp(EXP5) + '''
</div>''',
"5.2 In the Lab: Experiment 5; odor list matches B.1 (formaldehyde not smelled); solubility added",
"exp05.js B.1 odor vials: acetone, benzaldehyde, camphor, vanillin, cinnamaldehyde, 2,3-butanedione (formaldehyde appears only as a model in A.1 and in the intro). B.3 solubility in water of anisaldehyde, benzaldehyde, acetone, cyclohexanone; intro: aromatic aldehydes much less soluble.")

# ---------------------------------------------------------------- 5.4 (597105)
e(597105,
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p><strong>Tollens&rsquo; test:</strong> aldehydes reduce Ag<sup>+</sup> to a silver mirror on the tube; ketones give no reaction. <strong>Iodoform test:</strong> a <em>methyl ketone</em> (CH<sub>3</sub>&ndash;C=O) reacts with I<sub>2</sub> in NaOH to give a yellow solid, iodoform (CHI<sub>3</sub>), with a medicinal odor (the equation is drawn in the lecture-slide figure in Section 5.1). You will combine these results with the odors from Section 5.2 to identify an unknown carbonyl compound.</p>
</div>''',
'''<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>In Experiment 5 &ndash; Aldehydes and Ketones you first act out both reactions with models: you oxidize propanal to a carboxylic acid ([O]) and reduce acetone to 2-propanol, a 2&deg; alcohol ([H]). At the bench you run two tests. <strong>Tollens&rsquo; test:</strong> aldehydes reduce Ag<sup>+</sup> to a silver mirror (or a gray-black deposit of silver) on the tube; ketones give no reaction. All tubes are heated together for the same 5 minutes and compared with the acetone tube, because the reagent can deposit a little silver on its own (a false positive). <strong>Iodoform test:</strong> a <em>methyl ketone</em> (CH<sub>3</sub>&ndash;C=O) reacts with I<sub>2</sub> in NaOH to give a pale yellow solid, iodoform (CHI<sub>3</sub>), with a medicinal odor (the equation is drawn in the lecture-slide figure in Section 5.1). A yellow solution alone is not a positive result. You will combine these results with the odors and solubility from Section 5.2 to identify an unknown carbonyl compound.</p>
''' + labp(EXP5) + '''
</div>''',
"5.4 In the Lab: Experiment 5; model [O]/[H] added; Tollens' false-positive control; pale yellow solid",
"exp05.js A.5 (propanal [O] model), A.7 (propanone [H] -> 2-propanol, 2 deg), D (Tollens', all tubes 5 min together, compare with acetone, false positive possible), C (iodoform: pale yellow solid; yellow solution is not positive), E (unknown from odor, solubility, iodoform, Tollens').")

# ---------------------------------------------------------------- 5.5 (597106) NEW box after the D/L Professor Tip
e(597106,
'''<div class="box-note">
<p class="boxtitle">Professor Tip</p>
<p>Before you read left or right, check that the projection is drawn the standard way, CHO (or the most oxidized carbon) on top. Flipping the drawing upside down reverses the answer. And read the <em>bottom</em> chiral carbon, not the top one; the top one is the most common wrong choice on exams.</p>
</div>''',
'''<div class="box-note">
<p class="boxtitle">Professor Tip</p>
<p>Before you read left or right, check that the projection is drawn the standard way, CHO (or the most oxidized carbon) on top. Flipping the drawing upside down reverses the answer. And read the <em>bottom</em> chiral carbon, not the top one; the top one is the most common wrong choice on exams.</p>
</div>
<div class="box-note">
<p class="boxtitle">In the Lab</p>
<p>In the Chirality Stations workshop you and a partner work through 20 stations of prebuilt models and printed structures. At each one you decide whether a molecule is chiral, star (*) its chiral carbons, and tell whether two models are the same molecule, enantiomers or diastereomers, comparing them carbon by carbon as in this section. You also draw molecules with wedges and dashes and as Fischer projections, and label sugars D or L from the bottom chiral carbon. A few stations use sugar rings, where you name hemiacetals, hemiketals, acetals and ketals (Section 5.3 and Chapter 8).</p>
''' + labp(WCHI) + '''
</div>''',
"5.5 NEW In the Lab box: Chirality Stations workshop, placed after the D/L Professor Tip (end of the Fischer/D-L subsection)",
"workshop_chirality.js Goals and Directions: 20 stations with partner; chiral or achiral, star chiral carbons; same/enantiomers/diastereomers; wedge-dash and Fischer drawings, D/L sugars; hemiacetal/hemiketal/acetal/ketal stations. Placed after the Fischer D/L subsection so every skill named has already been taught on the page.")
