# Syllabus: AI in Physics Research
## Generative AI & Knowledge Platforms

## Course Overview

This 14-week graduate academic topics course provides practical experience in solving extensive
physics problems using advanced Generative AI workflows. Shifting beyond traditional machine
learning, this course focuses on "vibe-coding," developing theoretical frameworks with AI, and
building knowledge platforms that integrate services via Model Context Protocol (MCP) servers.
The course is divided into three phases: **The Common Baseline** (Weeks 1–5),
**Project Ideation & Deep Dives** (Weeks 6–7), and **Project Execution & Polish** (Weeks 8–14).
The experience culminates in a departmental showcase presentation.

## Course Information

| Item | Details |
| --- | --- |
| **Contact hours** | Twice a week for 1 hour 15 minutes |
| **Course dates** | September 9 to December 11, 2026 |
| **Method of evaluation** | Continuous assessment through mini-assignments, project proposal and pitch, peer review and participation, final project codebase and paper, and the departmental showcase presentation |

---

## Assessment Plan

This course utilizes a seminar/workshop model scaled for a maximum of 10 graduate students.
Assessment pivots away from traditional exams, focusing heavily on reproducibility, peer
collaboration, and the final deliverables. Evaluation is therefore a mix of individual coding
work, collaborative critique, and public presentation of the final project.

| Component | Weight | Description |
|-----------|--------|-------------|
| Standard Curriculum Mini-Assignments | 20% | Four short coding assignments during Weeks 1–4, reviewed for methodology rather than perfect accuracy. |
| Project Proposal & Pitch | 15% | A 2-page written proposal and a 5-minute presentation in Week 5. Graded on clarity, scope, and feasibility. |
| Peer Review & Participation | 15% | Code review in Week 10 and reading-group engagement in Weeks 11–12. |
| Final Project Codebase & Paper | 25% | A 4–6 page RevTeX paper and well-documented GitHub repository. Emphasis on reproducibility and physical interpretation. |
| Departmental Showcase Presentation | 25% | Public 10-minute presentation + 5-minute Q&A per student in Week 14. |

---

## Weekly Schedule

### Phase 1: The Common Baseline (Weeks 1–5)

#### Week 1: GenAI Underpinnings

- **Topics:** The architecture of Transformers, Attention mechanisms, and how latent spaces encode information.
- **Learning Objectives:** Understand the foundational mechanics of LLMs and clearly identify why these architectures inherently fail at rigorous mathematics without external grounding.
- **Assignments & Milestones:** Mini-assignment 1. Brainstorming domain-specific problems for the final project.
- **Grading:** Code is auto-graded or reviewed for baseline methodology.

#### Week 2: "Vibe-Coding" & Its Pitfalls

- **Topics:** Prompt engineering for physics scripts, recognizing hallucinations, and identifying broken boundary conditions.
- **Learning Objectives:** Navigate the illusion of competence in AI-generated code and safely debug generative coding outputs.
- **Assignments & Milestones:** Mini-assignment 2. Initial literature review of AI applications within the student's specific subfield.
- **Grading:** Code is auto-graded or reviewed for baseline methodology.

#### Week 3: RAG & Knowledge Platforms

- **Topics:** Building Retrieval-Augmented Generation (RAG) systems tailored for dense physics literature.
- **Learning Objectives:** Successfully query external knowledge bases, such as arXiv or digitized lab notes, to ground AI outputs in factual literature.
- **Assignments & Milestones:** Mini-assignment 3. Identifying accessible datasets and mapping out computational requirements for the final project.
- **Grading:** Code is auto-graded or reviewed for baseline methodology.

#### Week 4: Tool Use & Agents

- **Topics:** Introduction to the Model Context Protocol (MCP).
- **Learning Objectives:** Learn how to safely grant LLMs access to external computational tools and databases.
- **Assignments & Milestones:** Mini-assignment 4. Drafting the project scope and methodology.
- **Grading:** Code is auto-graded or reviewed for baseline methodology.

