import json


def replace_template_variables(template_dag: str = None, dict_variables: dict = None) -> str:
    """
    Функция, которая итерируется по всем ключам ключа основного словаря берет оттуда значение и подставляет в шаблон.

    Пример:
    ```json
    {
      "test":
      {
        "OWNER": "airflow",
        "DAG_ID": "test",
        "PK": "id"
        ...
      }
    }
    ```
    На вход поступает значения по ключу `test` и функция итерируется по ключам: `OWNER`, `DAG_ID`, `PK`, ...
    Берет значения по ключу и заменяет шаблон в указанном `template_dag`.

    Соответственно, по всем ключам, которые есть в словаре DAG будет произведена замена по шаблону.

    @param template_dag: Шаблон DAG; default 'None'.
    @param dict_variables: Словарь со значениями, которые необходимо поменять в шаблоне; default 'None'.
    @return: Измененный шаблон на основании значений по ключам.
    """
    for variables_ in dict_variables:
        template_dag = template_dag.replace(f'$${variables_}', f'{dict_variables[variables_]}')

    return template_dag


def dag_factory(type_dag: str = None) -> None:
    """
    Функция, которая генерирует DAG на основании выбранного `type_dag` и выбранных config на основании `type_dag`.

    Пример: Если указан `print_something` в `type_dag`, то функция для генерации DAG будет использовать config:
    "config_json_print_something.json" и сохранит сгенерированные DAG в папку:
    //dags/json_dags/print_something/<print_something_dag_name.py>

    @param type_dag: Указывается тип DAG для генерации print_something|etc; default 'None'.
    @return: Ничего не возвращает, а сохраняет сгенерированный DAG по определенному пути.
    """
    with open(f'dag_config_json_{type_dag}/config_{type_dag}_dag.json') as j:
        json_config = j.read()
        json_config = json.loads(json_config)

    with open(f'templates_dags/{type_dag}.txt', mode='r') as f:
        template = f.read()

    for dag in json_config:
        modified_template = replace_template_variables(template_dag=template, dict_variables=json_config[dag])
        with open(f'../dags/json_dags/{type_dag}/{dag}.py', mode='w') as dag_pyfile:
            dag_pyfile.write(modified_template)


dag_factory(type_dag='print_something')
