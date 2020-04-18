from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_normalize_dataset(self):
        expected_normalized_dataset = [[1, 0], [0, 1]]
        dataset = [[50, 30], [20, 90]]
        minmax_matrix = [[20, 50], [30, 90]]

        normalized_dataset = api.normalize_dataset(dataset, minmax_matrix)
        self.assertEqual(expected_normalized_dataset, normalized_dataset)
