# Full Course Plan: Generative AI in Physics Research
## Generative AI & Knowledge Platforms — 14-Week Graduate Seminar

This fourteen-week graduate physics seminar introduces researchers to the practical use of generative AI and knowledge-platform tools in scientific workflows. Meeting twice per week in sessions of 45–55 minutes each, the course is organized into three phases: **Phase 1: The Common Baseline** (Weeks 1–5) builds shared competency in LLM APIs, vibe-coding pitfalls, retrieval-augmented generation, tool-augmented agents, and the proposal process; **Phase 2: Project Ideation & Deep Dives** (Weeks 6–7) shifts focus to constructing and evaluating project-specific MCP servers; and **Phase 3: Project Execution & Polish** (Weeks 8–14) supports students through pipeline implementation, peer review, ethics, scientific writing, and a public departmental showcase. Assessment is weighted as follows: Standard Curriculum Mini-Assignments 20%, Project Proposal & Pitch 15%, Peer Review & Participation 15%, Final Project Codebase & Paper 25%, and Departmental Showcase Presentation 25%. Class enrolment is capped at ten graduate students to preserve the seminar format.

---

## How to Use This Guide

**Week structure.** Each week entry below contains three components. First, two meeting records — each giving the student introduction assignment (format, full topic prompt, and guiding questions), the active-engagement activity (full description, facilitation notes, and materials list), and the estimated duration. Second, a single homework assignment with background context, numbered instructions, a deliverables list, a grading-criteria table, time estimate, due date, and a tools-and-resources list. The three active-engagement archetypes used most frequently are: *live coding exercise* (students implement code in real time with the instructor circulating), *collaborative whiteboard* (students co-construct a diagram or map at the board), and *structured debate* or *Socratic seminar* (argument-driven discussion with structured roles and cold-calling). Facilitation notes are written for the instructor; they describe common failure modes, extension tasks for early finishers, and techniques for equitable participation.

**Student introduction rotation.** Each non-showcase meeting opens with a student introduction: a short prepared presentation in one of six formats (chalk talk, live demo, slide presentation, paper presentation, paper discussion, or mixed). The rotation table below assigns each of the ten enrolled students (labelled S1–S10) to two or three introduction slots spread across the 14 weeks. Formats vary by slot so that each student experiences multiple presentation styles. Week 5 Meeting 2 (the proposal pitch session) and Week 14 Meeting 2 (the departmental showcase) are whole-class events — every student presents and those slots are marked "ALL" in the table. Week 12 Meeting 1 is the only meeting with two simultaneous discussion leaders; both slots are assigned to different students. The instructor should distribute the rotation table to the class at the start of Week 1 so students have sufficient preparation time, especially for Week 11–12 paper discussion leadership slots that require reading and annotating a paper 48 hours in advance.

---

## Student Introduction Rotation Guide

| Week | Meeting | Assigned Student | Format |
|------|---------|-----------------|--------|
| 1  | 1 | S1  | 8-minute chalk talk |
| 1  | 2 | S2  | 10-minute live demo |
| 2  | 1 | S3  | 10-minute live demo |
| 2  | 2 | S4  | 8-minute chalk talk |
| 3  | 1 | S5  | 8-minute chalk talk |
| 3  | 2 | S6  | 10-minute slide presentation (max 6 slides) |
| 4  | 1 | S7  | 10-minute live demo |
| 4  | 2 | S8  | 10-minute slide presentation (max 6 slides) |
| 5  | 1 | S1  | 8-minute paper presentation |
| 5  | 2 | ALL | 5-minute pitch presentation (max 5 slides) per student |
| 6  | 1 | S2  | 10-minute slide presentation (max 6 slides) |
| 6  | 2 | S9  | 10-minute live demo |
| 7  | 1 | S3  | 8-minute paper presentation |
| 7  | 2 | S10 | 10-minute slide presentation (max 6 slides) |
| 8  | 1 | S4  | 10-minute slide presentation (max 6 slides) |
| 8  | 2 | S8  | 10-minute live demo |
| 9  | 1 | S5  | 10-minute live demo |
| 9  | 2 | S9  | 8-minute paper presentation |
| 10 | 1 | S1  | 10-minute slide presentation (max 6 slides) |
| 10 | 2 | S6  | 8-minute chalk talk |
| 11 | 1 | S2  | 15-minute paper discussion (whiteboard outline) |
| 11 | 2 | S7  | 15-minute paper discussion (whiteboard outline) |
| 12 | 1 | S3 & S4 | 15-minute paper discussion (whiteboard outline) each |
| 12 | 2 | S10 | 10-minute live demo |
| 13 | 1 | S5  | 8-minute paper presentation |
| 13 | 2 | S7  | 10-minute slide presentation (3 min demo + 7 min commentary) |
| 14 | 1 | S6  | 8-minute chalk talk |
| 14 | 2 | ALL | 10-minute showcase presentation (≤12 slides) + 5-min Q&A per student |

**Summary by student:**

| Student | Slots | Weeks |
|---------|-------|-------|
| S1  | 3 | 1M1 (chalk talk), 5M1 (paper presentation), 10M1 (slide presentation) |
| S2  | 3 | 1M2 (live demo), 6M1 (slide presentation), 11M1 (paper discussion) |
| S3  | 3 | 2M1 (live demo), 7M1 (paper presentation), 12M1 (paper discussion) |
| S4  | 3 | 2M2 (chalk talk), 8M1 (slide presentation), 12M1 (paper discussion) |
| S5  | 3 | 3M1 (chalk talk), 9M1 (live demo), 13M1 (paper presentation) |
| S6  | 3 | 3M2 (slide presentation), 10M2 (chalk talk), 14M1 (chalk talk) |
| S7  | 3 | 4M1 (live demo), 11M2 (paper discussion), 13M2 (slide presentation) |
| S8  | 2 | 4M2 (slide presentation), 8M2 (live demo) |
| S9  | 2 | 6M2 (live demo), 9M2 (paper presentation) |
| S10 | 2 | 7M2 (slide presentation), 12M2 (live demo) |

---

## Phase 1: The Common Baseline (Weeks 1–5)

Phase 1 establishes the technical and methodological baseline shared by all students before project work diverges. By the end of Week 5, every student will have built a reproducible Python environment, queried LLM APIs programmatically, debugged AI-generated physics code, implemented a RAG pipeline, constructed a minimal MCP server, and submitted a project proposal with a live pitch.

---

### Week 1: GenAI Underpinnings

#### Meeting 1 — How Transformers Work: Attention, Tokens, and Next-Token Prediction

**Student Introduction** (assigned: S1)

> *Format:* 8-minute chalk talk
> 
> **Topic prompt:** Prepare an 8-minute chalk talk explaining the key-query-value attention mechanism at
> the core of transformer models. Focus on why attention enables parallelism across
> sequence positions (unlike RNNs), how multi-head attention allows the model to attend
> to different aspects of the input simultaneously, and what "next-token prediction" as
> a training objective means for a physics researcher who will be querying the model.
> Start from the original "Attention Is All You Need" paper (Vaswani et al., 2017,
> arXiv:1706.03762) and the blog post "The Illustrated Transformer" by Jay Alammar.
> You will draw the attention computation from memory at the whiteboard — no slides or
> notes. Connect your explanation to Learning Objective 1: why does knowing this
> architecture help a physicist decide when to trust or distrust model outputs?
>
> **Guiding questions:**
> 1. Why does next-token prediction make transformers prone to confident-sounding but factually wrong outputs, and what does that imply for using them in physics calculations?
> 2. How does the attention mechanism decide which earlier tokens to weight heavily when generating the next token — and what happens when relevant context is far away in the prompt?
> 3. What architectural property of transformers makes it impossible for them to reliably perform exact symbolic computation, such as solving a differential equation analytically?

**Active Engagement** — Live coding exercise (45 minutes)

The instructor pre-loads a skeleton Jupyter notebook into the course GitHub repository (path: exercises/week01/meeting1_token_explorer.ipynb). Students clone the repository and open the notebook in their local Jupyter environment before class.

Step 1 (5 min): Instructor introduces the notebook. It contains three skeleton cells: (a) a cell that uses the `tiktoken` library to tokenize a physics sentence and print token IDs and decoded tokens side-by-side; (b) a cell stub for a function `count_tokens(prompt: str, model: str) -> int` that students must complete using `tiktoken.encoding_for_model`; (c) a cell that calls the OpenAI chat completions API (`openai>=1.0`) with a short physics prompt and prints the response, but has a bug: the model name is misspelled and the temperature is set to 2.0.

Step 2 (10 min): Students complete cell (b) — implement `count_tokens`. They may use GitHub Copilot or the OpenAI SDK docs. Instructor circulates and asks "What does the function return for an empty string?" to prompt edge-case thinking.

Step 3 (10 min): Students diagnose and fix the two bugs in cell (c). The misspelled model name will raise an `openai.NotFoundError`; temperature > 1.0 will either raise a validation error or produce incoherent output. Students document each fix with a markdown cell explaining what was wrong and why.

Step 4 (10 min): Students run the fixed cell with the prompt: "What is the binding energy per nucleon for iron-56, and why is it the peak of the curve?" They record the model's answer, then look up the known value (8.79 MeV) and note whether the model's number matches. If it hallucinates a value, they note that too.

Step 5 (5 min, debrief): Each student or pair shares: (1) which bug took longer to find and why, (2) whether the model's binding energy answer was numerically correct. Instructor asks: "Does a wrong number in a fluent sentence look different from a right number?" Use this to foreshadow the responsible-use discussion in Meeting 2.

*Facilitation notes:* Common stumbling point: students without API keys set up. Require key setup as pre-class homework (announced in the syllabus). Have a fallback: the `litellm` library can route to a free-tier model (e.g., Groq-hosted llama3) if OpenAI keys are unavailable. Keep the fallback URL in the course README. Early finishers: ask them to extend step 4 by trying two different temperatures (0.0 and 0.7) and comparing outputs for the same physics question. Does lower temperature produce a more physically accurate answer? Why or why not? Debrief approach: do not correct wrong answers immediately — ask the room first. The goal is to surface that numerical plausibility requires external verification, not just reading the model's output.

*Materials needed:* Course GitHub repository with skeleton notebook; OpenAI API keys (or Groq/litellm fallback); Jupyter installed in student environments; tiktoken and openai Python packages

---

#### Meeting 2 — Responsible Use, Attribution, and Setting Up a Reproducible Research Environment

**Student Introduction** (assigned: S2)

