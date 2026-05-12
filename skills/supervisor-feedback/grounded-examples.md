# Grounded Calibration Examples for the Supervisor-Feedback Agent

This document contains real supervisor and reviewer quotes from the PhD thesis review process, organised by the four categories under-represented in the current `supervisor-feedback` skill. Each example is labelled with its source and the date of the quote so the agent can be calibrated on authentic voice and typical severity.

**Sources in this document:**

- **ES** = Prof. Chng Eng Siong, primary supervisor. Structural, bullet-driven. Often writes one-line comments.
- **Nancy** = Dr. Nancy F. Chen, co-supervisor. Softer phrasing, focuses on argumentation gaps and framing.
- **Jeremy** = Chapter-level reviewer. Inline PDF annotations. Shorthand style ("proper sentence", "why upper case?", "undefined").

Each example follows the same format used in `SKILL.md`:

```
[Source | Date] ISSUE_TYPE (SEVERITY): "quoted problematic text"
→ Supervisor comment: the actual quote, verbatim where available
→ Interpretation: what the comment means
→ Fix: revised text (if the revision was executed)
```

---

## Category A: Abstract-Level Issues

### Example A1: Abstract written in paper style, not thesis style

```
[ES | 24 Feb 2026] SCOPE (SHOULD-FIX): The Chapter 2 opening paragraph begins
with "This chapter provides the foundational background for the three core
contributions of this thesis..." followed by a section-by-section summary.

→ Supervisor comment (verbatim):
  "The beginning of ch 2, it should looks more like an abstract to a paper,
   its an abstract to the chapter.
   - And why and how does the above support your thesis
   - You have some infor, but its not enough"

→ Interpretation: A chapter opening that only signposts sections is not an
  abstract. It must state the problem, the key findings of the chapter, and
  how the chapter supports the thesis argument.

→ Fix direction: Rewrite the opening as a self-contained abstract that says
  what the chapter contributes to the thesis, not what each section contains.
```

### Example A2: Thesis title too broad for the actual experimental scope

```
[Nancy | 27 Jan 2026] SCOPE (MUST-FIX): Thesis title
  "Efficient Self-Supervised Learning Representations for Audio Applications"

→ Supervisor comment (verbatim):
  "The current thesis title implies there are many audio applications, but
   would it make sense to be more specific on the actual tasks you ran
   experiments on in addition to what audio applications your approaches
   might have an impact on? Showing you have speech experience explicitly
   could help others understand more deeply the implications of the
   techniques you had experience with, where some might overlap with those
   in NLP, but of course this also partially depends on what kinds of
   speech tasks you worked on."

→ Interpretation: "Audio Applications" is too broad when the experiments are
  on speech and music only. The title should name the domains actually
  covered.

→ Fix: Title changed to "Efficient Self-Supervised Learning Representations
  for Speech and Music Applications".
```

### Example A3: Long run-on sentence at the end of the abstract

```
[Jeremy | March 2026] RUN-ON (MUST-FIX):
  "The proposals presented throughout this thesis have been evaluated across
   diverse speech tasks (Automatic Speech Recognition, Intent Classification,
   Keyword Spotting, Emotion Recognition, Speaker Identification) and music
   tasks (Singer Identification, Vocal Technique Detection, Instrument
   Classification, Pitch Classification in Music, Musical Genre
   Classification), and it is demonstrated across this thesis that the
   proposals achieve enhancements in accuracy and noise robustness on these
   tasks."

→ Supervisor comment (verbatim): "proper sentence" (annotated twice on the
  same sentence).

→ Interpretation: One sentence of roughly 70 words that packs the evaluation
  scope and the summary claim together. Must be split.

→ Fix (as applied): "The proposals presented in this thesis have been
  evaluated across five speech tasks (automatic speech recognition, intent
  classification, keyword spotting, emotion recognition, speaker
  identification) and five music tasks (singer identification, vocal
  technique detection, instrument classification, pitch classification,
  genre classification). The results demonstrate improvements in accuracy
  and noise robustness on these tasks."
```

