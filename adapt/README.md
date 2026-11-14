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
- **Question bank:** the questions are also in My Questions, in one folder per chapter ("CHEM 3B Ch 01 …"). They are public under CC BY 4.0, with Daniel Kwasniewski as author (instructor decision 2026-11-11: the question bank is CC BY 4.0).
- **Already in the course:** the two older "… Import" assignments were there before this setup and were left alone.

- **Now in the course (Nov 4, after the structure questions):** 914 questions across the 15 assignments: Ch1 101, Ch2 52, Ch3 60, Ch4 51, Ch5 121, Ch6 46, Ch7 52, Ch8 69, Ch9 66, Ch10 66, Ch11 76, Ch12 51, Ch13 31, Ch14 38, Ch15 34. Each student gets a random 50 (Ch 1, 3, 5, 8–11), 40 (Ch 2, 4, 6, 7, 12) or 25 (Ch 13–15) of them, worth 100 points per chapter. 515 questions have one of Dr. Dan's videos in the Hint button.

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

## Structure and figure questions for every chapter (added Nov 4)

- `CHEM3B_ChNN_more_QTI.zip` (Chapters 1–12, 14 and 15) hold 479 more questions that use drawn structures, graphs, pathways, Fischer and Haworth projections:
  - Chapter 1: 82, Chapter 2: 21, Chapter 3: 38 (including 14 re-imported, see below), Chapter 4: 26, Chapter 5: 79, Chapter 6: 26, Chapter 7: 30, Chapter 8: 29, Chapter 9: 25, Chapter 10: 30, Chapter 11: 41, Chapter 12: 20, Chapter 14: 18, Chapter 15: 14.
  - Every drawing is an image with a written description (alt text) for screen readers. The descriptions are written from the drawing data by `tools/struct_alt.py`: atoms, rings, positions, wedges, cis/trans layout, condensed formulas, and graph shapes. They describe the drawing without naming the answer.
  - Tables and equations that stand alone are real text, not images.
- `more_by_chapter.json` lists which questions go in which chapter.
- To rebuild: `python3 tools/adapt_more.py ids <imgdir>`, then `node tools/render_thin.js <imgdir>/ids.json <imgdir>`, then `python3 tools/adapt_more.py build <imgdir>`.

## Questions that were left out

These questions are still in the Try It widgets and the Final Boss game:

