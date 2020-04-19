from random import seed
from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api
from src.main.custom_library import multivariante_linear_regresion


class Test(TestCase):
    def test_predict(self):
        data_set = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
        coefficients = [0.4, 0.8]

        self.assertEqual(1.200, self.predict(data_set[0], coefficients))
        self.assertEqual(2.000, self.predict(data_set[1], coefficients))
        self.assertEqual(3.600, self.predict(data_set[2], coefficients))
        self.assertEqual(2.800, self.predict(data_set[3], coefficients))
        self.assertEqual(4.400, self.predict(data_set[4], coefficients))

    def test_estimate_coefficients_with_sgc(self):
        data_set = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]

        coefficients = multivariante_linear_regresion.estimate_coefficients_with_stochastic_gradient_descent(
            train_set=data_set,
            learning_rate=0.001,
            n_epoch=50
        )

        self.assertEqual([0.22998234937311363, 0.8017220304137576], coefficients)

    def test_multivariate_linear_regression_with_wine_dataset(self):
        seed(1)

        expected_scores = [
            0.0951642037233398,
            0.23186702624691477,
            0.1071129787936352,
            0.09957917995830148,
            0.1086209334617076
        ]

        wine_data_set = api.load_dataset_wine_quality()

        for i in range(len(wine_data_set[0])):
            api.str_column_to_float(dataset=wine_data_set, column=i)

        min_max = api.dataset_minmax(wine_data_set)
        api.normalize_dataset(wine_data_set, min_max)

        n_folds = 5
        learning_rate = 0.01
        n_epoch = 50

        scores = api.algorithm_evaluation_regression_with_cross_validation(
            wine_data_set,
            api.algorithm_regression_linear_stochastic_gradient_descent,
            n_folds,
            learning_rate,
            n_epoch
        )
        mean_rmse = (sum(scores) / float(len(scores)))
        mean_rmse = round(mean_rmse, 3)

        # With: folds = 5, learning_rate=0.003, epoch=100000 =>  Mean RMSE=0.087
        self.assertEqual(expected_scores, scores)
        self.assertEqual(0.128, mean_rmse)

    def predict(self, row, coef):
        return round(multivariante_linear_regresion.predict(row, coef), 3)
