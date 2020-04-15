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
