---
name: ppt-generator
description: 根据主题自动生成 PowerPoint 演示文稿
metadata:
  {
    "openclaw": {
      "emoji": "📊",
      "requires": { "bins": ["python3"], "env": [] },
      "install": [
        {
          "id": "pip",
          "kind": "pip",
          "package": "python-pptx",
          "label": "Install python-pptx"
        }
      ]
    }
  }
---

# PPT 生成器

根据主题自动生成专业的 PowerPoint 演示文稿。

## 快速开始

```bash
# 基础使用
python {baseDir}/scripts/generate_ppt.py --topic "AI 代理技术" --slides 10

# 自定义输出
python {baseDir}/scripts/generate_ppt.py --topic "机器学习" --slides 8 --output /tmp/demo.pptx
```

## 参数说明

| 参数 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| `--topic` | ✅ | - | PPT 主题 |
| `--slides` | ❌ | 10 | 幻灯片数量 |
| `--output` | ❌ | output.pptx | 输出文件路径 |

## 功能特点

- ✅ 自动生成结构化大纲
- ✅ 标题页、目录、内容页、总结页
- ✅ 支持自定义幻灯片数量
- ✅ 标准的 .pptx 格式
- ✅ 可在 PowerPoint、Keynote、Google Slides 打开

## 使用示例

### 示例 1：基础使用
```bash
python scripts/generate_ppt.py --topic "Python 编程入门"
```

生成 10 张幻灯片，保存到 `output.pptx`

### 示例 2：自定义数量
```bash
python scripts/generate_ppt.py --topic "深度学习基础" --slides 15
```

生成 15 张幻灯片

### 示例 3：自定义输出路径
```bash
python scripts/generate_ppt.py --topic "产品设计" --output ~/Documents/demo.pptx
```

保存到指定路径

## 安装依赖

```bash
# 创建虚拟环境
cd /home/curry/openclaw/projects/custom-skills/ppt-generator
python3 -m venv .venv

# 安装依赖
.venv/bin/pip install python-pptx

# 运行（使用虚拟环境）
.venv/bin/python scripts/generate_ppt.py --topic "主题" --slides 10
```

## 注意事项

- 需要 Python 3.6+
- 需要安装 python-pptx 库
- 输出文件格式为 .pptx
- 可在 Microsoft PowerPoint、Apple Keynote、Google Slides 中打开

## 后续改进

- [ ] 支持模板选择
- [ ] 集成 AI 生成内容
- [ ] 支持自定义样式
- [ ] 支持插入图片

---

*版本：0.1*
*创建时间：2026-02-22*
