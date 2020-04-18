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
