def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])

    return minmax


def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            value = row[i]
            min = minmax[i][0]
            max = minmax[i][1]
            row[i] = (value - min) / (max - min)
    return dataset

dataset = [
    [50, 30],
    [20, 90]
]

print "Dataset:"
print dataset
print

minmax = dataset_minmax(dataset)
print "Min, max:"
print minmax
print

print "Normalized dataset:"
print normalize_dataset(dataset, minmax)
