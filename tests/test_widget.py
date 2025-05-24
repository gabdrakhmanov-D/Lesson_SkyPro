import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize('incoming_data, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                                    ('Счет 73654108430135874305', 'Счет **4305'),
                                                    ('Maestro 1596837868705199','Maestro 1596 83** **** 5199'),
                                                    ('Счет 35383033474447895560', 'Счет **5560')]
                         )
def test_mask_account_card(incoming_data,expected):
    assert mask_account_card(incoming_data) == expected


@pytest.mark.parametrize('incoming_data', [None, 12345657, ['Счет', '132456465454']])
def test_mask_account_wrong_data(incoming_data):
    with pytest.raises(TypeError):
        mask_account_card(incoming_data)

