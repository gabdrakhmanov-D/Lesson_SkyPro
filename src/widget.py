

def mask_account_card(incoming_data: str) -> str:
    """Функция, которая принимает номер счета или карты и возвращает строку с замаскированным номером."""
    from src import masks
    if incoming_data:
        tmp_list = incoming_data.split()
        card_number = int(tmp_list[-1])
        if "Счет" in tmp_list:
            return f"{' '.join(tmp_list[0:-1])} {masks.get_mask_account(card_number)}"
        else:
            return f"{' '.join(tmp_list[0:-1])} {masks.get_mask_card_number(card_number)}"
    else:
        raise TypeError('Номер счета или карты не может быть пустым')


def get_date(date: str) -> str:
    """Функция, которая изменяет формат даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
