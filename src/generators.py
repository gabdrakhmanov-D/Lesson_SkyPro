from typing import Union, Any, Generator


def filter_by_currency(list_transact: list[dict[str, int | str]], currency) -> Generator[
    dict[str, int | str], Any, None]:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    return (dict_in_list_transact for dict_in_list_transact in list_transact if dict_in_list_transact["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(list_transact: list[dict[str, int | str]]):
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for dict_in_list_transact in list_transact:
        yield dict_in_list_transact["description"]


def card_number_generator(start_number: int, end_number: int) -> Generator[str, Any, None]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    empty_list = ['0']*16

    if end_number >= start_number:
        number_of_digits = end_number-start_number + 1
    else:
        number_of_digits = start_number - end_number + 1

    for x in range(number_of_digits):
        for i in range(-len(str(start_number)),0):
            empty_list[i] = str(start_number)[i]
        yield f'{''.join(empty_list[0:4])} {''.join(empty_list[4:8])} {''.join(empty_list[8:12])} {''.join(empty_list[12:])}'
        start_number += 1
