# rxn cluster notes: drawn examples for new "Reactions at a Glance" rows

- 597086 (3.9), 1 edit: after the last drawn example (Hydration, fileid 512455), added 4 figures: addition polymerization (n CH2=CH2 -> -(CH2-CH2)n-, condensed text, no reagent over the arrow because Section 3.5 names none), bromination (Br2, FeBr3; bromobenzene + HBr), nitration (HNO3, H2SO4; nitrobenzene + H2O), sulfonation (SO3, H2SO4; benzenesulfonic acid).
- 597100 (4.11), 1 edit: after Oxidation of a 2° alcohol (fileid 512472), added 3 figures: hydration (propene -> 2-propanol, "H2O, H+ catalyst"), combustion (ethanol + 3 O2 -> 2 CO2 + 3 H2O, "flame" over the arrow; O2 is shown on the left with its coefficient so the equation is visibly balanced), thiol oxidation (2 ethanethiol -> diethyl disulfide, "[O]").
- 597107 (5.6), 1 edit: after Acetal formation (fileid 512490), added 1 figure: acetal hydrolysis (1,1-dimethoxyethane -> ethanal + 2 CH3OH, "H2O, H+").
- Markup: each new item keeps the existing <p style="margin:.8em 0 .2em"><strong>Row name</strong></p> heading and img attributes, but the img sits in <figure class="figure"> with a <figcaption> ending "(Diagram: Daniel Kwasniewski, CC BY 4.0.)", the book's usual pattern for figures. The older items have no captions. The footer "Reaction examples drawn with the Bond Voyage! engine" is unchanged. These new ones were drawn with RDKit, and each caption carries its own credit.
- Placeholders: src="/@api/deki/files/FILEID__<name>/<name>" and fileid="FILEID__<name>". Replace both with the real file id after upload. Upload each SVG to its own page: p597086 -> 597086, and so on.
- The img width attributes are 1.2 times the SVG's native width (358-626 px), which matches the existing 438-760 px range.
- Checks: RDKit formula and element balance for each equation (rxn_draw_log.txt). Every equation balances. For the thiol, the [O] is counted as O -> H2O. PNG previews were viewed in rxn_png/.
- Nothing skipped.
- Script: rxn_draw.py (SVGs), rxn_edits.py (JSON).
