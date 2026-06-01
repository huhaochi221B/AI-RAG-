from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender}，你帮我取个名字，简单回答"
)
model = Tongyi(model="qwen-max")
# 调用format方法
# prompt_text = prompt_template.format(lastname="胡",gender="男孩")
# print(prompt_text)

# res = model.invoke(input=prompt_text)
# print(res)

# 构建执行链条的方法

chain = prompt_template | model

res = chain.invoke(input={"lastname": "胡", "gender": "女儿"})
print(res)

