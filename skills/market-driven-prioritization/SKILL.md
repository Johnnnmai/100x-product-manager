---
name: market-driven-prioritization
description: Use when ranking roadmap bets and needing market evidence to separate what to build now from what to validate next.
type: component
theme: strategy-positioning
best_for:
  - "Separating validated demand from internal enthusiasm during roadmap planning"
  - "Turning fuzzy feature requests into build, validate, or drop decisions"
  - "Keeping strategic bets tied to real market evidence"
scenarios:
  - "We have 12 candidate initiatives and need to decide which ones are ready for delivery versus validation"
  - "Leadership wants a feature because competitors launched it, but we have weak customer signal"
  - "I need a simple framework for showing what gets built now versus what still needs proof"
estimated_time: "10-15 min"
---

## Purpose

Rank features, initiatives, and strategic bets using **market evidence** rather than stakeholder energy, internal politics, or narrative momentum. Use this to decide what deserves immediate build capacity, what needs fast validation, and what should be parked before it turns into roadmap debt.

The core discipline is simple: ask *"Does the market need this?"* before asking *"Can we build this?"* Strong product teams do not prioritize only by impact and effort. They also prioritize by how real, recent, and decision-relevant the demand signal is.

### 中文

这个技能用于基于 **市场证据** 做优先级判断，而不是被内部意见、声音大的人、或者“看起来很重要”的叙事带着走。

核心原则只有一句话：先问 *市场需不需要*，再问 *团队能不能做*。

## Key Concepts

### Validation Status

| Status | Meaning | Default treatment |
| --- | --- | --- |
| Not validated | mostly assumptions | do not build yet |
| Partially validated | some signals, still uncertain | validate fast |
| Validated | strong evidence of demand | candidate for execution |

### Evidence Types

Good evidence can include:
- repeated customer requests
- churn or loss reasons
- usage or search behavior
- willingness to pay
- competitive pressure with customer relevance
- regulatory or market timing shifts

Weak evidence often sounds like:
- "leadership thinks this matters"
- "competitors have it"
- "AI is hot right now"
- "users will probably want this"

### The Real Priority Rule

If something is **high potential but weakly validated**, the next priority is usually not delivery. The next priority is **validation**.

### When To Use It

- quarterly planning
- feature ranking
- build vs. buy debates
- new product bets
- allocation of engineering bandwidth

### When Not To Use It

- urgent compliance work
- production incidents
- contractual must-do items with no real decision space

### 中文

优先级不是只看影响力和投入，还要看证据强度。

高潜力但低验证的项目，不应该直接进入开发，而应该先进入验证队列。

## Application

### Step 1: List the Candidates

Create a simple table with:
- item name
- user problem
- expected impact
- current evidence

### Step 2: Score Validation Honestly

For each candidate, label it:
- not validated
- partially validated
- validated

Then write down the actual evidence. If there is no evidence, say so directly.

### Step 3: Combine Validation With Impact

Use this default decision logic:

| Condition | Default move |
| --- | --- |
| Validated + high impact | prioritize for delivery |
| Validated + medium/low impact | schedule deliberately |
| Partially validated + high impact | run fast validation next |
| Partially validated + low impact | deprioritize |
| Not validated + high impact | design a proof test first |
| Not validated + low impact | drop or park |

### Step 4: Turn Uncertainty Into Validation Tasks

For partially validated or unvalidated items, define the fastest next step:
- 5 customer calls
- smoke test landing page
- prototype demo
- pricing or willingness-to-pay conversation
- usage-data cut

### Step 5: Publish the Decision

End with:
- what gets built now
- what gets validated next
- what gets dropped
- what assumptions remain

Suggested output format:

```markdown
| Item | Impact | Validation | Evidence | Decision |
| --- | --- | --- | --- | --- |
```

### 中文

推荐流程：
1. 先列候选项
2. 诚实判断验证状态
3. 把“验证强度 + 影响力”一起看
4. 对不确定项设计最快验证动作
5. 明确输出：现在做什么，先验证什么，直接砍什么

## Examples

### Example: B2B SaaS Q2 Prioritization

| Item | Impact | Validation | Evidence | Decision |
| --- | --- | --- | --- | --- |
| API integration | High | Validated | 5 enterprise accounts requested it | Build now |
| Mobile app | High | Not validated | internal assumption only | Validate first |
| Dashboard redesign | Medium | Partially validated | mixed customer feedback | Run targeted research |
| Dark mode | Low | Partially validated | nice-to-have comments only | Deprioritize |

### 中文

这个例子里最常见的错误是把 “高影响” 误当成 “高优先级”。如果没有证据，高影响只是想象中的影响。

## Common Pitfalls

### Treating Internal Opinion As Market Signal

If the only evidence is internal conviction, the item is not validated.

### Prioritizing Excitement Instead of Evidence

Trend pressure, AI pressure, and competitor pressure often create false urgency.

### Leaving the Next Step Ambiguous

If an item is not ready to build, say what validation step should happen next. Otherwise it will return in the next planning cycle as the same unresolved debate.

### 中文

常见问题：
- 把内部共识当成市场需求
- 因为热点或竞争焦虑而误判优先级
- 说“先不做”，但没有给出验证动作

## References

Related skills:
- `skills/prioritization-advisor/SKILL.md`
- `skills/problem-statement/SKILL.md`
- `skills/discovery-process/SKILL.md`
- `skills/rapid-iteration-cycle/SKILL.md`

Example:
- `skills/market-driven-prioritization/examples/sample.md`
