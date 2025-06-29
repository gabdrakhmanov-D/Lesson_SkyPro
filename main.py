import logging

from src.file_reader import csv_file_reader, excel_file_reader
from src.find_transact import get_required_dictionary, category_counter
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_dict_transactions
from src.widget import get_date, mask_account_card

logger_file = logging.getLogger('select_file')
logger_filter = logging.getLogger('select_filter')
logger_sort_by_data = logging.getLogger('sort_by_data')
logger_rub_transact = logging.getLogger('rub_transact')
logger_by_pattern = logging.getLogger('filter_by_pattern')
logger_main = logging.getLogger('main')

def select_file() -> list:
    logger_file.info('Старт работы функции')
    select_file = False
    while select_file not in ['1', '2', '3']:
        select_file = str(input(
            'Привет! Добро пожаловать в программу работы'
            'с банковскими транзакциями.Выберите необходимый пункт меню:\n'
            '1. Получить информацию о транзакциях из JSON-файла\n'
            '2. Получить информацию о транзакциях из CSV-файла\n'
            '3. Получить информацию о транзакциях из XLSX-файла\n'))

        if select_file == '1':
            logger_file.info('Выбран пункт 1, запрос отправлен get_dict_transactions')
            print('Для обработки выбран JSON-файл.')
            list_transactions = get_dict_transactions()
        elif select_file == '2':
            logger_file.info('Выбран пункт 2, запрос отправлен csv_file_reader')
            print('Для обработки выбран CSV-файл.')
            list_transactions = csv_file_reader()
        elif select_file == '3':
            logger_file.info('Выбран пункт 3, запрос отправлен в excel_file_reader')
            print('Для обработки выбран XLSX-файл.')
            list_transactions = excel_file_reader()
        else:
            logger_file.warning('Выбран неверный пункт в меню')
            print('Выбран неверный пункт в меню')
    logger_file.info('Возврат списка транзакций')
    return list_transactions


def select_filter() -> list:
    logger_filter.info('Старт работы функции')
    list_transact = select_file()
    if not list_transact:
        logger_filter.error('Получен пустой список, возврат пустого списка!')
    else:
        filter_transact = None
        while filter_transact not in ['EXECUTED', 'CANCELED', 'PENDING']:
            filter_transact = input('\nВведите статус, по которому необходимо выполнить фильтрацию.'
                                  'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n').upper()
            logger_filter.info(f'Пользователь ввел: {filter_transact}')
            if filter_transact in ['EXECUTED', 'CANCELED', 'PENDING']:
                logger_filter.info('Запрос списка транзакций у функции filter_by_state')
                list_transactions = filter_by_state(list_transact, filter_transact)
            else:
                logger_filter.warning(f'Пользователь ввел некорректный фильтр: {filter_transact}')
                print(f'Статус операции {filter_transact} недоступен.')
        logger_filter.info('Возврат списка транзакций')
        return list_transactions
    return []


def sort_by_data():
    list_transact = select_filter()
    logger_sort_by_data.info('Старт работы функции')
    if not list_transact:
        logger_sort_by_data.error('Получен пустой список, возврат пустого списка!')
    else:
        date_answer = None
        while date_answer not in ['да', 'нет']:
            date_answer = input('Отсортировать операции по дате? Да/Нет\n').lower()
            if date_answer == 'да':
                logger_sort_by_data.info('Пользователь выбрал Сортировку - Да')
                sorting_answer = None
                while sorting_answer not in ['по возрастанию', 'по убыванию', 'возрастанию', 'убыванию']:
                    sorting_answer = input('Отсортировать по возрастанию или по убыванию?\n').lower()
                    if sorting_answer in ['по возрастанию', 'возрастанию']:
                        logger_sort_by_data.info('Пользователь выбрал сортировку по возрастанию')
                        list_transactions = sort_by_date(list_transact, False)
                    elif sorting_answer in ['по убыванию', 'убыванию']:
                        logger_sort_by_data.info('Пользователь выбрал сортировку по убыванию')
                        list_transactions = sort_by_date(list_transact, True)
                    else:
                        logger_sort_by_data.warning(f'Пользователь ввел некорректное значение: {sorting_answer}')
                        print('\nВы ввели некорректное значение, повторите снова\n')
            elif date_answer == 'нет':
                logger_sort_by_data.info('Пользователь не выбрал сортировку')
                list_transactions = list_transact
            else:
                logger_sort_by_data.warning(f'Пользователь ввел некорректное значение: {date_answer}')
                print('\nВы ввели некорректное значение, повторите снова\n')
        logger_sort_by_data.info('Успешный возврат списка транзакций')
        return list_transactions
    return []

