from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
import os

basic_model = ChatDeepSeek(model="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY"))
advanced_model = ChatDeepSeek(model="deepseek-reasoner", api_key=os.getenv("DEEPSEEK_API_KEY"))

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
    model=basic_model,
    middleware=[dynamic_model_selection]
)

if __name__ == "__main__":
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "Hello"}]}
        # ResponseFormat(
        #     'model_name': 'deepseek-chat'
        # )
        # {"messages": [{"role": "user", "content": "Can you help me with a complex problem?"}] * 11}
        # ResponseFormat(
        #     'model_name': 'deepseek-reasoner'
        # )
    )
    print(result)