# Launch Decision Engine / 发布决策引擎

[English](#english) | [中文](#中文)

---

## English

### When to Use This Skill

Use this when you need to make a **go/no-go decision** for a feature launch.

### Interactive Process

I'll guide you through a structured launch decision.

---

### Step 1: Define the Launch

**What are we launching?**
- Feature/Product: _________
- Target users: _________
- Launch scope: _________

---

### Step 2: Go/No-Go Checklist

Rate each item (Pass/Partial/Fail):

#### Product Quality
- [ ] Feature complete?
- [ ] No critical bugs?
- [ ] Performance acceptable?
- [ ] Security review passed?

#### Market Readiness
- [ ] Market need validated?
- [ ] Timing is right?
- [ ] Competitive advantage clear?
- [ ] Users asking for it?

#### Business Readiness
- [ ] Pricing defined?
- [ ] Support process ready?
- [ ] Marketing assets ready?
- [ ] Legal/compliance cleared?

#### Technical Readiness
- [ ] Infrastructure ready?
- [ ] Monitoring in place?
- [ ] Rollback plan exists?
- [ ] Feature flags configured?

---

### Step 3: Score Summary

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Product Quality | _/4 | 25% | |
| Market Readiness | _/4 | 35% | |
| Business Readiness | _/4 | 20% | |
| Technical Readiness | _/4 | 20% | |
| **Total** | | 100% | |

**Score Key:**
- 4 = All pass
- 3 = 1 partial
- 2 = 1 fail
- 1 = Multiple failures

---

### Step 4: Decision Matrix

```
                    High Confidence
                        │
   Fix Critical +     │    GO ✅
   Market Ready       │
   ───────────────────┼──────────────────
   Market Not Ready   │    NO ❌
   + Low Confidence   │    or Wait
                        │
                   Low Confidence
```

---

### Step 5: Decision

**Recommendation: [ ] GO / [ ] NO-GO / [ ] CONDITIONAL GO**

Conditions (if conditional):
1. _________
2. _________
3. _________

---

### Step 6: Risk Mitigation

| Risk | Mitigation | Owner |
|------|------------|-------|
| | | |

---

### Key Principle

**Speed + Confidence:**
- Don't launch for perfection
- Launch when confident enough
- Have rollback ready

---

## 中文

### 何时使用此技能

当需要为功能发布做**通过/不通过**决策时使用。

### 交互式流程

我将引导你完成结构化的发布决策。

---

### 第一步：定义发布

**我们在发布什么？**
- 功能/产品：_________
- 目标用户：_________
- 发布范围：_________

---

### 第二步：通过/不通过清单

评估每个项目（通过/部分通过/失败）：

####产品质量
- [ ] 功能完成？
- [ ] 无关键 bug？
- [ ] 性能可接受？
- [ ] 安全审查通过？

#### 市场准备度
- [ ] 市场需求已验证？
- [ ] 时机正确？
- [ ] 竞争优势清晰？
- [ ] 用户要求？

#### 业务准备度
- [ ] 定价已定？
- [ ] 支持流程就绪？
- [ ] 营销素材就绪？
- [ ] 法律/合规批准？

#### 技术准备度
- [ ] 基础设施就绪？
- [ ] 监控到位？
- [ ] 回滚计划存在？
- [ ] 特性开关配置？

---

### 第三步：分数汇总

| 类别 | 分数 | 权重 | 加权 |
|------|------|------|------|
| 产品质量 | _/4 | 25% | |
| 市场准备度 | _/4 | 35% | |
| 业务准备度 | _/4 | 20% | |
| 技术准备度 | _/4 | 20% | |
| **总计** | | 100% | |

**分数说明：**
- 4 = 全部通过
- 3 = 1个部分通过
- 2 = 1个失败
- 1 = 多个失败

---

### 第四步：决策矩阵

```
                    高信心度
                        │
   修复关键问题 +     │    通过 ✅
   市场已就绪         │
   ───────────────────┼──────────────────
   市场未就绪         │    不通过 ❌
   + 低信心度         │    或等待
                        │
                   低信心度
```

---

### 第五步：决策

**建议：[ ] 通过 / [ ] 不通过 / [ ] 有条件通过**

条件（如有条件）：
1. _________
2. _________
3. _________

---

### 第六步：风险缓解

| 风险 | 缓解措施 | 负责人 |
|------|----------|--------|
| | | |

---

### 关键原则

**速度 + 信心：**
- 不要为了完美而发布
- 在足够有信心时发布
- 准备好回滚
