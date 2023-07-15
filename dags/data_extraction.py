import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.decorators import task

sys.path.insert(0, os.path.abspath('.'))

with DAG(
    dag_id='extraction_date',
    start_date=datetime(2023, 7, 15),
    schedule='@daily',
    catchup=False,
    tags=['extraction']
):

    @task(task_id='mongo_extraction')
    def mongo_extraction() -> None:
        from extraction.mongo_extraction import mongo_connection
        from extraction.utils.write_s3 import write_s3

        data = mongo_connection('hotmart', 'users')
        write_s3(data, 'users')

    mongo_extraction()
