from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'spark_example',
    default_args=default_args,
    description='A simple DAG to run PySpark job',
    schedule_interval='@once',
)

spark_task = BashOperator(
    task_id='spark_task',
    bash_command='spark-submit --master local[*] /app/pyspark_transformation.py',
    dag=dag,
)

spark_task
