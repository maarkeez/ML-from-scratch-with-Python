from src.main.custom_library import api_marchine_learning as api

dataset = [[50, 30], [20, 90], [30, 50]]
print "Dataset:"
print dataset
print

means = api.column_means(dataset)
print "Means:"
print means
print

stdevs = api.column_stdevs(dataset, means)
print "Standard Deviation:"
print stdevs
print

print "Standardize dataset:"
print api.standardize_dataset(dataset, means, stdevs)
