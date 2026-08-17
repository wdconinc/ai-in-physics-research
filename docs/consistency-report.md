# Consistency Report: Generative AI in Physics Research Course

Generated: 2026-07-28

---

## 1. Engagement Format Distribution

The six valid archetypes are: Live coding exercise, Socratic seminar, Pair debugging, Structured debate, Collaborative whiteboard, Peer code review.

| Format | W1M1 | W1M2 | W2M1 | W2M2 | W3M1 | W3M2 | W4M1 | W4M2 | W5M1 | W5M2 | W6M1 | W6M2 | W7M1 | W7M2 | W8M1 | W8M2 | W9M1 | W9M2 | W10M1 | W10M2 | W11M1 | W11M2 | W12M1 | W12M2 | W13M1 | W13M2 | W14M1 | W14M2 | Total | Status |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Socratic seminar | | ✓ | | | | ✓ | | | | | | | | | | | | ✓ | | | ✓ | | ✓ | | ✓ | | ✓ | | **7** | ⚠️ FLAGGED |
| Structured debate | | | | | | | | | | | | | ✓ | | | | | | ✓ | | | ✓ | | | | ✓ | | ✓ | **5** | ⚠️ FLAGGED |
| Live coding exercise | ✓ | | | ✓ | ✓ | | | | | | ✓ | | | | | | | | | | | | | | | | | | **4** | OK |
| Collaborative whiteboard | | | | | | | | | ✓ | | | ✓ | | ✓ | ✓ | | | | | | | | | | | | | | **4** | OK |
| Pair debugging | | | ✓ | | | | | | | | | | | | | ✓ | ✓ | | | | | | | | | | | | **3** | OK |
| Peer code review | | | | | | | | | | | | | | | | | | | | ✓ | | | | ✓ | | | | | **2** | OK |
| **Live Coding Exercise** *(bad caps)* | | | | | | | ✓ | | | | | | | | | | | | | | | | | | | | | | **1** | ⚠️ CAPS |
| **Collaborative Whiteboard** *(bad caps)* | | | | | | | | ✓ | | | | | | | | | | | | | | | | | | | | | **1** | ⚠️ CAPS |
| **Structured peer critique** *(invalid)* | | | | | | | | | | ✓ | | | | | | | | | | | | | | | | | | | **1** | ❌ INVALID |

> **Note on normalized counts:** "Live Coding Exercise" (W4M1) and "Live coding exercise" refer to the same archetype; normalized total = **5** (would be flagged). "Collaborative Whiteboard" (W4M2) and "Collaborative whiteboard" are the same; normalized total = **5** (would be flagged).

**Flagged formats (>4 uses, raw strings):** Socratic seminar (7), Structured debate (5)

**Additional issues:**
- W4M1 uses `"Live Coding Exercise"` (incorrect capitalization — should be `"Live coding exercise"`). Normalized total for this archetype = **5**, which also exceeds the threshold.
- W4M2 uses `"Collaborative Whiteboard"` (incorrect capitalization — should be `"Collaborative whiteboard"`). Normalized total for this archetype = **5**, which also exceeds the threshold.
- W5M2 uses `"Structured peer critique"` which is **not one of the six valid archetypes**. This must be replaced.

---

## 2. Student Intro Format Distribution

The four canonical formats are: "8-minute chalk talk", "10-minute slide presentation (max 6 slides)", "10-minute live demo", "8-minute paper presentation". Special one-off formats for Week 5 (pitch), Weeks 11–12 (reading-group discussion), Week 13M2 (demo variant), and Week 14M2 (showcase) are expected.

