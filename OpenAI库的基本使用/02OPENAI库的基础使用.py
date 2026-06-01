from openai import OpenAI

# 获取client对象,openAI类对象
client = OpenAI(
    base_url="https://api.deepseek.com",
)
# 调用模型
response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "user", "content": "你是一个Python编程专家,并且不说废话简单回答"},
        {"role": "assistant", "content": "我是一个Python编程专家,我会简单回答你的问题"},
        {"role": "user", "content": "输出1-10的数字,使用Python代码"}
    ]

)
# 处理结果
print(response.choices[0].message.content)
