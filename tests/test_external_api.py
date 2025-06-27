import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

from src.external_api import get_transaction_amount

load_dotenv()
API_KEY = os.getenv("API_KEY")


def test_get_transaction_amount_rub(examples_for_generators):
    """Тестирование транзакции в рублях"""
    assert get_transaction_amount(examples_for_generators[2]) == 43318.34


@patch("requests.get")
def test_get_transaction_amount_usd(mock_get, examples_for_generators):
    """Тестирование транзакции в долларах"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "status": "200",
        "message": "rates",
        "data": {"USDRUB": "64.1824"},
    }
    mock_get.return_value = mock_response

    assert get_transaction_amount(examples_for_generators[1]) == 5077786.08
    # Проверяем, что объект Mock был вызван один раз с правильным URL в качестве аргумента.
    mock_get.assert_called_once_with(
        f"https://currate.ru/api/?get=rates&pairs=USDRUB&key={API_KEY}"
    )


@patch("requests.get")
def test_get_transaction_amount_eur(mock_get, examples_for_generators):
    """Тестирование транзакции в евро"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "status": "200",
        "message": "rates",
        "data": {"EURRUB": "100"},
    }
    mock_get.return_value = mock_response

    assert (
        get_transaction_amount(
            {
                "id": 743628025,
                "state": "EXECUTED",
                "date": "2018-06-04T06:59:55.424356",
                "operationAmount": {
                    "amount": "1",
                    "currency": {"name": "EUR", "code": "EUR"},
                },
                "description": "Перевод организации",
                "from": "Счет 54883981902864782073",
                "to": "Счет 61834060137088759145",
            }
        )
        == 100.0
    )
    mock_get.assert_called_once_with(
        f"https://currate.ru/api/?get=rates&pairs=EURRUB&key={API_KEY}"
    )


@patch("requests.get")
def test_get_transaction_amount_error(mock_get, examples_for_generators):
    """Тестирование когда нет доступа к сайту"""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {
        "status": "404",
        "message": "rates",
        "data": {"USDRUB": "64.1824"},
    }
    mock_get.return_value = mock_response

    with pytest.raises(Exception):
        get_transaction_amount(examples_for_generators[1])
        mock_get.assert_called_once_with(
            f"https://currate.ru/api/?get=rates&pairs=USDRUB&key={API_KEY}"
        )
