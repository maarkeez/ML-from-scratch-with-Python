from math import sqrt


def column_stdevs(dataset, means):
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
