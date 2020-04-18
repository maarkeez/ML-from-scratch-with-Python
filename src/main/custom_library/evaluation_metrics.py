from math import sqrt


def accuracy(actual, predicted):
    total_instances = len(actual)
    correct = 0

    for i in range(total_instances):
        if actual[i] == predicted[i]:
            correct += 1

    return correct / float(total_instances) * 100


def confusion_matrix(actual, predicted):
    positive = 0
    negative = 1

    total_instances = len(actual)
    matrix = ConfusionMatrix()

    # Fill confusion matrix
    for i in range(total_instances):
        actual_value = actual[i]
        predicted_value = predicted[i]

        if positive == actual_value and positive == predicted_value:
            matrix.increment_tp()
        elif negative == actual_value and negative == predicted_value:
            matrix.increment_tn()
        elif negative == actual_value and positive == predicted_value:
            matrix.increment_fp()
        elif positive == actual_value and negative == predicted_value:
            matrix.increment_fn()

    return matrix


class ConfusionMatrix:
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0

    def __init__(self):
        pass

    def increment_tp(self):
        self.true_positives += 1

    def increment_fp(self):
        self.false_positives += 1

    def increment_tn(self):
        self.true_negatives += 1

    def increment_fn(self):
        self.false_negatives += 1

    def print_matrix(self):
        print "                            ACTUAL        "
        print "                   |  Positive | Negative "
        print "          Positive |     {}         {}    ".format(self.true_positives, self.false_positives)
        print "PREDICTED            "
        print "          Negative |     {}         {}    ".format(self.false_negatives, self.true_negatives)


def mean_absolute_error(actual, predicted):
    sum_error = 0.0
    total_instances = len(actual)

    for i in range(total_instances):
        sum_error += abs(predicted[i] - actual[i])

    return sum_error / float(total_instances)


def root_mean_squared_error(actual, predicted):
    sum_error = 0.0
    total_instances = len(actual)

    for i in range(total_instances):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)

    mean_error = sum_error / float(total_instances)

    return sqrt(mean_error)
