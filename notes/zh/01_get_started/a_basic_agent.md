# 基础智能体

给 LLM 装上工具，让它能执行真实操作。

## 为什么需要 Agent

LLM 只能对话，不能查天气、调 API、操作数据库。Agent 让模型能调用工具，与现实世界交互。

## 工作流程

```
用户提问 → LLM 决定调用工具 → 执行工具 → 返回结果 → LLM 生成回答
```

## 代码

```python
import os
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek

api_key = os.getenv("DEEPSEEK_API_KEY")

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=api_key,
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

## 关键点

**工具定义**：普通函数 + 类型注解 + docstring，LangChain 自动解析

```python
def get_weather(city: str) -> str:  # 类型注解
    """Get weather for a given city."""  # docstring → 工具描述
    return f"It's always sunny in {city}!"
```

**消息类型**：

| 类型 | 说明 |
|------|------|
| `HumanMessage` | 用户输入 |
| `AIMessage` | 模型响应 |
| `ToolMessage` | 工具执行结果 |

**格式化输出**：

```python
for msg in result["messages"]:
    print(f"[{type(msg).__name__}] {msg.content}")
```

## 运行

```bash
python src/01_get_started/a_basic_agent.py
```
