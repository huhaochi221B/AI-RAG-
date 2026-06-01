from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_deepseek import ChatDeepSeek

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人,可以作诗"),
        MessagesPlaceholder("history"),
        ("human","请再来一首唐诗")
    ]
)

history_data = [
    ("human","你来写一首唐诗"),
    ("system", "床前明月光,疑是地上霜.举头望明月,低头思故乡.")
]


model = ChatDeepSeek(model="deepseek-v4-flash")

# 组成链 要求每一个组件都是Runnable接口的子类
chain = chat_prompt_template | model

# res = chain.invoke({"history": history_data})
# print(res.content)

for chunk in chain.stream({"history": history_data}):
    print(chunk.content, end="", flush=True)

