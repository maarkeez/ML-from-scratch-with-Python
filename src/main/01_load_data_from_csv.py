from src.main.custom_library import api_marchine_learning as api

# Load pima dataset
pima_filename = "../resources/datasets/pima-indians-diabetes.data.csv"
pima_dataset = api.load_csv(pima_filename)
print(pima_dataset[0])
print

# Convert first column to float
api.str_column_to_float(pima_dataset, 0)
print(pima_dataset[0])
print

# Load iris dataset
iris_dataset = api.load_dataset_iris()
print(iris_dataset[0])
print

# Convert 5th column to int
lookup = api.str_column_to_int(iris_dataset, 4)
print(iris_dataset[0])
# Print keys for that column
print(lookup)
print