### Example A4: Loaded adjective in contribution header ("Flexible Domain Unification")

```
[Jeremy | March 2026] CAPITALISATION (MINOR): Abstract header reads
  "Flexible Domain Unification"

→ Supervisor comment (verbatim): "why upper case?"

→ Interpretation: Treating a concept phrase as a proper noun with title case
  is unjustified. Use sentence case for the concept.

→ Fix: "Flexible domain unification".
```

### Example A5: Jargon without definition ("learning interference")

```
[Jeremy | March 2026] UNDEFINED (SHOULD-FIX): Abstract uses the phrase
  "avoids learning interference between domains"

→ Supervisor comment (verbatim): "not sure what 'interference' means in
  this context."

→ Interpretation: "Learning interference" is ML jargon that is not universal.
  Replace with a mechanistic description.

→ Fix: "avoids the competing gradient signals that arise when distilling
  both domains simultaneously".
```

### Example A6: Prescriptive word choice ("enhancements" vs. "improvements")

```
[Jeremy | March 2026] OVERCLAIM (MINOR): Abstract concluding sentence uses
  "achieve enhancements in accuracy and noise robustness"

→ Supervisor comment (verbatim): "improvements"

→ Interpretation: "Enhancements" sounds promotional. "Improvements" is the
  neutral technical term.

→ Fix: "achieve improvements in accuracy and noise robustness".
```

### Example A7: Unexplained assumption in contribution claim

```
[Jeremy | March 2026] SCOPE (SHOULD-FIX): The Chapter 5 description ends with
  "without requiring shared initialization or retraining."

→ Supervisor comment (verbatim): "Explain that this gives the advantage of
  the flexibility to use a wider variety of models that are to be combined."

→ Interpretation: The absence of a constraint is stated without saying why
  the absence matters. Add one sentence explaining the practical gain.

→ Fix: After "...and without retraining." add: "This removes a key constraint
  of the task arithmetic approach and allows a wider variety of independently
  trained models to be combined."
```

### Example A8: Abstract names domains in aggregate; no individual tasks; no numbers

```
[ES | April 2026] MISSING-NUMBERS (MUST-FIX): The abstract read:
  "The proposals presented throughout this thesis have been evaluated across
   five speech tasks from the SUPERB benchmark, five music tasks from the
   MARBLE benchmark, and the ESC-50 environmental sound classification task.
   The correlation-based distillation framework improves speech task
   performance under both clean and noisy conditions. The task arithmetic
   approach achieves competitive performance with ensemble distillation
   while providing post-hoc control over domain emphasis. The
   correlation-permutation framework improves over naive model merging as
   well as task-arithmetic without requiring retraining or shared
   initialisation."

→ Supervisor comment (verbatim):
  "Name the speech and music tasks. Add some numbers of performance, to
   improve by how much, is it sota? etc."

→ Interpretation: ES expects an abstract to name the specific tasks (not
  "five speech tasks" but "ASR, KS, IC, ER, SID") and to attach quantitative
  outcomes to every improvement claim. A purely qualitative abstract does
  not satisfy his bar even when the prose is otherwise tight. This is the
  reverse of the more common style guide that tells students to keep
  numbers out of the abstract; ES specifically asks for them.

→ Fix (as applied by the author):
  "Evaluation spans five SUPERB speech tasks (ASR, KS, IC, ER, SID), five
   MARBLE music tasks (SingerID, VocID, InstCls, GenreID, PitchID), and
   ESC-50 environmental sound classification. ... The correlation-based
   distillation framework improves over the standard distillation baseline
   on the SUPERB speech tasks under both clean and CHiME-3 noisy
   conditions. ..."

→ Note: Even after this revision the author chose not to add numeric
  magnitudes, which ES then asked for again (see Example A9). The agent
  should keep flagging the absence of numbers until they are added, not
  stop at task naming alone.
```

