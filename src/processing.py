from typing import Union


def filter_by_state(
        list_dict: list[dict[str, Union[int, str]]], state="EXECUTED"
) -> list[dict[str, Union[int, str]]]:
    """Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению"""
    new_list = [i for i in list_dict if i["state"] == state]
    return new_list


def sort_by_date(
        list_dict: list[dict[str, Union[int, str]]], sorting=True
) -> list[dict[str, Union[int, str]]]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате."""
    from datetime import datetime

    from widget import get_date

    return sorted(
        list_dict,
        key=lambda date: datetime.strptime(get_date(date["date"]), "%d.%m.%Y"),
        reverse=sorting,
    )
