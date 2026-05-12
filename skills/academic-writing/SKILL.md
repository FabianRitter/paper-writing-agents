---
name: academic-writing
description: "Reference skill that codifies the prose standards enforced across every stage of the Supervisor-Agent workflow (abstract, list-of-questions phrasing, point-form phrasing, full chapter draft). Load whenever the user asks to write, revise, or tighten academic text for a thesis chapter, conference paper, or journal manuscript. Trigger on phrases like 'write a section', 'revise this paragraph', 'tighten the writing', 'make it less verbose', 'check my introduction', 'rewrite for the thesis', 'academic writing', 'paper draft', 'thesis draft', 'revise stage 6', or when the user provides LaTeX source and asks for improvements. Also auto-loaded as a dependency by the supervisor-feedback, list-of-questions, and point-form-answers skills whenever they need to cite a prose rule. OVERRIDES any default tendency toward verbose, hedging, or decorative prose."
---

# Academic Writing Skill

This skill enforces tight, precise academic prose for engineering theses and ML/speech/audio conference papers. It codifies the writing standards derived from real supervisor feedback (Prof. Chng Eng Siong, NTU), reviewer comments, and iterative revision history.

The guiding principle: **say it once, say it precisely, and move on.** Every sentence must earn its place. When the reader already knows something, do not repeat it.

This skill also encodes the author's natural writing voice (Section 10). The goal is to produce text that sounds like the author wrote it, not generic academic prose. Follow the error-avoidance rules (Sections 1–9) strictly, but within those constraints, write in the voice described in Section 10.

---

## 1. Core Prose Rules

### 1.1 One idea, one sentence

Each sentence carries exactly one claim or one piece of information. If a sentence has more than two commas, split it.

**Bad:**
```
SSL models exploit structural regularities present in raw waveforms such as
phonetic patterns, harmonic structures and temporal dependencies as their
implicit supervision, and such structural dependencies allow learning
representations without the need of expensive manual annotation.
```

**Good:**
```
SSL models exploit structural regularities in raw waveforms as implicit
supervision. These regularities include phonetic patterns, harmonic
structures, and temporal dependencies.
```

### 1.2 No redundant restatement

Never repeat the same idea across consecutive sentences or across sections. If Section 1.1 already established that distilled models degrade under noise, Section 1.2 must not re-explain why. A brief forward reference suffices.

**Bad (42 words):**
```
Existing approaches to improve the noise robustness of distilled models,
such as Robust DistilHuBERT, augment the distillation training with noisy
input and adversarial training via noise classifiers to encourage
noise-invariant representations. These methods have demonstrated a certain
degree of robustness to in-domain training noise. Nonetheless, these methods
depend on the teacher model being robust to noise...
```

**Good (18 words):**
```
Existing methods such as Robust DistilHuBERT improve in-domain robustness
but remain teacher-dependent and do not generalise to unseen noise conditions.
```

### 1.3 No connective hedging

Remove filler connectives that add no logical content. Cut "Furthermore,", "Besides,", "Additionally,", "It is also worth noting that", "Moreover,", "In addition," unless the sentence genuinely adds a new dimension that requires explicit signposting.

**Bad:**
```
Besides, this proposed formulation avoids the need for high-dimensional
projector layers, incurring in no additional trainable parameters during
distillation.
```

**Good:**
```
The formulation requires no projector layers and adds no trainable parameters.
```

**Exception — emphasis connectives with logical weight:** "Notably,", "Crucially,", and "Hence," are acceptable when they mark a genuine logical turning point or highlight a non-obvious implication. Use them sparingly (at most once per subsection) and only when the sentence that follows would lose emphasis without them.

**Acceptable:**
```
Crucially, this approach lacks flexibility; adjusting the emphasis between
speech and music requires complete retraining.
```

### 1.4 No double em-dashes

Never use em-dashes (---) or en-dashes (--) as parenthetical insertions. Use commas, full stops, or restructure the sentence.

