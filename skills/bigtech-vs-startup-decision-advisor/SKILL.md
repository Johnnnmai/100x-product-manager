---
name: bigtech-vs-startup-decision-advisor
description: Use when choosing between big tech and startup PM roles and you need a recommendation based on stage, risk, growth, and life constraints.
type: interactive
theme: career-leadership
best_for:
  - "Deciding between a startup PM role and a big tech PM role"
  - "Understanding which environment matches your current career needs"
  - "Making a role choice without defaulting to prestige or fear"
scenarios:
  - "I have a startup offer and a large-company PM process moving at the same time"
  - "I'm not sure whether I need brand, scope, mentorship, or upside most right now"
  - "I want a blunt recommendation instead of generic pros and cons"
estimated_time: "10-15 min"
---

## Purpose

Guide PMs through a structured decision between big tech and startup roles by scoring the trade-offs that actually matter: learning environment, scope, speed, compensation shape, risk tolerance, and career timing. Use this when a role choice feels emotionally noisy and you want a grounded recommendation instead of prestige-driven or fear-driven thinking.

This is not a generic career essay about "it depends." It is a decision advisor designed to produce a clear recommendation, the rationale behind it, and the risks of the alternative path.

## Key Concepts

### The Core Trade-Off

The big-tech vs startup decision is usually not about which path is objectively better. It is about which path matches **what you need now**.

| Dimension | Big tech usually offers | Startup usually offers |
| --- | --- | --- |
| **Brand signal** | Stronger market-recognized signaling | Weaker brand, stronger narrative if the company is real |
| **Scope shape** | Narrower surface, deeper specialization | Wider surface, messier ownership, faster context switching |
| **Speed** | Slower decisions, more process, larger blast radius | Faster loops, less cover, more volatility |
| **Mentorship** | More managers, systems, peer calibration | More ambiguity, mentorship quality varies wildly |
| **Compensation** | Higher cash stability and clearer leveling | Higher upside variance, more equity uncertainty |
| **Career story** | Strong operator signal in established systems | Strong builder signal if you actually own hard problems |

### What Most People Get Wrong

- They optimize for logo value when they actually need repetitions
- They optimize for upside when they actually need skill compounding
- They optimize for "impact" without checking whether the startup is real enough to give them leverage
- They compare compensation packages badly because they mix guaranteed value with story value

### Decision Lenses

Evaluate the choice across five lenses:

1. **Skill-building need** - Do you need structure, reps, or breadth?
2. **Risk tolerance** - Can you tolerate uncertainty in role, company, or pay?
3. **Signal need** - Do you need brand, story, or both?
4. **Life constraints** - Visa, family, runway, geography, burnout, manager quality
5. **Career timing** - Is this a season for compounding, stabilizing, or taking a bigger swing?

### When to Use This

- You are comparing startup and big-tech PM offers
- You are considering switching out of one environment into the other
- You keep changing your answer depending on who you talked to last

### When Not to Use This

- You have not inspected the actual company, role, manager, or compensation
- The decision is mostly about visa or legal constraints
- You are really choosing between specific companies, not company types

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol for this skill.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels
- interruption handling and pause/resume behavior
- numbered recommendations at decision points
- quick-select numbered response options for regular questions

This file defines the domain-specific scoring and recommendation logic. If there is a conflict, follow this file's domain logic.

## Application

This interactive skill asks **up to 4 adaptive questions**, then gives a recommendation with a decision memo.

### Question 1: What Are You Optimizing For Right Now?

Ask:

"What are you most trying to optimize for in the next 18-24 months?"

1. **Brand + calibration** - stronger signal, stronger PM operating standards
2. **Breadth + ownership** - wider scope, faster reps, more visible decisions
3. **Compensation stability** - predictable cash and lower downside
4. **Upside + asymmetric growth** - bigger swing, even with more uncertainty

### Question 2: What Kind of Environment Helps You Grow Best?

Ask:

"Where do you usually learn faster?"

1. **Structured systems** - clear expectations, strong peers, better feedback loops
2. **Messy environments** - ambiguity, speed, incomplete data, fast adaptation
3. **Depends on manager quality** - the manager matters more than company type
4. **Not sure** - I need help reasoning from recent experience

### Question 3: What Risk Can You Actually Carry?

Ask:

"How much real career and financial risk can you tolerate right now?"

1. **Low** - I need stability and downside protection
2. **Moderate** - I can take some risk, but not chaos
3. **High** - I can handle volatility if the upside is real
4. **Selective** - I can take startup risk only if the company quality is unusually strong

### Question 4: What Is the Real Constraint?

Ask:

"What constraint should have veto power in this decision?"

1. **Manager quality**
2. **Role scope and title trajectory**
3. **Compensation / runway**
4. **Visa, family, location, or lifestyle**

### Output

Generate:

1. **Recommendation**
   - Big tech
   - Startup
   - "Stay in process and compare specific companies, not archetypes"

2. **Decision memo**
   - why this environment fits now
   - where the other option is more attractive
   - what would need to be true to reverse the recommendation

3. **Risk warnings**
   - biggest failure mode if the user follows the recommendation
   - biggest regret risk if they do not

4. **Interview / diligence checklist**
   - 5 questions to validate the recommended path

5. **Next step**
   - if role choice is still noisy, recommend `pm-mock-interview-workflow`
   - if role narrative is weak, recommend `pm-resume-teardown`

## Examples

### Example Scenario

**Input:** A PM wants faster scope growth, has moderate risk tolerance, learns well in messy environments, and does not need a brand reset.

**Likely recommendation:** Startup, but only if manager quality and company reality are validated.

### Example Decision Logic

If the user says:
- breadth matters most
- messy environments are energizing
- they can carry moderate or high risk
- brand is not the current bottleneck

Then startup will usually dominate, unless the company is weak, the manager is poor, or compensation downside is too large.

## Common Pitfalls

### Pitfall 1: Choosing Prestige Over Need

**Symptom:** The role sounds safer or more impressive, but it does not solve the current career bottleneck.

**Fix:** Optimize for the next stage of compounding, not for social proof.

### Pitfall 2: Romanticizing Startup Scope

**Symptom:** Startup is assumed to mean more impact, but the company is too chaotic or too weak to create real leverage.

**Fix:** Check company quality, manager quality, and actual decision rights.

### Pitfall 3: Treating Equity Like Cash

**Symptom:** Compensation comparisons assume startup upside is guaranteed value.

**Fix:** Separate guaranteed compensation from probabilistic upside.

### Pitfall 4: Ignoring Life Constraints

**Symptom:** The user talks like a free agent but is actually constrained by runway, family, geography, or burnout.

**Fix:** Give the real constraint veto power.

## References

- Ben Horowitz, *The Hard Thing About Hard Things*
- Julie Zhuo, *The Making of a Manager*
- Reforge career frameworks on PM leveling and scope
- [`pm-resume-teardown`](../pm-resume-teardown/SKILL.md)
- [`pm-mock-interview-workflow`](../pm-mock-interview-workflow/SKILL.md)
