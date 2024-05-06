import pytest

from src.masks import masck_for_account, mask_for_card


@pytest.fixture
def bill_num() -> str:
    return "1234567890"


def test_account_mask(bill_num: str) -> None:
    assert masck_for_account(bill_num) == "**7890"


@pytest.mark.parametrize(
    "card_num, mask_card_num",
    [("1234567887654321", "1234 67** **** 4321"), ("1111111111111111", "1111 11** **** 1111")],
)
def test_card_mask(card_num: str, mask_card_num: str) -> None:
    assert mask_for_card(card_num) == mask_card_num
