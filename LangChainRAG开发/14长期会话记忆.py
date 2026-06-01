import os, json
from typing import Sequence

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_deepseek import ChatDeepSeek


# message_to_dict: 将message对象转换为字典
# message_from_dict: 将字典转换为message对象

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id, storage_path):
        self.session_id = session_id    # 会话id
        self.storage_path = storage_path    # 不同会话id的存储文件路径
        self.file_path = os.path.join(self.storage_path, session_id)

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)      # 已有的消息列表
        all_messages.extend(messages)            # 新的和已有的融合成一个list

        # 将数据同步写入本地文件
        # 类对象写入文件 -> 一堆二进制
        # 为了方便, 可以将BaseMessage消息转换为字典(借助JSON模块以json字符串写入文件)
        new_messages = []
        for message in all_messages:
            d = message_to_dict(message)
            new_messages.append(d)
        # 将数据写入文件
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property #@property 装饰器将message方法变成成员属性用
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f)    # 返回值就是:list[字典]
                return messages_from_dict(messages_data)

        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)




model = ChatDeepSeek(model="deepseek-v4-flash")
prompt = PromptTemplate.from_template(
    "你需要根据会话历史回应用户问题。对话历史：{chat_history}，用户提问：{input}，请回答"
)

str_parser = StrOutputParser()

base_chain = prompt | model | str_parser

store = {}
# 实现通过会话 id 获取 InMemoryChatMessageHistory 类对象
def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")


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

    # res = conversion_chain.invoke({"input": "这里有一只猫"}, session_config)
    # print("第1次执行:", res )
    #
    # res = conversion_chain.invoke({"input": "这里有两只狗"}, session_config)
    # print("第2次执行:", res)

    res = conversion_chain.invoke({"input": "这里有多少个宠物"}, session_config)
    print("第3次执行:", res)
