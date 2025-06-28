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

