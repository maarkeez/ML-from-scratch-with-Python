from math import exp


def predict(row, coefficients):
    y = coefficients[0]

    for i in range(len(row) - 1):
        y += coefficients[i + 1] * row[i]

    return 1.0 / (1.0 + exp(-y))


def estimate_coefficients_with_stochastic_gradient_descent(train_set, learning_rate, n_epoch):
    total_instances = len(train_set[0])
    coefficients = [0.0 for _ in range(total_instances)]

    for epoch in range(n_epoch):
        sum_error = 0

        for row in train_set:
            real_value = row[-1]
            predicted_value = predict(row, coefficients)

            error = real_value - predicted_value
            sum_error += error ** 2

            coefficients[0] = coefficients[0] + learning_rate * error * predicted_value * (1.0 - predicted_value)
            for i in range(len(row) - 1):
                coefficients[i + 1] = coefficients[i + 1] + \
                                      learning_rate * error * predicted_value * (1.0 - predicted_value) * row[i]

        print('>epoch=%d, learning_rate=%.3f, error=%.3f' % (epoch, learning_rate, sum_error))

    return coefficients


def logistic_regression(train_set, test_set, learning_rate, n_epoch):
    predictions = list()
    coefficients = estimate_coefficients_with_stochastic_gradient_descent(train_set, learning_rate, n_epoch)

    for row in test_set:
        y = predict(row, coefficients)
        y = round(y)
        predictions.append(y)

    return predictions