**Bad:**
```
The approach --- unlike joint distillation --- avoids loading both teachers.
```

**Good:**
```
Unlike joint distillation, the approach avoids loading both teachers.
```

### 1.5 Minimal parentheses

Avoid using parentheses to explain a concept inline. If the explanation is necessary, make it a proper clause or sentence. Parentheses are acceptable only for acronym definitions, citations, and short factual asides like parameter counts.

**Bad:**
```
The model is teacher-agnostic (meaning the student's noise robustness does
not depend on whether the teacher itself is robust to noise).
```

**Good:**
```
The model is teacher-agnostic. The student's noise robustness does not
depend on whether the teacher itself is robust to noise.
```

### 1.6 Plain sentence structure

Prefer subject-verb-object order. Avoid inverted or nested clause structures that force the reader to hold multiple contexts in memory.

**Bad:**
```
By driving the cross-correlation matrix between the teacher and student
representations towards an identity matrix, the cross-correlation term
ensures that the student learns the teacher's representational behaviour.
```

**Good:**
```
The cross-correlation term aligns the teacher and student feature spaces,
encouraging the student to reproduce the teacher's representational behaviour.
```

### 1.7 No clause-introducing colons

Avoid using colons to introduce explanatory clauses where a full stop or conjunction is more appropriate. Colons are acceptable before lists and before formal definitions.

**Bad:**
```
We observed that SID and PitchID exhibit opposing sensitivities to the
interpolation weights: configurations that improve one tend to degrade
the other.
```

**Good:**
```
We observed that SID and PitchID exhibit opposing sensitivities to the
interpolation weights. Configurations that improve one tend to degrade
the other.
```

---

## 2. Overclaiming Prevention

### 2.1 Hedge table

Use hedged language unless the claim is directly supported by a theorem or an experimental table on the same page.

| Avoid | Prefer |
|---|---|
| ensures / guarantees | encourages / promotes |
| the most prominent | a prominent |
| too large for deployment | difficult to deploy |
| demand a single model | benefit from a single model |
| should yield | has the potential to yield |
| enhancements | improvements |
| achieves noise robustness | improves noise robustness |
| novel | new / proposed |
| state-of-the-art | competitive / strong |
| optimal | effective / favourable |
| prove / proof (without formal proof) | demonstrate / show / indicate |

### 2.2 Hedged causal reasoning

When interpreting experimental results, hedge the *cause* of an observed effect. State the observation directly, then frame the explanation as plausible rather than certain.

**Pattern:** "[Observation]. Such results may be justified by [reason]." or "[Observation]. This suggests that [interpretation]."

**Bad:**
```
Adding more data hurts performance because models trained on larger datasets
are pushed further apart in the weight space.
```

**Good:**
```
Adding more pre-training data does not consistently improve performance.
Such results may be justified by two factors. First, models trained on
larger data may be pushed further apart in the weight space, degrading
interpolation. Second, the distillation process may rely more on the
teacher model's representational quality than on data diversity.
```

Note the structure: factual observation first, then hedged causes numbered explicitly. This is distinct from overclaiming prevention (Section 2.1), which concerns claims about one's own method. Hedged causal reasoning concerns interpretation of why an empirical pattern occurs.

### 2.3 Numbers in introductory chapters

The default in this repo's supervisor calibration is the opposite of the conservative style guide: **the abstract and the Chapter 1 contribution subsections (§1.2.x) must include quantitative results**, because Prof. Chng will explicitly ask for them when they are missing ("Conclusions?? Performance??", "Add some numbers of performance, to improve by how much, is it sota? etc.", "% over what corpus using what methods over what competitive methods missing"). When you write or revise these locations, include four pieces per claim:

1. The magnitude of improvement (absolute points or percent of baseline).
2. The baseline or competing method being compared against.
3. The corpus, benchmark, or noise condition.
4. The specific tasks named individually rather than aggregated as a domain ("ASR, KS, IC, ER, SID", not "five speech tasks").

