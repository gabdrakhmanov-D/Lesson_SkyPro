from src.external_api import get_transaction_amount


def test_get_transaction_amount(examples_for_generators):
    assert get_transaction_amount(examples_for_generators[2]) == 43318.34