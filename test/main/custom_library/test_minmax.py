from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_dataset_minmax(self):
        expected_min_max_matrix = [[1, 4], [2, 5]]
        dataset = [
            [1, 2],
            [1, 2],
            [4, 5],
        ]

        min_max_matrix = api.dataset_minmax(dataset)

        self.assertEqual(expected_min_max_matrix, min_max_matrix)
