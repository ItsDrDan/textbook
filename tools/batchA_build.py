"""Batch A (wrong content in text), review of 2026-11-12. Builds tools/batchA_content_fixes_2026-11-12.json
and checks each old string's count against pages/live."""
import json, sys
E = []  # (page, old, new, count, note)
def e(p, old, new, n=1, note=""): E.append((str(p), old, new, n, note))

# ---- Ch 1 ----
e(597058, "3 bonds and 1 lone pair, it is bent", "2 bonds and 1 lone pair, it is bent", 1, "1.5 shapes caption")
e(597058, "4 bonds and 1 lone pair, it is trigonal pyramid", "3 bonds and 1 lone pair, it is trigonal pyramid", 1, "1.5")
e(597058, "4 bonds and 2 lone pairs, it is bent", "2 bonds and 2 lone pairs, it is bent", 1, "1.5")
e(597057, "the nonpolar carbon dioxide becomes a gas at &minus;77&deg;C, almost 200&deg; lower than the temperature at which water boils",
          "the nonpolar carbon dioxide sublimes (goes straight from solid to gas) at &minus;78&deg;C, almost 180&deg; lower than the temperature at which water boils", 1, "1.4 CO2")
e(597055, "except that hydrogen is almost never written first (H<sub>2</sub>O is the prominent exception)",
          "except that hydrogen is usually written first when it is bonded to oxygen, sulfur or a halogen (H<sub>2</sub>O, H<sub>2</sub>S, HCl)", 1, "1.2")
e(597059, "Answer b</strong></dt>\n    <dd>\n    <p>This molecule has an alcohol functional group.</p>",
          "Answer b</strong></dt>\n    <dd>\n    <p>This molecule has an alcohol functional group and an amine (N&ndash;H) group.</p>", 1, "1.6 Ex answer b")
e(597060, "It is fine to write the H's to the <em>left</em> of a carbon (HOCH<sub>2</sub>CH<sub>3</sub>) when that shows the bonds more clearly.",
          "It is fine to write a group in reverse at the left end of a formula, such as HO&ndash; in HOCH<sub>2</sub>CH<sub>3</sub>, when that shows the bonds more clearly.", 1, "1.7")
e(597060, "Organic molecules are shown four ways: molecular formula, Lewis (expanded) structure, condensed structural formula, and line (skeletal) structure.",
          "Organic molecules are drawn four ways: Lewis structure, expanded structural formula, condensed structural formula, and line (skeletal) structure.", 1, "1.7 summary")
e(597060, r"\ce{CH2CH2}", r"\ce{CH2=CH2}", 1, "1.7"); e(597060, r"\ce{CHCH}", r"\ce{HC#CH}", 1, "1.7")
e(597060, r"\ce{CH3CHCHCH2CH2CH2CH3}", r"\ce{CH3CH=CHCH2CH2CH2CH3}", 1, "1.7 Table 2")
e(597060, r"\ce{CH2CHCH3}", r"\ce{CH2=CHCH3}", 1, "1.7 Table 2"); e(597060, r"\ce{CHCCH3}", r"\ce{HC#CCH3}", 1, "1.7 Table 2")
e(597061, "Because the fluorine atom has nine protons in its nucleus, it attracts the negatively charged electrons in the bond more than the hydrogen atom does with its one proton in its nucleus.",
          "Because fluorine is much more electronegative than hydrogen, it attracts the negatively charged electrons in the bond more strongly than the hydrogen atom does.", 1, "1.8")
