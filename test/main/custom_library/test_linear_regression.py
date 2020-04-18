from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_estimate_coefficients(self):
        data_set = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]

        b0, b1 = api.estimate_coefficients(data_set)
        b0 = round(b0, 3)
        b1 = round(b1, 3)

        self.assertEqual(0.400, b0)
        self.assertEqual(0.800, b1)
