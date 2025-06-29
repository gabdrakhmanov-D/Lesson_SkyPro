import json
import logging

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('./logs/utils.log', encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_dict_transactions(path_to_file: str = './data/operations.json') -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
       Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        logger.info('Старт работы функции')
        with open(path_to_file, "r", encoding='utf-8') as file:
            data = json.load(file)
            logger.info(f'Успешное открытие файла {path_to_file}')
            if type(data) is not list:
                logger.warning(f'Файл {path_to_file} имеет тип отличный от list, возврат пустого списка')
                return []
        logger.info('Успешная обработка файла и возврат содержимого')
        return data
    except Exception as ex:
        logger.error(f'Ошибка в работе функции: {ex}')
        return []
