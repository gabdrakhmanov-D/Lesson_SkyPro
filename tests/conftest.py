import pytest


@pytest.fixture
def dict_with_examples():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def dict_no_state_executed():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def dict_same_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512363"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425571"},
    ]


@pytest.fixture
def dict_wrong_date_format():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "21 февраля 2025"},
        {"id": 939719570, "state": "EXECUTED", "date": "12-12-2025"},
        {"id": 594226727, "state": "CANCELED", "date": "03.03.25"},
        {"id": 615064591, "state": "CANCELED", "date": ""},
    ]
