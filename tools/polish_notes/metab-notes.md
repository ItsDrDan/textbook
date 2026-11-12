# metab cluster notes (round 4): 19 edits on 7 pages
Built by work/build_metab.py; validator: pages 46, edits 81, problems 0 (all files merged).

## Task 1: fates of pyruvate (13.4 597192 keeps the full treatment; 13.5 597193 gets a pointer)
- 597193 #1: Learning objective 2 (pyruvate with and without oxygen) changed to "Count the ATP and NADH made in glycolysis and identify the steps that make them," because the fates are no longer taught on this page.
- 597193 #2: "Fate of pyruvate" h3 (aerobic h4, anaerobic h4, Fermentation box) replaced by a 2-sentence pointer to /@go/page/597192. The h3 heading and the Malik adapted-note (still needed for the glycolysis text) are kept verbatim. Div balance is unchanged.
  Moved to 13.4 rather than deleted: link-reaction video (78YEo1BlhuM), the two yeast fermentation diagrams with their CC BY credit line, the "oxidative decarboxylation / link reaction" term, "oxygen debt", the point that delayed soreness is not caused by lactate, and the three overall per-glucose outcomes (written in words as a new paragraph, not as the old mhchem equations).
  Dropped: the jogging photo (decorative; file 436290 is no longer used by this page), the "three enzymes and five coenzymes" detail for the PDH complex (beyond GOB level), and the mhchem overall equations (replaced by the words paragraph). The "lactate is a fuel" and Cori cycle points were already in 13.4. The Fermentation video at the top of 13.5 (YbdkbCU20_M) stays where it is.
- 597192 #4: Aerobic bullet gets the sentence on oxidative decarboxylation / link reaction.
- 597192 #5: Anaerobic bullet: "deep breaths" becomes the oxygen debt wording; the sentence on delayed soreness is added.
- 597192 #6: After Figure 13.4.2, inserts the two fermentation diagrams with their credit line, plus a one-line intro and the link-reaction video.
- 597192 #7: New "Overall, per glucose" paragraph after the NAD+ bookkeeping paragraph.

## Task 2: 14.4 (597203) duplicates
- 597203 #1: "Insulin, the blood glucose-regulating hormone" box removed. NOTE: 14.5 has no insulin content; the box repeats 13.9 (597195), which teaches insulin fully (GLUT4, glycogenesis, lipogenesis, gluconeogenesis off). No pointer was added because insulin is off-topic for oxidative phosphorylation. Nothing in the box was unique.
- 597203 #5: "Account of ATP production" section: the conversion paragraph, the 10-NADH overall equation and Table 1 (the second 32-ATP tally) are replaced by a pointer to /@go/page/597204 plus a short 2.5/1.5/GTP explanation. The net 32-ATP overall equation is kept because it appears nowhere else. The h2, adapted-note, and cyanide Molecule-in-the-Clinic box are kept.
- Checked 14.5 (597204): it has the full tally (32 malate–aspartate / 30 glycerol-3-P), 2.5/1.5, 10 per acetyl CoA, 36–38 older values, and 35% efficiency. This matches CONVENTIONS.md. No change was needed.

