---
name: market-driven-prioritization
description: Prioritize features based on market validation rather than internal opinions. Ask "Does the market need this?" before "Can we build this?"
type: component
---

## English

### Purpose

Prioritize features, initiatives, or projects based on **market validation** rather than internal opinions or political alignment. Ask "Does the market need this?" before "Can we build this?"

This skill ensures every prioritization decision is backed by market evidence, not just internal assumptions.

### Key Concepts

**Market Validation Status:**

| Status | Description | Priority |
|--------|-------------|----------|
| 🔴 **Not Validated** | Assumptions only, no market evidence | Lowest |
| 🟡 **Partially Validated** | Some signals, need more validation | Medium |
| 🟢 **Validated** | Clear market demand, data-supported | Highest |

**Market Validation Criteria:**

1. **User Demand Evidence**
   - Do users explicitly ask for this?
   - Is there search/data evidence of demand?
   - Are competitors building this?

2. **Market Timing**
   - Is the market ready for this?
   - Are there regulatory/external tailwinds?
   - Is there a window of opportunity?

3. **Competitive Advantage**
   - Does this create defensibility?
   - Does this capture market share?
   - Does this block competitors?

### When to Use This

- Prioritizing features for next quarter
- Making build vs. buy decisions
- Evaluating new product ideas
- Allocating engineering resources

### When NOT to Use This

- When you have clear regulatory requirements (compliance comes first)
- When there's no time for validation (emergency features)

---

## 中文

### 目的

基于**市场验证**而非内部观点或政治倾向来优先排序功能、计划或项目。在问"我们能构建这个吗？"之前，先问"市场需要这个吗？"

此技能确保每个优先排序决策都有市场证据支持，而非仅仅是内部假设。

### 核心概念

**市场验证状态：**

| 状态 | 描述 | 优先级 |
|------|------|--------|
| 🔴 **未验证** | 仅有假设，无市场证据 | 最低 |
| 🟡 **部分验证** | 一些信号，需要更多验证 | 中等 |
| 🟢 **已验证** | 明确市场需求，数据支持 | 最高 |

**市场验证标准：**

1. **用户需求证据**
   - 用户是否明确要求这个？
   - 是否有搜索/数据证据证明需求？
   - 竞争对手是否在构建这个？

2. **市场时机**
   - 市场是否准备好了？
   - 是否有监管/外部顺风？
   - 是否有时机窗口？

3. **竞争优势**
   - 这是否创造了护城河？
   - 这是否占据了市场份额？
   - 这是否阻止了竞争对手？

### 何时使用

- 为下季度优先排序功能
- 做出构建vs购买决策
- 评估新产品想法
- 分配工程资源

### 何时不使用

- 当有明确的监管要求时（合规优先）
- 当没有时间验证时（紧急功能）

---

## Application / 应用

### Step 1: List All Candidates / 列出所有候选项

List all features/initiatives to prioritize with their basic description.

### Step 2: Assess Market Validation Status / 评估市场验证状态

For each candidate, assign one of these statuses: 🔴 Not Validated, 🟡 Partially Validated, 🟢 Validated

### Step 3: Prioritize by Validation + Impact / 按验证状态+影响力优先

**Priority Order:**
1. 🟢 Validated + High Impact (DO FIRST)
2. 🟢 Validated + Low Impact (Schedule)
3. 🟡 Partially Validated + High Impact (Validate Fast)
4. 🟡 Partially Validated + Low Impact (Deprioritize)
5. 🔴 Not Validated + High Impact (Pivot)
6. 🔴 Not Validated + Low Impact (Drop)

### Output Template / 输出模板

| Feature | Impact | Validation Status | Validation Evidence | Priority |
|---------|--------|-----------------|-------------------|----------|
| | High/Med/Low | 🔴/🟡/🟢 | | P1/P2/P3/P4 |

---

## Key Principle / 关键原则

**Speed matters**: If something is 🟡 Partial + High Impact, the priority is NOT to build it—it's to VALIDATE it fast.

**速度很重要**：如果某个项目是🟡部分验证+高影响力，优先级不是构建它——而是快速验证它！

---

## Common Pitfalls / 常见陷阱

### Pitfall 1: Internal Opinion as Validation
**Symptom:** "We think users want this"

**Fix:** Always ask for market evidence. What data supports this?

### Pitfall 2: Prioritizing Without Validation
**Symptom:** Building features that are "obviously needed"

**Fix:** Even obvious needs should be validated. The market is always right.

### Pitfall 3: Analysis Paralysis
**Symptom:** Never validating because "perfect data" doesn't exist

**Fix:** Start with what you have. 5 user interviews > 0 interviews.

---

## Examples / 示例

**Scenario:** Prioritizing new features for a B2B SaaS product

| Feature | Impact | Validation Status | Priority |
|---------|--------|-------------------|----------|
| API Integration | High | 🟢 Validated (5 customers asked) | P1 |
| Mobile App | High | 🔴 Not Validated (assumptions only) | P3 |
| Dashboard Redesign | Medium | 🟡 Partial (mixed feedback) | P2 |
| Dark Mode | Low | 🟡 Partial (nice to have) | P4 |

---

## Related Skills / 相关技能

- `skills/problem-statement/SKILL.md` — Define the problem first
- `skills/discovery-process/SKILL.md` — Validate market needs
- `skills/prioritization-advisor/SKILL.md` — Additional prioritization frameworks

---

**Skill type:** Component
**Suggested filename:** `market-driven-prioritization.md`
**Suggested placement:** `/skills/components/`
**Dependencies:** None
