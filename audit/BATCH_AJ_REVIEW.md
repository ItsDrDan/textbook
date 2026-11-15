# Batch AJ review: hands-on labs from the study games (2026-11-14)

Author's request: "Add the six" demos from `RENAISSANCE-2026-11-14/INTERACTIVE_DEMOS_FOR_TEXTBOOKS.md`, test them in the iOS simulator, fix what is needed, check the code and the fit with each section, and add the H-Bond Lab to 1.8 if the page has room. Published 2026-11-14: games pushed to main first, then the seven pages (dry run and read-back 7/7).

## The seven boxes

| Section (page) | Box | Game link (compact view) | Where on the page | Frame |
|---|---|---|---|---|
| 4.1 (597090) | Hands-on Lab: Spot the group | `organic/?mode=spot&groups=alcohol,phenol,ether,thiol,alkene&view=lab` | "Sorting a molecule into the right family", before the Professor Tip | 560 px |
| 9.2 (597145) | Hands-on Lab: Build and break fats | `lipids/?topic=lab&view=lab` | End of "The three reactions", before "Oxidation of fats" | 600 px |
| 10.2 (597155) | Hands-on Lab: pH Dial | `pHcharge/?topic=dial&view=lab` | After the worked examples, before the second Try It | 640 px |
| 10.4 (597157) | Hands-on Lab: Condense and hydrolyze | `aminoacids/?mode=build&view=lab` | End of "Condensation builds it, hydrolysis breaks it" | 560 px |
| 11.3 (597168) | Hands-on Lab: Enzyme Bench (free play), plus a link to the guided lab (`?topic=bench&fam=temp,pH,sub`) | `enzymes/?explore=1&view=lab` | End of "Four variables, four curves", before "Worked examples" | 640 px |
| 11.4 (597169) | Hands-on Lab: Inhibitors on the Enzyme Bench | `enzymes/?topic=bench&fam=inh&view=lab` | End of "Competitive, noncompetitive, irreversible" | 600 px |
| 1.8 (597061) | See It Move: H-Bond Lab (link only, no frame) | `IMF/?course=3B&mode=lab&view=lab` | End of "Hydrogen Bonding Intermolecular Forces" | none |

Each framed box follows the Try It pattern (box-note, frame, "Not loading? Open this lab in a new tab"), with a green border so it reads as a lab, not a quiz. In print, the frame and the "Not loading?" line are hidden (`hideprint`) and one line says the lab is online (`showprint`).

**1.8 gets a link, not a frame.** 1.8 is the longest page in the book (about 7,900 words) and already holds five frames (three videos, two practice frames). The H-Bond Lab is also already linked from 1.11 Practice Games.

## Changes made to the games (local branches `book-links`, not pushed)

| Game | Change | Why |
|---|---|---|
| all six (organic, lipids, pHcharge, aminoacids, enzymes, IMF) | `?view=lab`: shows only the demo plus "Open the full game" | **Phone bug found in testing:** a full game inside a page is 1,000 to 3,500 px tall, so on an iPhone a swipe on the box scrolled the game, and the student had to scroll through the whole game to get back to the reading. With the compact view the box can stay at 560 to 640 px, and a swipe outside it scrolls the page; at the end of the box the swipe passes on to the page. |
| enzymes | `?explore=1` opens free play; `?fam=temp,pH,sub` or `?fam=inh` picks which lab families appear | No link could open free play, and 11.3 vs 11.4 need different families |
| organic | `?mode=spot` opens Spot It; `?groups=` limits which groups it asks about | The game read no mode from its link. Spot It asks about all 17 groups; 4.1 has taught only alcohol, phenol, ether and thiol (sulfide and disulfide come in 4.9), so the 4.1 box asks about those plus the alkene from Chapter 3 |
| aminoacids | `?mode=build` opens Condense & Hydrolyze; in the compact view the phone-only sticky button row scrolls normally | The game read no link at all; in a 560 px box the sticky Check/Hint row covered the amino acid cards |
| pHcharge, lipids, enzymes | Inside a frame, a `?topic=` link opens at the question instead of the title banner | Otherwise the box opened on the game's header |
| organic, aminoacids, enzymes | Load-time jump uses an instant scroll and re-runs after the page loads, unless the student has already scrolled | The games' smooth-scroll setting cancelled the jump on load |

Tests: enzymes `tools/check-bench.js` (54,000 checks), organic `tools/check-organic.js`, pHcharge `tools/check-dial.js` all pass; every game's script passes a syntax check. Each branch was rebased onto the other session's same-evening pushes (reasons text in enzymes, aminoacids, lipids; IMF v24) with no conflicts.

## Phone test (iOS simulator, Safari, real taps)

Device: iPhone 18 Pro Max (the iPhone 17e and 18 Pro were in use by other sessions). Each box was tested inside a local copy of its section page:

- **10.2 pH Dial:** predicted −2 for aspartic acid in strong base, dragged the dial to strongly basic; the "What changed" table filled in and said the prediction was right. Swiping inside the box scrolled the lab; past its end the page scrolled.
- **4.1 Spot It:** a wrong tap on a sulfur said it belongs to the disulfide group and asked for the alkene; a right tap (thiol on cysteine, earlier run) lit the group and gave the explanation.
- **9.2 Build and break fats:** tapped the fatty acid –OH and the glycerol H; both selected.
- **10.4 Condense and hydrolyze:** tapped His first for histidylprolylserine; it joined the chain. Before the sticky-row fix the button row hid the cards.
- **11.3 Enzyme Bench free play:** the graph stays pinned while the controls scroll; switching the axis to temperature drew the curve peaking at 37 °C and falling past 45 °C.
- **11.4 inhibitor lab:** opened on a competitive-inhibitor round with the "no inhibitor" comparison curve.
- **1.8 H-Bond Lab (compact view):** answered the prediction; feedback and XP appeared.

Not tested: real phones; LibreTexts' own page around the frame (the test pages copy the section HTML without LibreTexts' styles); Android.

## Fit with each section (checked against the live text)

- 11.3 says most human enzymes work best near 37 °C, denaturation between 45 and 55 °C, pepsin at pH 2.0 and trypsin near 8; the game uses 37 °C, denaturation at 45 °C, pepsin 2, trypsin 8. One small difference: the game's "typical body enzyme" works best at pH 7, and 11.3 says "near pH 7.4". Left as is (compatible); say if you want the game changed to 7.4.
- 10.2 uses the pI and no pKa values; so does the dial (your 2026-11-11 rule).
- 10.4: the game draws neutral amino acids (H<sub>2</sub>N–…–COOH) when building, as in Figure 10.4.3's hydrolysis row.
- 4.1: see the `groups=` limit above. Tasks drawn on molecules such as aspirin and acetaminophen still show other groups; a wrong tap on them names the group, which previews later chapters.
- The free play in 11.3 also has inhibitor controls; the box says they belong to 11.4.

## To publish (needs your OK)

1. Push the six `book-links` branches to each game's `main` (GitHub Pages), wait for Pages, and check one link live.
2. Publish batch AJ to the seven pages the usual way (dry-run against `tools/batchAJ_sha_2026-11-14.json`, save, read back, sync `pages/live`), then PR and merge.
3. Next PDF: the boxes print their intro and the "This lab runs online" line, with no frame.