### Example A9: Abstract still lacks % improvement, corpus, and competing-method comparison

```
[ES | April 2026] MISSING-NUMBERS (MUST-FIX): A second pass over the
  improved abstract still lacked numeric magnitudes and explicit comparisons.

→ Supervisor comment (verbatim):
  "Pls improve further the abstract -> details like experimental results
   improvement, % over what corpus using what methods over what competitive
   methods missing."

→ Interpretation: ES decomposes the missing information into four pieces
  the abstract must contain: (a) experimental results improvement, (b) %
  magnitude, (c) over what corpus, (d) over what competitive methods. All
  four must be present per claim. Naming the tasks alone is not enough.

→ Fix direction: For each contribution claim in the abstract, add a clause
  of the form "improves by X% / X points on [corpus or task] over
  [competitive baseline]". Use absolute points where percentages would be
  misleading (e.g. accuracy on a single task) and percent-of-baseline for
  WER-style metrics.

→ Tone calibration: ES uses arrows and abbreviated sentences ("Pls", "->",
  trailing fragment). The agent's MISSING-NUMBERS comments may emulate this
  brevity for structural items: "Add % improvement -> over what corpus, vs
  which method?"
```

---

## Category B: Research Question Framing

### Example B1: Chapter 2 question structure and mapping to contributions

```
[ES | 14 Feb 2026] LOGIC (MUST-FIX): The Chapter 2 section numbering was
  2.1 (SSL), 2.2 (?), 2.3 (?), 2.4 (Research Gaps). The student's mapping
  between literature sections and contribution chapters was not explicit.

→ Supervisor comment (verbatim):
  "2.4 research gaps to put inside your subsection discussing the lit
   background. Which is your 2.2 and 2.3
   - So I assume that your contributions directly address 2.2 and 2.3?
     Is the above true? I assume ch 2.2 support ch 3?
   - By having 2.3 -> does that support ch 4?"

→ Interpretation: The supervisor expects every literature subsection to have
  an explicit gap statement at its end, and each gap must map to a specific
  contribution chapter. A standalone "research gaps" section at the end of
  Chapter 2 is the wrong structure.

→ Fix direction: Dissolve the "Research Gaps" section. Embed a gap paragraph
  at the end of each relevant literature subsection, and explicitly state
  which contribution chapter it motivates.
```

### Example B2: Page budget mismatch across chapters

```
[ES | 14 Feb 2026] SCOPE (SHOULD-FIX): Planned page allocations show Ch 2 at
  22 pages and Ch 3 at 35 pages.

→ Supervisor comment (verbatim):
  "Ch 2 has 22 pages, Ch 3 has 35 pages, you need to balance ch2 increase
   -> 30 pages?"

→ Interpretation: A literature chapter that is substantially shorter than
  a single contribution chapter suggests the lit review is too thin. The
  supervisor wants the imbalance fixed. Content accross the thesis must be balanced.
```

### Example B3: Duplicated related-work sections

```
[ES | 14 Feb 2026] REDUNDANT (MUST-FIX): Chapter 3 contained its own
  Section 3.2 "Related Work" in addition to the Chapter 2 literature review.

→ Supervisor comment (verbatim):
  "In ch 3, again you have 3.2 (related work?) how different to ch 2?
   History and background?"

→ Interpretation: If Chapter 2 is doing its job, Chapter 3 should not repeat
  related work. Either cut it, or reduce it to a single paragraph that cites
  back to the Chapter 2 discussion.

→ Fix direction: Slim Section 3.2 to a brief pointer paragraph that
  cross-references Chapter 2 rather than re-reviewing the literature.
```

### Example B4: Consistency of evaluation benchmarks across chapters

