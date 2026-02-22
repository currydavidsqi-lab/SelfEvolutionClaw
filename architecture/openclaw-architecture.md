# OpenClaw 核心架构

> OpenClaw 的技术架构和核心概念

---

## 🏗️ 基础架构

### Agent Runtime
- **来源**：pi-mono 衍生
- **特点**：单一嵌入式代理运行时
- **位置**：Gateway 内嵌

### Agent Workspace
- **默认位置**：`~/.openclaw/workspace`
- **作用**：代理的唯一工作目录（cwd）
- **特点**：与 `~/.openclaw/` 分离（后者存储配置、凭证、会话）

---

## 📁 Workspace 文件结构

### Bootstrap 文件（启动时注入）

| 文件 | 用途 | 说明 |
|------|------|------|
| `AGENTS.md` | 操作指令 + "记忆" | 代理行为准则 |
| `SOUL.md` | 人格、边界、语气 | 定义代理个性 |
| `TOOLS.md` | 工具笔记 | 本地工具配置 |
| `BOOTSTRAP.md` | 一次性首次运行仪式 | 完成后删除 |
| `IDENTITY.md` | 代理名称/vibe/emoji | 身份标识 |
| `USER.md` | 用户资料 | 用户信息 |

### Memory 文件

| 文件 | 用途 | 特点 |
|------|------|------|
| `MEMORY.md` | 长期记忆 | 仅主会话加载 |
| `memory/YYYY-MM-DD.md` | 日常日志 | 只追加 |

---

## 🎯 Skills 系统

### 加载顺序（优先级从高到低）
1. **Workspace**（`<workspace>/skills`）
2. **Managed**（`~/.openclaw/skills`）
3. **Bundled**（系统自带）

### Skill 组成
```
skill-name/
├── SKILL.md        # 技能描述和使用指南
├── scripts/        # 脚本文件
├── references/     # 参考文档
└── assets/         # 资源文件
```

---

## ⚙️ 配置系统

### 配置文件
- **位置**：`~/.openclaw/openclaw.json`
- **格式**：JSON5（支持注释和尾随逗号）
- **特点**：热重载，自动应用变更

### 配置方式
1. **交互式向导**：`openclaw onboard` / `openclaw configure`
2. **CLI 命令**：`openclaw config get/set/unset`
3. **Control UI**：http://127.0.0.1:18789
4. **直接编辑**：编辑配置文件

---

## 🤖 自动化系统

### Cron Jobs
- **特点**：精确时间触发
- **环境**：独立会话
- **上下文**：无
- **适用**：一次性任务、精确调度

**配置示例**：
```json5
{
  "crons": [
    {
      "id": "daily-sync-morning",
      "schedule": "0 9 * * *",
      "timezone": "Asia/Shanghai",
      "message": "早上 9 点同步",
      "target": "telegram:8207814268"
    }
  ]
}
```

### Heartbeat
- **特点**：固定间隔（默认 30 分钟）
- **环境**：主会话
- **上下文**：有
- **适用**：批量检查、周期性任务

**配置示例**：
```json5
{
  "agents": {
    "defaults": {
      "heartbeat": {
        "every": "30m",
        "prompt": "检查邮箱、日历、天气"
      }
    }
  }
}
```

---

## 🪝 Hooks（钩子系统）

### 概述
事件驱动的自动化系统，在代理命令和事件发生时自动运行脚本。

### 内置 Hooks
1. **💾 session-memory**：`/new` 时保存会话上下文到记忆
2. **📎 bootstrap-extra-files**：注入额外的 bootstrap 文件
3. **📝 command-logger**：记录所有命令到日志
4. **🚀 boot-md**：启动时运行 `BOOT.md`

### 常见用途
- 会话重置时保存记忆快照
- 审计命令日志
- 触发后续自动化
- 扩展 OpenClaw 行为

---

## 📨 Command Queue（命令队列）

### 为什么需要队列
- 自动回复运行可能很昂贵（LLM 调用）
- 防止多个入站消息碰撞
- 避免共享资源竞争
- 减少上游速率限制风险

### 工作原理
- 按 **session key** 排队（每个会话只有一个活跃运行）
- 全局 lane 限制总体并行度
  - **main lane**：默认 4 并发
  - **subagent lane**：默认 8 并发
- 打字指示器立即触发

### Queue 模式

| 模式 | 行为 | 说明 |
|------|------|------|
| `steer` | 立即注入当前运行 | 工具调用边界取消 |
| `followup` | 当前结束后排队 | 下一轮处理 |
| `collect` | 合并所有排队消息 | **默认** |
| `steer-backlog` | steer + 保留用于 followup | 两次响应 |
| `interrupt` | 中止当前，运行最新 | Legacy |

---

## 🐳 Sandboxing（沙盒隔离）

### 概述
在 Docker 容器中运行工具，减少风险半径。

### 模式

| 模式 | 行为 | 说明 |
|------|------|------|
| `off` | 无沙盒 | 所有工具在主机运行 |
| `non-main` | 只沙盒非主会话 | 推荐配置 |
| `on` | 所有会话都沙盒 | 最高安全 |

### 沙盒化的内容
- ✅ 工具执行（exec、read、write、edit 等）
- ✅ 浏览器（可选）
- ✅ Docker 网络隔离

### 不沙盒化的内容
- ❌ Gateway 进程本身
- ❌ 明确允许在主机上运行的工具（e.g. `tools.elevated`）

### 浏览器沙盒特性
- **autoStart**：自动启动浏览器容器
- **专用 Docker 网络**：`openclaw-sandbox-browser`
- **CDP 访问控制**：CIDR allowlist
- **noVNC 观察者访问**：密码保护

---

## 🔄 Session Management

### Session 文件
- **位置**：`~/.openclaw/agents/<agentId>/sessions/`
- **格式**：JSONL（每行一个 JSON 对象）
- **索引**：`sessions.json`

### Session Key
- **格式**：`telegram:8207814268`（示例）
- **作用**：唯一标识一个会话
- **用途**：队列管理、消息路由

---

## 🌐 Channels（渠道）

### 支持的渠道
- Telegram
- Discord
- Signal
- WhatsApp
- Slack
- iMessage (BlueBubbles)
- IRC
- Matrix
- Google Chat
- Microsoft Teams
- LINE
- Zalo

### 渠道配置
```json5
{
  "channels": {
    "telegram": {
      "token": "YOUR_BOT_TOKEN",
      "allowFrom": ["+15555550123"]
    }
  }
}
```

---

## 📊 性能优化

### 并发控制
- **main lane**：4 并发
- **subagent lane**：8 并发
- **per-session**：1 活跃运行

### 上下文管理
- **自动压缩**：接近 token 限制时触发
- **记忆刷新**：压缩前保存记忆
- **文件注入**：大文件自动截断

---

## 🔒 安全机制

### 工具策略
- **黑名单**：禁止特定工具
- **白名单**：只允许特定工具
- **提升权限**：`tools.elevated` 绕过沙盒

### 沙盒隔离
- Docker 容器隔离
- 网络隔离
- 文件系统隔离

### 密钥管理
- 环境变量
- 配置文件（加密）
- 1Password 集成

---

*最后更新：2026-02-22*
