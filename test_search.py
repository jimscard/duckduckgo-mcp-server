#!/usr/bin/env python3
"""Simple test script to verify DuckDuckGo search functionality"""
import asyncio
import sys
from duckduckgo_mcp_server.server import searcher, fetcher

class MockContext:
    """Mock MCP context for testing"""
    async def info(self, message: str):
        print(f"[INFO] {message}")
    
    async def error(self, message: str):
        print(f"[ERROR] {message}", file=sys.stderr)

async def test_search(query: str):
    """Test the search functionality"""
    print(f"\n{'='*60}")
    print(f"Testing DuckDuckGo Search")
    print(f"Query: {query}")
    print(f"{'='*60}\n")
    
    ctx = MockContext()
    results = await searcher.search(query, ctx, max_results=5)
    formatted = searcher.format_results_for_llm(results)
    
    print(formatted)
    print(f"\n{'='*60}")
    print(f"Test completed successfully!")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "scottish terrier costumes"
    asyncio.run(test_search(query))
