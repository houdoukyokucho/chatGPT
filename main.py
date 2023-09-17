import logging
import os
import sys

from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.environ.get("OPEN_API_KEY")

from llama_index import (
    GPTVectorStoreIndex,
    StorageContext,
    download_loader,
    load_index_from_storage
)

# ログレベルの設定
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

# 質問を受け付ける。
question = input("Question: ")

# インデックスを作成する。
SimpleCSVReader = download_loader("SimpleCSVReader")
documents =  SimpleCSVReader().load_data(file="data.csv")
index = GPTVectorStoreIndex.from_documents(documents)

# インデックスを保存する。
index.storage_context.persist()

# インデックスを読み込む。
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# 回答をする。
query_engine = index.as_query_engine()
print(query_engine.query(question))
