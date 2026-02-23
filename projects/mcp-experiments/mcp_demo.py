#!/usr/bin/env python3
"""
MCP Server 测试 Demo
展示如何与 MCP 服务器交互
"""

import subprocess
import json

def test_filesystem_mcp():
    """测试 Filesystem MCP Server"""
    print("=" * 50)
    print("MCP Filesystem Server 测试")
    print("=" * 50)

    # MCP 协议交互示例
    print("\n1. MCP 协议基于 JSON-RPC 2.0")
    print("   服务器通过 stdio 通信")

    # 初始化请求示例
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }

    print(f"\n2. 初始化请求示例：")
    print(json.dumps(init_request, indent=2))

    # 列出工具请求
    list_tools_request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list"
    }

    print(f"\n3. 列出工具请求：")
    print(json.dumps(list_tools_request, indent=2))

    print("\n" + "=" * 50)
    print("MCP 服务器启动命令：")
    print("  npx @modelcontextprotocol/server-filesystem /tmp")
    print("\n可用工具（预期）：")
    print("  - read_file: 读取文件")
    print("  - write_file: 写入文件")
    print("  - list_directory: 列出目录")
    print("  - search_files: 搜索文件")
    print("=" * 50)


def show_popular_mcp_servers():
    """展示热门 MCP Servers"""
    print("\n📊 热门 MCP Servers")
    print("=" * 50)

    servers = [
        ("filesystem", "官方", "文件系统操作"),
        ("github", "GitHub", "GitHub API 集成"),
        ("playwright", "Microsoft", "浏览器自动化"),
        ("memory", "官方", "知识图谱记忆"),
        ("postgres", "官方", "PostgreSQL 数据库"),
        ("sqlite", "官方", "SQLite 数据库"),
    ]

    for name, provider, desc in servers:
        print(f"  • {name:15} ({provider:10}) - {desc}")

    print("=" * 50)


if __name__ == "__main__":
    test_filesystem_mcp()
    show_popular_mcp_servers()

    print("\n💡 下一步：")
    print("  1. 安装 Claude Desktop 或其他 MCP 客户端")
    print("  2. 配置 MCP 服务器")
    print("  3. 测试工具调用")
    print("\n📚 参考：https://modelcontextprotocol.io/")
