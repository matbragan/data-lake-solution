import os

from dotenv import load_dotenv
from pymongo import MongoClient

from utils.s3_write import s3_write

load_dotenv()


def mongo_connection(database: str, collection: str) -> list:
    client = MongoClient(os.getenv('MONGO_CONN'))
    database = client[database]
    collection = database[collection]

    data = collection.find({}, {'_id': 0})

    return list(data)


if __name__ == '__main__':
    data = mongo_connection('lake_solution', 'users')
    s3_write(data, 'users')
