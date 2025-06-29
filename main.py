from src.file_reader import csv_file_reader, excel_file_reader
from src.find_transact import get_required_dictionary
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_dict_transactions

if __name__ == '__main__':
    select_file = False
    while select_file not in ['1', '2', '3']:
        select_file = str(input(
            'Привет! Добро пожаловать в программу работы'
            'с банковскими транзакциями.Выберите необходимый пункт меню:\n'
            '1. Получить информацию о транзакциях из JSON-файла\n'
            '2. Получить информацию о транзакциях из CSV-файла\n'
            '3. Получить информацию о транзакциях из XLSX-файла\n'))

        if select_file == '1':
            print('Для обработки выбран JSON-файл.')
            list_transactions = get_dict_transactions()
        elif select_file == '2':
            print('Для обработки выбран CSV-файл.')
            list_transactions = csv_file_reader()
        elif select_file == '3':
            print('Для обработки выбран XLSX-файл.')
            list_transactions = excel_file_reader()
        else:
            print('Выбран неверный пункт в меню')

    filter_transact = None
    while filter_transact not in ['EXECUTED', 'CANCELED', 'PENDING']:
        filter_transact = input('\nВведите статус, по которому необходимо выполнить фильтрацию.'
                              'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n').upper()
        if filter_transact in ['EXECUTED', 'CANCELED', 'PENDING']:
            filtered_dict = filter_by_state(list_transactions, filter_transact)
        else:
            print(f'Статус операции {filter_transact} недоступен.')

    date_answer = None
    while date_answer not in ['да','нет']:
        date_answer = input('Отсортировать операции по дате? Да/Нет\n').lower()
        if date_answer == 'да':
            sorting_answer = None
            while sorting_answer not in ['по возрастанию', 'по убыванию', 'возрастанию', 'убыванию']:
                sorting_answer = input('Отсортировать по возрастанию или по убыванию?\n').lower()
                if sorting_answer in ['по возрастанию', 'возрастанию']:
                    sorting_dict_by_data = sort_by_date(filtered_dict, False)
                elif sorting_answer in ['по убыванию', 'убыванию']:
                    sorting_dict_by_data = sort_by_date(filtered_dict, True)
                else:
                    print('\nВы ввели некорректное значение, повторите снова\n')
        # elif date_answer == 'нет':
        #     date_sort = False
        else:
            print('\nВы ввели некорректное значение, повторите снова\n')

    transact_answer = None
    while transact_answer not in ['да','нет']:
        transact_answer = input('Выводить только рублевые транзакции? Да/Нет\n').lower()
        if transact_answer == 'да':
            rub_transact = 'RUB'
            dict_by_currency = filter_by_currency(sorting_dict_by_data, rub_transact)
        elif transact_answer == 'нет':
            rub_transact = False
            dict_by_currency = sorting_dict_by_data
        else:
            print('\nВы ввели некорректное значение, повторите снова\n')

    filter_word_answer = None
    while filter_word_answer not in ['да', 'нет']:
        filter_word_answer = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n').lower()
        if filter_word_answer == 'да':
            pattern = input('Введите нужное слово: ')
            filtered_dict_by_pattern = get_required_dictionary(dict_by_currency, pattern)
        elif filter_word_answer == 'нет':
            pattern = ''
        else:
            print('\nВы ввели некорректное значение, повторите снова\n')
    print('Распечатываю итоговый список транзакций...')
    print(filtered_dict_by_pattern)