from typing import Any, Generator


def filter_by_currency(
    list_transact: list[dict], currency
) -> Generator[dict]:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    return (
        dict_in_list_transact
        if (dict_in_list_transact.get("operationAmount")
            and dict_in_list_transact["operationAmount"]["currency"]["code"] == currency)
        else dict_in_list_transact for dict_in_list_transact in list_transact
        if dict_in_list_transact.get('currency_code') == currency)



def transaction_descriptions(list_transact: list[dict[str, int | str]]):
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for dict_in_list_transact in list_transact:
        yield dict_in_list_transact["description"]


def card_number_generator(
    start_number: int, end_number: int
) -> Generator[str, Any, None]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    bank_card_number = ["0"] * 16

    if end_number >= start_number:
        number_of_digits = end_number - start_number + 1
    else:
        number_of_digits = start_number - end_number + 1

    for number in range(number_of_digits):
        for digit_index in range(-len(str(start_number)), 0):
            bank_card_number[digit_index] = str(start_number)[digit_index]
        yield f"{''.join(bank_card_number[0:4])} {''.join(bank_card_number[4:8])} {''.join(bank_card_number[8:12])} {''.join(bank_card_number[12:])}"
        start_number += 1
