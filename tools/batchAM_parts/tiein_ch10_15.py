# Lab tie-in edits, group ch10_15 (sections 10.3, 10.10, 11.3, 11.5, 12.3, 13.3, 13.9, 15.5, 15.7).
# Uses e(pageid, old, new, note, why), defined by the caller. Runs from the textbook-git root.
# No edits needed on 10.5 (597158) or 11.8 (597173); see tiein_ch10_15_notes.md.

_BASE = "https://itsdrdan.github.io/chem3b-lab-manual/pdf/experiments/"

def _a(pdf, label):
    return '<a href="' + _BASE + pdf + '" target="_blank" rel="noopener">' + label + ' (PDF)</a>'

def _link(*pairs):
    return ('<p style="font-size:0.95em;"><strong>Lab manual:</strong> '
            + '; '.join(_a(p, l) for p, l in pairs) + '</p>\n')

EXP11 = ("Exp11_AminoAcids.pdf", "Experiment 11 &ndash; Amino Acids")
EXP12 = ("Exp12_PeptidesProteins.pdf", "Experiment 12 &ndash; Peptides and Proteins")
EXP13 = ("Exp13_Enzymes.pdf", "Experiment 13 &ndash; Enzymes")
EXP14 = ("Exp14_Vitamins.pdf", "Experiment 14 &ndash; Vitamins")
EXP15 = ("Exp15_NucleicAcids.pdf", "Experiment 15 &ndash; Nucleic Acids and DNA Extraction")

# ---------------------------------------------------------------- 10.3 (597156)
e(597156,
  'Cheese makers and your lab bench use the same idea: in <strong>Experiment 12</strong> you add acid to milk until it reaches pH 4.6, the casein curdles at its pI, and you collect it (see In the Lab below).',
  'Cheese makers and your lab bench use the same idea: in <strong>Experiment 12</strong> you add acid to warm milk drop by drop until the casein curdles near its pI, then you collect it and measure the pH (see In the Lab below).',
  "10.3 Valley Connection: Experiment 12 casein sentence",
  "exp12.js C.3 adds 20% acetic acid to milk warmed to about 50 °C until no more solid forms, then measures the pH; students do not titrate to a set pH of 4.6 (the manual gives no pI value, only 'in the acidic range'). The section's own pI of 4.6 stays in the paragraph above.")

e(597156,
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<ul>\n<li><strong>Experiment 11 &ndash; Amino Acids:</strong> classify amino acids by R group, then separate them by paper chromatography, make the spots visible with <strong>ninhydrin</strong> (it reacts with the free &alpha;-amino group to give a purple product, the reaction the section text describes), and identify an unknown from its R<sub>f</sub> value (distance moved by the spot &divide; distance moved by the solvent). Polar, charged side chains stick to the wet paper and travel less; nonpolar side chains travel farther with the solvent.</li>\n<li><strong>Experiment 12 &ndash; Peptides and Proteins (part 1):</strong> isolate casein from milk by adding acid until it reaches its isoelectric point, then tell amino acids from proteins with two color tests. <strong>Ninhydrin</strong> needs a free amino group, so it is strongest for free amino acids. The <strong>biuret test</strong> needs two or more peptide bonds, so blue Cu<sup>2+</sup> turns violet only with peptides and proteins, not with free amino acids. The denaturation part of this experiment belongs with Section 10.10.</li>\n</ul>\n</div>',
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<ul>\n<li><strong>Experiment 11 &ndash; Amino Acids:</strong> build amino acid models and classify each one by its R group, then separate six amino acids by thin-layer chromatography on cellulose plates, make the spots visible with <strong>ninhydrin</strong> (it reacts with the free &alpha;-amino group to give a purple product, the reaction the section text describes), and identify an unknown from its R<sub>f</sub> value (distance moved by the spot &divide; distance moved by the solvent). Polar, charged side chains stick to the polar cellulose and travel less; nonpolar side chains travel farther with the solvent.</li>\n<li><strong>Experiment 12 &ndash; Peptides and Proteins:</strong> in Part C you isolate casein from warm nonfat milk by adding acid until it reaches its isoelectric point, and you calculate the percent casein in the milk. In Part D you tell amino acids from proteins with two color tests. <strong>Ninhydrin</strong> needs a free amino group, so it is strongest for free amino acids. The <strong>biuret test</strong> needs two or more peptide bonds, so blue Cu<sup>2+</sup> turns violet only with peptides and proteins, not with free amino acids. Part B, denaturation, goes with Section 10.10.</li>\n</ul>\n'
  + _link(EXP11, EXP12) + '</div>',
  "10.3 In the Lab: Experiments 11 and 12; TLC on cellulose, part labels fixed",
  "exp11.js Part A builds amino acid models and classifies R groups; Part B is TLC on cellulose plates (not paper) with 6 knowns (Phe, Ala, Glu, Ser, Lys, Asp), ninhydrin, Rf to spot center. exp12.js has Parts A peptide models, B denaturation, C casein (20% acetic acid, % casein), D biuret and ninhydrin; the old 'part 1/part 2' labels do not exist.")

