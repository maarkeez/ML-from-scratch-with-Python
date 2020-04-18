def accuracy(actual, predicted):
    total_instances = len(actual)
    correct = 0

    for i in range(total_instances):
        if actual[i] == predicted[i]:
            correct += 1

    return correct / float(total_instances) * 100
