def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError('Номер карты должен состоять из 16 цифр!')
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    if not account_number.isdigit() or len(account_number) != 20:
        raise ValueError("Номер счета должен состоять из 20 цифр!")
    return f"**{str(account_number)[-4:]}"