**Bad (qualitative only):** `improves speech task performance under both clean and noisy conditions`
**Good (with the four pieces):** `improves over the standard distillation baseline on the four SUPERB speech tasks under CHiME-3 noisy conditions, with intent classification gaining 4.77 accuracy points`

**Where the old "no numbers" rule still applies:** The §1.1 motivation prose (problem landscape, domain context) still avoids numerical clutter; numbers live in §1.2 contribution paragraphs and the abstract, not in the motivation. The distinction is by paragraph role, not by chapter. Do not seed §1.1 with parameter counts or percentages from the experimental chapters.

**If the student has not yet measured the numbers:** flag the gap with `MISSING-NUMBERS` rather than inventing a magnitude. Suggest the structure ("X points on task T vs baseline B under corpus C") and let the student fill in the values from their tables.

### 2.4 Attribution of downstream performance

The upstream SSL model produces representations. The downstream model performs the task. Never conflate the two.

**Bad:** `HuBERT achieves strong ASR performance`
**Good:** `When paired with a downstream ASR model, HuBERT representations yield strong word error rates`

---

## 3. Structural Rules

### 3.1 Introduction chapter structure

An introduction chapter has three jobs: motivate, state contributions, and outline organisation. It should not review the literature or explain mechanisms in detail.

**Section 1.1 (Motivation):** State the problem landscape. Name limitations and gaps. Do not describe solutions or cite methods in detail. Open Chapter 1 with a high-level visual summary of the broad framework (e.g. SSL): one figure that labels input modality, architecture family, pre-training objective, whether the produced representation is continuous, and how it connects to downstream tasks. If a stronger version of this figure already lives in the literature review, promote (or duplicate) it into Section 1.1 rather than leave the introduction prose-only.

**Section 1.2 (Contributions):** For each contribution, follow this template:
1. One sentence naming the problem addressed (without re-explaining it if Section 1.1 already did).
2. One sentence stating the key idea.
3. One sentence stating the key property or advantage.
4. One sentence describing the evaluation scope (tasks, corpora, conditions). Name the tasks individually rather than aggregated as a domain ("ASR, KS, IC, ER, SID", not "five speech tasks").
5. One sentence with the quantitative outcome: name the magnitude of improvement, the baseline or competing method, and at least one representative task. Pattern: "Method M improves over baseline B on task T by X points / X% under condition C." If two outcomes matter (e.g. clean and noisy), give both.

Steps 4 and 5 may merge into one sentence when the prose flows naturally; both pieces of information must be present. Do not describe internal mechanisms such as specific loss terms, matrix operations, or architectural details. These belong in the methodology chapters.

**Section 1.3 (Organisation):** Brief. Two to three sentences per chapter. Do not restate the unifying theme if it was already introduced.

### 3.2 Contribution subsection openings

Vary the syntactic opening of each contribution subsection. Do not start consecutive subsections with "The first/second/third contribution addresses..."

**Good pattern:**
- Subsection 1: "To address [problem], we introduce..."
- Subsection 2: "Building on [previous contribution], we propose..."
- Subsection 3: "While [previous approach] requires [constraint], the third contribution removes this requirement by..."

### 3.3 No duplicate lists

If downstream tasks are enumerated in Section 1.1, do not re-enumerate them in Section 1.2. One list is sufficient. The full enumeration belongs in the literature review or experimental setup.

### 3.4 Unifying theme stated once

The thesis unifying theme should be stated clearly in one location. A brief reminder is acceptable in the thesis organisation section, but full re-explanation is not.

---

## 4. Sentence-Level Checks

### 4.1 Complete sentences

Every sentence must have a subject and a verb. No fragments. No telegraphic phrasing.

**Bad:** `Classifies the fundamental pitch of isolated instrumental notes.`
**Good:** `This task classifies the fundamental pitch of isolated instrumental notes.`

### 4.2 Ambiguous pronouns

