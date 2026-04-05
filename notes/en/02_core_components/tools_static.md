# Static Tools

Static tools are defined when creating the agent and remain unchanged throughout execution. This is the most common and straightforward approach.

## Basic Usage

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

## Tool Properties

The `@tool` decorator can be used to customize tool names, descriptions, argument schemas, and other properties.

## Important Note

If an empty tool list is provided, the agent will consist of a single LLM node without tool-calling capabilities.
