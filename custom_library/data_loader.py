from csv import reader
from math import sqrt


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


def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()

    for i, value in enumerate(unique):
        lookup[value] = i

    for row in dataset:
        row[column] = lookup[row[column]]

    return lookup


def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])

    return minmax


def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            value = row[i]
            min = minmax[i][0]
            max = minmax[i][1]
            row[i] = (value - min) / (max - min)
    return dataset


def column_means(dataset):
    number_of_columns = len(dataset[0])
    number_of_rows = float(len(dataset))
    means = [0 for i in range(number_of_columns)]

    for i in range(number_of_columns):
        col_values = [row[i] for row in dataset]
        means[i] = sum(col_values) / number_of_rows

    return means


def column_stdvevs(dataset, means):
    number_of_columns = len(dataset[0])
    number_of_rows_minus_one = float(len(dataset) - 1)
    stdevs = [0 for i in range(number_of_columns)]

    for i in range(number_of_columns):
        varianze = [pow(row[i] - means[i], 2) for row in dataset]
        stdevs[i] = sum(varianze)

    stdevs = [sqrt(x / number_of_rows_minus_one) for x in stdevs]
    return stdevs


def standardize_dataset(dataset, means, stdevs):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - means[i]) / stdevs[i]

    return dataset
