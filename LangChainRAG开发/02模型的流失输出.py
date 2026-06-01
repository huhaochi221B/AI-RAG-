from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

# 调用invoke向模型提问

res =model.stream(input="你是谁？")

for chunk in res:
    print(chunk,end="", flush=True)