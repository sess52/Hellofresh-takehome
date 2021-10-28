import airflow
from airflow import DAG

from airflow.operators.python import PythonOperator,BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import retreive_recipies 
import send_csv_to_s3
from sys

def _retreive_recipes():
	retreive_recipies.main()

def _send_csv_to_s3():
	send_csv_to_s3.main()

with DAG('my_dag',start_date = datetime(2021,1,1),schedule_interval = '@weekly',catchup=False) as dag:
	retreive_recipes = PythonOperator(task_id = 'retreive_recipes',python_callable = _retreive_recipes)
	send_csv_to_s3 = PythonOperator(task_id = 'send_csv_to_s3',python_callable = _send_csv_to_s3)
	retreive_recipes >> send_files_to_s3