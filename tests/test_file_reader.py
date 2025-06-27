from unittest import mock
from unittest.mock import patch

import pytest

from src.file_reader import csv_file_reader, excel_file_reader


@pytest.mark.parametrize("expected, test_list", [([{
                                                    "id": 650703,
                                                    "state": "EXECUTED",
                                                    "date": "2023-09-05T11:30:32Z",
                                                    "amount": 16210,
                                                    "currency_name": "Sol",
                                                    "currency_code": "PEN",
                                                    "from": "Счет 58803664561298323391",
                                                    "to": "Счет 39745660563456619397",
                                                    "description": "Перевод организации",
                                                    }],
                                                  '''id;state;date;amount;currency_name;currency_code;from;to;description\n
                                                  650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации''')])
def test_csv_file_reader(test_list, expected):
    """Тестирование успешного чтения CSV файла"""
    with patch('builtins.open', new_callable=mock.mock_open, read_data=test_list) as mock_data:
        assert csv_file_reader('test') == expected
        mock_data.assert_called_once_with('test', 'r', encoding='utf-8', errors='strict', newline='')


def test_csv_file_reader_no_file():
    """Тестирования случая когда CSV файл не найден"""
    with patch('builtins.open', side_effect=FileNotFoundError) as mock_data:
        assert csv_file_reader('test') == []
        mock_data.assert_called_once_with('test', 'r', encoding='utf-8', errors='strict', newline='')

def test_get_dict_transactions_str():
    """Тестирование случая когда в CSV файле строка"""
    with patch('builtins.open', new_callable=mock.mock_open, read_data='650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации') as mock_data:
        assert csv_file_reader('test') == []
        # Проверяем, что функция open была вызвана правильно
        mock_data.assert_called_once_with('test', 'r', encoding='utf-8', errors='strict', newline='')


def test_get_dict_transactions_empty_list():
    """Тестирование случая когда CSV файл пустой"""
    with patch('builtins.open', new_callable=mock.mock_open, read_data='') as mock_data:
        assert csv_file_reader('test') == []
        mock_data.assert_called_once_with('test', 'r', encoding='utf-8', errors='strict', newline='')