| Format | W1M1 | W1M2 | W2M1 | W2M2 | W3M1 | W3M2 | W4M1 | W4M2 | W5M1 | W5M2 | W6M1 | W6M2 | W7M1 | W7M2 | W8M1 | W8M2 | W9M1 | W9M2 | W10M1 | W10M2 | W11M1 | W11M2 | W12M1 | W12M2 | W13M1 | W13M2 | W14M1 | W14M2 | Total | Status |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 8-minute chalk talk | ✓ | | | ✓ | ✓ | | | | | | | | | | ✓ | | | ✓ | | ✓ | | | | ✓ | | | ✓ | | **8** | ⚠️ FLAGGED |
| 10-minute live demo | | ✓ | ✓ | | | | ✓ | | | | | ✓ | | | | ✓ | ✓ | | | | | | | | | | | | **6** | ⚠️ FLAGGED |
| 10-minute slide presentation (max 6 slides) | | | | | | ✓ | | ✓ | | | ✓ | | | ✓ | | | | | ✓ | | | | | | | | | | **5** | OK |
| 8-minute paper presentation | | | | | | | | | ✓ | | | | ✓ | | | | | | | | | | | | ✓ | | | | **3** | OK |
| 15-min paper discussion (whiteboard outline) | | | | | | | | | | | | | | | | | | | | | | ✓ | ✓ | | | | | | **2** | OK (reading-group variant) |
| 15-min paper discussion (whiteboard outline, no slides required) | | | | | | | | | | | | | | | | | | | | | ✓ | | | | | | | | **1** | ⚠️ MINOR (inconsistent with W11M2/W12M1) |
| 5-min pitch presentation (max 5 slides) per student | | | | | | | | | | ✓ | | | | | | | | | | | | | | | | | | | **1** | OK (W5 special) |
| 10-min slide presentation — 3 min demo + 7 min commentary | | | | | | | | | | | | | | | | | | | | | | | | | | ✓ | | | **1** | OK (W13M2 special) |
| 10-min showcase presentation (≤12 slides) + 5-min Q&A | | | | | | | | | | | | | | | | | | | | | | | | | | | | ✓ | **1** | OK (W14 special) |

**Flagged formats (>5 uses):** 8-minute chalk talk (8), 10-minute live demo (6)

**Minor inconsistency:** W11M1 uses `"15-minute paper discussion (whiteboard outline, no slides required)"` while W11M2 and W12M1 use `"15-minute paper discussion (whiteboard outline)"`. These describe the same format; the two strings should be normalized to one canonical form.

---

## 3. Homework Completeness

| Week | Criteria sum | # Deliverables | Estimated time | Status |
|---|:---:|:---:|:---|:---:|
| W01 | 100% | 4 | 3–4 hours | ✅ OK |
| W02 | 100% | 3 | 3–5 hours | ✅ OK |
| W03 | 100% | 4 | 4–5 hours | ✅ OK |
| W04 | 100% | 3 | 4–6 hours | ✅ OK |
| W05 | 100% | 3 | 5–8 hours | ✅ OK |
| W06 | 100% | 4 | 5–8 hours | ✅ OK |
| W07 | 100% | 4 | 5–7 hours | ✅ OK |
| W08 | 100% | 4 | 6–8 hours | ✅ OK |
| W09 | 100% | 4 | 5–7 hours | ✅ OK |
| W10 | 100% | **2** | 4–6 hours | ❌ ISSUE |
| W11 | 100% | 4 | 5–7 hours | ✅ OK |
| W12 | 100% | 3 | 4–6 hours | ✅ OK |
| W13 | 100% | 4 | 8–12 hours | ✅ OK |
| W14 | 100% | 4 | No new work | ✅ OK |

**Issues found:**
- **W10**: Only 2 named deliverables (`ethics_statement_<lastname>.md` and `peer_review_…md`). The minimum is 3. A third deliverable should be named — for example, a post-class self-assessment form (already mentioned in the grading criteria description but not listed as a deliverable) or a structured reading annotation.
- All 14 weeks sum grading criteria to exactly 100%. ✅
- All 14 weeks have an `estimated_time` field. ✅
- Estimated times increase appropriately from ~3–4 hours (W01) to 8–12 hours (W13), then reset to "no new work" (W14). ✅

