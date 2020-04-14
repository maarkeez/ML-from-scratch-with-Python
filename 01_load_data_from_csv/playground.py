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

# Load pima dataset
pima_filename = "datasets/pima-indians-diabetes.data.csv"
pima_dataset = load_csv(pima_filename)