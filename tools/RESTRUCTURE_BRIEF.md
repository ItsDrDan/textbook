# Restructure brief – move the right content into the chapter's section pages

Read `tools/AUTHOR_BRIEF.md` (standards, tools), `tools/COR_outline.md`, and `tools/POLISH_BRIEF.md` (sources) first. Dr. Dan's instruction, verbatim: *"keep things that are related to my slides. … any information that can get sprinkled into the individual sections of the chapters would be amazing. Then anything extra could be an extended notes, but it would be better to add them to the sections where appropriate."*

## The situation
Each chapter has ~8–12 **section pages** (Ball et al. / Malik text, transcluded; their text is in `ball_text/<pageid>.txt`, titles in `tools/REVIEW_BRIEF.md`'s section map) followed by a **Chapter Guide** that has grown to 5,000–8,000 words. Students read the sections first, so the teaching that belongs with a topic should sit *on that topic's section page*, right after the source text, and the Chapter Guide should go back to being a compact study guide.

Mechanism: a section page keeps its transclusion of the source text (do not touch that; `tools/transclusions.json` holds it) and we **append** our own block after it. You write that block as `sections/add_<pageid>.html`. The build concatenates transclusion + block. Only create an `add_` file for a section where you have real content to add; many sections will get one, some will not.

## What goes where
1. **Section pages (`sections/add_<pageid>.html`)** — for each Key Idea, worked example, figure, Professor Tip, clinical box, "In the Lab" note, common mistake and Try It widget currently in the guide: find the section whose source text covers that topic and move it there. Read `ball_text/<pageid>.txt` first so the block *adds* to the source (your language, your rules, the lecture's framing, a worked example in Problem/Solution/Check form, a clinical tie-in, a figure) instead of restating it. Where the source text uses a different convention from the course (older ATP values, "cytoplasm", different cut-offs, different enzyme class), add a short **"In this course"** note that states the convention to use on exams — this reconciliation is required wherever it applies.
   Block structure (exact):
   ```
   <h2>Lecture Connection</h2>
   <p>one or two sentences: what the lecture emphasizes about this section, in Dr. Dan's words</p>
   <h3>…topic…</h3> … (as many h3 blocks as needed: key points, a figure, a worked example box, tips, clinical boxes)
   <div class="box-note" style="border-left:6px solid #86509b;"> … Try It widget … </div>   (only where a widget exists for that skill)
   <p style="font-size:0.9em;color:#555;">Lecture Connection by Dr. Dan (Daniel Kwasniewski), Fresno City College, CC BY-NC-SA 4.0; the section text above keeps its own license and attribution.</p>
   ```
   Keep each block focused (typically 300–900 words plus figures). Figures: reuse the guide's inline SVGs and Slide*.png figures (caption them `Figure N.0:` — the build renumbers per page). Widget markup to copy (change the query, title, blurb, height):
   ```
   <div class="box-note" style="border-left:6px solid #86509b;">
   <p class="boxtitle">Try It: TITLE</p>
   <p>BLURB Your progress is saved in this browser.</p>
   <p><iframe src="https://itsdrdan.github.io/textbook/practice.html?t=TOPIC&amp;n=10&amp;title=TITLE" width="100%" height="620" style="border:0;border-radius:12px;background:#f5f6fb;" title="Try It: TITLE" loading="lazy"></iframe></p>
   <p style="font-size:0.9em;">Not loading? <a href="https://itsdrdan.github.io/textbook/practice.html?t=TOPIC&amp;n=10&amp;title=TITLE" target="_blank" rel="noopener">Open this practice in a new tab</a>.</p>
   </div>
   ```
   (Topics: structure hydrocarbons aromatic alcohols carbonyls chirality acids_esters amines carbs lipids proteins enzymes nucleic metabolism isomers properties; `q=regex` narrows; `rxn=key1,key2&mode=mix|identify|product|reactant|name` runs the reaction lab with keys combustion substitution hydrogenation halogenAdd hydrohalogenation hydration dehydration ox1Ald ox1Acid oxAldAcid ox2 reduction esterification esterHydrolysis saponification amidation amideHydrolysis amideBase hemiacetal acetal neutralAcid neutralAmine.)
2. **Chapter Guide (drafts, edit in place)** — slim it to a study guide of about 1,800–2,800 words: Learning Objectives; Key Ideas as *short* numbered summaries (3–8 lines each, in lecture language, each ending with a pointer like "Details and examples: Section 4.5") — **keep every existing `<h3>` heading text and order** (the build anchors widgets/schemes on them) and keep `<h2>Key Ideas</h2>`, `<h2>Video Lessons</h2>`, `<h2>Worked Examples</h2>`, `<h2>Common Mistakes to Avoid</h2>`, `<h2>Practice</h2>`, the Health Career Connection box and the "Next up"/games box; keep the 4–6 most exam-like worked examples in the guide (others move to sections); keep all Common Mistakes (they are short); keep the guide's Practice exercises. Clinical boxes: keep one short combined box in the guide; the fuller nursing/dental content moves to the sections it belongs to.
3. **Extended Notes (`sections/ext_chNN.html`)** — only for content that is in scope and worth keeping but fits no section (rare). Same page template as a full section page (objectives optional; needs the Attribution box). If you create none, say so.
4. **The ten new full section pages** (4.10, 7.11, 11.7, 12.9, 13.7–13.10, 14.5, 15.6) are already complete; do not duplicate their content into other sections — point to them instead.
5. **Practice Problems pages**: unchanged.

## Rules
- Nothing is lost: every fact, example, figure and box from the current guide ends up in exactly one place (a section block, the slim guide, or extended notes). Keep a ledger as you go.
- Slide-related content always stays (lecture wording, mnemonics, "Practice:" style prompts).
- Do not alter the transcluded source text and do not paraphrase it into your block.
- Accessibility/OER rules from the author brief apply to every block (alt/aria-label, th headers, attribution line).
- Headings inside blocks start at h2 ("Lecture Connection") then h3; never h1.
- Run `python3 tools/check_fragment.py sections/add_<id>.html` (no mode flag) on each block, `--guide` on the guide; preview any block with a figure.

## Report (under 500 words)
Per chapter: list of `add_` files created with one line each on what moved there; guide word count before → after; what stayed in the guide; extended-notes page (if any); any "In this course" reconciliation notes you wrote (and what the source text said).
