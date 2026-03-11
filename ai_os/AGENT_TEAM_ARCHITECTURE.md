# AI OS Agent Team & Swarm Architecture

基于现有代码结构复用设计的完整 Agent Team 方案。

## 一、现有资源分析

### 可直接复用的模块

| 现有资源 | 复用价值 | 对应新架构 |
|---------|---------|-----------|
| `100x-product-managers/` | 77个 PM Skills | **PM Compiler** 核心能力 |
| `ops/TASK_BOARD.md` | 任务状态管理 | **Control Plane** 任务调度 |
| `ops/tasks/{pending,running,done}/` | 任务队列 | **Worker Swarm** 执行状态 |
| `ops/approvals/{pending,approved,rejected}/` | 审批流程 | **Discord Approval Hub** |
| `ops/context_bundles/` | 上下文管理 | **Context Hub** |
| `ops/evidence/{raw,processed}/` | 证据采集 | **Evidence Ingestion Worker** |
| `ops/discord/outbox/` | Discord 集成 | **Discord Gateway** |
| `ops/paperclip/outbox/` | Paperclip 集成 | **Paperclip Gateway** |
| `ops/strategy_lab/{requests,reports}/` | 策略实验室 | **Strategy Lab Interface** |
| `ops/legacy/LEGACY_EXECUTION_ADAPTER.md` | 旧执行适配器 | **Legacy Adapter** |
| `scripts/sync_paperclip_agents.py` | Agent 同步 | **Agent Registry Sync** |
| `scripts/provision_company_portfolio.py` | 项目初始化 | **Portfolio Provisioner** |

---

## 二、Agent Team 架构

### 层级 1: PM Compiler (产品经理编译层)

**定位**: 替代原来的"100x PM 直接执行"，改为编译产出物

**复用**: 将 `100x-product-managers` skills 重构为编译管道

```
输入: raw PM request / strategy session
     ↓
执行链:
  1. market-driven-prioritization → priority score
  2. 10x-hypothesis-framework → hypothesis document
  3. epic-breakdown-advisor → epic breakdown
  4. opportunity-solution-tree → task tree
     ↓
输出: TaskEnvelope (JSON)
```

**TaskEnvelope 合同**:
```json
{
  "goal_id": "string",
  "initiative_id": "string",
  "epic_id": "string",
  "task_id": "string",
  "executor_type": "cloud_build | cloud_qa | cloud_research | local_fallback",
  "budget_cap": "number",
  "approval_required": "boolean",
  "context_bundle_ref": "path/to/context_bundle.json",
  "artifact_output_path": "path/to/output/",
  "acceptance_criteria": ["criterion1", "criterion2"],
  "latest_decisions": ["decision1", "decision2"]
}
```

### 层级 2: Control Plane (控制面)

**定位**: Paperclip 作为公司级控制面

**复用**: `ops/paperclip/outbox/` + `scripts/sync_paperclip_agents.py`

**核心 Agent 角色**:

| Agent | 职责 | 复用现有 |
|-------|------|---------|
| `CEO Agent` | portfolio 所有权, 优先级决策 | AI_OS_ARCHITECTURE.md 定义 |
| `Chief of Staff Agent` | 计划分解, issue tree 构建 | 复用 100x-product-managers skills |
| `CTO Agent` | 关键技术路径所有权 | 新建 |
| `QA Director Agent` | 发布门禁, 验证标准 | 新建 |
| `Research Lead Agent` | evidence 所有权, 调研统筹 | 新建 |
| `Growth Lead Agent` | GTM 策略, 增长路径 | 新建 |

### 层级 3: Execution Worker Swarm (执行 Worker 群)

**定位**: 分布式执行池，复用现有 OpenClaw/Claude Code/Codex

**复用**: `ops/EXECUTION_FLOW.md` + `ops/AGENT_RULES.md`

| Worker | 职责 | 运行时 |
|--------|------|--------|
| `Cloud Build Worker` | 构建、编码、实现 | OpenClaw build gateway |
| `Cloud QA Worker` | 测试、验证、回归 | OpenClaw verify gateway |
| `Cloud Research Worker` | 调研、证据采集、竞品分析 | OpenClaw research gateway |
| `Local Codex Builder` (fallback) | 本地紧急编码 | local Codex |
| `Staff Engineer` (fallback) | 本地技术审查 | local Claude |

