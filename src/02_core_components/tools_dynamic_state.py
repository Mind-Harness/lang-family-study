from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse, AgentState
from typing import Callable
from typing_extensions import NotRequired
from langchain_deepseek import ChatDeepSeek
import os
from langchain.tools import tool

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

@tool
def public_search(query: str) -> str:
    """Search for public information."""
    return f"[PUBLIC] Search results for: {query}"

@tool
def private_search(query: str) -> str:
    """Search for private information."""
    return f"[PRIVATE] Search results for: {query}"

@tool
def advanced_search(query: str) -> str:
    """Search for advanced information."""
    return f"[ADVANCED] Search results for: {query}"

class CustomState(AgentState):
    authenticated: NotRequired[bool]

@wrap_model_call(state_schema=CustomState)
def state_based_tools(
    request: ModelRequest,
    handler: Callable[[ModelRequest], ModelResponse]
) -> ModelResponse:
    """Filter tools based on conversation State."""
    state = request.state
    is_authenticated = state.get("authenticated", False)
    message_count = len(state["messages"])

    # Only enable sensitive tools after authentication
    if not is_authenticated:
        tools = [t for t in request.tools if t.name.startswith("public_")]
        request = request.override(tools=tools)
    elif message_count < 5:
        tools = [t for t in request.tools if t.name == "private_search"]
        request = request.override(tools=tools)
    else:
        tools = [t for t in request.tools if t.name == "advanced_search"]
        request = request.override(tools=tools)

    return handler(request)

agent = create_agent(
    model=model,
    tools=[public_search, private_search, advanced_search],
    middleware=[state_based_tools]
)

if __name__ == "__main__":
    result = agent.invoke({
        "messages": [{"role": "user", "content": "Search for AI news"}],
        "authenticated": False
    })
    print(result)
    # ResponseFormat(
    #     'name': 'public_search'
    # )

    # result = agent.invoke({
    #     "messages": [{"role": "user", "content": "Search for AI news"}],
    #     "authenticated": True
    # })
    # print(result)
    # ResponseFormat(
    #     'name': 'private_search'
    # )

    # result = agent.invoke({
    #     "messages": [
    #         {"role": "user", "content": "msg1"},
    #         {"role": "user", "content": "msg2"},
    #         {"role": "user", "content": "msg3"},
    #         {"role": "user", "content": "msg4"},
    #         {"role": "user", "content": "Search for AI news"},
    #     ],
    #     "authenticated": True
    # })
    # print(result)
    # ResponseFormat(
    #     'name': 'advanced_search'
    # )
