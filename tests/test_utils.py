import unittest
from pathlib import Path
from unittest.mock import patch

from src.utils import convert_amount, read_transaction_from_file_json


class TestUtils(unittest.TestCase):
    @patch("json.load")
    def test_load_operations_returns_empty_list_on_invalid_data(self, mock_load: unittest.mock.Mock) -> None:
        mock_load.return_value = {"invalid": "data"}
        operations = read_transaction_from_file_json(Path("data/operations.json"))
        self.assertIsInstance(operations, list)
        self.assertEqual(len(operations), 0)

    @patch("json.load")
    def test_load_operations_returns_empty_list_on_file_not_found(self, mock_load: unittest.mock.Mock) -> None:
        mock_load.side_effect = FileNotFoundError
        operations = read_transaction_from_file_json(Path("data/operations.json"))
        self.assertIsInstance(operations, list)
        self.assertEqual(len(operations), 0)

    @patch("requests.get")
    def test_convert_amount_returns_correct_value_for_usd(self, mock_get: unittest.mock.Mock) -> None:
        mock_response = unittest.mock.MagicMock()
        mock_response.json.return_value = {"Valute": {"USD": {"Value": 75.0}}}
        mock_get.return_value = mock_response

        operation = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
        amount_in_rubles = convert_amount(operation)
        self.assertEqual(amount_in_rubles, 7500.0)


if __name__ == "__main__":
    unittest.main()