e(597061, "methylamine possesses an &minus;NH group", "methylamine possesses an &minus;NH<sub>2</sub> group", 2, "1.8 Ex 2 + key")
# ---- Ch 2-3 ----
e(597069, "(counting from the <em>right</em> gives this carbon atom a lower number; rule 3)", "(counting from the <em>left</em> gives this carbon atom a lower number; rule 3)", 1, "2.5 Ex 1(c)")
e(597070, ">125</td>", ">126</td>", 1, "2.6 Table 2.6.1 octane, match lecture 126")
e(597073, "<li>ethylcyclohexane</li>\n</ol>\n",
          "<li>ethylcyclohexane</li>\n</ol>\n<div class=\"hideprint answer-inline\"><details class=\"hideprint\"><summary>Answer</summary><div>(a) Cycloheptane, C<sub>7</sub>H<sub>14</sub>: seven CH<sub>2</sub> groups joined in a ring, drawn in line form as a heptagon. (b) Ethylcyclohexane: a cyclohexane ring (hexagon) with one CH<sub>2</sub>CH<sub>3</sub> group attached to one ring carbon. No number is needed because there is only one substituent.</div></details></div>\n", 1, "2.9 Ex 1 answer (no key on page)")
e(597080, "<caption>Boiling points and water solubility of six-carbon hydrocarbons</caption>", "<caption>Boiling points and water solubility of some hydrocarbons</caption>", 1, "3.3 table lists 7-, 8-, 10-C compounds")
e(597081, "with H<sub>2</sub>O (H<sub>2</sub>SO<sub>4</sub> catalyst)</li>\n</ol>\n",
          "with H<sub>2</sub>O (H<sub>2</sub>SO<sub>4</sub> catalyst)</li>\n</ol>\n<div class=\"hideprint answer-inline\"><details class=\"hideprint\"><summary>Answer</summary><div>(a) CH<sub>3</sub>CH<sub>2</sub>CH=CH<sub>2</sub> + H<sub>2</sub> &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (butane). (b) CH<sub>3</sub>CH=CH<sub>2</sub> + Cl<sub>2</sub> &rarr; CH<sub>3</sub>CHClCH<sub>2</sub>Cl (1,2-dichloropropane). (c) CH<sub>3</sub>CH<sub>2</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub> + H<sub>2</sub>O &rarr; CH<sub>3</sub>CH<sub>2</sub>CH(OH)CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (3-hexanol). The alkene is symmetric, so the OH can go on either double-bond carbon and gives the same product.</div></details></div>\n", 1, "3.4 Ex 1 answer")
e(597081, "<h2 class=\"editable\">Answers</h2>\n<div class=\"answer-key-item\">",
          "<h2 class=\"editable\">Answers</h2>\n<div class=\"answer-key-item\"><p><strong>Exercise 3.4.1</strong></p><div>(a) CH<sub>3</sub>CH<sub>2</sub>CH=CH<sub>2</sub> + H<sub>2</sub> &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (butane). (b) CH<sub>3</sub>CH=CH<sub>2</sub> + Cl<sub>2</sub> &rarr; CH<sub>3</sub>CHClCH<sub>2</sub>Cl (1,2-dichloropropane). (c) CH<sub>3</sub>CH<sub>2</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub> + H<sub>2</sub>O &rarr; CH<sub>3</sub>CH<sub>2</sub>CH(OH)CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (3-hexanol). The alkene is symmetric, so the OH can go on either double-bond carbon and gives the same product.</div></div>\n<div class=\"answer-key-item\">", 1, "3.4 key")
e(597085, "contain the same fused three-ring skeleton as phenanthrene, but in steroids the rings are saturated, not aromatic",
          "contain four fused rings: three six-membered rings joined like those of phenanthrene plus a five-membered ring, and in steroids the rings are saturated, not aromatic", 1, "3.8")
