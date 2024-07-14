import unittest
from typing import Any
from unittest.mock import patch

import pandas as pd

from src.csv_xlsx import read_file_csv, read_file_xlsx


def test_read_file_csv() -> None:
    """Тесты для функции test_file_from_file_csv"""
    file_path = "../data/transactions.csv"
    transactions = read_file_csv(file_path)
    assert isinstance(transactions, list)
    assert all(isinstance(transaction, dict) for transaction in transactions)


@patch("pandas.read_excel")
def test_read_file_xlsx(read_excel: Any) -> None:
    """Тестирование файла transactions_excel.xlsx"""
    read_excel.return_value = pd.DataFrame({"Date": ["2022-01-01", "2022-02-01"], "Amount": [100.00, 200.00]})
    result_xlsx = read_file_xlsx("../data/transactions_excel.xlsx")
    expected_result = [{"Date": "2022-01-01", "Amount": 100.00}, {"Date": "2022-02-01", "Amount": 200.00}]
    unittest.TestCase().assertEqual(result_xlsx, expected_result)
