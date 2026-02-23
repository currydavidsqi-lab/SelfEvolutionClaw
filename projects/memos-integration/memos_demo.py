#!/usr/bin/env python3
"""
MemOS 集成 Demo
需要 MemOS API Key 和服务运行
"""

import os
import requests
from typing import Optional

class MemOSClient:
    """MemOS 简单客户端"""

    def __init__(self, api_key: str, base_url: str = "http://localhost:8000"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def add_memory(self, user_id: str, content: str, metadata: dict = None) -> dict:
        """添加记忆"""
        url = f"{self.base_url}/product/add"
        payload = {
            "user_id": user_id,
            "content": content,
            "metadata": metadata or {}
        }
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def search_memory(self, user_id: str, query: str, top_k: int = 10) -> dict:
        """搜索记忆"""
        url = f"{self.base_url}/product/search"
        payload = {
            "user_id": user_id,
            "query": query,
            "top_k": top_k
        }
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def list_memories(self, user_id: str) -> dict:
        """列出用户所有记忆"""
        url = f"{self.base_url}/product/list"
        params = {"user_id": user_id}
        response = requests.get(url, params=params, headers=self.headers)
        return response.json()


def demo():
    """MemOS 演示"""
    # 从环境变量获取 API Key
    api_key = os.getenv("MEMOS_API_KEY", "your-api-key-here")
    base_url = os.getenv("MEMOS_BASE_URL", "http://localhost:8000")

    client = MemOSClient(api_key, base_url)

    user_id = "demo-user-001"

    # 1. 添加记忆
    print("📝 添加记忆...")
    result = client.add_memory(
        user_id=user_id,
        content="用户喜欢吃草莓",
        metadata={"type": "preference", "category": "food"}
    )
    print(f"✅ 添加结果：{result}")

    # 2. 搜索记忆
    print("\n🔍 搜索记忆...")
    result = client.search_memory(
        user_id=user_id,
        query="用户喜欢吃什么？"
    )
    print(f"✅ 搜索结果：{result}")

    # 3. 列出所有记忆
    print("\n📋 列出所有记忆...")
    result = client.list_memories(user_id=user_id)
    print(f"✅ 记忆列表：{result}")


if __name__ == "__main__":
    print("=" * 50)
    print("MemOS 集成 Demo")
    print("=" * 50)
    print("\n⚠️ 需要：")
    print("1. MemOS 服务运行中（localhost:8000）")
    print("2. 设置环境变量 MEMOS_API_KEY")
    print("\n启动命令：")
    print("export MEMOS_API_KEY=your-key")
    print("python memos_demo.py")
    print("=" * 50)

    try:
        demo()
    except Exception as e:
        print(f"\n❌ 错误：{e}")
        print("请确保 MemOS 服务正在运行")
