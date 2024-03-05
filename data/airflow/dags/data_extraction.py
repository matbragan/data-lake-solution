from datetime import datetime

from airflow.decorators import task
from airflow.operators.dummy import DummyOperator

from airflow import DAG

with DAG(
    dag_id='extraction_data',
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
        from utils.s3_write import s3_write

        data = mongo_connection('lake_solution', 'users')
        s3_write(data, 'users')

    @task(task_id='mysql_extraction')
    def mysql_extraction() -> None:
        from extraction.mysql_extraction import mysql_connection
        from utils.s3_write import s3_write

        data = mysql_connection('lake_solution', 'sales')
        s3_write(data, 'sales')

    start_task >> [mongo_extraction(), mysql_extraction()] >> end_task