# ---------------------------------------------------------------- 10.10 (597163)
e(597163,
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Experiment 12 &ndash; Peptides and Proteins (part 2):</strong> you denature egg albumin with heat, acid, base, ethanol, tannic acid, and heavy-metal ions, and watch the clear solution turn cloudy as the unfolded chains clump. Each tube is a row of the table above: predict which interactions each agent disrupts before you add it, then check whether the protein precipitates. The casein isolation and the biuret and ninhydrin tests from the first part of the experiment are described with Section 10.3.</p>\n</div>',
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Experiment 12 &ndash; Peptides and Proteins:</strong> in Part B you denature egg albumin with heat (a boiling water bath), acid (10% HNO<sub>3</sub>), base (10% NaOH), 95% ethanol, and a heavy-metal ion (1% AgNO<sub>3</sub>), and compare each tube with an untreated control as the unfolded chains clump. Each tube matches a row of the table above: predict which interactions each agent disrupts before you add it, then check whether the protein precipitates. Parts C and D, the casein isolation and the biuret and ninhydrin tests, are described with Section 10.3.</p>\n'
  + _link(EXP12) + '</div>',
  "10.10 In the Lab: Experiment 12 Part B denaturation, tannic acid removed",
  "exp12.js Part B (B.1-B.5) uses only heat, 10% HNO3, 10% NaOH, 95% ethanol and 1% AgNO3 on egg albumin, with a control tube; no tannic acid and only one heavy metal (Ag+). Casein and color tests are Parts C and D.")

# ---------------------------------------------------------------- 11.3 (597168)
e(597168,
  'In Experiment 13 you will test three of them (enzyme concentration, temperature and pH), plus an inhibitor.',
  'In Experiment 13 you will test three of them (enzyme concentration, temperature and pH), and you will also test whether three added substances inhibit the enzyme.',
  "11.3 body sentence: Experiment 13 tests three possible inhibitors",
  "exp13.js Part D mixes amylase with 1% NaCl, 95% ethanol and 1% AgNO3 and asks which act as inhibitors; NaCl is a comparison that does not inhibit, so 'an inhibitor' is not quite right.")

e(597168,
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Experiment 13 &ndash; Enzymes:</strong> amylase hydrolyzes starch. The iodine test (blue-black with starch) fades as starch is digested, and Benedict&rsquo;s test detects the glucose and maltose produced. You will measure how enzyme concentration, temperature, pH, and an inhibitor change the rate, which gives you most of the curves on this page from your own data.</p>\n</div>',
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Experiment 13 &ndash; Enzymes:</strong> amylase hydrolyzes starch, mostly to maltose. The iodine test (blue-black with starch) fades as starch is digested, and Benedict&rsquo;s test detects the maltose and glucose produced. You will see how enzyme concentration (Part A), temperature (Part B) and pH (Part C) change the rate, and test whether sodium chloride, ethanol and silver ions (Ag<sup>+</sup>) inhibit the enzyme (Part D). Your graphs of activity against enzyme amount, temperature and pH give you three of the curves on this page from your own data.</p>\n'
  + _link(EXP13) + '</div>',
  "11.3 In the Lab: Experiment 13 Enzymes, parts named, inhibitor test fixed",
  "exp13.js: A enzyme concentration (Benedict's in A.3), B temperature, C pH (buffers 2, 4, 7, 10), D inhibition with NaCl, ethanol, AgNO3; students graph activity for A, B, C. Intro says amylase gives mostly maltose, a little glucose.")

