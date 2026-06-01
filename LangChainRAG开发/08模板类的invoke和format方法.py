from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("我的邻居是:{name}, 最喜欢:{hobby}")

res = template.format(name="狗蛋", hobby="看电影")
print(res,type(res))

res = template.invoke({"name": "乔奕磊", "hobby": "旅游"})
print(res,type(res))