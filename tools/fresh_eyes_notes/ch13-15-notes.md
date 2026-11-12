# ch13-15 draft edits — notes

Edit list: ch13-15.json (30 edits, 16 pages). Validated: every `old` count matches at application time (sequential), p/td/li/div counts unchanged, inline tags balanced.

## Edits
- 597192 13.4 — "58% … not conserved" → "other 65%" (matches the page's 35%).
- 597192 13.4 Diabetes box, type 1 paragraph — autoimmune, little or no insulin, can start at any age, lifelong insulin by injection or pump. Removed "juvenile-onset", "develops early in life" and "diabetics".
- 597192 13.4 Diabetes box, antibody paragraph — shortened to one sentence on autoantibody screening.
- 597192 13.4 Diabetes box, type 2 paragraph — explains insulin resistance; "about 90–95%". The 38 million figure was already on the page; no new statistics. Pointer "see Section 13.8" changed to Section 13.7, which has the county figures. Removed "adult-onset" and "noninsulin-dependent".
- 597192 13.4 Diabetes box, drug paragraph — rewritten:
  - metformin lowers liver glucose output and improves insulin sensitivity (points to 13.9);
  - sulfonylureas such as glyburide stimulate insulin release, with a hypoglycemia caution;
  - GLP-1 receptor agonists and SGLT2 inhibitors added;
  - insulin may later be needed;
  - normal fasting glucose 70–99 mg/dL (replaces 70–120, matches 13.7);
  - removed the false claim that glyburide "increases sensitivity of cell receptors".
- 597193 13.5 — Replaced "lactate makes muscles tire and sore": H+ contributes to the burn, lactate is a fuel (13.4), and delayed soreness is muscle micro-injury.
- 597203 14.4 — Both reduction-potential sentences reversed to the correct direction: electrons pass to a carrier that holds them more tightly (higher, more positive reduction potential), and O2 is last.
- 597203 14.4 — Brown fat: adults keep small deposits around the neck and shoulders (points to 15.6), replacing "Adults usually do not have brown fat…".
- 597202 14.3 — Deleted the C=O vs C=C bond-energy pseudo-explanation. The empirical NAD+/FAD rule stays, with the 2.5 vs 1.5 ATP values.
- 597204 14.5 efficiency — Glucose energy changed from 686 to 670 kcal (= 2,808 kJ, the value already used in 13.1 and 13.4), so 234/670 ≈ 35% honestly.
  - The efficiency paragraph now says 35%, and "remaining 65% (about two-thirds)".
  - The closing parenthetical now reads "about 35% is the figure this book uses".
  - The summary bullet is updated to match.
  - Exercise 6 stem and answer updated (count 2, inline and answer key): 670 − 234 = 436 kcal; 436/670 = 65%.
- 597205 14.6 Key Idea 3 — 34% → 35% efficient.
- 597206 14.7 Problem 14.64(d) — 34% → 35%.
- 597195 13.7 — Liver glycogen "enough for 12–24 hours" → "largely used up within about 12 to 24 hours".
- 597197 13.9 — Intro "runs out after roughly 24 hours" and summary "(about 24 h)" → "within about 12 to 24 hours".
- 597219 15.13 Cumulative 15.6 — "(about 12–18 hours)" → "(within about 12 to 24 hours)" (count 2).
- 597209 15.3 — Alt text of the ATP + carboxylate image no longer describes an "attack" or "red arrow"; it now lists reactants and products only. Added the overall equation to the text: fatty acid + ATP + CoA → fatty acyl CoA + AMP + PPi.
- 597218 15.12 Exercise 9(c) — Urea cycle location now matches 15.10: entry step and step 1 in the matrix, steps 2–4 in the cytosol (count 2).
- Answer-key headings — Each now quotes the Practice item it answers, using the house style (“Practice: …&hellip;”):
  - 597191: "Clinical Connection: Nursing (a)" and "(b)";
  - 597200: "Example 1: Carbon balance…";
  - 597208: "Example 1: Transamination";
  - 597210: "Professor Tip".

  Note: the inline answer `<details>` on these pages may also be wired to these labels by the page template. Only the answer-key text was changed.

## Not done / needs follow-up
- 597209 15.3 image fileid 446289 (clipboard_e30d89372ef33842c41d51ab6540b7b45.png) needs a redraw. I viewed it and it has two red curved mechanism arrows: acylate → Pα and P–O bond → O. That breaks CONVENTIONS (no curved-arrow mechanisms). Redraw it as a plain reaction: fatty acid carboxylate + ATP → acyl adenylate + PPi, with no curved arrows. Better still, use a single overall image: fatty acid + ATP + CoA → acyl CoA + AMP + PPi.
- 597192 13.4 image fileid 128222 shows only older sulfonylureas: tolbutamide, chlorpropamide and glyburide. I kept it, since the new text says "glyburide (shown above)", and its alt text is accurate. Optional: replace it with a metformin structure, or cut it to glyburide only.
- 597192 13.4: the complication bullets in the same box are unchanged. One reads "leading cause of blindness in adults over age 20"; CDC wording is "working-age adults". It wasn't in the assignment; flag it for a later pass.
- 597203 14.4, same paragraph: "Newborn babies have brown fat deposits on arteries…" was left as is, to keep the edit surgical.
