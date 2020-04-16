from unittest import TestCase

from src.main.custom_library import csv_loader


class Test(TestCase):
    def test_load_csv(self):
        expected_dataset = [["1.0", "2.0", "3.0", "4.0"]]
        dataset = csv_loader.load_csv("./resources/simple_dataset.csv")
        self.assertEqual(expected_dataset, dataset)