# ---------------------------------------------------------------- 11.5 (597170)
e(597170,
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Experiment 14 &ndash; Vitamins:</strong> classify vitamins as water- or fat-soluble, measure vitamin C in fruit juices by titration with iodine (vitamin C reduces I<sub>2</sub>; the first lasting blue-black color with starch marks the endpoint), and show that heating destroys vitamin C.</p>\n</div>',
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Experiment 14 &ndash; Vitamins:</strong> classify vitamins as water- or fat-soluble, standardize an iodine solution with a vitamin C tablet, then measure the vitamin C in a fruit juice and a powdered drink by titration with iodine (vitamin C reduces I<sub>2</sub>; the first lasting blue-black color with starch marks the endpoint), and show that boiling destroys vitamin C.</p>\n'
  + _link(EXP14) + '</div>',
  "11.5 In the Lab: Experiment 14 Vitamins, link added, samples matched",
  "exp14.js: A solubility (water vs CH2Cl2), B standardization with a vitamin C tablet, C fruit juice and powdered drink, D boil 15 min and re-titrate. Number 14 is already right; Figure 11.5.1 caption '(Experiment 14)' is correct and left alone.")

# ---------------------------------------------------------------- 12.3 (597177)
e(597177,
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p>In the DNA extraction lab you break open cells (strawberry, cheek, or onion) with a detergent solution, which dissolves the lipid membranes (Chapter 9). Salt is added so that Na<sup>+</sup> ions surround the negatively charged phosphate backbone; this lets the strands clump instead of repelling one another. Cold ethanol is layered on top: DNA is much less soluble in ethanol than in water, so it comes out of solution as a white, stringy mass at the boundary. Meat tenderizer (a protease) or pineapple juice can be added to digest the proteins wrapped around the DNA. The strings you lift out on a glass rod are millions of double helices tangled together.</p>\n</div>',
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p>In <strong>Experiment 15 &ndash; Nucleic Acids and DNA Extraction</strong> you mash a strawberry in a buffer of dish detergent and salt. The detergent breaks apart the lipid membranes (Chapter 9). The salt&rsquo;s Na<sup>+</sup> ions surround the negatively charged phosphate backbone; this lets the strands clump instead of repelling one another. After filtering, ice-cold alcohol (isopropyl alcohol or ethanol) is layered on top: DNA is much less soluble in alcohol than in water, so it comes out of solution as a white, stringy mass at the boundary. The strings you wind onto a stick are millions of double helices tangled together, plus some RNA and pectin from the fruit. In the same experiment you build nucleotide and base-pair models and separate the bases A, C, T and U by thin-layer chromatography.</p>\n'
  + _link(EXP15) + '</div>',
  "12.3 In the Lab: Experiment 15, strawberry only, no protease",
  "exp15.js Part B: strawberry only, extraction buffer = water + dish detergent + NaCl, filter through cheesecloth, layer ice-cold 91% isopropyl alcohol or 95% ethanol, spool on a wooden stick or glass rod; intro says the product is crude DNA with RNA and pectin. No meat tenderizer, pineapple, cheek or onion. Part A models, Part C TLC of A, C, T, U on silica F254 under UV.")

