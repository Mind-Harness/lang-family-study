# 使用 LangChain 官方 Skills 和 MCP 辅助开发

LangChain 官方提供了 **Skills** 和 **MCP** 两种方式来增强编程智能体的开发能力。

## Skills

Skills 是精心策划的指令和资源集合，让编程智能体成为 LangChain 开发专家。

**安装：**

```bash
npx skills add langchain-ai/langchain-skills --skill '*' --yes --global
```

安装后，智能体将掌握 LangChain、LangGraph、Deep Agents 的开发最佳实践。

## MCP

MCP (Model Context Protocol) 让智能体能按需访问 LangChain 官方文档。

**配置：**

```bash
claude mcp add-json langgraph-docs-mcp '{
  "type": "stdio",
  "command": "uvx",
  "args": ["--from", "mcpdoc", "mcpdoc", "--urls",
    "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt LangChain:https://python.langchain.com/llms.txt"]
}' -s user
```

配置后，智能体可以：
- `list_doc_sources` - 列出可用文档源
- `fetch_docs` - 获取指定文档内容

## 参考链接

- [LangChain Skills](https://github.com/langchain-ai/langchain-skills)
- [MCP 文档服务器](https://github.com/langchain-ai/mcpdoc)
- [LangChain MCP 文档](https://docs.langchain.com/oss/python/langchain/mcp/)
