from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_column_means(self):
        expected_column_means = [33.333333333333336, 56.666666666666664]
        dataset = [[50, 30], [20, 90], [30, 50]]

        column_means = api.column_means(dataset)

        self.assertEqual(expected_column_means, column_means)
