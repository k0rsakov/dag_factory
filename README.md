# Генерация DAG в Apache Airflow

Статья на [habr](https://habr.com/ru/articles/722688/)

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

___

Если вам необходима консультация/менторство/мок-собеседование и другие вопросы по дата-инженерии, то вы можете
обращаться ко мне. Все контакты указаны по
[ссылке](https://www.notion.so/korsak0v/Data-Engineer-185c62fdf79345eb9da9928356884ea0).