### 层级 4: Context & Evidence Layer

**定位**: 上下文编译 + 证据采集

**复用**:

| Agent | 职责 | 复用现有 |
|-------|------|---------|
| `Context Compiler` | 从 Git markdown 编译 bounded context | `ops/context_bundles/` |
| `Evidence Ingestion Worker` | 调用 Scrapling 采集结构化证据 | `ops/evidence/raw/` |
| `Context Hub` | 外部 API/框架文档获取 | 新建，参考 `context-hub` |

**ContextBundle 合同**:
```json
{
  "mission": "task goal description",
  "constraints": ["budget", "timeline", "tech_constraints"],
  "evidence_refs": ["path/to/evidence1", "path/to/evidence2"],
  "glossary": {"term": "definition"},
  "latest_decisions": ["decision1", "decision2"]
}
```

### 层级 5: Discord Approval Hub

**定位**: 人类审批 + 告警中心

**复用**: `ops/discord/outbox/`

**消息类型**:
- `approval_requested`: 需要人工审批
- `run_blocked`: 执行阻塞
- `budget_threshold_hit`: 预算阈值触发
- `run_completed`: 执行完成摘要

### 层级 6: Strategy Lab Interface (预测层预留)

**定位**: OASIS / MiroFish 接口预留

**复用**: `ops/strategy_lab/{requests,reports}/`

**合同**:

```json
// ForecastRequest
{
  "seed_material_refs": ["path/to/material1"],
  "decision_question": "what if we launch X?",
  "time_horizon": "Q3 2026",
  "scenario_prompt": "描述要模拟的场景"
}

// ForecastReport
{
  "scenario_summary": "string",
  "key_drivers": ["driver1", "driver2"],
  "risk_signals": ["signal1", "signal2"],
  "roadmap_implications": ["implication1"]
}
```

---

## 三、Swarm 协作模式

### 模式 1: PM → Control → Worker 流水线

```
[PM Compiler]
   ↓ TaskEnvelope
[Paperclip Control Plane]
   ↓
   ├─→ [Approval Required?]
   │       ↓ Yes → [Discord Hub] → Human
   │       ↓ No
   ↓
[Worker Swarm] → Cloud Build / QA / Research
   ↓
[Report] → [Paperclip] → [Discord Completion]
```

### 模式 2: Context Bundle 编译

```
[Context Hub Agent]
   ↓
   ├─ Git markdown (internal)
   ├─ context-hub (external APIs)
   └─ Scrapling (evidence)
   ↓
[Context Compiler] → ContextBundle
   ↓
[Worker] 只消费自己的 ContextBundle
```

### 模式 3: Strategy Lab 独立通道

```
[Strategy Lab Request]
   ↓
[Paperclip Strategy Interface]
   ↓
[OASIS / MiroFish] (mock for now)
   ↓
[ForecastReport] → Human Review
   ↓
[Implications] → PM Compiler → New TaskEnvelope
```

---

## 四、Agent 配置文件结构

在 `ai_os/agents/` 下创建:

```
ai_os/
├── agents/
│   ├── pm_compiler/
│   │   ├── AGENT.md          # PM Compiler 角色定义
│   │   ├── skills/           # 链接到 100x-product-managers
│   │   └── playbook.yaml     # 编译流程
│   ├── control_plane/
│   │   ├── CEO.md
│   │   ├── chief_of_staff.md
│   │   ├── cto.md
│   │   ├── qa_director.md
│   │   ├── research_lead.md
│   │   └── growth_lead.md
│   ├── workers/
│   │   ├── cloud_build.yaml
│   │   ├── cloud_qa.yaml
│   │   ├── cloud_research.yaml
│   │   └── local_fallback.yaml
│   ├── context/
│   │   ├── hub.yaml
│   │   └── compiler.yaml
│   ├── evidence/
│   │   └── ingestion_worker.yaml
│   ├── discord/
│   │   └── gateway.yaml
│   └── strategy_lab/
│       └── interface.yaml
├── contracts/
│   ├── TaskEnvelope.json
│   ├── ContextBundle.json
│   ├── ForecastRequest.json
│   ├── ForecastReport.json
│   └── DiscordMessage.json
├── workflows/
│   ├── pm_to_task.yaml
│   ├── control_approval.yaml
│   ├── worker_execution.yaml
│   └── strategy_lab.yaml
└── README.md
```

