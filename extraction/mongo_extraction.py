import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def mongo_connection(database: str, collection: str) -> list:
    client = MongoClient(os.getenv('MONGO_CONN'))
    database = client[database]
    collection = database[collection]

    data = collection.find({}, {'_id': 0})

    return list(data)
