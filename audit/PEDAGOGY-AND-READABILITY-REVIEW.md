# Pedagogy and readability review (master refinement pass, 2026-11-13)

Full reports, with a score row for every page and the reasoning for each edit: `audit/reviews/pedagogy_ch01-05.md`, `pedagogy_ch06-10.md`, `pedagogy_ch11-15.md`. The scores are also in `TEXTBOOK-COVERAGE-LEDGER.md`. Edits: `audit/edits/pedagogy_*.json` (67), all in the batch Q draft.

**How it was done.** Every landing page, section and Chapter Guide of Chapters 1–15 was read and scored 0–4 on accuracy, clarity, prerequisites, visuals, reasoning, practice and transfer. Three lead reviewers split the chapters; ten of the fifteen chapters were read by a second-level reviewer working to the same brief, so calibration between chapters can differ by about half a point. Visual scores come from alt text and captions; no image was viewed. Practice Problems and Practice Games pages were read for sequencing only.

## What the book does well (keep)

- The author's own Problem → Solution → Check examples are consistently good: they give the reason and a check a student can repeat.
- Lecture Connections state the exam-level version of each idea plainly.
- Strongest pages by score: 11.7, 12.5, 13.7, 14.5; the Chapter Guides generally.
- Rosa's case questions mostly need the chemistry (39 of 45).

## Patterns that cost students the most

| # | Pattern | Where (examples) | What was done |
|---|---|---|---|
| 1 | **Told twice, and the two tellings disagree.** The inherited source text and the Lecture Connection teach the same content in different words, sometimes with different outlines. | 4.5 (two "three reactions" lists), 5.4, 6.8, 7.6, 9.5, 10.2, 14.2, 14.4 (the chain three times, cyanide four), 15.4, 15.5, 15.6 | One-sentence bridges or corrections where they contradict (drafted). Cutting the duplicated source prose is a larger editorial decision: not drafted. |
| 2 | **Inherited worked examples state the answer.** No reason, no check. | 1.2, 1.3, 1.5, 2.5, 2.8, 3.4, 6.1, 6.4, 6.8, 7.1, 7.7, 8.4 Ex 1, 10.5 Ex 1, 11.2 Ex 1, 12.3 Ex 2, 12.6 Ex 1 | The weakest ones rewritten in place at the same length (drafted). |
| 3 | **Exercises with no answer.** | 24 exercises on 12 pages | Answers written (see errata E1). |
| 4 | **Terms used before or without definition.** | locant (2.3), resonance (3.7), triacylglycerol (3.2), "-dial" (5.2), ester/amide (5.3), mineral acid (6.7), nucleophilic acyl substitution (7.6), isotonic (8.3), α1–β2 (8.5), lipid (9.1), pI (10.1), σ-bonds (10.6), ΔG (13.2) | Defined in passing or replaced with plain wording (drafted). Left: formal charge (1.10 only), aliphatic (4.2), Le Chatelier (4.4), steric strain (10.7). |
| 5 | **Content ahead of its section.** | genetic code in 12.4 before 12.6; ATP bookkeeping by step number in 13.4 before 13.5; Try It boxes (see games file, G1) | Try It selections fixed. The text order is a restructuring question: not drafted. |
| 6 | **Promises the page does not keep.** | Route pages for Chapters 11–15 say "answer the Try It questions in each section"; about half the sections have none. 14.4's first objective names flavin mononucleotide, never taught. 15.4's objective says "understand obesity". | Reworded (drafted). |
| 7 | **Pages with no practice at all.** | 6.6, 9.4, 10.7, 10.9, 11.1, 11.3, 11.5, 11.6, 12.1, 12.4, 12.7, 13.2, 15.6, 15.11; 8.3 holds the mg/dL ↔ mmol/L calculation with no worked example | Not drafted: each needs one exercise written, which is new content. Listed in the checkpoint. |
| 8 | **Chapter Guide examples missing the Check step.** | 1.9 (Ex 2–4), 2.10 (Ex 1–4), 3.9 (Ex 1–5) | One added (3.9 Ex 2) as the pattern; the other eleven are on the checkpoint list. |
| 9 | **Applied boxes that do not need the chemistry.** | Valley 2.6, 3.5, 4.9, 10.3, 11.5 (both), 12.7, 15.7; about ten clinical boxes | 4.9 rewritten; question stems suggested for the rest (not drafted). |

## Exemplar: Section 4.5, Reactions of Alcohols (page 597094; PDF pp. 320–329)

Chosen because it has every part the brief asks for (reasoning, figures, worked examples, an exercise, a Valley Connection, a reaction-lab Try It) and a real weakness. Runners-up from the other reviewers: 7.7 (inherited example with no conditions) and 15.5 (its only worked example is the anion gap, which the section never teaches).

