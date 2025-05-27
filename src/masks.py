def get_mask_card_number(card_number: int = None) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    if card_number:
        card_number_str = str(card_number)
        hide_number_card = []
        i = 0

        for num in card_number_str:

            if i <= 5:  # в этом условии в новый список добавляем первые 6 цифр карты
                hide_number_card.append(num)
                i += 1
                if i % 4 == 0:
                    hide_number_card.append(
                        " "
                    )  # после 4 символов подряд вставляется пробел

            elif i > 5 and (
                (len(card_number_str) - i) > 4
            ):  # после шести цифр и до последних четырех вставляем звездочки
                hide_number_card.append("*")
                i += 1
                if i % 4 == 0:
                    hide_number_card.append(" ")

            else:  # в этом условии вставляем последние 4 цифры
                hide_number_card.append(num)
                i += 1
                if i % 4 == 0:
                    hide_number_card.append(" ")

        if hide_number_card[-1] == " ":
            del hide_number_card[-1]
        return "".join(hide_number_card)

    else:
        raise ValueError("Номер карты не может быть пустым")


def get_mask_account(account_number: int = None) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    if account_number:
        return f"**{str(account_number)[-4:]}"
    else:
        raise ValueError("Номер счета не может быть пустым")
