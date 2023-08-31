import json
import os

from dotenv import load_dotenv

load_dotenv()

database_hostname = os.getenv("DATABASE_HOSTNAME")

json_template = {
    "name": "sales-connector",
    "config": {
        "connector.class": "io.debezium.connector.mysql.MySqlConnector",
        "tasks.max": "1",
        "database.hostname": "",
        "database.port": "3306",
        "database.user": "newuser",
        "database.password": "Newuser4%",
        "database.server.id": "184054",
        "topic.prefix": "mysqlsales",
        "database.include.list": "lake_solution",
        "schema.history.internal.kafka.bootstrap.servers": "kafka:9092",
        "schema.history.internal.kafka.topic": "schemahistory.mysqlsales",
        "include.schema.changes": "true"
    }
}

json_template["config"]["database.hostname"] = database_hostname

mysql_connector = json.dumps(json_template, indent=4)

with open('mysql_connector.json', 'w') as json_file:
    json_file.write(mysql_connector)