# ---------------------------------------------------------------- 13.3 (597191)
e(597191,
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Digestion of foods:</strong> you will mix starch with saliva (salivary amylase) or a pancreatin solution at body temperature and follow the hydrolysis with two tests from Chapter 8. The iodine test fades from blue-black as starch disappears, and Benedict&rsquo;s test turns positive as maltose and glucose, both reducing sugars, appear. Boiling the enzyme first, or running the test in strong acid, stops the reaction: enzyme denaturation from Chapter 11 in a test tube.</p>\n</div>',
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Digestion of starch:</strong> in <strong>Experiment 13 &ndash; Enzymes</strong> you mix starch with amylase, the starch-digesting enzyme of saliva and pancreatic juice (the lab uses a purchased amylase), at body temperature and follow the hydrolysis with two tests from Chapter 8. The iodine test fades from blue-black as starch disappears, and Benedict&rsquo;s test turns positive as maltose and a little glucose, both reducing sugars, appear. In a boiling water bath, or in a pH 2 buffer like stomach acid, the starch is not digested: enzyme denaturation from Chapter 11 in a test tube.</p>\n'
  + _link(EXP13) + '</div>',
  "13.3 In the Lab: digestion box tied to Experiment 13 (amylase on starch); saliva/pancreatin removed",
  "The manual has no digestion-of-foods lab. exp13.js uses a commercial alpha-amylase (Instructor Notes) on 1% starch at 37 °C with iodine and Benedict's (A.3), a boiling bath (Part B) and a pH 2 buffer (Part C); no saliva or pancreatin, so only that work is described.")

# ---------------------------------------------------------------- 13.9 (597195)
e(597195,
  'In the metabolism experiment you will test simulated &ldquo;urine&rdquo; samples and connect each result to the hormone picture of this section.',
  'If your course runs a urine-analysis lab, you will test simulated &ldquo;urine&rdquo; samples and connect each result to the hormone picture of this section.',
  "13.9 In the Lab: urine glucose, 'metabolism experiment' made conditional (no manual lab)",
  "The lab manual (Experiments 1-15 and two workshops) has no urine-analysis or metabolism experiment, so the box no longer claims one; chemistry kept, no link.")

# ---------------------------------------------------------------- 15.5 (597213)
e(597213,
  'In the metabolism experiment you will test simulated &ldquo;urine&rdquo; samples for ketone bodies and glucose together.',
  'If your course runs a urine-analysis lab, you will test simulated &ldquo;urine&rdquo; samples for ketone bodies and glucose together.',
  "15.5 In the Lab: urine ketones, 'metabolism experiment' made conditional (no manual lab)",
  "No urine-analysis or metabolism experiment in the lab manual; chemistry kept, no link.")

# ---------------------------------------------------------------- 15.7 (597215)
e(597215,
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Urine analysis, protein:</strong> healthy kidneys keep proteins in the blood, so urine normally has only a trace. The protein pad on a test strip, or the biuret test you used on peptides in Chapter 10, detects protein in simulated &ldquo;urine&rdquo;; a positive result (<em>proteinuria</em>) is a sign of kidney damage, a common complication of diabetes and high blood pressure.</p>\n</div>',
  '<div class="box-note">\n<p class="boxtitle">In the Lab</p>\n<p><strong>Urine analysis, protein:</strong> healthy kidneys keep proteins in the blood, so urine normally has only a trace. The protein pad on a urine test strip detects protein, and so does the biuret test you ran on proteins in <strong>Experiment 12 &ndash; Peptides and Proteins</strong> (Chapter 10). If your course runs a urine-analysis lab, you will use one of these tests on simulated &ldquo;urine&rdquo;. A positive result (<em>proteinuria</em>) is a sign of kidney damage, a common complication of diabetes and high blood pressure.</p>\n'
  + _link(EXP12) + '</div>',
  "15.7 In the Lab: urine protein made conditional; biuret tied to Experiment 12",
  "No urine-analysis lab in the manual; the only manual work here is the biuret test, exp12.js D.1 (glycine, tyrosine, gelatin, egg albumin, casein), so the box links Experiment 12 for that test only.")
