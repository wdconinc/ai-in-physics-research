# Internal Consistency Review
## AI in Physics Research Course Artifacts

## 1. Executive Summary

This refresh reflects the current repository state after artifact creation and YAML/doc consistency fixes.

| Metric | Count | Source |
|---|---:|---|
| Core consistency issues (formal audits) | 4 | `file_audit.json`, `crossweek_audit.json`, `convention_audit.json` |
| Blocking core issues | 0 | All former core blockers resolved |
| Important core issues | 1 | 1 medium convention issue |
| Informational core issues | 3 | 2 cross-week info + 1 low convention issue |
| Operational readiness checklist items | 52 | `instructor_materials_audit.json` |
| Operational blockers (pending) | 23 | `instructor_materials_audit.json.summary.by_priority.BLOCKING` |
| Operational items resolved | 17 | `instructor_materials_audit.json.summary.resolved_items` |

Top risk: remaining operational prep execution (23 blocking checklist items), not missing repository artifacts.

## 2. Scope and Method

Inputs reviewed:
- `file_audit.json`, `crossweek_audit.json`, `convention_audit.json`, `instructor_materials_audit.json`
- `week-01.yaml` ... `week-14.yaml`
- `docs/full-course-plan.md`
- `docs/syllabus.md`

Method:
1. Re-ran artifact existence checks for all required exercise/starter files.
2. Re-validated cross-week dependency and deadline wording in updated YAML.
3. Re-audited naming/URL/model conventions in week YAML sources.
4. Recomputed instructor-readiness summary with resolved vs pending status.

## 3. High-Severity Findings (Blocking)

| ID | Finding | Evidence | Impact | Required action |
|---|---|---|---|---|
| B-01 | Former missing exercise/starter artifacts resolved | `file_audit.json.missing_files = []`; `resolved_missing_files = 9` | Core delivery unblock achieved | Keep smoke-testing these files before each offering |
| B-02 | Former W10/W12 naming mismatch resolved | `week-10.yaml`, `week-12.yaml` use `<reviewer_lastname>/<author_lastname>` | Reduces submission ambiguity | Preserve canonical schema in future edits |
| B-03 | Former URL-scheme/stale-link blocker set resolved in YAML | `convention_audit.json.issues` no high-severity URL blockers | Reduces immediate link breakage risk | Keep periodic link checks |
| B-04 | 23 blocking operational readiness tasks remain pending | `instructor_materials_audit.json.summary.by_priority.BLOCKING` | Delivery risk shifts to execution readiness | Close pending runbook tasks with owners/dates/status updates |

## 4. Important Findings (Non-blocking but high impact)

| ID | Finding | Count/Scope | Impact | Action |
|---|---|---:|---|---|
| I-01 | Personal GitHub repo dependency (`art-of-readme`) remains | 1 | External continuity risk for W12 reading prep | Pin commit and/or mirror excerpt into instructor-controlled materials |

## 5. Informational Findings (Cleanup / quality)

| ID | Finding | Impact | Action |
|---|---|---|---|
| N-01 | W14 estimated-time says “No new work” while self-assessment is new | Messaging ambiguity | Reword to “No new code/paper sections; reflective deliverable remains” |
| N-02 | W12 rubric still combines self-audit + partner-audit in one criterion | Grading transparency ambiguity | Split into distinct rubric rows or add explicit sub-weighting |
| N-03 | Mixed “Claude claude-3-5-sonnet-20241022” wording persists | Cosmetic consistency issue | Normalize to “Claude (claude-3-5-sonnet-20241022)” |

## 6. Missing Artifact Manifest (with required specs)

### 6.1 Exercise files

All previously missing required exercise/starter artifacts are now present:

- `exercises/week01/meeting1_token_explorer.ipynb`
- `week02_buggy_harmonic_oscillator.py`
- `week02_test_driven_skeleton.ipynb`
- `week02_starter/ai_generated_oscillator.py`
- `week03_rag_skeleton.ipynb`
- `week03_fallback_corpus.json`
- `skeleton_mcp_server.py`
- `multi_api_pipeline_broken.py`
- `agentic_bug_hunt.py`

### 6.2 Forms and rubrics

Instructor forms/rubrics added under `instructor/forms`, `instructor/rubrics`, and `instructor/debate-briefs` are detected and counted as resolved where applicable.

### 6.3 Suggested repository tree

Current repository now includes the core Week 1/2/3/6/8/9 exercise artifacts plus instructor materials introduced by the fix set.

## 7. Cross-Week Dependency Validation

### 7.1 Dependency graph

Dependency-chain records remain valid (`VALID`) and structurally intact.

### 7.2 Validated chains

- 12/12 dependency-chain records remain `VALID`.
- Former warnings are resolved:
  - W13 `v0.9-draft` → W14 `v1.0-final` is now explicit in W14 Step 2.
  - W10 Step 3 delayed grading handoff to W12 is now explicit in W10/W12 language.

### 7.3 Deadline and grading ambiguities

Residual non-blocking ambiguities:
- W14 “No new work” wording vs self-assessment deliverable.
- W12 rubric criterion bundling (self-audit + partner audit).

## 8. Naming, Placeholder, and File Convention Audit

### 8.1 Current variants

Current week YAMLs consistently use:
- `<lastname>`
- `<reviewer_lastname>`
- `<author_lastname>`

Legacy variants (`<your_lastname>`, `<partner_lastname>`, `<reviewer>`, `<author>`) are not present in current week YAML files.

### 8.2 Proposed canonical standard

