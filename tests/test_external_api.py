from src.external_api import get_transaction_amount


def test_get_transaction_amount(examples_for_generators):
    assert get_transaction_amount(examples_for_generators[2]) == 43318.34

def test_get_transaction_amount_usd(examples_for_generators):
    assert get_transaction_amount(examples_for_generators[1]) == 5077786.08