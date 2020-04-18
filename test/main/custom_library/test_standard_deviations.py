import copy
from unittest import TestCase

from src.main.custom_library import api_marchine_learning as api


class Test(TestCase):
    dataset = [[50, 30], [20, 90], [30, 50]]
    means = [33.333333333333336, 56.666666666666664]
    dataset_stdevs = [15.275252316519467, 30.550504633038933]

    def test_column_stdevs(self):
        stdevs = api.column_stdevs(self.dataset, self.means)

        self.assertEqual(self.dataset_stdevs, stdevs)

    def test_standardize_dataset(self):
        expected_standarized_dataset = [
            [1.0910894511799618, -0.8728715609439694],
            [-0.8728715609439697, 1.091089451179962],
            [-0.21821789023599253, -0.2182178902359923]
        ]
        dataset = copy.deepcopy(self.dataset)

        api.standardize_dataset(dataset, self.means, self.dataset_stdevs)

        self.assertEqual(expected_standarized_dataset, dataset)