#### Week 5: GenAI in Theoretical Physics

- **Topics:** Using AI for symbolic regression, hypothesis generation, and automated theorem proving by combining LLMs with symbolic engines like SymPy.
- **Learning Objectives:** Bridge the gap between stochastic token generation and strict symbolic constraints.
- **Assignments & Milestones:** Project Proposal Pitch.
- **Grading:** 5-minute presentations delivered to the class, graded on clarity of the 2-page proposal and the pitch itself, followed by immediate feedback.

---

### Phase 2: Project Ideation & Deep Dives (Weeks 6–7)

#### Week 6: Building MCP Servers

- **Topics:** Practical lab on developing an MCP server.
- **Learning Objectives:** Connect an LLM to a live physical database (e.g., SIMBAD, Materials Project) or a local Python simulator.
- **Assignments & Milestones:** Data cleaning, pipeline setup, and exploratory data analysis (EDA) for the student's specific project.

#### Week 7: Evaluating AI in Physics

- **Topics:** Developing robust benchmarking strategies for generative outputs.
- **Learning Objectives:** Effectively test AI outputs against established physical invariants and fundamental conservation laws.
- **Assignments & Milestones:** Establishing traditional baseline models before applying GenAI to the project problem.

---

### Phase 3: Project Execution & Polish (Weeks 8–14)

#### Week 8: Advanced Platform Integration

- **Topics:** Hooking custom physics evaluation loops into agentic frameworks such as AutoGen or LangChain.
- **Learning Objectives:** Build multi-step, autonomous workflows capable of iterative scientific reasoning.
- **Assignments & Milestones:** Initial model training and iterative refinement.

#### Week 9: Debugging Agentic Workflows

- **Topics:** Handling infinite loops, context window limits, and prompt injection in scientific knowledge platforms.
- **Learning Objectives:** Maintain stability and logical consistency in complex, LLM-driven architectures.
- **Assignments & Milestones:** Troubleshooting project architectures and addressing logic errors.

#### Week 10: Ethics & Reproducibility

- **Topics:** Properly citing AI contributions and ensuring vibe-coded projects can be perfectly reproduced by other researchers.
- **Learning Objectives:** Uphold academic integrity when deploying generative tools in physics research.
- **Assignments & Milestones:** Mid-Project Code Review.
- **Grading:** Peer-to-peer code analysis in class; students are evaluated on their participation and collaborative feedback.

#### Week 11: Seminar / Reading Group (Part 1)

- **Topics:** Student-led discussions on cutting-edge papers relevant to their specific projects.
- **Learning Objectives:** Critically analyze contemporary research at the intersection of AI and physics.
- **Assignments & Milestones:** Finalizing model results and generating scientific visualizations.
- **Grading:** Evaluated on engagement and contribution to the reading group discussion.

#### Week 12: Seminar / Reading Group (Part 2)

- **Topics:** Continuation of student-led paper discussions.
- **Learning Objectives:** Synthesize broader trends in AI physics applications.
- **Assignments & Milestones:** Drafting the final report in Physical Review or NeurIPS format.
- **Grading:** Evaluated on engagement and contribution to the reading group discussion.

#### Week 13: Scientific Communication

- **Topics:** Effectively presenting AI results to skeptical traditional physicists.
- **Learning Objectives:** Defend the validity, interpretability, and rigor of AI-generated insights in a physical sciences context.
- **Assignments & Milestones:** Practice presentations with peer and instructor feedback.

#### Week 14: Course Wrap-Up & Showcase

- **Topics:** Course evaluations and final Q&A.
- **Learning Objectives:** Synthesize the 14-week experience and publicly articulate research findings.
- **Assignments & Milestones:** Final Project Codebase & Paper due. Departmental Showcase: Public presentation of results.
- **Grading:** The final paper and repository account for 25% of the grade. The departmental showcase presentation (10 minutes + 5 minutes Q&A) accounts for the final 25%.
