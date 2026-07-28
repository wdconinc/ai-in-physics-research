# Pedagogy Style Guide
## AI in Physics Research – Generative AI & Knowledge Platforms
### Graduate Seminar | 14 Weeks | 2 × 60-Minute Meetings | Max 10 Students

---

## Course Model

This course runs as a **seminar/workshop**. There are no traditional lectures. Every meeting
is built around a student-led introduction (8–10 minutes) followed by a structured active
engagement activity (45–50 minutes). The instructor's role is to facilitate, not to deliver
content. This guide defines the norms that make that model work consistently across all
28 meetings.

---

## 1. Student Introductions

### Purpose

The student introduction sets the conceptual stage for the active engagement that follows.
It is not a mini-lecture and should not attempt comprehensive coverage. Its goals are:
- **Activate prior knowledge** so students arrive at the activity with a shared vocabulary.
- **Surface one or two open questions** that the activity will then pressure-test.
- **Establish the presenting student's ownership** of that meeting's content.

A good introduction ends with the presenter posing one of their guiding questions to the room,
which the instructor immediately pivots into the engagement activity.

### Formats

Choose the format based on content type. All formats are hard-capped at 10 minutes;
the instructor should gently interrupt at the limit.

| Format | Duration | When to Use |
|---|---|---|
| **8-minute chalk talk** | 8 min | Conceptual or mathematical topics where drawing is more expressive than slides (e.g., transformer attention, RAG pipeline diagrams). Student explains from memory at the whiteboard — no notes allowed. |
| **10-minute slide presentation (max 6 slides)** | 10 min | Literature or survey topics where curating key ideas from multiple sources is the skill being exercised. Hard limit of 6 slides enforces selectivity. |
| **10-minute live demo** | 10 min | Tools or code topics where seeing the tool run is more informative than describing it. Student runs a live demonstration in a Jupyter notebook or terminal, narrating as they go. |
| **8-minute paper presentation** | 8 min | Single-paper deep dives. Student presents the paper's method, key result, and one substantive critique. Must name at least one thing the paper does not show. |

### Writing Effective Topic Prompts

A topic prompt is the 3–5 sentence instruction given to the assigned student so they can
prepare independently. An effective prompt includes:

- **A specific concept or tool to cover**, not a broad theme. Write "Explain the
  key-query-value attention mechanism and why it enables parallelism" rather than "talk about
  transformers."
- **Named papers or resources** the student should engage with (title + arXiv ID is
  sufficient). Do not leave the student to discover the literature from scratch.
- **2–3 guiding questions** the presentation must address. These questions drive the
  transition into the active engagement activity.
- **An explicit connection to the week's learning objective**, so the student understands
  why this specific topic matters today.

### Time Budget

- Student introduction: **8–10 minutes**
- Transition and setup: **2–5 minutes**
- Active engagement: **45–50 minutes**

The instructor should keep the introduction to time without apology. Overrunning the intro
compresses the engagement, which is the pedagogically richer portion of the meeting.

---

## 2. Active Engagement Archetypes

### Archetype 1: Live Coding Exercise

**What it is:** The instructor pre-loads a skeleton script or a partially complete Jupyter
notebook into a shared repository. Students extend it in real time using AI tools (Copilot,
Claude API, etc.) to complete a defined task — for example, implementing a RAG query over
arXiv abstracts or building an MCP server endpoint.

**When to use:** Weeks 1–4 (Phase 1, technical baseline). Use when the learning objective
requires students to have hands-on experience with a specific tool or API, not just conceptual
understanding.

**Facilitation:**
- Pre-test the skeleton in the exact environment students will use.
- Set a concrete, checkable goal: "Your notebook should return the top-3 arXiv abstracts
  relevant to a given physics query and print the cosine similarities."
- Circulate; do not solve problems for students — ask "what does the error message say?"
- If students finish early, extend: "Now make it work for multi-hop queries."

**Debrief (5 min):** Each student or pair shares the approach they took. Compare: did
different AI tool prompts lead to different solutions? Which is more readable? Faster?

---

### Archetype 2: Socratic Seminar

**What it is:** The instructor poses a single, genuinely contested question. Students discuss
in structured rounds: first, each student may respond to the question; then, students respond
to each other's responses. No laptops unless the question requires looking something up.