e(597085, "from <em>pheno</em>, an old name for benzene", "from <em>phene</em>, an old name for benzene", 1, "3.8")
# ---- Ch 4-5 ----
e(597090, "contains an oxygen atom or a nitrogen atom", "contains an oxygen atom or a sulfur atom", 1, "4.1 (table has thiols, no N family)")
e(597091, "Alcohols with three or more carbons have constitutional isomers", "Alcohols with two or more carbons have constitutional isomers", 1, "4.2")
e(597092, ">&ndash;164</td>", ">&ndash;162</td>", 1, "4.3 Table 1 methane bp")
e(597097, "are barely soluble in water (8 g/100 mL of water)", "are only moderately soluble in water (about 8 g/100 mL of water)", 1, "4.8")
e(597099, "only a tiny fraction of it (well under 1%) is ionized", "only a small fraction of it (about 1%) is ionized", 2, "4.10 Ex 8 + key")
e(597100, "(actual values: &minus;1, 8, 97, and 188 &deg;C)", "(actual values: &minus;1, 7, 97, and 188 &deg;C)", 1, "4.11, ethyl methyl ether bp 7")
e(597101, "(or methyl butyl ether)", "(or butyl methyl ether)", 2, "4.12 Cum 4.5 + key")
e(597101, "(bp &minus;25 &deg;C)", "(bp &minus;24 &deg;C)", 2, "4.12 Cum 4.1 + key, match 4.3/4.8")
e(597103, r"\ce{2Ag(NH3)2^{+}(aq) -&gt; RCOO^{-} +}", r"\ce{2Ag(NH3)2^{+}(aq) + 3OH^{-}(aq) -&gt; RCOO^{-} +}", 1, "5.2 Tollens balanced")
e(597103, "<td data-th=\"Boiling Point (&deg;C)\" style=\"text-align:center;\">6</td>", "<td data-th=\"Boiling Point (&deg;C)\" style=\"text-align:center;\">7</td>", 1, "5.2 table ethyl methyl ether")
e(597103, "(ethyl methyl ether, 6 &deg;C)", "(ethyl methyl ether, 7 &deg;C)", 1, "5.2 lecture")
e(597105, r"\ce{CH3CH2OH + Cr2O7^{2-}(reddish orange) -&gt;[H2SO4 + H2O] CH3COOH + Cr^{3+}(green)}",
          r"\ce{3CH3CH2OH + 2Cr2O7^{2-}(reddish orange) + 16H+ -&gt; 3CH3COOH + 4Cr^{3+}(green) + 11H2O}", 1, "5.4 dichromate balanced")
e(597105, "Antabuse drugs inhibit aldehyde dehydrogenase from converting acetaldehyde to acetic acid",
          "Disulfiram (Antabuse) blocks aldehyde dehydrogenase, so acetaldehyde is not converted to acetic acid", 1, "5.4")
e(597105, r"\ce{2[Ag(NH3)2]OH + R-CHO -&gt; 2Ag(s) + 4NH3 + R-COOH + H2O}\nonumber \]</p>",
          r"\ce{2[Ag(NH3)2]OH + R-CHO -&gt; 2Ag(s) + 4NH3 + R-COOH + H2O}\nonumber \]</p>" + "\n\n<p>(In the basic reagent the acid is present as its carboxylate salt, RCOO<sup>&minus;</sup>.)</p>", 1, "5.4 Tollens vs table")
e(597043, "Red blood cells live about three months", "Red blood cells live about four months (120 days)", 1, "Ch 5 opener")
e(597108, "Glucose does exactly this with itself to form its ring (Chapter 8)", "Glucose does step (a), the hemiacetal step, with itself to form its ring (Chapter 8)", 2, "5.7 Cum 5.2 + key")
# ---- Ch 6-7 ----
e(597109, "is built on the same two-atom unit: a carbon double-bonded to an oxygen with one more bond available.",
          "is built on the same unit: a carbon double-bonded to an oxygen and bonded to an R group, with one more bond available.", 1, "6.1")
e(597111, "(about 1.0 g/100 g of water)", "(about 1.1 g/100 g of water)", 1, "6.3 match Table 6.3.1")
e(597113, "Carboxylic acids have <strong>no positional isomers</strong>, since the COOH is always C1;",
          "The COOH group itself has <strong>no positional isomers</strong>, since it is always C1 (other substituents on the chain can still move);", 1, "6.5 vs 6.12 Problem 6.65(e)")
e(597113, "the name of the acyl group (RCOO) with the", "the name of the acid part (RCOO&ndash;, the acyl group plus its oxygen) with the", 1, "6.5")
e(597115, "Esterification is the first <strong>condensation</strong> reaction of the course:",
          "Esterification is the first <strong>condensation</strong> reaction you write in full in this course (acetal formation in Section 5.3 was a preview):", 1, "6.7")
