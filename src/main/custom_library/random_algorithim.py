# The prediction output it's a random value from the train values
from random import randrange


def random_algorithm(train, test):
    output_values = [row[-1] for row in train]

    possible_predictions = list(set(output_values))
    predicted = list()
    for _ in test:
        index = randrange(len(possible_predictions))
        predicted.append(possible_predictions[index])

    return predicted