```
[ES | 14 Feb 2026] SCOPE (MUST-FIX): Chapter 3 evaluates only three SUPERB
  tasks while Chapter 4 evaluates the full SUPERB + MARBLE suite.

→ Supervisor comment (verbatim):
  "You mention superb and marble -> are these used in ch 3 and 4?"

→ Interpretation: Benchmarks introduced in Chapter 2 should be used
  consistently across contribution chapters, or the inconsistency must be
  justified.

→ Fix direction: Either expand Chapter 3's evaluation to cover more SUPERB
  tasks (and ideally some MARBLE tasks), or add a sentence justifying why
  Chapter 3 uses a subset.
```

### Example B5: Chapter 2 over-long and poorly subdivided

```
[ES | 14 Feb 2026] STRUCTURE (SHOULD-FIX): Section 2.1 on SSL contained
  subsections 2.1.1 through 2.1.7, all flat under one heading.

→ Supervisor comment (verbatim):
  "ch 2.1 is too long, move 2.1.6, 2.1.7 as new subsection?"

→ Interpretation: Flat subsection lists that run beyond five or six entries
  are unreadable. Grouping related subsections into a new top-level subsection
  improves navigation.

→ Fix direction: Move 2.1.6 and 2.1.7 under a new top-level 2.x dedicated to
  SSL downstream evaluation.
```

### Example B6: Argumentation gaps in the initial thesis proposal

```
[Nancy | 27 Jan 2026] LOGIC (MUST-FIX): The initial proposal listed chapters
  and publications but did not include an abstract or a list of research
  questions.

→ Supervisor comment (verbatim):
  "I would especially appreciate to have the abstract and list of research
   questions so we can more closely examine where are the argumentation
   gaps that we should fill in."

→ Interpretation: A proposal without an abstract and research questions
  cannot be evaluated for argument structure. These must be produced before
  substantive chapter review is possible.

→ Fix direction: Produce an abstract, a numbered list of research questions
  grouped by chapter, and a mapping from questions to published papers.
```

---

## Category C: Notation, Symbols, and Equation Introduction

This category is thin in the email record. The supervisor's notation feedback appears primarily in Jeremy's inline PDF annotations rather than in the email chain. Below are the grounded examples I can cite; all come from Jeremy's Chapter 3 PDF annotations.

### Example C1: Vague hedging without mechanism

```
[Jeremy | March 2026] VERBOSE (MUST-FIX): Chapter 3 motivation read
  "a cross-correlation metric computed between teacher and student
   representations may capture shared task-relevant structure while being
   less sensitive to noise components that affect the two models differently."

→ Supervisor comment (verbatim): "not sure what 'less sensitive' means in
  this context."

→ Interpretation: "Less sensitive" is too loose for a motivation paragraph
  that introduces the core method. The mechanism must be named.

→ Fix: Rewrite to state the mechanism in terms of independence. "Because
  the noise distortions applied to teacher and student inputs are sampled
  independently, noise components in one model's representations are
  unlikely to be linearly dependent on those in the other, and thus
  contribute less to the cross-correlation signal than shared task-relevant
  structure."
```

### Example C2: Shared initialisation left undefined

```
[Jeremy | March 2026] UNDEFINED (SHOULD-FIX): Abstract used "shared
  initialization" without saying what it means.

→ Supervisor comment (verbatim): "that were initialised from a common
  parameter set"

→ Interpretation: The reviewer is giving you the exact replacement wording.
  Use it.

→ Fix: "...without requiring that the models were initialised from a common
  parameter set, and without retraining."
```

### Example C3: Reviewer-flagged recurring patterns (from `feedback_revision.md`)

These are not single quotes but recurring annotation shorthands Jeremy uses. They should inform how the agent phrases its own comments.

