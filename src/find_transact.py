import re
from src.utils import get_dict_transactions

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='../logs/find_transact.log',
                    filemode='w',
                    encoding='utf-8')
get_dict_logger = logging.getLogger('get_req_dict')


def get_required_dictionary(list_of_dict: list[dict], pattern: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка"""

    if type(pattern) is not str:
        get_dict_logger.error(f'Искомое значение не строка! Возврат пустого списка')
        return []
    elif list_of_dict:
        get_dict_logger.info(f'Старт работы функции. Искомое значение: {pattern}')
        pattern = pattern.lower()
        search_string = re.compile(pattern)
        matches = []
        get_dict_logger.info(f'Перебор словарей из списка транзакций')
        for dict_transact in list_of_dict:
            try:
                if re.search(search_string, dict_transact.get("description").lower()):
                    matches.append(dict_transact)
            except Exception as ex:
                get_dict_logger.error(f'Ошибка в ключе поиска: {ex}')
                continue
        get_dict_logger.info(f'Поиск прошел успешно. Возврат списка значений')
        return matches
    get_dict_logger.error(f'Получен пустой список. Возврат пустого списка')
    return []

# Напишите функцию, которая будет принимать список словарей с данными о
# банковских операциях и список категорий операций, а возвращать словарь,
# в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.

def category_counter(list_of_dict: list[dict], list_of_category: list) -> dict:
    pass

if __name__ == '__main__':

    a= get_required_dictionary(get_dict_transactions('../data/operations.json'), 'переводa' )
    print(len(a))
    # print(a)
    for i in a:
        print(i)