FROM apache/airflow:2.10.2-python3.9

RUN apt-get update \ 
    && apt-get install -y  \
        gcc \
        python3-dev \
        build-essential \
        libssl-dev \
        libffi-dev \
    && apt-get clean

# # Voltar ao usuário 'airflow' para instalação dos pacotes Python (PyPI)
# USER airflow

# # Instalar pymongo como pacote adicional
# RUN pip install --user pymongo

# # Definir variáveis de ambiente do Airflow
# ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

# # Expor a porta padrão do Airflow
# EXPOSE 8080

# # Copiar os DAGs para o diretório correto do Airflow
# COPY dags/ /opt/airflow/dags/

# # Comando padrão para iniciar o Airflow webserver
# CMD ["airflow", "webserver"]