**When to use:** Conceptual or methodological weeks — especially when a clean right answer does
not exist (e.g., "When should a physicist trust an LLM output over a first-principles
calculation?"). Also effective for ethics and evaluation topics.

**Facilitation:**
- Prepare 3 follow-up probes in case discussion stalls: a concrete counterexample, a
  provocation, and a redirection ("What would a skeptical referee say?").
- Name specific students to respond rather than opening to the room; cold-calling is more
  equitable in a 10-person seminar than voluntary turn-taking.
- Keep a live whiteboard list of the key disagreements surfaced.

**Debrief (5 min):** Instructor summarizes the 2–3 key disagreements that were not resolved.
These become optional follow-up prompts for the homework.

---

### Archetype 3: Pair Debugging

**What it is:** Students work in pairs. Each pair receives a pre-written script or notebook
that contains 3–5 planted bugs: some are classical coding errors, but at least two must be
AI-specific failure modes (a hallucinated API call, an off-by-one in a tokenization step,
a physically implausible output that nevertheless passes syntax). Pairs must find and fix all
bugs within 30 minutes and document each fix with a one-sentence explanation.

**When to use:** Weeks involving code reliability — specifically when the learning objective
asks students to identify failure modes in AI-generated code. Also useful after students have
submitted homework that the instructor knows contained common errors.

**Facilitation:**
- Assign pairs by rotating alphabetically so pairing changes each time.
- Bugs should span multiple difficulty levels so pairs do not get stuck or finish too quickly.
- The hallucinated API call bug is typically the last one found; prompt pairs who have found
  all others to "check whether the output is physically plausible."

**Debrief (5 min):** Each pair shares their most interesting bug — the one that required
physical reasoning to detect, not just Python knowledge.

---

### Archetype 4: Structured Debate

**What it is:** Students are divided into two sides (assign randomly or by prior position).
One side defends a claim about AI methodology; the other critiques it. Each side has 5 minutes
to prepare, 5 minutes to present, and 5 minutes to rebut. Examples of productive claims:
"AI-generated literature summaries are reliable enough for a physics methods section" or
"Fine-tuning a domain model is always preferable to prompt engineering for physics tasks."

**When to use:** Ethics, evaluation, and communication weeks. Also effective at Phase 2
transition to force students to commit to a methodological position before designing their
project.

**Facilitation:**
- Assign students to the side opposite their stated view; this forces genuine engagement
  with the strongest version of the opposing argument.
- Time each segment strictly — use a visible timer.
- Instructor should not express a personal view during the debate; save it for the debrief.

**Debrief (5 min):** Identify the strongest argument from each side. Poll the room: did anyone
change their view? What would it take to resolve the question empirically?

---

### Archetype 5: Collaborative Whiteboard

**What it is:** All students collectively build a shared artifact on the whiteboard — a system
architecture diagram, a data-flow map, a taxonomy of AI failure modes, or a concept map
connecting the week's ideas. The instructor starts by writing the central concept and asking
"What connects to this?" Students take turns adding nodes and edges, negotiating with each
other when they disagree.

**When to use:** Design and architecture weeks — especially when students need to synthesize
multiple concepts into a coherent structure (e.g., Week 4 MCP tool architectures, Week 7
knowledge platform integration). Effective as a mid-project checkpoint to externalize mental
models.

**Facilitation:**
- Resist the urge to organize the whiteboard yourself. Let it be messy, then ask students
  to reorganize it.
- Prompt with "What is missing?" and "Does anyone disagree with how this arrow is drawn?"
- For 10 students, ensure everyone makes at least one contribution — call on quiet students
  directly.

**Debrief (2 min):** Photograph the whiteboard and post it to the course repository before the
next class. The diagram often becomes a reference artifact students cite in their papers.

---

### Archetype 6: Peer Code Review

**What it is:** Each student submits their project codebase (or a defined subset) before class.
In class, students review a peer's code using a structured rubric covering reproducibility,
physical plausibility, and documentation. Reviews are written in a GitHub pull request review
format, with line-level comments. A structured rotation ensures each student reviews exactly
one peer and is reviewed by exactly one peer per round.

**When to use:** Weeks 10–12 (Phase 3). Use when students have enough project code to review
meaningfully. Two rounds are scheduled: Week 10 focuses on functionality and correctness;
Week 12 focuses on reproducibility and documentation.

**Facilitation:**
- Distribute the rubric in advance so students know what to look for.
- Require at least 3 line-level comments and 1 summary comment per review.
- Circulate to ensure reviews are substantive, not surface-level.

**Debrief (5 min):** Each reviewer shares one actionable suggestion they gave. This creates a
public record of what the class values in research code.

---

## 3. Variety and Progression

### Phase 1 (Weeks 1–5): Instructor-Guided and Scaffolded

Phase 1 meetings are more structured. The instructor provides the skeleton code, the dataset,
the question. Live coding exercises dominate because students need hands-on experience with
specific tools before they can design their own use of them. Student intros in Phase 1 tend
toward chalk talks and live demos — formats that privilege demonstration over curation.

The mood should feel like a well-run lab practicum: productive, focused, and collaborative,
but clearly guided.

### Phase 2 (Weeks 6–7): Student Ownership Begins

In Phase 2, students have submitted their proposals and are now responsible for the direction
of their own project. Engagement shifts toward collaborative whiteboards (externalizing design
decisions) and structured debates (committing to methodological positions). Intros shift toward
slide presentations and paper presentations as students engage more deeply with literature.

The mood should feel like a research group meeting: students are expected to have opinions and
to defend them.

### Phase 3 (Weeks 8–14): Student-Led, Instructor as Reviewer

Phase 3 meetings are driven by project progress. Peer code review, Socratic seminar, and
structured debate dominate. The instructor's primary role is to ask hard questions, not to
provide answers. Student intros are now paper presentations and live demos of project results.

The mood should feel like a pre-submission lab group meeting: high intellectual standards,
honest critique, and mutual investment in making each other's work better.

### Variety Rules

- **No single engagement format should appear more than 4 times across all 28 meetings.**
- **No single intro format should appear more than 5 times across all 28 meetings.**

These rules are checked by the ConsistencyChecker agent after Phase B generation. If a format
appears too frequently, the ClassWeekAgent output for that meeting should be revised to
substitute a less-used format that is equally appropriate for the content.

---

*This guide is the normative reference for all ClassWeekAgent outputs. When in doubt about
format choice, prefer the format that asks students to produce or defend something over a
format that asks them to consume or observe.*
