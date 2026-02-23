#!/usr/bin/env python3
"""
Advanced PPT to PNG Converter with Charts
支持图表渲染的增强版转换器
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def render_title_slide(draw, width, height, slide_data):
    """渲染标题页"""
    # 蓝色背景
    draw.rectangle([0, 0, width, height], fill='#2563EB')
    
    # 主标题
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # 标题
    title = slide_data.get('title', 'Title')
    bbox = draw.textbbox((0, 0), title, font=title_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, height // 2 - 80), title, fill='white', font=title_font)
    
    # 副标题
    subtitle = slide_data.get('subtitle', '')
    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, height // 2 + 50), subtitle, fill='#DBEAFE', font=subtitle_font)

def render_content_slide(draw, width, height, slide_data):
    """渲染内容页"""
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        content_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        desc_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except:
        title_font = ImageFont.load_default()
        content_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    
    # 标题栏
    draw.rectangle([0, 0, width, 100], fill='#2563EB')
    draw.text((40, 25), slide_data.get('title', ''), fill='white', font=title_font)
    
    # 内容
    y_pos = 150
    for item in slide_data.get('content', []):
        # 圆点
        draw.ellipse([50, y_pos + 8, 68, y_pos + 26], fill='#3B82F6')
        
        if isinstance(item, dict):
            # 标题
            draw.text((80, y_pos), item.get('title', ''), fill='#1E3A8A', font=content_font)
            # 描述
            desc = item.get('desc', '')
            if desc:
                # 自动换行
                words = desc.split()
                lines = []
                current_line = []
                for word in words:
                    current_line.append(word)
                    test_line = ' '.join(current_line)
                    bbox = draw.textbbox((0, 0), test_line, font=desc_font)
                    if bbox[2] - bbox[0] > width - 200:
                        current_line.pop()
                        lines.append(' '.join(current_line))
                        current_line = [word]
                lines.append(' '.join(current_line))
                
                for i, line in enumerate(lines):
                    draw.text((80, y_pos + 30 + i * 25), line, fill='#6B7280', font=desc_font)
                y_pos += 30 + len(lines) * 25
        else:
            draw.text((80, y_pos), str(item), fill='#374151', font=content_font)
        
        y_pos += 70

def render_chart_slide(draw, width, height, slide_data):
    """渲染柱状图页"""
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        value_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        value_font = ImageFont.load_default()
    
    # 标题栏
    draw.rectangle([0, 0, width, 100], fill='#2563EB')
    draw.text((40, 25), slide_data.get('title', ''), fill='white', font=title_font)
    
    # 图表区域
    data = slide_data.get('chart_data', [])
    if not data:
        return
    
    max_val = max(item['value'] for item in data)
    chart_left = 150
    chart_right = width - 150
    chart_top = 180
    chart_bottom = height - 150
    chart_width = chart_right - chart_left
    chart_height = chart_bottom - chart_top
    
    # 绘制坐标轴
    draw.line([(chart_left, chart_bottom), (chart_right, chart_bottom)], fill='#E5E7EB', width=2)
    draw.line([(chart_left, chart_top), (chart_left, chart_bottom)], fill='#E5E7EB', width=2)
    
    # 计算柱子宽度
    bar_count = len(data)
    bar_gap = 40
    total_gaps = (bar_count + 1) * bar_gap
    bar_width = (chart_width - total_gaps) // bar_count
    
    # 绘制柱子
    for i, item in enumerate(data):
        bar_height = int((item['value'] / max_val) * chart_height * 0.8)
        x_left = chart_left + (i + 1) * bar_gap + i * bar_width
        x_right = x_left + bar_width
        y_top = chart_bottom - bar_height
        
        # 柱子（渐变效果用纯色模拟）
        draw.rectangle([x_left, y_top, x_right, chart_bottom], fill='#3B82F6', outline='#2563EB')
        
        # 数值
        value_text = f"{item['value']:.0f}K"
        bbox = draw.textbbox((0, 0), value_text, font=value_font)
        text_width = bbox[2] - bbox[0]
        x_center = (x_left + x_right) // 2
        draw.text((x_center - text_width // 2, y_top - 30), value_text, fill='#2563EB', font=value_font)
        
        # 名称
        name = item['name']
        bbox = draw.textbbox((0, 0), name, font=label_font)
        text_width = bbox[2] - bbox[0]
        draw.text((x_center - text_width // 2, chart_bottom + 20), name, fill='#374151', font=label_font)

def render_comparison_slide(draw, width, height, slide_data):
    """渲染对比表格页"""
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        stars_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        desc_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        title_font = ImageFont.load_default()
        name_font = ImageFont.load_default()
        stars_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    
    # 标题栏
    draw.rectangle([0, 0, width, 100], fill='#2563EB')
    draw.text((40, 25), slide_data.get('title', ''), fill='white', font=title_font)
    
    # 表格
    items = slide_data.get('comparison_data', [])
    y_pos = 150
    row_height = 90
    
    for i, item in enumerate(items):
        # 行背景
        bg_color = '#F9FAFB' if i % 2 == 0 else '#FFFFFF'
        draw.rectangle([50, y_pos, width - 50, y_pos + row_height], fill=bg_color, outline='#E5E7EB')
        
        # 名称
        draw.text((70, y_pos + 15), item.get('name', ''), fill='#1E3A8A', font=name_font)
        
        # Stars
        draw.text((350, y_pos + 20), item.get('stars', ''), fill='#EAB308', font=stars_font)
        
        # 描述
        desc = item.get('desc', '')
        # 自动换行
        words = desc.split()
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            test_line = ' '.join(current_line)
            bbox = draw.textbbox((0, 0), test_line, font=desc_font)
            if bbox[2] - bbox[0] > width - 550:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))
        
        for j, line in enumerate(lines[:2]):  # 最多2行
            draw.text((500, y_pos + 15 + j * 22), line, fill='#6B7280', font=desc_font)
        
        y_pos += row_height

def create_detailed_ppt_images():
    """创建详细版 PPT 图片"""
    output_dir = Path('/home/curry/.openclaw/workspace/ppt-preview/enhanced')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    width, height = 1920, 1080
    
    slides = [
        # Slide 1: Title
        {
            'type': 'title',
            'title': 'AI Agent Frameworks 2026',
            'subtitle': 'Comprehensive Guide with Charts & Tables'
        },
        # Slide 2: Chart
        {
            'type': 'chart',
            'title': 'GitHub Stars Comparison (K)',
            'chart_data': [
                {'name': 'AutoGPT', 'value': 165},
                {'name': 'LangChain', 'value': 127},
                {'name': 'MetaGPT', 'value': 64},
                {'name': 'Letta', 'value': 21},
                {'name': 'DeerFlow', 'value': 20},
            ]
        },
        # Slide 3: Comparison Table
        {
            'type': 'comparison',
            'title': 'Framework Comparison',
            'comparison_data': [
                {'name': 'LangChain', 'stars': '⭐ 127K', 'desc': 'Universal framework, 50+ LLM providers, production-ready'},
                {'name': 'AutoGPT', 'stars': '⭐ 165K', 'desc': 'First autonomous agent, self-prompting, internet access'},
                {'name': 'MetaGPT', 'stars': '⭐ 64K', 'desc': 'Multi-agent teams, software company simulation'},
                {'name': 'DeerFlow', 'stars': '⭐ 20K', 'desc': 'ByteDance SuperAgent, long tasks, sandbox support'},
                {'name': 'Letta', 'stars': '⭐ 21K', 'desc': 'Stateful agents, advanced memory, self-improvement'},
            ]
        },
        # Slide 4-8: Detailed Content
        {
            'type': 'content',
            'title': 'LangChain - Universal Framework',
            'content': [
                {'title': '📦 Core Components', 'desc': 'Chains, Agents, Memory, Tools, Retrievers - modular building blocks for LLM apps'},
                {'title': '🔌 LLM Support', 'desc': '50+ providers: OpenAI, Anthropic, Google, HuggingFace, local models'},
                {'title': '🏭 Production Ready', 'desc': 'LangSmith for monitoring, LangServe for deployment, evaluation tools'},
                {'title': '👥 Community', 'desc': '2000+ contributors, 100+ templates, extensive documentation'},
                {'title': '💡 Best For', 'desc': 'Building custom LLM applications, RAG systems, chatbots, agents'},
            ]
        },
        {
            'type': 'content',
            'title': 'AutoGPT - Autonomous Pioneer',
            'content': [
                {'title': '🤖 Core Concept', 'desc': 'Fully autonomous agent that self-prompts and plans tasks without human intervention'},
                {'title': '🌐 Capabilities', 'desc': 'Internet access, file operations, code execution, API calls'},
                {'title': '🎯 How It Works', 'desc': 'Goal → Sub-tasks → Execute → Evaluate → Iterate (loop until done)'},
                {'title': '🌟 Impact', 'desc': 'Inspired 1000+ clones: GPT-Engineer, AgentGPT, BabyAGI, OpenDevin'},
                {'title': '⚠️ Challenges', 'desc': 'Can get stuck in loops, expensive API calls, reliability issues'},
            ]
        },
        {
            'type': 'content',
            'title': 'MetaGPT - Multi-Agent Teams',
            'content': [
                {'title': '👥 Team Simulation', 'desc': 'Simulates a software company with specialized agents (PM, Architect, Engineer)'},
                {'title': '🎭 Roles', 'desc': 'Product Manager, Architect, Engineer, QA, Project Manager - each with specific tasks'},
                {'title': '🔄 Workflow', 'desc': 'Requirements → Design → Code → Test → Deploy (full software lifecycle)'},
                {'title': '✨ Unique Feature', 'desc': 'Complete software project from one prompt (PRD → code → docs)'},
                {'title': '📊 Results', 'desc': 'Generated games, apps, tools in minutes - impressive demos'},
            ]
        },
        {
            'type': 'content',
            'title': 'DeerFlow - ByteDance SuperAgent',
            'content': [
                {'title': '⏱️ Long-Running Tasks', 'desc': 'Handle tasks from minutes to hours (not just quick Q&A)'},
                {'title': '🛠️ Components', 'desc': 'Skills, Tools, Sub-agents, Sandbox, File System, Context Engineering'},
                {'title': '🧠 Memory', 'desc': 'Long-term memory integration, cross-session persistence'},
                {'title': '🔒 Safety', 'desc': 'Sandbox execution, permission control, audit logs'},
                {'title': '🏢 Backed By', 'desc': 'ByteDance (TikTok parent), enterprise-grade, production-ready'},
            ]
        },
        {
            'type': 'content',
            'title': 'Framework Selection Guide',
            'content': [
                {'title': '🎓 Learning & Prototyping', 'desc': 'LangChain - Best documentation, largest community, most examples'},
                {'title': '🚀 Quick Autonomous Tasks', 'desc': 'AutoGPT - Simple setup, self-driven, good for experimentation'},
                {'title': '🏢 Team Projects', 'desc': 'MetaGPT - Role-based collaboration, software development'},
                {'title': '⏰ Long-Running Tasks', 'desc': 'DeerFlow - Hours-long tasks, enterprise features, production'},
                {'title': '💡 Recommendation', 'desc': 'Start with LangChain for learning, explore others based on specific needs'},
            ]
        },
    ]
    
    for i, slide_data in enumerate(slides, 1):
        img = Image.new('RGB', (width, height), '#FFFFFF')
        draw = ImageDraw.Draw(img)
        
        slide_type = slide_data.get('type', 'content')
        
        if slide_type == 'title':
            render_title_slide(draw, width, height, slide_data)
        elif slide_type == 'chart':
            render_chart_slide(draw, width, height, slide_data)
        elif slide_type == 'comparison':
            render_comparison_slide(draw, width, height, slide_data)
        else:
            render_content_slide(draw, width, height, slide_data)
        
        # 保存
        img_path = output_dir / f'slide_{i:02d}.png'
        img.save(img_path, 'PNG', quality=95)
        print(f"✅ Slide {i}: {img_path}")
    
    print(f"\n✨ Total: {len(slides)} slides")
    print(f"📁 Location: {output_dir}")

if __name__ == "__main__":
    print("Creating Enhanced PPT Images with Charts...")
    print("=" * 60)
    create_detailed_ppt_images()
    print("=" * 60)
    print("✨ Done!")
