from src.main.custom_library import api_marchine_learning as api

dataset = [
    [50, 30],
    [20, 90]
]

print "Dataset:"
print dataset
print

minmax = api.dataset_minmax(dataset)
print "Min, max:"
print minmax
print

print "Normalized dataset:"
print api.normalize_dataset(dataset, minmax)
print

pima_filename = "../resources/datasets/pima-indians-diabetes.data.csv"
pima_dataset = api.load_csv(pima_filename)
# Convert string columns to float
for i in range(len(pima_dataset[0])):
    api.str_column_to_float(pima_dataset, i)
pima_minmax = api.dataset_minmax(pima_dataset)
pima_dataset = api.normalize_dataset(pima_dataset, pima_minmax)

print "Normalized pima (first row):"
print pima_dataset[0]
print
