#!/usr/bin/env python3
"""
Deep Technical PPT Generator
深入技术架构的 PPT 生成器
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def create_langchain_deep_dive():
    """创建 LangChain 深度技术 PPT"""
    output_dir = Path('/home/curry/.openclaw/workspace/ppt-preview/deep-langchain')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    width, height = 1920, 1080
    
    slides = [
        {
            'type': 'title',
            'title': 'LangChain Architecture Deep Dive',
            'subtitle': 'Technical Analysis of Core Components & Design'
        },
        {
            'type': 'architecture',
            'title': 'LangChain Ecosystem Architecture',
            'content': [
                '┌─────────────────────────────────────────┐',
                '│         LangChain Platform              │',
                '├─────────────────────────────────────────┤',
                '│  ┌──────────┐  ┌──────────┐  ┌───────┐ │',
                '│  │LangChain │  │LangGraph │  │LangSm │ │',
                '│  │Framework │  │  Agent   │  │Observ │ │',
                '│  └──────────┘  └──────────┘  └───────┘ │',
                '│  ┌──────────┐  ┌──────────┐  ┌───────┐ │',
                '│  │LangServe │  │Templates │  │Hub    │ │',
                '│  │Deployment│  │ & Examples│ │Community│',
                '│  └──────────┘  └──────────┘  └───────┘ │',
                '└─────────────────────────────────────────┘',
            ]
        },
        {
            'type': 'modules',
            'title': 'Core Modules Breakdown',
            'modules': [
                {
                    'name': '1. langchain-core',
                    'desc': 'Base abstractions: BaseLanguage, BaseChatModel, BaseRetriever, BaseTool',
                    'files': '150+ base classes, interfaces, schemas'
                },
                {
                    'name': '2. langchain-community',
                    'desc': 'Third-party integrations: 50+ LLMs, 40+ vector stores, 30+ tools',
                    'files': '800+ integration implementations'
                },
                {
                    'name': '3. langchain',
                    'desc': 'Chains, Agents, Memory, Prompts, Utilities',
                    'files': '200+ chain types, agent strategies'
                },
                {
                    'name': '4. langgraph',
                    'desc': 'Stateful agent orchestration, cycles, persistence',
                    'files': 'Graph-based workflow engine'
                },
            ]
        },
        {
            'type': 'code',
            'title': 'Core Abstractions: Base LLM Interface',
            'code': '''class BaseLLM(Runnable[LanguageModelInput, str]):
    """Abstract base class for all LLM implementations"""
    
    @abstractmethod
    def _generate(
        self,
        prompts: List[str],
        *,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> LLMResult:
        """Run the LLM on the given prompts"""
        pass
    
    @abstractmethod
    def _llm_type(self) -> str:
        """Return type of LLM"""
        pass
    
    def invoke(
        self,
        input: LanguageModelInput,
        config: Optional[RunnableConfig] = None,
        **kwargs: Any,
    ) -> str:
        """Invoke the LLM with input"""
        return self._generate([input], **kwargs).generations[0][0].text'''
        },
        {
            'type': 'code',
            'title': 'Chain Architecture: Sequential Chain',
            'code': '''class SequentialChain(Chain):
    """Chain that runs multiple chains in sequence"""
    
    chains: List[Chain] = Field(default_factory=list)
    input_variables: List[str] = Field(default_factory=list)
    output_variables: List[str] = Field(default_factory=list)
    
    def _call(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        """Execute chains in sequence, passing outputs forward"""
        _inputs = inputs.copy()
        
        for i, chain in enumerate(self.chains):
            # Pass previous outputs to next chain
            _outputs = chain(_inputs, callbacks=run_manager)
            _inputs.update(_outputs)
        
        # Return only requested outputs
        return {k: _inputs[k] for k in self.output_variables}'''
        },
        {
            'type': 'flowchart',
            'title': 'RAG Pipeline Architecture',
            'content': [
                '┌──────────────┐    ┌──────────────┐    ┌──────────────┐',
                '│   Document   │───▶│   Embedding  │───▶│Vector Store  │',
                '│   Loader     │    │   Model      │    │(Chroma/FAISS)│',
                '└──────────────┘    └──────────────┘    └──────┬───────┘',
                '                                                 │',
                '┌──────────────┐    ┌──────────────┐    ┌──────▼───────┐',
                '│    Query     │───▶│  Embedding   │───▶│  Retriever   │',
                '│              │    │  (Same)      │    │  Top-K Docs  │',
                '└──────────────┘    └──────────────┘    └──────┬───────┘',
                '                                                 │',
                '┌──────────────┐    ┌──────────────┐    ┌──────▼───────┐',
                '│   Context    │◀───│    Prompt    │◀───│   Relevant   │',
                '│  + Question  │    │  Template    │    │   Documents  │',
                '└──────┬───────┘    └──────────────┘    └──────────────┘',
                '       │',
                '       ▼',
                '┌──────────────┐',
                '│     LLM      │',
                '│  Generation  │',
                '└──────────────┘',
            ]
        },
        {
            'type': 'modules',
            'title': 'Memory System Architecture',
            'modules': [
                {
                    'name': '1. ConversationBufferMemory',
                    'desc': 'Stores all messages in raw form. Simple but token-heavy.',
                    'files': 'Pro: Complete history | Con: Context limit'
                },
                {
                    'name': '2. ConversationBufferWindowMemory',
                    'desc': 'Keeps last N messages. Balanced approach.',
                    'files': 'Pro: Controlled size | Con: Loses early context'
                },
                {
                    'name': '3. VectorStoreRetrieverMemory',
                    'desc': 'Semantic search over history. Scalable.',
                    'files': 'Pro: Relevant recall | Con: Requires embedding'
                },
                {
                    'name': '4. ConversationKnowledgeGraphMemory',
                    'desc': 'Extracts entities and relations. Structured.',
                    'files': 'Pro: Rich relationships | Con: Complex setup'
                },
            ]
        },
        {
            'type': 'table',
            'title': 'Agent Types Comparison',
            'headers': ['Agent Type', 'Strategy', 'Best For', 'Limitations'],
            'rows': [
                ['Zero-shot', 'No examples, pure reasoning', 'Simple tasks', 'Unreliable for complex'],
                ['ReAct', 'Reasoning + Acting loop', 'Tool usage', 'Can loop infinitely'],
                ['Structured', 'JSON parsing', 'API calls', 'Requires format'],
                ['OpenAI Functions', 'Native tool calling', 'GPT models', 'Model specific'],
                ['Plan-and-Execute', 'Plan first, then execute', 'Multi-step tasks', 'Overhead for simple'],
            ]
        },
    ]
    
    render_slides(slides, output_dir, width, height)

def create_deerflow_deep_dive():
    """创建 DeerFlow 深度技术 PPT"""
    output_dir = Path('/home/curry/.openclaw/workspace/ppt-preview/deep-deerflow')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    width, height = 1920, 1080
    
    slides = [
        {
            'type': 'title',
            'title': 'DeerFlow 2.0 Architecture',
            'subtitle': 'Super Agent Harness - Technical Deep Dive'
        },
        {
            'type': 'architecture',
            'title': 'DeerFlow System Architecture',
            'content': [
                '┌───────────────────────────────────────────────────┐',
                '│                  Frontend (React)                 │',
                '│              http://localhost:2026                │',
                '└────────────────────┬──────────────────────────────┘',
                '                     │',
                '┌────────────────────▼──────────────────────────────┐',
                '│            Backend (FastAPI + Python)             │',
                '│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌──────┐ │',
                '│  │  Agent  │  │ Memory  │  │ Sandbox │  │Tools │ │',
                '│  │ Engine  │  │ Manager │  │ Runtime │  │Manager│ │',
                '│  └─────────┘  └─────────┘  └─────────┘  └──────┘ │',
                '└────────────────────┬──────────────────────────────┘',
                '                     │',
                '┌────────────────────▼──────────────────────────────┐',
                '│           Sandbox Container (Docker)              │',
                '│  ┌──────────┐  ┌──────────┐  ┌───────────────┐   │',
                '│  │/mnt/user │  │/mnt/skill│  │  Workspace    │   │',
                '│  │  /data   │  │  s/      │  │  Environment  │   │',
                '│  └──────────┘  └──────────┘  └───────────────┘   │',
                '└───────────────────────────────────────────────────┘',
            ]
        },
        {
            'type': 'filesystem',
            'title': 'Sandbox File System Structure',
            'content': [
                '/mnt/',
                '├── user-data/',
                '│   ├── uploads/          # User uploaded files',
                '│   ├── workspace/         # Agent working directory',
                '│   └── outputs/           # Final deliverables',
                '├── skills/',
                '│   ├── public/',
                '│   │   ├── research/SKILL.md',
                '│   │   ├── report-generation/SKILL.md',
                '│   │   ├── slide-creation/SKILL.md',
                '│   │   ├── web-page/SKILL.md',
                '│   │   └── image-generation/SKILL.md',
                '│   └── custom/',
                '│       └── your-skill/SKILL.md',
                '└── system/',
                '    ├── tools/',
                '    └── templates/',
            ]
        },
        {
            'type': 'modules',
            'title': 'Core Components Deep Dive',
            'modules': [
                {
                    'name': '1. Agent Engine (LangGraph)',
                    'desc': 'State machine orchestration: Plan → Execute → Evaluate → Iterate',
                    'files': 'backend/agent/graph.py, nodes/, state.py'
                },
                {
                    'name': '2. Memory System',
                    'desc': 'User profile, preferences, cross-session persistence',
                    'files': 'backend/memory/user_profile.py, session_store.py'
                },
                {
                    'name': '3. Sandbox Runtime',
                    'desc': 'Isolated Docker container execution, file operations',
                    'files': 'backend/sandbox/docker_manager.py, executor.py'
                },
                {
                    'name': '4. Skills & Tools',
                    'desc': 'Modular capability system, MCP server integration',
                    'files': 'backend/skills/loader.py, mcp_client.py'
                },
            ]
        },
        {
            'type': 'code',
            'title': 'Skill Definition Structure',
            'code': '''# /mnt/skills/public/research/SKILL.md
---
name: research
description: Deep research capability
version: 2.0
requires: [web_search, web_fetch, file_write]
---

# Research Skill

## Workflow
1. Understand Topic: Analyze question
2. Search: Query sources
3. Extract: Fetch content
4. Synthesize: Combine findings
5. Report: Generate output

## Best Practices
- Multiple search queries
- Prioritize authoritative sources
- Cite with links
- Structure output

## Usage
agent.use_skill("research", {
    "topic": "AI agents",
    "depth": "comprehensive"
})'''        },
        {
            'type': 'flowchart',
            'title': 'Sub-Agent Orchestration Flow',
            'content': [
                '┌──────────────┐',
                '│  Lead Agent  │',
                '│   (Main)     │',
                '└──────┬───────┘',
                '       │ Decompose Task',
                '       ▼',
                '┌──────────────┐     ┌──────────────┐     ┌──────────────┐',
                '│ Sub-Agent 1  │     │ Sub-Agent 2  │     │ Sub-Agent 3  │',
                '│  (Research)  │     │  (Analysis)  │     │ (Generation) │',
                '└──────┬───────┘     └──────┬───────┘     └──────┬───────┘',
                '       │                    │                    │',
                '       │ Parallel Execution  │                    │',
                '       ▼                    ▼                    ▼',
                '┌──────────────┐     ┌──────────────┐     ┌──────────────┐',
                '│ Isolated     │     │ Isolated     │     │ Isolated     │',
                '│ Context      │     │ Context      │     │ Context      │',
                '└──────┬───────┘     └──────┬───────┘     └──────┬───────┘',
                '       │                    │                    │',
                '       └────────────────────┴────────────────────┘',
                '                            │',
                '                            ▼',
                '                    ┌──────────────┐',
                '                    │  Synthesis   │',
                '                    │  & Output    │',
                '                    └──────────────┘',
            ]
        },
        {
            'type': 'modules',
            'title': 'Context Engineering Strategies',
            'modules': [
                {
                    'name': '1. Progressive Skill Loading',
                    'desc': 'Load skills only when task requires them',
                    'files': 'Keeps context lean, works with token-sensitive models'
                },
                {
                    'name': '2. Sub-Agent Isolation',
                    'desc': 'Each sub-agent has separate context window',
                    'files': 'No contamination, focused execution'
                },
                {
                    'name': '3. Summarization Pipeline',
                    'desc': 'Compress completed sub-tasks, offload to filesystem',
                    'files': 'Stay sharp across long multi-step tasks'
                },
                {
                    'name': '4. Long-Term Memory',
                    'desc': 'User profile, preferences, accumulated knowledge',
                    'files': 'Better personalization over time'
                },
            ]
        },
        {
            'type': 'table',
            'title': 'Sandbox Execution Modes',
            'headers': ['Mode', 'Description', 'Pros', 'Cons'],
            'rows': [
                ['Local', 'Run directly on host', 'Fast, simple', 'Less isolated'],
                ['Docker', 'Isolated container', 'Secure, reproducible', 'Overhead'],
                ['Kubernetes', 'K8s pods via provisioner', 'Scalable, enterprise', 'Complex setup'],
            ]
        },
    ]
    
    render_slides(slides, output_dir, width, height)

def render_slides(slides, output_dir, width, height):
    """渲染所有幻灯片"""
    # 加载字体
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 56)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        content_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 18)
        module_title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        module_desc_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        code_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        content_font = ImageFont.load_default()
        module_title_font = ImageFont.load_default()
        module_desc_font = ImageFont.load_default()
        code_font = ImageFont.load_default()
    
    for i, slide_data in enumerate(slides, 1):
        img = Image.new('RGB', (width, height), '#FFFFFF')
        draw = ImageDraw.Draw(img)
        
        slide_type = slide_data.get('type', 'content')
        
        # 标题栏
        draw.rectangle([0, 0, width, 100], fill='#1E40AF')
        draw.text((50, 25), slide_data.get('title', ''), fill='white', font=title_font)
        
        if slide_type == 'title':
            # 标题页特殊处理
            draw.rectangle([0, 0, width, height], fill='#1E40AF')
            title = slide_data.get('title', '')
            subtitle = slide_data.get('subtitle', '')
            
            bbox = draw.textbbox((0, 0), title, font=title_font)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            draw.text((x, height // 2 - 100), title, fill='white', font=title_font)
            
            bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            draw.text((x, height // 2 + 20), subtitle, fill='#DBEAFE', font=subtitle_font)
        
        elif slide_type == 'architecture' or slide_type == 'filesystem' or slide_type == 'flowchart':
            # 架构图/文件系统
            y_pos = 150
            for line in slide_data.get('content', []):
                draw.text((100, y_pos), line, fill='#1F2937', font=content_font)
                y_pos += 35
        
        elif slide_type == 'modules':
            # 模块详解
            y_pos = 150
            for module in slide_data.get('modules', []):
                # 模块名
                draw.text((100, y_pos), module['name'], fill='#1E3A8A', font=module_title_font)
                # 描述
                y_pos += 35
                draw.text((120, y_pos), module['desc'], fill='#374151', font=module_desc_font)
                # 文件
                y_pos += 30
                draw.text((120, y_pos), f"Files: {module['files']}", fill='#6B7280', font=module_desc_font)
                y_pos += 60
        
        elif slide_type == 'code':
            # 代码展示
            code_bg_top = 140
            code_bg_bottom = height - 50
            draw.rectangle([80, code_bg_top, width - 80, code_bg_bottom], fill='#1F2937')
            
            code = slide_data.get('code', '')
            y_pos = code_bg_top + 20
            for line in code.split('\n'):
                # 语法高亮（简化版）
                color = '#10B981' if 'def ' in line or 'class ' in line else '#F9FAFB'
                if line.strip().startswith('#'):
                    color = '#9CA3AF'
                draw.text((100, y_pos), line, fill=color, font=code_font)
                y_pos += 22
        
        elif slide_type == 'table':
            # 表格
            headers = slide_data.get('headers', [])
            rows = slide_data.get('rows', [])
            
            y_pos = 160
            row_height = 70
            
            # 表头
            draw.rectangle([80, y_pos - 10, width - 80, y_pos + row_height], fill='#3B82F6')
            x_pos = 100
            for header in headers:
                draw.text((x_pos, y_pos + 15), header, fill='white', font=module_title_font)
                x_pos += (width - 200) // len(headers)
            y_pos += row_height + 10
            
            # 数据行
            for i, row in enumerate(rows):
                bg_color = '#F9FAFB' if i % 2 == 0 else '#FFFFFF'
                draw.rectangle([80, y_pos, width - 80, y_pos + row_height], fill=bg_color, outline='#E5E7EB')
                
                x_pos = 100
                for cell in row:
                    draw.text((x_pos, y_pos + 20), str(cell), fill='#374151', font=module_desc_font)
                    x_pos += (width - 200) // len(headers)
                
                y_pos += row_height
        
        # 保存
        img_path = output_dir / f'slide_{i:02d}.png'
        img.save(img_path, 'PNG', quality=95)
        print(f"✅ Slide {i}: {img_path}")
    
    print(f"\n✨ Total: {len(slides)} slides")
    print(f"📁 Location: {output_dir}")

if __name__ == "__main__":
    print("Creating Deep Technical PPTs...")
    print("=" * 60)
    
    print("\n📊 Creating LangChain Deep Dive...")
    create_langchain_deep_dive()
    
    print("\n📊 Creating DeerFlow Deep Dive...")
    create_deerflow_deep_dive()
    
    print("=" * 60)
    print("✨ All Done!")
