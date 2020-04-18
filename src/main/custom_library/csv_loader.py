import os
from csv import reader


def load_csv(filename):
    dataset = list()
    with open(filename, "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row:
                dataset.append(row)

    print("Loaded data")
    print("\t- File: {0}".format(filename))
    print("\t- Rows: {0}".format(len(dataset)))
    print("\t- Columns: {0}".format(len(dataset[0])))
    print
    return dataset


def load_dataset_pima():
    filename = resource_path("pima-indians-diabetes.data.csv")
    return load_csv(filename)


def load_dataset_iris():
    filename = resource_path("iris.data.csv")
    return load_csv(filename)


def load_dataset_swedish_insurance():
    filename = resource_path("swedish_insurance.csv")
    return load_csv(filename)

def load_dataset_wine_quality():
    filename = resource_path("swedish_insurance.csv")
    return load_csv(filename)

def resource_path(resource_file_name):
    custom_library_path = os.path.split(__file__)[0]
    main_path = parent_path(custom_library_path)
    src_path = parent_path(main_path)
    resources_path = resolve_path(src_path, "resources")
    dataset_path = resolve_path(resources_path, "datasets")
    return resolve_path(dataset_path, resource_file_name)


def parent_path(path):
    return os.path.abspath(os.path.join(path, os.pardir))


def resolve_path(parent_path, path):
    return os.path.join(parent_path, path)
