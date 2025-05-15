from typing import Union


def filter_by_state(list_dict:list[dict[str,Union[int,str]]], state= 'EXECUTED') -> list[dict[str,Union[int,str]]]:
    '''Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению'''
    new_list = []
    for i in list_dict:
        if i['state'] == state:
            new_list.append(i)
    return new_list


def sort_by_date(list_dict:list[dict[str,Union[int,str]]], sorting = True) -> list[dict[str,Union[int,str]]]:
    '''Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date).'''
    return sorted(list_dict, key=lambda date: date['date'], reverse= sorting)

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))