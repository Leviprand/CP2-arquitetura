# CP2-arquitetura
Este repositório contém o projeto CP2 Arquitetura, que utiliza Docker e Docker Compose para configuração e orquestração de ambientes. O objetivo é criar um fluxo de trabalho que permita a inserção automatizada de dados dos clientes, utilizando as dags que são executadas pelo Apache Airflow.

## Requisitos
* Docker
* Docker Compose

## Como Usar
1. Clone o Repositório:

```
git clone https://github.com/Leviprand/CP2-arquitetura.git
cd CP2-arquitetura
```

2. Construa e inicie os containers usando Docker Compose:

```
docker-compose up --build
```

3. Para parar os containers, utilize:

```
docker-compose down
```

4. Para acessar o Apache Airflow, pelo browser utilize:

```
http://localhost:8080
```

5. Para acessar a plataforma do Apache Airflow, uilize estas credenciais:

__Username (Usuário)__:


```
airflow
```

__Password (Senha)__:

```
airflow
```

6. Para acessar o MongoDB visualmente é necessario que seja utilizando o MongoDB Compass:

- Utilize este link para efetuar o download do Compass:

```
https://www.mongodb.com/products/tools/compass
```
- Quando finalizar a instalação do Compass utilize as credenciais utilizada no docker-compose.yml, caso não tenha alterado utilize  esta string de conexão:

```
mongodb://root:password@127.0.0.1:27017/
```

- Caso tenha alterado segue a estrutura da string de conexão:

```
mongodb://{USUARIO}:{SENHA}@{IP_DA_MAQUINA}:{PORTA}/
```

7. Para iniciar o processo de inserção dos dados no banco de dados, vá ate o Airflow, no localhost, vá em DAGs, e clique na DAG "dag_mongo_insert", clique em "Trigger DAG", localizado na parte superior direita da tela.


## Estrutura do Projeto

Este projeto esta organizado em diretórios que contêm arquivos essenciais para a criação, configuração e execução dos containers Docker.

### Estrutura de Pastas

* __/__: Raiz do projeto onde estará todas as pastas e arquivos necessarios para rodar o projeto;
* __/config__: Esta pasta contêm os arquivos de configurações para rodar o Apache Airflow;
* __/dags__: Esta pasta contêm os arquivos dags em python que seram executados pelo Apache Airflow;
* __/logs__: Esta pasta contêm os logs de quando o Apache Airflow ira rodar;
* __/pligins__: Esta pasta contêm os arquivo ou pastas para os plugins que seram utilizadas no projeto.

