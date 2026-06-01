from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model="qwen3-max", streaming=True)

messages = [
    ("system", "你是李白"),
    ("human", "给我写一首唐诗"),
    ("ai", """
    《月下独酌·其二》

    金樽对月饮长空，
    万里江天一色同。
    醉踏青崖云作伴，
    笑邀白鹿访仙翁。
    星垂大野浮银汉，
    浪卷千峰入玉虹。
    莫问明朝何处去，
    且将肝胆照苍穹！
    """ ),
    ("human", "就按你上一个回复的格式，输出诗句")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content, end="", flush=True)