| Step | Detail |
|---|---|
| Original problem | (1) The source text says the three alcohol reactions are oxidation, dehydration and esterification; the Lecture Connection below says combustion, dehydration and oxidation. (2) "Oxidation" is used for a full section before it is defined; the definition sits only in the Lecture Connection. (3) The Summary says primary alcohols give aldehydes and stops, while the text, Example 1 and the Valley box all carry on to the carboxylic acid. (4) Exercise 1 (three alcohols to oxidize) has no answer on screen or in print. |
| Diagnosis | A student who reads top to bottom meets an undefined key word, then two outlines that disagree, then practises and cannot check the work, then revises from a Summary that omits the step the Valley box is built on. None of this is a chemistry error; all of it is friction at the point where the chapter's main reaction is learned. |
| Revision (4 edits, about 70 words added) | **Before:** "Primary and secondary alcohols are readily oxidized. We saw earlier…" **After:** "Primary and secondary alcohols are readily oxidized. For an organic molecule, oxidation means gaining bonds to oxygen or losing bonds to hydrogen; here the alcohol loses two H atoms and its C–O single bond becomes a C=O double bond. We saw earlier…" · **Before:** "Alcohols do three things in this course: they burn (combustion), they lose water (dehydration) and they lose hydrogen (oxidation)." **After:** "…in this chapter: … The esterification branch of Figure 4.5.1 waits until Chapter 6." · **Summary:** "Primary alcohols are oxidized to form aldehydes, which are oxidized further to carboxylic acids." · **Exercise 4.5.1 answer** added inline and in the print key: (a) 3°, no reaction; (b) 2-methyl-1-propanol → 2-methylpropanal → 2-methylpropanoic acid; (c) 3-methyl-2-hexanol → 3-methyl-2-hexanone. |
| Test evidence | Each `old` string occurs exactly once in the live page; the edited page keeps the same tag balance (`audit/preview/597094.html`); the answers were worked from the figure descriptions; the live page passes axe on its own content; the Try It on this page (reaction lab: dehydration and the three oxidations) loads and matches the section. |
| Web / PDF comparison | **Before:** live page and PDF p. 329 viewed (Try It box, Lecture Connection credit, print key with one entry). **After:** not available until the page is published and one page is compiled; this is the first check to run after the publish OK (compile page 597094 alone, confirm the key now has two entries and no new page break). |

## Rubric averages (0–4), computed from the ledger

| Chapter | Accuracy | Clarity | Prerequisites | Visuals | Reasoning | Practice | Transfer |
|---|---|---|---|---|---|---|---|
| 1 | 4.0 | 3.2 | 3.1 | 3.0 | 2.7 | 2.7 | 2.4 |
| 2 | 4.0 | 3.2 | 3.4 | 3.0 | 3.0 | 2.8 | 2.3 |
| 3 | 4.0 | 3.4 | 3.2 | 3.2 | 3.0 | 2.7 | 2.4 |
| 4 | 3.9 | 3.6 | 3.4 | 3.3 | 3.3 | 3.1 | 2.4 |
| 5 | 4.0 | 3.4 | 3.4 | 3.3 | 3.1 | 3.6 | 2.7 |
| 6 | 4.0 | 3.3 | 3.2 | 3.2 | 2.5 | 2.4 | 2.9 |
| 7 | 3.9 | 2.9 | 2.9 | 3.1 | 2.8 | 2.5 | 2.7 |
| 8 | 4.0 | 3.4 | 3.3 | 3.4 | 2.9 | 3.1 | 2.9 |
| 9 | 3.4 | 3.0 | 2.7 | 2.7 | 2.7 | 2.9 | 3.1 |
| 10 | 3.7 | 3.2 | 3.3 | 2.8 | 2.7 | 2.2 | 2.8 |
| 11 | 4.0 | 3.5 | 3.5 | 2.9 | 2.7 | 2.5 | 3.0 |
| 12 | 4.0 | 3.5 | 3.3 | 3.1 | 2.7 | 2.6 | 2.7 |
| 13 | 3.8 | 3.3 | 3.0 | 3.2 | 3.2 | 3.2 | 3.5 |
| 14 | 3.9 | 3.2 | 3.2 | 3.0 | 2.9 | 3.1 | 2.7 |
| 15 | 3.7 | 2.9 | 3.1 | 2.9 | 2.5 | 2.6 | 3.1 |
| **All** | **3.9** | **3.3** | **3.2** | **3.1** | **2.9** | **2.8** | **2.8** |

Accuracy is the highest dimension in every chapter, which matches the correctness checks of 11-11 and 11-13. The weak dimensions are transfer (Chapters 1–5: applied boxes that do not need the chemistry), practice (sections with no exercise or Try It) and reasoning (inherited examples). Lowest chapter overall: 9, then 7, 10 and 15. Scores for different chapters came from different readers; compare within a chapter more than between chapters.
