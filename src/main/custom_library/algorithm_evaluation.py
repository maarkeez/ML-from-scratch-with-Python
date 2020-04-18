import copy

import evaluation_metrics
import split_dataset
from src.main.custom_library import column_conversion


# Assumptions:
# - Last column of the dataset is the output
# - It's a classification problem "evaluation_metrics.accuracy" is used
def classification_with_train_test_split(data_set, algorithm, split, *args):
    output_value_col_index = -1
    train, test = split_dataset.train_test_split(data_set, split)

    test_set = column_conversion.clear_column(test, output_value_col_index)

    actual = [row[output_value_col_index] for row in test]
    predicted = algorithm(train, test_set, *args)

    accuracy = evaluation_metrics.accuracy(actual, predicted)
    return accuracy


# Assumptions:
# - Last column of the dataset is the output
# - It's a classification problem "evaluation_metrics.accuracy" is used
def classification_with_cross_validation(data_set, algorithm, n_folds, *args):
    output_value_col_index = -1
    folds = split_dataset.cross_validation_split(data_set, n_folds)
    scores = list()

    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])

        test_set = copy.deepcopy(fold)
        test_set = column_conversion.clear_column(test_set, output_value_col_index)

        actual = [row[output_value_col_index] for row in fold]
        predicted = algorithm(train_set, test_set, *args)

        accuracy = evaluation_metrics.accuracy(actual, predicted)
        scores.append(accuracy)

    return scores


def regression_with_simple_linear(data_set, algorithm, split, *args):
    output_value_col_index = -1

    train_set, test_set_raw = split_dataset.train_test_split(data_set, split)
    test_set = column_conversion.clear_column(test_set_raw, output_value_col_index)

    actual = [row[output_value_col_index] for row in test_set_raw]
    predicted = algorithm(data_set, test_set, *args)

    return evaluation_metrics.root_mean_squared_error(actual, predicted)
