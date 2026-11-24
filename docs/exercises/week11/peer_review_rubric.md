# Week 11 Meeting 2 — Peer Code Review Rubric

Use this rubric for the in-class review (30 min) and for the written review you submit in Homework 11.

**You review:** your assigned partner's project repository as it stands at the start of class.
**Goal:** help your partner make the result reproducible by a stranger — not to score points.

## What your review must contain

| Requirement | Minimum |
|---|---|
| Inline comments tied to a file and line number | 5 |
| Comments per rubric category (A–D below) | 1 each |
| Blocking issues, each with a specific proposed fix | 1 |
| Overall summary (template at the end) | 1 |

Submit as a GitHub PR review on your partner's repository, or as `peer_review_<reviewer_lastname>_reviews_<author_lastname>.md`.

## Severity labels

Start every comment with one label.

| Label | Meaning | Author must |
|---|---|---|
| `[blocking]` | A stranger cannot reproduce or trust the main result until this is fixed | Fix it, or justify in writing why not |
| `[suggestion]` | Would improve clarity, robustness, or maintainability | Respond; fixing is optional |
| `[question]` | You cannot tell whether this is a problem | Answer |
| `[praise]` | Something done well that others should copy | — |

## Suggested time budget (30 min)

| Minutes | Activity |
|---|---|
| 0–8 | A — clone and attempt the reproduction command |
| 8–14 | B — seeds, randomness, secrets |
| 14–23 | C — trace the key result back to code and data |
| 23–27 | D — AI tool documentation |
| 27–30 | Write the summary; pick your top 3 findings |

If the reproduction in A fails, record the first failure point as a blocking comment and move on. Do not spend the session debugging your partner's environment.

---

## A. Can I reproduce the main result from the README alone?

Work only from the README. Do not ask your partner for help; every question you would need to ask is a finding.

- [ ] The README states what the project computes and names the main result (figure or table).
- [ ] One documented command reproduces that result (e.g. `make reproduce` or a single script call).
- [ ] `requirements.txt` or `environment.yml` exists with pinned versions, and installs in a fresh environment.
- [ ] The Python version is stated.
- [ ] No hardcoded absolute paths or machine-specific settings.
- [ ] Required input data is committed, cached, or fetched by a documented step.
- [ ] Expected runtime and any API cost are stated.
- [ ] The command ran to completion for you. If not: the first failure point is recorded.
- [ ] The output you obtained matches the committed result (same numbers, or within a stated tolerance).

| Rating | Description |
|---|---|
| 3 — Reproducible | Fresh clone + README produces the main result with no outside help |
| 2 — Minor gaps | Works after one or two fixes you could work out yourself (e.g. a missing package) |
| 1 — Major gaps | Runs partially, or needs information that is not in the repository |
| 0 — Not reproducible | No reproduction command, or it fails with no clear path forward |

## B. Are random seeds and API keys handled correctly?

**Randomness**

- [ ] `REPRODUCIBILITY.md` exists and lists every source of randomness in the pipeline.
- [ ] Seeds are set in the code where the document says they are (check the actual lines).
- [ ] LLM calls use `temperature=0` or the lowest available setting, and the model name and version are pinned rather than an alias such as "latest".
- [ ] Remaining nondeterminism (LLM output drift, live API data, thread ordering) is acknowledged, with a mitigation such as cached responses.
- [ ] If time allows: two runs give identical output, or the differences are explained.

**Secrets**

- [ ] No API keys, tokens, or passwords in any committed file. Search the repository for `sk-`, `api_key`, `token`, `Bearer`.
- [ ] No secrets in the git history (`git log -p -S "api_key"` is a quick check), in notebook outputs, or in log files.
- [ ] `.env` is listed in `.gitignore`; `.env.example` is present and says how to obtain each key.
- [ ] Keys are read from environment variables, and a missing key gives a clear error message.
- [ ] Logged tool-call arguments are sanitized.

!!! warning "If you find a committed secret"
    Tell your partner directly and immediately — do not paste the key into a review comment. The key must be revoked; deleting it from the file is not enough because it remains in the git history.

