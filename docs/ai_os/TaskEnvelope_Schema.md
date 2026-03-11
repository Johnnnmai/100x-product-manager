# TaskEnvelope Schema

TaskEnvelope 是 PM compiler 的标准输出格式，定义了从战略到可执行任务的完整链路。

## Schema

```yaml
TaskEnvelope:
  goal_id: string          # 关联的公司目标
  initiative_id: string    # 关联的 initiative
  epic_id: string          # 关联的 epic (可选)

  # 执行规格
  executor_type:
    - openclaw_build      # 云端构建
    - openclaw_verify     # 云端验证
    - openclaw_research  # 云端研究
    - codex_local         # 本地 Codex
    - claude_local        # 本地 Claude

  budget_cap: number       # 预算上限 (cents)
  time_estimate_hours: number

  # 交付规格
  acceptance_criteria:
    - criterion: string
      verification_method: string
      evidence_path: string

  context_bundle_ref: string   # 引用 ContextBundle
  artifact_output_path: string # 输出路径

  # 审批
  approval_required: boolean
  approval_type:
    - budget_exceed
    - external_api
    - production_deploy
    - content_publish

  # 状态
  status:
    - drafted      # 待编译
    - pending_approval  # 待审批
    - in_progress # 执行中
    - done        # 完成
    - blocked     # 阻塞
```

## 示例

```yaml
task_envelope:
  goal_id: "goal-001"
  initiative_id: "init-001"
  epic_id: "epic-001"

  executor_type: "openclaw_build"
  budget_cap: 50000
  time_estimate_hours: 8

  acceptance_criteria:
    - criterion: "API 返回正常"
      verification_method: "curl localhost:3000/health"
      evidence_path: "evidence/health-check.json"
    - criterion: "单元测试通过"
      verification_method: "npm test"
      evidence_path: "evidence/test-results.json"

  context_bundle_ref: "ctx-001"
  artifact_output_path: "projects/roomjoy/artifacts/api-v1"

  approval_required: false
  status: "pending_approval"
```
