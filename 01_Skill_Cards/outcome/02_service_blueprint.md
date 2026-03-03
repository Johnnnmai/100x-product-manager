# Skill Card: Service Blueprint (Product is Service)

## Definition

Map the complete service journey including user actions, touchpoints, failure modes, and fallback mechanisms.

---

## When to Use

- Designing any user-facing product or feature
- When handoffs between systems/users can fail
- For critical user journeys (checkout, signup, etc.)
- When reliability is a key requirement

---

## Outputs (Artifacts)

| Artifact | Description | Required? |
|----------|-------------|------------|
| Service Blueprint | End-to-end journey map | Yes |
| Failure Modes | List of ways things can go wrong | Yes |
| Fallback Mechanisms | What happens when things fail | Yes |
| SLA Definitions | Service level agreements | Conditional |
| Ownership Map | Who owns each touchpoint | Yes |

---

## Pass Criteria

- [ ] At least 10 failure modes identified
- [ ] Each failure mode has a defined fallback
- [ ] Clear ownership for each touchpoint
- [ ] SLA defined for critical paths
- [ ] Blueprint covers happy path AND error paths

---

## Red Flags

- ⚠️ Only happy path documented
- [ ] No fallback for critical failures
- ⚠️ Ownership gaps (no one responsible for X)
- ⚠️ SLA missing for user-critical flows

---

## Example

**Scenario:** ATM withdrawal

**Service Blueprint includes:**
- User inserts card → enters PIN → selects amount → receives cash → card returned
- Failure modes: Card stuck, cash not dispensed, wrong amount, network timeout
- Fallbacks: Manual cash dispensing, receipt printing, customer service handoff

**Result:** Users trust ATM because failure modes are handled

---

## Context Adapter

### Startup Version
- Minimum artifacts: Service Blueprint + 5 failure modes + fallbacks
- Timeline: 1-2 days
- Focus: Manual fallbacks and workarounds acceptable

### Big Tech Version
- Required artifacts: All artifacts + SLA/SLO + on-call rotation
- Timeline: 1-2 weeks
- Focus: Production-grade reliability required

---

## Related Skills

- 01_problem_framing
- 09_rollout_rollback
- 10_threat_model
