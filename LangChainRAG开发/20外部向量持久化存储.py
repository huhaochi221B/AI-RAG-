from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

# Chroma 轻量级向量数据库
# 下载LangChain-chroma chromaDB


vector_store = Chroma(
    collection_name="test",     # 表名
    embedding_function=DashScopeEmbeddings(),   # 嵌入模型
    persist_directory="./chroma_db"     # 文件夹
)

# loader = CSVLoader(
#     file_path="./data/info.csv",
#     encoding="utf-8",
#     source_column="source",     # 指定本条数据来源是哪路
# )
#
# documents = loader.load()
#
# print(documents[1])
#
# # 向量存储的新增,删除,检索
#
# vector_store.add_documents(
#     documents=documents,    # 添加的文档, 类型为list[Document]
#     ids=["id" + str(i) for i in range(1, len(documents) + 1)]   # 给添加的文档提供id
# )
#
# vector_store.delete(["id1", "id2"])

result = vector_store.similarity_search(
    "Python是不是简单易学",
    3,
    filter={"source": "黑马程序员"}
)

print(result)