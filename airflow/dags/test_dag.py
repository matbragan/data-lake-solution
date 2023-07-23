from datetime import datetime

from airflow.operators.bash import BashOperator

from airflow import DAG

with DAG(
    dag_id='test_dag',
    start_date=datetime(2023, 7, 16),
    catchup=False
):

    pip_list = BashOperator(
        task_id='pip_list',
        bash_command='pip show pymongo'
    )

    hostname = BashOperator(
        task_id='hostname',
        bash_command='hostname -I'
    )

    [pip_list, hostname]
