import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_transaction_amount(transaction: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
       Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
       и конвертации суммы операции в рубли."""

    transact = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency in ["USD","EUR"]:
        response = requests.get(f'https://currate.ru/api/?get=rates&pairs={currency}RUB&key={API_KEY}')
        if response.status_code != 200:
            raise Exception(f"Курс для конвертации не получен. Возможная причина: {response.reason}")
        exchange_rate = float(response.json()['data'][f'{currency}RUB'])
        amount = round(transact * exchange_rate, 2)
        return amount
    return transact