Replace "this", "they", "it" with the specific noun when the antecedent is unclear.

**Bad:** `They additionally show that such discrete labels...`
**Good:** `The authors of [citation] additionally show that such discrete labels...`

### 4.3 Paragraph cohesion

Two symmetric rules govern paragraph length:

1. **Single-sentence paragraphs.** Every paragraph has at least two sentences. If it cannot be expanded, merge it with an adjacent paragraph.

2. **Over-fragmentation.** Conversely, do not break a single logical movement into two consecutive paragraphs. Prof. Chng's verbatim phrasing on this is: *"Join the text. Your paragraph breaks too finely. Same idea can be merged!"* When two consecutive paragraphs share the same grammatical subject (or refer to it by pronoun) and the second opens with "Despite", "However", "Although", or "Nonetheless" referring back to the first, merge them. Drop any meta-sentence that only restates intent ("This thesis identifies three key limitations...") if the next paragraph already enumerates them.

Counter-rule: if the second paragraph introduces a new subject, a new section's claim, or a list of items that justify a separate paragraph for visual scanning, leave the break. Merging is the default only when the logical movement is continuous.

### 4.4 Terminological precision

Do not mix the artifact (representation) with the generator (model). Do not use "fine-tune a representation" when you mean "fine-tune the model". Do not conflate "noise" with "acoustic events" unless the context is unambiguous.

### 4.5 Acronym discipline

Expand every acronym on first use, even common ones (CNN, GPU, SSL). After first expansion, use only the acronym.

---

## 5. Formatting and Notation (LaTeX)

### 5.1 British spelling

Use British English throughout. Search each chapter for "-ize", "-ization", "-eled", "-eling" and correct all instances.

| American (avoid) | British (use) |
|---|---|
| labeled | labelled |
| modeling | modelling |
| initialize | initialise |
| optimize | optimise |
| generalize | generalise |
| organize | organise |
| analyze | analyse |

### 5.2 Notation consistency

| Type | Format | Example |
|---|---|---|
| Scalar | italic, not bold | $t$, $D$, $\lambda$ |
| Vector | bold lowercase | $\boldsymbol{x}$, $\boldsymbol{z}$ |
| Matrix | bold uppercase | $\mathbf{W}$, $\mathbf{C}$ |
| Function | plain italic | $f(\cdot)$, $\sigma(\cdot)$ |
| Set / space | calligraphic | $\mathcal{X}$, $\mathcal{D}$ |

### 5.3 Equation introduction

Every equation must be preceded by a complete sentence that explains what it computes. The reader must never encounter an equation without knowing its purpose.

### 5.4 Colons in formal prose

Avoid colons to introduce clauses. Use full stops or conjunctions instead. Colons are acceptable before lists or formal definitions.

### 5.5 Capitalisation

Do not capitalise common nouns or compound terms unless they are proper nouns or established names. "audio large language models" not "Audio Large Language Models". Exception: benchmark names (SUPERB, MARBLE).

---

## 6. Revision Workflow

When revising existing text:

1. **Read the full section first** to understand context before making local changes.
2. **Produce old → new pairs** for manual application in Overleaf. Do not rewrite entire files.
3. **Minimal diff.** Change only what the feedback requires. Do not rewrite surrounding paragraphs.
4. **Preserve LaTeX commands.** Keep all `\cite{}`, `\ref{}`, `\label{}`, `\gls{}`, `\thesisrevision{}` commands intact.
5. **Mark pending items** as `\textit{TBD}` in black. Mark hypotheses or incomplete sections in `\textcolor{red}{}`.

---

## 7. Pre-Submission Checklist

Run through these checks before sending any chapter:

