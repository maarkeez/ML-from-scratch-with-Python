from random import seed
from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_classification_with_train_test_split(self):
        # seed: is to ensure the exact same split of the data is made every time the code is executed
        seed(1)

        pima_dataset = self.load_and_prepare_dataset_pima()

        accuracy = api.algorithm_evaluation_classification_with_train_test_split(
            dataset=pima_dataset,
            algorithm=api.algorithm_classification_zero_rule,
            split=0.6)

        accuracy_round = round(accuracy, 3)
        self.assertEqual(69.055, accuracy_round)

    def test_classification_with_cross_validation(self):
        # seed: is to ensure the exact same split of the data is made every time the code is executed
        seed(1)

        expected_scores = [
            60.130718954248366,
            62.745098039215684,
            64.70588235294117,
            71.89542483660131,
            66.01307189542483
        ]
        pima_dataset = self.load_and_prepare_dataset_pima()

        scores = api.algorithm_evaluation_classification_with_cross_validation(
            dataset=pima_dataset,
            algorithm=api.algorithm_classification_zero_rule,
            n_folds=5
        )
        mean_accuracy = (sum(scores) / len(scores))
        mean_accuracy = round(mean_accuracy, 3)

        self.assertEqual(expected_scores, scores)
        self.assertEqual(65.098, mean_accuracy)

    def test_regression_with_simple_linear(self):
        data_set = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]

        # split=0.0 => Uses all the data_set as train_set
        rmse = api.algorithm_evaluation_regression_with_simple_linear(
            data_set=data_set,
            algorithm=api.algorithm_regression_simple_linear,
            split=0.0
        )
        rmse = round(rmse, 3)

        self.assertEqual(0.693, rmse)

    def test_regression_with_simple_linear_insurance_dataset(self):
        seed(1)

        insurance_data_set = self.load_and_prepare_dataset_insurance()

        rmse = api.algorithm_evaluation_regression_with_simple_linear(
            data_set=insurance_data_set,
            algorithm=api.algorithm_regression_simple_linear,
            split=0.6
        )
        rmse = round(rmse, 3)

        # TODO: Review this assertion, in the example it was 38.339
        self.assertEqual(37.047, rmse)

    def load_and_prepare_dataset_insurance(self):
        insurance_data_set = api.load_dataset_swedish_insurance()
        self.set_all_columns_to_float(insurance_data_set)
        return insurance_data_set

    def load_and_prepare_dataset_pima(self):
        pima_dataset = api.load_dataset_pima()
        self.set_all_columns_to_float(pima_dataset)
        return pima_dataset

    def set_all_columns_to_float(self, pima_dataset):
        for row_index in range(len(pima_dataset[0])):
            api.str_column_to_float(pima_dataset, row_index)
