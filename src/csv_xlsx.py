from typing import Any

import pandas as pd


def read_file_csv(filename: Any) -> Any:
    """Читает file scv и возвращает список"""
    if filename.endswith(".csv"):
        open_ = pd.read_csv(filename, encoding="utf-8")
        transactions = open_.to_dict(orient="records")
        return transactions
    else:
        return []


def read_file_xlsx(file: Any) -> Any:
    """Чтение файла xlsx и возврат списка"""
    data = pd.read_excel(file)
    return data.to_dict("records")


# Проверка
# print(read_file_csv("../data/transactions.csv"))
# print(read_file_xlsx("../data/transactions_excel.xlsx"))
