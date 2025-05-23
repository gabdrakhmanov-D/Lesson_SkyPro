from src.masks import get_mask_account, get_mask_card_number

import pytest

@pytest.mark.parametrize('card_number, expected', [(1234567890123456, '1234 56** **** 3456'),
                                                   (1234567890, '1234 5678 90'),
                                                   (123456789012345678, '1234 56** **** **56 78'),
                                                   (12345678901234567890, '1234 56** **** **** 7890')])

def test_mask_card(card_number, expected):
    assert get_mask_card_number(card_number) == expected
def test_mask_card_empty_number():
    with pytest.raises(TypeError):
        get_mask_card_number()

@pytest.mark.parametrize('account_number, expected', [(73654108430135874305, '**4305'),
                                                      (123456, '**3456'),
                                                      (None, '')])

def test_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected