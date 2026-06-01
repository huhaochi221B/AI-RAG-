from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="./data/咏鹅.pdf",
    mode="single",   # single 只返回一个Document对象
    password="123456"
)
i = 0
for doc in loader.lazy_load():
    i += 1
    print(doc)
    print("=" * 80)