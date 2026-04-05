# 构建真实世界的 Agent

接下来，构建一个实用的天气预报代理，展示关键的生产概念：

- 详细的系统提示词，帮助代理表现更好
- 创建能够与外部数据集成的工具
- 一致响应的模型配置
- 结构化输出以实现可预测的结果
- 用于类似聊天交互的会话记忆
- 创建并运行该代理来测试功能齐全的代理

让我们逐步走一遍：

## 1. 定义系统提示词

系统提示词定义了你的代理的角色和行为。保持具体且可执行：

```python
SYSTEM_PROMPT = """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
- get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location."""
```

## 2. 创建工具

工具可以通过调用你定义的函数，让模型与外部系统交互。工具可以依赖运行时上下文，也可以与代理内存交互。

请注意下面 `get_user_location` 工具如何使用运行时上下文：

```python
from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime

@tool
def get_weather_for_location(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str

@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "SF"
```

工具应有充分的文档：其名称、描述和参数名称都成为模型提示的一部分。LangChain 的 `@tool` 装饰器通过 `ToolRuntime` 参数添加元数据并启用运行时注入。更多信息请参阅工具指南。

## 3. 配置模型

根据你的用例设置合适的参数：

```python
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0.5,
    timeout=10,
    max_tokens=1000
)
```

根据所选模型和提供者，初始化参数可能有所不同；详情请参阅他们的参考页面。

## 4. 定义响应格式

如果你需要代理响应匹配特定模式，也可以选择定义结构化响应格式。

```python
from dataclasses import dataclass

# We use a dataclass here, but Pydantic models are also supported.
@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A punny response (always required)
    punny_response: str
    # Any interesting information about the weather if available
    weather_conditions: str | None = None
```

## 5. 添加内存

给代理添加内存以维持交互间的状态。这使代理能够记住之前的对话和上下文。

```python
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
```

在生产环境中，使用持久检查点，将消息历史保存到数据库中。详情请参见添加和管理内存。

## 6. 创建并运行代理

现在把你的代理和所有组件组装起来，运行起来！

```python
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location, get_weather_for_location],
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)

# `thread_id` is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])
# ResponseFormat(
#     punny_response="Florida is still having a 'sun-derful' day! The sunshine is playing 'ray-dio' hits all day long! I'd say it's the perfect weather for some 'solar-bration'! If you were hoping for rain, I'm afraid that idea is all 'washed up' - the forecast remains 'clear-ly' brilliant!",
#     weather_conditions="It's always sunny in Florida!"
# )


# Note that we can continue the conversation using the same `thread_id`.
response = agent.invoke(
    {"messages": [{"role": "user", "content": "thank you!"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])
# ResponseFormat(
#     punny_response="You're 'thund-erfully' welcome! It's always a 'breeze' to help you stay 'current' with the weather. I'm just 'cloud'-ing around waiting to 'shower' you with more forecasts whenever you need them. Have a 'sun-sational' day in the Florida sunshine!",
#     weather_conditions=None
# )
```

## 总结

恭喜你！你现在拥有了一个人工智能代理，能够：

- 理解上下文并记住对话内容
- 智能使用多种工具
- 以一致格式提供结构化的回答
- 通过上下文处理用户特定信息
- 保持对话状态

想了解如何通过 LangSmith 追踪你的代理，请参阅 LangSmith 文档。