- [ ] Read every sentence aloud. If you run out of breath, split it.
- [ ] Search for "ensure", "guarantee", "demand", "too large", "the most", "novel". Soften all.
- [ ] Search for undefined acronyms. First use must have expansion.
- [ ] Verify all symbols are defined on or near first use.
- [ ] Verify notation consistency: vectors bold, matrices bold uppercase, scalars plain italic.
- [ ] Search for American spellings: "-ize", "-ization", "-eled", "-eling".
- [ ] Verify every equation has a preceding sentence.
- [ ] Check for ambiguous "this", "they", "it". Replace with specific nouns.
- [ ] Check for single-sentence paragraphs. Merge or expand.
- [ ] Check for over-fragmented paragraphs: same subject, contrastive opener ("Despite", "However"), continuous logical flow. Merge them.
- [ ] Verify upstream vs downstream attribution is clear.
- [ ] Remove colons used to introduce clauses.
- [ ] Remove unnecessary capitalisation of common nouns.
- [ ] In the abstract and §1.2 contribution paragraphs, verify that each result claim names the magnitude, baseline, corpus, and the individual tasks (not aggregated as a domain). Flag missing pieces with `MISSING-NUMBERS`.
- [ ] In Chapter 1, verify that a high-level visual figure exists near the opening. If only prose is present, flag with `NO-CH1-FIGURE`.
- [ ] Verify each section opens with context before technical detail.
- [ ] Check that no idea is stated twice across consecutive paragraphs.
- [ ] Remove all filler connectives ("Furthermore", "Besides", "Additionally") unless logically necessary.
- [ ] Remove all em-dashes. Restructure with commas or full stops.
- [ ] Remove explanatory parentheses. Promote to proper clauses.

---

## 8. Section-Specific Guidance

### 8.1 Abstract

Three to four sentences maximum per component: background, problem, method, result. No citations. No acronym definitions beyond the most essential. **Include numbers.** Prof. Chng explicitly asks for them when they are missing: "Add some numbers of performance, to improve by how much, is it sota? etc.", and again "% over what corpus using what methods over what competitive methods missing". For each result claim, include the magnitude (X points or X%), the corpus or benchmark, and the competing method. Name the tasks individually (e.g. "ASR, KS, IC, ER, SID") rather than aggregated as a domain ("five speech tasks"). If a result is genuinely state of the art, say so; if it is competitive but not SOTA, use the word "competitive" with the named comparison method.

### 8.2 Introduction (Paper)

Follow the funnel structure: broad context (2-3 sentences) → specific problem (2-3 sentences) → gap in existing work (2-3 sentences) → proposed approach (2-3 sentences) → contributions list (numbered, one sentence each) → paper organisation (optional, one sentence per section).

### 8.3 Related Work

Organise by theme, not chronologically. Each paragraph covers one theme. The final sentence of each paragraph positions the current work relative to the reviewed literature. Do not merely list papers.

### 8.4 Method

Open with a problem formulation paragraph that defines notation. Follow with subsections for each component. End each subsection by connecting the component to the overall method. Use algorithm blocks for procedural steps.

### 8.5 Experiments

Open with experimental setup (dataset, metrics, baselines, implementation). Follow with results organised by research question or hypothesis. Each result paragraph: state the finding, cite the table or figure, explain why. Do not speculate beyond what the data shows.

**Question-driven structure (conference papers):** For short papers (e.g. Interspeech, ICASSP), organising experiments around explicit research questions is effective. Frame each subsection as a question the reader would naturally ask, then answer it with evidence.

**Pattern:**
```
Question 1: Why can't we directly merge HuBERT and MERT rather than
distill them and merge them?

Table 1 demonstrates that naively merging HuBERT and MERT by averaging
their weights leads to poor performance across all tasks. [evidence follows]
```

This is distinct from inline rhetorical questions (which remain prohibited, see Section 9). Structural questions are paragraph or subsection headings that frame the experimental narrative. They are acceptable in conference papers. In thesis chapters, prefer declarative subsection titles ("Effect of interpolation weights") over question titles, unless the chapter is adapting a published paper that already uses question framing.

### 8.6 Conclusion

