---
name: rapid-iteration-cycle
description: Validate ideas fast with short proof loops. Use lightweight tests to learn before scaling investment.
type: workflow
---

## Purpose

Use this workflow to validate a product idea, feature bet, or growth hypothesis **quickly** instead of turning uncertainty into a long roadmap commitment.

The job of this skill is to turn a vague product bet into a short learning loop: define the hypothesis, design the smallest credible test, gather evidence, and make a hard follow-up decision.

### 中文

这个工作流用于在投入大量研发前，快速验证一个产品想法、功能假设或增长假设。

它的目标不是做一个“迷你版完整产品”，而是把不确定性压缩进一个短周期学习回路里。

## Key Concepts

### MVT, Not MVP

This skill optimizes for a **minimum viable test**, not a minimum viable product.

That means:
- test the assumption, not the whole roadmap
- use the smallest believable experience
- prefer speed of learning over polish

### Standard Cadence

| Phase | Typical timing | Output |
| --- | --- | --- |
| Define | Day 1 | hypothesis, metric, kill condition |
| Build | Days 2-5 | test asset or prototype |
| Test | Days 6-12 | real-user exposure and evidence |
| Decide | Days 13-14 | scale, iterate, or stop |

### Good Hypothesis Format

```text
If we change [thing], then [metric or behavior] should improve because [reason].
```

### When To Use It

- new feature bets
- onboarding experiments
- pricing or packaging tests
- market validation before roadmap commitment

### When Not To Use It

- urgent defects
- mandatory compliance work
- work where the decision is already fixed

### 中文

关键点：
- 做最小可行验证，不做最小可行产品
- 用最短周期换最快学习
- 结果必须能导向明确决策：扩、改、停

## Application

### Phase 1: Define the Bet

Write down:
- the problem being tested
- the hypothesis
- the primary success metric
- the kill condition

If you cannot define the kill condition, the test is too vague.

### Phase 2: Design the Smallest Credible Test

Possible test formats:
- clickable prototype
- concierge workflow
- fake-door or smoke test
- pricing conversation
- limited beta with manual backend

Ask:
- what is the smallest version that still produces believable evidence?

### Phase 3: Run the Test

Decide before launch:
- target audience
- duration
- sample threshold
- what qualitative evidence you will collect

Avoid changing the test halfway through unless the test is clearly broken.

### Phase 4: Decide

Use one of three outcomes:

| Outcome | Meaning | Next move |
| --- | --- | --- |
| Validated | evidence supports the bet | scale or invest further |
| Partially validated | some signal, still unclear | revise and rerun |
| Invalidated | evidence does not support the bet | stop or pivot |

### Phase 5: Capture the Learning

Always document:
- what was tested
- what signal was observed
- what surprised the team
- what decision follows now

### 中文

执行顺序：
1. 先定义假设、主指标、终止条件
2. 设计最小但可信的验证方式
3. 运行测试并收集定量/定性证据
4. 明确输出：通过、部分通过、未通过
5. 把学习沉淀成下一步动作

## Examples

### Example: Onboarding Simplification

Hypothesis:
- if onboarding drops from five steps to two, activation should improve because fewer users abandon the flow

MVT:
- launch a simplified prototype for a controlled cohort

Decision:
- if activation increases by at least 15 percent without lowering downstream quality, expand the test

### 中文

一个好例子通常满足三点：
- 测试对象清楚
- 成败标准清楚
- 下一步动作清楚

## Common Pitfalls

### Building Too Much

If the team spends most of the cycle building infrastructure, the test is too heavy.

### Using Too Many Metrics

One primary metric is better than five weak ones. Use secondary metrics only as guardrails.

### Running the Test Without a Decision Rule

If nobody knows what result is enough to continue, the experiment becomes theater.

### 中文

常见错误：
- 把验证做成开发项目
- 指标太多导致结论模糊
- 开始前没有定义“什么结果算通过”

## References

Related skills:
- `skills/market-driven-prioritization/SKILL.md`
- `skills/pol-probe/SKILL.md`
- `skills/pol-probe-advisor/SKILL.md`
- `skills/discovery-process/SKILL.md`