| Category | Canonical rule |
|---|---|
| Single-author deliverables | `<lastname>` |
| Reviewer role placeholder | `<reviewer_lastname>` |
| Reviewed/author role placeholder | `<author_lastname>` |
| Peer review file | `peer_review_<reviewer_lastname>_reviews_<author_lastname>.md` |
| Repro audit file | `reproducibility_audit_<reviewer_lastname>_reviews_<author_lastname>.md` |
| Root persistent files | `REPRODUCIBILITY.md`, `BUG_LOG.md`, `REVIEW_RESPONSES.md` |

### 8.3 Migration mapping table

Resolved mapping:
- W10 peer-review schema now aligned with canonical reviewer/author placeholder style.
- W12 reproducibility-audit schema now aligned with canonical reviewer/author placeholder style.

## 9. URL / Tool / Model Reference Audit

### 9.1 URL validation matrix

Current week YAML references no longer show the prior high-severity stale/scheme-missing URL set that drove blockers.

Residual important URL dependency:
- `https://github.com/hackergrrl/art-of-readme` (personal-repo continuity risk).

### 9.2 Tool/package naming checks

No blocking package-name errors found. Advisory optional-package guidance remains (`langchain`, `llama-index`).

### 9.3 Model pinning and reproducibility risks

Pinned `claude-3-5-sonnet-20241022` usage is now dominant in week YAMLs. Residual cleanup is wording normalization in prose examples.

## 10. Instructor Operational Readiness Checklist

### 10.1 Pre-course (Day 0) checklist

Core repository artifacts and instructor forms are substantially improved; remaining execution tasks are primarily operational and scheduling-focused.

### 10.2 Rolling weekly prep checklist

| Category | Count | Status |
|---|---:|---|
| Total checklist items | 52 | Audited |
| Resolved | 17 | `status = RESOLVED` |
| Pending | 35 | `status = PENDING` |
| Pending BLOCKING | 23 | Requires closure before delivery |
| Pending IMPORTANT | 11 | High-impact but non-blocking |
| Pending RECOMMENDED | 1 | Optional hardening |

### 10.3 Showcase preparation checklist

Showcase prep tasks remain pending and should be actively tracked in `instructor/runbook.md` through execution.

## 11. Implementation Roadmap for Next Phase

### Phase 0 — Critical unblockers

| Task ID | Deliverable | Status |
|---|---|---|
| P0-01 | Create 9 missing exercise/starter artifacts | **Completed** |
| P0-02 | Standardize peer-review placeholder schemas | **Completed** |
| P0-03 | Repair prior stale/scheme URL blockers in YAML | **Completed (core set)** |
| P0-04 | Operational blocker closure from runbook | **In progress** (23 blocking tasks pending) |

### Phase 1 — Consistency hardening

| Task ID | Deliverable | Status |
|---|---|---|
| P1-01 | Explicit W13→W14 tag dependency language | **Completed** |
| P1-02 | Clarify W10/W12 grading handoff | **Completed** |
| P1-03 | Final prose cleanup of model naming format | Pending |
| P1-04 | External reading dependency hardening | Pending |

### Phase 2 — Quality improvements

| Task ID | Deliverable | Status |
|---|---|---|
| P2-01 | Add machine-checkable convention lint | Deferred |
| P2-02 | Weekly readiness dashboard from checklist statuses | Deferred |
| P2-03 | Automated link-check with manual exception allowlist | Deferred |
| P2-04 | Split W12 mixed rubric criterion | Pending |

## 12. Acceptance Criteria for Implementation Completion

**CI-checkable criteria**
1. All 9 required starter artifacts exist at expected paths. **Pass**
2. Peer-review/repro-audit naming schema aligned. **Pass**
3. W14 explicitly references `v0.9-draft` progression. **Pass**
4. W10/W12 delayed grading handoff explicit. **Pass**
5. No remaining high-severity core consistency issues in formal audits. **Pass**

**Manual review criteria**
1. Remaining runbook blocking tasks have owner/date/closure tracking. **Pending**
2. Personal-repo reading dependency risk is mitigated. **Pending**
3. W12 mixed rubric criterion split or sub-weighted. **Pending**
4. W14 “No new work” wording clarified. **Pending**

## 13. Appendix

### 13.1 Full issue register table

| Source | Severity | Count |
|---|---|---:|
| `file_audit.json` | BLOCKING | 0 |
| `file_audit.json` | IMPORTANT | 0 |
| `crossweek_audit.json` | WARNING | 0 |
| `crossweek_audit.json` | INFO | 2 |
| `convention_audit.json` | HIGH | 0 |
| `convention_audit.json` | MEDIUM | 1 |
| `convention_audit.json` | LOW | 1 |
| `instructor_materials_audit.json` (operational, pending) | BLOCKING | 23 |
| `instructor_materials_audit.json` (operational, pending) | IMPORTANT | 11 |
| `instructor_materials_audit.json` (operational, pending) | RECOMMENDED | 1 |

### 13.2 Traceability matrix (issue → source week/line context)

| Issue ID | Issue summary | Source context |
|---|---|---|
| R-01 | Nine required starter artifacts now present | `file_audit.json.resolved_missing_files` |
| C-01 | W14 “No new work” wording vs self-assessment deliverable | `week-14.yaml` (`estimated_time`, Step 4) |
| C-02 | W12 mixed rubric criterion remains bundled | `week-12.yaml` (`grading_criteria` reproducibility row) |
| V-01 | Personal repo dependency (`art-of-readme`) remains | `week-12.yaml` meeting 2 topic prompt resources |
| V-02 | Mixed “Claude claude-3-5-sonnet-20241022” prose remains | `week-05.yaml` and `week-10.yaml` example text |
| O-01 | Pending operational blockers remain | `instructor_materials_audit.json.summary.by_priority.BLOCKING` |
