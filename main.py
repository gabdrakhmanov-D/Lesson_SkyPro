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

def select_file() -> str:
    """Функция, запрашивающая из какого файла получить информацию о транзакциях. Возвращает тип файла."""

    logger_file.info('Старт работы функции')
    selected_file = ''
    while selected_file not in ['1', '2', '3']:
        selected_file = str(input(
            'Привет! Добро пожаловать в программу работы'
            'с банковскими транзакциями.Выберите необходимый пункт меню:\n'
            '1. Получить информацию о транзакциях из JSON-файла\n'
            '2. Получить информацию о транзакциях из CSV-файла\n'
            '3. Получить информацию о транзакциях из XLSX-файла\n'))

        if selected_file == '1':
            logger_file.info('Выбран пункт 1')
            print('Для обработки выбран JSON-файл.')
            file_type = 'json'
        elif selected_file == '2':
            logger_file.info('Выбран пункт 2')
            print('Для обработки выбран CSV-файл.')
            file_type = 'csv'
        elif selected_file == '3':
            logger_file.info('Выбран пункт 3')
            print('Для обработки выбран XLSX-файл.')
            file_type = 'xlsx'
        else:
            logger_file.warning('Выбран неверный пункт в меню')
            print('Выбран неверный пункт в меню, повторите ввод.')
    return file_type


