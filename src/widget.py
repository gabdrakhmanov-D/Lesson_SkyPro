import re

from src import masks


def mask_account_card(incoming_data: str) -> str:
    """Функция, которая принимает номер счета или карты и возвращает строку с замаскированным номером."""
    tmp_list = incoming_data.split()
    if not any(symbols.isalpha() for symbols in tmp_list[:-1]) and not any(
        symbols.isdigit() for symbols in tmp_list[-1]
    ):  # проверяет, состоит ли строка из букв и цифр
        raise ValueError("Некорректный номер карты или счета")

    card_number = tmp_list[-1]
    if "Счет" in tmp_list[0]:
        return f"{' '.join(tmp_list[0:-1])} {masks.get_mask_account(card_number)}"
    else:
        return f"{' '.join(tmp_list[0:-1])} {masks.get_mask_card_number(card_number)}"


def get_date(date: str) -> str:
    """Функция, которая изменяет формат даты"""
    match = re.match(
        r"\d{4}-\d{2}-\d{2}", date
    )  # шаблон для проверки даты по формату гг.мм.дд
    if match:
        return f"{match.group()[-2:]}.{match.group()[5:7]}.{match.group()[0:4]}"
    else:
        raise ValueError("Неверный формат даты")