---

## 五、复用现有 100x PM Skills 映射

| 100x PM Skill | 新架构用途 | 复用方式 |
|---------------|-----------|---------|
| `market-driven-prioritization` | PM Compiler 优先级阶段 | 链接引用 |
| `10x-hypothesis-framework` | PM Compiler 假设阶段 | 链接引用 |
| `epic-breakdown-advisor` | PM Compiler Epic 分解 | 链接引用 |
| `opportunity-solution-tree` | PM Compiler 任务树构建 | 链接引用 |
| `prd-development` | PM Compiler PRD 输出 | 链接引用 |
| `roadmap-planning` | PM Compiler Roadmap 生成 | 链接引用 |
| `company-research` | Research Lead / Evidence Worker | 链接引用 |
| `context-engineering-advisor` | Context Hub 能力 | 链接引用 |

**注意**: 不移动原始文件，只在 `ai_os/agents/pm_compiler/skills/` 创建符号链接或引用文件。

---

## 七、AI Revenue Flywheel (业务飞轮)

基于你提供的完整 AI 公司操作系统架构，这是业务飞轮的 Agent 实现方案。

### 飞轮全图 (10 环节)

```
Signal (趋势信号)
    ↓
Offer (产品供给)
    ↓
Asset (交付资产)
    ↓
Content (内容拆分)
    ↓
Distribution (渠道投放)
    ↓
Funnel (引流转化)
    ↓
Sales (成交)
    ↓
Retention (复购/升级)
    ↓
Analytics (归因+实验)
    ↓
Memory (经验沉淀)
    ↓
Signal (更强的趋势信号)
```

### Agent 分工 (按飞轮阶段)

#### Strategy Layer
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Strategy Agent` | Claude | 战略方向制定 |

#### Signal Layer (趋势信号)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Trend Scout Agent` | Claude + Web | 平台热门、关键词趋势 |
| `Competitor Scan Agent` | Claude + Web | 竞品分析、畅销榜 |

#### Offer Layer (产品供给)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Offer Architect Agent` | Claude | 产品设计、Offer Card |
| `Pricing Agent` | Claude | 定价策略 |

#### Asset Layer (交付资产)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Ebook Factory Agent` | Claude | 电子书生成 |
| `Template Factory Agent` | Codex | 模板生成 |
| `Format & Packaging Agent` | Codex | 格式转换、包装 |

#### Content Layer (内容拆分)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Hook Agent` | Claude | Hook 变体生成 |
| `Script Agent` | Claude | 脚本撰写 |
| `Post Agent` | Claude | 帖子撰写 |

#### Distribution Layer (渠道投放)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Scheduler Agent` | Codex | 定时发布 |
| `TikTok Agent` | OpenClaw | TikTok 发布 |
| `XHS Agent` | OpenClaw | 小红书发布 |
| `LinkedIn Agent` | OpenClaw | LinkedIn 发布 |

#### Funnel Layer (引流转化)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Landing Page Agent` | Claude | Landing Page 生成 |
| `Website Builder Agent` | Codex | 网站建设 |
| `Lead Magnet Agent` | Claude | Lead Magnet 生成 |

#### Sales Layer (成交)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Sales Copy Agent` | Claude | 销售文案 |
| `Checkout Ops Agent` | Codex | 结账流程 |

#### Retention Layer (复购)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Email Sequence Agent` | Claude | 邮件序列 |
| `Community Agent` | Claude | 社区运营 |

#### Analytics Layer (归因+实验)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Attribution Agent` | Codex | 归因追踪 |
| `Experiment Agent` | Claude | 实验设计 |
| `Metrics Agent` | Codex | 指标仪表盘 |