---

## 4. Assessment Category Coverage

| Category | Weeks mapped | Expected weeks | Status |
|---|:---:|:---:|:---:|
| Standard Curriculum Mini-Assignments | 1, 2, 3, 4 | 1–4 | ✅ OK |
| Project Proposal & Pitch | 5 | 5 | ✅ OK |
| Final Project Codebase & Paper | 6, 7, 8, 9, 13 | 6, 7, 8, 9, 13, 14 | ⚠️ See note |
| Peer Review & Participation | 10, 11, 12 | 10, 11, 12 | ✅ OK |
| Departmental Showcase Presentation | (14, combined) | 14 | ⚠️ See note |

**Note on W14:** Week 14's `assessment_category` is set to `"Final Project Codebase & Paper (25%) and Departmental Showcase Presentation (25%)"` — a combined string that does not exactly match either of the two standalone category names. Both categories are therefore represented in W14, but only via this combined string. This is not a correctness error (the course rubric clearly covers both), but it means automated category matching against exact strings will fail for both "Final Project Codebase & Paper" (which expects W14) and "Departmental Showcase Presentation" (which expects W14). If downstream tooling does exact-string matching on `assessment_category`, W14 should either use two entries or the combined string should be registered as a valid alias.

---

## 5. Phase Progression

**Phase 1 (Weeks 1–5) — Scaffolded foundations:** ✅ Well-executed. Homework instructions name specific files (`week01_<lastname>.ipynb`, `corpus.json`, `.env.example`), specific tools (OpenAI SDK, FAISS, MCP SDK, SIMBAD), specific commands (`pytest`, `IndexFlatIP`), and specific expected outputs (e.g., "energy levels E_n = hbar·ω·(n+0.5)"). Step-by-step guidance leaves little ambiguity. Estimated time starts at 3–4 hours and rises to 5–8 hours by W05, reflecting growing complexity without overwhelming students.

**Phase 2 (Weeks 6–7) — Open-ended, project-focused:** ✅ The shift is visible. W06 says "build two tools of your choice relevant to your research domain" — no prescribed domain, no mandated data source. W07 asks students to design their own evaluation protocol with their own success threshold and to choose their own three papers for annotation. Prescriptiveness drops noticeably; instructions set structural requirements (schema declarations, diagram completeness, word-count bounds) but not content.

**Phase 3 (Weeks 8–14) — Concrete milestones with high autonomy:** ✅ Each week delivers a specific project artifact (data pipeline, reproducibility controls, results section, paper draft, final paper) without prescribing implementation details. Students make their own design decisions within quality guardrails. The progression is coherent: W08 → pipeline, W09 → logging/reproducibility, W10 → ethics + peer review, W11 → results draft, W12 → limitations + responses, W13 → full draft, W14 → final submission. Estimated times peak at W13 (8–12 hours), signaling the highest-stakes milestone.

**Overall verdict:** The scaffolding decreases appropriately across the three phases. No phase-ordering violations were found.

---

## 6. Engagement Variety Across Phases

### Counts by format and phase

| Format | Phase 1 (W1–5, 10 mtgs) | Phase 2 (W6–7, 4 mtgs) | Phase 3 (W8–14, 14 mtgs) | Grand Total |
|---|:---:|:---:|:---:|:---:|
| Live coding exercise *(normalized)* | **5** | 1 | 0 | 6 |
| Pair debugging | 1 | 0 | **2** | 3 |
| Collaborative whiteboard *(normalized)* | 2 | 2 | 1 | 5 |
| Socratic seminar | 2 | 0 | **5** | 7 |
| Structured debate | 0 | 1 | **4** | 5 |
| Peer code review | 0 | 0 | **2** | 2 |
| Structured peer critique *(invalid)* | 1 | 0 | 0 | 1 |

### Assessment against expected progression

