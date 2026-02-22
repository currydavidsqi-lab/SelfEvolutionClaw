# OpenClaw 内置技能库

> 53 个内置技能完整清单

---

## 🧩 编程开发（5个）

### coding-agent
- **用途**：调用 Codex、Claude Code、Pi 等编程代理
- **场景**：构建新功能、重构代码、review PR、批量修复 issue
- **注意**：需要 `pty:true`，需要在 git 目录下运行

### github
- **用途**：GitHub 操作（PR、Issue、CI、API 查询）
- **场景**：检查 PR 状态、创建/关闭 issue、查看 CI 日志
- **工具**：`gh` CLI

### gh-issues
- **用途**：自动修复 GitHub Issues
- **场景**：自动生成 PR、处理 review comments
- **特点**：支持 fork 模式、watch 模式、cron 模式

### oracle
- **用途**：代码分析工具
- **场景**：捆绑 prompt + 文件，让其他模型分析
- **特点**：支持 GPT-5.2 Pro、长思考模式

### mcporter
- **用途**：MCP 服务器工具
- **场景**：调用各种 MCP 服务器和工具
- **特点**：支持 HTTP 和 stdio 模式

---

## 🌤️ 信息查询（4个）

### weather
- **用途**：获取天气和预报
- **场景**：当前天气、未来几天预报、旅行规划
- **数据源**：wttr.in（无需 API key）

### summarize
- **用途**：总结 URL、播客、视频、本地文件
- **场景**：快速了解文章/视频内容、提取 YouTube 转录
- **特点**：支持多种 LLM（OpenAI、Anthropic、Google）

### goplaces
- **用途**：Google Places API
- **场景**：地点搜索、详情、评价
- **工具**：`goplaces` CLI

### xurl
- **用途**：Twitter/X API CLI
- **场景**：发推、回复、搜索、关注等
- **特点**：完整的 X API 操作

---

## 📝 笔记任务（8个）

### obsidian
- **用途**：操作 Obsidian vault
- **场景**：搜索、创建、移动、删除笔记
- **特点**：自动更新 wikilinks

### notion
- **用途**：Notion API 操作
- **场景**：创建/查询数据库、管理页面
- **需要**：`NOTION_API_KEY`

### bear-notes
- **用途**：Bear notes CLI
- **场景**：创建、搜索、管理 Bear 笔记
- **工具**：`grizzly` CLI

### apple-notes
- **用途**：Apple Notes CLI
- **场景**：创建、查看、编辑、搜索笔记
- **工具**：`memo` CLI

### things-mac
- **用途**：Things 3 任务管理
- **场景**：添加、更新、搜索任务
- **特点**：macOS 独占

### apple-reminders
- **用途**：Apple 提醒事项
- **场景**：创建、完成、删除提醒
- **特点**：同步到 iPhone/iPad

### trello
- **用途**：Trello 看板
- **场景**：看板、列表、卡片管理
- **需要**：`TRELLO_API_KEY` 和 `TRELLO_TOKEN`

### blogwatcher
- **用途**：RSS/博客监控
- **场景**：监控博客更新、扫描新文章
- **工具**：`blogwatcher` CLI

---

## 🎵 多媒体（10个）

### spotify-player
- **用途**：Spotify 播放控制
- **场景**：搜索歌曲、播放/暂停、切换设备
- **需要**：Spotify Premium

### openai-image-gen
- **用途**：批量生成图片
- **场景**：根据提示生成图片、创建画廊
- **模型**：GPT image、DALL-E 2/3

### nano-banana-pro
- **用途**：Gemini 图片生成/编辑
- **场景**：生成图片、编辑图片、多图合成
- **需要**：`GEMINI_API_KEY`

### openai-whisper
- **用途**：本地语音转文字
- **场景**：转录音频文件
- **特点**：本地运行，无需 API key

### sag
- **用途**：ElevenLabs TTS
- **场景**：文字转语音
- **需要**：`ELEVENLABS_API_KEY`

### sherpa-onnx-tts
- **用途**：本地离线 TTS
- **场景**：离线文字转语音
- **特点**：完全本地，无需网络

### songsee
- **用途**：音频频谱可视化
- **场景**：生成频谱图、特征面板
- **特点**：支持多种可视化模式

### gifgrep
- **用途**：GIF 搜索
- **场景**：搜索 Tenor/Giphy、下载、提取帧
- **特点**：TUI 预览

### video-frames
- **用途**：视频帧提取
- **场景**：从视频中提取帧、缩略图
- **工具**：ffmpeg

