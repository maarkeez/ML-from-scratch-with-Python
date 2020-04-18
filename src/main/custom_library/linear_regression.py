import mean
import variance


def algorithm_regression_simple_linear(train_set, test_set):
    b0, b1 = estimate_coefficients(train_set)

    predictions = list()
    for row in test_set:
        x = row[0]
        y = b0 + b1 * x
        predictions.append(y)

    return predictions


def estimate_coefficients(data_set):
    x = [row[0] for row in data_set]
    y = [row[1] for row in data_set]

    mean_x = mean.mean_of_list(x)
    mean_y = mean.mean_of_list(y)

    b1 = variance.covariance_of_lists(x, y) / variance.variance_of_list(x)
    b0 = mean_y - b1 * mean_x

    return b0, b1
