from unittest import TestCase

from src.main.custom_library import normalize


class Test(TestCase):
    def test_normalize_dataset(self):
        expected_normalized_dataset = [[1, 0], [0, 1]]
        dataset = [[50, 30], [20, 90]]
        minmax_matrix = [[20, 50], [30, 90]]

        normalized_dataset = normalize.normalize_dataset(dataset, minmax_matrix)
        self.assertEqual(expected_normalized_dataset, normalized_dataset)
