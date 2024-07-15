import pytest

from src.widget import convert_datetime_to_date, mask_for_card_or_account


@pytest.fixture
def input_number() -> str:
    return "Visa Platinum 7000792289606361"


def test_mask_for_card_or_account(input_number: str) -> None:
    assert mask_for_card_or_account(input_number) == "Visa Platinum 7000 92** **** 6361"


@pytest.fixture
def input_data() -> str:
    return "2018-07-11T02:26:18.671407"


def test_data_split(input_data: str) -> None:
    assert convert_datetime_to_date(input_data) == "11.07.2018"
