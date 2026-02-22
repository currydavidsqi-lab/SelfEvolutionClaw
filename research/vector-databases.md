# 向量数据库研究

> AI 记忆系统的核心组件

---

## 🔍 研究发现

### 1. Vault AI ⭐ 3,403
**用途**：ChatGPT 长期记忆
**技术栈**：
- OpenAI API
- Pinecone 向量数据库
- 支持自定义知识库（PDF、txt、epub）

**特点**：
- 简单的 React 前端
- 上传自定义文件
- 长期记忆存储

---

### 2. 向量搜索课程笔记 ⭐ 327
**课程**：COS 597A @ Princeton
**主题**：AI 中的长期记忆 - 向量搜索和数据库

**内容**：
- 向量搜索原理
- 数据库设计
- 实际应用

---

### 3. Kektordb ⭐ 56
**用途**：内存向量数据库 & AI 网关
**语言**：Go

**特点**：
- HNSW 算法
- 混合搜索（BM25）
- GraphRAG 上下文
- 内置 RAG Pipeline
- 可嵌入应用

---

## 📊 向量数据库对比

| 数据库 | 语言 | 特点 | 适用场景 |
|--------|------|------|----------|
| **Pinecone** | SaaS | 托管服务，易用 | 生产环境 |
| **Qdrant** | Rust | 高性能，开源 | 大规模部署 |
| **Milvus** | Go | 分布式，可扩展 | 企业级应用 |
| **Weaviate** | Go | 语义搜索 | 知识图谱 |
| **Chroma** | Python | 轻量级，易用 | 快速原型 |
| **Kektordb** | Go | 内存，可嵌入 | 实时应用 |

---

## 💡 关键技术

### HNSW (Hierarchical Navigable Small World)
**用途**：高效近似最近邻搜索

**优点**：
- 查询速度快
- 内存效率高
- 可扩展性好

**适用**：
- 大规模向量搜索
- 实时应用

---

### 混合搜索
**组合**：
- 向量搜索（语义）
- BM25（关键词）
- 加权融合

**优势**：
- 提高准确率
- 覆盖不同查询类型

---

### GraphRAG
**概念**：图 + RAG

**特点**：
- 知识图谱增强
- 上下文理解更深
- 关系推理

---

## 🚀 与 OpenClaw 集成

### 方案 1：使用 MemOS
**MemOS 内置**：
- 向量数据库
- 统一 API
- OpenClaw 插件

**优点**：
- 开箱即用
- 不需要额外配置
- 官方支持

---

### 方案 2：独立部署
**选择**：
- Qdrant（性能优先）
- Chroma（快速原型）

**集成方式**：
- OpenClaw Skill
- Python 客户端
- REST API

---

## 📚 学习资源

### 官方文档
- Pinecone: https://docs.pinecone.io/
- Qdrant: https://qdrant.tech/documentation/
- Milvus: https://milvus.io/docs/

### 教程
- Vector Search Best Practices
- Building RAG with Vector DB
- Scaling Vector Search

---

*研究时间：2026-02-22 22:15*
