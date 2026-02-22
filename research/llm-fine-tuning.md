# LLM 微调（Fine-tuning）

> 大语言模型微调技术和工具

---

## 🔥 热门项目（按 Star 排序）

### 1. LlamaFactory ⭐ 67,433
**定位**：Unified Efficient Fine-Tuning of 100+ LLMs & VLMs

**核心特点**：
- **最火的微调框架**（67K stars）
- ACL 2024 论文
- 支持 100+ LLMs 和 VLMs
- 统一高效的微调

**支持模型**：
- Llama、Qwen、ChatGLM
- Baichuan、Yi、Mistral
- 多模态模型

**适用场景**：
- 模型微调
- 领域适配
- 任务定制

---

### 2. Llama Cookbook ⭐ 18,209
**开发商**：Meta
**定位**：Your go to guide for Building with Llama

**核心特点**：
- Meta 官方
- 完整的 Llama 指南
- 包含推理、微调、RAG

**内容**：
- 快速开始
- 模型推理
- 微调教程
- RAG 构建
- 端到端解决方案

---

### 3. Weights & Biases ⭐ 10,848
**定位**：The AI developer platform

**核心特点**：
- AI 开发平台
- 模型训练和微调
- 从实验到生产的完整管理

**功能**：
- 实验追踪
- 超参数调优
- 模型管理
- 可视化分析

---

### 4. H2O LLM Studio ⭐ 4,886
**定位**：No-code GUI for fine-tuning LLMs

**核心特点**：
- 无代码 GUI
- 微调框架
- 易于使用

**优点**：
- 可视化操作
- 无需编程
- 快速微调

---

### 5. Kiln ⭐ 4,664
**定位**：Build, Evaluate, and Optimize AI Systems

**核心特点**：
- AI 系统构建
- 评估和优化
- 包含微调、RAG、代理

**功能**：
- 微调
- 评估
- 合成数据生成
- 数据集管理
- MCP 支持

---

## 💡 核心概念

### 1. 微调方法

**全量微调**：
- 调整所有参数
- 效果最好
- 资源需求大

**参数高效微调（PEFT）**：
- LoRA（Low-Rank Adaptation）
- QLoRA（量化 LoRA）
- Adapter
- Prefix Tuning

---

### 2. 微调流程

```
数据准备 → 模型选择 → 微调训练 → 评估验证 → 部署应用
```

**关键步骤**：
1. **数据准备**：清洗、格式化、增强
2. **模型选择**：基础模型、规模
3. **微调方法**：LoRA、QLoRA 等
4. **训练监控**：损失、指标
5. **评估验证**：性能、质量
6. **部署应用**：推理、服务

---

## 📊 框架对比

| 框架 | Stars | 特点 | 适用场景 |
|------|-------|------|----------|
| **LlamaFactory** | 67K | 统一框架，100+ 模型 | 通用微调 |
| **Llama Cookbook** | 18K | Meta 官方指南 | Llama 开发 |
| **WandB** | 11K | 实验管理 | 训练监控 |
| **H2O LLM Studio** | 5K | 无代码 GUI | 快速微调 |
| **Kiln** | 5K | 全流程平台 | 系统构建 |

---

## 🚀 与 OpenClaw 的关系

### 集成可能性

**LlamaFactory + OpenClaw**：
- 为 OpenClaw 定制模型
- 领域适配
- 提升特定任务性能

**WandB + OpenClaw**：
- 监控代理性能
- 实验追踪
- 优化调参

---

## 📚 学习资源

### 官方文档
- LlamaFactory: https://github.com/hiyouga/LlamaFactory
- Llama Cookbook: https://github.com/meta-llama/llama-cookbook
- WandB: https://wandb.ai/

### 论文
- "LoRA: Low-Rank Adaptation of Large Language Models"
- "QLoRA: Efficient Finetuning of Quantized LLMs"

---

## 🔮 趋势分析

### 当前状态
- LlamaFactory 一骑绝尘（67K stars）
- 微调成为定制 LLM 的标配
- PEFT 方法普及

### 未来方向
1. **更高效**
   - 新的 PEFT 方法
   - 自动化微调
   - 少样本学习

2. **更易用**
   - 无代码平台
   - 自动化流程
   - 可视化界面

3. **更专业**
   - 领域微调
   - 多模态微调
   - 持续学习

---

*研究时间：2026-02-23 03:40*
