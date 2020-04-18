from random import randrange


# The prediction output it's a random value from the train values
def random_algorithm(train, test):
    output_values = [row[-1] for row in train]

    possible_predictions = list(set(output_values))
    predicted = list()
    for _ in test:
        index = randrange(len(possible_predictions))
        predicted.append(possible_predictions[index])

    return predicted


# The prediction output is the most common value in the train dataset
def algorithm_classification_zero_rule(train, test):
    output_values = [row[-1] for row in train]

    prediction = max(set(output_values), key=output_values.count)
    predicted = [prediction for _ in range(len(test))]

    return predicted

# The prediction output is the mean of the train dataset
def algorithm_regression_zero_rule(train, test):
    output_values = [row[-1] for row in train]

    prediction = sum(output_values) / float(len(output_values))
    predicted = [prediction for _ in range(len(test))]

    return predicted