> *Format:* 10-minute live demo
> 
> **Topic prompt:** Prepare a 10-minute live demo showing how a reproducible Python research environment
> is constructed from scratch. In your Jupyter notebook (or terminal), walk through:
> (1) creating a conda environment with a pinned Python version; (2) installing
> `openai`, `anthropic`, `litellm`, `numpy`, `matplotlib`, and `jupyter`; (3) exporting
> an `environment.yml`; (4) loading an API key from a `.env` file using `python-dotenv`
> so the key never appears in the notebook; and (5) committing the environment file to
> a GitHub repository while confirming that `.env` is in `.gitignore`. Reference the
> OpenAI Python SDK quickstart (https://platform.openai.com/docs/quickstart) and
> the Anthropic Python SDK docs (https://docs.anthropic.com/en/api/getting-started).
> Connect to Learning Objective 3: a reproducible environment is a prerequisite for
> any AI-assisted finding to be trusted or replicated by a collaborator.
>
> **Guiding questions:**
> 1. What is the minimal set of steps a collaborator needs to follow to reproduce your AI-assisted experiment from a fresh machine — and which step is most commonly forgotten?
> 2. Why is loading an API key from an environment variable (rather than hardcoding it) both a security practice and a reproducibility practice?
> 3. If you use an AI to generate code, what do you need to document so that your published paper's methods section is accurate and complete?

**Active Engagement** — Socratic seminar (45 minutes)

The instructor poses a single contested question written on the whiteboard before students arrive: "An AI model drafted 40% of the methods code in a published physics paper. The paper does not mention this. Is that a problem, and if so, for whom?"

Step 1 (3 min): Students read two short excerpts (pre-printed, one page total): (a) the APS guidelines on AI-assisted writing (2023); (b) one paragraph from a retracted preprint where an LLM hallucinated a citation. No laptops during this step.

Step 2 (10 min, first round): Instructor calls on each student in turn (not volunteers) to give a one-sentence answer to the central question. Students may not repeat what a previous speaker said — they must add something new or explicitly refine a prior point. Instructor writes key claims on the whiteboard as students speak.

Step 3 (15 min, second round): Instructor poses three follow-up probes in sequence, pausing for 3–4 minutes of open discussion after each: Probe A (counterexample): "Suppose the AI-generated code is provably correct and the physical results are validated. Does the omission still matter?" Probe B (provocation): "A first-author PhD student and their advisor disagree on whether to disclose. What does each stand to lose by disclosing vs. not disclosing?" Probe C (redirection): "What would a skeptical referee specifically need to know about the AI's role to evaluate the paper's reproducibility?"

Step 4 (12 min): Students individually write three bullet points (in their notebook or on paper): (1) a specific disclosure practice they will adopt for their own work this semester; (2) one situation where AI use in physics research is clearly appropriate; (3) one situation where it is clearly inappropriate. Pairs share and compare their lists.

Step 5 (5 min, debrief): Instructor summarizes the 2–3 key disagreements that were not resolved. These are written on the whiteboard and photographed. Instructor explicitly connects unresolved disagreements to the homework: "Your mini-assignment asks you to document your AI use — these disagreements are why that documentation matters."

*Facilitation notes:* This seminar works only if the instructor does not express a personal view on the central question until the very end of the debrief — and even then, frame it as "my current working position, open to revision." Students in STEM often want the instructor to give the right answer; resist this. Cold-calling in step 2 is essential for equity: in a 10-person seminar, voluntary participation concentrates in 3–4 students. Name each student directly: "Alex, what is your one-sentence answer?" If discussion stalls after Probe A, use: "If reproducibility only requires that the code runs, what is the peer reviewer actually checking?" This usually restarts disagreement. For step 4, circulate and read over students' shoulders to identify interesting disagreements between pairs before the debrief. Seed the debrief by naming a specific pair disagreement: "Priya said X and Jordan said Y — let's hear both."

*Materials needed:* Pre-printed one-page excerpt packet (APS AI guidelines excerpt + retracted preprint paragraph); whiteboard and markers; printed or projected central question; student notebooks or paper for step 4

---

#### Homework Assignment 1: First Contact: Querying an LLM API with a Physics Question

**Assessment category:** Standard Curriculum Mini-Assignments | **Estimated time:** 3–4 hours | **Due:** Before the first class meeting of Week 2

**Background:** Before AI-assisted methods can contribute to physics research, a researcher must be able to set up a controlled, reproducible environment, query a model programmatically, and critically evaluate the output against known physical results. This assignment establishes that baseline: you will build the minimal infrastructure needed for all subsequent work in this course and confront, for the first time, the practical problem of detecting hallucinations in a domain where you have independent knowledge. The environment you create here — version-controlled, with secrets managed properly, and dependencies pinned — will serve as the foundation for every assignment that follows.

**Instructions:**
1. Create a new GitHub repository named `ai-physics-<lastname>` (public or private with the instructor added as collaborator). Initialize it with a README.md. Clone the repository locally. Create a `.gitignore` that includes `.env`, `__pycache__/`, and `*.pyc`. Commit and push.
2. Set up a reproducible Python environment: run `conda create -n ai-physics python=3.11`, activate it, then install `openai>=1.0`, `anthropic`, `litellm`, `numpy`, `matplotlib`, `jupyter`, and `python-dotenv`. Export the environment with `conda env export > environment.yml` and commit it. Alternatively, use `pip` and produce a `requirements.txt` via `pip freeze > requirements.txt`. Your choice of tool must be documented in the README.
3. Create a `.env` file (not committed) containing your API key as `OPENAI_API_KEY=sk-...` (or `ANTHROPIC_API_KEY` if using the Anthropic SDK, or a `GROQ_API_KEY` if using litellm with Groq as a free-tier fallback). In your notebook, load it with `from dotenv import load_dotenv; load_dotenv()` and access the key via `os.environ`. Never hardcode the key in the notebook.
4. Create a Jupyter notebook named `week01_<lastname>.ipynb`. In the notebook, write a Python function `query_llm(prompt: str, model: str = 'gpt-4o-mini') -> str` that sends a prompt to the LLM API using the OpenAI Python SDK (or Anthropic SDK / litellm) and returns the response text. Document the function with a docstring. Then query the model with at least three physics prompts of your choice — each should have a known answer you can verify independently. For each response: (a) record the model's answer verbatim; (b) look up the accepted value from a textbook or the PDG/NIST database; (c) compute or state the discrepancy; (d) classify the response as correct, approximately correct, or hallucinated, with one sentence of justification. Identify and clearly label at least one hallucination or significant limitation in the model's responses.

**Deliverables:**
- A Jupyter notebook named `week01_<lastname>.ipynb` containing: the `query_llm` function with a docstring, at least three physics queries with model responses, a quantitative or qualitative comparison of each response to the known answer, and an explicit identification and discussion of at least one hallucination or hard limit.
- A `requirements.txt` or `environment.yml` file that fully specifies the Python environment, including pinned versions, so that the notebook can be run from a fresh install.
- A `README.md` with: a one-paragraph description of what the notebook does, step-by-step instructions for reproducing the results from scratch (including how to create the `.env` file without revealing the key), and a one-paragraph reflection on what you learned about LLM reliability in a physics context.
- A `.gitignore` that excludes `.env` and Python cache files. Confirm (in the README) that no API keys appear anywhere in the committed repository.

**Grading criteria:**

| Criterion | Weight | Excellent looks like |
|-----------|--------|---------------------|
| Methodology correctness | 30% | The `query_llm` function uses the OpenAI SDK (or an approved alternative) correctly — correct endpoint, valid model name, API key loaded from environment. The three physics prompts are substantive questions with known answers. The comparison methodology is sound: accepted values are sourced from PDG, NIST, or textbook and stated explicitly. |
| Reproducibility | 25% | Any graduate student can re-run the notebook from scratch following only the README instructions: environment file is present and complete, API key is loaded from a `.env` file (not hardcoded), cells run top-to-bottom without error, and the `.gitignore` prevents accidental key commits. |
| Physical plausibility | 25% | At least one hallucination or hard limit is identified and discussed with physical reasoning — not just "the model got it wrong" but an explanation of what the correct value is, why the model's answer is wrong, and what this suggests about when to trust LLM outputs for similar questions. At least one correct response is also validated against a known source. |
| Code clarity | 20% | The notebook reads as a coherent document: the `query_llm` function has a docstring, each major notebook section has a markdown cell explaining its purpose, variable names are descriptive, and the comparison between model output and known answer is clearly laid out. |

**Tools and resources:**
- OpenAI Python SDK: `pip install openai>=1.0`; quickstart at https://platform.openai.com/docs/quickstart
- Anthropic Python SDK (alternative): `pip install anthropic`; docs at https://docs.anthropic.com/en/api/getting-started
- litellm (free-tier fallback via Groq): `pip install litellm`; supports OpenAI-compatible interface with Groq-hosted models at no cost
- python-dotenv for secret management: `pip install python-dotenv`; load with `load_dotenv()` before `os.environ` calls
- tiktoken for token counting: `pip install tiktoken`
- PDG Particle Data Group (known values): https://pdg.lbl.gov
- NIST Physical Reference Data (constants, atomic data): https://physics.nist.gov/PhysRefData
- Course GitHub repository with skeleton notebook: exercises/week01/
- APS guidelines on AI-assisted writing (2023): https://www.aps.org/policy/statements

---

### Week 2: Vibe-Coding & Pitfalls

#### Meeting 1 — How AI Coding Assistants Generate Code — and Why They Fail

**Student Introduction** (assigned: S3)

> *Format:* 10-minute live demo
> 
> **Topic prompt:** Research and demonstrate how large language model-based coding assistants — specifically GitHub Copilot and Claude (claude-3-5-sonnet-20241022) — generate code from natural language prompts. Focus on the internal mechanics that lead to failure: why does an LLM confidently hallucinate a non-existent NumPy or SciPy function, and what statistical properties of training data cause plausible-but-wrong physics outputs? Use the blog post "Copilot Internals" (GitHub Next, 2023) and Poldrack et al. "AI-assisted coding: Experiments with GPT-4" (arXiv:2304.13187) as primary sources. Your presentation must make the connection between how these tools are trained and the specific failure modes students will encounter in today's debugging exercise.
>
> **Guiding questions:**
> 1. What prompt structures (specification-first vs. open-ended) most reliably produce syntactically correct but physically wrong code, and why?
> 2. When an AI assistant hallucinates a scipy.integrate function signature, what about its training distribution explains that specific error?
> 3. How would you distinguish a hallucinated API call from a genuine API change between library versions if you could not run the code?

**Active Engagement** — Pair debugging (45 minutes)

Before class: the instructor prepares a Python script named `week02_buggy_harmonic_oscillator.py` (committed to the course repository) that was ostensibly generated by Claude to compute the first five energy levels of a quantum harmonic oscillator and plot the corresponding wavefunctions. The script contains exactly five planted bugs spanning three difficulty tiers:

- **Bug 1 (easy — syntax/logic):** The loop computing energy levels uses `E_n = hbar * omega * n` instead of `E_n = hbar * omega * (n + 0.5)`, omitting the zero-point energy term.
- **Bug 2 (easy — off-by-one):** The wavefunction array is indexed as `psi[1:N]` instead of `psi[0:N]`, causing the ground state wavefunction to be silently dropped from the plot.
- **Bug 3 (medium — hallucinated API):** The script calls `scipy.special.hermite_poly(n, x)`, which does not exist; the correct call is `scipy.special.hermite(n)(x)` (using the polynomial object returned by `scipy.special.hermite`).
- **Bug 4 (medium — wrong normalization):** The Hermite–Gaussian wavefunction is normalized by dividing by `np.sqrt(n!)` instead of `np.sqrt(2**n * math.factorial(n) * np.sqrt(np.pi))`, producing amplitudes that are not unit-normalized.
- **Bug 5 (hard — plausible-but-wrong physics):** The script plots probability density as `psi` instead of `np.abs(psi)**2`, so the y-axis shows the (signed) wavefunction rather than the probability density, which looks visually plausible but is physically incorrect.

Step 1 (2 min): Instructor assigns pairs alphabetically by last name (five pairs for ten students). Each pair clones the repository and opens `week02_buggy_harmonic_oscillator.py`.

Step 2 (3 min): Pairs run the script as-is and record every error message or unexpected output in a shared comment block at the top of the file.

Step 3 (25 min): Pairs work to identify and fix all five bugs. For each bug found, they add a comment: `# BUG [number]: [one sentence describing what the AI got wrong]` and `# FIX: [one sentence describing the correct approach]`. Pairs must not use AI tools during this phase.

Step 4 (5 min): Pairs verify their fixed script against two sanity checks: (a) the ground state energy printed to stdout must equal 0.5 * hbar * omega (with hbar=omega=1), and (b) the probability densities integrated over x must each equal 1.0 to within 1%.

Step 5 (10 min): Class debrief — each pair shares the bug they found last (typically Bug 5). Instructor asks: "Which of these bugs would pytest catch automatically, and which require physical reasoning?"

*Facilitation notes:* Prepare the buggy script in advance and test that it runs without crashing on Bugs 1–4 (only Bug 3 raises an AttributeError; the others produce wrong results silently). This is intentional — students must check physical plausibility, not just error messages. If a pair finds all five bugs in fewer than 20 minutes, extend: ask them to write a pytest test suite with at least three assertions that would have caught bugs 1, 4, and 5 automatically. For pairs stuck on Bug 3: prompt them to run `help(scipy.special)` or check the SciPy docs page for `hermite` — do not tell them the correct call. For pairs stuck on Bug 5: ask "Does this quantity have to be non-negative everywhere? Why?" This usually surfaces the sign issue within two minutes. Keep a running tally on the whiteboard of which bugs each pair has found, so the room can see whether Bug 5 is consistently the last to be identified.

*Materials needed:* `week02_buggy_harmonic_oscillator.py` committed to the course GitHub repository; Python environment with numpy, scipy, matplotlib, and math pre-installed; whiteboard for tracking pair progress; printed or projected SciPy documentation for scipy.special.hermite

---

#### Meeting 2 — Test-Driven Prompting — Making AI Code Reliable

**Student Introduction** (assigned: S4)

> *Format:* 8-minute chalk talk
> 
> **Topic prompt:** Research and present the "specification-first" and "test-driven" prompting strategies for AI code generation, as described in Chen et al. "Evaluating Large Language Models Trained on Code" (arXiv:2107.03374, the HumanEval paper) and the iterative refinement workflow documented in Peng et al. "Is Your Code Generated by ChatGPT Really Correct?" (arXiv:2305.01210). Focus specifically on how writing a pytest test suite before prompting the AI changes the quality of generated code compared to open-ended prompting. Your presentation must end with a live demonstration: show the class one example where a zero-shot prompt produces wrong code and a test-driven prompt produces correct code for the same physics task (suggested: computing the period of a simple pendulum as a function of amplitude using numerical integration).
>
> **Guiding questions:**
> 1. Why does providing an AI assistant with a failing test case before asking it to write code improve reliability, compared to describing the desired behavior in prose?
> 2. What kinds of physics errors can pytest reliably catch, and what kinds require a human physicist to verify?
> 3. In an iterative refinement workflow, how do you decide when to stop prompting and accept the AI's output?

**Active Engagement** — Live coding exercise (45 minutes)

Before class: the instructor commits a skeleton Jupyter notebook named `week02_test_driven_skeleton.ipynb` to the course repository. The notebook contains: a problem statement (implement a projectile motion simulator in Python that computes range, maximum height, and time of flight for a given launch angle and initial speed, accounting for air resistance using a linear drag model F_drag = -b*v), and a pre-written pytest test suite (five tests): `test_vacuum_range` (verifies R = v0² sin(2θ)/g), `test_vacuum_max_height` (verifies H_max = v0² sin²θ/(2g) for zero drag), `test_drag_reduces_range` (verifies any positive drag coefficient reduces range), `test_time_of_flight_positive` (verifies TOF is always positive and finite), and `test_symmetry_broken_by_drag` (verifies optimal launch angle is strictly less than 45 degrees with drag).

Step 1 (3 min): Instructor explains the workflow: students will write a prompt for Claude or GitHub Copilot that includes the test suite and asks the AI to generate code that passes all five tests.

Step 2 (15 min): Each student individually prompts Claude (claude-3-5-sonnet-20241022 via the web interface) or GitHub Copilot using a test-driven prompt of their own design. They paste the AI output into the "AI-Generated Code" cell and run pytest.

Step 3 (10 min): Students who have passing tests help those who do not by comparing prompt strategies — not by sharing code. Instructor circulates and asks each student: "What did you include in your prompt that you think made the difference?"

Step 4 (10 min): Each student runs one iteration of refinement: take the failing test output, include it verbatim in a follow-up prompt, and ask the AI to fix its own code. Document whether the AI identifies the physical root cause or only addresses the Python error.

Step 5 (7 min): Whole-class debrief. Instructor collects on the whiteboard: (a) how many students passed all 5 tests on the first attempt, (b) which test was hardest to get the AI to pass, and (c) one example where the AI "fixed" a failing test by weakening the assertion rather than fixing the physics.

*Facilitation notes:* Pre-run the skeleton notebook and confirm pytest is importable and that the five tests fail on an empty implementation (returning zeros). Expect most first-attempt AI outputs to pass tests 1–4 but fail `test_symmetry_broken_by_drag`, because this test requires the AI to implement a numerical optimization loop. Use this as a teaching moment about specification completeness. If students find that the AI passes all tests with a trivial solution (e.g., hardcoding the expected output), point out that their test suite is underspecified. Reserve 2 minutes at the end to explicitly connect today's activity to Mini-Assignment 2.

*Materials needed:* `week02_test_driven_skeleton.ipynb` committed to the course GitHub repository; Python environment with numpy, scipy, and pytest pre-installed; student access to Claude (claude-3-5-sonnet-20241022) via web interface or GitHub Copilot via IDE; projector to display prompt comparison during debrief

---

#### Homework Assignment 2: Bug Hunt and Test-Driven Repair of an AI-Generated Physics Script

**Assessment category:** Standard Curriculum Mini-Assignments | **Estimated time:** 3–5 hours | **Due:** Before the first class meeting of Week 3

**Background:** AI coding assistants frequently generate code that is syntactically valid, runs without crashing, and produces output that looks physically reasonable — yet contains subtle errors that only careful physical reasoning can detect. This assignment trains you to be a critical consumer of AI-generated physics code by systematically finding, documenting, and repairing bugs in a script that was generated by Claude (claude-3-5-sonnet-20241022) with minimal prompting. You will then apply the test-driven prompting strategy practiced in class to produce a corrected, well-tested replacement.

**Instructions:**
1. Clone the course repository and open `week02_starter/ai_generated_oscillator.py`. This script was produced by Claude with the prompt "Write a Python script that computes and plots the first five energy levels and wavefunctions of the quantum harmonic oscillator using numpy and scipy." Run the script using Python 3.10+ and record every error message and every output value. Do not fix anything yet — just observe. Write your observations in a markdown file named `week02_<lastname>_bugreport.md`.
2. Identify all bugs in `ai_generated_oscillator.py`. There are exactly five. For each bug, add an entry to `week02_<lastname>_bugreport.md` with the following fields: (a) Bug number and location (file and line number); (b) Category — choose one of: hallucinated API, off-by-one error, wrong physics formula, incorrect normalization, or wrong output quantity; (c) What the AI produced and why it is wrong — explain in one to two sentences using physical reasoning, not just "it crashes"; (d) The correct code and a citation (equation number from Griffiths "Introduction to Quantum Mechanics" or equivalent) supporting your fix.
3. Write a pytest test suite in `week02_<lastname>.ipynb` containing at least five tests that collectively would have caught all five bugs if they had existed before the AI generated the code. Each test must include a docstring explaining what physical property it checks and why. Run your tests against the original buggy script to confirm they fail, then run them against your fixed version to confirm they pass. Include the pytest output for both runs in your notebook.
4. Use a test-driven prompting strategy to ask Claude (claude-3-5-sonnet-20241022) or GitHub Copilot to regenerate the quantum harmonic oscillator script from scratch, this time including your test suite in the prompt. Paste your full prompt into a markdown cell in `week02_<lastname>.ipynb`, then paste the AI's output into the next code cell and run your test suite against it. If any tests still fail, perform one round of iterative refinement: paste the failing test output back into Claude and ask it to correct its code. Document whether the AI's correction addresses the physical root cause or only the Python error. Include a one-paragraph reflection on what this exercise reveals about the reliability of AI-assisted physics coding.

**Deliverables:**
- A Jupyter notebook named `week02_<lastname>.ipynb` containing: your five-test pytest suite with docstrings; the pytest output for the buggy script (showing failures) and for the fixed script (showing all passing); your test-driven AI prompt and the AI-generated corrected code; and the one-paragraph reflection on AI reliability.
- A markdown file named `week02_<lastname>_bugreport.md` containing the structured bug report for all five bugs (number, location, category, explanation, correct code with citation).
- A `requirements.txt` or `environment.yml` listing all Python package versions used (numpy, scipy, matplotlib, pytest, and any others), with a `README.md` containing one paragraph of instructions for reproducing your results from a fresh clone.

**Grading criteria:**

| Criterion | Weight | Excellent looks like |
|-----------|--------|---------------------|
| Methodology correctness | 30% | All five bugs correctly identified with accurate category labels and physically grounded explanations; test-driven prompting strategy applied as specified; corrected script produces physically correct energy levels (E_n = hbar*omega*(n+0.5)) and unit-normalized probability densities. |
| Reproducibility | 25% | Any graduate student can re-run the notebook and all tests from a fresh clone using only the provided requirements.txt and README instructions; random seeds set where applicable; no hardcoded absolute paths; API keys loaded from environment variables. |
| Physical plausibility | 25% | The bug report explains each error in terms of physical consequences; at least two tests check explicitly physical properties (e.g., non-negativity of probability density, correct zero-point energy, unit normalization); the reflection connects AI failure modes to physical reasoning requirements. |
| Code clarity | 20% | The notebook reads as a coherent document; each pytest test has a docstring stating the physical property being checked; the bug report is clearly structured; the AI prompt is reproduced verbatim and annotated with a sentence explaining the prompting strategy used. |

**Tools and resources:**
- Claude (claude-3-5-sonnet-20241022) via https://claude.ai — free tier is sufficient
- GitHub Copilot — available via student GitHub Education Pack or course license
- pytest — install via `pip install pytest` or include in environment.yml
- pytest-nbmake — optional, allows running pytest directly on Jupyter notebooks
- NumPy (numpy >= 1.24), SciPy (scipy >= 1.10), Matplotlib (matplotlib >= 3.7)
- Griffiths, D.J. "Introduction to Quantum Mechanics" (3rd ed.) — Chapter 2 (sections 2.3–2.4) for the harmonic oscillator energy levels and wavefunctions
- Course repository: `week02_starter/` directory contains `ai_generated_oscillator.py`
- arXiv:2304.13187 (Poldrack et al.) for background on AI coding failure modes

---

### Week 3: RAG & Knowledge Platforms

#### Meeting 1 — Embeddings, Vector Stores, and the RAG Pipeline

**Student Introduction** (assigned: S5)

> *Format:* 8-minute chalk talk
> 
> **Topic prompt:** Explain the end-to-end architecture of a retrieval-augmented generation (RAG) pipeline, focusing on how text is converted to dense vector embeddings, stored in a vector database, and retrieved via approximate nearest-neighbor search. Cover cosine similarity as the retrieval metric, common chunking strategies (fixed-size vs. sentence-boundary), and how FAISS or ChromaDB implement the index. Draw the full pipeline from a physics query string to a grounded LLM answer. Engage with the foundational paper "FAISS: A Library for Efficient Similarity Search" (Johnson et al., arXiv:1702.08734) and the sentence-transformers library documentation for all-MiniLM-L6-v2. Your presentation must connect directly to this week's objective: implementing a RAG pipeline over arXiv physics abstracts.
>
> **Guiding questions:**
> 1. Why does cosine similarity work better than Euclidean distance for comparing sentence embeddings, and what geometrical property of normalized vectors makes this so?
> 2. If your physics paper corpus has abstracts of very different lengths, what chunking strategy would you choose and why might uniform chunking hurt retrieval precision?
> 3. At what point in the RAG pipeline does the LLM first see text from the retrieved documents, and what would happen if retrieval fails silently?

**Active Engagement** — Live coding exercise (45 minutes)

Students build a minimal RAG pipeline over a small corpus of arXiv abstracts in real time.

Step 1 (5 min): Instructor shares a skeleton Jupyter notebook pre-loaded in the course repository. The notebook has cells for imports (arxiv, sentence_transformers, faiss-cpu, openai or anthropic) and empty function stubs: `fetch_abstracts()`, `embed_texts()`, `build_index()`, `retrieve()`, and `answer_with_rag()`. Students clone the repo or open it in their cloud environment.

Step 2 (10 min): Students complete `fetch_abstracts()` using the arxiv Python library to pull 30 abstracts for a query relevant to their subfield (e.g., "dark matter direct detection" or "quantum error correction surface codes"). They print the first abstract to verify the fetch works.

Step 3 (10 min): Students complete `embed_texts()` using `SentenceTransformer('all-MiniLM-L6-v2')` to produce a (30, 384) NumPy array of embeddings. They check the shape and verify that two thematically similar abstracts have cosine similarity > 0.7.

Step 4 (10 min): Students build a flat FAISS index (`faiss.IndexFlatIP` after L2-normalizing embeddings), add the embeddings, and complete `retrieve()` to return the top-3 abstracts for a given query string. They print the titles and cosine similarities for one test query.

Step 5 (5 min): Students wire `retrieve()` into `answer_with_rag()`: the retrieved abstract text is prepended as context in the LLM system prompt. They run one physics question with and without RAG and observe whether the grounded answer cites a real paper.

Debrief (5 min): Each student or pair shares one result — did RAG change the answer? Was the retrieved abstract actually relevant? Instructor collects observations on the whiteboard.

*Facilitation notes:* Pre-test the skeleton notebook in the exact Python environment students will use; confirm that `pip install arxiv sentence-transformers faiss-cpu` works without conflicts. Have a fallback set of 30 pre-fetched abstracts as a JSON file in the repo in case the arXiv API is slow or rate-limited during class. If students finish Steps 1-4 early, extend: "Now query with a deliberately vague question like 'what is energy?' and note which abstracts come back — is the retrieval still sensible?" For students whose subfield queries return fewer than 30 results, suggest broadening the arXiv category filter. Do not debug for students — ask "what does the shape of your embedding matrix print out?" to guide them to the source of shape mismatches.

*Materials needed:* Course GitHub repository with skeleton notebook `week03_rag_skeleton.ipynb`; pre-fetched fallback corpus `week03_fallback_corpus.json`; Python environment with arxiv, sentence-transformers, faiss-cpu, and either openai or anthropic installed; projector for instructor to display one working solution during debrief

---

#### Meeting 2 — Evaluating Retrieval Quality for Scientific Queries

**Student Introduction** (assigned: S6)

> *Format:* 10-minute slide presentation (max 6 slides)
> 
> **Topic prompt:** Present the standard information-retrieval metrics — precision@k, recall@k, and Mean Reciprocal Rank (MRR) — and explain why they must be adapted for scientific queries where relevance is not binary. Specifically, discuss how TREC-style relevance judgments work and why a physics abstract may be "partially relevant" to a query. Reference the BEIR benchmark paper (Thakur et al., 2021, arXiv:2104.08663), which evaluates retrieval models on domain-specific corpora including scientific text, and note which embedding models perform best on biomedical and scientific subsets. Connect this to today's objective: measuring whether your Week 3 RAG pipeline retrieves the right abstracts for known physics questions, and identifying the failure modes — keyword mismatch, concept drift, and embedding space collapse — that degrade scientific retrieval.
>
> **Guiding questions:**
> 1. If your RAG pipeline returns the top-3 abstracts for a question about "Cooper pair condensation" but none of them use that exact phrase, how would you decide whether the retrieval succeeded or failed?
> 2. The BEIR benchmark shows that BM25 (a sparse keyword method) outperforms dense embeddings on some scientific datasets. What property of physics literature might explain this counter-intuitive result?
> 3. When would high precision@3 but low recall be acceptable for a physics research assistant, and when would it be dangerous?

**Active Engagement** — Socratic seminar (45 minutes)

The seminar addresses the question: "Is retrieval-augmented generation reliable enough to trust as a literature source in a physics methods section?"

Step 1 (3 min): Instructor writes the central question on the whiteboard. Students spend 2 minutes writing a one-sentence position statement (yes/no/it depends, with a one-line justification) on a notecard — these are collected and read aloud anonymously to reveal the distribution of initial views without anchoring discussion.

Step 2 (15 min) — First round: Instructor cold-calls each student once to give their initial response to the question. Students may not repeat a point already made; they must either extend, qualify, or counter what has been said. Instructor tracks key claims on the whiteboard without editorializing.

Step 3 (15 min) — Second round (peer responses): Students now respond directly to each other's claims, not to the instructor. Instructor intervenes only with probes: (a) "Can you give a concrete physics example where that claim would break down?" (b) "What would a skeptical referee say about using RAG-retrieved citations in a paper?" (c) "If you had to specify a retrieval precision threshold before trusting an RAG answer, what number would you choose and why?"

Step 4 (7 min) — Evidence round: Students are now allowed to open laptops and pull up one piece of evidence (from their Week 3 notebook results, the BEIR paper, or the arXiv API documentation) that supports or refutes the most contested claim on the whiteboard. Each student who found evidence has 60 seconds to present it.

Debrief (5 min): Instructor summarizes the 2–3 core disagreements that were not resolved.

*Facilitation notes:* Prepare three follow-up probes in case discussion stalls: (1) "Name a physics question where you are confident RAG would retrieve the right abstract every time — what makes that query easy?" (2) "Name a physics question where you are confident RAG would fail — what makes it hard?" (3) "If the LLM answer is correct but the retrieved abstracts are wrong, is that a success or a failure of RAG?" Cold-call students in an order that pairs confident and quiet students alternately. The anonymous notecard step is important: it prevents anchoring. Do not express a personal view during the seminar.

*Materials needed:* Whiteboard and markers; one notecard per student for anonymous position statements; student laptops with Week 3 RAG notebooks accessible; printed or digital copy of BEIR benchmark paper (arXiv:2104.08663) for the evidence round

---

#### Homework Assignment 3: Building and Evaluating a RAG Pipeline over Physics Abstracts

**Assessment category:** Standard Curriculum Mini-Assignments | **Estimated time:** 4–5 hours | **Due:** Before the first class meeting of Week 4

**Background:** Retrieval-augmented generation (RAG) grounds LLM answers in a retrieved document corpus, reducing hallucination and making claims traceable to specific sources. For physics research, this means an LLM can in principle cite real papers rather than fabricate citations. However, retrieval quality depends heavily on the embedding model, the chunking strategy, and the specificity of the physics query — failures are common and often silent. In this assignment you build a minimal but complete RAG pipeline over a set of arXiv abstracts from your subfield, measure its retrieval precision on questions with known correct sources, and compare LLM answer quality with and without RAG context.

**Instructions:**
1. **Fetch abstracts:** Use the arxiv Python library to retrieve between 30 and 50 abstracts for a physics query relevant to your research subfield. Store each abstract as a dictionary with keys: id, title, authors, abstract, url. Save the corpus to a JSON file named `corpus.json` so it can be reloaded without re-fetching. Print the number of results retrieved and the title of the first abstract to confirm the fetch succeeded.
2. **Embed and index:** Embed each abstract text using `SentenceTransformer('all-MiniLM-L6-v2')`. L2-normalize the resulting embedding matrix, then build a `faiss.IndexFlatIP` index and add all embeddings. Save the index to disk as `corpus.faiss` using `faiss.write_index()`. Report the embedding matrix shape and confirm that the cosine similarity between two abstracts you judge to be thematically related is greater than 0.6. Set `numpy.random.seed(42)` before any stochastic operations.
3. **Design your evaluation set:** Write exactly 5 physics questions whose correct answers can be verified from the retrieved corpus. For at least 3 of these questions, identify in advance which specific abstract(s) from your corpus contain the answer (record the arXiv ID). These are your "gold" retrievals. Store the questions and gold IDs in a structured list in your notebook.
4. **Query and evaluate retrieval:** For each of the 5 questions, embed the question, query the FAISS index for the top-3 abstracts, and record the retrieved arXiv IDs and cosine similarity scores. For the 3 questions with gold IDs, compute precision@3 (fraction of the top-3 retrievals that match a gold ID). For all 5 questions, write a one-sentence qualitative judgment of whether the retrieval was relevant. Report the mean precision@3 across the 3 gold questions.
5. **Compare RAG vs. no-RAG answers:** For each of the 5 questions, call an LLM twice: once with no additional context (baseline), and once with the top-3 retrieved abstract texts prepended to the system prompt as context (RAG). Record both answers. For the 3 gold questions, judge each answer pair as "RAG better", "Baseline better", or "Equivalent", and write a one-sentence justification. Write a Markdown cell of 100–150 words identifying at least two specific conditions under which RAG improved the LLM's accuracy and at least one condition where it made no difference or degraded the answer, citing the specific question text and retrieved abstract IDs as evidence. [EDIT: vague "Discuss in a Markdown cell" replaced with specific word-count, structure, and evidence requirements] Load your API key from a `.env` file using python-dotenv — do not hardcode it.

**Deliverables:**
- A Jupyter notebook named `week03_<lastname>.ipynb` containing all five steps above, with Markdown cells explaining each step and a final summary cell discussing retrieval quality and RAG improvement for your subfield query.
- A `corpus.json` file containing the fetched abstracts (committed to the repository or included in the zip submission).
- A `requirements.txt` or `environment.yml` listing all dependencies with pinned versions, and a `README.md` with a single paragraph explaining how to reproduce the results from a fresh clone (including how to supply the API key via a `.env` file).
- A `.env.example` file (not `.env`) showing the required environment variable names with placeholder values (e.g., `OPENAI_API_KEY=your-key-here`).

**Grading criteria:**

| Criterion | Weight | Excellent looks like |
|-----------|--------|---------------------|
| Methodology correctness | 30% | RAG pipeline follows the correct sequence: fetch → embed → index → retrieve → generate. FAISS index built from L2-normalized embeddings using IndexFlatIP. Precision@3 computed correctly for the gold questions. LLM calls use retrieved context in the system prompt for RAG condition and no retrieval context for baseline. API key loaded from environment variables, not hardcoded. |
| Reproducibility | 25% | Any graduate student can re-run the notebook from scratch using only the README instructions: corpus.json is present so no re-fetching is required, FAISS index rebuilt deterministically, random seed set, all dependencies listed with pinned versions, API key loaded from .env file documented in .env.example. |
| Physical plausibility | 25% | Student explicitly checks that retrieved abstracts are physically relevant to the posed questions — not just lexically similar. For at least 2 of the 5 questions, the student compares the RAG-grounded LLM answer against a known result and notes whether the LLM answer is consistent. The discussion cell identifies at least one failure mode. |
| Code clarity | 20% | The notebook reads as a coherent scientific document: each of the five steps introduced with a Markdown cell stating its purpose, functions named descriptively, code cells have a single clear purpose, and the final summary cell synthesizes the precision@3 results and RAG vs. baseline comparison in plain prose. |

**Tools and resources:**
- arxiv (Python library): https://pypi.org/project/arxiv/ — for fetching abstracts
- sentence-transformers (PyPI): `SentenceTransformer('all-MiniLM-L6-v2')` for embedding
- faiss-cpu (PyPI): `faiss.IndexFlatIP` for vector indexing and retrieval
- python-dotenv (PyPI): for loading API keys from a `.env` file
- OpenAI Python SDK or Anthropic Python SDK: for LLM answer generation
- langchain or llama-index (optional): may be used to wire retrieval and generation, but the notebook must also show the raw FAISS retrieval step explicitly
- BEIR benchmark paper (Thakur et al., 2021, arXiv:2104.08663): for context on evaluating retrieval models on scientific corpora
- Course repository skeleton notebook `week03_rag_skeleton.ipynb` as a starting point

---

### Week 4: Tool Use & Agents

#### Meeting 1 — MCP Specification and Connecting LLMs to External Tools

**Student Introduction** (assigned: S7)

> *Format:* 10-minute live demo
> 
> **Topic prompt:** Explain the Model Context Protocol (MCP) specification, focusing on its JSON-RPC 2.0 transport layer, the distinction between resources (static data exposed to the LLM) and tools (callable functions the LLM can invoke), and how tool schemas are defined using JSON Schema. Walk through a minimal MCP server–client handshake: how does the client discover available tools, and how does the server return a structured result? Reference the official MCP specification at https://modelcontextprotocol.io and the Anthropic blog post "Introducing the Model Context Protocol" (November 2024). Your presentation must address: (1) Why does MCP use JSON-RPC rather than a custom protocol? (2) How do tool input schemas constrain what an LLM can pass as arguments? (3) How does this architecture differ from a plain function-calling API (e.g., OpenAI function calling)? This topic grounds the live coding exercise that follows, where students will implement their own MCP server wrapping a real physics database.
>
> **Guiding questions:**
> 1. What is the difference between a "resource" and a "tool" in the MCP specification, and when would you expose a physics dataset as one versus the other?
> 2. If an LLM receives a JSON Schema describing a tool's input parameters, how does that schema influence the reliability of the LLM's tool calls?
> 3. What happens when an MCP server returns an error — how does the protocol signal failure back to the LLM client, and how should the client recover?

**Active Engagement** — Live coding exercise (45 minutes)

Students implement a minimal MCP server that wraps two physics database queries. A skeleton repository is pre-loaded with stub functions and a requirements file.

Step 1 (5 min): Instructor shows the skeleton structure — a Python file using the mcp SDK with two empty `@server.tool()` stubs: `query_simbad()` and `search_arxiv()`. Students clone the skeleton or open it in the shared environment.

Step 2 (15 min): Students implement `query_simbad(object_name: str) -> dict` using `astroquery.simbad` to retrieve the object type, spectral type, and parallax for a named star. The tool schema (input type, description, required fields) must be declared correctly so the LLM can call it without guidance. AI coding assistants (Copilot, Claude) are encouraged; students narrate what they are prompting and why.

Step 3 (15 min): Students implement `search_arxiv(keyword: str, max_results: int) -> list` using the arxiv Python library, returning a list of dicts with title, authors, and abstract for the top results. Students test each tool in isolation using the MCP inspector or a direct JSON-RPC call before connecting to an LLM client.

Step 4 (5 min): Students run the server and invoke both tools via a minimal LLM client script (pre-provided) that asks "What is the spectral type of Betelgeuse and what are the 3 most recent arXiv papers about it?" Verify that the LLM correctly chains both tool calls and returns a coherent answer.

Debrief (5 min): Each student shares one unexpected error they encountered and how they resolved it. Instructor notes which errors were protocol-level vs. API-level vs. physical-plausibility issues.

*Facilitation notes:* Pre-test the skeleton in the exact environment students will use — astroquery SIMBAD queries can fail silently if the TAP service is unavailable; have a cached fallback JSON response ready. Set a concrete, checkable goal visible on the projector: "Your server should return spectral type 'M1-2Ia-Iab' for Betelgeuse." Circulate and resist solving problems directly — ask "What does the JSON-RPC error code tell you?" If students finish early, extend: "Now add rate-limit handling — what happens if you call search_arxiv 10 times in 5 seconds?" For pairs who struggle with the MCP SDK, direct them to the `mcp.types` module to see the ToolResult and CallToolResult schemas.

*Materials needed:* Skeleton repository with requirements.txt (mcp, astroquery, arxiv, anthropic or openai SDK); pre-tested MCP client script; projector showing expected output for Betelgeuse query; backup cached API responses for network failures

---

#### Meeting 2 — Agentic Workflows: Multi-Step Reasoning, Tool Chaining, and Failure Recovery

**Student Introduction** (assigned: S8)

> *Format:* 10-minute slide presentation (max 6 slides)
> 
> **Topic prompt:** Explain how LLMs execute multi-step agentic workflows using iterative tool-call loops: the model receives a user query, emits a tool_use block, receives a tool_result, and decides whether to call another tool or synthesize a final answer. Discuss two prompt engineering patterns for reliable tool use: (1) the ReAct (Reason + Act) pattern (Yao et al., arXiv:2210.03629) where the model interleaves reasoning steps with tool calls, and (2) structured output constraints that prevent the model from fabricating tool arguments. Address the failure modes that arise in agentic loops: infinite looping when tool calls do not converge, cascading errors when an upstream tool returns bad data, and safety issues from unbounded API calls. Your presentation must address: (1) What terminates an agentic loop? (2) How do you bound the number of tool calls to prevent runaway API costs? (3) What is the tradeoff between giving the model autonomy to choose tools versus prescribing the exact tool-call sequence?
>
> **Guiding questions:**
> 1. In a ReAct-style agentic loop, what information must be preserved across tool-call iterations so the model maintains coherent reasoning?
> 2. If a tool returns an error or an implausible value (e.g., a negative stellar mass), should the agentic loop retry, skip, or halt — and who decides?
> 3. How would you design a rate-limit safeguard for an agentic workflow that might call the arXiv API dozens of times for a single user query?

**Active Engagement** — Collaborative whiteboard (45 minutes)

Students collectively design an end-to-end agentic pipeline architecture for a concrete physics task on the whiteboard.

Step 1 (3 min): Instructor writes the central node on the whiteboard: "Agentic Pipeline: 'Characterize a newly observed transient source.'" and asks "What does this pipeline need?" Students call out components; instructor writes them as nodes without organizing.

Step 2 (12 min): Students take turns at the whiteboard adding directional edges between nodes. Required nodes to surface (instructor prompts if missing): user query parser, LLM reasoning loop, SIMBAD tool, arXiv tool, error handler, rate limiter, output formatter, physical plausibility checker. Students must label each edge with the data type flowing across it (e.g., "object_name: str", "tool_result: JSON", "final_report: str").

Step 3 (10 min): Instructor poses three stress-test scenarios and asks students to trace the failure path on the diagram: (a) SIMBAD returns no match for the source name; (b) the LLM calls `search_arxiv` with an empty keyword string; (c) the pipeline has been running for 60 seconds and has made 20 tool calls without producing a final answer. Students draw recovery edges or add new nodes to handle each case.

Step 4 (10 min): Students negotiate and reorganize the diagram — "Does this arrow make sense? Should the rate limiter be before or after the LLM reasoning loop?" Instructor prompts quiet students directly: "Where would you add a sanity check on the output?"

Step 5 (5 min): Instructor photographs the final whiteboard, assigns one student to post it to the course repository before next class, and highlights two design decisions the class will revisit when evaluating their Week 4 homework pipelines.

Debrief (5 min): Each student names one node or edge they would change if the pipeline needed to run unsupervised overnight versus interactively with a human in the loop.

*Facilitation notes:* Resist organizing the whiteboard yourself for the first 15 minutes — let it be messy. The act of students reorganizing it is where the learning happens. Keep a mental list of nodes that must appear (rate limiter, error handler, physical plausibility checker) and surface them with questions rather than additions: "What happens when this tool gets called 50 times? Is there a node for that?" For 10 students, ensure every student adds at least one node or edge — cold-call quieter students with "Can you draw the connection between the rate limiter and the LLM loop?" The stress-test scenarios in Step 3 reliably generate productive disagreement; let disagreements run for 2 minutes before asking the room to vote on a resolution.

*Materials needed:* Whiteboard with multiple colors of markers; camera or phone for photographing final diagram; projector showing the three stress-test scenarios during Step 3; course repository access to post the diagram photograph

---

#### Homework Assignment 4: Building a Tool-Augmented Physics Agent with MCP

**Assessment category:** Standard Curriculum Mini-Assignments | **Estimated time:** 4–6 hours | **Due:** Before the first class meeting of Week 5

**Background:** Building on the retrieval pipeline from Week 3 and the debugging experience from Week 2, this assignment introduces a higher-level abstraction: the Model Context Protocol, which enables LLMs to call external tools reliably by standardizing how tool schemas, inputs, and results are communicated between a language model client and a server exposing domain-specific capabilities. [EDIT: added "building on Week 3" narrative arc context] In this assignment you will build a minimal MCP server that exposes two physics database queries as LLM-callable tools, then wire it into a short agentic loop that uses both tools to answer a compound physics question. The goal is not just a working pipeline but a documented understanding of where and how it fails — reliability analysis is as important as functionality in production AI systems.

**Instructions:**
1. Install the required libraries (mcp, astroquery, arxiv, and either anthropic or openai) and create a Python module named `mcp_server_week04_<lastname>.py`. Implement two MCP tools using the `@server.tool()` decorator: (1) `query_simbad(object_name: str) -> dict`, which queries the SIMBAD TAP service via astroquery.simbad and returns at minimum the object type, spectral type, parallax, and radial velocity for the named object; and (2) `search_arxiv(keyword: str, max_results: int) -> list`, which returns a list of dicts with title, authors, abstract, and arXiv ID for the most recent papers matching the keyword. Each tool's JSON Schema must be complete enough that an LLM can invoke it correctly without additional guidance. Include a requirements.txt and load all API keys from a `.env` file.
2. Write a Jupyter notebook named `week04_<lastname>.ipynb` that starts the MCP server as a subprocess and connects to it with an LLM client. Send the compound query to the LLM: "What is the spectral type and parallax of Betelgeuse, and what are the 3 most recent arXiv papers whose abstracts mention Betelgeuse? Summarize what the papers suggest about its current evolutionary status." Log every tool call the LLM makes (tool name, input arguments, and returned result) so the full reasoning chain is visible in the notebook output.
3. Run the same agentic query for a second astronomical object of your choice and verify the SIMBAD output against the SIMBAD web interface manually. Document whether the LLM's summary of the arXiv papers is consistent with the abstracts it received — flag any factual discrepancies between the summary and the raw abstracts.
4. Deliberately trigger at least two distinct failure modes in your pipeline and document them in a markdown file named `week04_failures_<lastname>.md`. For each failure mode, record: the input that triggered it, the error or incorrect output produced, whether the agentic loop recovered or required manual intervention, and one sentence describing how you would fix it in a production system.
5. Add a `README.md` to your submission repository with one paragraph explaining how to reproduce your results from scratch (including starting the MCP server), the Python version and key library versions used, and a note on which LLM model you used and any relevant model-version caveats. Ensure all API keys are loaded from a `.env` file and that your `.env` file is listed in `.gitignore`.

**Deliverables:**
- A Python module named `mcp_server_week04_<lastname>.py` containing a working MCP server with two tools (`query_simbad` and `search_arxiv`) with complete JSON Schema declarations.
- A Jupyter notebook named `week04_<lastname>.ipynb` demonstrating the full agentic loop for Betelgeuse and a second object of your choice, with all tool calls and results logged and a physical plausibility check documented.
- A markdown file named `week04_failures_<lastname>.md` documenting at least two failure modes: the triggering input, the erroneous output, the recovery behavior, and a proposed fix for each.

**Grading criteria:**

| Criterion | Weight | Excellent looks like |
|-----------|--------|---------------------|
| Methodology correctness | 30% | The MCP server correctly implements the JSON-RPC protocol using the mcp SDK; both tools have complete JSON Schema declarations; the agentic loop correctly chains both tool calls and produces a coherent synthesized answer. |
| Reproducibility | 25% | Any graduate student can reproduce the full pipeline from a fresh clone using only the README instructions; requirements.txt or environment.yml is present; all API keys are loaded from a `.env` file; the MCP server starts without manual path edits; the notebook runs top-to-bottom without errors. |
| Physical plausibility | 25% | The SIMBAD output for at least one object is cross-checked against the SIMBAD web interface and the comparison is documented; the LLM's summary of arXiv papers is compared against the raw abstracts and any factual discrepancies are flagged; at least one sanity check on a physical quantity is explicitly stated. |
| Code clarity | 20% | The MCP server module has docstrings for each tool function; the notebook is organized with Markdown cells separating each logical step; variable names are descriptive; the failure modes markdown is structured with clear headings for each failure case. |

**Tools and resources:**
- mcp Python SDK (`pip install mcp`)
- astroquery for SIMBAD access (`pip install astroquery`)
- arxiv Python library (`pip install arxiv`)
- anthropic or openai Python SDK for the LLM client
- python-dotenv for `.env` file loading (`pip install python-dotenv`)
- MCP specification: https://modelcontextprotocol.io
- Anthropic blog post: "Introducing the Model Context Protocol" (November 2024)
- ReAct paper: Yao et al., arXiv:2210.03629
- SIMBAD web interface for manual cross-checking: https://simbad.cds.unistra.fr/simbad/
- arXiv API documentation: https://info.arxiv.org/help/api/index.html

---

### Week 5: GenAI in Theoretical Physics & Project Proposals [EDIT: extended week title to reflect that both meetings focus on proposal development, not only GenAI in theoretical physics; the symbolic regression student intro is one component of a week whose primary purpose is proposal writing and pitching]

#### Meeting 1 — What Makes a Strong GenAI Research Proposal in Physics?

**Student Introduction** (assigned: S1)

> *Format:* 8-minute paper presentation
> 
> **Topic prompt:** Explain how symbolic regression has been used to discover physical laws from data, focusing on the AI Feynman project (Udrescu & Tegmark 2020, arXiv:1905.11172) and the PySR library (Cranmer 2023, arXiv:2305.01582). Cover: (1) what symbolic regression is and how it differs from neural-network regression; (2) one concrete example of a physical equation rediscovered from noisy data; (3) whether these methods discover genuinely new physics or recapitulate known laws. Your presentation should connect directly to this week's central question: what would a well-formed GenAI research question in theoretical physics look like?
>
> **Guiding questions:**
> 1. Did the AI Feynman system discover new physics, or did it rediscover equations already in the Feynman symbolic regression benchmark? What is the difference, and why does it matter for how we evaluate AI-assisted discovery claims?
> 2. What would a falsifiable version of "AI can discover new physics laws" look like as a research question? What dataset, method, and success criterion would you need to specify?
> 3. Where does symbolic regression fail, and what does that failure mode reveal about the limits of current GenAI tools for theoretical physics?

**Active Engagement** — Collaborative whiteboard (45 minutes)

Students collectively build a shared map on the whiteboard of what constitutes a strong GenAI research question in theoretical physics. The instructor writes the central node "A strong research question" and asks: "What connects to this?"

Step 1 (5 min): Each student silently writes one ingredient of a good research question on a sticky note or directly on the whiteboard (e.g., "names a specific dataset," "states how you will know if it worked," "uses a specific AI tool").

Step 2 (15 min): Students take turns adding their ingredients as nodes, connecting them to related nodes already on the board. When two students disagree about whether an ingredient is necessary or sufficient, the class votes and the disagreement is recorded as an open edge with a question mark.

Step 3 (15 min): The instructor selects three student proposal ideas (shared informally before class, or hypothetical examples) and asks the class to evaluate each against the map. For each idea: Is the research question specific enough? Is the dataset named and accessible? Is the AI/MCP method appropriate? The class annotates the whiteboard with strengths and gaps for each example.

Step 4 (10 min): Each student takes 90 seconds to revise their own proposal's research question sentence based on the map criteria, writing it on a notecard. Cards are collected and returned with written instructor feedback before Meeting 2.

Debrief (5 min): Instructor photographs the whiteboard and posts it to the course repository. Names the 2–3 most commonly missing ingredients across the class's notecards (without identifying individual students).

*Facilitation notes:* Post the whiteboard photo to the course repository within 24 hours so students can reference it while finalizing their proposals. Before the session, ask students to email you a one-sentence draft of their research question — this lets you select 3 representative examples (strong, adequate, and weak) to evaluate anonymously in Step 3 without embarrassing anyone. If the class converges too quickly and the map seems complete, push back: "Is every ingredient here actually necessary? Can you construct a bad research question that has all of these?" Call on quiet students directly during Step 2 — do not rely on volunteers.

*Materials needed:* Whiteboard and markers; sticky notes (optional); notecards for Step 4; camera or phone to photograph whiteboard

---

#### Meeting 2 — Proposal Pitch Session

**Student Introduction** (assigned: ALL — all students present this meeting)

> *Format:* 5-minute pitch presentation (max 5 slides) per student
> 
> **Topic prompt:** There is no assigned student introduction for this meeting. The entire session is structured as back-to-back 5-minute proposal pitches, one per student, with 2 minutes of structured peer Q&A after each pitch, facilitated by the instructor. Students should arrive having submitted their written proposal PDF and slides before class begins. The instructor opens with a 3-minute orientation: reviewing the feedback form, setting the timer protocol, and modeling the kind of question peers should ask.
>
> **Guiding questions:**
> 1. What specific physics question will your project answer?
> 2. What AI/MCP method will you use, and why is it appropriate for this question?
> 3. What dataset will you use, and how will you evaluate success?

**Active Engagement** — Peer code review (50 minutes)

Each student presents for 5 minutes, then receives 2 minutes of structured peer questions using a feedback form distributed at the start of class. The instructor facilitates and models constructive critique for the first pitch by demonstrating how to complete the feedback form aloud before peers respond.

Session structure:
- **Opening (3 min):** Instructor reviews the feedback form, sets timer protocol, and reminds the class that critique is a form of intellectual generosity.
- **Pitches (50 min):** 10 students × 7 min each (5 min pitch + 2 min Q&A). A visible countdown timer is used. The instructor cuts off at 5 minutes without apology. After each Q&A, peers silently complete the feedback form for that presenter; forms are collected and given to the presenter at the end of class.
- **Group discussion (7 min):** After all pitches, instructor leads a 7-minute discussion: "What themes did you notice across proposals? What gaps appeared most frequently? Which proposals seemed most feasible, and why?" This is conducted without singling out individuals.

Note: If the class has fewer than 10 students, the saved time should be used to extend the group discussion or allow a second round of questions for proposals that generated the most peer interest.

*Facilitation notes:* Distribute the structured feedback form before pitches begin — either printed or shared digitally. The form has exactly three fields: (1) one specific strength of the proposed research question or method; (2) one specific question about feasibility, dataset access, or methodology that the presenter should address in their project; (3) one concrete suggestion for improving the scope or clarity of the research question. Keep the form to one page so peers can complete it in under 90 seconds. For the first pitch, complete the form aloud yourself before opening to peer questions — this calibrates the class's expectations. Do not allow general praise without specificity during the Q&A; redirect with "What specifically impressed you, and why does it matter for the project?" Collect all feedback forms at the end of class and return them to the corresponding presenters within 24 hours.

*Materials needed:* Printed or shared feedback forms; projector for slides; visible countdown timer; instructor evaluation sheet for pitch delivery grading

---

#### Homework Assignment 5: Project Proposal

**Assessment category:** Project Proposal & Pitch | **Estimated time:** 5–8 hours (proposal writing + pitch preparation) | **Due:** Proposal PDF and slides submitted before Meeting 2 of Week 5; live pitch delivered in Meeting 2

**Background:** Weeks 1–4 gave you the technical vocabulary — LLM APIs, code debugging, RAG pipelines, and MCP servers — that you need to make a credible research proposal. [EDIT: added "building on Weeks 1–4" narrative arc connection to explain why the proposal is possible now] Your project proposal is your public commitment to a research direction for the remaining nine weeks of the course. It is not a wish list — it is a contract with your peers and instructor that you have identified a specific, tractable question and confirmed that the tools and data you need are accessible. Writing a good proposal is also a communication exercise: you must convince a skeptical reader that your question is worth pursuing and that you have a credible plan to answer it within the available time and computational resources.

**Instructions:**
1. Write a 2-page project proposal in RevTeX (article class, 11pt font, standard margins). Use the following section structure: Abstract (100 words max), Research Question, Proposed Method, Dataset and Evaluation Criteria, Timeline (Weeks 6–14), References.
2. In the Research Question section, state one specific, falsifiable question your project will answer. The question must name the physical system or dataset, the AI/MCP method you will use, and how you will know if the method succeeded.
3. In the Proposed Method section, name the specific tools and libraries you will use (e.g., "I will build an MCP server using the mcp Python SDK to query the Materials Project REST API, then use Claude claude-3-5-sonnet-20241022 to synthesize property trends for perovskite oxides").
4. In the Dataset section, identify a specific, accessible dataset (with URL or DOI) and state its size, format, and any preprocessing required.
5. Prepare a 5-slide pitch deck (PDF) matching the proposal structure: one slide per section (skip references). Rehearse by delivering it out loud at least twice with a running timer, aiming for exactly 5 minutes; record any section that overruns and trim it before Meeting 2. [EDIT: vague "Practice delivering it" replaced with specific rehearsal protocol — timed out-loud run-throughs]

**Deliverables:**
- A RevTeX source file named `proposal_<lastname>.tex`
- A compiled PDF named `proposal_<lastname>.pdf`
- A 5-slide pitch deck as `proposal_slides_<lastname>.pdf`

**Grading criteria:**

| Criterion | Weight | Excellent looks like |
|-----------|--------|---------------------|
| Research question clarity | 35% | The question is specific, falsifiable, names the dataset and method, and is clearly stated in one sentence. |
| Feasibility | 30% | The proposed scope is achievable in 8 weeks using named, available tools and datasets; resource gaps are acknowledged. |
| Pitch delivery | 20% | The live pitch is clear, confident, within the 5-minute limit, and addresses all three guiding questions. |
| Written proposal quality | 15% | The document is formatted in RevTeX, is 2 full pages, and all required sections are present and coherent. |

**Tools and resources:**
- RevTeX 4.2 (install via TeX Live or MikTeX)
- Overleaf (free online LaTeX editor) as an alternative
- APS Physical Review author guide for RevTeX formatting
- PySR (symbolic regression library) as one example AI tool to explore
- SymPy for symbolic computation examples

---

> **Phase transition — from shared curriculum to individual projects:** Weeks 1–5 built a common technical foundation that every student now shares: reproducible environments, API querying, debugging, RAG pipelines, tool-augmented agents, and a submitted project proposal. Starting in Week 6, each student works primarily on their *own* project. The Phase 2 meetings still serve the full class but the homework deliverables are now project-specific. Bring your approved proposal and any early data or API explorations to every class session from this point forward. [EDIT: added explicit Phase 1→2 transition note signaling shift to individual project work]

## Phase 2: Project Ideation & Deep Dives (Weeks 6–7)

Phase 2 pivots from shared curriculum to project-specific development. Students design and build the MCP server infrastructure that will underpin their final project, and develop the evaluation protocols and annotated bibliographies that frame their research contributions. By the end of Week 7, every student has a working MCP server prototype, a named evaluation baseline, and three annotated papers grounding their methodology.

---

### Week 6: Building MCP Servers

#### Meeting 1 — MCP Server Internals: Transport, Schemas, and Capability Negotiation

**Student Introduction** (assigned: S2)

> *Format:* 10-minute slide presentation (max 6 slides)
> 
> **Topic prompt:** MCP server internals — the JSON-RPC 2.0 transport layer, the tool schema (inputSchema expressed as a JSON Schema object), and how the MCP host and server negotiate capabilities during the initialization handshake. Read the MCP specification at https://modelcontextprotocol.io/specification (focus on the "Transports", "Tools", and "Lifecycle" sections) and browse the mcp Python SDK source on GitHub (modelcontextprotocol/python-sdk), paying close attention to how `@mcp.tool()` decorators map to JSON Schema entries. Prepare up to 6 slides that walk through a single tool call from the LLM client to the server and back, annotating each JSON-RPC message at each stage. Your presentation must address the guiding questions below and connect to this week's learning objective: students will implement their own tool endpoints, so they need to understand exactly what the runtime expects to receive and return.
>
> **Guiding questions:**
> 1. What fields are required in a JSON Schema inputSchema object for an MCP tool, and what happens when a required field is absent from a client call?
> 2. How does the MCP initialization handshake let a server advertise which capabilities (tools, resources, prompts, sampling) it supports, and why does this matter for client compatibility?

**Active Engagement** — Collaborative whiteboard (45 minutes)

Before committing code, students sketch their project-specific MCP server architecture on the whiteboard to solidify design decisions before coding begins.

Step 1 (5 min): Each student takes a marker and claims a section of the whiteboard. They write their project name at the top and draw a box labeled "MCP Server" in the center. Instructor asks: "What goes inside that box?"

Step 2 (15 min): Students sketch their complete MCP server architecture. The diagram must show: the LLM client at the top, the MCP server in the center with named tool endpoints and their inputSchema summaries (key fields only), and the external API or data source at the bottom, with arrows labeled with the data types flowing in each direction. Students annotate each tool with the one error case they plan to handle.

Step 3 (15 min): Gallery walk — each student has 90 seconds to explain their architecture to the room. The class asks one clarifying question per diagram. Instructor records on the shared whiteboard section: design choices that appear in multiple student architectures (indicating a common pattern) and design choices that are idiosyncratic (indicating a project-specific need).

Step 4 (5 min): Each student identifies the one tool endpoint they will implement first and writes it at the top of their section with its inputSchema. This becomes their implementation target for the remainder of the class period.

Debrief (5 min): Instructor photographs all diagrams and posts them to the course repository within one hour. Highlights two or three design decisions that generated the most discussion — these are the questions students should address explicitly in their homework design documents.

*Facilitation notes:* Pre-assign whiteboard sections before students arrive so time is not lost negotiating space. For a 10-person seminar, use a large whiteboard divided into 10 labeled zones, or provide each student a large sheet of paper if whiteboard space is limited. If a student does not yet have a project domain, have them design a server that wraps the NIST WebBook API for thermodynamic property lookup — this is a safe default with clear schemas. During the gallery walk, coach students to explain their data-type annotations: "What does your arrow from the LLM to the tool actually carry in JSON?" Photograph all diagrams before students leave.

*Materials needed:* Large whiteboard divided into 10 labeled sections (or large-format paper sheets), markers, camera or phone for photographing diagrams, course repository access for posting photos

---

#### Meeting 2 — Physics MCP Servers in the Wild: Design Reviews and Project Demos

**Student Introduction** (assigned: S9)

> *Format:* 10-minute live demo
> 
> **Topic prompt:** A real-world physics MCP server example — specifically, wrap either the Materials Project REST API (mp-api Python client) or the SIMBAD/VizieR astronomical database (astroquery) as a functioning MCP server with at least two tool endpoints. Build a minimal but working prototype in a Jupyter notebook or Python script and run it live during your introduction. Demonstrate: (1) the server starting and advertising its tool list, (2) a successful tool call returning real data, and (3) what happens when you send a malformed request. Read the mp-api quickstart (https://materialsproject.org/api) or the astroquery documentation (https://astroquery.readthedocs.io) as your primary resource. Your demo must address the guiding questions below and connect to this week's learning objective: students should see a complete, running example before they demo their own servers later in this meeting.
>
> **Guiding questions:**
> 1. What design choices did you make when mapping the external API's query parameters to MCP tool inputSchema fields, and what were the trade-offs?
> 2. How did you handle rate limiting or authentication so the MCP server can be used by multiple students without credential leaks?

**Active Engagement** — Collaborative whiteboard (45 minutes)

The whiteboard session has two phases: individual sketching and collective critique.

Phase 1 — Individual architecture sketches (15 min): Each student goes to the whiteboard (or a labeled section of it) and draws the architecture of their own project's MCP server. The diagram must show: the LLM client at the top, the MCP server in the middle (with named tool and resource endpoints), and the external data source or API at the bottom, with arrows labeled with the data types flowing in each direction. Students should annotate each tool endpoint with its inputSchema summary (just the key fields) and its return type.

Phase 2 — Peer critique (20 min): The instructor assigns each student to critique the diagram immediately to their right. The critic must identify: (a) one data flow arrow that is ambiguous or missing, (b) one error case the diagram does not account for, and (c) one alternative design the author has not considered. Critics state their observations aloud; the author may respond but not yet edit the diagram. The instructor records the most-disputed design decisions on a shared section of the whiteboard.

Phase 3 — Live prototype demos (10 min): Any student who has a running prototype (from the Meeting 1 homework or early work) demonstrates it live — one successful call and one error case. The class asks one clarifying question per demo.

Debrief (5 min, instructor): The instructor photographs all diagrams and posts them to the course repository. Highlight the two or three design decisions that generated the most disagreement.

*Facilitation notes:* Assign whiteboard sections before students arrive. During Phase 2 critique, call on quieter students first. If a student's critique is too surface-level ("the arrows look fine"), push with "What happens if the external API is down — does this diagram tell you where the error surfaces?" If no students have a working prototype for Phase 3, use the student introducer's demo from the start of class as the shared example. Photograph all diagrams before students leave. Post to the course repository within one hour.

*Materials needed:* Large whiteboard with markers (or large-format paper sheets), camera or phone for photographing diagrams, course repository access for posting photos

---

#### Homework Assignment 6: Project MCP Server Prototype

**Assessment category:** Final Project Codebase & Paper | **Estimated time:** 5–8 hours | **Due:** Before the first class meeting of Week 7

**Background:** This week you build the core tool infrastructure for your own research project: a working MCP server that exposes at least two tool endpoints wrapping a physics-relevant external API or dataset. The server you submit this week is not a throwaway exercise — it will become a committed component of your final project codebase, and the design decisions you make now (schema choices, error handling strategy, authentication approach) will carry forward into Weeks 7–14. Treat this assignment as the first real engineering deliverable of your project, not as a tutorial exercise.

**Instructions:**
1. Design the tool schema for your project-specific MCP server. Write a design document (1 page, any format) listing: (a) the two tool endpoints you will implement, (b) each tool's inputSchema (as a JSON Schema object), (c) the expected output format, and (d) the external API or data source each tool will call.
2. Implement the MCP server in Python using the mcp SDK. Each tool must handle at least one error case (e.g., API timeout, missing parameter, invalid input) and return a structured error message rather than crashing.
3. Write a test script (`test_mcp_server.py`) that calls each tool endpoint with both valid and invalid inputs and verifies the outputs match the expected schema.
4. Document the server in a `README.md`: include installation instructions, environment variables required, example tool calls with expected outputs, and a brief description of known failure modes.
5. Demonstrate the server in class during Meeting 2 by running it live and showing a successful LLM-client tool call.

**Deliverables:**
- Python module `mcp_server_<lastname>.py` containing the MCP server implementation
- Test script `test_mcp_server_<lastname>.py` with at least 4 test cases (2 valid, 2 error)
- `README.md` with installation and usage instructions
- Design document `design_<lastname>.md` or `design_<lastname>.pdf`

**Grading criteria:**

| Criterion | Weight | Excellent looks like |
|-----------|--------|---------------------|
| Tool functionality | 40% | Both tool endpoints return correct, schema-conforming outputs for valid inputs and structured errors for invalid inputs. |
| Reproducibility | 30% | The server can be installed and run from scratch using only the README instructions and a fresh Python environment. |
| Code documentation | 20% | README is complete, tool schemas are documented with examples, and error cases are described. |
| Design clarity | 10% | The design document clearly states the tool's purpose, schema, and the external data source it wraps. |

**Tools and resources:**
- mcp Python SDK (`pip install mcp`)
- MCP specification: https://modelcontextprotocol.io/specification
- astroquery (for SIMBAD, VizieR, NASA ADS)
- mp-api (for Materials Project access)
- arxiv Python library
- pytest for test script

---

### Week 7: Evaluating AI in Physics

#### Meeting 1 — Benchmarking AI Outputs Against Physical Ground Truth

**Student Introduction** (assigned: S3)

> *Format:* 8-minute paper presentation
> 
> **Topic prompt:** Evaluation metrics for AI in physics — calibration curves, mean absolute error in physical units, coverage of uncertainty intervals, and R² vs. physically meaningful error tolerances. Read Cranmer et al. 2020 "The frontier of simulation-based inference" (arXiv:1911.01429) and identify how the authors evaluate their inference methods against ground truth posteriors. In 3–5 sentences, name at least two specific metrics the paper uses, explain what a well-calibrated posterior means in a physics context, and describe one case where a low aggregate error metric can still hide a physically significant failure mode. Connect this to your own project: what would a well-calibrated evaluation look like for an AI component you plan to use?
>
> **Guiding questions:**
> 1. If an AI model achieves 5% MAE on predicted band gaps — better than the variance in DFT functionals — does that make it adequate for materials discovery? What additional evidence would a skeptical referee demand?
> 2. How do you distinguish a model that is accurate on average from one that is accurate where it matters? Can you construct a scenario where the two diverge?

**Active Engagement** — Structured debate (45 minutes)

Claim for debate (displayed on a slide throughout): "A neural network that achieves MAE < 0.1 eV on a held-out test set is ready to replace DFT for high-throughput materials screening."

Step 1 — Assign sides (2 min): Randomly split the room into two groups of ~5. One group defends the claim; the other critiques it. Assign students to the side opposite their intuited view wherever possible.

Step 2 — Preparation (5 min): Each side caucuses privately. They must identify (a) the two strongest arguments for their position, (b) the opposing side's most likely strongest counterargument, and (c) one piece of evidence or reasoning that would change their position.

Step 3 — Opening statements (6 min total): Each side delivers a 3-minute opening statement. One spokesperson presents; others may pass written notes.

Step 4 — Rebuttal (6 min total): Each side has 3 minutes to respond directly to the other side's opening statement. New evidence may be introduced.

Step 5 — Open cross-examination (10 min): Both sides may question each other directly. Instructor enforces that every question receives a direct answer before follow-ups are allowed.

Step 6 — Debrief (8 min): Instructor asks: What additional data would resolve this debate? Students name specific experiments, datasets, or validation studies. Instructor lists open questions on the whiteboard. Poll: did anyone change their position?

*Facilitation notes:* Assign the paper before class (Perdew et al. 1996 PRL on DFT accuracy, or a recent neural network potential benchmark such as Batzner et al. 2022 NequIP, arXiv:2101.03164). Display the claim on a persistent slide — students should be arguing about that specific numeric threshold, not about AI in general. Keep a visible countdown timer for each segment; do not let opening statements run long as it compresses rebuttal. If one side dominates, prompt the weaker side with: "Your opponents have not addressed X — is that a concession?" Debrief key probe: "Name a physical regime where 0.1 eV MAE would be catastrophically wrong. Now name one where 1 eV MAE would be acceptable. What does that tell you about the adequacy of aggregate metrics?" Do not express your own view during the debate; save it for the final two minutes of debrief.

*Materials needed:* Slide with the debate claim displayed; printed or digital access to at least one neural network potential benchmark paper (e.g., Batzner et al. 2022 or Smith et al. 2017 ANI-1); visible countdown timer; whiteboard for recording open questions

---

#### Meeting 2 — Uncertainty Quantification and Evaluation Protocol Design

**Student Introduction** (assigned: S10)

> *Format:* 10-minute slide presentation (max 6 slides)
> 
> **Topic prompt:** Uncertainty quantification (UQ) for AI-generated physical quantities — conformal prediction, Monte Carlo dropout, and deep ensembles, and how each applies when the quantity carries physical units and must be compared to experimental measurement uncertainty. Read Lakshminarayanan et al. 2017 "Simple and scalable predictive uncertainty estimation using deep ensembles" (arXiv:1612.01474) and one physics-specific application such as Wen & Bhatt 2020 on UQ for interatomic potentials or Peterson et al. 2017 on uncertainty in atomistic simulations. In 3–5 sentences, explain what it means for an uncertainty interval to be calibrated, contrast coverage probability with interval sharpness, and describe a case where overconfident AI predictions would lead to a physically wrong conclusion. Explain how you would apply one of these UQ methods to your own project.
>
> **Guiding questions:**
> 1. A deep ensemble reports a 95% confidence interval for a predicted cross-section. If you run 100 predictions and 12 of the true values fall outside the reported interval, what does that tell you, and what should you do next?
> 2. When is it better to have a wide, calibrated uncertainty interval than a narrow, overconfident one? Give a concrete example from experimental or computational physics.

**Active Engagement** — Collaborative whiteboard (45 minutes)

Goal: Collectively build a generalized evaluation protocol rubric on the whiteboard that any student in the room could apply to assess an AI component in their own project.

Step 1 — Seed the whiteboard (3 min): Instructor writes the central node "AI Component Evaluation Protocol" and draws five empty branches labeled: (1) Primary metric, (2) Baseline, (3) Test dataset, (4) UQ method, (5) Success threshold. Ask: "What belongs in each branch?"

Step 2 — Individual contribution round (10 min): Each student takes a marker in turn and adds at least one concrete item to any branch — a specific metric name, a baseline type, a dataset source, a UQ method, or an example success criterion. Students must speak aloud as they write, explaining their choice. Others may challenge by raising a hand; the instructor arbitrates briefly.

Step 3 — Project-specific annotation (12 min): Each student picks their own project and, at their seat, drafts their own version of the five-branch protocol using the shared vocabulary on the whiteboard. They write their primary metric with units, their named baseline, their test dataset with a DOI or URL, their UQ approach, and their numeric success criterion.

Step 4 — Gallery share (10 min): Three students volunteer (or are called on) to read their five-point protocol aloud. The room asks: Is the metric specific enough? Is the baseline realistic? Is the success threshold defensible?

Step 5 — Debrief (7 min): Instructor photographs the whiteboard. Ask: "Which branch was hardest to fill in, and why?" Highlight the branches where students disagreed — these are the live methodological tensions in the field. Connect the rubric directly to the Week 7 homework deliverable.

*Facilitation notes:* Resist the urge to organize the whiteboard before students have contributed — let it be messy first, then ask a student to reorganize a branch that has grown unwieldy. Call on quiet students by name for the contribution round; every student must add something. Common stalling point: the "success threshold" branch. Prompt with: "If a journal referee asked you what 'good enough' means for your AI component, what specific number would you defend?" If students propose vague thresholds ("better than baseline"), push back: "Better by how much? At what confidence level?" For the gallery share, prioritize students whose projects are most different from each other so the room sees a range of evaluation contexts. Post the whiteboard photograph to the course repository within 24 hours.

*Materials needed:* Whiteboard with sufficient space for a five-branch diagram; multiple colored markers (use color to distinguish metric types from dataset sources from UQ methods); camera or phone for whiteboard photograph; blank paper or open laptops for Step 3

---

#### Homework Assignment 7: Project Evaluation Protocol and Annotated Bibliography

**Assessment category:** Final Project Codebase & Paper | **Estimated time:** 5–7 hours | **Due:** Before the first class meeting of Week 8

**Background:** Rigorous evaluation is what separates a physics result from a physics-flavored computation. Before you build the core of your project in Weeks 8–13, you need a clear, quantitative answer to: "How will I know if my AI component works?" This week's deliverables establish that standard in writing. A specific evaluation protocol written now — with named metrics, a named baseline, a named test dataset, and a numeric success criterion — will prevent the most common project failure mode: building something that is hard to evaluate fairly. The annotated bibliography grounds your evaluation choices in what the field already knows.

**Instructions:**
1. Write a one-page evaluation protocol document (`evaluation_protocol_<lastname>.md`) for your project's primary AI component. It must specify: (a) the primary evaluation metric (e.g., MAE in eV, F1 score, percent deviation from DFT baseline), (b) the baseline model or method you will compare against, (c) the test dataset you will use (with source URL or DOI), and (d) the threshold for "success" (e.g., "MAE < 0.1 eV, matching chemical accuracy"). The threshold must be a specific number with units and a justification of one or two sentences explaining why that threshold is physically meaningful.
2. Draw a project architecture diagram (`architecture_<lastname>.pdf` or `.png`) showing the full data flow from raw data source through your AI pipeline to the final evaluated output. Include all of the following labeled components: data source(s), preprocessing steps, AI model or tool, any MCP server or external API calls, and the evaluation step that applies your metric. Use any diagramming tool (draw.io at https://diagrams.net, Mermaid at https://mermaid.js.org, or hand-drawn and photographed clearly). The diagram must be readable at standard screen resolution — label every arrow and box.
3. Find three papers directly relevant to your project's AI method or physics domain. For each paper, write a 150-word annotation covering exactly four points: (a) what AI method the paper uses, (b) how it evaluates the AI output (specific metrics and datasets), (c) whether the evaluation is adequate — and why or why not, citing at least one specific omission or strength — and (d) one specific technique or finding you will adapt for your own project, stated concretely enough that a reader could verify whether you actually did it. Compile all three annotations into `bibliography_<lastname>.md` using a standard citation format (APA, AIP, or BibTeX rendered as text).
4. Implement a baseline model for your project in a Jupyter notebook (`baseline_<lastname>.ipynb`). Load your test dataset, fit or define the baseline, evaluate it using the metric you specified in Step 1, and report the result with units. Include a markdown cell interpreting the baseline result physically: is it better or worse than you expected, and why? You will compare your AI model's performance against this baseline in later weeks.

**Deliverables:**
- `evaluation_protocol_<lastname>.md` — one-page evaluation protocol with metric, baseline, test dataset (with DOI or URL), and numeric success threshold with justification
- `architecture_<lastname>.pdf` or `.png` — project architecture diagram showing the full pipeline from data source to evaluated output with all components labeled
- `bibliography_<lastname>.md` — annotated bibliography of 3 papers, each annotation addressing all four required points in approximately 150 words
- `baseline_<lastname>.ipynb` — Jupyter notebook implementing and evaluating the baseline model on the test dataset, reporting the evaluation metric with units and a physical interpretation

**Grading criteria:**

| Criterion | Weight | Excellent looks like |
|-----------|--------|---------------------|
| Evaluation protocol specificity | 35% | The protocol names a specific metric with units, a named baseline method, a named test dataset with a source URL or DOI, and a numeric success threshold with a one-to-two sentence physical justification. Vague thresholds ("better than baseline") or missing dataset sources are inadequate. |
| Architecture diagram completeness | 25% | The diagram shows the full pipeline from data source to evaluated output with all components present and labeled: data source, preprocessing, AI model or tool, any external API or MCP server calls, and the evaluation step. Every arrow and box is readable at standard screen resolution. |
| Annotation quality | 25% | Each annotation addresses all four required points (AI method, evaluation approach, adequacy judgment, concrete adaptation plan) and falls within approximately 150 words. The "what I will adapt" statement is specific enough to be verifiable in the final project. |
| Baseline implementation | 15% | The baseline notebook runs end-to-end without errors, reports the evaluation metric value with correct units on the named test dataset, and includes a markdown cell with a physical interpretation of the baseline result. |

**Tools and resources:**
- scikit-learn for baseline models (linear regression, k-NN, SVR)
- matplotlib/seaborn for calibration curves and evaluation plots
- draw.io (https://diagrams.net) for graphical architecture diagrams
- Mermaid (https://mermaid.js.org) for code-based flowchart diagrams
- Semantic Scholar or Google Scholar for paper discovery
- uncertainties (Python package) for uncertainty propagation in baseline metrics
- MAPIE or nonconformist (Python) for conformal prediction baselines

---

> **Phase transition — from design to execution:** By the end of Week 7 every student has a working MCP server prototype, a named evaluation baseline, and a written evaluation protocol. Phase 3 is execution mode: the deliverables from Weeks 8–13 are direct components of your final submission. The lab notebook from Week 8, the observability infrastructure from Week 9, the peer reviews from Weeks 10 and 12, and the paper drafts from Weeks 11–13 all feed into the final codebase and paper due in Week 14. Plan your Week 8 start by ensuring your MCP server runs cleanly, your test dataset is downloaded, and your evaluation protocol is pinned. [EDIT: added explicit Phase 2→3 transition note signaling shift into project execution mode]

## Phase 3: Project Execution & Polish (Weeks 8–14)

Phase 3 is the longest and most intensive phase of the course. Students build, debug, and document their full project pipeline (Weeks 8–9), then engage in two rounds of structured peer code review (Weeks 10 and 12), read and discuss cutting-edge papers in a seminar format (Weeks 11–12), write and polish their scientific paper (Weeks 11–13), and conclude with a public departmental showcase (Week 14). The homework load is heavier than in earlier phases; the Week 13 assignment is explicitly flagged as the largest of the semester.

---

### Week 8: Advanced Platform Integration

#### Meeting 1 — Unifying Heterogeneous Scientific Databases

**Student Introduction** (assigned: S4)

> *Format:* 10-minute slide presentation (max 6 slides)
> 
> **Topic prompt:** Data normalization across heterogeneous scientific APIs — how do you reconcile unit systems (CGS vs SI), identifier schemes (object names vs coordinates vs DOIs), and schema differences when combining SIMBAD, Materials Project, and arXiv data in one pipeline? Prepare a slide presentation (up to 6 slides) showing a concrete normalization schema you have used or designed for your own project — for example, how you would unify a SIMBAD celestial-object record (ICRS coordinates, flux in Jy) with an arXiv abstract (DOI, author list, date) into a single internal data model. You should engage with the astroquery documentation and the Materials Project REST API schema (https://api.materialsproject.org) before class. Your presentation must address: (1) what canonical identifier you chose as the primary key and why, (2) how you handle objects that exist in one database but not another, and (3) how unit conversion is encoded so downstream code never sees raw heterogeneous units. Connect your answer explicitly to Learning Objective 3 — producing a data provenance record — by explaining how your schema tracks which database each field came from.
>
> **Guiding questions:**
> 1. What is the minimal canonical identifier that is present (or derivable) across SIMBAD, Materials Project, and arXiv, and what do you do when an object has no entry in one of the three systems?
> 2. If two APIs return the same physical quantity in different unit systems, where in the pipeline does the conversion happen, and how does the provenance record encode which system the raw value came from?

**Active Engagement** — Collaborative whiteboard (45 minutes)

Each student takes a 5-minute turn at the whiteboard to sketch the data-flow diagram for their own project pipeline: where data enters, how it is normalized, where it is cached, and where errors can occur. Use two marker colors throughout — one for data flow, one for error/exception paths — so failure modes are visually distinct from the happy path.

After all students have sketched their pipelines (approximately 50 minutes for 10 students at 5 minutes each), the class votes by show of hands on the 2 pipelines that appear most architecturally complex or that expose the most interesting failure modes. Those two pipelines are discussed in depth for the remaining time: the class asks the pipeline's owner clarifying questions and suggests normalization or error-handling improvements.

The instructor facilitates by prompting with "What is missing from this diagram?" and "Does anyone disagree with how this arrow is drawn?" rather than by filling in the diagram themselves. Every student must contribute at least one annotation or question during the depth-discussion phase; the instructor should call on quiet students directly.

*Facilitation notes:* Pre-assign whiteboard sections before class so students do not waste time negotiating space. Use different marker colors for data flow vs error paths — establish this norm during the first sketch so all subsequent sketches follow it. Photograph all sketches at the end of class with a phone or tablet and post the images to the course repository before the next meeting; these photographs become a shared reference for pipeline architecture discussions in Weeks 9–12. If a student's pipeline is not yet implemented, ask them to sketch the intended architecture — the gaps that emerge are equally informative.

*Materials needed:* Whiteboard divided into 10 labeled sections, markers in at least two colors, phone or tablet camera for end-of-class photographs

---

#### Meeting 2 — Resilient API Clients and Data Provenance

**Student Introduction** (assigned: S8)

> *Format:* 10-minute live demo
> 
> **Topic prompt:** Building resilient API clients for long-running agentic pipelines — specifically exponential backoff with jitter, circuit-breaker patterns, local caching with diskcache or sqlite3, and structured provenance logging. Prepare a 10-minute live demo in a Jupyter notebook or terminal that shows a concrete implementation. Your demo must include: (1) a working example of the tenacity library (`@retry` decorator with `stop_after_attempt(3)`, `wait_exponential`, and a `before_sleep` logging callback) applied to a real API call (e.g., astroquery SIMBAD or mp-api); (2) a diskcache or sqlite3 cache that prevents redundant API calls across pipeline runs; (3) a provenance record written as a JSON file that captures source URL, access timestamp, and any transformation applied. Run the demo against a live API if network is available; have a pre-recorded fallback in case of connectivity issues. Connect to Learning Objectives 1 and 2: students should see exactly how exponential backoff and null-field handling are implemented in production-quality research code.
>
> **Guiding questions:**
> 1. The tenacity library retries on exceptions — what exception types should you catch when calling astroquery vs mp-api, and what exceptions should you let propagate immediately rather than retrying?
> 2. When a field is missing from an API response, the instructions say to log the missing field and substitute a sentinel value — what sentinel value is physically meaningful (vs. just convenient) for a missing flux measurement, and how do you ensure downstream code handles it correctly?

**Active Engagement** — Pair debugging (45 minutes)

The instructor provides a pre-written Python script (`multi_api_pipeline_broken.py`, committed to the course repository before class) that fetches data from SIMBAD and the Materials Project, normalizes units, and writes a provenance JSON file. The script contains exactly 3 planted failures:

- **(a)** A rate-limit exception from astroquery that is caught by a bare `except` clause and silently swallowed instead of being retried — the pipeline appears to succeed but returns stale cached data from a previous run.
- **(b)** A unit mismatch: luminosity values from SIMBAD are in solar luminosities but are added directly to a column labeled "L_SI" without conversion, producing values that are off by a factor of ~3.8×10²⁶.
- **(c)** A missing null check: the Materials Project response occasionally omits the "band_gap" field for metallic compounds; the script accesses `response["band_gap"]` without a `.get()` guard and raises a `KeyError` on those entries.

Students are assigned to pairs (rotating alphabetically from the Week 7 pairing). Pairs have 30 minutes to find and fix all three bugs and document each fix with a one-sentence explanation in a comment above the corrected line. After 30 minutes, the instructor calls time regardless of progress.

Debrief (10 minutes): each pair shares the bug they found last — typically the unit mismatch, since it requires physical reasoning rather than Python knowledge to detect. The instructor asks: "How would a provenance record have made bug (b) detectable without running the pipeline?" to connect the exercise directly to Learning Objective 3.

*Facilitation notes:* Plant the bugs at different depths of difficulty: the null-check bug (c) is typically found first because it raises an obvious exception; the silent-swallow bug (a) is found second because it requires reading the error-handling code carefully; the unit mismatch (b) is found last because it requires checking whether the numerical values are physically plausible. If a pair finishes all three bugs early, ask them to write a fourth test case that would catch bug (b) automatically without human inspection. Assign pairs by rotating alphabetically through the class roster so each student works with a new partner each week. Commit the broken script and a separate solution script to the course repository at least 24 hours before class.

*Materials needed:* Laptops with Python environment (tenacity, astroquery, mp-api, diskcache installed), course repository access, broken pipeline script pre-committed to repo

---

#### Homework Assignment 8: Project Data Pipeline Implementation

**Assessment category:** Final Project Codebase & Paper | **Estimated time:** 6–8 hours | **Due:** Before the first class meeting of Week 9

**Background:** This assignment is the first concrete milestone of your final project codebase. The data ingestion module you build this week will be submitted as part of your final repository in Week 14 and will be reviewed by a peer in Week 10. Build it as if you are writing production research code: documented, reproducible, and resilient to the API failures that inevitably occur in long-running pipelines. The provenance record you produce this week will also serve as the evidentiary foundation for the data section of your final paper.

**Instructions:**
1. Implement the data ingestion layer of your project pipeline as a Python module (`data_pipeline_<lastname>.py`). The module must fetch data from at least two external sources (APIs, databases, or files), normalize units and identifiers to a consistent internal schema, and write the result to a local cache (SQLite database or parquet file) to avoid redundant API calls.
2. Add error handling for at least two distinct failure modes: (a) API timeout or rate limit — implement exponential backoff using the tenacity library with at least 3 retries; (b) missing or null fields — log the missing field with its source URL and substitute a documented sentinel value rather than crashing.
3. Write a data provenance JSON file (`provenance_<lastname>.json`) that records, for each dataset: source URL or API endpoint, access timestamp, version or commit hash of the source (if available), and any transformations applied.
4. Run your pipeline on real data and record the first analysis result in a Jupyter lab notebook (`lab_notebook_<lastname>.ipynb`). The notebook must include: the raw output from at least one API call, the normalized version, and a plot comparing your AI pipeline's output to your Week 7 baseline on at least 5 data points.

**Deliverables:**
- `data_pipeline_<lastname>.py` — data ingestion module with error handling
- `provenance_<lastname>.json` — data provenance record
- `lab_notebook_<lastname>.ipynb` — lab notebook with first analysis results and baseline comparison plot
- Updated `README.md` in the project repository documenting how to run the pipeline

**Grading criteria:**

| Criterion | Weight | Excellent looks like |
|-----------|--------|---------------------|
| Pipeline functionality | 40% | The pipeline fetches from two sources, normalizes data, caches results, and handles both required failure modes without crashing. |
| Reproducibility | 30% | Running the pipeline from a fresh clone produces identical cached data; provenance.json is complete and accurate. |
| Analysis results | 20% | The lab notebook shows real data from the pipeline and includes a quantitative comparison to the Week 7 baseline. |
| Code documentation | 10% | The pipeline module has docstrings on all functions; the README documents how to run the pipeline end-to-end. |

**Tools and resources:**
- tenacity (`pip install tenacity`) for retry logic
- diskcache or sqlite3 for local caching
- astroquery for SIMBAD/VizieR/NASA ADS access
- mp-api for Materials Project
- pandas for data normalization
- pyarrow for parquet file output

---

### Week 9: Debugging Agentic Workflows

#### Meeting 1 — Structured Debugging and Observability for Agentic Pipelines

**Student Introduction** (assigned: S5)

> *Format:* 10-minute live demo
> 
> **Topic prompt:** Structured debugging of AI pipelines — the OODA loop (Observe, Orient, Decide, Act) applied to agentic failures; how to add structured logging with Python's logging module and JSON log formatting; how to use LangSmith or a simple trace dictionary to capture tool call sequences. Read the LangSmith tracing documentation and the python-json-logger README before class. Demonstrate adding structured logging to a short agentic script (20–40 lines) and show how to replay a failure from the resulting logs alone. Your presentation must connect directly to Learning Objective 2: adding logging sufficient to reproduce any failure from the logs alone. 3–5 sentences of spoken context, then a live terminal demo.
>
> **Guiding questions:**
> 1. What information must a log entry contain to allow a failure to be reproduced from the log alone?
> 2. How do you distinguish a model hallucination from a tool failure in a log trace?
> 3. What is prompt drift and how would you detect it in a long agentic conversation?

**Active Engagement** — Pair debugging (45 minutes)

Instructor pre-loads a broken 60-line agentic pipeline script (`agentic_bug_hunt.py`, shared via the course repo) with three planted failures:
1. A tool call that silently returns an empty list instead of raising an error when the API returns 0 results.
2. A prompt that accumulates context across iterations causing a token limit overflow on iteration 4.
3. A missing random seed causing non-reproducible results between runs.

Pairs have 30 minutes to find all three bugs using only the script and its logs. They must write a `bug_report.md` naming the line number, the failure mode category (from the week's taxonomy), and the fix applied. Last 10 minutes: each pair shares their most interesting bug; class votes on best fix.

*Facilitation notes:* Run the script yourself before class to confirm all three bugs trigger reliably. Share the script 10 minutes before class starts so pairs can read it cold. If pairs finish early, give them a bonus challenge: add structured JSON logging to the fixed script. Debrief by revealing the bugs one at a time, asking each pair whether they found it and what threw them off.

*Materials needed:* `agentic_bug_hunt.py` pre-loaded in course GitHub repo; pairs need laptops with Python environment

---

#### Meeting 2 — Reproducibility in Agentic Workflows

**Student Introduction** (assigned: S9)

> *Format:* 8-minute paper presentation
> 
> **Topic prompt:** Reproducibility for agentic workflows — how to record tool call sequences (storing inputs/outputs as a JSON trace), how to set and propagate random seeds through a pipeline that uses both numpy and an LLM (temperature=0 for determinism), and how to use pytest-recording or vcr.py to mock API calls in tests. Read Pineau et al. 2021 "Improving Reproducibility in ML Research" (arXiv:2011.09961) before class, focusing on their reproducibility checklist. Present the key findings of this paper in 8 minutes: what does their checklist identify as the most common reproducibility failures in ML research, why is temperature=0 necessary but not sufficient for full pipeline reproducibility, and how does the paper connect to Learning Objective 2? Engage deeply with the paper's arguments — this is a paper presentation, not a chalk talk. You may bring annotated notes but should speak to the argument, not read from them.
>
> **Guiding questions:**
> 1. What does it mean for an agentic pipeline to be "reproducible" if the LLM is stochastic?
> 2. What is the minimum information that must be logged to allow another researcher to reproduce your result?
> 3. How do vcr.py cassettes help make agentic tests deterministic?

**Active Engagement** — Structured debate (45 minutes)

The instructor poses the central motion for debate: "Agentic AI pipelines can be made scientifically reproducible to the same standard as conventional computational physics code."

Step 1 — Assign sides (2 min): Instructor divides the room into two teams of ~5. Team A argues FOR (agentic pipelines CAN be reproducible); Team B argues AGAINST. Instructor assigns students to the side opposite their intuited view wherever possible to strengthen both arguments.

Step 2 — Preparation (5 min): Each team caucuses. They must prepare: (a) two opening arguments citing specific technical mechanisms (e.g., temperature=0, vcr.py cassettes, seed logging), (b) the strongest counterargument from the other side, and (c) one piece of evidence from Pineau et al. 2021 that supports their position.

Step 3 — Opening statements (6 min total): Each team delivers a 3-minute opening statement. Spokesperson leads; others may pass written notes. Arguments must be technically grounded — vague claims about AI uncertainty are insufficient.

Step 4 — Rebuttals (8 min total): 4 minutes per team. Each team must directly address the other's opening. New technical evidence may be introduced. Instructor enforces focus: "Address their specific argument, not a different one."

Step 5 — Open floor (10 min): Students from either team may speak freely. Instructor injects: "What if you can reproduce the same conclusion but not the exact numbers — is that sufficient for science?" and "Name a physical result from your own project that is or is not reproducible under this standard."

Step 6 — Vote and debrief (10 min): Anonymous vote: has your position changed? Instructor reveals the Pineau et al. practical consensus and synthesizes what students should actually do in their own projects to maximize reproducibility.

*Facilitation notes:* Prepare 3 controversial claims to inject if discussion stalls: (1) "Setting temperature=0 is sufficient for reproducibility." (2) "You should log every token the LLM generates." (3) "A result is reproducible if I can get the same conclusion even if not the same exact numbers." Have the Pineau et al. checklist ready to project as a concrete reference. Keep a visible countdown timer for each segment. Do not let the debate become philosophical — keep pushing both teams back to concrete technical mechanisms.

*Materials needed:* Index cards for notes during preparation; projector for Pineau et al. checklist; visible countdown timer

---

#### Homework Assignment 9: Adding Observability and Reproducibility to Your Project Pipeline

**Assessment category:** Final Project Codebase & Paper | **Estimated time:** 5–7 hours | **Due:** Before the first class meeting of Week 10

**Background:** A pipeline that cannot be debugged from its logs is not a scientific instrument — it is a black box. This week you will instrument your project pipeline with structured logging and commit at least one reproducible result to your GitHub repository, establishing the observability standards your final codebase must meet.

**Instructions:**
1. Add structured JSON logging to every tool call in your project pipeline using Python's logging module configured with a JSONFormatter (`pip install python-json-logger`). Each log entry must include: timestamp, tool name, input arguments (sanitized to remove API keys), output summary (first 200 characters or a structured dict), elapsed time in milliseconds, and success/failure status.
2. Set and document all random seeds in your pipeline. For numpy operations, call `numpy.random.seed(42)` at the top of your main script. For LLM calls, set `temperature=0` (or the lowest deterministic setting available). Add a `REPRODUCIBILITY.md` file listing every source of randomness in your pipeline and how it is controlled.
3. Find and fix at least one bug in your own pipeline this week. Document it in a `BUG_LOG.md` file with: the bug description, the failure mode category (from class taxonomy: silent failure, hallucination, context overflow, loop, non-reproducibility), the line(s) of code affected, and the fix applied.
4. Commit at least one key analysis result to your GitHub repository. The result must be the single most important quantitative output your pipeline has produced so far — for example, a bar chart of precision@3 scores across evaluation questions, a scatter plot of predicted vs. actual values for your baseline, or a table of retrieved abstracts and their cosine similarity scores. [EDIT: vague "key analysis result" replaced with three concrete examples] The commit must include: the result itself (a figure or table), the exact command to reproduce it (in the README or a Makefile target), and the log file from the run that produced it.

**Deliverables:**
- Updated project repository on GitHub with JSON logging added to all tool calls
- `REPRODUCIBILITY.md` documenting all random seeds and non-deterministic components
- `BUG_LOG.md` documenting at least one bug found and fixed with the required fields
- At least one committed analysis result (figure or table) with a reproduction command in the README

**Grading criteria:**

| Criterion | Weight | Excellent looks like |
|-----------|--------|---------------------|
| Logging completeness | 35% | Every tool call produces a structured JSON log entry with all required fields; a reviewer can trace the full execution from the log without running the code. |
| Reproducibility controls | 30% | REPRODUCIBILITY.md is complete; all random seeds are set and documented; running the pipeline twice produces identical output. |
| Bug documentation | 20% | BUG_LOG.md identifies the bug with line numbers, classifies it using the week's taxonomy, and describes the fix clearly enough to understand without running the code. |
| Committed result | 15% | A figure or table is committed to the repository with a one-command reproduction instruction that works from a fresh clone. |

**Tools and resources:**
- python-json-logger (`pip install python-json-logger`)
- tenacity for retry logging
- vcr.py or pytest-recording for mocking API calls in tests
- Pineau et al. 2021 "Improving Reproducibility in ML Research" (arXiv:2011.09961)
- GNU Make for defining reproduction commands as Makefile targets


---

### Week 10: Ethics & Reproducibility

#### Meeting 1 — AI Research Ethics and Disclosure Standards

**Student Introduction** (assigned: S1) [EDIT: corrected from S5; rotation table and summary both assign S1 to 10M1]
> *Format:* 10-minute slide presentation (max 6 slides)
>
> **Topic prompt:** Prepare a 10-minute slide presentation (max 6 slides) covering current journal and professional society policies on AI tool use disclosure in physics research. Read: (1) the Nature portfolio editorial on AI use in papers (https://www.nature.com/articles/d41586-023-00191-1); (2) the APS statement on AI in peer review; (3) at least one recent arXiv paper that includes an explicit AI tools statement. Your presentation must identify where current policies are specific enough to follow and where they leave room for interpretation, using concrete examples drawn from the three sources. Connect to this week's theme: students will write their own AI tools and ethics statements in Homework 10, and a clear understanding of existing policy language is the prerequisite. [EDIT: rewrote topic prompt from note-style ("Student should read..."; "3-5 sentences.") to directive format consistent with other week intros; removed template placeholder text]
>
> **Guiding questions:**
> 1. What is the difference between disclosing AI use for writing assistance vs. AI use for data analysis?
> 2. Which current journal policies are specific enough to follow, and which leave room for interpretation?
> 3. What information should an AI tools statement contain to be scientifically useful to a reader?

**Active Engagement** — Structured debate (45 minutes)

The class debates the motion: "An LLM-generated figure in a physics paper requires explicit caption-level disclosure, not just a methods-section statement."

Setup (5 min): Instructor assigns 5 students to argue FOR and 5 AGAINST. Each side gets 5 minutes to prepare arguments using laptops. Instructor provides a one-paragraph case summary for each side.
Opening statements (6 min): Each side delivers a 3-minute opening statement (one spokesperson, but anyone can speak).
Rebuttals (8 min): 4 minutes per side. Instructor enforces time strictly.
Open floor (10 min): Any student may speak; instructor cold-calls quieter students.
Vote and debrief (6 min): Anonymous re-vote; reveal whether opinions shifted; instructor summarizes the actual APS/Nature policies as the practical resolution.

*Facilitation notes:* Prepare a one-page "briefing document" for each side before class (can be AI-generated, which is itself a teaching moment). If debate stalls, inject: "What if the figure looks identical to what a human would draw — does that change your answer?" Debrief by noting that the field is actively unsettled and students should default to over-disclosure for now.

*Materials needed:* One-page briefing documents for each side; timer; APS and Nature policy pages bookmarked

---

#### Meeting 2 — In-Class Peer Code Review

**Student Introduction** (assigned: S6) [EDIT: S6 confirmed correct per rotation table]
> *Format:* 8-minute chalk talk
>
> **Topic prompt:** Prepare an 8-minute chalk talk (no notes, whiteboard only) on how to write an actionable code review comment for physics research code. Read Google's Engineering Practices Guide on code review (https://google.github.io/eng-practices/review/reviewer/) and adapt three principles specifically to the challenges of physics code — where the reviewer may not know the subdomain. At the whiteboard, present two concrete examples side by side: one actionable code review comment and one unhelpful comment (drawn from open-source physics repositories or fabricated). Explain specifically what makes one actionable and the other not. Connect to today's peer review exercise: students will post real inline comments on their partner's repository, and these principles govern what makes those comments useful. [EDIT: rewrote from note-style ("Topic:... Student should read... 3-5 sentences.") to directive format; removed template placeholder text]
>
> **Guiding questions:**
> 1. What makes a code review comment 'actionable' rather than just critical?
> 2. How do you review code for physical correctness when you may not know the reviewer's physics subdomain?
> 3. What is the difference between a blocking comment and a suggestion in a code review?

**Active Engagement** — Peer code review (45 minutes)

Pre-class setup: Assign review pairs before class (student A reviews student B's repo; student B reviews student A's repo). Share the review rubric (below) 48 hours before class so students can prepare.

In-class (45 min):
- Minutes 0-30: Each student opens their assigned partner's GitHub repository and writes inline comments directly in a GitHub PR or as a structured markdown review document. The rubric has four sections: (1) Can I reproduce the main result from the README alone? (2) Are all random seeds and API keys handled correctly? (3) Is every quantitative claim in the code traceable to a specific output? (4) Is AI tool use documented?
- Minutes 30-40: Partners meet for 10 minutes. The reviewer explains their top 3 findings; the author clarifies intent for any comments they disagree with.
- Minutes 40-45: Each reviewer shares their single most important finding with the class (1 min each, round-robin).

*Facilitation notes:* Circulate during the review period — ask each student "What's the most confusing thing you've encountered so far?" to surface common issues across projects. If a student finishes early, have them write a second pass focusing only on the provenance.json file. Remind students that the goal is to help their partner, not to score points. After class, collect all review documents and grade them for depth and constructiveness.

*Materials needed:* GitHub access for all students; review rubric printed or shared digitally; laptops required

---

#### Homework Assignment 10: Ethics Statement and Peer Review Submission

**Assessment category:** Peer Review & Participation | **Estimated time:** 4-6 hours (2-3 hr review + 1-2 hr ethics statement) | **Due:** Peer review submitted before Week 11 Meeting 1; review responses due before Week 12 Meeting 1 (graded in Week 12 participation/reproducibility rubric)

**Background:** Building on the structured logging and observability infrastructure added in Week 9, this week pivots to the social and ethical dimensions of AI-assisted research: what you must disclose about how that pipeline was built, and what a peer reviewer should be able to verify. [EDIT: added "building on Week 9" narrative arc bridge] Transparency about AI tool use is now a professional expectation in physics research, and peer code review is how the community maintains reproducibility standards. This week you will write the ethics and limitations statement that will appear in your final paper, and submit your written peer review of your partner's codebase.

**Instructions:**
1. Write an 'AI Tools and Ethics' statement (300-500 words) for your project. The statement must specify: (a) which AI tools you used (name and version, e.g., 'Claude claude-3-5-sonnet-20241022 via the Anthropic API'); (b) what each tool was used for (e.g., 'code generation', 'prose improvement', 'data analysis'); (c) how you verified the AI's outputs (e.g., 'all numerical results were cross-checked against the baseline model from Week 7'); (d) any limitations of your AI use that a reader should know. Save as ethics_statement_<lastname>.md.
2. Submit your written peer code review as a GitHub PR review on your partner's repository or as a structured markdown document (peer_review_<reviewer_lastname>_reviews_<author_lastname>.md). The review must include: at least 5 inline comments at specific line numbers, one comment in each of the four rubric categories, and at least one 'blocking' issue (something that must be fixed for reproducibility) with a specific proposed fix.
3. Respond to all comments in your partner's review of your code. For each comment: either implement the fix and reference the commit, or explain in writing (in the PR thread or a REVIEW_RESPONSES.md file) why you chose not to. This response is due before Week 12 Meeting 1 and is graded in Week 12 under the participation/reproducibility rubric (not Week 10).

**Deliverables:**
- ethics_statement_<lastname>.md — AI tools and ethics statement (300-500 words)
- peer_review_<reviewer_lastname>_reviews_<author_lastname>.md or GitHub PR review with at least 5 inline comments
- REVIEW_RESPONSES.md — written responses to all blocking peer review comments received in Week 10, due before Week 12 Meeting 1

**Grading criteria:**

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Depth of technical feedback | 40% | The review includes at least 5 inline comments at specific line numbers, covers all four rubric categories, and the blocking issue includes a specific proposed fix (not just 'fix this'). Week 10 scoring covers the review artifact itself; Step 3 author response scoring is deferred to Week 12 participation/reproducibility grading. |
| Constructive tone | 30% | All comments are phrased as suggestions or questions rather than criticism; the review explains why each issue matters for reproducibility or correctness. |
| Ethics statement quality | 30% | The statement names specific AI tools with versions, describes their use with enough detail for a reader to assess impact on the results, and acknowledges at least one genuine limitation. |

**Tools and resources:**
- GitHub Pull Request review interface for inline comments
- APS Statement on the Use of AI in Physics Research (https://www.aps.org/policy/statements)
- Nature portfolio AI use policy (https://www.nature.com/articles/d41586-023-00191-1)
- Google Engineering Practices — Code Review (https://google.github.io/eng-practices/review/reviewer/)

---

### Week 11: Seminar / Reading Group Part 1

#### Meeting 1 — Reading Group Session A

**Student Introduction** (assigned: S2) [EDIT: corrected from S7; rotation table and summary both assign S2 to 11M1]
> *Format:* 15-minute paper discussion (whiteboard outline, no slides required)
>
> **Topic prompt:** You will lead a 15-minute discussion of a paper directly relevant to your project. Select a paper published in the last 3 years that uses an AI or ML method central to your research question. Prepare a structured presentation covering: (1) the physical problem being solved; (2) the AI method used and why it was chosen; (3) the evaluation approach and its adequacy; (4) one specific finding you will apply or adapt in your own project; (5) one weakness or open question in the paper. Prepare 3 discussion questions for the class. You do not need slides — a whiteboard outline is sufficient.
>
> **Guiding questions:**
> 1. What physical problem does this paper solve, and how does the AI method address it?
> 2. Is the evaluation rigorous enough to trust the paper's main claim?
> 3. What would you do differently, and how does this paper inform your own project?

**Active Engagement** — Socratic seminar (55 minutes)

The hour is structured as follows:
Minutes 0-15: First student leads their paper discussion using their prepared outline and 3 questions.
Minutes 15-30: Second student leads their paper discussion (same format).
Minutes 30-50: Structured synthesis discussion. Instructor asks: "What evaluation patterns appeared in both papers? What would a skeptical Physical Review referee ask about either paper?" Students respond in structured rounds — no one speaks twice until everyone has spoken once.
Minutes 50-60: Each student writes one sentence on a notecard: "The one thing I will change about my own evaluation approach based on today's discussion is ___." Cards are collected and anonymized summaries shared next class.

*Facilitation notes:* Assign the two paper leaders at least one week in advance. Ask them to share their paper with the class 48 hours before the meeting. During the synthesis discussion, keep a running list on the whiteboard of "evaluation patterns" and "open referee questions" — this serves as a study guide for the showcase. If discussion stalls, project a specific figure from one of the papers and ask "How would you reproduce this figure from a fresh clone of the code?"

*Materials needed:* Whiteboard; papers shared digitally 48 hours in advance; index cards for synthesis round

---

#### Meeting 2 — Reading Group Session B

**Student Introduction** (assigned: S7) [EDIT: corrected from S8; rotation table and summary both assign S7 to 11M2]
> *Format:* 15-minute paper discussion (whiteboard outline)
>
> **Topic prompt:** You will lead a 15-minute discussion of a paper directly relevant to your project. Select a paper that uses a different AI method than the Week 11 Meeting 1 papers (to maximize class exposure to diverse approaches). Prepare the same structured outline as Meeting 1 leaders: physical problem, AI method, evaluation, what you will adapt, one weakness, and 3 discussion questions. Post your paper to the course repo 48 hours in advance.
>
> **Guiding questions:**
> 1. How does this paper's AI method differ from those discussed in Meeting 1, and when would you choose one over the other?
> 2. What caveats would you add to the abstract if you were a co-author?
> 3. What single experiment would most strengthen this paper's main claim?

**Active Engagement** — Structured debate (55 minutes)

Minutes 0-15: Third student leads their paper discussion.
Minutes 15-30: Fourth student leads their paper discussion.
Minutes 30-55: Structured debate on the motion: "The results section of an AI-in-physics paper should always include a comparison to a non-AI baseline, even if the baseline is trivially worse."

Setup (3 min): Instructor assigns 5 students FOR, 5 AGAINST (not the paper leaders for this round).
Opening statements (6 min): 3 min per side.
Rebuttals (8 min): 4 min per side.
Open floor (8 min): Free discussion; instructor injects: "What if the baseline is 100× more expensive to compute than the AI method?"
Vote and debrief (5 min): Reveal actual Physical Review Data guidelines on baselines.

*Facilitation notes:* The debate motion is intentionally provocative — most students will initially vote FOR. The AGAINST side often argues for computational cost exceptions, which is a genuine research tradeoff. Prepare the Physical Review Data author guidelines (https://journals.aps.org/prd/authors) as the authoritative reference for the debrief. Assign sides before class to ensure balance.

*Materials needed:* Papers shared 48 hours in advance; PRD author guidelines bookmarked

---

#### Homework Assignment 11: Draft Results Section and Reading Group Summary

**Assessment category:** Peer Review & Participation | **Estimated time:** 5-7 hours | **Due:** Before the first class meeting of Week 12

**Background:** With the peer code review from Week 10 complete and reviewer feedback in hand, this week turns to translating your pipeline's outputs into scientific prose. [EDIT: added "building on Week 10" narrative arc bridge] Writing a results section for AI-assisted physics research requires translating stochastic model outputs into physical claims with appropriate uncertainty. This week you will produce a draft results section that will receive peer feedback before the final paper deadline, and you will document the reading group discussion to help the class build a shared knowledge base.

**Instructions:**
1. Write a draft results section (600-900 words) for your project paper in RevTeX format (results_draft_<lastname>.tex). The section must: (a) report your primary evaluation metric with a numeric value and uncertainty estimate (e.g., 'MAE = 0.08 ± 0.02 eV, compared to the DFT baseline of 0.31 ± 0.05 eV'); (b) include at least one figure (saved as results_fig1_<lastname>.pdf) showing the AI output vs. baseline or ground truth; (c) state explicitly what each AI-generated quantity represents physically; (d) note at least one result that was unexpected or inconsistent with prior work.
2. Write a 300-word reading group summary (reading_group_summary_<lastname>.md) covering the two papers discussed in the meeting you attended. For each paper: state the main claim in one sentence, identify the strongest and weakest aspect of the evaluation, and write one question you would ask the authors. Commit the summary to the course repository before the next class.
3. Draft written responses to two skeptical reviewer questions about your AI methodology (use the most challenging questions raised during the Week 11 reading group discussions if possible). [EDIT: vague "Formulate written responses" replaced with "Draft" plus a specific source for the questions] Write these as you would in a rebuttal letter (reviewer_response_<lastname>.md): quote the hypothetical reviewer comment, then write a 100-150 word response citing your evaluation protocol, baseline comparison, and reproducibility controls.

**Deliverables:**
- results_draft_<lastname>.tex — draft results section in RevTeX
- results_fig1_<lastname>.pdf — figure showing AI output vs. baseline or ground truth
- reading_group_summary_<lastname>.md — 300-word summary of two papers (committed to course repo)
- reviewer_response_<lastname>.md — responses to two hypothetical skeptical reviewer questions

**Grading criteria:**

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Discussion engagement | 30% | Student contributes at least two substantive new points during the reading group (not just agreeing or restating); paper leaders receive full credit for leading their discussion with the required structure. |
| Results section quality | 40% | The draft results section reports the evaluation metric with uncertainty, includes a figure comparing AI to baseline, and explicitly interprets each quantity in physical terms. |
| Reading group summary | 15% | The summary addresses all required points for both papers and is committed to the course repo before the next class. |
| Reviewer response quality | 15% | Each response is 100-150 words, cites specific evidence from the project (evaluation metric, baseline comparison, reproducibility controls), and directly addresses the hypothetical concern. |

**Tools and resources:**
- RevTeX 4.2 (or Overleaf for online editing)
- matplotlib with publication-quality defaults (plt.rcParams update)
- Semantic Scholar or Google Scholar for paper discovery
- APS Physical Review Data author guidelines (https://journals.aps.org/prd/authors)

---

### Week 12: Seminar / Reading Group Part 2

#### Meeting 1 — Advanced & Cross-Cutting AI-in-Physics Reading Group

**Student Introduction** (assigned: S3 & S4) [EDIT: corrected from S9; rotation table and summary both assign S3 and S4 to 12M1 as a joint two-student slot]
> *Format:* 15-minute paper discussion (whiteboard outline)
>
> **Topic prompt:** Each of the two students leads a 15-minute paper discussion on a cross-cutting or advanced AI-in-physics paper — one that addresses AI reproducibility or reliability at a field-wide scale rather than within a single method. Recommended papers (choose one each, or propose an alternative with instructor approval):
>   • Hutson, M. (2018). "Artificial intelligence faces reproducibility crisis." Science 359(6377):725-726. https://doi.org/10.1126/science.359.6377.725
>   • Kapoor, S. & Narayanan, A. (2023). "Leakage and the Reproducibility Crisis in ML-based Science." Patterns 4(9):100804. https://doi.org/10.1016/j.patter.2023.100804
> Each presenter should: (1) sketch the paper's main claim and evidence on the whiteboard; (2) locate a concrete example of the failure mode the paper describes in AI-in-physics literature; (3) propose one corrective practice the class could adopt today.
> Use the format "15-minute paper discussion (whiteboard outline)": draw the argument structure, not slides. No notes — you must be able to reproduce the paper's core logic from memory at the whiteboard.
>
> **Guiding questions:**
> 1. What specific evaluation or publication practice does this paper identify as the root cause of irreproducibility?
> 2. Does this failure mode apply to your own project? Where?
> 3. What would a reproducibility-passing version of the paper's worst-case example look like?

**Active Engagement** — Socratic seminar (45 minutes)

Synthesis discussion connecting all four papers discussed across Weeks 11 and 12. The goal is to surface shared evaluation patterns and open problems that cut across AI methods in physics.

Central question posed by the instructor at the start of the seminar:
"After four papers, what is the single most important thing the physics community should change about how it evaluates AI-generated results — and what would stop it from doing so?"

Structure (45 min):
- Round 1, "First responses" (12 min): Instructor cold-calls each student in turn for a 60-90 second response to the central question. No interruptions; other students take brief notes.
- Round 2, "Peer responses" (15 min): Each student may respond to a specific thing someone said in Round 1. Instructor enforces the rule that a student may not simply repeat their Round 1 point — they must engage with another student's idea.
- Round 3, "Convergence or divergence?" (10 min): Instructor asks: "Which two student positions from Round 1 are most in tension? Can they be reconciled?" Instructor facilitates direct dialogue between the two named students.
- Debrief (8 min): Instructor lists on the whiteboard the 2-3 key disagreements that were NOT resolved. These become optional essay prompts available for the final paper's discussion section.

Instructor follow-up probes (use if discussion stalls):
  • "Kapoor & Narayanan argue that leakage is the rule, not the exception. Does anyone disagree? What would falsify that claim for physics specifically?"
  • "Hutson wrote in 2018. Name one thing that has concretely improved since then, and one thing that has gotten worse."
  • "If you were a referee, which of today's papers would you reject for reproducibility reasons? Be specific."

No laptops during seminar. Students should bring the Week 11 and Week 12 papers with annotations.

*Facilitation notes:* Before Round 1, write each paper's title on the whiteboard so students can reference them by number. Cold-call by name — do not open to volunteers; equitable participation is especially important in a 10-person seminar where confident students can dominate. Keep a live whiteboard list of the key claims being made; update it between rounds. At the start of Round 2, point to two claims on the board that are in apparent tension and ask students to address the tension directly. If a student raises a genuinely novel point not captured on the board, add it; this signals that new ideas are welcome even late in the discussion. Reserve the final 2 minutes of the debrief to ask: "What single sentence would you add to your own limitations section because of today's discussion?"

*Materials needed:* Whiteboard and markers; printed or annotated digital copies of all four reading-group papers (Weeks 11 and 12); no laptops during seminar

---

#### Meeting 2 — In-Class Peer Code Review — Reproducibility Audit

**Student Introduction** (assigned: S10)
> *Format:* 8-minute chalk talk
>
> **Topic prompt:** Prepare an 8-minute chalk talk (no notes, whiteboard only) on what a complete, publication-ready README looks like for an AI-assisted physics project. Study the following resources before class: [EDIT: removed "Topic:" prefix; rewrote opening in directive format consistent with other week intros]
>   • "Art of README" (https://github.com/hackergrrl/art-of-readme) — read the full document.
>   • At least two READMEs from published AI-in-physics codebases on GitHub (e.g., from papers with code, https://paperswithcode.com, filtered to physics).
>   • The Software Sustainability Institute checklist for research software documentation (https://www.software.ac.uk/resources/guides).
> Your 8-minute chalk talk (no notes, whiteboard only) must cover exactly these five required elements of a publication-ready README:
>   1. Installation: exact commands from a clean environment (conda or venv, Python version pinned).
>   2. Data download: the exact command or URL to retrieve all input data, plus the expected file sizes or checksums.
>   3. Reproduction command: the single command that regenerates all figures in the paper (e.g., `make reproduce`).
>   4. Expected outputs: what the user should see — with numerical ranges or sha256 checksums for key output files.
>   5. Known failure modes: at least one documented situation in which the pipeline fails or gives wrong results, with a workaround.
> End your talk by posing this question to the room: "Of the five elements, which one is most commonly missing in physics code releases — and why?"
>
> **Guiding questions:**
> 1. Of the five README elements, which is most commonly missing in physics code releases — and why?
> 2. How do you write a reproduction command that works on hardware you don't control?
> 3. What is the difference between documenting a known failure mode and hiding it?

**Active Engagement** — Peer code review (45 minutes)

Second in-class peer code review session, focused entirely on reproducibility audit. This round uses a different partner pairing from Week 10 (rotate the assignment ring by two positions so no student reviews the same partner twice).

Pre-class setup: Instructor circulates the reproducibility audit checklist 48 hours before class. Each student must have their repository in a state where it could plausibly be reviewed by a stranger.

Reproducibility Audit Checklist (reviewer works through these in order):
  1. Clone test: Does `git clone <repo> && cd <repo> && pip install -r requirements.txt && make reproduce` complete without errors on a fresh environment? (If not: what is the first failure point?)
  2. Figure provenance: Is every figure that appears in the paper generated by a named, findable script? (Check each figure's caption for a filename or command.)
  3. Data provenance: Does provenance.json (or equivalent) cover all data sources with URLs, download dates, and file hashes?
  4. Secret hygiene: Are all API keys absent from committed files? Is a .env.example present with instructions for obtaining each key?
  5. Output stability: Do numerical outputs match the expected ranges or checksums documented in the README? (Run the reproduction command and compare.)

In-class structure (45 min):
- Minutes 0-30: Each reviewer works through the checklist against their assigned partner's repository. Write checklist findings as GitHub PR review comments (one comment per checklist item, minimum). Flag any item as PASS, PARTIAL, or FAIL with a one-sentence justification.
- Minutes 30-40: Reviewer-author pairs meet for 10 minutes. Reviewer walks through their FAIL and PARTIAL findings. Author asks clarifying questions and notes which issues they plan to fix before Week 13.
- Minutes 40-45: Round-robin share-out (1 min per student): each reviewer names the single checklist item their partner's repo failed or nearly failed, and the specific fix required.

After class: reviewer submits the completed checklist as a GitHub PR review or as a structured markdown file (reproducibility_audit_<reviewer_lastname>_reviews_<author_lastname>.md) within 24 hours.

*Facilitation notes:* Distribute the audit checklist as a printout at the start of class — even students who read it digitally benefit from a physical copy to mark up. During minutes 0-30, circulate and ask each reviewer "Which checklist item have you found to be the hardest to verify so far?" — this surfaces common gaps across projects and lets you intervene early. If a student's `make reproduce` fails immediately, help them get unstuck (one intervention of up to 3 minutes) rather than letting them spend the whole period debugging a trivial environment issue. Remind reviewers that a PARTIAL is not a pass: if a reproduction command exists but is not documented in the README, that is PARTIAL, not PASS. The round-robin share-out at the end creates a public record of what reproducibility gaps are common across the class — photograph or transcribe the board and post it to the course repository.

*Materials needed:* Reproducibility audit checklist (printed or shared digitally 48 hours before class); GitHub access for all students; laptops required; sha256sum available on each machine

---

#### Homework Assignment 12: Limitations Section, Review Responses, and Self-Audit

**Assessment category:** Peer Review & Participation | **Estimated time:** 4-6 hours (1-2 hr limitations section + 1-2 hr review responses + 1 hr self-audit) | **Due:** All three deliverables submitted before Week 13 Meeting 1; REVIEW_RESPONSES.md must be committed to the project repository (not submitted separately)

**Background:** With the second round of peer code review complete, your project is entering its final polishing phase. This week's homework has three mutually reinforcing tasks. First, you will write the limitations section of your final paper — the section that requires the most intellectual honesty because it asks you to characterize where your AI methods fail. Second, you will formally close out the Week 10 peer review cycle by resolving all blocking comments and documenting your decisions. Third, you will apply the Week 12 reproducibility audit checklist to your own repository before Week 13's final check, so you arrive at the final submission deadline without last-minute surprises.

**Instructions:**
1. Write the limitations section for your final paper in RevTeX (400-600 words, not counting any inline citations). The section must: (a) Identify at least two specific failure modes of the AI method(s) you used — not generic AI limitations, but limitations observable in your own results (e.g., "the retrieval step returns irrelevant abstracts when the query uses non-standard terminology, which we observed in 3 of 12 test queries on lattice QCD papers"). (b) Quantify the failure mode where possible (frequency, magnitude, or severity). (c) Describe what additional data, compute, or methodological change would be required to overcome each limitation. (d) Cite at least one paper from the Week 11 or Week 12 reading group that corroborates or contextualizes a limitation you describe. Save as limitations_<lastname>.tex. This section will be incorporated directly into the final paper.
2. Resolve all blocking comments from your Week 10 peer review. For each blocking comment: (a) Implement the fix and reference the fixing commit SHA in a REVIEW_RESPONSES.md file (e.g., "Resolved in commit abc1234: added sha256 checksum to README data download section"). (b) If you are not implementing a fix, document your decision with a one-paragraph justification in REVIEW_RESPONSES.md explaining why the comment does not apply or why the alternative approach is preferable. Every blocking comment must have an entry in REVIEW_RESPONSES.md. Non-blocking suggestions may be addressed at your discretion, but note which ones you chose to address and which you deferred.
3. Run the Week 12 reproducibility audit checklist (five items) against your own repository as a self-audit. For each checklist item, record your honest assessment (PASS, PARTIAL, or FAIL) and the specific evidence (e.g., the exact command you ran and its output). Submit this self-audit as self_audit_checklist_<lastname>.md. For any item you rated PARTIAL or FAIL, add a brief plan (1-3 sentences) describing what you will fix before the Week 14 final submission.

**Deliverables:**
- limitations_<lastname>.tex — limitations section in RevTeX (400-600 words)
- REVIEW_RESPONSES.md — responses to all Week 10 peer review comments (blocking comments fully resolved)
- self_audit_checklist_<lastname>.md — reproducibility self-audit with PASS/PARTIAL/FAIL per item and remediation plan for any non-PASS items

**Grading criteria:**

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Discussion engagement | 30% | Substantive contributions in both the reading group synthesis seminar (Meeting 1) and the review-pair debrief (Meeting 2); demonstrates having read and annotated the assigned papers before class. Assessed by in-class observation and post-class self-assessment form submitted within 24 hours. |
| Reproducibility audit quality | 35% | The self-audit checklist is complete (all five items addressed), honest (PARTIAL and FAIL ratings are not inflated to PASS), and identifies at least one genuine gap with a specific, actionable remediation plan. Reviewers' audit of their partner's repo is also graded here: at least one FAIL or PARTIAL must be documented with a line-level comment and a concrete fix. |
| Limitations section quality | 35% | Honestly describes at least two AI method failure modes with specific examples drawn from the student's own results (not generic AI criticism); at least one failure mode is quantified; at least one citation from the Week 11 or Week 12 reading group is incorporated; the section is 400-600 words in valid RevTeX. |

**Tools and resources:**
- RevTeX (document class revtex4-2) for the limitations section
- GitHub Pull Request interface for resolving and referencing review comments
- GNU Make for running the reproduction command during self-audit
- sha256sum for generating and verifying file checksums in the audit

---

### Week 13: Scientific Communication

#### Meeting 1 — Writing the AI-Assisted Physics Paper

**Student Introduction** (assigned: S5) [EDIT: corrected from S1; rotation table and summary both assign S5 to 13M1]
> *Format:* 8-minute paper presentation
>
> **Topic prompt:** Research and present how AI writing assistants (Claude, GPT-4, Grammarly) have been used in published physics papers — and where they went wrong. Find at least one published retraction or correction where AI-assisted writing introduced a factual error or hallucination. Present: (1) a brief taxonomy of legitimate vs. problematic AI writing assistance; (2) the specific failure case; (3) a practical workflow for using LLMs to improve clarity without distorting scientific claims (e.g., always show the LLM the underlying data before asking it to describe results). Limit to 8 minutes.
>
> **Guiding questions:**
> 1. What is the difference between using an LLM to fix grammar and using it to paraphrase a results sentence?
> 2. How do you verify that an LLM-improved sentence still accurately describes the underlying data?
> 3. What should an author disclose when they use an LLM to help write their abstract?

**Active Engagement** — Socratic seminar (45 minutes)

Central question: "If an LLM rewrites your results section and the rewritten version is clearer but slightly overstates the certainty of your findings, is that a scientific integrity violation or an editing error?"

Round 1 (8 min): Each student writes their answer on an index card (anonymous). Instructor reads 4-5 aloud.
Round 2 (15 min): Structured discussion. Instructor cold-calls: "What if you didn't notice the overstatement until after publication?" and "Does it matter whether the LLM or you wrote the overstatement?"
Round 3 (8 min): Students pair up and draft a 2-sentence policy for their own paper: "I will use LLMs for ___, and I will NOT use LLMs for ___."
Debrief (9 min): Pairs share their policies. Instructor synthesizes into a practical class consensus and posts it to the course repo.

*Facilitation notes:* Prepare a concrete example: take a real results sentence like "The model achieves 94.3% accuracy" and show 3 LLM rewrites with varying degrees of overstatement. Ask students to rank them by acceptability. This makes the abstract question concrete. End by sharing the ICML 2024 policy on LLM use as a reference point.

*Materials needed:* Index cards; projector showing the example results sentence and its LLM rewrites; ICML 2024 and APS AI policy bookmarked

---

#### Meeting 2 — Practice Showcase Presentations

**Student Introduction** (assigned: S7) [EDIT: corrected from S2; rotation table and summary both assign S7 to 13M2]
> *Format:* 10-minute slide presentation (max 6 slides) — 3 min demo + 7 min commentary
>
> **Topic prompt:** Prepare and deliver the opening 3 minutes of your showcase presentation as a demonstration model for the class. Your goal is to show what an effective opening looks like: a crisp motivation statement (why this physics problem matters), your specific research question stated in one sentence, and the key result in one sentence with a figure. After your demo, briefly explain the choices you made (why this opening, what you cut, what you emphasized). This is a teaching demonstration, not a performance — feel free to narrate your thinking.
>
> **Guiding questions:**
> 1. How do you state a specific AI-assisted research question to a mixed physics audience in one sentence?
> 2. What makes an opening figure compelling to a non-specialist?
> 3. What did you have to cut from your full talk to fit the 3-minute version, and how did you decide what to cut?

**Active Engagement** — Structured debate (55 minutes)

Each student delivers a 3-minute practice version of their showcase talk (motivation → question → key result → one conclusion). The class provides structured written feedback after each talk using a shared feedback form with four fields: (1) Was the research question clear after the first 60 seconds? (2) Was the key result stated with a number and its uncertainty? (3) Was the AI methodology explained at a level a non-AI physicist could evaluate? (4) One specific suggestion for improvement.

Timing: 3 min talk + 2 min for audience to fill in feedback form = 5 min per student × 10 students = 50 min total.
Final 5 min: Instructor synthesizes the most common feedback themes and states what the departmental audience will expect in Week 14.

*Facilitation notes:* Use a shared Google Form or paper form for structured feedback — collecting written feedback prevents the conversation from being dominated by one or two voices. After the session, compile all feedback for each student and email it to them before Week 14. Time talks strictly with a visible timer. Coach students who go over: "What's the one sentence your audience absolutely needs to hear?"

*Materials needed:* Shared feedback form (Google Form or printed copies); visible countdown timer; projector

---

#### Homework Assignment 13: Complete Paper Draft, Claim-Tracing Table, and Repository Tag

**Assessment category:** Final Project Codebase & Paper | **Estimated time:** 8-12 hours (the largest homework of the semester — plan accordingly) | **Due:** Before the first class meeting of Week 14 (final submission deadline)

**Background:** The Week 14 showcase is one week away. This homework produces the three artifacts that constitute your final submission: a complete paper draft, a claim-tracing table ensuring every number in your paper is reproducible, and a tagged repository release. Each artifact will be reviewed by the instructor before the showcase.

**Instructions:**
1. Assemble your complete paper draft in RevTeX (paper_draft_<lastname>.tex). All six sections must be present and substantive: Abstract (100 words max), Introduction (motivation and research question), Methods (AI tools, MCP server, evaluation protocol — sufficient for a reader to reproduce your approach), Results (from your Week 11 draft, revised based on peer comments), Discussion (interpretation, comparison to baseline, limitations from Week 12), Conclusion (one paragraph). Compile to PDF and confirm it is 4-6 pages excluding references.
2. Build a claim-tracing table (claim_trace_<lastname>.md). For every quantitative claim in your Results and Discussion sections, record: (a) the exact quoted sentence from the paper, (b) the notebook filename and cell number that produces the number, (c) the command to run that cell in isolation (e.g., 'jupyter nbconvert --to script results.ipynb && python results.py --cell 12'), and (d) the expected output value or range. The table must have at least 5 entries.
3. Use Claude or GPT-4 to improve the clarity of your Abstract and Introduction by pasting each section into the model with the following prompt: "Improve the clarity and scientific precision of this physics paper section without changing any quantitative claims, adding new scientific assertions, or weakening any stated uncertainties. Return only the revised text." [EDIT: vague "improve the clarity" replaced with a specific, copy-pasteable prompt instruction that guards against overstatement] Save the original sections as abstract_original_<lastname>.txt and the LLM-improved version as abstract_llm_<lastname>.txt. Write a 200-word reflection (llm_writing_reflection_<lastname>.md) explaining: what you changed, what you rejected, and whether the LLM introduced any inaccuracies you had to correct.
4. Tag your GitHub repository with the version tag v0.9-draft using 'git tag v0.9-draft && git push origin v0.9-draft'. Confirm the tag is visible on GitHub. The tagged commit must include your data pipeline, the main analysis notebook, provenance.json, REPRODUCIBILITY.md, and the paper draft PDF.

**Deliverables:**
- paper_draft_<lastname>.tex and paper_draft_<lastname>.pdf — complete 4-6 page paper draft
- claim_trace_<lastname>.md — claim-tracing table with at least 5 entries
- abstract_original_<lastname>.txt, abstract_llm_<lastname>.txt, and llm_writing_reflection_<lastname>.md — LLM writing comparison
- GitHub repository tag v0.9-draft visible on GitHub with all required files committed

**Grading criteria:**

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Paper completeness | 40% | All six sections are present and substantive; the paper is 4-6 pages in RevTeX; the Results section reports at least one metric with uncertainty. |
| Claim traceability | 30% | Every quantitative claim in the paper has a corresponding entry in the claim-tracing table with a working reproduction command. |
| LLM writing reflection | 15% | The reflection identifies at least one specific inaccuracy or overstatement the LLM introduced and explains how it was corrected. |
| Repository tag | 15% | The v0.9-draft tag exists on GitHub and the tagged commit includes all required files. |

**Tools and resources:**
- RevTeX 4.2 or Overleaf
- Claude or GPT-4 for writing assistance (document your prompts)
- jupyter nbconvert for converting notebooks to scripts
- git tag for creating repository releases
- GitHub Releases interface as an alternative to command-line tagging

---

### Week 14: Showcase & Wrap-Up

#### Meeting 1 — Final Submission and Adversarial Q&A Rehearsal

**Student Introduction** (assigned: S6) [EDIT: corrected from S3; rotation table and summary both assign S6 to 14M1]
> *Format:* 8-minute chalk talk
>
> **Topic prompt:** Reflect on the 14-week course arc in a forward-looking synthesis, not a recap: what has changed in AI capabilities for physics research since the course began? Find one AI-in-physics development from the past month (a preprint, tool release, or policy change) and present it as a "course update" — what would we cover differently if the course started today? Your chalk talk must be delivered from the whiteboard with no notes; connect the new development explicitly to one topic from Phase 1 or Phase 2 that it would change, extend, or supersede. [EDIT: removed "3-5 sentences." template placeholder; integrated "This is a forward-looking synthesis" note into the prose directive]
>
> **Guiding questions:**
> 1. What is the single most important thing you learned about AI's role in physics research that you did not know at the start of the course?
> 2. What capability or tool released in the last month would have changed how you designed your project?
> 3. What question about AI in physics research do you now have that you did not know to ask in Week 1?

**Active Engagement** — Socratic seminar (55 minutes)

Adversarial Q&A rehearsal. Each student has 5 minutes total: 2 minutes to state their project's main result in plain language (no slides), then 3 minutes of adversarial questions from the instructor and class playing the role of a skeptical physics faculty audience.

Instructor prepares a question bank before class — one tailored question per student targeting their most vulnerable methodological choice (e.g., "Why did you trust the LLM's output here rather than computing it directly?", "Your baseline is linear regression — why not a physics-informed neural network?", "How do you know this result isn't a hallucination that happens to match your test set?").

After all 10 students have gone (50 min), 10-minute debrief: what questions surprised you? What answers felt strongest? Instructor previews what faculty will likely ask at the showcase.

*Facilitation notes:* Prepare the tailored question bank by reading all paper drafts before this meeting. The goal is not to embarrass students but to surface real vulnerabilities they can address before the showcase. Give students 48 hours notice that this format will be adversarial so they can prepare. After class, email each student their tailored question and a suggested response approach.

*Materials needed:* Instructor question bank (one tailored question per student, prepared from paper drafts); no slides needed from students

---

#### Meeting 2 — Departmental Showcase

**Student Introduction** (assigned: ALL)
> *Format:* 10-minute showcase presentation (≤12 slides) + 5-minute Q&A per student
>
> **Topic prompt:** Each student delivers a 10-minute showcase presentation to a departmental audience (faculty, other graduate students, and invited guests), followed by 5 minutes of open Q&A. Your presentation must cover: motivation and research question (2 min), methods including AI tools and MCP server (3 min), results with evaluation against baseline (3 min), conclusions and limitations (2 min). Every quantitative result must appear on a slide with its uncertainty and a brief statement of how it was validated. Prepare for adversarial questions about your AI methodology — reviewers will probe whether results could be hallucinations or artifacts.
>
> **Guiding questions:**
> 1. Can you explain your main result and its significance in two sentences to a physicist who has never used an LLM?
> 2. What is the strongest evidence that your AI output is correct and not a plausible-looking hallucination?
> 3. If you had one more month, what would you do to strengthen your main claim?

**Active Engagement** — Structured debate (50 minutes presentations + 10 minutes retrospective = 60 minutes)

Showcase presentations (50 min for 10 students at 10+5 min each; may be extended if the showcase is held in a larger venue with more Q&A time).

After all presentations (final 10 min): Course retrospective. Instructor asks three questions in sequence; students respond popcorn-style (anyone can speak, no repeating what was said):
(1) "What is the one AI tool or technique from this course you will still be using in your research five years from now?"
(2) "What is the one thing about AI in physics research that turned out to be much harder than you expected?"
(3) "What would you tell a first-year graduate student who is considering this course next year?"

Instructor closes with a brief reflection on how AI capabilities have evolved even over the 14 weeks of the course, and what that means for physics research going forward.

*Facilitation notes:* Coordinate with the department to secure a larger room and invite faculty at least two weeks in advance. Assign a student timekeeper with a visible 2-minute warning signal. After the retrospective, take a group photo. Collect all showcase slide decks and post them to the course repository with student permission. Send a thank-you email to faculty attendees with links to students' GitHub repositories.

*Materials needed:* Departmental presentation room; projector; student slide decks submitted 24 hours in advance; visible timer; faculty invited 2 weeks in advance

---

#### Homework Assignment 14: Final Project Codebase, Paper, and Showcase Presentation

**Assessment category:** Final Project Codebase & Paper (25%) and Departmental Showcase Presentation (25%) | **Estimated time:** No new work this week — all deliverables assembled from previous weeks | **Due:** Final paper and repository tag due before Meeting 1 of Week 14; slides due 24 hours before Meeting 2

**Background:** Week 14 has no new assignment — the semester's work culminates in two final deliverables that together constitute 50% of your course grade. The final codebase and paper represent the scientific contribution; the showcase presentation is your public defense of that contribution. Both are due before Meeting 1 of Week 14.

**Instructions:**
1. Submit your final paper as a compiled PDF (paper_final_<lastname>.pdf) via the course submission portal or by emailing the instructor. The paper must be 4-6 pages in RevTeX, include all six sections (Abstract, Introduction, Methods, Results, Discussion, Conclusion), report at least one evaluation metric with uncertainty, and include an AI Tools & Ethics statement. The paper must compile from source using 'pdflatex paper_final_<lastname>.tex' with no errors.
2. Starting from your Week 13 v0.9-draft tag, refine the repository and then tag the final state as v1.0-final using 'git tag v1.0-final && git push origin v1.0-final'. The tagged commit must include: all analysis notebooks, data_pipeline_<lastname>.py, provenance.json, REPRODUCIBILITY.md, BUG_LOG.md, claim_trace_<lastname>.md, a complete README with a one-command reproduction instruction, requirements.txt or environment.yml, and the compiled paper PDF.
3. Submit your showcase slide deck (slides_final_<lastname>.pdf, ≤12 slides) at least 24 hours before Meeting 2. Slides must include: a title slide with your research question, at least one figure showing your key result vs. the baseline with uncertainty bars, and a final slide stating your main conclusion and one open question.
4. Deliver your 10-minute showcase presentation in Meeting 2. Speak to the slides you submitted; do not read from them. Be prepared to answer adversarial questions about your AI methodology. After the Q&A, submit a one-page self-assessment (self_assessment_<lastname>.md) within 48 hours of the showcase: state your strongest result, your biggest methodological limitation, and one specific thing you would do differently.

**Deliverables:**
- paper_final_<lastname>.pdf — final 4-6 page RevTeX paper
- GitHub repository tagged v1.0-final with all required files
- slides_final_<lastname>.pdf — showcase slide deck (≤12 slides, submitted 24 hr before showcase)
- self_assessment_<lastname>.md — one-page self-assessment submitted within 48 hours of the showcase

**Grading criteria:**

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Reproducibility (Codebase & Paper — 25%) | 30% | Running 'git clone && pip install -r requirements.txt && make reproduce' from a fresh environment produces the main result figure and matches the value reported in the paper within stated uncertainty. |
| Physical interpretation (Codebase & Paper — 25%) | 30% | Every AI-generated quantity in the paper is explicitly interpreted in physical terms with units and uncertainty; at least one result is compared quantitatively to a non-AI baseline or literature value. |
| Clarity of narrative (Showcase — 25%) | 20% | A physics faculty member unfamiliar with the student's subfield can follow the talk from motivation to conclusion without prior briefing; the research question is stated in the first 2 minutes. |
| Defensibility of AI claims (Showcase — 25%) | 20% | The student answers at least two adversarial questions about their AI methodology with specific evidence (citing evaluation metric, baseline comparison, or reproducibility controls) rather than general assurances. |

**Tools and resources:**
- git tag and git push origin for creating the final repository release
- pdflatex or Overleaf for compiling the final paper
- GNU Make for the one-command reproduction target
- GitHub Releases page to verify the v1.0-final tag is publicly visible

---

## Appendix A: Grading Rubrics Summary

| Assessment Category | Weight | Primary Weeks | Key Criteria |
|--------------------|--------|---------------|-------------|
| Standard Curriculum Mini-Assignments | 20% | 1–4 | Methodology correctness (30%), Reproducibility (25%), Physical plausibility (25%), Code clarity (20%) |
| Project Proposal & Pitch | 15% | 5 | Research question clarity (35%), Feasibility (30%), Pitch delivery (20%), Written proposal quality (15%) |
| Peer Review & Participation | 15% | 10–12 | Depth of technical feedback (40%), Constructive tone (30%), Discussion engagement (30%) |
| Final Project Codebase & Paper | 25% | 6–9, 13–14 | Reproducibility (30%), Physical interpretation (30%), Academic writing quality (25%), Code documentation (15%) |
| Departmental Showcase Presentation | 25% | 14 | Clarity of narrative (30%), Defensibility of AI claims (35%), Q&A handling (25%), Visual presentation (10%) |

---

## Appendix B: Tools and Resources Reference

### Python Libraries

- anthropic (Python SDK) — `pip install anthropic`; docs at https://docs.anthropic.com/en/api/getting-started
- arxiv — `pip install arxiv`; for fetching abstracts from the arXiv API
- astroquery — `pip install astroquery`; for SIMBAD, VizieR, and NASA ADS access
- diskcache — local disk caching for API responses
- faiss-cpu — `pip install faiss-cpu`; vector indexing and retrieval (IndexFlatIP)
- jupyter nbconvert — for converting notebooks to runnable scripts
- langchain / llama-index — optional RAG pipeline wiring (langchain, llama-index)
- litellm — `pip install litellm`; free-tier fallback via Groq with OpenAI-compatible interface
- matplotlib — `pip install matplotlib`; publication-quality plotting (matplotlib >= 3.7); use with seaborn and plt.rcParams update
- mcp (Python SDK) — `pip install mcp`; Model Context Protocol server implementation
- mp-api — Materials Project API client for crystal structure and property data
- numpy — `pip install numpy`; numerical arrays (numpy >= 1.24)
- pandas — data normalization and tabular data handling
- pyarrow — Parquet file output for data pipelines
- pytest / pytest-nbmake / pytest-recording (vcr.py) — testing frameworks including notebook testing and API call mocking
- python-dotenv — `pip install python-dotenv`; secret management via `.env` files
- python-json-logger — `pip install python-json-logger`; structured JSON logging for pipeline observability
- PySR — symbolic regression library
- scikit-learn — baseline models (linear regression, k-NN, SVR)
- scipy — `pip install scipy`; scientific computing (scipy >= 1.10)
- sentence-transformers — `SentenceTransformer('all-MiniLM-L6-v2')` for embedding generation
- sha256sum — command-line tool for generating and verifying file checksums
- sympy — symbolic computation
- tenacity — `pip install tenacity`; retry logic with exponential backoff for API calls
- tiktoken — `pip install tiktoken`; token counting for OpenAI models
- uncertainties — uncertainty propagation in baseline metrics
- MAPIE / nonconformist — conformal prediction baselines

### APIs and Databases

- arXiv API — https://info.arxiv.org/help/api/index.html; for programmatic access to preprints
- Materials Project — https://materialsproject.org; crystal structure and property database (access via mp-api)
- NASA ADS — Astrophysics Data System; accessible via astroquery
- NIST Physical Reference Data — https://physics.nist.gov/PhysRefData; constants and atomic data
- PDG Particle Data Group — https://pdg.lbl.gov; known particle physics values
- SIMBAD / VizieR — astronomical object database and catalogue service; accessible via astroquery at https://simbad.cds.unistra.fr/simbad/
- Semantic Scholar / Google Scholar — for literature discovery and paper search

### AI Tools and Services

- Anthropic API / Claude (claude-3-5-sonnet-20241022 and other models) — https://claude.ai; free tier available; also accessible via https://claude.ai
- GitHub Copilot — AI code completion; available via GitHub Education Pack or course license
- GPT-4 / OpenAI API — `pip install openai>=1.0`; quickstart at https://platform.openai.com/docs/quickstart
- litellm / Groq (free-tier LLM access) — OpenAI-compatible interface at no cost

### Papers and References

- APS Statement on the Use of AI in Physics Research — https://www.aps.org/policy/statements
- APS Physical Review Data author guidelines — https://journals.aps.org/prd/authors
- Anthropic blog: "Introducing the Model Context Protocol" (November 2024)
- arXiv:2011.09961 — Pineau et al. (2021), "Improving Reproducibility in ML Research"
- arXiv:2104.08663 — Thakur et al. (2021), BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models
- arXiv:2210.03629 — Yao et al., ReAct: Synergizing Reasoning and Acting in Language Models
- arXiv:2304.13187 — Poldrack et al., AI coding failure modes (background on LLM coding pitfalls)
- Griffiths, D.J. "Introduction to Quantum Mechanics" (3rd ed.) — Chapter 2 (sections 2.3–2.4) for harmonic oscillator energy levels and wavefunctions
- Hutson, M. (2018). "Artificial intelligence faces reproducibility crisis." Science 359(6377):725-726. https://doi.org/10.1126/science.359.6377.725
- ICML 2024 policy on LLM use in research submissions
- Kapoor, S. & Narayanan, A. (2023). "Leakage and the Reproducibility Crisis in ML-based Science." Patterns 4(9):100804. https://doi.org/10.1016/j.patter.2023.100804
- MCP specification — https://modelcontextprotocol.io/specification
- Nature portfolio AI use policy — https://www.nature.com/articles/d41586-023-00191-1

### Writing and Document Tools

- draw.io (https://diagrams.net) — graphical architecture and flowchart diagrams
- git tag / GitHub Releases — for creating versioned repository releases (`git tag v1.0-final && git push origin v1.0-final`)
- GNU Make — defining reproduction commands as Makefile targets (`make reproduce`)
- Google Engineering Practices — Code Review guide: https://google.github.io/eng-practices/review/reviewer/
- Mermaid (https://mermaid.js.org) — code-based flowchart diagrams
- Overleaf — free online LaTeX editor; alternative to local RevTeX installation
- pdflatex — local LaTeX compilation (`pdflatex paper_final_<lastname>.tex`)
- RevTeX 4.2 (document class revtex4-2) — APS journal format; install via TeX Live or MikTeX

---

*This course guide was assembled by an agent fleet from structured week specifications. Last updated: 2026-07-28.*
