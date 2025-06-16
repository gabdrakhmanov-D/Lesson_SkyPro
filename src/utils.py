import json


def get_dict_transactions(path_to_file: str) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
       Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path_to_file, "r", encoding='utf-8') as file:
            data = json.load(file)
            if type(data) != list:
                return []
        return data
    except Exception:
        return []
