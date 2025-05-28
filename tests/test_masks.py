import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("7000792289606361", "7000 79** **** 6361"),
    ],
)
def test_mask_card(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", ["123456789012345", "1245", "card number"])
def test_mask_card_wrong_number(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("73654108430135871111", "**1111"),
        ("73654108430135807777", "**7777")],
)
def test_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", ["736541084301", "9876543210", "account_number"])
def test_mask_account_empty_number(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)
