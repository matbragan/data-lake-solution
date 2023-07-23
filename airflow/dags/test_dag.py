from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='test_dag',
    start_date=datetime(2023, 7, 16),
    catchup=False
):
    
    pip_list = BashOperator(
        task_id='pip_list',
        bash_command='pip show pymongo'
    )

    pip_list
