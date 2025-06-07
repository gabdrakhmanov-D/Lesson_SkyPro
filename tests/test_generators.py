import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.mark.parametrize("currency, expected", [("USD", {
                                                          "id": 939719570,
                                                          "state": "EXECUTED",
                                                          "date": "2018-06-30T02:08:58.425572",
                                                          "operationAmount":
                                                              {
                                                              "amount": "9824.07",
                                                              "currency": {
                                                                  "name": "USD",
                                                                  "code": "USD"
                                                              }
                                                          },
                                                          "description": "Перевод организации",
                                                          "from": "Счет 75106830613657916952",
                                                          "to": "Счет 11776614605963066702"
                                                        }),
                                                ("RUB", {
                                                            "id": 873106923,
                                                            "state": "EXECUTED",
                                                            "date": "2019-03-23T01:09:46.296404",
                                                            "operationAmount": {
                                                                "amount": "43318.34",
                                                                "currency": {
                                                                    "name": "руб.",
                                                                    "code": "RUB"
                                                                }
                                                            },
                                                            "description": "Перевод со счета на счет",
                                                            "from": "Счет 44812258784861134719",
                                                            "to": "Счет 74489636417521191160"
                                                            }),
                                                ("RUB", {
                                                            "id": 594226727,
                                                            "state": "CANCELED",
                                                            "date": "2018-09-12T21:27:25.241689",
                                                            "operationAmount": {
                                                                "amount": "67314.70",
                                                                "currency": {
                                                                    "name": "руб.",
                                                                    "code": "RUB"
                                                                }
                                                            },
                                                            "description": "Перевод организации",
                                                            "from": "Visa Platinum 1246377376343588",
                                                            "to": "Счет 14211924144426031657"
                                                        }),
                                                ("USD", {
                                                            "id": 895315941,
                                                            "state": "EXECUTED",
                                                            "date": "2018-08-19T04:27:37.904916",
                                                            "operationAmount": {
                                                                "amount": "56883.54",
                                                                "currency": {
                                                                    "name": "USD",
                                                                    "code": "USD"
                                                                }
                                                            },
                                                            "description": "Перевод с карты на карту",
                                                            "from": "Visa Classic 6831982476737658",
                                                            "to": "Visa Platinum 8990922113665229"
                                                        })])
def test_filter_by_currency(examples_for_generators, currency, expected):
    generator = filter_by_currency(examples_for_generators, currency)
    assert next(generator), next(generator) == expected


@pytest.mark.parametrize("currency, expected", [("EUR", [])])
def test_filter_by_currency_eur_and_empty_list(examples_for_generators, currency,expected):
    generator_eur = filter_by_currency(examples_for_generators, currency)
    generator_empty_list = filter_by_currency([], "USD")
    assert list(generator_eur) == expected
    assert list(generator_empty_list) == []


@pytest.mark.parametrize("expected", ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"])
def test_transaction_descriptions(examples_for_generators, expected):
    generator = transaction_descriptions(examples_for_generators)
    assert next(generator), next(generator) == expected


@pytest.mark.parametrize("start_number, end_number, expected", [(1, 2, "0000 0000 0000 0001"),
                                                                (1, 2, "0000 0000 0000 0002"),
                                                                (9999999999999997, 9999999999999999, "9999 9999 9999 9997"),
                                                                (9999999999999997, 9999999999999999, "9999 9999 9999 9998"),
                                                                (9999999999999997, 9999999999999999, "9999 9999 9999 9999")])
def test_card_number_generator(start_number, end_number, expected):
    generator_1_2 = card_number_generator(start_number, end_number)
    assert next(generator_1_2), next(generator_1_2) == expected