def filter_rub_transact():
    logger_rub_transact.info('Старт работы функции')
    list_transact = sort_by_data()
    if not list_transact:
        logger_rub_transact.error('Получен пустой список, возврат пустого списка!')
    else:
        transact_answer = None
        while transact_answer not in ['да', 'нет']:
            transact_answer = input('Выводить только рублевые транзакции? Да/Нет\n').lower()
        if transact_answer == 'да':
            logger_rub_transact.info('Пользователь выбрал только рублевые транзакции')
            rub_transact = 'RUB'
            list_transactions = filter_by_currency(list_transact, rub_transact)
        elif transact_answer == 'нет':
            logger_rub_transact.info('Пользователь не выбрал рублевые транзакции')
            list_transactions = list_transact
        else:
            logger_rub_transact.warning(f'Пользователь ввел некорректное значение: {transact_answer}')
            print('\nВы ввели некорректное значение, повторите снова\n')
        logger_rub_transact.info('Успешный возврат списка транзакций')
        return list_transactions
    return []

def filter_by_pattern():
    logger_by_pattern.info('Старт работы функции')
    list_transact = filter_rub_transact()
    if not list_transact:
        logger_by_pattern.error('Получен пустой список, возврат пустого списка!')
    else:
        filter_word_answer = None
        while filter_word_answer not in ['да', 'нет']:
            filter_word_answer = input(
                'Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n').lower()
            if filter_word_answer == 'да':
                pattern = input('Введите нужное слово: ')
                logger_by_pattern.info(f'Пользователь выбрал фильтр по значению: {pattern}')
                list_transactions = get_required_dictionary(list_transact, pattern)
            elif filter_word_answer == 'нет':
                logger_by_pattern.info('Фильтрация по словам не выбрана')
                list_transactions = list_transact
            else:
                logger_by_pattern.warning(f'Пользователь ввел некорректное значение: {filter_word_answer}')
                print('\nВы ввели некорректное значение, повторите снова\n')
        logger_by_pattern.info('Успешный возврат списка транзакций')
        return list_transactions
    return []

def main():
    logger_main.info('Старт работы функции')
    list_transact = filter_by_pattern()
    if not list_transact:
        logger_main.error('Получен пустой список, возврат пустого списка!')
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        return

    logger_main.info('Получен список транзакций')
    print('\nРаспечатываю итоговый список транзакций...\n')

    print(f'Всего банковских операций в выборке: ')

    set_descriptions = set()
    for description in list_transact:
        set_descriptions.add(description.get('description'))
    logger_main.info(f'Получен список категорий: {list(set_descriptions)}, передача его в category_counter')
    for key, value in category_counter(list_transact, list(set_descriptions)).items():
        print(f'{key}: {value}')
    print()

    for item in list_transact:
        print('-'*45)
        print(f'{get_date(item['date'])} {item.get('description')}')
        if item.get('from') or item.get('from') != 0:
                print(f'{mask_account_card(item.get('from'))} -> {mask_account_card(item.get('to'))}')
        else:
            print(f'{mask_account_card(item.get('to'))}')
        if item.get('operationAmount'):
            print(f'Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['code']}')
        else:
            print(f'Сумма: {item['amount']} {item['currency_code']}')
        print('*'*45,'\n')

if __name__ == '__main__':
    main()