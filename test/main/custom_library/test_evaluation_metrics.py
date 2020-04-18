from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_accuracy(self):
        actual = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        predicted = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1]

        accuracy = api.evaluate_accuracy(actual, predicted)

        self.assertEqual(80.0, accuracy)

    def test_confusion_matrix(self):
        positive = 0
        negative = 1

        actual = [positive, positive, positive, positive, positive, negative, negative, negative, negative, negative]
        predicted = [positive, negative, negative, positive, positive, negative, positive, negative, negative, negative]

        matrix = api.evaluate_confusion_matrix(actual, predicted)
        matrix.print_matrix()

        self.assertEqual(3, matrix.true_positives)
        self.assertEqual(1, matrix.false_positives)

        self.assertEqual(4, matrix.true_negatives)
        self.assertEqual(2, matrix.false_negatives)

    def test_mae(self):
        actual = [0.1, 0.2, 0.3, 0.4, 0.5]
        predicted = [0.11, 0.19, 0.29, 0.41, 0.5]

        mae = api.evaluate_mean_absolute_error(actual, predicted)
        mae_round = round(mae, 3)

        self.assertEqual(0.008, mae_round)
