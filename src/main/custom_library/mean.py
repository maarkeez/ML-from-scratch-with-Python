def column_means(dataset):
    number_of_columns = len(dataset[0])
    number_of_rows = float(len(dataset))
    means = [0 for i in range(number_of_columns)]

    for i in range(number_of_columns):
        col_values = [row[i] for row in dataset]
        means[i] = sum(col_values) / number_of_rows

    return means


def mean_of_list(value_list):
    return sum(value_list) / float(len(value_list))
