def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            value = row[i]
            min = minmax[i][0]
            max = minmax[i][1]
            row[i] = (value - min) / (max - min)
    return dataset