| Shorthand | Meaning | Typical trigger |
|---|---|---|
| "proper sentence" | Fragment, run-on, or telegraphic phrasing | Missing subject, comma-spliced clauses |
| "proper sentence" (on an equation) | Equation introduced by a fragment | "The loss. $\mathcal{L} = ...$" |
| "why upper case?" | Unnecessary capitalisation of a common noun | "Flexible Domain Unification" |
| "undefined" | Symbol, acronym, or term used before definition | $P$ used without explanation |
| "add reference" | Factual claim without citation | "SSL models have shown..." with no cite |
| "too definitive" | Claim without supporting evidence | "ensures", "guarantees", "prevents" |
| "nothing is ensured" | Same as above, more direct | Strong claims on a loss function |
| "british spelling" | Spelling inconsistency | "maximization" in a British-spelling thesis |

### Example C4: Terminological precision on model vs. representation

```
[Jeremy | March 2026] ATTRIBUTION (SHOULD-FIX): §1.1 read
  "In practice, these SSL representations are adapted to specific downstream
   tasks either by full-finetuning the SSL model..."

→ Supervisor interpretation: You cannot fine-tune a representation. You
  fine-tune the model that produces the representation.

→ Fix: "In practice, SSL models are adapted to downstream tasks through
  full fine-tuning or by learning a linear combination of their frozen
  hidden-layer representations."
```

Note that I do not have direct written quotes on equation-introduction style from ES or Nancy. If the agent needs stronger calibration on this, it should rely on the shorthand table above plus the style-guide rule that "every equation has a preceding sentence explaining what it computes" from `thesis_style_guide.md`.

---

## Category D: Chapter-Opening and Literature-Review Issues

### Example D1: Chapter opening as a table of contents

```
[ES | 24 Feb 2026] SCOPE (MUST-FIX): The Chapter 2 opening read:

  "This chapter provides the foundational background for the three core
   contributions of this thesis. Section 2.1 examines self-supervised
   learning (SSL) for speech and music, covering the principal pre-training
   paradigms and the models most relevant to this work: HuBERT, WavLM, and
   MERT. Section 2.2 introduces the SUPERB and MARBLE evaluation benchmarks,
   which together define the 11-task evaluation protocol adopted throughout
   this thesis. Section 2.3 reviews knowledge distillation techniques for
   compressing large SSL models, with particular attention to noise
   robustness in distilled models and the research gap motivating our
   correlation-based approach (Chapter 3). Finally, Section 2.4 surveys
   model merging methods, including task arithmetic and permutation-based
   alignment, identifying the limitations that motivate the contributions
   of Chapter 4 and Chapter 5."

→ Supervisor comment (verbatim):
  "The beginning of ch 2, it should looks more like an abstract to a paper,
   its an abstract to the chapter.
   - And why and how does the above support your thesis
   - You have some infor, but its not enough"

→ Interpretation: This opening describes what each section covers but does
  not say what the chapter itself contributes to the thesis. The supervisor
  wants a compressed chapter abstract that states the problem, the key
  findings of the literature, and the thesis-level gap these findings expose.

→ Fix direction: Replace the section-by-section signposting with a three or
  four paragraph chapter abstract. Paragraph one: the problem the chapter is
  about. Paragraph two: what the literature has established. Paragraph three:
  the specific gap or limitation that motivates the thesis contributions.
  Then begin Section 2.1.
```

### Example D2: Research gap placement

```
[ES | 14 Feb 2026] STRUCTURE (MUST-FIX): The student placed all research gaps
  in a single Section 2.4 at the end of Chapter 2.

→ Supervisor comment (verbatim):
  "2.4 research gaps to put inside your subsection discussing the lit
   background. Which is your 2.2 and 2.3"

→ Interpretation: Gaps must be embedded at the end of the relevant literature
  subsection, not collected at the end of the chapter. Each gap should sit
  next to the evidence that exposes it.

→ Fix direction: Dissolve Section 2.4. At the end of each subsection in 2.2
  and 2.3, add one paragraph titled or labelled "Research gap" that names the
  limitation and the contribution chapter that addresses it.
```

### Example D3: Chapter mapping must be explicit

