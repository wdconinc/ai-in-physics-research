# Instructor Operations Runbook

This runbook converts all **39 BLOCKING** operational findings into executable tasks.

Status key: `TODO` (default), `IN PROGRESS`, `DONE`, `BLOCKED`.

## Pre-course Day 0

| ID | Week/Meeting | Task | Owner | Deadline | Depends On | Status |
|---|---|---|---|---|---|---|
| OP-01 | W1 M1 | Create `exercises/week01/meeting1_token_explorer.ipynb` | Course Staff | Day 0 (T-14d) | Week 1 activity spec | TODO |
| OP-02 | W1 M1 | Pre-test `exercises/week01/meeting1_token_explorer.ipynb` in student env | Instructor + TA | Day 0 (T-10d) | OP-01 | TODO |
| OP-03 | W2 M1 | Create `week02_buggy_harmonic_oscillator.py` | Course Staff | Day 0 (T-14d) | Week 2 bug list | TODO |
| OP-04 | W2 M1 | Pre-test `week02_buggy_harmonic_oscillator.py` in student env | TA | Day 0 (T-10d) | OP-03 | TODO |
| OP-05 | W2 M2 | Create `week02_test_driven_skeleton.ipynb` | Course Staff | Day 0 (T-14d) | Week 2 pytest plan | TODO |
| OP-06 | W2 M2 | Pre-run `week02_test_driven_skeleton.ipynb`; verify pytest setup | TA | Day 0 (T-10d) | OP-05 | TODO |
| OP-07 | W3 M1 | Create `week03_rag_skeleton.ipynb` | Course Staff | Day 0 (T-14d) | Week 3 RAG flow | TODO |
| OP-08 | W3 M1 | Create `week03_fallback_corpus.json` | Course Staff | Day 0 (T-14d) | Week 3 abstract schema | TODO |
| OP-09 | W3 M1 | Pre-test `week03_rag_skeleton.ipynb` in student env | TA | Day 0 (T-10d) | OP-07, OP-08 | TODO |
| OP-10 | W4 M1 | Create MCP skeleton repo (`mcp_skeleton/` with requirements + stubs) | Course Staff | Day 0 (T-14d) | MCP exercise spec | TODO |
| OP-11 | W4 M1 | Prepare pre-tested MCP client + cached SIMBAD fallback JSON | TA | Day 0 (T-10d) | OP-10 | TODO |
| OP-12 | W4 M1 | Pre-test MCP skeleton + verify SIMBAD availability | Instructor + TA | Day 0 (T-7d) | OP-10, OP-11 | TODO |
| OP-13 | W5 M2 | Prepare structured peer feedback form for pitches | Instructor | Day 0 (T-7d) | `instructor/forms/week05_proposal_feedback_form.md` | TODO |
| OP-14 | W5 M2 | Prepare instructor pitch evaluation sheet | Instructor | Day 0 (T-7d) | `instructor/forms/week05_pitch_evaluation_sheet.md` | TODO |
| OP-15 | W6 M1 | Create `skeleton_mcp_server.py` | Course Staff | Day 0 (T-14d) | Week 6 server spec | TODO |
| OP-16 | W6 M1 | Pre-test `skeleton_mcp_server.py` (`mcp`, `pint`) in student env | TA | Day 0 (T-7d) | OP-15 | TODO |
| OP-17 | W8 M2 | Create `multi_api_pipeline_broken.py` (3 planted bugs) | Course Staff | Day 0 (T-14d) | Week 8 debugging lab spec | TODO |
| OP-18 | W9 M1 | Create `agentic_bug_hunt.py` (3 planted failures) | Course Staff | Day 0 (T-14d) | Week 9 debugging lab spec | TODO |
| OP-19 | W10 M1 | Prepare debate brief FOR caption-level disclosure | Instructor | Day 0 (T-7d) | `instructor/debate-briefs/week10_ethics_debate_brief_for.md` | TODO |
| OP-20 | W10 M1 | Prepare debate brief AGAINST caption-level disclosure | Instructor | Day 0 (T-7d) | `instructor/debate-briefs/week10_ethics_debate_brief_against.md` | TODO |
| OP-21 | W10 M2 | Prepare peer code review rubric (4 sections) | Instructor | Day 0 (T-7d) | `instructor/rubrics/week10_peer_code_review_rubric.md` | TODO |
| OP-22 | W12 M2 | Prepare reproducibility audit checklist (5 checks) | Instructor | Day 0 (T-7d) | `instructor/rubrics/week12_reproducibility_audit_checklist.md` | TODO |
| OP-23 | W13 M2 | Prepare practice showcase feedback form | Instructor | Day 0 (T-7d) | `instructor/forms/week13_showcase_feedback_form.md` | TODO |
| OP-24 | W14 M1 | Prepare tailored adversarial question bank template | Instructor | Day 0 (T-7d) | `instructor/forms/week14_question_bank_template.md` | TODO |

