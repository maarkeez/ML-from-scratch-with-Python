from custom_library import data_loader

dataset = [[50, 30], [20, 90], [30, 50]]
print "Dataset:"
print dataset
print

means = data_loader.column_means(dataset)
print "Means:"
print means
print

stdevs = data_loader.column_stdvevs(dataset, means)
print "Standard Deviation:"
print stdevs
print

print "Standardize dataset:"
print data_loader.standardize_dataset(dataset, means, stdevs)