from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
from langchain_core.tools import tool


@tool(description="查询天气")
def get_weather() -> str:
    return "晴天"

agent = create_agent(
    model=ChatDeepSeek(model="deepseek-v4-flash"),
    tools=[get_weather],
    system_prompt="你是一个聊天助手,可以回答用户问题"
)



res = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "明天太原天气如何?"}
        ]
    }
)

for msg in res["messages"]:
    print(type(msg).__name__, msg.content)