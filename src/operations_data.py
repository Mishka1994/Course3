import json
import os

PATH = os.path.join('fixture', 'operations_data.py')


def get_operations_from_json(PATH):
    """
    Функция считывает данные из JSON-файла и возвращает список словарей, которые
    содержат информацию об операциях.
    :param path: Путь к файлу.
    :return: Список словарей.
    """
    with open(PATH) as file:
        operations = json.load(file)
        return operations


def choose_only_executed_operation(operations):
    """
    Функция пересоздает список, внося только выполненные операции.
    :param operations: Список всех операций
    :return: Список с выполненными операциями.
    """
    operations = [elem for elem in operations if 'state' in elem and elem['state'] == 'EXECUTED']
    return operations


def sorted_operations_by_date(operations):
    return sorted(operations, key=lambda operations: operations['date'], reverse=True)