### nano-pdf
- **用途**：PDF 自然语言编辑
- **场景**：用自然语言指令编辑 PDF
- **特点**：基于 AI

---

## 🖥️ 系统管理（6个）

### healthcheck
- **用途**：系统安全检查和加固
- **场景**：安全审计、防火墙配置、SSH 加固
- **特点**：支持多种风险配置

### tmux
- **用途**：远程控制 tmux 会话
- **场景**：监控后台进程、发送输入、抓取输出
- **注意**：只能操作已存在的会话

### 1password
- **用途**：密码管理 CLI
- **场景**：读取/注入密码、运行 secrets
- **特点**：需要 tmux 会话授权

### peekaboo
- **用途**：macOS UI 自动化
- **场景**：截屏、点击、输入、拖拽、菜单控制
- **特点**：完整的 macOS UI 自动化

### session-logs
- **用途**：会话日志搜索
- **场景**：查询历史对话、分析会话
- **工具**：jq 查询

### model-usage
- **用途**：CodexBar 成本分析
- **场景**：分析 API 使用成本
- **特点**：macOS 独占

---

## 📱 通讯（7个）

### discord
- **用途**：Discord 集成
- **场景**：消息、反应、投票、线程
- **需要**：Discord token

### slack
- **用途**：Slack 操作
- **场景**：消息、反应、固定、成员信息
- **需要**：Slack token

### bluebubbles
- **用途**：iMessage 集成
- **场景**：发送、反应、编辑、撤销
- **需要**：BlueBubbles 服务器

### imsg
- **用途**：iMessage/SMS CLI
- **场景**：查看聊天、发送消息
- **特点**：macOS 独占

### wacli
- **用途**：WhatsApp CLI
- **场景**：发送消息、搜索历史、同步
- **注意**：仅用于第三方通讯

### himalaya
- **用途**：邮件 CLI
- **场景**：读取、发送、搜索邮件
- **特点**：IMAP/SMTP

### voice-call
- **用途**：语音通话
- **场景**：发起、继续、结束通话
- **支持**：Twilio、Telnyx、Plivo

---

## 🏠 智能家居（5个）

### openhue
- **用途**：Philips Hue 灯光控制
- **场景**：开关灯、调节亮度、设置场景
- **需要**：Hue Bridge

### sonoscli
- **用途**：Sonos 音箱控制
- **场景**：播放、暂停、音量、分组
- **工具**：`sonos` CLI

### blucli
- **用途**：Bluesound/NAD 播放器
- **场景**：播放控制、TuneIn 搜索
- **工具**：`blu` CLI

### camsnap
- **用途**：RTSP/ONVIF 摄像头
- **场景**：抓拍、录制、运动检测
- **工具**：`camsnap` CLI

### eightctl
- **用途**：Eight Sleep 床垫控制
- **场景**：温度、闹钟、时间表
- **需要**：认证

---

## 🔧 元技能（3个）

### skill-creator
- **用途**：创建新的 skills
- **场景**：设计和打包自定义技能
- **组成**：SKILL.md + scripts/ + references/ + assets/

### clawhub
- **用途**：技能市场
- **场景**：搜索、安装、更新、发布技能
- **命令**：`clawhub search/install/update/publish`

### canvas
- **用途**：HTML 内容展示
- **场景**：游戏、可视化、仪表板
- **架构**：Canvas Host → Node Bridge → Node App

---

## 🛠️ 其他工具（5个）

### gemini
- **用途**：Gemini CLI
- **场景**：Q&A、总结、生成
- **特点**：避免交互模式

### gog
- **用途**：Google Workspace
- **场景**：Gmail、Calendar、Drive、Contacts
- **需要**：OAuth 设置

### food-order
- **用途**：Foodora 订餐
- **场景**：重新订购、跟踪订单
- **工具**：`ordercli`

### ordercli
- **用途**：外卖订单管理
- **场景**：检查订单、跟踪状态
- **支持**：Foodora、Deliveroo

### openai-whisper-api
- **用途**：Whisper API 版本
- **场景**：云端语音转文字
- **需要**：`OPENAI_API_KEY`

---

## 📊 统计

| 类别 | 数量 |
|------|------|
| 编程开发 | 5 |
| 信息查询 | 4 |
| 笔记任务 | 8 |
| 多媒体 | 10 |
| 系统管理 | 6 |
| 通讯 | 7 |
| 智能家居 | 5 |
| 元技能 | 3 |
| 其他 | 5 |
| **总计** | **53** |

---

*最后更新：2026-02-22*
