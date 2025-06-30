import pytest
from src.find_transact import get_required_dictionary, category_counter


@pytest.mark.parametrize("pattern", ["Перевод организации", "перевод организации"])
def test_get_required_dictionary(pattern, examples_for_generators):
    """Тестирование успешного поиска транзакций"""
    assert get_required_dictionary(examples_for_generators, pattern) == [examples_for_generators[0],
                                                                         examples_for_generators[-1]]


@pytest.mark.parametrize("pattern", [21, ["Перевод организации"]])
def test_get_required_dictionary_wrong_pattern(examples_for_generators, pattern):
    """Тестирование некорректного ввода значения поиска"""
    assert get_required_dictionary(examples_for_generators, pattern) == []


def test_get_required_dictionary_wrong_dict():
    """Тестирование случая передачи пустого списка для поиска"""
    assert get_required_dictionary([], "Перевод организации") == []


@pytest.mark.parametrize("list_dict, expected", [(
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ],
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ])])
def test_get_required_dictionary_no_key(list_dict, expected):
    """Тестирование случая, когда в каком то из словарей нет ключа 'description'"""
    assert get_required_dictionary(list_dict, "Перевод организации") == expected


# Тестирование для category_counter
@pytest.mark.parametrize("category", [["Перевод организации", "Перевод со счета на счет"]])
def test_category_counter(category, examples_for_generators):
    """Тестирование успешного подсчета категорий"""
    assert category_counter(examples_for_generators, category) == {"Перевод организации": 2,
                                                                   "Перевод со счета на счет": 2}


@pytest.mark.parametrize("category", ["Перевод организации", "Перевод со счета на счет"])
def test_category_counter_wrong_category(examples_for_generators, category):
    """Тестирование некорректного ввода значения категорий"""
    assert category_counter(examples_for_generators, category) == {}


def test_category_counter_wrong_dict():
    """Тестирование случая передачи пустого списка для поиска категорий"""
    assert category_counter([], ["Перевод организации", "Перевод со счета на счет"]) == {}


@pytest.mark.parametrize("list_dict, expected", [(
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ],
            {
                "Перевод организации": 1
            }
        )])
def test_category_counter_no_key(list_dict, expected):
    """Тестирование случая, когда в каком то из словарей нет ключа 'description'"""
    assert category_counter(list_dict, ["Перевод организации"]) == expected
