# CHEM 3B homework in LibreTexts ADAPT

## What is already set up (Nov 4, 2026)

- **Course:** "CHEM 3B: Introductory Organic and Biochemistry" in ADAPT (course 4605).
- **15 chapter assignments,** named "CHEM 3B Chapter N: …", with 449 multiple-choice questions in total:
  - Chapter 1: 19
  - Chapter 2: 31
  - Chapter 3: 36
  - Chapter 4: 25
  - Chapter 5: 42
  - Chapter 6: 20
  - Chapter 7: 22
  - Chapter 8: 40
  - Chapter 9: 41
  - Chapter 10: 36
  - Chapter 11: 35
  - Chapter 12: 31
  - Chapter 13: 31
  - Chapter 14: 20
  - Chapter 15: 20
- **Assignment template:** "CHEM 3B Chapter Homework". All 15 assignments use it:
  - real-time grading
  - 3 attempts per question, with no attempt penalty
  - hints on, with no hint penalty
  - late work accepted but marked late
  - assignment group: Homework
- **Feedback:** a wrong answer shows a hint. A right answer shows the full explanation.
- **Question bank:** the questions are also in My Questions, in one folder per chapter ("CHEM 3B Ch 01 …"). They are public under CC BY-NC-SA 4.0, with Daniel Kwasniewski as author.
- **Already in the course:** the two older "… Import" assignments were there before this setup and were left alone.

## What you still need to do in ADAPT

1. Set **available on / due dates** for each assignment, either in the assignment's properties or by bulk editing on the course's assignment list.
2. Check **points per question**. The default is 10; change it if you want 1 point each.
3. Link the course to Canvas: **Course Properties → LMS**. The FCC Canvas admin may need to turn on the ADAPT LTI tool once. After that, scores flow into the Canvas gradebook.
4. Make the course **shown** to students when you are ready.

## Files here

- **`CHEM3B_ChNN_…_QTI.zip`:** the same question sets in Canvas QTI format. Use them to re-import into ADAPT (**My Questions → Bulk Import → Canvas QTI**), or into Canvas (**Settings → Import Course Content → QTI .zip file**).
- **`CHEM3B_ADAPT_question_list.csv`:** every question with its correct answer, for review.
- **To rebuild after editing the Try It bank:** run `python3 tools/adapt_export.py`.

## Extra questions (added Nov 4)

- `CHEM3B_Ch03_extra_QTI.zip`, `CHEM3B_Ch13_extra_QTI.zip` and `CHEM3B_Ch15_extra_QTI.zip` hold 44 more questions:
  - questions that use drawn structures and figures, as images with written descriptions (alt text);
  - 12 new Chapter 13 questions, which are also in the Try It bank (`fb-3B-1001` to `fb-3B-1012`).
- They are built by `tools/render_thin.js` and `tools/adapt_thin.py`.
- They were added to the Chapter 3, 13 and 15 assignments.

## Questions that were left out

These questions are still in the Try It widgets and the Final Boss game:

- Questions that need a drawn structure or figure, or have structures as answer choices.
- Questions taken from your Canvas quizzes.

Other chapters still have structure-based questions that are not in ADAPT yet. The same image method can add them.
