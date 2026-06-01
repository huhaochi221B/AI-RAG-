from langchain_core.output_parsers import JsonOutputParser
from langchain_deepseek.chat_models import ChatDeepSeek
from langchain_core.prompts import PromptTemplate

json_paser = JsonOutputParser()

model = ChatDeepSeek(model="deepseek-v4-flash")

first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请帮忙起名字，并封装为 JSON 格式。要求key是name,value是你你起的名字"
)
second_prompt = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义。"
)

chain = first_prompt | model | json_paser | second_prompt | model

for chunk in chain.stream({"lastname": "王", "gender": "男"}):
    print(chunk.content, end="", flush=True)
