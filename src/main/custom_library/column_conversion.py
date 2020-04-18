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


def clear_column(matrix, col_index):
    matrix_cleared = list()
    for row in matrix:
        row_copy = list(row)
        row_copy[col_index] = None
        matrix_cleared.append(row_copy)
    return matrix_cleared
