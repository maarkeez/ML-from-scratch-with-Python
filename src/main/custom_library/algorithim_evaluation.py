import evaluation_metrics
import split_dataset
from src.main.custom_library import column_conversion


# Assumptions:
# - Last column of the dataset is the output
# - It's a classification problem "evaluation_metrics.accuracy" is used
def with_train_test_split(dataset, algorithm, split, *args):
    output_value_col_index = -1
    train, test = split_dataset.train_test_split(dataset, split)

    test_set = column_conversion.clear_column(test, output_value_col_index)

    actual = [row[output_value_col_index] for row in test]
    predicted = algorithm(train, test_set, *args)

    accuracy = evaluation_metrics.accuracy(actual, predicted)
    return accuracy