## Weekly rolling prep

| ID | Week/Meeting | Task | Owner | Deadline | Depends On | Status |
|---|---|---|---|---|---|---|
| OP-25 | W1 M1 | Confirm students configured OpenAI/Groq key in `.env` | Students + TA check | 24h before W1 M1 | onboarding email + env guide | TODO |
| OP-26 | W1 M2 | Print APS excerpt + retracted-preprint paragraph packet | TA | 24h before W1 M2 | approved packet source | TODO |
| OP-27 | W5 M2 | Confirm proposal PDF + 5-slide deck submitted | Students + Instructor check | 24h before W5 M2 | submission form/repo path | TODO |
| OP-28 | W8 M2 | Commit broken pipeline + solution script; assign rotating pairs | Instructor + TA | 24h before W8 M2 | OP-17 | TODO |
| OP-29 | W9 M1 | Run `agentic_bug_hunt.py`; confirm all 3 bugs still trigger | TA | 24h before W9 M1 | OP-18 | TODO |
| OP-30 | W10 M2 | Assign W10 peer-review pairs (A↔B) | Instructor | 48h before W10 M2 | class roster | TODO |
| OP-31 | W11 M1 | Assign two paper discussion leaders | Instructor | 7 days before W11 M1 | class roster | TODO |
| OP-32 | W11 M1 | Share both assigned papers with class | Discussion leaders + Instructor | 48h before W11 M1 | OP-31 | TODO |
| OP-33 | W11 M2 | Assign 3rd/4th discussion leaders and confirm papers shared | Instructor | 7 days before W11 M2 | class roster | TODO |
| OP-34 | W12 M2 | Circulate reproducibility checklist + assign rotated review pairs (+2 offset from W10) | Instructor | 48h before W12 M2 | OP-22, OP-30 | TODO |

## Showcase prep

| ID | Week/Meeting | Task | Owner | Deadline | Depends On | Status |
|---|---|---|---|---|---|---|
| OP-35 | W13 M2 | Compile peer feedback and email each student before W14 | Instructor + TA | Within 24h after W13 M2 | OP-23 | TODO |
| OP-36 | W14 M1 | Read all `paper_draft_<lastname>.tex` to draft tailored questions | Instructor | 48h before W14 M1 | draft submissions | TODO |
| OP-37 | W14 M1 | Verify students submitted `paper_draft_<lastname>.pdf` | Students + Instructor check | before W14 M1 start | submission tracker | TODO |
| OP-38 | W14 M2 | Reserve presentation room and invite faculty | Instructor/Admin | 14 days before W14 M2 | room booking system | TODO |
| OP-39 | W14 M2 | Verify showcase slides (`slides_final_<lastname>.pdf`, <=12 slides) submitted | Students + TA check | 24h before W14 M2 | submission tracker | TODO |

## Coverage check
- Blocking items converted: **39/39**
- Source: `instructor_materials_audit.json` (`priority = BLOCKING`)
