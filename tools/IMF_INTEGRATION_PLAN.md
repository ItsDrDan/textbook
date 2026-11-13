# Sticky Molecules (IMF game) in the CHEM 3B textbook: plan

Drafted 2026-11-13. **Option 1 is live** (published 2026-11-13 on Dr. Dan's OK). Options 2–4 are not published; ADAPT, the Try It bank and GitHub Pages still wait for his OK.

- **Game:** `ItsDrDan/IMF`, v11, live at https://itsdrdan.github.io/IMF/
- **3B view (`?course=3B`):** five tiles: Spot the Forces, Boiling Point Battles, Liquids & Mixing, Cells & Osmosis and Biomolecules.
- **Labs that open in 3B:**
  - H-Bond Lab (`&mode=lab`)
  - Mixing Beaker (`&mode=mix`)
  - Cell Lab (`&mode=cell`)
  - Protein Fold Lab (`&mode=fold`)

  All four links were checked on 2026-11-13; each opens its lab with CHEM 3B selected.

## Where the book teaches intermolecular forces

| Topic | Book section (page id) | Game tile → topic |
|---|---|---|
| The three forces, H bonding, boiling points, like dissolves like | **1.8** (597061) | Spot the Forces; Boiling Point Battles; Liquids & Mixing; H-Bond Lab |
| Family boiling points and solubility | 2.6, 3.3, **4.3**, 4.8, 5.2, 6.3, 6.6, **7.2**, **7.5** | Spot the Forces → Forces in organic families; Boiling Point Battles → Organic boiling points |
| Sugars dissolve; cellulose fibers vs. starch | 8.5, **8.7** (597140) | Biomolecules → Sugars, starch and cellulose |
| Fatty-acid melting points | **9.1** (597144) | Boiling Point Battles → Fatty acids: melting points |
| Soaps, micelles, bilayer, tonicity | 9.2, **9.5** (597148) | Biomolecules → Membranes, soaps and colloids; Cells & Osmosis; Cell Lab |
| Side-chain interactions, folding, denaturation | 10.7, **10.8** (597161), **10.10** (597163) | Biomolecules → Amino acid side chains, Protein folding; Protein Fold Lab |
| Base-pair hydrogen bonds | **12.2** (597176) | Biomolecules → DNA base pairs |

**Hub units vs. book chapters.** The hub card's 3B units are not the same as the book's chapters. In the hub, Unit 2 is Alkanes, Unit 10 is Lipids and Unit 11 is Amino Acids and Proteins. The questionbank export also tags items to Unit 4 (Alcohols), Unit 9 (Carbohydrates), Unit 13 (Nucleic Acids) and Unit 15. The Unit 15 tag (Metabolism and Energy) is on the osmosis and tonicity items, and it looks wrong: they belong in Unit 10, Lipids (see Follow-ups).

## Option 1: Practice Games pages. Published 2026-11-13

**Draft edits:** `tools/imf_games_2026-11-13.json`, built by `tools/imf_games_build.py`. Preview copies of the pages are in `tools/imf_preview/`.

The draft adds a **Sticky Molecules** section to seven Practice Games pages. Each section goes just before the page's Final Boss section, in the `build_games_page` house pattern:
- an h2 heading and the game blurb;
- a chapter-specific "For this chapter" line;
- the embedded game at `?course=3B`;
- an "Open in a new tab" link;
- where it helps, one lab link.

| Page | Id | Focus | Lab link |
|---|---|---|---|
| 1.11 | 597232 | Spot the Forces, Boiling Point Battles, Liquids & Mixing (1.8) | H-Bond Lab |
| 4.13 | 597234 | Organic boiling points; like dissolves like (4.3, 4.8) | Mixing Beaker |
| 7.14 | 597237 | Amines: 1°/2° vs. 3°; amides (7.2, 7.5) | none |
| 8.10 | 597238 | Sugars, starch and cellulose (8.5, 8.7) | none |
| 9.9 | 597239 | Fatty-acid melting points; membranes and soaps; tonicity (9.1, 9.2, 9.5) | Cell Lab |
| 10.13 | 597240 | Side chains and folding (10.7, 10.8, 10.10) | Protein Fold Lab |
| 12.12 | 597242 | DNA base pairs (12.2) | none |

- **Pages left out on purpose:** 2.12, 3.11, 5.8 and 6.13. Their physical-properties sections are short, and 1.11, 4.13 and 7.14 already cover the same comparisons. If you want them, each takes one line in `PLAN`.
- **Pages touched:** only Practice Games pages. None is on the batch L list. All seven repo copies matched live by SHA-256 on 2026-11-13.
- **No new licence line.** The games are embedded by link and are not part of the licensed text, and each page's existing footer already credits the games to ItsDrDan.
- **Published 2026-11-13** through the deki API (contents POST, cookie session). Before each POST the script checked the page's live SHA-256 against the repo copy and the rebuilt body against the preview. LibreTexts then renumbered the `mt-section` ids (the new section takes the Final Boss number). With that renumbering applied, all 7 pages match the previews by SHA-256, and `pages/live/` holds the server form.

**One thing to check before publishing:** the 9.9 tip points to Biomolecules → "Membranes, soaps and colloids". That game topic also asks about colloids and the Tyndall effect, which the book does not teach. Either accept the extra questions, or have the game hide the colloid items for `?course=3B`.

## Option 2: Try It bank and ADAPT. Recommended after review; candidate list drafted

**Draft list:** `tools/imf_deck_candidates_2026-11-13.json`, built by `tools/imf_deck_candidates_build.py`. It covers all 217 items the export tags for 3B and gives a decision for each:

| Decision | Items |
|---|---|
| Keep | 108 |
| Reword first | 4 |
| Drop | 105 |

**Kept and reworded items are in the bank's own format** (builder fixed 2026-11-13; before that, `k` held the index of the right choice and the choices were in game order):
- fields `t`, `q`, `c`, `h`, `w`, `k`, `d` and `x`;
- the correct answer is `c[0]`, `x[0]` is null and `k` is 0 (`k` is the calculator flag);
- the stem has no `<div>` wrapper (56 stems still start with the game's styled figure block);
- **not yet like the bank in one way:** 46 items have 3 choices and 4 have 2 choices (fb-3B-2211, 2212, 2217, 2220); every bank item today has 4. Decide before import;
- `src: "imf-game"` and `from: <IMF id>`;
- provisional ids `fb-3B-2126` upward;
- feedback text with the " ." spacing slip from the export cleaned up.

**Why items were dropped:**
- **2-choice steps** (yes/no, "which is higher?"): a 50% guess. Their 3–4-choice "why" partners are kept.
- **Typed-number items** (6 DNA counts): the decks are multiple choice only.
- **Generated near-duplicates:** 30 of the 36 tonicity variants, plus repeated DNA items.
- **Topics not in the book:** colloids, the Tyndall effect, plant-cell turgor and plasmolysis.
- **Lab-dependent stems** ("this chain", "the box").

**Where the 112 kept and reworded items go:**

| Bank file (`t`) | Items | Sections |
|---|---|---|
| properties | 33 | 1.8 |
| lipids | 34 | 9.1 (10), 9.2 (1), 9.5 (23) |
| proteins | 20 | 10.7, 10.8, 10.10 |
| alcohols / carbonyls / acids_esters / amines / hydrocarbons | 15 | 2.6–7.5 ("strongest force" items for each family, plus 5 solubility items) |
| carbs / nucleic | 10 | 8.5, 8.7, 12.2 |

**Gaps these fill.** The current bank has:
- 0 items on cellulose hydrogen bonding;
- 0 tonicity items in `lipids`, and none anywhere else in the bank (an earlier count of 4 came from regex false positives: "galactonic", "chemiosmotic", "chemiosmosis", "hemolytic anemia");
- few side-chain-pairing items.

**GOB level.** All kept items are qualitative: forces, ranking, where side chains go, what heat breaks. None uses pKa, mechanisms, R/S or E/Z. They follow the book's conventions:
- three IMFs;
- four R-group interactions;
- "polar neutral" Cys;
- crenation and hemolysis.

**Reword before import:**
- **IMF-ed71f91a:** the "ion–dipole" distractor names a force the book does not teach.
- **IMF-07403e27 and IMF-dc0fd8e8:** the stems refer to "the/this protein" from the lab picture.
- **IMF-0d14ac35:** the curdling question says salt bridges; 10.10 says salt bridges and H bonds. Check the wording.

**Proposed steps after review:**
1. Append the kept items to `bank/*.json` in both `textbook-git` and the GitHub Pages copy (`github/textbook/bank`). The existing Try It widgets then draw them with no page edits: Ch 1 `t=properties`, Ch 9 `t=lipids`, Ch 10 `t=proteins`, Ch 12 `t=nucleic`.
2. **ADAPT (course 4605):** create the items through the ADAPT API in the chapter folders, CC BY 4.0, author Daniel Kwasniewski, as was done for the 100 items on 2026-11-12. Then add them to the matching chapter assignments. Suggested caps, so IMF does not crowd the random draw:

   | Chapter | Items |
   |---|---|
   | Ch 1 | ≤ 15 (Ch 1 already has 106) |
   | Ch 9 | 20 |
   | Ch 10 | 15 |
   | Ch 8 | 5 |
   | Ch 12 | 5 |
   | Ch 2–7 | 1–2 each |

   - **Figure items:** 21 kept items have an inline SVG in the stem (DNA ladders, fatty-acid cards, side-chain cards, bilayer). Try It shows them as they are. ADAPT needs them rendered to PNG with alt text through the `tools/render_thin.js` route. That route needs Node, which is not installed on this Mac.
   - **Video hints:** run `tools/adapt_hints_new_2026_11_12.py` with the IMF lesson videos.
3. Add a ledger entry, and update the counts in `adapt/README.md`.

## Option 3: Figures from the labs. One worth making; not drawn yet

**Make it: Protein Fold Lab, "heat breaks attractions, not covalent bonds" (10.10, or 10.8).**
- **Layout:** landscape (about 3:1). Folded chain on the left, heated chain on the right.
- **Labels:** the hydrogen bond, salt bridge and hydrophobic contacts are labeled and let go on the right. The peptide backbone and the disulfide stay.
- **Why it adds something:** 10.10 now has only a folding cartoon and an amyloid figure, and neither shows which links survive heating. It would also give an in-house alternative to 10.8 Figure 1, whose caption lists "coordinate bonds with metal ions". CONVENTIONS says four R-group interactions and no metal coordinate bonds.
- **Credit:** "(Figure: Daniel Kwasniewski, CC BY 4.0.)", in house style, drawn from the lab's own SVG geometry.

**Skip the other labs:**
- **H-Bond Lab:** 1.8 Figures 8–9 already show water and methanol H bonding.
- **Mixing Beaker:** 4.3 already has the ethanol–water figure, and 1.8 has 14 figures.
- **Cell Lab:** done in batch K (9.5.6).
- **DNA base pairs:** 12.2.2 already shows A–T 2 and G–C 3.

## Option 4: In-text practice. Comes for free with Option 2

The book's in-text practice is the Try It widget (`practice.html?t=…&q=…`), and it draws from the bank. Once Option 2 lands, the existing widgets pick up the new items. Two new section widgets would then be worth adding, in a later batch (their filters are thin until the import):
- **9.5 (597148), after Figure 9.5.6:** "Try It: Tonicity", `t=lipids&q=tonic|crenat|hemoly|osmo|saline&n=8`.
- **10.8 (597161):** "Try It: Side-chain interactions", `t=proteins&q=salt bridge|hydrophobic|disulfide|side chain&n=8`.

Neither page is on the batch L list.

## Follow-ups outside this book (not done)

**Game (`ItsDrDan/IMF`):**
- **Fatty-acid melting points that differ from the book's 9.1 table:**

  | Fatty acid | Game | Book |
  |---|---|---|
  | Palmitoleic | 0 °C | 0.5 °C |
  | Oleic | 14 °C | 13 °C |
  | Arachidonic | −50 °C | −49 °C |

  Lauric, myristic, palmitic, stearic, linoleic and linolenic match. These values are on the game's "needs Dr. Dan's review" list.
- **Liquids & Mixing tile:** its 3B blurb mentions vapor pressure, surface tension and viscosity, which are not 3B topics.
- **Fluoromethane:** the claim that it "does not mix well with water" (IMF-e1c9f7fb) is debatable. It is dropped here anyway.

**Questionbank (`ItsDrDan/questionbank`):** the IMF sampler tags the osmosis, tonicity and Cell Lab items to `3B-15` (Metabolism and Energy). They should be `3B-10` (Lipids).

**Book:** the 10.8 Figure 1 caption lists metal coordinate bonds, which contradicts CONVENTIONS. Fix the caption, or replace the figure with the Fold Lab figure above.
