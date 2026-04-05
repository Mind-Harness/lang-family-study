# Static Model

Static models are configured once when creating the agent and remain unchanged throughout execution. This is the most common and straightforward approach.

## Using Model Identifier String

To initialize a static model from a model identifier string:

```python
from langchain.agents import create_agent

agent = create_agent("openai:gpt-5", tools=tools)
```

Model identifier strings support automatic inference (e.g., `"gpt-5"` will be inferred as `"openai:gpt-5"`). Refer to the reference to see a full list of model identifier string mappings.

## Using Model Instance

For more control over the model configuration, initialize a model instance directly using the provider package. In this example, we use `ChatOpenAI`. See Chat models for other available chat model classes.

```python
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-5",
    temperature=0.1,
    max_tokens=1000,
    timeout=30
    # ... (other params)
)
agent = create_agent(model, tools=tools)
```

Model instances give you complete control over configuration. Use them when you need to set specific parameters like `temperature`, `max_tokens`, `timeout`, `base_url`, and other provider-specific settings. Refer to the reference to see available params and methods on your model.

## Example with DeepSeek

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
