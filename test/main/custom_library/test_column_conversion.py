from unittest import TestCase

from src.main.custom_library import column_conversion


class Test(TestCase):
    def test_str_column_to_float(self):
        expected_dataset = [[1.0, "2.0", "3.0"]]
        dataset = [["1.0", "2.0", "3.0"]]

        column_conversion.str_column_to_float(dataset, column=0)

        self.assertEqual(expected_dataset, dataset)

    def test_str_column_to_int(self):
        expected_dataset = [
            ["1.0", 2],
            ["1.1", 2],
            ["1.2", 1],
            ["1.3", 1],
            ["1.4", 0],
            ["1.5", 0]
        ]
        expected_value_map = {'One': 2, 'Three': 0, 'Two': 1}
        dataset = [
            ["1.0", "One"],
            ["1.1", "One"],
            ["1.2", "Two"],
            ["1.3", "Two"],
            ["1.4", "Three"],
            ["1.5", "Three"]
        ]

        column_value_map = column_conversion.str_column_to_int(dataset, column=1)

        self.assertEqual(expected_dataset, dataset)
        self.assertEqual(column_value_map, expected_value_map)
