# 静态工具

静态工具在创建代理时定义，执行过程中保持不变。这是最常见且最直接的方法。

## 基本用法

```python
from langchain.tools import tool
from langchain.agents import create_agent

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"

agent = create_agent(model, tools=[search, get_weather])
```

## 工具属性

`@tool` 装饰器可用于自定义工具名称、描述、参数模式及其他属性。

## 注意事项

如果提供空工具列表，代理将由一个没有工具调用功能的 LLM 节点组成。
