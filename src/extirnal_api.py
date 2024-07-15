from typing import Dict

import requests

from src.logger import logger_setup

logger = logger_setup()


def convert_amount_(operation: Dict) -> float:
    """
    Функция конвертирует сумму транзакции в рубли.
    """
    amount = float(operation["operationAmount"]["amount"])
    currency = operation["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        logger.info("Функция convert_amount выводит всё правильно")
        return amount
    elif currency == "USD" or currency == "EUR":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if currency == "USD":
            usd_rate = float(data["Valute"]["USD"]["Value"])
            logger.info("Функция convert_amount выводит всё правильно")
            return amount * usd_rate
        elif currency == "EUR":
            eur_rate = float(data["Valute"]["EUR"]["Value"])
            logger.info("Функция convert_amount выводит всё правильно")
            return amount * eur_rate
    return 0.0
