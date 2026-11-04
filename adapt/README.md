# CHEM 3B homework sets for LibreTexts ADAPT

The 15 zip files here are homework question banks, one per chapter of *Introductory Organic and Biological Chemistry for FCC*. Each zip is a QTI 1.2 package, the same format Canvas exports. ADAPT stores these as "Native" questions.

| Chapter | Questions | Chapter | Questions |
|---|---|---|---|
| 1 Bonding Review | 19 | 9 Lipids | 41 |
| 2 Alkanes and Cycloalkanes | 31 | 10 Amino Acids and Proteins | 36 |
| 3 Alkenes, Alkynes and Aromatics | 13 | 11 Enzymes and Vitamins | 35 |
| 4 Alcohols, Phenols, Ethers and Thiols | 25 | 12 Nucleic Acids and Protein Synthesis | 31 |
| 5 Aldehydes, Ketones and Chirality | 42 | 13 Carbohydrate Metabolism | 11 |
| 6 Carboxylic Acids and Esters | 20 | 14 Metabolism and Energy Production | 20 |
| 7 Amines and Amides | 22 | 15 Metabolism of Lipids and Proteins | 19 |
| 8 Carbohydrates | 40 | **Total** | **405** |

## What is in each question

- Every question is multiple choice, worth 1 point.
- The answer order is shuffled, so the correct answer is not always A.
- Each question has the explanation from the book's Try It practice as feedback.

## Where the questions came from

- The questions come from the book's Try It bank (`bank/*.json`), which you wrote.
- They are sorted into chapters by the same topics the Chapter Guides use.
- Two kinds of questions were left out:
  - Questions that need a drawn structure, a figure or structure answer choices, because they don't survive a text-only export. They are still in the Try It widgets and the Final Boss game.
  - Questions taken from your Canvas quizzes.

`CHEM3B_ADAPT_question_list.csv` lists every question with its correct answer, so you can check a chapter before you assign it.

## Importing into ADAPT (one-time setup)

1. Sign in at adapt.libretexts.org with your LibreOne instructor account.
2. Create a course: **My Courses → New Course**. Use something like "CHEM 3B – Introductory Organic and Biological Chemistry (FCC)".
3. Open **My Questions** (the Question Bank). Choose **Bulk Import** (some versions say "Import Questions" or "QTI Import"), then upload one chapter's zip. Put each chapter in its own folder, such as "Ch 01 Bonding Review".
4. In the course, create one assignment per chapter. Use **Add Questions → My Questions**, pick that chapter's folder, and select the questions you want (or all of them).
5. Set the assignment options. Suggested settings: real-time feedback, 2–3 attempts per question, and late penalty per your syllabus.
6. Link the course to Canvas with **Course Properties → LMS**. The FCC Canvas admin may need to turn on the ADAPT LTI tool once. After that, ADAPT scores flow into the Canvas gradebook.

**Note:** ADAPT's menu names change from time to time. If you can't find the QTI import, LibreTexts support can import the zips for you. Email them the files and say they are QTI 1.2 Canvas-format question banks.

## Using them in Canvas instead

The same zips import directly into Canvas:

1. Go to **Settings → Import Course Content → QTI .zip file**.
2. Each chapter becomes a question bank you can draw quizzes from.

## Rebuilding

After you edit the Try It bank, run:

```
python3 tools/adapt_export.py
```

This regenerates every zip and the question list.
