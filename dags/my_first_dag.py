from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Função Python para ser usada no PythonOperator
def my_task():
    print("Executando minha primeira tarefa!")

# Definir parâmetros básicos da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Criando a DAG
with DAG(
    'my_first_dag',  # Nome da DAG
    default_args=default_args,
    description='Minha primeira DAG no Airflow',
    schedule_interval=timedelta(days=1),  # Intervalo de agendamento: 1 vez por dia
    catchup=False,  # Desabilita a execução retroativa
) as dag:

    # Define tarefas
    start_task = DummyOperator(task_id='start')

    my_python_task = PythonOperator(
        task_id='my_python_task',
        python_callable=my_task  # Função Python a ser executada
    )

    # Definindo a ordem das tarefas
    start_task >> my_python_task
