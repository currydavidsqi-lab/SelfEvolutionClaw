# GitHub 项目发现的技能

> 探索 AI 代理生态发现的项目和技能

---

## 🔥 热门 AI 代理项目

### 1. DeerFlow (字节跳动) ⭐ 20,062
**官网**: https://deerflow.tech
**GitHub**: https://github.com/bytedance/deer-flow

**核心特点**：
- SuperAgent 编排框架
- 支持沙盒、记忆、工具、技能、子代理
- 处理几分钟到几小时的任务
- 完全重写的 2.0 版本

**关键功能**：
- **Skills & Tools**：扩展代理能力
- **Sub-Agents**：子代理系统
- **Sandbox & File System**：沙盒文件系统
- **Context Engineering**：上下文工程
- **Long-Term Memory**：长期记忆

**配置示例**：
```yaml
models:
  - name: gpt-4
    display_name: GPT-4
    use: langchain_openai:ChatOpenAI
    model: gpt-4
    api_key: $OPENAI_API_KEY
    max_tokens: 4096
    temperature: 0.7
```

---

### 2. MemOS ⭐ 5,730
**GitHub**: https://github.com/MemTensor/MemOS
**官网**: https://memos.openmem.net/

**核心特点**：
- **AI 记忆操作系统**
- **特别支持 OpenClaw**（moltbot、clawdbot、openclaw）
- 跨任务技能重用和进化
- 企业级优化

**关键功能**：
- 统一存储/检索/管理长期记忆
- 知识库（KB）集成
- 多模态记忆
- 工具记忆
- 上下文感知交互

**学术支持**：
- arXiv:2507.03724 - MemOS: A Memory OS for AI System
- arXiv:2505.22101 - MemOS: An Operating System for MAG

---

### 3. Antigravity Awesome Skills ⭐ 13,960
**GitHub**: https://github.com/sickn33/antigravity-awesome-skills

**核心特点**：
- **889+ 个通用 AI 代理技能**
- 支持所有主流 AI 编程助手
- 包含 Anthropic、OpenAI、Google、Microsoft 官方技能

**支持平台**：
- 🟣 Claude Code (Anthropic CLI)
- 🔵 Gemini CLI (Google DeepMind)
- 🟢 Codex CLI (OpenAI)
- 🟠 Kiro CLI (AWS)
- 🔴 Antigravity IDE (Google DeepMind)
- 🩵 GitHub Copilot (VSCode Extension)
- 🟠 Cursor (AI-native IDE)
- ⚪ OpenCode (Open-source CLI)
- 🌸 AdaL CLI (Self-evolving Coding Agent)

**技能类别**：
- 官方技能（Anthropic、OpenAI、Google）
- 社区贡献技能
- 打包技能集合
- 工作流模板

---

### 4. Letta ⭐ 21,203
**GitHub**: https://github.com/letta-ai/letta

**核心特点**：
- **有状态的代理平台**
- AI with advanced memory
- Can learn and self-improve over time

**适用场景**：
- 需要长期记忆的代理
- 自我改进的 AI 系统
- 个性化 AI 助手

---

### 5. Mem0 ⭐ 47,766
**GitHub**: https://github.com/mem0ai/mem0

**核心特点**：
- **Universal memory layer for AI Agents**
- 最火的记忆层项目
- 跨平台记忆管理

**适用场景**：
- 为任何 AI 代理添加记忆
- 跨会话持久化
- 上下文管理

---

## 🔧 MCP Server 生态系统

### 1. Awesome MCP Servers ⭐ 81,324
**GitHub**: https://github.com/punkpeye/awesome-mcp-servers

**核心特点**：
- 最火的 MCP 资源集合
- 包含各种 MCP 服务器

---

### 2. Context7 ⭐ 46,473
**GitHub**: https://github.com/upstash/context7

**核心特点**：
- Upstash 文档 MCP
- Up-to-date code documentation for LLMs
- AI code editors

---

### 3. MindsDB ⭐ 38,552
**GitHub**: https://github.com/mindsdb/mindsdb

**核心特点**：
- Federated Query Engine
- The only MCP Server you'll ever need
- AI-integrated database

---

### 4. Playwright MCP ⭐ 27,492
**GitHub**: https://github.com/microsoft/playwright-mcp

**核心特点**：
- Microsoft Playwright MCP
- Browser automation for MCP

---

### 5. GitHub MCP Server ⭐ 27,138
**GitHub**: https://github.com/github/github-mcp-server

**核心特点**：
- GitHub 官方 MCP Server
- GitHub API 集成

---

## 📚 其他重要项目

### Haystack ⭐ 24,256
**GitHub**: https://github.com/deepset-ai/haystack

**核心特点**：
- AI orchestration framework
- Context-engineered, production-ready
- Modular pipelines and agent workflows

---

### 12-Factor Agents ⭐ 18,301
**GitHub**: https://github.com/humanlayer/12-factor-agents

**核心特点**：
- Agent 构建原则
- Principles for LLM-powered software
- Production-ready agents

---

### Composio ⭐ 27,110
**GitHub**: https://github.com/ComposioHQ/composio

**核心特点**：
- 1000+ 工具包支持
- 工具搜索、上下文管理、认证
- 沙盒工作台

---

### Vercel AI ⭐ 21,938
**GitHub**: https://github.com/vercel/ai

**核心特点**：
- TypeScript AI 工具包
- Next.js 团队出品
- 构建 AI 应用和代理

---

### Google ADK Python ⭐ 17,905
**GitHub**: https://github.com/google/adk-python

**核心特点**：
- Google 官方 Python AI 代理工具包
- 代码优先
- 构建、评估、部署复杂 AI 代理

---

## 💡 技能生态趋势

### 标准化
- 通用技能格式正在形成
- 跨平台兼容成主流
- 社区驱动增长迅速

### 记忆系统
- 长期记忆成为标配
- 跨任务重用需求增加
- 企业级优化成熟

### MCP 生态
- MCP Server 爆发增长
- 官方支持增加（GitHub、Microsoft）
- 工具集成平台化

---

## 📊 项目统计

| 项目类型 | 数量 | 总 Star 数 |
|---------|------|-----------|
| AI 代理框架 | 5 | 100K+ |
| 记忆系统 | 3 | 70K+ |
| MCP Servers | 5 | 220K+ |
| 工具集成 | 3 | 65K+ |
| **总计** | **16** | **455K+** |

---

*最后更新：2026-02-22*