Three paragraphs maximum. Summarise contributions without re-explaining methods. State limitations honestly. Suggest concrete future directions, not vague aspirations.

---

## 9. Common Patterns to Avoid

| Pattern | Problem | Fix |
|---|---|---|
| "In this work, we propose..." repeated | Redundant across abstract, intro, and method | State once in the introduction. In method, jump directly into formulation. |
| Inline rhetorical questions | Informal tone | Rewrite as declarative statements. |
| "It is worth noting that" | Filler | Delete the phrase. Start with the actual content. |
| Three-way synonym chains | Verbose | Pick the most precise word. Use it once. |
| "In order to" | Verbose | Replace with "To". |
| "Due to the fact that" | Verbose | Replace with "Because". |
| "A number of" | Vague | Replace with "Several" or give the actual number. |
| "In the context of" | Verbose | Replace with "In" or "For". |
| "It can be seen that" | Empty | Delete. State the observation directly. |
| "We can observe that" | Empty | Delete. State the observation directly. |
| "As mentioned earlier" | If it needs re-mentioning, re-state the fact. Otherwise delete. | Either a brief phrase or cut entirely. |

**Note on structural vs inline questions:** The ban on rhetorical questions (row 2) applies to inline questions embedded in flowing prose, e.g. "But what happens when we add noise?". It does NOT apply to explicit question-framed subsection headings used to organise experimental narratives (see Section 8.5). The distinction is: if the question acts as a section organiser and is immediately followed by evidence, it is structural. If it appears mid-paragraph as a stylistic device, it is rhetorical and should be rewritten.

---

## 10. Voice Profile

This section captures the author's natural writing register. When producing new text, write within these patterns. They are compatible with all error-avoidance rules in Sections 1–9.

### 10.1 Register and tone

The target register is **semi-formal and confident**. Not stiff or impersonal, not conversational. The writing should read like an experienced researcher explaining a method to a peer, not like a textbook or a blog post.

**Characteristic patterns:**
- Active voice with "we" for the author's contributions: "We propose to learn...", "We extend the concept of...", "We posit that..."
- Active voice with named subjects for others' work: "DistilHuBERT distils the knowledge of HuBERT into..."
- Passive voice only for general facts or when the agent is genuinely irrelevant: "The model is initialised by copying the CNN encoder..."
- Use "e.g." and "i.e." naturally inline: "...general representations, e.g. audio large language models."
- Use semicolons to join closely related independent clauses rather than starting a new sentence: "...adjusting the emphasis between speech and music requires complete retraining; this limits adaptability."

### 10.2 Paragraph architecture

Every paragraph follows the **problem-first** pattern:

1. Open with the gap, limitation, or question that motivates the paragraph.
2. Pivot to the approach, method, or finding that addresses it.
3. Close with the implication or connection to the next paragraph.

