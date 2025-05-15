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
    pass