e(597118, "HA + H<sub>2</sub>O &rarr; A<sup>&minus;</sup>", "HA + H<sub>2</sub>O &#8652; A<sup>&minus;</sup>", 1, "6.10 equilibrium arrow")
e(597118, "R&ndash;NH<sub>2</sub> + H<sub>2</sub>O &rarr; R&ndash;NH<sub>3</sub><sup>+</sup>", "R&ndash;NH<sub>2</sub> + H<sub>2</sub>O &#8652; R&ndash;NH<sub>3</sub><sup>+</sup>", 1, "6.10")
e(597120, "(186 &deg;C versus 99 &deg;C", "(187 &deg;C versus 99 &deg;C", 2, "6.12 P6.54(b) + key")
e(597122, "<td>213 (mp 79)</td>", "<td>213 (mp 81)</td>", 1, "7.2 match Table 7.5.1")
e(597045, "Lidocaine and articaine are amides and benzocaine is an ester, and the amine in each one is why it is sold as a water-soluble hydrochloride salt.",
          "Lidocaine and articaine are amides and benzocaine is an ester. The basic amine in lidocaine and articaine is why each is sold as a water-soluble hydrochloride salt; benzocaine&rsquo;s aromatic amine is too weak a base, so it is used only topically.", 1, "Ch 7 opener vs P7.54(d)")
e(597123, " (its bitter taste is also used to discourage nail biting)", "", 1, "7.3")
e(597127, "Carboxylic Acid and Amide</a>", "Carboxylic Acid and Amine</a>", 1, "7.7 video chapter link (YouTube title too)")
e(597129, "Examples of these drugs include nicotine, morphine, codeine, and heroin. The plant produces these substances",
          "Examples of these drugs include nicotine, morphine, and codeine; heroin is made from morphine in the lab. The plant produces these alkaloids", 1, "7.9")
e(597129, "Figure \\(\\PageIndex{1}\\): Nicotine, morphine, codeine, and heroin are alkaloids.",
          "Figure \\(\\PageIndex{1}\\): Nicotine, morphine, and codeine are plant alkaloids; heroin is made from morphine.", 1, "7.9 caption")
# ---- Ch 8-9 ----
e(597138, "Yes for the three monosaccharides and the right-hand unit of maltose", "Yes for the two monosaccharides (glucose and fructose) and the right-hand unit of maltose", 1, "8.5")
e(597140, "&alpha;(1&rarr;4) chains of about 24&ndash;30 units", "&alpha;(1&rarr;4) chains of about 25&ndash;30 units", 1, "8.7 one range")
e(597142, "Our digestive enzymes (amylases) break only &alpha; glycosidic bonds, so the &beta;(1&rarr;4) links in cellulose pass through",
          "Our starch-digesting enzymes (amylases) break only &alpha; glycosidic bonds, and we have no enzyme for the &beta;(1&rarr;4) glucose&ndash;glucose links in cellulose, so they pass through", None, "8.9 P8.4")
