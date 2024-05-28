import json
from typing import Dict, List

import requests


def load_operations(file_path: str) -> List[Dict]:
    """
    Функция загружает данные о финансовых транзакциях из JSON-файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []


def convert_amount(operation: Dict) -> float:
    """
    Функция конвертирует сумму транзакции в рубли.
    """
    amount = float(operation["operationAmount"]["amount"])
    currency = operation["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    elif currency == "USD" or currency == "EUR":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if currency == "USD":
            usd_rate = float(data["Valute"]["USD"]["Value"])
            return amount * usd_rate
        elif currency == "EUR":
            eur_rate = float(data["Valute"]["EUR"]["Value"])
            return amount * eur_rate
    return 0.0


# Пример использования
dict_for_test = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": 9, "currency": {"name": "USD", "code": "USD"}},
    }
]

operations = load_operations("../data/operations.json")
print(operations)

amount_in_rubles = convert_amount(dict_for_test[0])
print(amount_in_rubles)
