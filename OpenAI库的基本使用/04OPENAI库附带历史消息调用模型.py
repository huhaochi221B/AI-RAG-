from openai import OpenAI

# 获取client对象,openAI类对象
client = OpenAI(
    base_url="https://api.deepseek.com",
)
# 调用模型
response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "system", "content": "你是一个AI助理"},
        {"role": "user", "content": "小明有两条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有三只宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几只动物"}
    ],
    stream=True
)
# 处理结果
for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content,
            end=" ",  # 每一段以空格分隔
            flush=True  # 立刻刷新缓冲区
            )
