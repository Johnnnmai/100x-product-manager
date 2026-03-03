# 100X PM Skills / 100X 产品经理技能体系

[English](#english) | [中文](#中文)

---

## English

### Philosophy

**10X vs 100X: What's the Difference?**

| Concept | Focus | Description |
|---------|-------|-------------|
| **10X PM** | Personal Efficiency | Individual productivity gains - work faster, better |
| **100X PM** | Organizational Leverage | Change team/organization output curve through systems |

**Our Focus: 100X Only**

10X is "work harder," 100X is "fewer decisions but higher accuracy" - turning uncertainty into controllable variables.

---

### The 6 MECE Decision Categories

Every PM must answer these 6 questions. Each has unique failure modes:

| Category | Question | Failure Mode |
|----------|----------|--------------|
| **Outcome** | What result should users get? | Building useless products |
| **Evidence** | How do we prove it works? | Blind optimization |
| **Solution** | What do we build/not build? | Endless rework |
| **Delivery** | How do we ship on time? | Death by delay |
| **Risk** | How do we fail safely? | Catastrophic launches |
| **Alignment** | Who decides, who blocks? | Internal耗 |

---

### 12 Core Skill Cards

#### A. Outcome (2 cards)
1. Problem Framing & Outcome Spec
2. Service Blueprint (Product is Service)

#### B. Evidence (2 cards)
3. Metrics Tree & Counter Metrics
4. Experiment Design (A/B or Quasi-experiment)

#### C. Solution (2 cards)
5. MVP Cutline & Non-goals
6. Edge Cases & Non-functional Requirements

#### D. Delivery (2 cards)
7. Milestone Plan & Critical Path
8. Launch Readiness Review (LRR)

#### E. Risk (2 cards)
9. Rollout & Rollback Plan
10. Abuse & Threat Model

#### F. Alignment (2 cards)
11. Stakeholder Map & Decision Owner
12. Exec Narrative (1 page)

---

### 3 Playbooks

| Playbook | When to Use | Duration |
|----------|-------------|----------|
| **startup_mvp_0_to_1** | New product from 0 to 1 | 2-4 weeks |
| **bigtech_feature_launch** | New feature in large org | 4-8 weeks |
| **regulated_platform_change** | Financial/Security/Infrastructure | 8-12 weeks |

---

### Quick Start

**For Startup:**
```
1 → 5 → 7 → 3 → 9 (required)
2 → 4 (optional)
```

**For Big Tech:**
```
1 → 3 → 4 → 6 → 8 → 9 → 10 → 11 → 12 (required)
2 → 7 (optional)
```

**For Regulated Products:**
```
1 → 2 → 3 → 6 → 8 → 9 → 10 → 11 → 12 (required)
+ Compliance checklist, audit logging spec
```

---

## 中文

### 核心理念

**10X vs 100X：区别是什么？**

| 概念 | 重点 | 描述 |
|------|------|------|
| **10X PM** | 个人效率 | 个人生产力提升 - 更快、更好地工作 |
| **100X PM** | 组织杠杆 | 通过系统改变团队/组织的产出曲线 |

**我们的重点：只做100X**

10X是"更努力"，100X是"更少决策但更高准确率"——把不确定性变成可控变量。

---

### 6类 MECE 决策框架

每个PM必须回答这6个问题。每类都有独特的失败模式：

| 类别 | 问题 | 失败模式 |
|------|------|----------|
| **Outcome 结果** | 用户应该获得什么结果？ | 构建无用的产品 |
| **Evidence 证据** | 如何证明它有效？ | 盲目优化 |
| **Solution 方案** | 构建什么、不构建什么？ | 无限返工 |
| **Delivery 交付** | 如何按时发布？ | 拖延致死 |
| **Risk 风险** | 如何安全失败？ | 灾难性发布 |
| **Alignment 对齐** | 谁决定、谁阻塞？ | 内部消耗 |

---

### 12张核心 Skill Cards

#### A. Outcome 结果 (2张)
1. 问题定义与结果规范
2. 服务蓝图（产品即服务）

#### B. Evidence 证据 (2张)
3. 指标树与反指标
4. 实验设计 (A/B 或准实验)

#### C. Solution 方案 (2张)
5. MVP 切分线与非目标
6. 边缘情况与非功能需求

#### D. Delivery 交付 (2张)
7. 里程碑计划与关键路径
8. 发布就绪审查 (LRR)

#### E. Risk 风险 (2张)
9. 灰度发布与回滚计划
10. 滥用与威胁模型

#### F. Alignment 对齐 (2张)
11. 利益相关方地图与决策所有者
12. 高管叙事（一页纸）

---

### 3个 Playbooks

| Playbook | 适用场景 | 时长 |
|----------|----------|------|
| **startup_mvp_0_to_1** | 从0到1的新产品 | 2-4周 |
| **bigtech_feature_launch** | 大厂新功能 | 4-8周 |
| **regulated_platform_change** | 金融/安全/基础设施 | 8-12周 |

---

### 快速开始

**Startup 场景：**
```
1 → 5 → 7 → 3 → 9（必做）
2 → 4（可选）
```

**Big Tech 场景：**
```
1 → 3 → 4 → 6 → 8 → 9 → 10 → 11 → 12（必做）
2 → 7（可选）
```

**受监管产品场景：**
```
1 → 2 → 3 → 6 → 8 → 9 → 10 → 11 → 12（必做）
+ 合规清单、审计日志规范
```

---

## Directory Structure

```
100x-product-managers/
├── README.md                    # This file
├── 00_Glossary/
│   └── 100x_pm.md             # Terminology definitions
├── 01_Skill_Cards/
│   ├── template.md             # Skill card template
│   ├── outcome/               # Category A
│   │   ├── 01_problem_framing.md
│   │   └── 02_service_blueprint.md
│   ├── evidence/             # Category B
│   │   ├── 03_metrics_tree.md
│   │   └── 04_experiment_design.md
│   ├── solution/             # Category C
│   │   ├── 05_mvp_cutline.md
│   │   └── 06_edge_cases.md
│   ├── delivery/             # Category D
│   │   ├── 07_milestone_plan.md
│   │   └── 08_launch_readiness.md
│   ├── risk/                # Category E
│   │   ├── 09_rollout_rollback.md
│   │   └── 10_threat_model.md
│   └── alignment/            # Category F
│       ├── 11_stakeholder_map.md
│       └── 12_exec_narrative.md
├── 02_Playbooks/
│   ├── startup_mvp_0_to_1.md
│   ├── bigtech_feature_launch.md
│   └── regulated_platform_change.md
└── 03_Artifacts/
    └── [Referenced in skill cards]
```

---

## License

CC BY-NC-SA 4.0
