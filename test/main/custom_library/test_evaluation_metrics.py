from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_accuracy(self):
        actual = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        predicted = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1]

        accuracy = api.evaluate_accuracy(actual, predicted)

        self.assertEqual(80.0, accuracy)
