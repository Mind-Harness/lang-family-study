# Basic Agent

Give an LLM tools to interact with the real world.

## Why Agent

LLMs can only chat. They can't check weather, call APIs, or query databases. Agents let models use tools.

## Flow

```
User query → LLM decides to call tool → Execute tool → Return result → LLM responds
```

## Code

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

## Key Points

**Tool Definition**: Regular function + type hints + docstring. LangChain parses automatically.

```python
def get_weather(city: str) -> str:  # type hints
    """Get weather for a given city."""  # docstring → tool description
    return f"It's always sunny in {city}!"
```

**Message Types**:

| Type | Description |
|------|-------------|
| `HumanMessage` | User input |
| `AIMessage` | Model response |
| `ToolMessage` | Tool execution result |

**Format Output**:

```python
for msg in result["messages"]:
    print(f"[{type(msg).__name__}] {msg.content}")
```

## Run

```bash
python src/01_get_started/a_basic_agent.py
```
