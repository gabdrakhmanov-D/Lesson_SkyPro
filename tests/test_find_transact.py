import pytest
from src.find_transact import get_required_dictionary, category_counter


@pytest.mark.parametrize("pattern", ["Перевод организации", "перевод организации"])
def test_get_required_dictionary(pattern, examples_for_generators):
    """Тестирование успешного поиска транзакций"""
    assert get_required_dictionary(examples_for_generators, pattern) == [examples_for_generators[0], examples_for_generators[-1]]


