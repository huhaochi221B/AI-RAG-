import os

from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime
import config_data as config
import hashlib
from langchain_chroma import Chroma

def check_md5(md5_str: str):
    """检查传入的MD5字符是否已经被传入过了
        return False表示md5未处理过  True表示md5已处理过
    """
    if not os.path.exists(config.md5_path):
        # if 进入表示文件不存在
        open(config.md5_path, 'w', encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path, 'r', encoding="utf-8").readlines():
            line = line.strip()     # 处理字符串前后的空格和回车
            if line == md5_str:
                return True

        return False


def save_md5(md5_str: str):
    """保存传入的MD5字符"""
    with open(config.md5_path, "a", encoding="utf-8") as f:
        f.write(md5_str + '\n')

def get_string_md5(input_str: str, encoding="utf-8"):
    """获取传入的字符串的MD5"""
    # 将字符串转换为byte字节数组
    str_bytes = input_str.encode(encoding= encoding)

    # 创建MD5对象
    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)
    return md5_obj.hexdigest()


class KnowledgeBaseService(object):
    def __init__(self):
        # 创建保存向量数据库的目录,已存在则跳过
        os.makedirs(config.persist_directory, exist_ok=True)

        self.chroma = Chroma(
            collection_name=config.collection_name,     # 表名
            embedding_function=DashScopeEmbeddings(model="text-embedding-v1"),
            persist_directory=config.persist_directory  # 指定向量数据库的保存目录
        )
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,   # 块大小
            chunk_overlap=config.chunk_overlap, # 块重叠
            separators=config.separators,   # 文本分隔符
            length_function=len             # 获取文本长度的函数
        )

    def upload_by_str(self, data: str, filename):
        """将传入的字符串进行向量化,存入向量数据库中"""
        md5_hax = get_string_md5(data)

        if check_md5(md5_hax):
            return "[跳过]数据已处理过"


        if len(data) > config.max_splite_char_number:
            knowledge_chunks: list[str] = self.spliter.split_text(data)

        else:
            knowledge_chunks = [data]

        metadata = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "hhc",
        }

        self.chroma.add_texts(
            knowledge_chunks,
            metadatas=[metadata for _ in knowledge_chunks]
        )

        save_md5(md5_hax)

        return "[成功]数据处理完成"





if __name__ == '__main__':
    service = KnowledgeBaseService()
    r = service.upload_by_str("周杰伦", "textfile")
    print(r)




