import os
from unittest import TestCase

from src.main.custom_library import csv_loader


class Test(TestCase):
    def test_load_csv(self):
        csv_path = self.resource_path("simple_dataset.csv")
        expected_dataset = [["1.0", "2.0", "3.0", "4.0"]]
        dataset = csv_loader.load_csv(csv_path)
        self.assertEqual(expected_dataset, dataset)

    def resource_path(self, resource_file_name):
        current_test_path = os.path.split(__file__)[0]
        main_path = self.parent_path(current_test_path)
        test_pkg_path = self.parent_path(main_path)
        resources_path = self.resolve_path(test_pkg_path, "resources")
        return self.resolve_path(resources_path, resource_file_name)

    def parent_path(self, path):
        return os.path.abspath(os.path.join(path, os.pardir))

    def resolve_path(self, parent_path, path):
        return os.path.join(parent_path, path)
