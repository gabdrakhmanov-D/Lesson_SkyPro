import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('incoming_data, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                                    ('Счет 73654108430135874305', 'Счет **4305'),
                                                    ('Maestro 1596837868705199','Maestro 1596 83** **** 5199'),
                                                    ('Счет 35383033474447895560', 'Счет **5560')]
                         )
def test_mask_account_card(incoming_data,expected):
    assert mask_account_card(incoming_data) == expected

def test_mask_account_card_empty():
    """Тест если не пришли никакие данные"""
    with pytest.raises(TypeError) as exc_info:
        mask_account_card()
    assert str(exc_info.value) == "Номер счета или карты может состоять только из строки!"

@pytest.mark.parametrize('incoming_data', [12345657, ['Счет', '132456465454']])
def test_mask_account_wrong_data(incoming_data):
    """Тестирует функцию если введен неверный тип данных"""
    with pytest.raises(TypeError):
        mask_account_card(incoming_data)

@pytest.mark.parametrize('incoming_data', ['0007922 89606361', 'Maestro', 'Счет', 'Счет73654108430135874305'])
def test_mask_account_card_missing_data(incoming_data):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(incoming_data)
    assert str(exc_info.value) == 'Некорректный номер карты или счета'

#Тест функции get_date()
@pytest.mark.parametrize('date, expected',[('2024-03-11T02:26:18.671407', '11.03.2024'),
                                           ('2025-04-12T02:26:18.671407', '12.04.2025'),
                                           ('2023-12-01T02:26:18.671407', '01.12.2023')])
def test_get_date(date,expected):
    assert get_date(date) == expected

def test_get_date_empty_date():
    with pytest.raises(ValueError) as exc_info:
        get_date()
    assert str(exc_info.value) == 'Дата не может быть пустой'

@pytest.mark.parametrize('date', ['2024.12.10', '2024-april-01', '01/01/2028','1 may 2025', 'просто строка без даты'])
def test_get_date_wrong_format_date(date):
    with pytest.raises(ValueError) as exc_info:
        get_date(date)
    assert str(exc_info.value) == 'Неверный формат даты'