from typing import Any, Dict, Iterator, List

transactions = [
    {
        "id": "939719570",
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": "142264268",
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": "873106923",
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": "895315941",
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": "594226727",
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(list_of_dictionaries: List[Dict[str, Any]], code: str) -> Iterator[int]:
    """
    Функция, которая возвращает идентификаторы транзакций по коду валюты
    """
    return (
        transaction["id"]
        for transaction in filter(lambda x: x["operationAmount"]["currency"]["code"] == code, list_of_dictionaries)
    )


def transaction_descriptions(transaction: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Функция, которая выводит description каждой операции по очереди
    """
    return (transaction["description"] for transaction in transaction)


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Функция, которая генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        numbre = str(number)
        yield f"{'0' * (16 - len(numbre))}{number}"
