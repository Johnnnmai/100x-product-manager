# ForecastRequest & ForecastReport Schema

Strategy Lab 接口定义，用于 OASIS / MiroFish 预测系统集成。

## ForecastRequest

```yaml
ForecastRequest:
  request_id: string       # 请求 ID

  # 输入
  seed_material_refs:
    - ref_id: string
      type: "market_report" | "competitor_analysis" | "financial_data" | "user_feedback"
      path: string

  decision_question: string    # 核心决策问题
  time_horizon:
    - unit: "week" | "month" | "quarter" | "year"
      value: number

  scenario_prompt: string      # 场景描述

  # 约束
  constraints:
    - constraint: string
      type: "resource" | "regulatory" | "market"

  # 元数据
  requested_by: string
  requested_at: string
  priority: "low" | "normal" | "high" | "critical"
```

## ForecastReport

```yaml
ForecastReport:
  report_id: string
  request_id: string

  # 场景摘要
  scenario_summary:
    - scenario: string
      probability: number    # 0-1
      impact: "low" | "medium" | "high"

  # 关键驱动因素
  key_drivers:
    - driver: string
      direction: "positive" | "negative" | "neutral"
      confidence: number     # 0-1
      evidence_refs: string[]

  # 风险信号
  risk_signals:
    - signal: string
      severity: "low" | "medium" | "high" | "critical"
      mitigation: string

  # 路线图影响
  roadmap_implications:
    - initiative: string
      adjustment: string
      priority_shift: "up" | "down" | "same"

  # 置信度
  overall_confidence: number   # 0-1
  methodology: string

  # 元数据
  generated_by: string
  generated_at: string
  version: string
```

## 示例

### ForecastRequest

```yaml
request:
  request_id: "req-001"

  seed_material_refs:
    - ref_id: "seed-001"
      type: "market_report"
      path: "reports/q4-market-analysis.md"

  decision_question: "是否应该在 2026 Q2 推出企业版？"
  time_horizon:
    - unit: "quarter"
      value: 4

  scenario_prompt: |
    考虑以下场景：
    1. 企业市场需求增长 30%
    2. 竞品推出类似功能
    3. 经济环境恶化

  requested_by: "CEO"
  requested_at: "2026-03-10T10:00:00Z"
  priority: "high"
```

### ForecastReport

```yaml
report:
  report_id: "rpt-001"
  request_id: "req-001"

  scenario_summary:
    - scenario: "企业市场需求增长"
      probability: 0.7
      impact: "high"
    - scenario: "竞品推出类似功能"
      probability: 0.6
      impact: "medium"

  key_drivers:
    - driver: "企业 SaaS 市场增长"
      direction: "positive"
      confidence: 0.8
      evidence_refs: ["gartner-2026-q1"]
    - driver: "获客成本上升"
      direction: "negative"
      confidence: 0.6
      evidence_refs: ["internal-cohort-analysis"]

  risk_signals:
    - signal: "竞品提前发布"
      severity: "high"
      mitigation: "加速 MVP 迭代"

  roadmap_implications:
    - initiative: "企业版发布"
      adjustment: "提前 Q2"
      priority_shift: "up"

  overall_confidence: 0.65
  methodology: "Monte Carlo simulation + expert judgment"

  generated_by: "OASIS-v1"
  generated_at: "2026-03-10T12:00:00Z"
  version: "1.0"
```
