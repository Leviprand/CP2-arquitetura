from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pymongo
import csv
import os

CSV_FILEPATH = os.path.join('/opt/airflow/dags', 'Checkpoint5e6profTiago.csv')  # Atualize este caminho conforme necessário
MONGO_CONN_ID = 'mongoid'  # ID da conexão MongoDB configurada no Airflow


def insert_csv_to_mongo(csv_filepath, mongo_conn_id):
    from airflow.hooks.base import BaseHook
    connection = BaseHook.get_connection(mongo_conn_id)

    client = pymongo.MongoClient("mongodb://root:password@192.168.0.170:27017/")
    db = client[connection.schema]
    collection = db['airflow']

    with open(csv_filepath, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            query = {'id': row['id']}  # Critério de busca (verifica se o email já existe)
            update = {"$set": row}  # Define os campos que serão atualizados
            # Realiza a inserção ou atualização (upsert=True)
            collection.update_one(query, update, upsert=True)

# Definir os argumentos padrão da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'dag_mongo_insert',
    default_args=default_args,
    description='DAG para inserir dados do CSV no MongoDB',
    schedule_interval=timedelta(days=1),  # Executar diariamente
    catchup=False,
) as dag:

    # Tarefa Python para inserir o CSV no MongoDB
    insert_csv_task = PythonOperator(
        task_id='insert_csv_to_mongo',
        python_callable=insert_csv_to_mongo,
        op_kwargs={
            'csv_filepath': CSV_FILEPATH,
            'mongo_conn_id': MONGO_CONN_ID,
        },
    )

    # Ordem de execução das tarefas
    insert_csv_task
