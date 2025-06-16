def get_transaction_amount(transaction: dict):
    transact = float(transaction["operationAmount"]["amount"])
    return transact