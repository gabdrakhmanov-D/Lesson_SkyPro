from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(examples_for_generators):
    generator_usd = filter_by_currency(examples_for_generators, "USD")
    generator_rub =  filter_by_currency(examples_for_generators, "RUB")
    generator_none = filter_by_currency(examples_for_generators, "EUR")
    assert  next(generator_usd)== {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
    assert next(generator_usd) == {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
    assert next(generator_rub) == {
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
        }
    # assert next(generator_none) == 'Error: нет такой валюты в списке'

def test_transaction_descriptions(examples_for_generators):
    generator = transaction_descriptions(examples_for_generators)
    assert next(generator) == 'Перевод организации'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод с карты на карту'
    assert next(generator) == 'Перевод организации'

def test_card_number_generator():
    generator_1_2 = card_number_generator(1, 2)
    assert next(generator_1_2) == '0000 0000 0000 0001'
    assert next(generator_1_2) == '0000 0000 0000 0002'
def test_card_number_generator_end_of_range():
    generator_end_of_range = card_number_generator(9999999999999997, 9999999999999999)
    assert next(generator_end_of_range) == '9999 9999 9999 9997'
    assert next(generator_end_of_range) == '9999 9999 9999 9998'
    assert next(generator_end_of_range) == '9999 9999 9999 9999'
