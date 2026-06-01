from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
from langchain_core.tools import tool

@tool(description="获取股票价格")
def get_price(name: str) -> str:
    return f"股票{name}价格为20元"

@tool(description="查询股票信息")
def get_info(name: str) -> str:
    return f"{name}是一家A股上市的公司,专注于教育"

agent = create_agent(
    model=ChatDeepSeek(model="deepseek-v4-flash"),
    tools=[get_info, get_price],
    system_prompt="""
    你是一个股票查询助手,你需要根据用户的指令进行股票查询
    """,
)

for chunk in agent.stream(
    {"messages":[{"role": "user", "content": "传智教育股价多少?并介绍一下"}]},
    stream_mode="values"
):
    latest_message = chunk['messages'][-1]
    print(latest_message)