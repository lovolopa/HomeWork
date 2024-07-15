import csv
from typing import Any

import pandas as pd


def read_file_csv(file_path: str) -> Any:
    poos = []
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            poos.append(row)
    return poos


def read_file_xlsx(file: Any) -> Any:
    """Чтение файла xlsx и возврат списка"""
    data = pd.read_excel(file)
    return data.to_dict("records")


# Проверка
# print(read_file_csv("../data/transactions.csv"))
# print(read_file_xlsx("../data/transactions_excel.xlsx"))