```
[ES | 14 Feb 2026] LOGIC (MUST-FIX): The mapping between literature subsections
  and contribution chapters was implicit.

→ Supervisor comment (verbatim):
  "So I assume that your contributions directly address 2.2 and 2.3? Is the
   above true? I assume ch 2.2 support ch 3? By having 2.3 -> does that
   support ch 4?"

→ Interpretation: Stated as questions, but the supervisor is asserting that
  each literature subsection must map to a contribution chapter, and the
  mapping must be stated explicitly in the chapter abstract or in each gap
  paragraph.

→ Fix direction: In the chapter abstract, name the mapping. For example:
  "Section 2.2 reviews knowledge distillation and identifies the limitation
  that motivates Chapter 3. Section 2.3 reviews model merging and identifies
  the two limitations that motivate Chapters 4 and 5."
```

### Example D4: Chapter-internal related work duplicates the lit review

```
[ES | 14 Feb 2026] REDUNDANT (MUST-FIX): Chapter 3 contained its own Section
  3.2 titled "Related Work".

→ Supervisor comment (verbatim):
  "In ch 3, again you have 3.2 (related work?) how different to ch 2?
   History and background?"

→ Interpretation: If Chapter 2 reviews the literature, Chapter 3 should not
  repeat it. A contribution chapter's related work section should cite back
  to Chapter 2 and only introduce material that is specifically needed to
  situate the contribution.

→ Fix direction: Reduce Section 3.2 to one paragraph that references the
  relevant subsection of Chapter 2 and introduces only the specific prior
  works that are directly compared against in Chapter 3.
```

### Example D5: Chapter 1 introduces SSL in prose only; high-level figure missing

```
[ES | April 2026] NO-CH1-FIGURE (SHOULD-FIX): Section 1.1 of Chapter 1
  introduced HuBERT, MERT, and the SSL framework using prose paragraphs
  alone. A diagram covering the same material existed in Chapter 2 (the
  literature review) but not in the introduction.

→ Supervisor comment (paraphrased from the meeting):
  ES asked for a high-level visual explanation of SSL to be moved into
  Chapter 1. The figure must clarify, on one page: the input modality
  (continuous waveform; speech, music, or environmental sound), the SSL
  architecture family, the pre-training objective, whether the produced
  representation is continuous, and how the representation connects to
  downstream tasks.

→ Interpretation: An introduction that defines SSL only in prose forces
  five definitional jobs into the same paragraph. A figure separates the
  conceptual layer from the literature-review-level detail. The figure
  belongs in Chapter 1 even at the cost of duplicating content already
  shown in Chapter 2; if duplication is undesirable, the Chapter 2 instance
  should be removed or specialised.

→ Fix (as applied): The author improved the existing Chapter 2 figure and
  promoted it to Chapter 1, keeping the Chapter 2 version only where it
  carries detail not appropriate for an introduction.
```

---

## Category E: Chapter 1 Contribution Subsections

### Example E1: Contribution paragraph closes without performance numbers

```
[ES | April 2026] MISSING-NUMBERS (MUST-FIX): The §1.2.1 contribution
  paragraph for the correlation-based distillation framework ended with:
  "This contribution has been evaluated across 11 speech and music
  downstream tasks under both clean and noisy conditions."

→ Supervisor comment (verbatim): "Conclusions?? Performance??"

→ Interpretation: A contribution paragraph in Chapter 1 must close with a
  numeric outcome sentence. ES considers "evaluated across N tasks" to be
  scope information, not a result. A concluding result sentence must name
  the magnitude of improvement, the baseline compared against, and ideally
  one representative task with absolute numbers. Without this, the
  contribution is unverified at the introduction level.

→ Fix (as applied):
  "The framework is evaluated across nine downstream tasks spanning speech,
   music, and environmental sound under clean and noisy (CHiME-3, 10 dB
   SNR) conditions. The proposed loss improves over the standard
   noise-robust distillation baseline on all four SUPERB speech tasks.
   Intent classification, for instance, gains 3.58 accuracy points on
   clean speech and 4.77 on noisy speech, narrowing the clean-to-noisy
   degradation gap on this task from 3.74 to 2.55 points compared to the
   previous noise-robust distillation method."

→ Apply the same closure to every §1.2.x: each contribution must end with
  a sentence of the form "Method M gains X points on task T compared with
  baseline B under condition C". One representative task is enough; the
  full per-task table belongs in the contribution chapter.

→ Note for the agent: this rule resolves an apparent conflict with the
  older "no numbers in the introduction" guidance. ES wants numbers in
  §1.2 contribution paragraphs and in the abstract. He does not want
  numbers spread through §1.1 motivation prose; that is where the older
  guidance still applies. The distinction is by paragraph role, not by
  chapter.
```

