import logging


logger = logging.getLogger('mask')
file_handler = logging.FileHandler('../logs/masks.log', encoding= 'utf-8', mode= 'w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    logger.info(f'Старт работы функции')
    if not card_number.isdigit() or len(card_number) != 16:
        logger.error(f'Ошибка: неверный формат номера карты')
        raise ValueError('Номер карты должен состоять из 16 цифр!')
    logger.info(f'Возврат маски номера карты')
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    logger.info(f'Старт работы функции')
    if not account_number.isdigit() or len(account_number) != 20:
        logger.error(f'Ошибка: неверный формат номера счета')
        raise ValueError("Номер счета должен состоять из 20 цифр!")
    logger.info(f'Возврат маски счета')
    return f"**{str(account_number)[-4:]}"