e(597145, "laurate (C(=O)(CH2)12CH3)", "myristate (C(=O)(CH2)12CH3)", 1, "9.2 Fig 9.2.3 alt")
e(597147, "especially abundant in the brain and nerves, in the white matter of the myelin sheath,", "especially abundant in the white matter of the brain and in the myelin sheath,", 1, "9.4")
e(597149, "(240 g is a typical amount)", "(an adult body contains roughly 35 g)", 1, "9.6")
e(597151, "70 &deg;C", "69 &deg;C", 4, "9.8 Cum 9.2 + key, match 9.1")
# ---- Ch 10-11 ----
e(597155, "which has lost a negative charge (Glu &rarr; Val)", "which has lost two negative charges (one Glu &rarr; Val in each &beta; chain)", 1, "10.2 vs 10.12")
e(597155, "<td data-th=\"pI\" style=\"text-align:center;\">9.8</td>", "<td data-th=\"pI\" style=\"text-align:center;\">9.7</td>", 1, "10.2 lysine pI")
e(597155, "lysine about 9.7&ndash;9.8", "lysine about 9.7", 1, "10.2 tip")
e(597159, "HbS carries one less negative charge than HbA", "HbS carries two fewer negative charges than HbA (one per &beta; chain)", 1, "10.6")
e(597165, "Isoelectric points of three amino acids (for the questions below)", "Isoelectric points of four amino acids (for the question below)", 1, "10.12 P10.59")
e(597166, "&mdash;for enzyme classification&mdash;", "&mdash;for Enzyme Commission&mdash;", 1, "11.1")
e(597167, r"\[S + E \rightarrow E&ndash;S", r"\[S + E \rightleftharpoons E&ndash;S", 1, "11.2 Eq 1")
e(597167, "form the type of interaction you just identified.</li>\n</ol>\n</div></section>",
          "form the type of interaction you just identified.</li>\n</ol>\n<div class=\"hideprint answer-inline\"><details class=\"hideprint\"><summary>Answer</summary><div>(a) A negatively charged COO<sup>&minus;</sup> group would form an ionic attraction (a salt bridge) with a positively charged group in the active site. (b) Lysine or arginine, whose side chains carry a positive charge (&ndash;NH<sub>3</sub><sup>+</sup> or a protonated guanidino group) at physiological pH.</div></details></div>\n</div></section>", 1, "11.2 Ex 1 answer")
e(597168, "You will test all four variables in Experiment 13.", "In Experiment 13 you will test three of them (enzyme concentration, temperature and pH), plus an inhibitor.", 1, "11.3")
e(597168, "which gives you every curve on this page from your own data", "which gives you most of the curves on this page from your own data", 1, "11.3 In the Lab")
e(597170, "Needed to make the zymogens (inactive precursors) of prothrombin and other blood-clotting factors",
          "Needed to make prothrombin and the other blood-clotting zymogens (inactive precursors)", 1, "11.5 vit K")
e(597170, "an antioxidant and a clotting cofactor.", "an antioxidant and a helper in blood clotting.", 1, "11.5 cofactor rule")
e(597173, "an antioxidant, and a clotting cofactor.", "an antioxidant, and a helper in blood clotting.", 1, "11.8")
# ---- Ch 12-13 ----
e(597180, "with death usually occurring before the age of three", "with death usually occurring by about age four", 1, "12.7 Tay-Sachs (NINDS)")
e(597180, "know PKU, sickle cell disease, cystic fibrosis and Tay&ndash;Sachs disease.",
          "know PKU, sickle cell disease and Tay&ndash;Sachs disease, plus cystic fibrosis (described under mutations below).", 1, "12.7 CF not in table")
e(597188, r"\overset{|}{C}}=\overset{\LARGE&nbsp;H}{\overset{|}{C}}RR'}_{Double bond}}", r"\overset{|}{C}}-\overset{\LARGE&nbsp;H}{\overset{|}{C}}RR'}_{Single bond}}", 1, "13.1 FADH2/FAD pair")
e(597188, r"but it contains about 1 g of \(\ce{ATP}\) at a time.", r"but it contains only a small pool, roughly 50&ndash;250 g, of \(\ce{ATP}\) at any moment.", 1, "13.1 ATP pool (estimates vary)")
e(597188, "the reverse of photosynthesis happens in the digestion of glucose", "the reverse of photosynthesis happens in the oxidation (catabolism) of glucose", 1, "13.1")
e(597188, "Use the Latin roots and", "Use the Greek roots and", 1, "13.1")
e(597198, "Latin roots:", "Greek roots:", 1, "13.10")
e(597199, "Use the Latin roots.", "Use the Greek roots.", 1, "13.11 P13.65")
e(597194, "Both start from glucose-6-phosphate in the cytosol.", "Both run in the cytosol. Glycolysis starts from glucose; the PPP branches off at glucose-6-phosphate.", 2, "13.6 Ex 4 + key")
# ---- Ch 14-15, back ----
e(597203, r"\(\ce{NADH}\) and \(\ce{FADH}\) are transported", r"\(\ce{NADH}\) and \(\ce{FADH2}\) are transported", 1, "14.4")
e(597203, r"reduce \(\ce{O}\) into", r"reduce \(\ce{O2}\) into", 1, "14.4")
e(597203, "This is the only place in the body where you actually &ldquo;use&rdquo; the oxygen you breathe.", "This is where you actually &ldquo;use&rdquo; nearly all of the oxygen you breathe.", 1, "14.4")
e(597205, "Chapter 13 covered Stages 1 and 2; this chapter is Stage 3, oxidation.",
          "Chapter 13 covered Stage 1 and most of Stage 2; this chapter finishes Stage 2 (pyruvate &rarr; acetyl CoA) and then covers Stage 3, oxidation.", 1, "14.6 match 14.1")
