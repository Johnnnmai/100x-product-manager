# Market-Driven Prioritization / 市场驱动的优先级框架

[English](#english) | [中文](#中文)

---

## English

### When to Use This Skill

Use this when you need to prioritize features, initiatives, or projects based on **market validation** rather than internal opinions.

### Core Question

**"Does the market really need this?"**

### The Framework

#### Step 1: List All Candidates
List all features/initiatives to prioritize with their basic description.

#### Step 2: Assess Market Validation Status

For each candidate, assign one of these statuses:

| Status | Description | Priority |
|--------|-------------|----------|
| 🔴 **Not Validated** | Assumptions only, no market evidence | Lowest |
| 🟡 **Partially Validated** | Some signals, need more validation | Medium |
| 🟢 **Validated** | Clear market demand, data-supported | Highest |

#### Step 3: Market Validation Criteria

Evaluate each candidate against these questions:

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

#### Step 4: Prioritize by Validation + Impact

Create a 2x2 matrix:

```
                    High Impact
                        │
      🟢 Validate +    │    🟢 Validate +
      🟡 Partial       │    🔴 Not Validated
      ─────────────────┼──────────────────
      🟡 Partial +     │    🔴 Not Validated
      🔴 Not Validated │    + Low Impact
                        │
                   Low Impact
```

**Priority Order:**
1. 🟢 Validated + High Impact (DO FIRST)
2. 🟢 Validated + Low Impact (Schedule)
3. 🟡 Partial + High Impact (Validate Fast)
4. 🟡 Partial + Low Impact (Deprioritize)
5. 🔴 Not Validated + High Impact (Pivot)
6. 🔴 Not Validated + Low Impact (Drop)

### Output Template

| Feature | Impact | Validation Status | Validation Evidence | Priority |
|---------|--------|-----------------|-------------------|----------|
| | High/Med/Low | 🔴/🟡/🟢 | | P1/P2/P3/P4 |

### Key Principle

**Speed matters**: If something is 🟡 Partial + High Impact, the priority is NOT to build it - it's to VALIDATE it fast.

---

## 中文

### 何时使用此技能

当需要基于**市场验证**而非内部观点来优先排序功能、计划或项目时使用。

### 核心问题

**"市场真的需要这个吗？"**

### 框架

#### 第一步：列出所有候选项
列出所有待优先排序的功能/计划，附带基本描述。

#### 第二步：评估市场验证状态

为每个候选项分配以下状态之一：

| 状态 | 描述 | 优先级 |
|------|------|--------|
| 🔴 **未验证** | 仅有假设，无市场证据 | 最低 |
| 🟡 **部分验证** | 一些信号，需要更多验证 | 中等 |
| 🟢 **已验证** | 明确市场需求，有数据支持 | 最高 |

#### 第三步：市场验证标准

根据以下问题评估每个候选项：

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

#### 第四步：按验证状态 + 影响力优先

创建 2x2 矩阵：

```
                    高影响力
                        │
      🟢 已验证 +      │    🟢 已验证 +
      🟡 部分验证      │    🔴 未验证
      ─────────────────┼──────────────────
      🟡 部分验证 +    │    🔴 未验证 +
      🔴 未验证        │    低影响力
                        │
                   低影响力
```

**优先级顺序：**
1. 🟢 已验证 + 高影响力（优先做）
2. 🟢 已验证 + 低影响力（安排做）
3. 🟡 部分验证 + 高影响力（快速验证）
4. 🟡 部分验证 + 低影响力（降低优先级）
5. 🔴 未验证 + 高影响力（转向）
6. 🔴 未验证 + 低影响力（放弃）

### 输出模板

| 功能 | 影响力 | 验证状态 | 验证证据 | 优先级 |
|------|--------|----------|----------|--------|
| | 高/中/低 | 🔴/🟡/🟢 | | P1/P2/P3/P4 |

### 关键原则

**速度很重要**：如果某个项目是 🟡 部分验证 + 高影响力，优先级不是构建它——而是快速验证它！
