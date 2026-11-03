# Author brief – CHEM 3B OER textbook enhancement (read fully before writing)

You are writing for **"Introductory Organic and Biological Chemistry for FCC"**, a free LibreTexts remix (Ball et al., *The Basics of GOB Chemistry*, plus a few sections from *Fundamentals of GOB Chemistry (LibreTexts)*) built by Dr. Dan (Daniel Kwasniewski), chemistry instructor at Fresno City College, for CHEM 3B. Students: mostly pre-nursing, dental hygiene, radiologic technology, respiratory therapy. They have had CHEM 3A (intro general chemistry). Course outline: `tools/COR_outline.md` – **everything you write must sit inside that outline; never add topics beyond it, never drop below it.**

## What you edit
Drafts live in `/mnt/user-data/outputs/CHEM3B_LibreTexts_Drafts/`:
- `ChNN_Chapter_Guide_*.html` – Dr. Dan's own chapter guide (Learning Objectives → Key Ideas (numbered `<h3>`s) → Video Lessons → Worked Examples → Common Mistakes → Practice). **Edit in place.**
- `ChNN_Practice_Problems_*.html` – 40–60 original problems in `box-exercise` blocks with `<details>` answers. **Edit in place (append new problems; keep numbering continuous `Problem N.k`).**
New full section pages (only when your assignment lists them) go in `/home/claude/textbook/sections/chNN_<pageid>.html`.

A build script later inserts reaction-scheme figures and "Try It" widgets after specific `<h3>` headings and before `<h2>Practice</h2>`, and renumbers `<figcaption>Figure N.x:` in document order. Therefore:
- **Do not rename or delete any existing `<h2>`/`<h3>` heading text.** You may add new `<h3>` sections (continue the numbering, e.g. `<h3>8. …</h3>`) and new content inside sections.
- Keep `<h2>Practice</h2>` exactly as is; keep the `Health Career Connection` box-note (you may extend it).
- Number new figures `Figure N.0:` (they get renumbered) – but every figure must have a `<figcaption>Figure N.0: …</figcaption>`.
- Pages are HTML *fragments* (no `<html>/<head>/<body>`), pasted into LibreTexts. Scripts are stripped; inline `<svg>` and standard HTML survive.

## OER standards (non-negotiable)
1. **All prose, examples and problems are original.** Do not copy or closely paraphrase Timberlake, McMurry, OpenStax, Wikipedia or the Pearson test bank. Explain in your own words; use your own molecules and numbers. Never reproduce a homework or exam question.
2. **Licensing/attribution**: new full section pages end with the attribution box (template below). Figures drawn with the tools below get the caption suffix "(Structures drawn with the Bond Voyage! engine.)" or "(Diagram: Dr. Dan, CC BY-NC-SA 4.0.)".
3. **Accessibility**: heading levels in order (h2 → h3, no skips); every `<img>`/`<svg>` has meaningful `alt`/`aria-label`; tables have `<th>` headers and a short lead-in sentence; never rely on color alone; abbreviations spelled out on first use; `<details><summary>Answer</summary>` for hidden answers.
4. **Accuracy over flourish.** Every chemical fact, pKa-level claim, enzyme name, pathway count (ATP/NADH), drug class and clinical statement must be correct at the GOB-textbook level. If a number is textbook-dependent (e.g., ATP per glucose 30–32 vs 36–38), state the convention this book uses: **modern values 2.5 ATP/NADH, 1.5 ATP/FADH₂ → 30–32 ATP per glucose (32 with the malate–aspartate shuttle, 30 with the glycerol-3-phosphate shuttle)**; mention that older texts say 36–38.
5. **Scope discipline**: GOB level. No mechanisms with arrows, no SN1/SN2, no detailed organic synthesis, no pharmacology dosing. Clinical content is context for the chemistry, not medicine instruction; no treatment advice.