## Task 3: figure renumbering
- 597192 #1–#2: Figure \(\PageIndex{3}\) → \(\PageIndex{1}\) (in-text ref + caption).
- 597192 #3: Figure 13.4.4 → 13.4.2 (caption; no in-text refs).
- 597203 #2: The uncaptioned summary image (file 436865) is the image that the text already called "Figure \(\PageIndex{3}\)" (twice). It is wrapped in <figure> with the caption "Figure \(\PageIndex{3}\): …" so the references resolve. Before this, there was no Figure 3 caption.
- 597203 #3: "two forms of fermentation shown in Figure \(\PageIndex{3}\)" → \(\PageIndex{4}\) (fermentation is in the respiration.svg figure, Figure 4).
- 597203 #4: Figure 14.4.1 → 14.4.5 (was a duplicate of \(\PageIndex{1}\)).
- 597200 #1: Figure 14.1.1 → 14.1.3 (was a duplicate of \(\PageIndex{1}\); "Video \(\PageIndex{1}\)" is a separate counter and was left alone).
- 597201 #1: Figure \(\PageIndex{2}\) → \(\PageIndex{1}\) (3×: 2 in-text, 1 caption).
- 597201 #2: Figure \(\PageIndex{3}\) → \(\PageIndex{2}\) (3×: 2 in-text, 1 caption).
- 597148 #1: Figure 9.5.1 → 9.5.5 (was a duplicate of \(\PageIndex{1}\); \(\PageIndex{1}\)–\(\PageIndex{4}\) are already in order).
- 597177 #1: Figure 12.3.1 → 12.3.3 (was a duplicate of \(\PageIndex{1}\)).
- No change needed: 597193 (\(\PageIndex{1}\), 13.5.2), 597204 (14.5.1–2), 597128 (7.8.1–2), 597156 (no numbered figures), 597183 (12.5.1–3).
- No other page cites any of the renumbered hard-coded figure numbers.

## Task 4: other duplicated passages (reported, not fixed)
- 13.4 within the page: the Ball "Metabolism of Pyruvate" paragraph + Figure \(\PageIndex{1}\) (fates of pyruvate) repeats the Lecture Connection "Three fates of pyruvate" list + Figure 13.4.2. There are two fates-of-pyruvate figures on one page.
- 13.4 Table \(\PageIndex{1}\) (the full 30–32 ATP tally) and the shuttle paragraph in "ATP Yield from Glycolysis" repeat the 14.5 tally and the 14.5 shuttle section. 13.4's own text says only the glycolysis rows are taught there.
- The 35% efficiency calculation appears in 13.4, 14.4 ("Heating the body", per NADH) and 14.5 ("How efficient is it?").
- 14.1 (597200) "Getting in: pyruvate → acetyl CoA" (PDH, NAD+/CoA/thiamine, 2 NADH + 2 CO2) repeats the aerobic bullet in 13.4. The 14.1 Thiamine/Wernicke Clinical Connection repeats the thiamine half of the 13.4 Nursing box.
- 14.2 (597201) Ball "Electron Transport" text + Lecture "Electron transport: order of appearance" (CoQ, cytochrome c, FADH2 skips Complex I → 1.5 ATP) repeat the 14.4 "Four stations, two shuttles" list and the "Why 2.5 and 1.5" paragraph. 14.2 Table \(\PageIndex{1}\) (10 ATP per acetyl CoA) repeats 14.5 Example 2(a) and the 14.2 Professor Tip.
- 14.4 "Summary of glucose catabolism" + "Comparison of ATP yield" (2 ATP before the cycle, 6 NADH, 2 FADH2, 2 GTP, 10 NADH; anaerobic 2 ATP) repeat the 14.5 bookkeeping list and "Aerobic versus anaerobic".
- 14.4 within the page: CO/cyanide → Complex IV → lactate → hydroxocobalamin is told three times (Valley Connection, Molecule in the Clinic, Clinical Connection: Nursing). The Ball/Malik electron transport section repeats the Lecture "Four stations" list. "Heating the body" brown fat repeats the Health Career newborn thermoregulation bullet.
- Lactate/shock/sepsis clinical material appears in 13.4 (Example 2 + Nursing box), 14.4 (Nursing: sepsis) and 14.5 (Nursing: shock).
- Dental caries as glycolysis → lactic acid appears in 13.5 (Dental Hygiene box) and 14.4 (Dental Hygiene: "Plaque bacteria run on fermentation").
- Side finding, not a duplicate: in the 14.2 (597201) print answer key, the entry titled "Example 1: Oxidized or reduced?" actually holds the answer to the Practice item ("The reduced form of nicotinamide adenine dinucleotide…").
