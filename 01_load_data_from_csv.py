from custom_library import data_loader

# Load pima dataset
pima_filename = "datasets/pima-indians-diabetes.data.csv"
pima_dataset = data_loader.load_csv(pima_filename)
print(pima_dataset[0])
print

# Convert first column to float
data_loader.str_column_to_float(pima_dataset, 0)
print(pima_dataset[0])
print

# Load iris dataset
iris_filename = "datasets/iris.data.csv"
iris_dataset = data_loader.load_csv(iris_filename)
print(iris_dataset[0])
print

# Convert 5th column to int
lookup = data_loader.str_column_to_int(iris_dataset, 4)
print(iris_dataset[0])
# Print keys for that column
print(lookup)
print

