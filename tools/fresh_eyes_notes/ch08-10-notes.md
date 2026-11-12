# ch08-10 draft edits: notes (34 edits, 16 pages; nothing applied to repo)

## Tier 1
- 597164 10.11 Chapter Guide, Key Idea 1: "Nine are essential" → "Ten are essential … this course counts arginine as the tenth" (CONVENTIONS).
- 597144 9.1 adapted-source table: arachidonic acid condensed formula → CH3(CH2)4(CH=CHCH2)4(CH2)2COOH (C=C at C5,8,11,14; omega-6). Old one placed C=C at C4,7,10,13 (omega-7). Same <sub> markup.
- 597139 8.6 To Your Health: galactosemia "need to restrict milk is not permanent" → diet is lifelong; newborn screening mentioned.
- 597163 10.10 lecture table: "which is why it sterilizes" → "disinfects (… does not sterilize)".
- 597163 10.10 section text: prion paragraph split in two: prions = CJD and mad cow disease; Alzheimer's, Parkinson's, Huntington's and familial amyloidosis are misfolding diseases but not prion diseases.
- 597163 10.10 lecture "Misfolding": spreading and autoclave resistance are now attributed to prions only.
- 597146 9.3 IRDS, three edits: (1) surfactant = mostly phospholipid plus some protein, main component DPPC (a lecithin); lecithin = phosphatidylcholine; phosphatidic acid kept and correctly described (fits the existing image anchored in that paragraph). (2) Risk highest before ~28 weeks, still significant to ~34 weeks. (3) Nonstandard L/S bands replaced with "about 2 or more suggests mature lungs", framed as an older test; antenatal corticosteroids to the mother, surfactant, ventilator.
- 597154 10.1: Ball table arginine "almost as strong a base as sodium hydroxide" → "the most strongly basic side chain (a guanidinium group); +1 at pH 7.4". The lecture "Basic" rule is rewritten (only His, Lys, Arg; the amide N of Asn/Gln and the ring N of Trp are not basic). The hydrophilic definition now says "extra amine-type nitrogen" so Trp is not swept in.

## Tier 2
- 597155 10.2 lecture: "switch flips at about pH 2 … pH 9–10" paragraph replaced with a no-number version; "pI sits halfway between … (about 2) … (about 9–10)" → "Amino acids with a neutral R group have pI values near 6." Everything else in the paragraph (Asp/Glu/Lys/Arg/His pI values) is unchanged.
- 597157 10.4 Example 1: Asp side-chain charge now justified by category (carboxylic acid loses H+ at body pH), not "pI near 3".
- 597159 10.6: "two resonance contributors, as shown below" → "behaves partly like a double bond"; "about 40% double bond character … no free rotation" → "planar and does not rotate"; the "(shown in blue in the structure above)" pointer is removed.
- 597158 10.5 adapted text: "hydrophobic interaction is often misused…" → "In this course … are called hydrophobic interactions. They arise because…"
- Lipase (spec decision): 597145 9.2 lecture list item (fat cells = complete; digestion = 2 FA + monoacylglycerol); 597150 9.7 Example 5 problem reframed to fat-cell lipases, with a digestion caveat in Check; 597151 P9.65(a) question → complete hydrolysis with an acid catalyst; answer (c) updated with an intestine caveat (inline + key, count 2); P9.55(c) "releasing fatty acids (and glycerol when hydrolysis is complete)" (inline + key, count 2).
- 597139 8.6: removed the "about 70% of the world's adult population" and "Up to 20% of the US" sentences; points to the NIH figures in the Valley Connection. Also removed "adults usually have a less active form of the enzyme" (it is reduced production, not a different form).
- 597139 8.6 trisaccharide alt texts: I viewed both images (files 128189 and 128188).
  - Example (128189): the 1–2 link points up (β) and the 2–3 link points down (α), matching the written solution. The alt text was reversed and is now fixed.
  - Exercise (128188): both links point UP (β, β). The old alt text said ring 2 was α. Now fixed. No answer is printed for the Exercise on the page.
- Glycogen spacing → about every 8 to 12 units: 597140 lecture table (was 10–15) and 597141 Guide Exercise 3 (was "about every 10"). The 597140 adapted text and the 597142 P8.51 answer already said 8–12, so no edit was needed there.
- 597140 glycogen breakdown: in the table, "Glucose is hydrolyzed from the chain ends" → "The enzyme glycogen phosphorylase breaks glucose units off the chain ends"; in the nursing box, "liver hydrolyzes glucose from…" → "breaks glucose units off…".

## Tier 5
- 597137 8.4 Learning Objectives: added "<li>Convert a Fischer projection to a Haworth projection and back, and label the α and β anomers.</li>".

## Validation note
Tag balance was checked as net (opening − closing) for p/td/li in old vs new. Two edits intentionally add a complete element:
- 597163 prion split adds one <p>…</p>.
- 597137 adds one <li>…</li>.
A raw open-count equality check would flag those two; they are balanced.

## Not done / needs follow-up
- 597159 10.6 resonance image (file 431968, `clipboard_ec460cf1acff2449ad2cd8f4913cb30e9.png`) still shows red curved arrows; this violates the no-curved-arrow rule.
  - Recommend removing it. Exact old string to delete: the whole `<p class="mt-align-center"><img alt="Two resonance contributors of the peptide bond … carries a negative charge." … fileid="431968" /></p>` paragraph (count 1), new = "".
  - Alternatively, redraw it as a single planar peptide unit with no arrows.
  - Its alt text is still accurate for the image as it stands, so I did not change it.
- The 8.6 Exercise trisaccharide is β,β per the image, so there is no α/β contrast; if a contrast is wanted, the image would need a redraw. The Ball original may have intended α,β.
