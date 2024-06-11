import json
from typing import Dict, List

import requests

from src.logger import logger_setup

logger = logger_setup()


def load_operations(file_path: str) -> List[Dict]:
    """
    Функция загружает данные о финансовых транзакциях из JSON-файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("Функция load_operations рабоатет успешно")
                return data
            else:
                logger.error("С функций load_operations что-то не так")
                return []
    except FileNotFoundError:
        logger.error("Ошибка не выводит файл исправь и возвращайся снова")
        return []


def convert_amount(operation: Dict) -> float:
    """
    Функция конвертирует сумму транзакции в рубли.
    """
    amount = float(operation["operationAmount"]["amount"])
    currency = operation["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        logger.info("Функция convert_amount работает успешно")
        return amount
    elif currency == "USD" or currency == "EUR":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if currency == "USD":
            usd_rate = float(data["Valute"]["USD"]["Value"])
            logger.info("Функция convert_amount работает успешно")
            return amount * usd_rate
        elif currency == "EUR":
            eur_rate = float(data["Valute"]["EUR"]["Value"])
            logger.info("Функция convert_amount работает успешно")
            return amount * eur_rate
    return 0.0


value = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


# Проверка
convert_amount(value)
