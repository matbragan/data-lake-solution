from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy import DummyOperator

with DAG(
    dag_id='extraction_date',
    start_date=datetime(2023, 7, 15),
    schedule='@daily',
    catchup=False,
    tags=['extraction']
):

    start_task = DummyOperator(task_id='start_task')

    end_task = DummyOperator(task_id='end_task')

    @task(task_id='mongo_extraction')
    def mongo_extraction() -> None:
        from extraction.mongo_extraction import mongo_connection
        from utils.write_s3 import write_s3

        data = mongo_connection('hotmart', 'users')
        write_s3(data, 'users')

    @task(task_id='mysql_extraction')
    def mysql_extraction() -> None:
        from extraction.mysql_extraction import mysql_connection
        from utils.write_s3 import write_s3

        data = mysql_connection('hotmart', 'sales')
        write_s3(data, 'sales')

    start_task >> [mongo_extraction(), mysql_extraction()] >> end_task