| Rating | Description |
|---|---|
| 3 | All randomness documented and controlled; no secrets anywhere; `.env.example` complete |
| 2 | Seeds and secrets are handled, but documentation is incomplete or one source of randomness is missed |
| 1 | Seeds missing for a component that affects the main result, or secret handling is fragile |
| 0 | A secret is committed, or the results change between runs with no explanation |

## C. Is every quantitative claim traceable to a specific output?

Pick the single most important number or figure in the repository and follow it backwards: **claim → output file → script and line → input data → source**.

- [ ] Each number quoted in the README, notebooks, or draft paper is produced by a named script or notebook cell — not typed in by hand.
- [ ] Each committed figure or table has a generating script and command you can find.
- [ ] The log file from the run that produced the main result is committed, and its values agree with the reported result.
- [ ] The provenance file (`provenance_<lastname>.json`) covers every dataset used: source URL or endpoint, access timestamp, source version, transformations applied.
- [ ] Units are stated and consistent from raw data through to the reported value.
- [ ] Reported values carry an uncertainty, and the code that computes it is identifiable.
- [ ] Cuts, filters, and dropped records are visible in the code and logged, not silent.
- [ ] Any value produced by an LLM (extracted, summarized, or computed) is identifiable as such and has been checked against an independent source.
- [ ] Physics sanity check: the result has the right order of magnitude, sign, and limiting behaviour.

You may not know your partner's subfield. You can still check units, dimensions, limiting cases, and whether the code does what the comments and README say it does. Use `[question]` freely.

| Rating | Description |
|---|---|
| 3 | The chosen claim traces cleanly from statement to source data; provenance is complete |
| 2 | Traceable, but with one undocumented step or an incomplete provenance entry |
| 1 | The chain breaks: a value appears whose origin you cannot find |
| 0 | Results cannot be connected to code or data |

## D. Is AI tool use documented?

- [ ] The repository states which AI tools were used, with name and version, in the README or an AI tools / ethics statement.
- [ ] For each tool, the purpose is stated: code generation, prose, data analysis, literature search.
- [ ] Substantially AI-generated code is identifiable (comment, commit message, or a list in the statement).
- [ ] The statement says how AI output was verified: tests, comparison with a baseline, manual derivation.
- [ ] Prompts that directly produce results are committed (prompt files, or logged with the run).
- [ ] The model identifiers named in the documentation match the ones in the code and logs.
- [ ] `BUG_LOG.md` records any AI-introduced bugs that were found, with the failure-mode category.
- [ ] At least one genuine limitation of the AI use is acknowledged.

The ethics statement is due with Homework 11, so it may still be a draft. Review what is there and say what is missing.

| Rating | Description |
|---|---|
| 3 | A reader can tell which results depend on AI output and how that output was verified |
| 2 | Tools and purposes are listed, but verification is vague or versions are missing |
| 1 | AI use is mentioned only in general terms |
| 0 | No documentation of AI use |

---

## Writing an actionable comment

Each comment should contain four things: **label, observation, why it matters, proposed fix.**

| | Example |
|---|---|
| Not actionable | "Seeds are a mess." |
| Actionable | "`[blocking]` `data_pipeline.py` line 42: `np.random.shuffle(idx)` runs before any seed is set, so the train/test split differs on each run and the reported score will not reproduce. Suggest creating `rng = np.random.default_rng(42)` at the top of `main()` and calling `rng.shuffle(idx)`." |

- Describe the code, not the author.
- Say *why* the issue matters for reproducibility or correctness.
- Phrase uncertain points as questions.
- Include at least one `[praise]` comment.

## Summary template

Copy this to the top of your review.

```markdown
## Peer review summary

- Reviewer:
- Author / repository:
- Commit reviewed (SHA):
- Reproduction attempted: yes / no — outcome:

| Category | Rating (0–3) | One-line justification |
|---|---|---|
| A. Reproducibility from README | | |
| B. Seeds and API keys | | |
| C. Traceability of claims | | |
| D. AI tool documentation | | |

### Blocking issues
1. <file:line> — <issue> — <proposed fix>

### Top 3 findings (to discuss with the author)
1.
2.
3.

### What works well
-
```

The 0–3 ratings are feedback for the author and do not enter their grade. Your review is graded on depth and constructive tone (see the Homework 11 grading criteria).