- Questions taken from your Canvas quizzes (40 items tagged `src: "canvas-quiz"` in bank/*.json; written by the instructor, confirmed 2026-11-12).

## Shuffled structure choices

When the answer choices are drawn structures, the A–D grid is shuffled for each question, so the right answer is not always "Structure A". Fourteen Chapter 3 questions from the first extra set had the right answer always in position A; they are re-imported in `CHEM3B_Ch03_more_QTI.zip` with a shuffled grid, and the old copies were taken out of the Chapter 3 assignment.

## Update of 2026-11-12 (fresh-eyes review, Tier 6)

- **Live course now holds 1,031 questions:** Ch1 106, Ch2 65, Ch3 79, Ch4 54, Ch5 93, Ch6 59, Ch7 57, Ch8 76, Ch9 75, Ch10 75, Ch11 82, Ch12 58, Ch13 53, Ch14 51, Ch15 48. Random-draw sizes per student are unchanged.
- **Added (100 new ADAPT questions, created through the ADAPT API and placed in the chapter folders, CC BY 4.0):**
  - 65 new bank items, fb-3B-2061 to 2125: course-outline gaps and Central Valley / current-clinical contexts.
  - 35 older text items that the exporter never picked up.
- **Updated in place (13, "automatically update" for own assignments, reason recorded):** fb-3B-0161, 0199, 0237, 0238, 0239, 0246, 0445, 0641, 0914, 0915, 0916, 0917, 0926. 0914–0916 are now text-only.
- **Moved:** fb-3B-0237 and 0238 (now alkene/alcohol items) from Chapter 2 to Chapter 3.
- **Removed from assignments (32; still in the bank and in My Questions):** 18 chirality wedge/dash near-duplicates (Ch 5), 9 fatty-acid ATP variants (Ch 15), 5 molar-mass drill items (Ch 1). The list is in `adapt_target_2026-11-12.json` ("retire").
- **Exporter:** `tools/adapt_export.py` now reads only `PLAN` from `build_pages.py`; it no longer runs the page build. An explicit `{id: chapter}` map places items that no widget regex catches. The run prints a warning if any usable item is left in no chapter. `adapt_target_2026-11-12.json` is the per-chapter target, and the live course matches it. The one exception: fb-3B-1011 and 1012 stay in Chapter 13, where they were already live, although the exporter files them under Ch 14 and Ch 15.
- The new questions have no video hint yet. The "Watch Dr. Dan's lesson" hints on older questions are unchanged.

## Update of 2026-11-12 (night): live check after the review
- **Licence fields:** checked all 1,031 live questions. Each is CC BY 4.0, author Daniel Kwasniewski, with no attribution needed.
- **pKa removed live:** five questions still had the pre-11-11 pKa wording in ADAPT, although the bank had been rewritten. They were updated in place to the bank version (reason recorded, "automatically update", hints unchanged):
  - fb-3B-0078 (ADAPT 354359)
  - fb-3B-0864 (355041)
  - fb-3B-0865 (355042)
  - fb-3B-0870 (355047)
  - fb-3B-0871 (355048)
- **Re-scan:** no question text, hint or solution in the course mentions pKa, and every assignment uses the latest revision of each question.
- **Video hints:** the 537 "Watch Dr. Dan's lesson" hints are left as they are (instructor decision). The QTI LICENSE.txt notes that linked videos are not covered by CC BY.
- **Editing note:** PATCH /api/questions/{id} only saves when the body is built from the open editor form (CreateQuestion questionForm, server fields removed) with qti_prompt, qti_randomize_order, qti_simple_choice_N, qti_json_type, folder_id, tags: [] and the unwrapped hint. A body built from the API view returns "We were not able to save this question."

## Update of 2026-11-13: live course brought in line with the bank
- **22 questions updated in place** in course 4605 ("automatically update" for own assignments, reason recorded: "Wording aligned with the textbook conventions and question bank (2026-11-13)."). Each was read back after saving and matches the bank on stem, choices, key, feedback and hint. Video hints were not touched.
  - Wording fixes made in the bank on 2026-11-13: fb-3B-0147 (ADAPT 354550), 0151 (354585), 0227 (354232), 0228 (355789), 0456 (354537), 0599 (354730), 0629 (354921), 0974 (354604), 0983 (354542).
  - Live copies that were older than the bank: fb-3B-0195 (355024), 0301 (355118), 0725 (354976), 0727 (354978), 0754 (355035), 0755 (355036), 0756 (355037), 0872 (355049), 0887 (355082), 0889 (355084), 0934 (354969), 0952 (355052), 2013 (355208).
  - fb-3B-0872 and 0887 got new answer choices as well as a new stem (0887 no longer asks for Km). The others changed only in stem or feedback wording; no key changed.
- **Not updated:** fb-3B-0979, which is retired from the assignments (it is still in My Questions with its old feedback).
- **Re-scan of all 1,031 live questions:** no pKa, Km, "hydride", meso, sp3 or "ion–dipole" wording, and no assignment is waiting on a question revision.
- **Export files:** all 36 QTI zips, the payloads and the CSV were rebuilt from the bank the same day (see tools/BANK_FIX_2026-11-13.md), so they now match the live course for every id.
- **How the save works (for next time):** open the question in an assignment's question view, click the pencil, and the request the editor sends is PATCH /api/questions/{id} with the get-question-to-edit object, where attachments, learning_outcomes, media_uploads, tags and clone_history are arrays (not JSON strings), qti_answer_json is left out, and these are added: qti_prompt, qti_randomize_order, qti_simple_choice_0..3, qti_json, reason_for_edit, changes_are_topical "", session_identifier (a UUID), source_url_required true, framework_item_sync_question {descriptors: [], levels: []}, webwork_attachments [], automatically_update_revision "1", assignment_id 0, revision_action "notify". A body in that shape saves from a plain fetch; "propagate" is refused when the question text changes.


## Update of 2026-11-13 (evening): 78 new questions created live

- **Live course now holds 1,109 questions:** Ch1 114, Ch2 75, Ch3 85, Ch4 64, Ch5 93, Ch6 69, Ch7 57, Ch8 86, Ch9 75, Ch10 80, Ch11 82, Ch12 58, Ch13 58, Ch14 51, Ch15 62. Random-draw sizes per student are unchanged.
- **Added:** fb-3B-2238 to 2315 (78 bank items: Lewis structures, alkene and alkyne naming, ketone bodies, and the thin-topic set). Chapter comes from each item's `sec` tag: Ch1 8, Ch2 10, Ch3 6, Ch4 10, Ch6 10, Ch8 10, Ch10 5, Ch13 5, Ch15 14.
- Each was created through the ADAPT API straight into its chapter assignment and chapter folder, public, CC BY 4.0, author Daniel Kwasniewski, no video hint. Points follow each assignment's default.
- **Read back:** every one of the 78 is in its assignment, with stem, choices, key and feedback identical to the bank. None of the titles existed before, and no assignment has a duplicate title.
- **How creation works (for next time):** POST /api/questions with the same editor-shaped body as the PATCH above, minus the server fields (id, page_id, iframe_id, dates, revision fields, qti_answer_json), with `assignment_id` set to the chapter assignment and `folder_id` to the chapter folder (14979 + chapter). The reply names the assignment the question was added to.