**Phase 1 should lean toward Live coding exercise and Pair debugging:**
- Live coding exercise accounts for 5 of 10 Phase 1 meetings (50%). ✅
- Pair debugging appears only once (W02M1, 10%). ⚠️ Could be higher — consider adding a second Pair debugging session in Weeks 3–4 to reinforce the debugging mindset, particularly given that W02's homework centers on finding bugs.
- W05M2 uses the invalid archetype "Structured peer critique" instead of a valid one such as "Peer code review", which would be a natural fit for pitch feedback.

**Phase 3 should lean toward Socratic seminar, Structured debate, Peer code review:**
- These three together account for 11 of 14 Phase 3 meetings (79%). ✅ The progression is clearly visible.
- The 2 Pair debugging sessions in Phase 3 (W08M2, W09M1) are defensible — they correspond to the reproducibility/debugging week — but they slightly dilute the intended Phase 3 character.

**Phase 2 (W6–7):** Dominated by Collaborative whiteboard (2/4 = 50%) plus one Live coding and one Structured debate. This is a reasonable bridge between phases.

---

## 7. Recommended Fixes

1. **W05M2 — Invalid engagement archetype:** Replace `"Structured peer critique"` with `"Peer code review"` (or `"Structured debate"`). "Structured peer critique" is not one of the six valid archetypes and will fail validation. "Peer code review" is the natural choice for a pitch-feedback session.

2. **W04M1 — Capitalization error in engagement format:** Change `"Live Coding Exercise"` to `"Live coding exercise"` to match the canonical archetype name. This also resolves the normalized overuse issue: with consistent casing, Live coding exercise has 5 appearances and should have one instance replaced (see fix 9).

3. **W04M2 — Capitalization error in engagement format:** Change `"Collaborative Whiteboard"` to `"Collaborative whiteboard"` to match the canonical archetype name. This also resolves the normalized overuse issue for Collaborative whiteboard (5 appearances after normalization).

4. **W10 — Fewer than 3 named deliverables:** The week has only 2 deliverables. Add a third: e.g., `"post_class_self_assessment_<lastname>.md — one-paragraph self-assessment (submitted within 24 hours)"` which is already referenced in the W12 grading criteria description but not listed as a W10 deliverable.

5. **Socratic seminar overuse (7 appearances, threshold 4):** Reduce by replacing at least 2–3 instances with underused archetypes. Suggested substitutions: W13M1 → `"Peer code review"` (fits the paper-draft review context), W14M1 → `"Structured debate"` (fits a final-week critical discussion), or W09M2 → `"Collaborative whiteboard"` (fits the reproducibility audit context).

6. **Structured debate overuse (5 appearances, threshold 4):** Reduce by replacing 1 instance. Suggested: W11M2 → `"Peer code review"` (the reading-group debrief format fits a code-review structure better than a formal debate).

7. **Live coding exercise overuse (5 normalized appearances, threshold 4):** After applying fix 2, reduce by 1. Suggested: W06M1 → `"Collaborative whiteboard"` (the MCP server design session is more naturally collaborative than a solo live coding exercise).

8. **Collaborative whiteboard overuse (5 normalized appearances, threshold 4):** After applying fix 3, reduce by 1. Suggested: W07M2 → `"Structured debate"` (the architecture review lends itself to a debate on design tradeoffs).

9. **8-minute chalk talk overuse (8 appearances, threshold 5):** Replace at least 2–3 instances with other intro formats. Suggested: W08M1 → `"10-minute slide presentation (max 6 slides)"`, W10M2 → `"10-minute live demo"`, W14M1 → `"8-minute paper presentation"`.

10. **W11M1 — Inconsistent intro format string:** W11M1 uses `"15-minute paper discussion (whiteboard outline, no slides required)"` while W11M2 and W12M1 use `"15-minute paper discussion (whiteboard outline)"`. Normalize all three to a single canonical string (either form is acceptable; pick one and apply it consistently) to prevent format-counting discrepancies.
