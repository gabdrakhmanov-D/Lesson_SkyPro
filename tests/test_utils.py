from unittest.mock import patch, Mock

from src.utils import get_dict_transactions


def test_get_dict_transactions_str(temp_file_str):
    """Тестирование случая когда в JSON файле строка"""
    assert get_dict_transactions(temp_file_str) == []


def test_get_dict_transactions_empty_list(temp_file_empty_list):
    """Тестирование случая когда JSON файл пустой"""
    assert get_dict_transactions(temp_file_empty_list) == []


def test_get_dict_transactions_no_file():
    """Тестирования случая когда файл не найден"""
    assert get_dict_transactions('abc') == []


def test_get_dict_transactions(temp_json_file):
    """Тестирование успешного чтения файла"""
    assert get_dict_transactions(temp_json_file) == [
                                                      {
                                                        "id": 441945886,
                                                        "state": "EXECUTED",
                                                        "date": "2019-08-26T10:50:58.294041",
                                                        "operationAmount":
                                                                            {
                                                                              "amount": "31957.58",
                                                                              "currency":
                                                                                          {
                                                                                            "name": "руб.",
                                                                                            "code": "RUB"
                                                                                          }
                                                                            },
                                                        "description": "Перевод организации",
                                                        "from": "Maestro 1596837868705199",
                                                        "to": "Счет 64686473678894779589"
                                                      },
                                                      {
                                                        "id": 41428829,
                                                        "state": "EXECUTED",
                                                        "date": "2019-07-03T18:35:29.512364",
                                                        "operationAmount":
                                                                            {
                                                                              "amount": "8221.37",
                                                                              "currency":
                                                                                          {
                                                                                            "name": "USD",
                                                                                            "code": "USD"
                                                                                          }
                                                                            },
                                                        "description": "Перевод организации",
                                                        "from": "MasterCard 7158300734726758",
                                                        "to": "Счет 35383033474447895560"
                                                      }]
