# Final release checklist (2026-11-14)

## A. Lecture textbook readiness

| Gate | State | Evidence / what is left |
|---|---|---|
| Scientific correctness | ✅ | No false statement that changes an answer. Citrate synthase switched to transferase (batch AH Part C, bank fb-3B-2030). |
| Answer keys | ✅ | ~2,000 items re-solved, 0 wrong keys; every printed problem has one answer. |
| Student usability | ✅ (simulated only) | Study path intact in all 15 chapters; no real-student testing done. |
| Web functionality | ✅ with one platform item | All 36 game/widget endpoints and 75 videos load; 0 broken internal links; one Try It played by hand. Phone (iPhone 17 simulator, signed out): pages, side-scroll figures, Answer toggles, embedded game and Glossary work; **Previous/Next arrows point to another Workbench book** (N1), recheck after Bookshelf publication. |
| PDF print | ✅ with two platform items | Recompile, then check: p. 1 cover author (LibreTexts registry) and the 13.5 footer. |
| Accessibility | ✅ with limits | Alt text fix B1 drafted. Screen-reader and keyboard sessions never run; the accessibility statement claims automated checks only, which is accurate. |
| Licensing | ✅ | Mixed licenses kept: CC BY own pages, CC BY-NC-SA adapted pages (Detailed Licensing, PDF pp. 1346–1348), games stated as all rights reserved, Source Attributions table. Nothing changed. |
| Instructor-facing claims | ✅ after batch AH | Lab manual wording and problem counts (F2–F4). About page says no independent peer review yet; keep it that way. |

### Steps to release

1. Read `audit/BATCH_AH_REVIEW.md`; approve, drop or reword rows.
1a. Update the Chapter 14 lecture slides ("Citrate synthase is a Ligase") and any exam key to transferase.
2. Push `bank/metabolism.json` (fb-3B-2030) to GitHub Pages and update the live ADAPT question fb-3B-2030 (POST/PATCH recipe in `adapt/README.md`), then publish batch AH the usual way (dry-run against the `before` hashes, save, read back, sync `pages/live`); in the same step change "last updated" on About This Book and add a version-history line.
3. Compile the full PDF; check p. 1 author, the 13.5 footer, "Swipe sideways" = 0, no label under 6 pt (`tools/check_figure_labels.py` floors).
4. After Bookshelf publication, open any page signed out and check the Previous/Next arrows (N1); report to LibreTexts if still wrong.
4a. Ask LibreTexts to create the author record for `dkwasniewski` (cover "Unknown").
5. Merge `audit/2026-11-final-gate` (reports + batch AH tooling) when ready.

### Known limitations (publish with these stated or accepted)

- LibreTexts glossary pop-ups have an ARIA problem; the Glossary page is the accessible fallback (documented).
- The printed Glossary omits its intro paragraph (LibreTexts template).
- 29 external source links refuse automated checks (403); they load in a browser.
- Games are free but not openly licensed (stated in For Instructors).

## B. Companion lab manual integration readiness

Not a release gate for the textbook.

| Gate | State |
|---|---|
| Manual published | ⏳ in preparation |
| Experiment numbering crosswalk | ⏳ 26 rows in `LAB_MANUAL_INTEGRATION_BACKLOG.md` |
| In the Lab science and safety | ✅ checked 2026-11-14 |
| Student-facing promises | ✅ after batch AH (F1, F3) |
| Links from boxes to the manual | ⏳ after publication |
