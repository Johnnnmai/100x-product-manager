# 100x PM Skills → AI OS Agent Architecture Mapping

本文档展示如何复用现有的 100x-product-managers skills 到新的 AI OS Agent 架构。

## 映射原则

- **不移动原始文件**: 技能保持原位置，只创建引用/链接
- **分层复用**: 不同层级调用不同技能
- **编译式调用**: PM Compiler 按需调用技能，不是一次性加载全部

---

## PM Compiler Agent Skills 映射

| 技能 | 阶段 | 输入 | 输出 | 复用方式 |
|------|------|------|------|---------|
| `market-driven-prioritization` | 优先级 | market data | priority score | 链接引用 |
| `10x-hypothesis-framework` | 假设 | problem statement | hypothesis doc | 链接引用 |
| `epic-breakdown-advisor` | Epic分解 | epic request | epic breakdown | 链接引用 |
| `opportunity-solution-tree` | 任务树 | opportunity | task tree | 链接引用 |
| `prd-development` | PRD | feature request | PRD doc | 链接引用 |
| `roadmap-planning` | Roadmap | initiatives | roadmap | 链接引用 |
| `launch_checklist` | 发布检查 | launch scope | checklist | 链接引用 |
| `mvp_cutline` | MVP定义 | full scope | MVP scope | 链接引用 |

---

## Control Plane Skills 映射

### Chief of Staff

| 技能 | 用途 |
|------|------|
| `product-strategy-session` | 战略会议 |
| `roadmap-planning` | 路线图规划 |
| `stakeholder_map` | 利益相关方映射 |

### CTO

| 技能 | 用途 |
|------|------|
| `architecture-review-checklist` | 架构评审 |
| `tech-debt-prioritization` | 技术债务优先级 |

### Research Lead

| 技能 | 用途 |
|------|------|
| `company-research` | 公司调研 |
| `discovery-process` | 发现流程 |
| `experiment_design` | 实验设计 |
| `metrics_tree` | 指标树 |

### Growth Lead

| 技能 | 用途 |
|------|------|
| `acquisition-channel-advisor` | 获客渠道 |
| `business-health-diagnostic` | 业务诊断 |
| `saas-revenue-growth-metrics` | 增长指标 |
| `tam-sam-som-calculator` | 市场规模 |
| `pricing-strategy-advisor` | 定价策略 |

### QA Director

| 技能 | 用途 |
|------|------|
| `test-strategy-template` | 测试策略 |
| `quality-gates-definition` | 质量门禁 |

---

## AI Revenue Flywheel 技能映射

基于新的业务架构，新增以下技能需求:

### Signal Layer

| 技能 | Agent | 输入 | 输出 |
|------|-------|------|------|
| `trend-scouting` | Trend Scout Agent | 平台热门 | Signal Cards |
| `competitor-scan` | Competitor Scan Agent | 竞品列表 | Competitor Analysis |

### Offer Layer

| 技能 | Agent | 输入 | 输出 |
|------|-------|------|------|
| `offer-architecture` | Offer Architect Agent | Signal Card | Offer Card |
| `pricing-strategy` | Pricing Agent | Market data | Pricing model |

### Asset Layer

| 技能 | Agent | 输入 | 输出 |
|------|-------|------|------|
| `ebook-generation` | Ebook Factory Agent | Outline | PDF/Epub |
| `template-generation` | Template Factory Agent | Spec | Notion/Excel |

### Content Layer

| 技能 | Agent | 输入 | 输出 |
|------|-------|------|------|
| `hook-generation` | Hook Agent | Product | Hook variants |
| `script-writing` | Script Agent | Product | Script |
| `post-writing` | Post Agent | Script | Posts |

### Funnel Layer

| 技能 | Agent | 输入 | 输出 |
|------|-------|------|------|
| `landing-page-gen` | Landing Page Agent | Offer | Landing page |
| `lead-magnet-gen` | Lead Magnet Agent | Product | Free asset |
| `website-builder` | Website Builder Agent | Spec | Website |

### Sales Layer

