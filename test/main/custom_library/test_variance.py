from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_variance_of_list(self):
        data_list = [1, 2, 4, 3, 5]
        expected_variance = 10.000

        actual_variance = api.variance_of_list(data_list)

        self.assertEqual(expected_variance, actual_variance)

    def test_covariance_of_lists(self):
        data_set = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
        x = [row[0] for row in data_set]
        y = [row[1] for row in data_set]

        covariance = api.covariance_of_lists(x, y)

        self.assertEqual(8.0, covariance)
