from random import seed
from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_random_algorithm(self):
        # seed: is to ensure the exact same split of the data is made every time the code is executed
        seed(1)
        train = [[0], [1], [0], [1], [0], [1]]
        test = [[None], [None], [None], [None]]

        predictions = api.algorithm_random(train, test)

        self.assertEqual([0, 1, 1, 0], predictions)

    def test_algorithm_classification_zero_rule(self):
        # seed: is to ensure the exact same split of the data is made every time the code is executed
        seed(1)
        train = [[0], [1], [2], [2], [3], [3], [3]]
        test = [[None], [None], [None], [None]]

        predictions = api.algorithm_classification_zero_rule(train, test)

        self.assertEqual([3, 3, 3, 3], predictions)

    def test_algorithm_regression_zero_rule(self):
        # seed: is to ensure the exact same split of the data is made every time the code is executed
        seed(1)
        train = [[10], [15], [12], [15], [18], [20]]
        test = [[None], [None], [None], [None]]

        predictions = api.algorithm_regression_zero_rule(train, test)

        self.assertEqual([15.0, 15.0, 15.0, 15.0], predictions)
