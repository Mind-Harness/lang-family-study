# Using LangChain Skills and MCP for Development Assistance

LangChain provides two ways to enhance your coding agent's capabilities: **Skills** and **MCP**.

## Skills

Skills are curated instructions and resources that turn coding agents into LangChain development experts.

**Installation:**

```bash
npx skills add langchain-ai/langchain-skills --skill '*' --yes --global
```

After installation, your agent will have best practices for LangChain, LangGraph, and Deep Agents development.

## MCP

MCP (Model Context Protocol) allows agents to access LangChain official documentation on demand.

**Configuration:**

```bash
claude mcp add-json langgraph-docs-mcp '{
  "type": "stdio",
  "command": "uvx",
  "args": ["--from", "mcpdoc", "mcpdoc", "--urls",
    "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt LangChain:https://python.langchain.com/llms.txt"]
}' -s user
```

After configuration, your agent can:
- `list_doc_sources` - List available documentation sources
- `fetch_docs` - Fetch specific documentation content

## References

- [LangChain Skills](https://github.com/langchain-ai/langchain-skills)
- [MCP Doc Server](https://github.com/langchain-ai/mcpdoc)
- [LangChain MCP Documentation](https://docs.langchain.com/oss/python/langchain/mcp/)
