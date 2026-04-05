# 静态模型

静态模型在创建代理时仅配置一次，执行过程中保持不变。这是最常见且最直接的方法。

## 使用模型标识符字符串

从一个模型标识符字符串初始化静态模型：

```python
from langchain.agents import create_agent

agent = create_agent("openai:gpt-5", tools=tools)
```

模型标识符字符串支持自动推理（例如，`"gpt-5"` 会被推断为 `"openai:gpt-5"`）。请参阅参考文献查看完整的模型标识符字符串映射列表。

## 使用模型实例

为了更好地控制模型配置，可以直接使用提供者包初始化模型实例。在这个例子中，我们使用 `ChatOpenAI`。参见聊天模型，了解其他可用的聊天模型类别。

```python
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-5",
    temperature=0.1,
    max_tokens=1000,
    timeout=30
    # ... (其他参数)
)
agent = create_agent(model, tools=tools)
```

模型实例让你完全控制配置。当你需要设置具体参数，比如 `temperature`、`max_tokens`、`timeout`、`base_url` 以及其他提供者专属设置时，就用它们。请参阅参考文献，查看模型可用的参数和方法。

## DeepSeek 示例

```python
import os
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek

api_key = os.getenv("DEEPSEEK_API_KEY")

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=api_key,
)

agent = create_agent(model)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "Hello, how are you?"}]}
)
print(response)
```