## Voice and style
- Clear, warm, direct second person ("you"), short paragraphs, concrete before abstract. Define every technical term when first used. No filler, no hype, no emoji.
- Use the existing CSS vocabulary only: `box-objectives`, `box-note` (with `<p class="boxtitle">Professor Tip</p>` for tips; `Health Career Connection`; `In the Lab`; `Clinical Connection: Nursing`; `Clinical Connection: Dental Hygiene`), `box-example` (worked examples: `<p class="boxtitle">Example k: …</p>` then **Problem / Solution / Check** structure), `box-exercise` (problems), `figure class="figure"` + `figcaption`, `table class="mt-responsive-table"` with `<thead>`.
- Chemistry notation: subscripts/superscripts with `<sub>`/`<sup>`; use &rarr; &harr; &deg; &ndash; entities; 1&deg;/2&deg;/3&deg;; Greek via entities (&alpha; &beta;).
- "Professor Tip" (never "Dr. Dan says"). Refer to the games by their names (Bond Voyage! Organic Reactions, Organic Origins, Carb Lab, Peptide Builder, Final Boss, Lewis Structure Studio, Flash cards). Videos: Dr. Dan's YouTube CHEM 3B playlist is already in each guide – do not invent new video links.

## Medical terminology and health-profession examples (required where natural, never forced)
Weave in correctly used medical terminology with a one-phrase definition on first use, e.g. *xerostomia* (dry mouth), *dental caries* (tooth decay), *gingivitis/periodontitis*, *demineralization/remineralization* of enamel (hydroxyapatite), *plaque biofilm*, *halitosis*, *hyperglycemia/hypoglycemia*, *diabetic ketoacidosis (DKA)*, *hyperlipidemia*, *atherosclerosis*, *jaundice*, *edema*, *acidosis/alkalosis*, *NPO*, *IV infusion (D5W = 5% dextrose in water, lactated Ringer's)*, *HbA1c*, *lipid panel (LDL/HDL/triglycerides)*, *liver enzymes (ALT/AST)*, *cardiac enzymes (CK-MB, troponin)*, *phenylketonuria (PKU)*, *lactose intolerance*, *galactosemia*, *G6PD deficiency*, *sickle cell disease*.
Dental-hygiene chemistry you may use (all within COR topics): fluoride and hydroxyapatite → fluorapatite (ionic, review only), acid produced by plaque bacteria from sugars (glycolysis → lactic acid, critical pH ≈ 5.5), sugar alcohols (xylitol, sorbitol) in sugar-free gum, chlorhexidine (a bis-biguanide, an amine-containing antiseptic), eugenol (a phenol, clove oil, in temporary cements), local anesthetics as amides (lidocaine, articaine, mepivacaine) vs esters (benzocaine, procaine), epinephrine in anesthetic (amine), nitrous oxide, methacrylate (ester) resins and acrylic (PMMA) for composites/dentures, alginate (polysaccharide) impressions, collagen in gingiva/periodontal ligament, salivary amylase and lysozyme, salivary buffering (bicarbonate), bleaching with hydrogen/carbamide peroxide (oxidation), chewing gum sweeteners (aspartame = a methyl ester dipeptide; PKU warning).
Nursing chemistry you may use: isopropyl alcohol swabs, ethanol/methanol/ethylene glycol metabolism by alcohol dehydrogenase (why fomepizole/ethanol are antidotes – concept only), acetaminophen (an amide + phenol) and aspirin (an ester + carboxylic acid; salicylate), ibuprofen (carboxylic acid), nitroglycerin (nitrate ester), opioid alkaloids (amines; morphine has a phenol), epinephrine/norepinephrine/dopamine (catecholamines), statins and cholesterol, lipid panel, omega-3 (EPA/DHA), fat-soluble vitamin toxicity, insulin (a peptide hormone; cannot be taken orally – hydrolysis), glucagon, lactate (lactic acidosis, sepsis), DKA ketones (acetone breath), HbA1c (glycation), heparin (polysaccharide), urea/BUN and creatinine, hyperammonemia and hepatic encephalopathy, transaminases, enzyme markers of MI, cyanide/CO and electron transport, uncouplers and fever, G6PD deficiency and oxidative drugs, sickle-cell mutation (Glu → Val), cystic fibrosis, PKU diet, lactose-free formula, parenteral nutrition.
Keep each clinical box 80–180 words, concrete, and tie it to a chemistry skill the student just learned.

## Figure tools (run from `/home/claude/textbook`)
- Structure: `node tools/draw.js struct "<SMILES>" [skeletal|expanded|condensed]` → inline SVG (condensed gives HTML text). Write phenol as `OC1=CC=CC=C1`, benzene `C1=CC=CC=C1`.
- Reaction scheme from the game's templates: `node tools/draw.js rxn <key> "<regex on reactant name>"`; keys: `node tools/draw.js rxnlist`.
- Pathway / flow diagrams: write a JSON spec and run `node tools/pathway.js spec.json > out.svg` (header of `tools/pathway.js` documents the spec: nodes on a col/row grid, kinds mol/energy/enzyme/note/tissue/start, edges with labels/via points). Use it for every metabolic pathway, cycle, regulation diagram or concept flow. Use `colw` 170–200 for long labels; put edge labels on longer edges; check for overlaps.
- Preview any fragment: `python3 tools/preview.py page.html out.png 900 [maxheight]`, then look at the PNG with the Read tool. **Look at every figure you make** and fix overlaps/clipping before you finish.
- Wrap figures: `<figure class="figure"><svg …>…</svg><figcaption>Figure N.0: …</figcaption></figure>`. Give the `<svg>` `role="img" aria-label="…"` (pathway.js does this from `alt`).
- Do not use external images. Existing SlideNN.png figures stay as they are.

## Problems (end-of-chapter)
Add **10–14 new original problems per chapter** to the Practice Problems page: continue the numbering; include 3–4 multiple choice, 2 "compare and contrast / predict", 2 "analyze the graphic/table/data" (you may embed a small table or figure), 2–3 clinical-application items (nursing or dental hygiene scenario that turns on the chemistry), 1–2 integrative items linking chapters. Every answer gives the reasoning, not just the letter. Put them under a new `<h2>More Practice: Clinical and Integrative</h2>` (and `<h2>More Practice: Analyze and Compare</h2>`) before the end of the file. No exact or near-exact homework/exam questions.

## Full section pages (stub replacements) – required structure
```
<div class="box-objectives"><p class="boxtitle">Learning Objectives</p><ul>…3–5 items…</ul></div>
<p>lead paragraph that says why this matters to a health-career student</p>
<h2>…</h2> sections with figures, tables, a Professor Tip, 2–3 box-example worked examples (Problem/Solution/Check)
<div class="box-note"><p class="boxtitle">Clinical Connection: Nursing</p>…</div>   (and/or Dental Hygiene)
<h2>Summary</h2><ul>…</ul>
<h2>Exercises</h2> 5–8 box-exercise items with <details> answers
<div class="box-note"><p class="boxtitle">Attribution</p><p>Written by Dr. Dan (Daniel Kwasniewski), Fresno City College, for CHEM 3B, with AI assistance; reviewed by the author. Licensed <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener">CC BY-NC-SA 4.0</a>. Structures drawn with the Bond Voyage! engine.</p></div>
```
Target 1,200–2,000 words, 2–4 figures. These pages replace empty placeholders in the LibreTexts "Fundamentals of GOB" book, so they must be complete, standalone lessons.

## Guide enhancements – what "polished" means here
- Fill every COR gap for the chapter with real teaching (a short explanation, one figure or table, one worked example), not a sentence.
- Add a `Clinical Connection: Nursing` and a `Clinical Connection: Dental Hygiene` box (or extend the Health Career Connection) with correct terminology.
- Add at least one new worked example in Problem/Solution/Check form that mirrors the kind of task the COR objectives describe (name↔structure, predict product, rank by property, classify).
- Add 2–3 Common Mistakes if the list is thin.
- Tighten wording; fix any inaccuracies you notice (report them).
- Do not bloat: aim for +25–45% length, every addition earning its place.

## Verification before you finish
1. `python3 -c "import html.parser"` style sanity is not enough – open your edited files in the preview tool and read the PNG; check figures, tables, boxes.
2. Run `python3 tools/check_fragment.py <file>` for every file you touched (balanced tags, headings present, no scripts, alt text, no external images).
3. Re-read every clinical sentence and every number; cross-check reaction products and names; make sure no COR topic for your chapter is missing and nothing out of scope slipped in.
4. Report back (concise): files changed; new sections added (titles); figures created; problems added (count and numbers); any inaccuracy you fixed in existing text; anything you were unsure about.

## Addendum
- `tools/draw.js` cannot lay out fused rings (indole, purine, naphthalene, steroids, nucleobases). For those, use `tools/molsvg.py` (hand-placed atoms/bonds in the same visual style; read its header and the example at the bottom) or write a clean hand SVG; caption credit "Diagram: Dr. Dan, CC BY-NC-SA 4.0."
- Guides from chapters 1–8 ended up roughly 2–2.5× their original length because they absorbed the COR build-outs; that is acceptable. Clinical boxes may run to ~220 words when the assignment lists many items.
- Nested `<svg>` elements inside a composed figure should carry `role="presentation"`; the outer one carries `role="img" aria-label`.
