from argparse import ArgumentError


def mask_account_card(incoming_data: str = None) -> str:
    """Функция, которая принимает номер счета или карты и возвращает строку с замаскированным номером."""
    from src import masks
    if incoming_data and isinstance(incoming_data, str):
        tmp_list = incoming_data.split()
        if any(symbols.isalpha() for symbols in tmp_list[:-1]) and any(symbols.isdigit() for symbols in tmp_list[-1]):# проверяет, состоит ли строка из букв и цифр
            card_number = int(tmp_list[-1])
            if "Счет" in tmp_list:
                return f"{' '.join(tmp_list[0:-1])} {masks.get_mask_account(card_number)}"
            else:
                return f"{' '.join(tmp_list[0:-1])} {masks.get_mask_card_number(card_number)}"
        else:
            raise ValueError('Некорректный номер карты или счета')
    else:
        raise TypeError('Номер счета или карты может состоять только из строки!')

def get_date(date: str) -> str:
    """Функция, которая изменяет формат даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
