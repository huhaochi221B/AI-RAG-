from ollama import embeddings

md5_path = "./md5.text"

# Chroma
collection_name = "rag"
persist_directory = "./chroma_db"


# Splitter
chunk_size = 100
chunk_overlap = 100
separators = ["\n\n", "\n", " ", "", ".", "!", "?", "，", "。", "？", "！", ";"]
max_splite_char_number = 1000   # 单个文档最大字符数


similarity_threshold = 1    # 检索返回匹配文档的文档数量


embeddings_model_name = "text-embedding-v1"
chat_model_name = "deepseek-v4-flash"


session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }