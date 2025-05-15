from typing import Union


def filter_by_state(list_dict:list[dict[str,Union[int,str]]], state= 'EXECUTED') -> list[dict[str,Union[int,str]]]:
    '''Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению'''
    pass