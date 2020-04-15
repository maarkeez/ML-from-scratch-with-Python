from custom_library import data_loader

dataset = [
    [50, 30],
    [20, 90]
]

print "Dataset:"
print dataset
print

minmax = data_loader.dataset_minmax(dataset)
print "Min, max:"
print minmax
print

print "Normalized dataset:"
print data_loader.normalize_dataset(dataset, minmax)
print

pima_filename = "datasets/pima-indians-diabetes.data.csv"
pima_dataset = data_loader.load_csv(pima_filename)
# Convert string columns to float
for i in range(len(pima_dataset[0])):
    data_loader.str_column_to_float(pima_dataset, i)
pima_minmax = data_loader.dataset_minmax(pima_dataset)
pima_dataset = data_loader.normalize_dataset(pima_dataset, pima_minmax)

print "Normalized pima (first row):"
print pima_dataset[0]
print