# Skill Card: Abuse & Threat Model

## Definition

Identify potential security threats, abuse vectors, and mitigation strategies before launch.

---

## When to Use

- Before any public-facing feature
- For features handling user data or payments
- When security is a known concern
- For platform products

---

## Outputs (Artifacts)

| Artifact | Description | Required? |
|----------|-------------|------------|
| Threat Model | Identified threats | Yes |
| Attack Vectors | How attacks could happen | Yes |
| Mitigations | How to prevent attacks | Yes |
| Abuse Cases | Ways product could be misused | Yes |
| Logging Requirements | What to audit | Conditional |

---

## Pass Criteria

- [ ] At least 5 threat categories covered
- [ ] Each threat has mitigation strategy
- [ ] Abuse cases identified
- [ ] Key logging requirements defined
- [ ] Security review completed

---

## Red Flags

- ⚠️ No threat model
- ⚠️ Security not considered
- ⚠️ Abuse vectors ignored
- ⚠️ No logging for audit

---

## Example

**Scenario:** User-generated content feature

**Threats:**
- Spam / bot content
- Malicious links
- Data leakage
- Privilege escalation
- DDoS

**Mitigations:**
- Rate limiting
- Content moderation
- Input sanitization
- Access controls
- CDN + WAF

---

## Context Adapter

### Startup Version
- Minimum artifacts: Threat Model + Mitigations
- Timeline: 1 day
- Focus: Top 5 most likely threats

### Big Tech Version
- Required artifacts: All 5 artifacts
- Timeline: 1-2 weeks
- Full security review, compliance requirements

---

## Related Skills

- 02_service_blueprint
- 06_edge_cases
- 09_rollout_rollback
