import json
from unittest import mock
from unittest.mock import patch, Mock

import pytest

from src.utils import get_dict_transactions


def test_get_dict_transactions_str():
    """Тестирование случая когда в JSON файле строка"""
    with patch('builtins.open',new_callable=mock.mock_open, read_data='{"name": "Alice", "age": 25}') as mock_data:
        assert get_dict_transactions('test') == []
        mock_data.assert_called_once_with('test', 'r', encoding='utf-8') # Проверяем, что функция open была вызвана правильно


def test_get_dict_transactions_empty_list():
    """Тестирование случая когда JSON файл пустой"""
    with patch('builtins.open',new_callable=mock.mock_open, read_data='') as mock_data:
        assert get_dict_transactions('test') == []
        mock_data.assert_called_once_with('test', 'r', encoding='utf-8') # Проверяем, что функция open была вызвана правильно


def test_get_dict_transactions_not_found():
    """Тестирования случая когда файл не найден"""
    with patch('builtins.open', side_effect=FileNotFoundError) as mock_data:
        assert get_dict_transactions('test') == []
        mock_data.assert_called_once_with('test', 'r', encoding='utf-8') # Проверяем, что функция open была вызвана правильно

@pytest.mark.parametrize("expected, test_list", [([{
                            "id": 441945886,
                            "state": "EXECUTED",
                            "date": "2019-08-26T10:50:58.294041",
                            "operationAmount": {
                              "amount": "31957.58",
                              "currency": {
                                "name": "руб.",
                                "code": "RUB"
                              }
                            },
                            "description": "Перевод организации",
                            "from": "Maestro 1596837868705199",
                            "to": "Счет 64686473678894779589"
                          }], '''[
                          {
                            "id": 441945886,
                            "state": "EXECUTED",
                            "date": "2019-08-26T10:50:58.294041",
                            "operationAmount": {
                              "amount": "31957.58",
                              "currency": {
                                "name": "руб.",
                                "code": "RUB"
                              }
                            },
                            "description": "Перевод организации",
                            "from": "Maestro 1596837868705199",
                            "to": "Счет 64686473678894779589"
                          }]''')])
def test_get_read_success(test_list, expected):
    """Тестирование успешного чтения файла"""
    with patch('builtins.open',new_callable=mock.mock_open, read_data=f"{test_list}") as mock_data:
        assert get_dict_transactions('test') == expected
        mock_data.assert_called_once_with('test', 'r', encoding='utf-8') # Проверяем, что функция open была вызвана правильно