#### Infrastructure Layer (基础设施)
| Agent | Runtime | 职责 |
|-------|---------|------|
| `Memory Agent` | Claude | 组织记忆存储 |
| `Runtime Agent` | Codex | 运行时管理 |
| `Security Agent` | Claude | 安全审计 |

### 产品线分类

| 产品线 | 定价 | 示例 | Agent |
|--------|------|------|-------|
| **Cash Products** | $9-39 | 面试模板、Checklist | Template Factory |
| **Flagship Products** | $49-199 | PM Interview Playbook | Ebook Factory |
| **Micro Assets** | $300-2k | 流量站、小工具站 | Website Builder |

### 飞轮执行示例

```
Day 1: Trend Scout 发现 "PM interview" 趋势
    ↓
Day 1-2: Offer Architect 生成 Offer Card
    ↓
Day 2-3: Ebook Factory 产出 PM Interview Playbook
    ↓
Day 3-4: Hook/Script/Post 生成 30 TikToks, 50 posts
    ↓
Day 4-5: Distribution Agents 发布到各平台
    ↓
Day 5-7: Landing Page + Email Capture 收集潜在客户
    ↓
Day 7+: Sales 转化 → Revenue Tracking 记录
    ↓
Week 2: Experiment Agent 测试 Hook A vs B
    ↓
Week 2: Memory Agent 更新 lessons learned
    ↓
Next: 更强的 Signal 进入下一轮
```

---

## 八、Phase 实施计划

### Phase 0: 安全与现状固化
- [ ] 轮换已暴露密钥 (GitHub token, Discord bot token)
- [ ] 确认 `ops/legacy/` 适配器规范
- [ ] 固化现有执行流程为 "legacy adapter"

### Phase 1: Agent Team 基础搭建
- [ ] 创建 `ai_os/` 目录结构
- [ ] 定义 PM Compiler Agent
- [ ] 链接 100x-product-managers skills
- [ ] 定义 Control Plane roles (CEO, CTO, etc.)

### Phase 2: Control Plane 集成
- [ ] Paperclip 控制面部署 (参考 `scripts/sync_paperclip_agents.py`)
- [ ] TaskEnvelope 合同实现
- [ ] 与 ops/tasks/ 队列集成

### Phase 3: Worker Swarm 接入
- [ ] Cloud Build Worker 配置
- [ ] Cloud QA Worker 配置
- [ ] Local Fallback 配置
- [ ] 执行报告格式统一

### Phase 4: Context & Evidence Layer
- [ ] Context Bundle 编译器
- [ ] Evidence Ingestion Worker (对接 Scrapling)
- [ ] Context Hub 外部 API 获取

### Phase 5: Discord 审批中心
- [ ] Discord Gateway 实现
- [ ] 4 类消息模型
- [ ] 审批闭环流程

### Phase 6: Strategy Lab 接口预留
- [ ] ForecastRequest / ForecastReport 合同
- [ ] Strategy Lab 入口
- [ ] Mock 引擎

### Phase 7: Revenue Flywheel 实现
- [ ] Trend Scout + Competitor Scan
- [ ] Offer Architect + Pricing
- [ ] Ebook/Template Factory
- [ ] Content (Hook/Script/Post)
- [ ] Distribution (TikTok/XHS/LinkedIn)
- [ ] Funnel (Landing Page)
- [ ] Sales + Revenue Tracking
- [ ] Experiment + Memory

---

## 九、下一步行动

1. **确认现有 ops/ 目录结构** - 检查目录是否都已创建
2. **创建 ai_os/ 目录** - 开始搭建 Agent 配置结构
3. **定义第一个 PM Compiler** - 从 `market-driven-prioritization` 开始
4. **配置 Paperclip 同步** - 复用 `scripts/sync_paperclip_agents.py`
5. **启动飞轮** - 从 Signal Layer 开始 (Trend Scout)

---

*此方案基于现有 `100x-product-managers`、`ops/` 和 `docs/AI_OS_ARCHITECTURE.md` 架构复用设计，整合了 AI Revenue Flywheel 业务模型。*
