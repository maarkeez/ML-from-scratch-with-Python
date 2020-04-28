from random import seed
from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api
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

    def test_estimate_coefficients(self):
        expected_coefficients = [-0.8596443546618897, 1.5223825112460005, -2.218700210565016]

        coefficients = logistic_regresion.estimate_coefficients_with_stochastic_gradient_descent(
            train_set=self.data_set,
            learning_rate=0.3,
            n_epoch=100
        )

        self.assertEqual(expected_coefficients, coefficients)

    def test_logistic_regression(self):
        seed(1)

        pima_data_set = api.load_dataset_pima()

        for i in range(len(pima_data_set[0])):
            api.str_column_to_float(pima_data_set, i)

        min_max = api.dataset_minmax(pima_data_set)
        api.normalize_dataset(pima_data_set, min_max)

        n_folds = 5
        l_rate = 0.1
        n_epoch = 100
        scores = api.algorithm_evaluation_classification_with_cross_validation(
            pima_data_set,
            api.algorithm_regression_logistic,
            n_folds,
            l_rate,
            n_epoch
        )

        expected_scores = [73.20261437908496,
                           75.81699346405229,
                           75.81699346405229,
                           83.66013071895425,
                           78.43137254901961]
        self.assertEqual(expected_scores, scores)

        expected_mean_accuracy = 77.386
        accuracy = round(sum(scores) / float(len(scores)), 3)
        self.assertEqual(expected_mean_accuracy, accuracy)

    def assertRowPrediction(self, row_index, expected_prediction):
        predicted = logistic_regresion.predict(self.data_set[row_index], self.coefficients)
        self.assertEqual(expected_prediction, round(predicted, 3))
