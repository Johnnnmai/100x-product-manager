# Discord 事件模型

Discord 作为审批+告警中心的事件定义。

## 消息类型

### 1. approval_requested

```
🔔 审批请求

**任务**: {task_title}
**类型**: {approval_type}
**申请人**: {agent_name}
**预算**: ${amount}

[批准] [驳回] [查看详情]
```

**字段**:
- `task_id`: 任务 ID
- `task_title`: 任务标题
- `approval_type`: budget_exceed | external_api | production_deploy | content_publish
- `agent_name`: 申请 agent
- `budget`: 金额 (cents)
- `reason`: 申请理由

### 2. run_blocked

```
⚠️ 任务阻塞

**任务**: {task_title}
**阻塞原因**: {block_reason}
**阻塞者**: {blocker}

[查看详情] [人工接管]
```

**字段**:
- `task_id`: 任务 ID
- `task_title`: 任务标题
- `block_reason`: 阻塞原因
- `blocker`: 阻塞因素 (approval_waiting | external_dependency | resource_unavailable | error)
- `suggestion`: 解决建议

### 3. budget_threshold_hit

```
💰 预算阈值告警

**任务**: {task_title}
**已消耗**: ${spent} / ${cap}
**阈值**: {threshold}%

[查看详情]
```

**字段**:
- `task_id`: 任务 ID
- `task_title`: 任务标题
- `budget_cap`: 预算上限 (cents)
- `budget_spent`: 已消耗 (cents)
- `threshold`: 触发阈值 (%)

### 4. run_completed

```
✅ 任务完成

**任务**: {task_title}
**执行者**: {agent_name}
**耗时**: {duration}
**产出**: {artifact_path}

[查看产出] [关闭]
```

**字段**:
- `task_id`: 任务 ID
- `task_title`: 任务标题
- `agent_name`: 执行 agent
- `duration_minutes`: 执行时长
- `artifact_path`: 产出路径
- `verification_status`: passed | failed | partial

## Discord Bot 配置

```yaml
discord:
  bot_token: "${DISCORD_BOT_TOKEN}"
  channel_id: "${DISCORD_CHANNEL_ID}"

  # 事件路由
  events:
    approval_requested:
      channel: "approvals"
      mention_role: "@board"

    run_blocked:
      channel: "alerts"
      mention_role: "@on-call"

    budget_threshold_hit:
      channel: "finance"
      mention_role: "@cfo"

    run_completed:
      channel: "activity"
      mention: false
```

## 审批交互

### 批准流程

```
User: /approve {task_id}
Bot: ✅ 已批准任务 {task_id}
      状态已更新: in_progress -> approved
```

### 驳回流程

```
User: /reject {task_id} {reason}
Bot: ❌ 已驳回任务 {task_id}
      原因: {reason}
      状态已更新: in_progress -> rejected
```

### 人工接管

```
User: /takeover {task_id}
Bot: 🎯 任务 {task_id} 已转交人工处理
      请在 Paperclip 中查看详情
```
