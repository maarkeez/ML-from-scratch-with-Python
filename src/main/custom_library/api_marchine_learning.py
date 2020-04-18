import column_conversion
import csv_loader
import evaluation_metrics
import mean
import minmax
import normalize
import split_dataset
import standard_deviations
from src.main.custom_library import random_algorithim


def load_csv(filename):
    return csv_loader.load_csv(filename)


def str_column_to_float(dataset, column):
    column_conversion.str_column_to_float(dataset, column)


def str_column_to_int(dataset, column):
    return column_conversion.str_column_to_int(dataset, column)


def dataset_minmax(dataset):
    return minmax.dataset_minmax(dataset)


def normalize_dataset(dataset, minmax):
    return normalize.normalize_dataset(dataset, minmax)


def column_means(dataset):
    return mean.column_means(dataset)


def column_stdevs(dataset, means):
    return standard_deviations.column_stdevs(dataset, means)


def standardize_dataset(dataset, means, stdevs):
    return standard_deviations.standardize_dataset(dataset, means, stdevs)


def split_with_train_test(dataset, split=0.6):
    return split_dataset.train_test_split(dataset, split)


def split_with_cross_validation(dataset, folds=3):
    return split_dataset.cross_validation_split(dataset, folds)


def evaluate_accuracy(actual, predicted):
    return evaluation_metrics.accuracy(actual, predicted)


def evaluate_confusion_matrix(actual, predicted):
    return evaluation_metrics.confusion_matrix(actual, predicted)


def evaluate_mean_absolute_error(actual, predicted):
    return evaluation_metrics.mean_absolute_error(actual, predicted)


def evaluate_root_mean_squared_error(actual, predicted):
    return evaluation_metrics.root_mean_squared_error(actual, predicted)


def algorithm_random(train, test):
    return random_algorithim.random_algorithm(train, test)