| 技能 | Agent | 输入 | 输出 |
|------|-------|------|------|
| `sales-copy` | Sales Copy Agent | Product | Sales copy |
| `checkout-ops` | Checkout Ops Agent | Product | Checkout flow |

### Retention Layer

| 技能 | Agent | 输入 | 输出 |
|------|-------|------|------|
| `email-sequence` | Email Sequence Agent | Product | Email series |
| `community-setup` | Community Agent | Product | Community |

### Analytics Layer

| 技能 | Agent | 输入 | 输出 |
|------|-------|------|------|
| `attribution-tracking` | Attribution Agent | Revenue events | Attribution |
| `experiment-design` | Experiment Agent | Hypothesis | Experiment |
| `metrics-dashboard` | Metrics Agent | Raw data | Dashboard |

---

## 技能引用结构

在 `ai_os/agents/pm_compiler/skills/` 创建引用文件:

```
ai_os/agents/pm_compiler/skills/
├── market-driven-prioritization.md -> ../../100x-product-managers/skills/market-driven-prioritization/SKILL.md
├── 10x-hypothesis-framework.md -> ../../100x-product-managers/skills/10x-hypothesis-framework/SKILL.md
├── epic-breakdown-advisor.md -> ../../100x-product-managers/skills/epic-breakdown-advisor/SKILL.md
├── opportunity-solution-tree.md -> ../../100x-product-managers/skills/opportunity-solution-tree/SKILL.md
└── prd-development.md -> ../../100x-product-managers/skills/prd-development/SKILL.md
```

使用符号链接或相对路径引用，避免文件复制。

---

## 执行流程示例

### 场景: 新数字产品开发

```
1. [Trend Scout Agent]
   → skill: trend-scouting (new)
   → input: TikTok trending, XHS hot, Amazon bestseller
   → output: 10 Signal Cards

2. [Offer Architect Agent]
   → skill: offer-architecture (new)
   → input: Signal Card #1
   → output: Offer Card (pm-interview-os-v1)

3. [PM Compiler Agent]
   → skills: market-driven-prioritization + 10x-hypothesis-framework
   → input: Offer Card
   → output: TaskEnvelope

4. [Ebook Factory Agent]
   → skill: ebook-generation (new)
   → input: Offer Card + TaskEnvelope
   → output: PDF ebook

5. [Hook/Script/Post Agents]
   → skills: hook-generation, script-writing, post-writing
   → input: Ebook content
   → output: 30 TikToks, 50 posts, 10 articles

6. [Distribution Agents]
   → skills: scheduler, channel posting
   → input: Content
   → output: Published posts + links

7. [Landing Page Agent]
   → skill: landing-page-gen
   → input: Offer Card
   → output: Landing page with checkout

8. [Revenue Tracking]
   → skill: attribution-tracking
   → input: Purchase events
   → output: Revenue metrics

9. [Experiment Agent]
   → skill: experiment-design
   → input: Hypothesis (Hook A vs B)
   → output: Experiment result

10. [Memory Agent]
    → Update lessons learned
    → Signal for next iteration
```

---

## 实施优先级

### Phase 1: 复用现有
- [x] market-driven-prioritization
- [x] 10x-hypothesis-framework
- [x] epic-breakdown-advisor
- [x] opportunity-solution-tree

### Phase 2: 新建核心
- [ ] trend-scouting (Signal)
- [ ] offer-architecture (Offer)
- [ ] ebook-generation (Asset)

### Phase 3: 扩展内容
- [ ] hook-generation
- [ ] script-writing
- [ ] post-writing

### Phase 4: 扩展分发
- [ ] landing-page-gen
- [ ] distribution automation

### Phase 5: 扩展销售
- [ ] sales-copy
- [ ] checkout-ops
- [ ] revenue-tracking

---

## 总结

通过这个映射:
- **现有技能**: 77个 PM Skills → PM Compiler + Control Plane
- **新增技能**: 按飞轮阶段逐步实现
- **复用方式**: 引用而非复制，保持单一事实来源