e(597210, "as shown in reactions 1 and 2, respectively, in Figure \\(\\PageIndex{1}\\).", "as described in Section 15.8.", 1, "15.10 moved figure")
e(597210, "as shown in reactions 1 and 3 in Figure \\(\\PageIndex{1}\\).", "as shown in Figure 15.8.1.", 1, "15.10 moved figure")
e(597213, "Once low potassium has been ruled out, potassium is added to the IV fluids to replace this key electrolyte.",
          "Low potassium must be ruled out (or corrected) before insulin is started, because insulin drives potassium into cells; once the potassium level is not high and the patient is making urine, potassium is added to the IV fluids to replace this key electrolyte.", 1, "15.5 DKA")
e(597213, "after two to three days of fasting the brain, which cannot burn fatty acids, gets most of its energy from ketone bodies,",
          "the brain, which cannot burn fatty acids, starts using ketone bodies after two to three days of fasting and gets most of its energy from them after several weeks of starvation,", 1, "15.5")
e(597216, "2 NH<sub>3</sub> (ammonia) + CO<sub>2</sub> + 3 ATP + H<sub>2</sub>O &rarr; H<sub>2</sub>N-CO-NH<sub>2</sub> (urea) + 2 ADP + 4 P<sub>i</sub> + AMP.",
          "NH<sub>4</sub><sup>+</sup> + HCO<sub>3</sub><sup>&minus;</sup> + aspartate + 3 ATP + 2 H<sub>2</sub>O &rarr; H<sub>2</sub>N-CO-NH<sub>2</sub> (urea) + fumarate + 2 ADP + AMP + 4 P<sub>i</sub>. One nitrogen comes from ammonium and the other from aspartate.", 1, "15.9 match table")
e(597216, "the same hydrolysis arginase performs in the liver", "a hydrolysis, the same reaction type as the arginase step that makes urea in the liver", 1, "15.9 urease")
e(597216, "where uric acid crystals accumulate in the joints, as illustrated in Figure \\(\\PageIndex{2}\\).", "where uric acid crystals accumulate in the joints.", 1, "15.9 gout photo not on page")
e(597216, "<p>Figure \\(\\PageIndex{2}\\): Gout causes the inflammation visible in this person&rsquo;s left big toe joint. (credit: &quot;Gonzosft&quot;/Wikimedia Commons)</p>\n", "", 1, "15.9 orphan caption")
e(597219, "A person recovering from surgery is expected to be in positive nitrogen balance", "A person who is eating well and regaining strength in the weeks after surgery is expected to be in positive nitrogen balance", None, "15.13 P15.9")
e(488232, "giving a carboxylic acid and an alcohol (or amine).", "giving a carboxylic acid and an alcohol (from an ester) or an ammonium salt (from an amide).", 1, "Glossary")

L = "pages/live/"
bad = 0; out = {}
for p, old, new, n, note in E:
    t = open(L + p + ".html", encoding="utf-8").read()
    c = t.count(old)
    if n is None: n = c
    flag = "" if (c == n and c > 0) else "  <-- MISMATCH"
    if flag: bad += 1
    print(f"{p} found {c} expect {n} {note}{flag}")
    out.setdefault(p, []).append({"old": old, "new": new, "count": n, "note": note})
json.dump(out, open("tools/batchA_content_fixes_2026-11-12.json", "w"), ensure_ascii=False, indent=1)
print(len(E), "edits on", len(out), "pages;", bad, "mismatches")
