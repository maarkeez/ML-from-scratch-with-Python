from random import seed
from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    def test_with_train_test_split(self):
        # seed: is to ensure the exact same split of the data is made every time the code is executed
        seed(1)

        # Load and prepare data
        pima_dataset = api.load_dataset_pima()
        for row_index in range(len(pima_dataset[0])):
            api.str_column_to_float(pima_dataset, row_index)

        accuracy = api.algorithm_evaluation_with_train_test_split(
            dataset=pima_dataset,
            algorithm=api.algorithm_classification_zero_rule,
            split=0.6)

        accuracy_round = round(accuracy, 3)
        self.assertEqual(69.055, accuracy_round)
