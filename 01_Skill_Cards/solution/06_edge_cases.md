# Skill Card: Edge Cases & Non-functional Requirements

## Definition

Identify and plan for edge cases, error states, and non-functional requirements (performance, security, accessibility, etc.).

---

## When to Use

- Before any launch or release
- When building consumer products
- When compliance is required
- When scale is a concern

---

## Outputs (Artifacts)

| Artifact | Description | Required? |
|----------|-------------|------------|
| Edge Cases List | Top 20 edge cases | Yes |
| Handling Strategy | How each is handled | Yes |
| NFR Checklist | Non-functional requirements | Yes |
| Rejection Criteria | When to reject gracefully | Conditional |
| Error Messages | User-facing error copy | Conditional |

---

## Pass Criteria

- [ ] At least 20 edge cases identified
- [ ] Each has a defined handling strategy
- [ ] NFR checklist completed (performance, security, privacy, accessibility)
- [ ] Clear rejection criteria for invalid inputs
- [ ] Error messages are user-friendly

---

## Red Flags

- ⚠️ Less than 10 edge cases
- ⚠️ No handling strategy defined
- ⚠️ NFR not considered
- ⚠️ "Happy path only" thinking

---

## Example

**Scenario:** Payment processing

**Edge Cases:**
- Card declined mid-transaction
- Network timeout during payment
- Duplicate payment attempt
- Currency conversion failure
- Card type not supported
- Payment amount exceeds limit

**Handling:** Each has specific error message + retry logic + logging

---

## Context Adapter

### Startup Version
- Minimum artifacts: Edge Cases (top 10) + Handling Strategy
- Timeline: 1 day
- NFR: Focus on critical only

### Big Tech Version
- Required artifacts: All artifacts
- Timeline: 1 week
- NFR: Full coverage (privacy, security, latency, cost, accessibility)

---

## Related Skills

- 02_service_blueprint
- 05_mvp_cutline
- 10_threat_model
