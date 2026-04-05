import os
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek

api_key = os.getenv("DEEPSEEK_API_KEY", "your-deepseek-api-key")

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=api_key,
)

agent = create_agent(model)

if __name__ == "__main__":
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Hello, how are you?"}]}
    )
    print(response)
