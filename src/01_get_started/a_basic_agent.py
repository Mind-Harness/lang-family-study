import os
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek

api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("Please set environment variable DEEPSEEK_API_KEY")

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

if __name__ == "__main__":
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )

    print("=" * 60)
    for msg in result["messages"]:
        msg_type = type(msg).__name__
        print(f"[{msg_type}]")
        if hasattr(msg, "content") and msg.content:
            print(f"  Content: {msg.content}")
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            print(f"  Tool Calls: {msg.tool_calls}")
