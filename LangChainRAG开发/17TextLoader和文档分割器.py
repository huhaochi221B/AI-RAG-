from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("./data/我的学习笔记.txt", encoding="utf-8")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,     # 片段长度
    chunk_overlap=50,   # 片段重叠长度
    # 文本自然段落分隔的依据符号
    separators=["\n\n", "\n", " ", "", "", "。", "？", "！", "，", "、"],
    length_function=len
)

split_docs = splitter.split_documents(docs)
print(len(split_docs))

for doc in split_docs:
    print(doc)
    print("=" * 80)