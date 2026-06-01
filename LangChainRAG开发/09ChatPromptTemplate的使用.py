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

#StringPrompt Value
prompt_text = chat_prompt_template.invoke({"history": history_data}).to_string()
print(prompt_text)

model = ChatDeepSeek(model="deepseek-v4-flash")
res = model.invoke(prompt_text)
print(res.content)

