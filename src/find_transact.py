import re
from collections import Counter

from src.utils import get_dict_transactions

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='../logs/find_transact.log',
                    filemode='w',
                    encoding='utf-8')
get_dict_logger = logging.getLogger('get_req_dict')
cat_count_logger = logging.getLogger('category_counter')


def get_required_dictionary(list_of_dict: list[dict], pattern: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка"""

    if type(pattern) is not str:
        get_dict_logger.error('Искомое значение не строка! Возврат пустого списка')
        return []
    elif list_of_dict:
        get_dict_logger.info(f'Старт работы функции. Искомое значение: {pattern}')
        pattern = pattern.lower()
        search_string = re.compile(pattern)
        matches = []
        get_dict_logger.info('Перебор словарей из списка транзакций')
        for dict_transact in list_of_dict:
            try:
                if re.search(search_string, dict_transact.get("description").lower()):
                    matches.append(dict_transact)
            except Exception as ex:
                get_dict_logger.error(f'Ошибка в ключе поиска: {ex}')
                continue
        get_dict_logger.info('Поиск прошел успешно. Возврат списка значений')
        return matches
    get_dict_logger.error('Получен пустой список. Возврат пустого списка')
    return []

# Напишите функцию, которая будет принимать список словарей с данными о
# банковских операциях и список категорий операций, а возвращать словарь,
# в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.

def category_counter(list_of_dict: list[dict], list_of_category: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций.
       Возвращает словарь, в котором ключи — это названия категорий,
       а значения — это количество операций в каждой категории."""

    if type(list_of_category) is not list:
        cat_count_logger.error('Параметр "Список категорий операций" не является списком!')
        return {}
    elif list_of_dict:
        cat_count_logger.info('Старт работы функции. Переборка и сравнений значений списка категорий')
        count_list = []
        for dict_transact in list_of_dict:
            try:
                if dict_transact.get("description") in list_of_category:
                    count_list.append(dict_transact.get("description"))
            except Exception as ex:
                get_dict_logger.error(f'Ошибка в ключе поиска: {ex}')
                continue
        counted = Counter(count_list)
        cat_count_logger.info('Подсчет прошел успешно. Возврат словаря значений')
        return counted
    cat_count_logger.error('Получен пустой список. Возврат пустого словаря')
    return {}

if __name__ == '__main__':

    a= category_counter(get_dict_transactions('../data/operations.json')[:50], ["Перевод организации", "Перевод с карты на счет"] )
    # print(len(a))
    print(a)
    # for i in a:
    #     print(i)