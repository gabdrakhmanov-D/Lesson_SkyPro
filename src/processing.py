from typing import Union


def filter_by_state(
        list_dict: list[dict[str, Union[int, str]]], state="EXECUTED"
) -> list[dict[str, Union[int, str]]]:
    """Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению"""
    return [dict_in_list for dict_in_list in list_dict if dict_in_list["state"] == state]


def sort_by_date(
        list_dict: list[dict[str, Union[int, str]]], sorting=True
) -> list[dict[str, Union[int, str]]]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате."""
    from datetime import datetime

    from src.widget import get_date

    return sorted(
        list_dict,
        key=lambda date: datetime.fromisoformat(date["date"]),
        reverse=sorting,
    )
