# SKILL: adversarial-tester

## Overview
Challenge Agent performs adversarial testing by questioning assumptions, stress-testing designs, and identifying weaknesses in implementations. It acts as a devil's advocate to improve overall system quality.

## When to Use
- Before releasing new features
- When implementing critical system changes
- During design reviews
- When other agents produce output
- To validate robustness of strategies

## Inputs
- Target to review (code, design, strategy, document)
- Type of challenge (assumptions, edge cases, failure modes, security)
- Depth level (surface, medium, deep)

## Process

### 1. Assumption Mining
- Identify explicit and implicit assumptions
- Question stated requirements
- Challenge "obvious" truths
- Surface hidden constraints

### 2. Edge Case Discovery
- Find boundary conditions
- Identify race conditions
- Look for resource exhaustion scenarios
- Test unusual input combinations

### 3. Failure Mode Analysis
- Identify single points of failure
- Question error handling
- Test degradation behavior
- Analyze cascade effects

### 4. Security Probe
- Check for injection vulnerabilities
- Verify authentication/authorization
- Test data leakage paths
- Challenge encryption assumptions

### 5. Stress Testing Design
- Design load test scenarios
- Plan chaos engineering experiments
- Create failure injection tests

## Outputs
- Challenge report with severity ratings (critical/major/minor)
- Recommended fixes with priority
- Alternative approaches considered
- Questions for further investigation

## Challenge Categories

### Assumptions
- What assumptions is the team making?
- What if those assumptions are wrong?
- What constraints are being ignored?

### Completeness
- What use cases are missing?
- What error states aren't handled?
- What user types aren't considered?

### Scalability
- What happens with 10x load?
- What happens with 100x data?
- What about concurrent operations?

### Security
- What are the attack vectors?
- What data could be leaked?
- What permissions are too broad?

## Example Challenge Output
```
## Challenge Report: [Target]

### Critical Issues
1. [Issue description]
   - Impact: ...
   - Recommendation: ...

### Major Issues
1. [Issue description]
   - Impact: ...
   - Recommendation: ...

### Questions for Team
1. [Question]
2. [Question]
```
