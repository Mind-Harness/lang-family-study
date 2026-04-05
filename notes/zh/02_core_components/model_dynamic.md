# 动态模型

动态模型在运行时根据当前状态和上下文进行选择。这支持了复杂的路由逻辑和成本优化。

## 基本用法

要使用动态模型，使用 `@wrap_model_call` 装饰器创建中间件，在请求中修改模型：

```python
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse

basic_model = ChatOpenAI(model="gpt-4.1-mini")
advanced_model = ChatOpenAI(model="gpt-4.1")

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
        model = advanced_model
    else:
        model = basic_model

    return handler(request.override(model=model))

agent = create_agent(
    model=basic_model,  # Default model
    tools=tools,
    middleware=[dynamic_model_selection]
)
```

## DeepSeek 示例

```python
from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
import os

basic_model = ChatDeepSeek(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)
advanced_model = ChatDeepSeek(
    model="deepseek-reasoner",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        model = advanced_model
    else:
        model = basic_model

    return handler(request.override(model=model))

agent = create_agent(
    model=basic_model,
    middleware=[dynamic_model_selection]
)
```

## 注意事项

使用结构化输出时不支持预绑模型（`bind_tools` 已调用的模型）。如果你需要动态选择模型并带结构化输出，确保传递给中间件的模型没有预绑。

## 参考资料

- 关于模型配置的详细信息，请参见 [Models](https://docs.langchain.com/docs/models)。
- 关于动态模型选择模式，请参见 [中间件中的动态模型](https://docs.langchain.com/docs/middleware/dynamic-model)。
