from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.runnables import  RunnableLambda
from langchain_deepseek.chat_models import ChatDeepSeek
from langchain_core.prompts import PromptTemplate

json_paser = JsonOutputParser()

model = ChatDeepSeek(model="deepseek-v4-flash")

str_parser = StrOutputParser()

first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请帮忙起名字，并封装为 JSON 格式。要求仅输出姓名,不要其他内容"
)
second_prompt = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义。"
)

my_func = RunnableLambda(lambda ai_msg : {"name": ai_msg.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "王", "gender": "男"}):
    print(chunk, end="", flush=True)
 