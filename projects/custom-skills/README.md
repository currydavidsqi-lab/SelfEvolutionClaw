# 自定义技能开发

> 创建和发布自己的 OpenClaw 技能

---

## 🎯 项目目标

**核心目标**：
- 学习技能开发流程
- 创建实用的自定义技能
- 发布到 ClawHub 社区

**预期成果**：
- 3-5 个自定义技能
- 开发文档
- ClawHub 发布

---

## 📋 技能开发流程

### 1. 需求分析
- 确定技能用途
- 定义功能范围
- 设计用户交互

### 2. 技能设计
- 编写 SKILL.md
- 设计脚本/工具
- 准备参考文档

### 3. 开发实现
- 编写脚本
- 测试功能
- 优化性能

### 4. 打包发布
- 遵循 OpenClaw 规范
- 测试兼容性
- 发布到 ClawHub

---

## 💡 技能创意清单

### 1. PPT 生成器 📊
**功能**：根据主题自动生成 PPT

**技术栈**：
- python-pptx
- Markdown → PPT
- AI 生成内容

**文件结构**：
```
ppt-generator/
├── SKILL.md
├── scripts/
│   ├── generate_ppt.py
│   └── templates/
└── references/
    └── ppt-templates.md
```

---

### 2. API 测试工具 🧪
**功能**：自动化 API 测试和验证

**技术栈**：
- requests
- pytest
- JSON Schema

**文件结构**：
```
api-tester/
├── SKILL.md
├── scripts/
│   ├── test_api.py
│   └── validators.py
└── references/
    └── api-testing.md
```

---

### 3. 学习笔记整理器 📝
**功能**：自动整理和总结学习笔记

**技术栈**：
- Markdown 处理
- AI 总结
- 自动分类

**文件结构**：
```
note-organizer/
├── SKILL.md
├── scripts/
│   ├── organize.py
│   └── summarize.py
└── references/
    └── note-formats.md
```

---

### 4. 代码审查助手 🔍
**功能**：自动代码审查和建议

**技术栈**：
- AST 分析
- AI 审查
- 最佳实践检查

**文件结构**：
```
code-reviewer/
├── SKILL.md
├── scripts/
│   ├── review.py
│   └── checks/
└── references/
    └── code-standards.md
```

---

### 5. Git 提交助手 📦
**功能**：自动生成 Git 提交信息

**技术栈**：
- Git 命令
- AI 生成
- Conventional Commits

**文件结构**：
```
git-committer/
├── SKILL.md
├── scripts/
│   └── generate_commit.py
└── references/
    └── commit-conventions.md
```

---

## 🚀 第一个技能：PPT 生成器

### 需求分析

**用户场景**：
```
用户：帮我做一个关于 AI 代理的 PPT
技能：[生成大纲] → [创建幻灯片] → [添加内容] → [输出 .pptx]
```

**功能**：
- 根据主题生成大纲
- 自动创建幻灯片
- 生成标题、内容、要点
- 支持模板选择
- 输出 .pptx 文件

---

### 技能设计

**SKILL.md**：
```markdown
---
name: ppt-generator
description: 根据主题自动生成 PowerPoint 演示文稿
metadata:
  {
    "openclaw": {
      "emoji": "📊",
      "requires": { "bins": ["python3"], "env": [] }
    }
  }
---

# PPT 生成器

根据主题自动生成专业的 PowerPoint 演示文稿。

## 快速开始

\`\`\`bash
python {baseDir}/scripts/generate_ppt.py --topic "AI 代理技术" --slides 10
\`\`\`

## 参数说明

- `--topic`：PPT 主题
- `--slides`：幻灯片数量（默认 10）
- `--template`：模板名称（可选）
- `--output`：输出路径（默认 ./output.pptx）

## 示例

\`\`\`bash
# 基础使用
python scripts/generate_ppt.py --topic "Python 编程"

# 指定模板
python scripts/generate_ppt.py --topic "机器学习" --template academic

# 自定义输出
python scripts/generate_ppt.py --topic "产品设计" --output /tmp/demo.pptx
\`\`\`
```

---

### 开发实现

**generate_ppt.py**：
```python
#!/usr/bin/env python3
"""PPT 生成器脚本"""

import argparse
from pptx import Presentation
from pptx.util import Inches, Pt

def generate_outline(topic: str, slides: int) -> list:
    """生成 PPT 大纲"""
    # TODO: 使用 AI 生成大纲
    outline = [
        {"title": f"{topic} - 简介", "content": ["要点1", "要点2", "要点3"]},
        # ... 更多幻灯片
    ]
    return outline

def create_ppt(outline: list, template: str = None) -> Presentation:
    """创建 PPT"""
    prs = Presentation()

    for slide_data in outline:
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide.shapes.title
        title.text = slide_data["title"]

        content = slide.placeholders[1]
        for point in slide_data["content"]:
            content.text += f"• {point}\n"

    return prs

def main():
    parser = argparse.ArgumentParser(description="PPT 生成器")
    parser.add_argument("--topic", required=True, help="PPT 主题")
    parser.add_argument("--slides", type=int, default=10, help="幻灯片数量")
    parser.add_argument("--template", help="模板名称")
    parser.add_argument("--output", default="output.pptx", help="输出路径")

    args = parser.parse_args()

    # 生成大纲
    outline = generate_outline(args.topic, args.slides)

    # 创建 PPT
    prs = create_ppt(outline, args.template)

    # 保存
    prs.save(args.output)
    print(f"PPT 已生成：{args.output}")

if __name__ == "__main__":
    main()
```

---

### 测试计划

**测试场景**：
1. 基础功能测试
   - 生成 5 张幻灯片
   - 验证输出文件

2. 模板测试
   - 测试不同模板
   - 验证样式

3. 边界测试
   - 空 topic
   - 超长 topic
   - 负数 slides

4. 性能测试
   - 生成 50 张幻灯片
   - 测量时间

---

## 📚 学习资源

### OpenClaw Skills 文档
- [Skills 开发指南](https://docs.openclaw.ai/tools/skills)
- [SKILL.md 规范](https://docs.openclaw.ai/tools/skills#skill-md)
- [最佳实践](https://docs.openclaw.ai/tools/skills#best-practices)

### 示例技能
- [内置技能源码](https://github.com/openclaw/openclaw/tree/main/skills)
- [ClawHub 热门技能](https://clawhub.com)

---

## 🎯 里程碑

| 里程碑 | 目标日期 | 状态 |
|--------|----------|------|
| M1: 第一个技能完成 | 2026-02-24 | ⏳ 进行中 |
| M2: 三个技能完成 | 2026-02-26 | 📋 待开始 |
| M3: ClawHub 发布 | 2026-02-28 | 📋 待开始 |

---

*创建时间：2026-02-22*
*状态：开发阶段*