---

## Category F: Paragraph Cohesion and Flow

### Example F1: Paragraph break splits a single logical movement

```
[ES | April 2026] OVER-FRAGMENTED (SHOULD-FIX): Section 1.1 closed one
  paragraph with the sentence "...yielding representations specialised to
  their respective domains." and immediately opened a new paragraph:
  "Despite the strong downstream performance of these models, several
  limitations hinder their practical deployment and restrict their
  applicability. This thesis identifies three key limitations that motivate
  the research presented in the subsequent chapters."

→ Supervisor comment (verbatim):
  "Join the text. Your paragraph breaks too finely. Same idea can be
   merged!"

→ Interpretation: ES reads the two paragraphs as one logical movement:
  prominent SSL models exist; they have limitations this thesis addresses.
  A paragraph break here forces the reader to re-acquire the subject and
  signals a topic shift that does not actually occur. Drop the meta-sentence
  "This thesis identifies three key limitations..." if the next section
  immediately enumerates them; it is restating intent rather than carrying
  new information.

→ Fix (as applied):
  "The progress of SSL in audio has produced several prominent models. For
   speech, HuBERT representations perform competitively on the SUPERB
   benchmark. For music, MERT adopts a similar architecture but uses
   music-specific acoustic features and pre-training data, with comparable
   success on the MARBLE benchmark. Although architecturally similar, the
   two models are pre-trained on different data and objectives, yielding
   representations specialised to their respective domains. Despite their
   strong downstream performance, several limitations hinder their
   practical deployment. This thesis identifies three such limitations,
   which motivate the research presented in the subsequent chapters."

→ Heuristic for the agent: If two consecutive paragraphs share the same
  grammatical subject (or refer to it by pronoun), and the second paragraph
  opens with "Despite", "However", "Although", "Nonetheless", or a similar
  contrast connective referring back to the first, consider OVER-FRAGMENTED
  before suggesting any other restructuring. The default fix is to merge,
  not to add a transition sentence.

→ Counter-heuristic (do not over-merge): If the second paragraph introduces
  a new subject, a new section's claim, or a list of items that justify a
  separate paragraph for visual scanning, leave the break. OVER-FRAGMENTED
  is for repeated subject and continuous logical flow only.
```

---

## Tone Calibration Notes for the Agent

Having read the real quotes, a few observations about how ES and Nancy phrase feedback that the agent should replicate:

1. **ES uses bullets, not prose.** His emails are short, numbered, and often written as half-sentences with arrow pointers. The agent should emulate this compression for structural comments.

2. **ES often phrases a demand as a question.** "Ch 2 has 22 pages, Ch 3 has 35 pages, you need to balance ch2 increase->30 pages?" ends in a question mark but is a directive. The agent can do the same when flagging structural problems.

3. **Nancy uses softer framing.** "Would it make sense to..." and "I would especially appreciate to have..." are her registers. For argumentation-level feedback, the agent can use the softer register. For structural and line-level errors, stay closer to ES's terseness.

4. **Jeremy's shorthand is two or three words.** "proper sentence", "why upper case?", "undefined". The agent should use these literal shorthands where they fit, because the student recognises them.

5. **Never pad.** None of the three sources add decorative sentences. If the comment is one word ("improvements"), leave it at one word.