def select_filter() -> str:
    """Функция, запрашивает у пользователя статус по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""

    logger_filter.info('Старт работы функции')
    filter_transact = None
    while filter_transact not in ['EXECUTED', 'CANCELED', 'PENDING']:
        filter_transact = input('\nВведите статус, по которому необходимо выполнить фильтрацию.'
                              'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n')
        if filter_transact.upper() in ['EXECUTED', 'CANCELED', 'PENDING']:
            logger_filter.info(f'Возврат cтатуса фильтрации: {filter_transact}')
            answer_filter = filter_transact.upper()
            break
        else:
            logger_filter.warning(f'Пользователь ввел некорректный фильтр: {filter_transact}')
            print(f'Статус операции {filter_transact} недоступен.')
    return answer_filter


def sort_by_data() -> tuple[bool, bool]:
    """Функция запрашивает у пользователя сортировать по дате или нет.
    Если да, запрашивает делать сортировку по убыванию или возрастанию"""

    logger_sort_by_data.info('Старт работы функции')
    need_sort_date = False
    sorting_order = False
    date_answer = None
    while date_answer not in ['да', 'нет']:
        date_answer = input('Отсортировать операции по дате? Да/Нет\n').lower()
        if date_answer == 'да':
            need_sort_date = True
            logger_sort_by_data.info('Пользователь выбрал Сортировку - Да')
            sorting_answer = None
            while sorting_answer not in ['по возрастанию', 'по убыванию', 'возрастанию', 'убыванию']:
                sorting_answer = input('Отсортировать по возрастанию или по убыванию?\n').lower()
                if sorting_answer in ['по возрастанию', 'возрастанию']:
                    logger_sort_by_data.info('Пользователь выбрал сортировку по возрастанию')
                    break
                elif sorting_answer in ['по убыванию', 'убыванию']:
                    logger_sort_by_data.info('Пользователь выбрал сортировку по убыванию')
                    sorting_order = True
                    break
                else:
                    logger_sort_by_data.warning(f'Пользователь ввел некорректное значение: {sorting_answer}')
                    print('\nВы ввели некорректное значение, повторите снова\n')
        elif date_answer == 'нет':
            logger_sort_by_data.info('Пользователь не выбрал сортировку')
            break
        else:
            logger_sort_by_data.warning(f'Пользователь ввел некорректное значение: {date_answer}')
            print('\nВы ввели некорректное значение, повторите снова\n')
    return need_sort_date, sorting_order


def filter_rub_transact() -> bool:
    """Функция, которая запрашивает выводить только рублевые транзакции или нет"""

    logger_rub_transact.info('Старт работы функции')
    transact_answer = None
    while transact_answer not in ['да', 'нет']:
        transact_answer = input('Выводить только рублевые транзакции? Да/Нет\n').lower()
        if transact_answer == 'да':
            logger_rub_transact.info('Пользователь выбрал только рублевые транзакции')
            need_rub_transact = True
            break
        elif transact_answer == 'нет':
            logger_rub_transact.info('Пользователь не выбрал рублевые транзакции')
            need_rub_transact = False
            break
        else:
            logger_rub_transact.warning(f'Пользователь ввел некорректное значение: {transact_answer}')
            print('\nВы ввели некорректное значение, повторите снова\n')
    return need_rub_transact


def filter_by_pattern() -> tuple[bool, str] | tuple[bool, bool]:
    """Функция, запрашивает необходимость фильтрации по слову. В случае положительного ответа. Запрашивает слово."""
    logger_by_pattern.info('Старт работы функции')
    filter_word_answer = None
    need_filter_by_pattern = False
    pattern = False
    while filter_word_answer not in ['да', 'нет']:
        filter_word_answer = input(
            'Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n').lower()
        if filter_word_answer == 'да':
            pattern = input('Введите нужное слово: ')
            logger_by_pattern.info(f'Пользователь выбрал фильтр по значению: {pattern}')
            need_filter_by_pattern = True
            break
        elif filter_word_answer == 'нет':
            logger_by_pattern.info('Фильтрация по словам не выбрана')
            break
        else:
            logger_by_pattern.warning(f'Пользователь ввел некорректное значение: {filter_word_answer}')
            print('\nВы ввели некорректное значение, повторите снова\n')
    return need_filter_by_pattern, pattern

def main():

    logger_main.info('Старт работы функции')
    file_type = select_file()
    filter_status = select_filter()
    need_sort_date, sorting_order = sort_by_data()
    need_rub_filter = filter_rub_transact()
    need_filter_by_pattern, pattern = filter_by_pattern()

    if file_type == 'csv':
        list_transactions = csv_file_reader()
        if list_transactions:
            logger_main.info('Успешно получен список транзакций csv')
        else:
            logger_main.error('Список транзакций csv пуст!')
    elif file_type == 'xlsx':
        list_transactions = excel_file_reader()
        if list_transactions:
            logger_main.info('Успешно получен список транзакций xlsx')
        else:
            logger_main.error('Список транзакций xlsx пуст!')
    else:
        list_transactions = get_dict_transactions()
        if list_transactions:
            logger_main.info('Успешно получен список транзакций json')
        else:
            logger_main.error('Список транзакций json пуст!')

    list_transactions = filter_by_state(list_transactions, filter_status)
    if list_transactions:
        logger_main.info(f'Успешно получен отфильтрованный по {filter_status} список транзакций')
    else:
        logger_main.error('Функция filter_by_state вернула пустой список!')

    if need_sort_date:
        list_transactions = sort_by_date(list_transactions, sorting_order)
        if list_transactions:
            logger_main.info(f'Успешно получен отсортированный по дате список транзакций')
        else:
            logger_main.error('Функция sort_by_date вернула пустой список!')

    if need_rub_filter:
        list_transactions = filter_by_currency(list_transactions,'RUB', file_type)
        if list_transactions:
            logger_main.info('Успешно получен список транзакций отсортированный по валюте: "RUB"')
        else:
            logger_main.error('Функция filter_by_currency вернула пустой список!')

    if need_filter_by_pattern:
        list_transactions = get_required_dictionary(list_transactions, pattern)
        if list_transactions:
            logger_main.info(f'Успешно получен список транзакций отсортированный по слову: {pattern}')
        else:
            logger_main.error('Функция get_required_dictionary вернула пустой список!')


    if not list_transactions:
        logger_main.error('Получен пустой список!')
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        return

    logger_main.info('Получен список транзакций')
    print('\nРаспечатываю итоговый список транзакций...\n')

    print(f'Всего банковских операций в выборке: ')

    list_transactions = list(list_transactions)
    set_descriptions = set()
    for description in list_transactions:
        set_descriptions.add(description.get('description'))
    logger_main.info(f'Получен список категорий: {list(set_descriptions)}, передача его в category_counter')

    count_dict = category_counter(list_transactions, list(set_descriptions))
    for key, value in count_dict.items():
        print(f'{key}: {value}')
    print()

    for item in list_transactions:
        print('-'*45)
        print(f'{get_date(item['date'])} {item.get('description')}')
        if item.get('from') and item.get('from') != 0:
                print(f'{mask_account_card(item.get('from'))} -> {mask_account_card(item.get('to'))}')
        else:
            print(f'{mask_account_card(item.get('to'))}')
        if item.get('operationAmount'):
            print(f'Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['code']}')
        else:
            print(f'Сумма: {item['amount']} {item['currency_code']}')
        print('*'*45,'\n')
    logger_main.info('Завершение работы программы')

if __name__ == '__main__':
    main()