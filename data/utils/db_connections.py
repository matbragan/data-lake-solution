import os

import mysql.connector
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def mongo_connection(
    database: str,
    table: str
) -> list:
    client = MongoClient(os.getenv('MONGO_CONN'))
    database = client[database]
    collection = database[table]

    data = collection.find({}, {'_id': 0})
    data = list(data)

    return data


def mysql_connection(
    database: str,
    table: str
) -> list:
    cnx = mysql.connector.connect(
        host=os.getenv('MYSQL_CONN_HOST'),
        user=os.getenv('MYSQL_CONN_USER'),
        password=os.getenv('MYSQL_CONN_PASSWORD'),
        database=database
    )

    cursor = cnx.cursor()

    query = f'select * from {table};'

    cursor.execute(query)
    data = cursor.fetchall()

    return data
