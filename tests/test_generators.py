from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions

usd_transactions = filter_by_currency(transactions, "USD")
descriptions = transaction_descriptions(transactions)
cards = card_number_generator(1, 5)


def test_filter_by_currency() -> None:
    assert next(usd_transactions) == "939719570"
    assert next(usd_transactions) == "142264268"
    assert next(usd_transactions) == "895315941"


def test_card_number_generator() -> None:
    assert next(cards) == "0000000000000001"
    assert next(cards) == "0000000000000002"
    assert next(cards) == "0000000000000003"
    assert next(cards) == "0000000000000004"
    assert next(cards) == "0000000000000005"


def test_transactions_for_test() -> None:
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"
