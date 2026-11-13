# Batch E: licensing and attribution (review 2026-11-12)

Every finding was re-checked against the live page and its source before any change was written.

## E1: book pages (18 edits on 13 pages; tools/batchE1_fixes_2026-11-12.json, not yet published)

- **Bare "(Public domain)" credits (8 captions, 1.7 ×3, 5.5, 10.8, 13.1 ×3, 15.4):** Malik's own pages give these only as "(Copyright; Public domain)" with no creator, so each now reads "(Figure from *Introduction to Organic and Biochemistry* (Malik), public domain.)", keeping the existing correction notes.
- **Commons photos, matched visually to their Commons files** (author and licence from the Commons API):
  - 3.3 tomatoes: Softeis, CC BY-SA 3.0 (it had no credit).
  - 4.7 Fig 1: model by Benjah-bmm27 (public domain), crystals by W. Oelen (CC BY-SA 3.0); it said only "from Wikipedia".
  - 15.8 ergospirometry photo: Cosmed, CC BY-SA 3.0. It said "from Wikipedia" and also credited Ball.
- **1.8 Figs 10 and 11:** both are OpenStax *Chemistry 2e* §10.1 figures (Fig 11 was credited to Ball). Credit: *Chemistry 2e* (Flowers et al., OpenStax), CC BY-NC-SA 4.0, with the existing correction note.
- **15.1 lipoprotein diagram:** authors and chapter named (Jairam, Uchida and Narayanaswami, IntechOpen 2012, CC BY 3.0), plus a grammar fix ("is based").
- **10.7 Fig 1:** the caption notes that each panel's creator and licence are printed on the panel.
- **Source Attributions page:**
  - The videos line now names the third-party channels (Amoeba Sisters, BioMan Biology, NDSU, Biotech Review, NHLBI).
  - The figures line notes that third-party images are credited individually.
- **About:** the Malik count changes from 21 to 20 (84 + 20 + 11 + 10 = 125 section pages).

Checked and left unchanged:
- **11.6 *Biology 2e*:** the credit says CC BY-NC-SA 4.0, and OpenStax's catalogue confirms it, so the review's suggestion was wrong.
- **The 11 *Fundamentals of GOB* rows that name "LibreTexts" as author:** that is how LibreTexts itself attributes the book.

## E2: question bank (done locally; not ADAPT)

- The generators (adapt_export, adapt_nov5, adapt_thin) and cumulative.py now say "Questions by Daniel Kwasniewski, CC BY 4.0".
- All 36 QTI zips were rewritten with that description and a LICENSE.txt (title, author, source, licence, plus a note that linked videos are not covered). Every zip passes an integrity test.

## Decisions for the author

1. **CC BY-SA images still in the book:**
   - The images: 3.3 tomatoes, 4.7 phenol crystals, 15.8 ergospirometry photo, and the collagen panel (Laboratoires Servier) inside 10.7 Fig 1.
   - The conflict: the About page says every ShareAlike source figure was replaced. Also, 10.7 is a Malik page (CC BY 4.0).
   - The choice: replace them, or keep them credited and change the About sentence.
2. **Uncredited photos from Malik** (15.4: polar bears, orca, camel, geese; 9.3: snake venom): Malik gives no source. Replace them with verified public-domain photos, or remove them.
3. **The 40 `canvas-quiz` questions** (bank/*.json; used in the Try It widgets and Final Boss, not in ADAPT): did you write them? The book says the widget question bank was written by you.
4. **Live ADAPT licence, author and attribution fields, and the "Watch Dr. Dan's lesson" hints:** not checked, because the browser is not signed in to adapt.libretexts.org.
