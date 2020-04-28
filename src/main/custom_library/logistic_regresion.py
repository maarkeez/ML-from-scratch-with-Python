from math import exp


def predict(row, coefficients):
    y = coefficients[0]

    for i in range(len(row) - 1):
        y += coefficients[i + 1] * row[i]

    return 1.0 / (1.0 + exp(-y))
