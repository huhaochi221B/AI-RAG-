from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_deepseek import ChatDeepSeek

model = ChatDeepSeek(model="deepseek-v4-flash")
prompt = PromptTemplate.from_template(
    "你需要根据会话历史回应用户问题。对话历史：{chat_history}，用户提问：{input}，请回答"
)

str_parser = StrOutputParser()

base_chain = prompt | model | str_parser

store = {}
# 实现通过会话 id 获取 InMemoryChatMessageHistory 类对象
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]

# 创建一个新的链,对原有的链增强功能:自动附加历史消息

conversion_chain = RunnableWithMessageHistory(
    base_chain,     # 原有链
    get_history,    # 通过会话id获取历史消息
    input_messages_key="input",     #表示用户输入在模板中的占位符
    history_messages_key="chat_history"
)

if __name__ == '__main__':
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }

    res = conversion_chain.invoke({"input": "这里有一只猫"}, session_config)
    print("第1次执行:", res )

    res = conversion_chain.invoke({"input": "这里有两只狗"}, session_config)
    print("第2次执行:", res)

    res = conversion_chain.invoke({"input": "这里有多少个宠物"}, session_config)
    print("第3次执行:", res)
