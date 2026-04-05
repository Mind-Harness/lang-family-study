import os
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"

agent = create_agent(model, tools=[search, get_weather])

if __name__ == "__main__":
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather like in San Francisco?"}]}
    )
    # ResponseFormat(
    #     tool_calls=[{'name': 'get_weather', 'args': {'location': 'San Francisco'}, 'id': 'call_00_VOdN4EeEAbi04wT0tmRj84cs', 'type': 'tool_call'}]
    # )

    # result = agent.invoke(
    #     {"messages": [{"role": "user", "content": "Search for the latest news on AI advancements."}]}
    # )
    # ResponseFormat(
    #     tool_calls=[{'name': 'search', 'args': {'query': 'latest news AI advancements 2024'}, 'id': 'call_00_rlUagh2E8waf96nWJg7r8lT1', 'type': 'tool_call'}]
    # )

    print(result)