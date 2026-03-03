# Skill Card: Problem Framing & Outcome Spec

## Definition

Define what problem you're solving, for whom, and what outcome success looks like.

---

## When to Use

- Starting any new product or feature
- When stakeholders disagree on what problem to solve
- Before writing any PRD
- When scope keeps expanding without clear rationale

---

## Outputs (Artifacts)

| Artifact | Description | Required? |
|----------|-------------|------------|
| Problem Statement | One-paragraph description of the problem | Yes |
| Outcome Spec | Measurable success criteria | Yes |
| Segment Definition | Who specifically benefits | Yes |
| Context Mapping | User scenario description | Yes |
| Assumption Register | List of all assumptions | Yes |

---

## Pass Criteria

- [ ] Problem can be rephrased as "User X trying to do Y but blocked by Z"
- [ ] Outcome is measurable with specific metric and target
- [ ] Target segment is clearly defined with size estimate
- [ ] All assumptions are documented and testable
- [ ] Problem is validated with real users (not just internal opinion)

---

## Red Flags

- ⚠️ Problem statement uses "we" instead of "user"
- ⚠️ Outcome is vague (e.g., "improve experience")
- [ ] No clear user segment identified
- ⚠️ Assumptions are not testable
- ⚠️ Problem was not validated with users

---

## Example

**Scenario:** A B2B SaaS company wants to reduce churn

**What was done:**
- Problem: "Mid-market customers with 10-50 seats are churning at 8%/month because they can't get value in first 30 days"
- Outcome: "Reduce day-30 activation rate from 40% to 70% within 6 months"
- Segment: Companies with 10-50 seats, used product 3+ times in first week

**Result:** Product team focused on onboarding flow, churn dropped to 4%/month

---

## Context Adapter

### Startup Version
- Minimum artifacts: Problem Statement + Outcome Spec
- User validation: Interview 5-10 target users
- Timeline: 1-2 days
- Pass criteria: Problem resonates with 80%+ interviewees

### Big Tech Version
- Required artifacts: All 5 artifacts
- User validation: Quantitative data + user research
- Required approvals: Stakeholder sign-off on outcome
- Timeline: 1-2 weeks

---

## Related Skills

- 02_service_blueprint
- 03_metrics_tree
- 11_stakeholder_map