**Example (from the author's published work):**
```
An intuitive approach to get a unified speech+music representation would be
to pre-train a single model on both domains. However, pre-training from
scratch is computationally expensive and most times infeasible for academic
research. A more practical alternative is knowledge distillation, where a
smaller model can learn from multiple larger teacher models.
```

The opening sentence names the naive approach (implicitly: the gap is that this approach is expensive). The second sentence states the limitation. The third pivots to the alternative. No filler, no meta-commentary.

### 10.3 Concise motivation sentences

Motivation sentences should be tight and functional. State the desideratum and the reason in one sentence. Do not build up to the point across three sentences.

**Author's natural pattern:**
```
A unified model is desirable for applications that require general
representations, e.g. audio large language models.
```

**Avoid inflated version:**
```
In recent years, there has been growing interest in developing models that
can handle multiple audio domains simultaneously. Such models would be
particularly useful for applications that demand general-purpose
representations. One important example of such applications is audio large
language models.
```

### 10.4 Numbered inline reasoning

When listing advantages, reasons, or factors, use numbered prose items with bold headers rather than bullet points. This is a distinctive structural choice in the author's writing.

**Pattern:**
```
We identify two key advantages of task arithmetic:

1. Computational Efficiency: Unlike ensemble distillation, which requires
training with six prediction heads, task arithmetic involves distilling each
teacher separately. This reduces GPU memory usage during distillation.

2. Flexibility: Task arithmetic allows dynamic adjustment of domain
contributions through interpolation weights. In contrast, ensemble
distillation fixes the balance between domains during pre-training.
```

Each numbered item opens with a bold label, gives one sentence of explanation, then one sentence of contrast or implication. Keep to 2–4 items. If the list exceeds 4, reconsider whether the items are genuinely parallel.

### 10.5 Transitional phrases (preferred set)

The author's natural transitions, used sparingly and only when logically warranted:

| Purpose | Preferred phrases |
|---|---|
| Logical consequence | "Thus,", "Hence," |
| Emphasis on importance | "Crucially,", "Notably," |
| Contrast | "However,", "In contrast,", "While [X], [Y]..." |
| Concession | "Nonetheless,", "While effective, such an approach..." |
| Positing | "We posit that...", "We hypothesise that..." |
| Hedged interpretation | "This suggests that...", "Such results may be justified by..." |
| Pivoting to proposal | "To address this, we...", "A more practical alternative is..." |

**Avoid:** "Furthermore,", "Moreover,", "Additionally,", "Besides,", "It is also worth noting that,", "On the other hand,"

### 10.6 Confidence calibration in prose

The author calibrates hedging to the strength of evidence:

| Evidence level | Phrasing |
|---|---|
| Proven by theorem or formal argument | "X holds", "X follows from" |
| Supported by experimental table | "X achieves / yields / outperforms" (direct claim) |
| Supported by experimental trend | "X suggests that...", "X indicates that..." |
| Plausible interpretation of results | "Such results may be justified by...", "This may be because..." |
| Hypothesis for future work | "We posit that...", "It is plausible that..." |
| Speculative | "One possible direction is...", "It remains to be seen whether..." |

This is finer-grained than the overclaiming prevention table (Section 2.1). Section 2.1 prevents wrong word choices. This table governs sentence-level framing of claims.

### 10.7 What the author's writing does NOT do

To preserve authenticity, avoid these patterns that are NOT part of the author's voice, even if they are common in academic writing:

- **No "firstly / secondly / thirdly"** — use "First, ... Second, ..." or numbered items.
- **No "the remainder of this paper is organised as follows"** — if needed, state it more directly: "Section 2 reviews related work. Section 3 describes the proposed method."
- **No "to the best of our knowledge"** — if the claim needs hedging, hedge the claim itself.
- **No "in this paper, we" at the start of the abstract** — start with the problem or the domain context.
- **No "we believe that"** — use "we posit that" or simply state the claim with appropriate hedging.
- **No "it should be noted that"** or "it is important to mention that" — state the content directly.
- **No "leveraging"** — use "using" or "exploiting" depending on context.
- **No "utilising"** — use "using".
- **No "showcase"** — use "demonstrate" or "show".
- **No "delve into"** — use "examine", "analyse", or "investigate".

---

## 11. Conference Paper vs Thesis Adjustments

Some voice patterns behave differently across formats. When writing, check which format applies.

| Feature | Conference paper | Thesis chapter |
|---|---|---|
| Question-framed experiment sections | Acceptable and effective | Convert to declarative subsection titles |
| Numbered contributions in introduction | One sentence each | Up to four sentences each (problem, idea, advantage, result) |
| "We" usage | Throughout | Throughout, but can mix with passive for variety |
| Abstract length | 150–200 words, no citations | 200–300 words, may include 1–2 key citations |
| Related work depth | One paragraph per theme, 2–4 sentences | One subsection per theme, full treatment |
| Results discussion | Terse: finding + table reference + one-line explanation | Extended: finding + table + analysis + connection to thesis narrative |
| Limitations | 1–2 sentences in conclusion | Dedicated subsection with honest assessment |
