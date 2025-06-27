from unittest import mock
from unittest.mock import patch
import pandas as pd

import pytest

from src.file_reader import csv_file_reader, excel_file_reader


# Тесты для функции csv_file_reader
@pytest.mark.parametrize(
    "expected, test_list",
    [
        (
            [
                {
                    "id": 650703,
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": 16210,
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                }
            ],
            """id;state;date;amount;currency_name;currency_code;from;to;description\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации""",
        )
    ],
)
def test_csv_file_reader(test_list, expected):
    """Тестирование успешного чтения CSV файла"""
    with patch(
        "builtins.open", new_callable=mock.mock_open, read_data=test_list
    ) as mock_data:
        assert csv_file_reader("test") == expected
        mock_data.assert_called_once_with(
            "test", "r", encoding="utf-8", errors="strict", newline=""
        )


def test_csv_file_reader_no_file():
    """Тестирование случая когда CSV файл не найден"""
    with patch("pandas.read_csv", side_effect=FileNotFoundError) as df_mock:
        assert csv_file_reader("path") == []
        df_mock.assert_called_once_with("path", delimiter=";")


def test_csv_file_reader_empty_list():
    """Тестирование случая когда CSV файл пустой"""
    with patch("builtins.open", new_callable=mock.mock_open, read_data="") as mock_data:
        assert csv_file_reader("test") == []
        mock_data.assert_called_once_with(
            "test", "r", encoding="utf-8", errors="strict", newline=""
        )


# Тесты для функции excel_file_reader
@pytest.mark.parametrize(
    "expected",
    [
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    ],
)
@patch("pandas.read_excel")
def test_excel_file_reader(df_mock, expected):
    """Тестирование успешного чтения Excel файла"""
    mock_data = pd.DataFrame(
        {
            "id": [650703],
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    )
    df_mock.return_value = mock_data
    assert excel_file_reader("path") == expected
    df_mock.assert_called_once_with("path")


def test_excel_file_reader_no_file():
    """Тестирование случая когда Excel файл не найден"""
    with patch("pandas.read_excel", side_effect=FileNotFoundError) as df_mock:
        assert excel_file_reader("path") == []
        df_mock.assert_called_once_with("path")


def test_excel_file_reader_str():
    """Тестирование случая когда Excel файл пустой"""
    with patch("pandas.read_excel") as df_mock:
        mock_data = pd.DataFrame()
        df_mock.return_value = mock_data
        assert excel_file_reader("path") == []
        df_mock.assert_called_once_with("path")
