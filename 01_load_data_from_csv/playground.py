from csv import reader

# Load a CSV file
def load_csv(filename):

    dataset = list()
    with open(filename, "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row:
               dataset.append(row)

    print("Loaded data")
    print("\t- File: {0}".format(filename))
    print("\t- Rows: {0}".format(len(dataset)))
    print("\t- Columns: {0}".format(len(dataset[0])))
    return dataset

def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()

    for i, value in enumerate(unique):
        lookup[value] = i

    for row in dataset:
        row[column] = lookup[row[column]]

    return lookup

# Load pima dataset
pima_filename = "../00_datasets/pima-indians-diabetes.data.csv"
pima_dataset = load_csv(pima_filename)
print(pima_dataset[0])

# Convert first column to float
str_column_to_float(pima_dataset, 0)
print(pima_dataset[0])


# Load iris dataset
iris_filename = "../00_datasets/iris.data.csv"
iris_dataset = load_csv(iris_filename)
print(iris_dataset[0])

# Convert 5th column to int
lookup = str_column_to_int(iris_dataset, 4)
print(iris_dataset[0])
# Print keys for that column
print(lookup)

