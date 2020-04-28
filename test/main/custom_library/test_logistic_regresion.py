from unittest import TestCase

from src.main.custom_library import logistic_regresion


class Test(TestCase):
    data_set = [
        [2.7810836, 2.550537003, 0],
        [1.465489372, 2.362125076, 0],
        [3.396561688, 4.400293529, 0],
        [1.38807019, 1.850220317, 0],
        [3.06407232, 3.005305973, 0],
        [7.627531214, 2.759262235, 1],
        [5.332441248, 2.088626775, 1],
        [6.922596716, 1.77106367, 1],
        [8.675418651, -0.242068655, 1],
        [7.673756466, 3.508563011, 1]
    ]
    coefficients = [-0.406605464, 0.852573316, -1.104746259]

    def test_predict(self):
        self.assertRowPrediction(row_index=0, expected_prediction=0.299)
        self.assertRowPrediction(row_index=1, expected_prediction=0.146)
        self.assertRowPrediction(row_index=2, expected_prediction=0.085)
        self.assertRowPrediction(row_index=3, expected_prediction=0.220)
        self.assertRowPrediction(row_index=4, expected_prediction=0.247)
        self.assertRowPrediction(row_index=5, expected_prediction=0.955)
        self.assertRowPrediction(row_index=6, expected_prediction=0.862)
        self.assertRowPrediction(row_index=7, expected_prediction=0.972)
        self.assertRowPrediction(row_index=8, expected_prediction=0.999)
        self.assertRowPrediction(row_index=9, expected_prediction=0.905)

    def assertRowPrediction(self, row_index, expected_prediction):
        predicted = logistic_regresion.predict(self.data_set[row_index], self.coefficients)
        self.assertEqual(expected_prediction, round(predicted, 3))
