def mask_account_card(incoming_data: str):
    '''Функция, которая принимает номер счета или карты и возвращает строку с замаскированным номером.'''
    import masks
    tmp_list = incoming_data.split()
    card_number = int(tmp_list[-1])
    hide_number_card = []
    if 'Счет' in tmp_list:
        return f'{' '.join(tmp_list[0:-1])} {masks.get_mask_account(card_number)}'
    else:
        return f'{' '.join(tmp_list[0:-1])} {masks.get_mask_card_number(card_number)}'
