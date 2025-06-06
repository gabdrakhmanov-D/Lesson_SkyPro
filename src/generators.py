from typing import Union, Any, Generator


def filter_by_currency(list_transact: list[dict[str, int | str]], currency) -> Generator[
    dict[str, int | str], Any, None]:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    return (dict_in_list_transact for dict_in_list_transact in list_transact if dict_in_list_transact["operationAmount"]["currency"]["code"] == currency)
