# ContextBundle Schema

ContextBundle 定义了每个任务可消费的上下文边界，确保 agent 不能默认读取整个仓库。

## Schema

```yaml
ContextBundle:
  id: string              # 唯一标识
  task_id: string         # 关联的 TaskEnvelope

  # 核心上下文
  mission: string         # 任务使命 (一句话)
  constraints:
    - constraint: string
      type: "budget" | "time" | "scope" | "technical"

  # 证据引用
  evidence_refs:
    - ref_id: string
      type: "github_file" | "web_content" | "api_doc" | "research_report"
      path: string
      description: string
      snapshot_date: string

  # 术语表
  glossary:
    - term: string
      definition: string

  # 最新决策
  latest_decisions:
    - decision_id: string
      decision: string
      rationale: string
      made_by: string
      made_at: string

  # 边界
  allowed_paths:          # 允许读取的路径
    - "src/api/*"
    - "docs/api/*"

  blocked_paths:          # 禁止读取的路径
    - "**/credentials/**"
    - "**/.env*"

  max_tokens: number      # 最大上下文 token 数

  # 元数据
  created_by: string
  created_at: string
  version: string
```

## 示例

```yaml
context_bundle:
  id: "ctx-001"
  task_id: "task-001"

  mission: "实现用户认证 API"

  constraints:
    - constraint: "使用 JWT"
      type: "technical"
    - constraint: "2小时内完成"
      type: "time"

  evidence_refs:
    - ref_id: "ev-001"
      type: "api_doc"
      path: "docs/api/auth.md"
      description: "Auth API 文档"
      snapshot_date: "2026-03-10"

  glossary:
    - term: "JWT"
      definition: "JSON Web Token"

  latest_decisions:
    - decision_id: "dec-001"
      decision: "使用 Redis 存储 session"
      rationale: "性能更好"
      made_by: "CTO"
      made_at: "2026-03-09"

  allowed_paths:
    - "src/auth/**"
    - "tests/auth/**"

  blocked_paths:
    - "**/credentials/**"
    - "**/*.env"

  max_tokens: 32000

  created_by: "pm-compiler"
  created_at: "2026-03-10T10:00:00Z"
  version: "1.0"
```

## 规则

1. **禁止整仓读取**: 默认不允许 agent 读取整个仓库
2. **边界强制**: agent 只能访问 `allowed_paths` 中的文件
3. **证据驱动**: 所有外部输入通过 `evidence_refs` 引用
4. **版本化**: ContextBundle 有版本号，支持回溯
