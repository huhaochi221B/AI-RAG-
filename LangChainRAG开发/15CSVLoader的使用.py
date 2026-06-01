from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": ",",    # 指定分隔符
        "quotechar": '"',    # 指定带有分隔符文本的引号包围是单引号还是双引号
        # 如果数据有表头,就不要下方代码
        "fieldnames": ['a','b','c','d']
    },
    encoding="utf-8"
)

documents = loader.load()

print(documents)

# 懒加载
for document in loader.lazy_load():
    print(document)