# dag_factory

Для получения docker-compose для Airflow, необходимо выполнить команду:

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml'
```

Так как в данном репозитории уже находится docker-compose Airflow, то эту команду 
выполнять не нужно.

Для поднятия Airlow необходимо выполнить команду:

```bash
docker-compose up -d 
```

Airflow будет доступен по данному адресу: http://0.0.0.0:8080/

Login: `airflow`
Password: `airflow`

Для корректного отображения зависимостей в DAG необходимо выполнить команды:
```bash
python3 -m venv venv
``` 

```bash
pip install -r requirements.txt
```
