import json

d = {
    "name": "周杰伦",
    "age": 18,
    "gender": "男"
}

s = json.dumps(d, ensure_ascii=False)
print(s)

l = [
    {
        "name": "周杰伦",
        "age": 18,
        "gender": "男"
    },
    {
        "name": "王力宏",
        "age": 19,
        "gender": "男"
    },
    {
        "name": "林志玲",
        "age": 20,
        "gender": "女"
    }

]

# json.dumps()     Python → JSON 字符串      序列化（写
print(json.dumps(l, ensure_ascii=False))



# json.loads()    JSON 字符串 → Python       反序列化（读）
json_str = '{"name": "周杰伦", "age": 18,"gender": "男"}'
json_array_str = '[{"name": "周杰伦", "age": 18, "gender": "男"}, {"name": "王力宏", "age": 19, "gender": "男"}, {"name": "林志玲", "age": 20, "gender": "女"}]'
res_dict = json.loads(json_str)   # 反序列化为 字典
print(res_dict, type(res_dict))

res_list = json.loads(json_array_str)  # 反序列化为 列表
print(res_list, type(res_list))